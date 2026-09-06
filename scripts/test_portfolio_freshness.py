"""Offline verification of portfolio_freshness.py logic — no network, no writes.

Runs as a CI gate before the real audit. Proves the three properties that
matter most: private repositories never reach the report, an API failure is
rendered as N/A rather than 0, and untrusted repository metadata cannot break
the markdown table or fire an @mention.
"""
import os
import sys

os.environ["CONTROL_REPO"] = ""
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import portfolio_freshness as F  # noqa: E402

REPOS = [
    {"name": "alpha", "html_url": "https://x/alpha", "private": False, "archived": False,
     "fork": False, "license": {"spdx_id": "MIT"}, "description": "iyi repo",
     "topics": ["a", "b"], "pushed_at": "2026-09-01T00:00:00Z",
     "homepage": "https://alpha.example"},
    {"name": "beta", "html_url": "https://x/beta", "private": False, "archived": False,
     "fork": False, "license": None, "description": None, "topics": [],
     "pushed_at": "2024-01-01T00:00:00Z", "homepage": ""},
    {"name": "evil|pipe", "html_url": "https://x/evil", "private": False, "archived": True,
     "fork": False, "license": {"spdx_id": "NOASSERTION"},
     "description": "pipe | and @umutseve4 and #1 and <script>", "topics": ["z"],
     "pushed_at": None, "homepage": "http://insecure.example"},
    {"name": "secret", "html_url": "https://x/secret", "private": True, "archived": False,
     "fork": False, "license": {"spdx_id": "MIT"}, "description": "GIZLI",
     "topics": [], "pushed_at": "2026-09-01T00:00:00Z", "homepage": ""},
]


def fake_paginated(path, cap_pages=10):
    if "/users/" in path:
        return REPOS, None
    if "beta/pulls" in path:
        return [], "HTTP 403"          # error path -> must render N/A, not 0
    if "alpha/pulls" in path:
        return [{"n": 1}, {"n": 2}], None
    return [], None


F.api_paginated = fake_paginated
F._request = lambda *a, **k: (200, {}, {})   # probe -> "canlı (200)"

rows = F.collect()
body = F.render(rows, "2026-08-30 03:17 UTC")

fails = []
if any(r["name"] == "secret" for r in rows):
    fails.append("private repo rapora sızdı")
if "GIZLI" in body:
    fails.append("private açıklama gövdede")
if len(rows) != 3:
    fails.append(f"repo sayısı {len(rows)} != 3")
beta = [r for r in rows if r["name"] == "beta"][0]
if beta["open_prs"] != "N/A":
    fails.append("hata durumu 0 olarak raporlandı")
if "| 2 |" not in body:
    fails.append("açık PR sayısı görünmüyor")
if "@\u200b" not in body:
    fails.append("mention nötrleştirilmedi")
if "\\|" not in body:
    fails.append("pipe kaçırılmadı")
if "&lt;script&gt;" not in body:
    fails.append("html kaçırılmadı")
if "N/A (homepage boş)" not in body:
    fails.append("boş homepage yanlış")
if F.MARKER not in body:
    fails.append("marker yok")
if "atlandı (https değil)" not in body:
    fails.append("http probe atlanmadı")
if "Önceki rapor" not in body:
    fails.append("önceki damga yok")
if "lisans" not in body:
    fails.append("lisans bayrağı yok")
if F.prev_stamp(body) is None:
    fails.append("generated damgası okunamıyor")
if len(body) > F.MAX_BODY:
    fails.append("gövde sınırı aşıldı")

print(body)
print("\n================ TEST ================")
print("FAIL: " + "; ".join(fails) if fails else "PASS — 14/14 kontrol geçti")
sys.exit(1 if fails else 0)
