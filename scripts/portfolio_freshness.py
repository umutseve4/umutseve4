#!/usr/bin/env python3
"""Portfolio freshness monitor — read-only audit of PUBLIC repositories.

Scope decision (deliberate, do not widen without a security review):
  * Repositories are listed via GET /users/{owner}/repos, which NEVER returns
    private repositories. Private data is therefore excluded by construction,
    not by a downstream filter. This is why no PAT is required.
  * The only write performed is updating a single tracking issue in the control
    repository, using that repository's own GITHUB_TOKEN (issues: write).

Failure policy: a value that could not be determined is reported as "N/A" or an
explicit error marker. It is NEVER reported as 0 / "ok".
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

API = "https://api.github.com"
API_VERSION = "2022-11-28"
UA = "umutseve4-portfolio-freshness/1.0"

OWNER = os.environ.get("TARGET_OWNER", "umutseve4")
CONTROL_REPO = os.environ.get("CONTROL_REPO", "")  # "owner/repo"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
ISSUE_LABEL = os.environ.get("ISSUE_LABEL", "portfolio-freshness")
ISSUE_TITLE = os.environ.get("ISSUE_TITLE", "Portföy tazelik raporu (otomatik)")
MARKER = "<!-- portfolio-freshness-report:v1 -->"
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"

STALE_DAYS = int(os.environ.get("STALE_DAYS", "180"))
MAX_BODY = 60000  # GitHub hard limit is 65536; keep headroom.

errors: list[str] = []


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #
def _request(url: str, method: str = "GET", data: dict | None = None,
             timeout: int = 20, auth: bool = True):
    """Return (status, headers, parsed_body_or_text). Never raises on HTTP error."""
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", API_VERSION)
    req.add_header("User-Agent", UA)
    if body is not None:
        req.add_header("Content-Type", "application/json")
    if auth and TOKEN:
        req.add_header("Authorization", "Bearer " + TOKEN)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            try:
                return r.status, dict(r.headers), json.loads(raw)
            except json.JSONDecodeError:
                return r.status, dict(r.headers), raw.decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, dict(e.headers), json.loads(raw)
        except Exception:
            return e.code, dict(e.headers), raw.decode("utf-8", "replace")
    except Exception as e:  # timeout, DNS, TLS, reset
        return 0, {}, f"{type(e).__name__}: {e}"


def api_paginated(path: str, cap_pages: int = 10) -> tuple[list, str | None]:
    """Follow rel=next. Returns (items, error). Partial results are an error."""
    items: list = []
    url = f"{API}{path}"
    sep = "&" if "?" in path else "?"
    url = f"{url}{sep}per_page=100"
    for _ in range(cap_pages):
        status, headers, body = _request(url)
        if status != 200 or not isinstance(body, list):
            return items, f"HTTP {status}"
        items.extend(body)
        nxt = None
        for part in headers.get("Link", "").split(","):
            if 'rel="next"' in part:
                nxt = part[part.find("<") + 1:part.find(">")]
        if not nxt:
            return items, None
        url = nxt
        time.sleep(0.1)
    return items, "pagination cap reached"


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def sanitize(text: str | None, limit: int = 90) -> str:
    """Repository metadata is untrusted input: neutralise table/markdown breakage
    and accidental @mentions before it lands in an issue body."""
    if not text:
        return "—"
    t = " ".join(str(text).split())
    t = t.replace("|", "\\|").replace("`", "'").replace("<", "&lt;").replace(">", "&gt;")
    t = t.replace("@", "@\u200b").replace("#", "#\u200b")
    if len(t) > limit:
        t = t[: limit - 1] + "…"
    return t


def age_days(iso: str | None) -> int | None:
    if not iso:
        return None
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return None
    return (datetime.now(timezone.utc) - dt).days


def probe(url: str) -> str:
    """Best-effort liveness probe. Response bodies are never stored."""
    if not url:
        return "N/A"
    if not url.startswith("https://"):
        return "atlandı (https değil)"
    status, headers, _ = _request(url, timeout=12, auth=False)
    if status == 0:
        return "erişilemedi"
    if status in (301, 302, 307, 308):
        return f"{status} yönlendirme"
    if status == 200:
        return "canlı (200)"
    return f"HTTP {status}"


# --------------------------------------------------------------------------- #
# Collection
# --------------------------------------------------------------------------- #
def collect() -> list[dict]:
    repos, err = api_paginated(f"/users/{OWNER}/repos?type=owner&sort=full_name")
    if err:
        errors.append(f"repo listesi eksik olabilir: {err}")
    if not repos:
        print("FATAL: repo listesi boş", file=sys.stderr)
        sys.exit(1)

    rows = []
    for r in repos:
        if r.get("private"):  # defence in depth; this endpoint cannot return them
            continue
        name = r["name"]
        row = {
            "name": name,
            "url": r["html_url"],
            "archived": bool(r.get("archived")),
            "fork": bool(r.get("fork")),
            "license": (r.get("license") or {}).get("spdx_id") or "YOK",
            "description": r.get("description"),
            "topics": len(r.get("topics") or []),
            "pushed_days": age_days(r.get("pushed_at")),
            "homepage": (r.get("homepage") or "").strip(),
        }

        prs, perr = api_paginated(f"/repos/{OWNER}/{name}/pulls?state=open")
        row["open_prs"] = "N/A" if perr else len(prs)
        if perr:
            errors.append(f"{name}: açık PR sayılamadı ({perr})")

        row["site"] = probe(row["homepage"]) if row["homepage"] else "N/A (homepage boş)"
        rows.append(row)
        time.sleep(0.05)
    return rows


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #
def flags(row: dict) -> list[str]:
    f = []
    if row["license"] in ("YOK", "NOASSERTION"):
        f.append("lisans")
    if not row["description"]:
        f.append("açıklama")
    if row["topics"] == 0:
        f.append("topic")
    d = row["pushed_days"]
    if d is not None and d > STALE_DAYS and not row["archived"]:
        f.append(f"{d}g sessiz")
    if isinstance(row["open_prs"], int) and row["open_prs"] > 0:
        f.append(f"{row['open_prs']} açık PR")
    if row["site"].startswith(("HTTP", "erişilemedi")):
        f.append("site")
    return f


def render(rows: list[dict], prev_generated: str | None) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    needs = [r for r in rows if flags(r)]
    no_lic = sum(1 for r in rows if r["license"] in ("YOK", "NOASSERTION"))
    no_top = sum(1 for r in rows if r["topics"] == 0)
    no_desc = sum(1 for r in rows if not r["description"])

    out = [
        MARKER,
        f"<!-- generated: {now} -->",
        "",
        f"# Portföy tazelik raporu — {now}",
        "",
        "> Bu **izleme** raporudur, otomatik onarım yapmaz. Kapsam: "
        f"`{OWNER}` hesabının **public** repoları. Private repolar hiç okunmaz "
        "(`GET /users/{owner}/repos` private döndürmez), bu yüzden PAT gerekmez.",
        "",
        "## Özet",
        "",
        "| public repo | lisanssız | topic'siz | açıklamasız | dikkat isteyen |",
        "|---|---|---|---|---|",
        f"| {len(rows)} | {no_lic} | {no_top} | {no_desc} | {len(needs)} |",
        "",
    ]

    if prev_generated:
        out += [f"Önceki rapor: `{prev_generated}` — döngü canlı mı buradan görülür.", ""]

    out += ["## Dikkat isteyenler", ""]
    if needs:
        out += ["| repo | bulgular |", "|---|---|"]
        for r in sorted(needs, key=lambda x: len(flags(x)), reverse=True):
            out.append(f"| [{sanitize(r['name'], 60)}]({r['url']}) | {', '.join(flags(r))} |")
    else:
        out.append("Yok — tüm public repolar temel hijyen kriterlerini geçiyor.")

    out += ["", "## Tam envanter", "",
            "| repo | lisans | topic | açıklama | son push | açık PR | site |",
            "|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda x: x["name"].lower()):
        d = r["pushed_days"]
        push = "N/A" if d is None else f"{d} gün"
        out.append(
            f"| [{sanitize(r['name'], 60)}]({r['url']}){' `arşiv`' if r['archived'] else ''} "
            f"| {r['license']} | {r['topics']} | {sanitize(r['description'])} "
            f"| {push} | {r['open_prs']} | {r['site']} |"
        )

    out += ["", "## Koşu bütünlüğü", ""]
    if errors:
        out.append("Bu koşuda **eksik veri var**; aşağıdaki değerler `N/A`, `0` değil:")
        out += [f"- {sanitize(e, 200)}" for e in errors[:25]]
    else:
        out.append("Tüm sorgular başarılı; raporda tahmin edilmiş değer yok.")

    out += [
        "",
        "---",
        "*Otomatik üretildi. Public repoda **60 gün** hiç etkinlik olmazsa GitHub "
        "zamanlanmış workflow'ları devre dışı bırakır — yukarıdaki üretim tarihi "
        "bayatlarsa döngü ölmüş demektir.*",
    ]

    body = "\n".join(out)
    if len(body) > MAX_BODY:
        body = body[: MAX_BODY - 200] + "\n\n… *(rapor karakter sınırı nedeniyle kısaltıldı)*"
    return body


# --------------------------------------------------------------------------- #
# Single-issue upsert (idempotent, marker-based)
# --------------------------------------------------------------------------- #
def prev_stamp(body: str | None) -> str | None:
    if not body:
        return None
    for line in body.splitlines():
        if line.startswith("<!-- generated:"):
            return line.replace("<!-- generated:", "").replace("-->", "").strip()
    return None


def upsert(rows: list[dict]) -> None:
    if not CONTROL_REPO:
        print(render(rows, None))
        return
    status, _, found = _request(
        f"{API}/repos/{CONTROL_REPO}/issues?state=all&labels={ISSUE_LABEL}&per_page=20"
    )
    target = None
    if status == 200 and isinstance(found, list):
        for it in found:
            if "pull_request" in it:
                continue
            if MARKER in (it.get("body") or ""):
                target = it
                break
    else:
        errors.append(f"mevcut issue aranamadı (HTTP {status}) — yenisi açılabilir")

    body = render(rows, prev_stamp(target.get("body") if target else None))

    if DRY_RUN:
        print(body)
        print(f"\n--- DRY_RUN: yazma yapılmadı (hedef issue: "
              f"{target['number'] if target else 'yeni'}) ---", file=sys.stderr)
        return

    if target:
        st, _, res = _request(
            f"{API}/repos/{CONTROL_REPO}/issues/{target['number']}",
            method="PATCH", data={"body": body, "state": "open"})
        action = f"güncellendi #{target['number']}"
    else:
        st, _, res = _request(
            f"{API}/repos/{CONTROL_REPO}/issues", method="POST",
            data={"title": ISSUE_TITLE, "body": body, "labels": [ISSUE_LABEL]})
        action = f"oluşturuldu #{res.get('number') if isinstance(res, dict) else '?'}"
    if st not in (200, 201):
        print(f"FATAL: issue yazılamadı HTTP {st}: {res}", file=sys.stderr)
        sys.exit(1)
    print(f"Issue {action}: {res.get('html_url') if isinstance(res, dict) else ''}")


def main() -> None:
    rows = collect()
    print(f"{len(rows)} public repo tarandı, {len(errors)} eksik veri.")
    upsert(rows)
    if errors:
        print("::warning::Koşu kısmi: bazı değerler N/A olarak raporlandı.")


if __name__ == "__main__":
    main()
