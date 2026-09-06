<!-- ────────────────────────────  00 / OPENING TITLE  ──────────────────────────── -->
<div align="center">

<img width="100%" src="https://umutseve4.github.io/cover/zift-banner.svg" alt="ZİFT — Umut Sever · evidence over adjectives" />

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=22&duration=2600&pause=700&color=FF4D4F&center=true&vCenter=true&width=1000&lines=Build.+Measure.+Verify.;Econometrics+%28Ekonometri%29+%40+Uluda%C4%9F+University;Python+%C2%B7+SQL+%C2%B7+dbt+%C2%B7+DuckDB+%C2%B7+FastAPI+%C2%B7+CI%2FCD;Evidence+pages+instead+of+screenshots;And+raw+WebGL2+%2B+hand-written+GLSL+for+the+soul" alt="Build. Measure. Verify." />

<br/>

<a href="https://umutseve4.github.io"><img src="https://img.shields.io/badge/PORTFOLIO-0B0B0B?style=for-the-badge&logo=githubpages&logoColor=FF4D4F" alt="Portfolio" /></a>
<a href="https://www.linkedin.com/in/umut-sever-7851b73a6/"><img src="https://img.shields.io/badge/LINKEDIN-0B0B0B?style=for-the-badge&logo=linkedin&logoColor=FF4D4F" alt="LinkedIn" /></a>
<a href="https://x.com/umutseve4"><img src="https://img.shields.io/badge/X-0B0B0B?style=for-the-badge&logo=x&logoColor=FF4D4F" alt="X" /></a>
<img src="https://komarev.com/ghpvc/?username=umutseve4&label=VIEWS&color=FF4D4F&style=for-the-badge" alt="profile views" />

</div>

<!-- ────────────────────────────  01 / STATEMENT  ──────────────────────────── -->
<div align="center">

`01 / STATEMENT`

### **Claims are not proof.**

</div>

I'm an incoming first-year **Econometrics (Ekonometri)** student at **Bursa Uludağ University** — classes begin **28 September 2026** — building toward **data engineering**: pipelines, contracts, run ledgers, and evidence pages that anyone can open and audit.

My rule is narrow and unforgiving: a project counts only when it has **a public artifact, a green pipeline, and an honest limitations section**. Where a claim can't be verified, the page says so out loud — including missing scheduled days and synthetic-fixture modes.

The other half of my brain writes renderers from scratch: **raw WebGL2 with hand-written GLSL**, zero runtime dependencies, plus a UE5 racing sim. Data pipeline or fragment shader — no black boxes either way.

```python
class UmutSever:
    school     = "Econometrics (Ekonometri) @ Bursa Uludağ University"
    alumni     = "Tofaş Science High School"
    location   = "Bursa, Türkiye"
    target     = "AI & Data Engineering — verified milestone by milestone"

    building   = ["econ-lakehouse", "pulsegrid", "ekodiff", "cosmic-econometric-observatory"]
    learning   = ["PostgreSQL at depth", "Docker", "AWS DEA-C01", "time series"]
    edge       = "Zero-dependency WebGL2 / GLSL · UE5 · Blender"

    philosophy = "Tested > claimed. Deployed > demoed. Evidence > adjectives."
```

<br/>

<!-- ────────────────────────────  02 / LIVE SURFACES  ──────────────────────────── -->
<div align="center">

`02 / LIVE SURFACES`

### **Open them. They run in your browser.**

Every link below was reachable at the time of writing — no screenshots, no promises.

</div>

| Experience | What it is | Live |
|---|---|---|
| **SEVER/05 — Portfolio** | Editorial case-study site: ownership, key decision, and the line between *tested* and *deployed* | [umutseve4.github.io](https://umutseve4.github.io) |
| **PulseGrid 3D** | A cinematic data-reliability city in Three.js — failure → quarantine → replay → recovery, with a full accessible table equivalent when WebGL is unavailable | [open](https://umutseve4.github.io/pulsegrid-3d/) |
| **Kozmik Ekonometri Rasathanesi** | 144 real course records, 147 nodes / 146 edges, every row carrying source id, line position and SHA-256 digest | [open](https://umutseve4.github.io/cosmic-econometric-observatory/) |
| **Tercih Atlası 2026** | Explainable decision surface for 20 career fields — score = `0.30F + 0.25G + 0.20I + 0.15X + 0.10E`, stated as an editorial model, not advice | [open](https://umutseve4.github.io/tercih-atlasi/) |
| **Çanakkale 1915** | Single-file Three.js cinematic scene — a commemorative sequence, not a game; motion respects `prefers-reduced-motion` | [open](https://umutseve4.github.io/canakkale-1915-webgl/) |
| **EkoDiff — Akademik Zaman Makinesi** | Curriculum version diffs and a local-first what-if engine; nothing about a student leaves the browser | [open](https://umutseve4.github.io/ekodiff/) |
| **econ-lakehouse — run evidence** | Static page rendered from an append-only Parquet run ledger; missing days are *shown*, not hidden | [open](https://umutseve4.github.io/econ-lakehouse/) |

<br/>

<!-- ────────────────────────────  03 / SELECTED SYSTEMS  ──────────────────────────── -->
<div align="center">

`03 / SELECTED SYSTEMS`

### **Work with receipts.**

</div>

<table>
<tr>
<td width="50%" valign="top">

#### ▸ econ-lakehouse
**Medallion lakehouse for Turkish macro data**

- Python ingest → **Parquet bronze** → **dbt + DuckDB** silver/gold
- Data-quality gates between every layer
- Scheduled via GitHub Actions, each execution appended to a **Parquet audit ledger**
- Evidence page states its own scope: runs use a committed **synthetic fixture** — it proves orchestration, not upstream data freshness

`Python` `dbt` `DuckDB` `Parquet` `Actions`

[→ Repo](https://github.com/umutseve4/econ-lakehouse) · [→ Evidence](https://umutseve4.github.io/econ-lakehouse/)

</td>
<td width="50%" valign="top">

#### ▸ enflasyonum
**Personal inflation index vs official TÜİK CPI**

- **FastAPI + PostgreSQL** pipeline, deployed on Render
- **Laspeyres index across 13 ECOICOP sub-indices** — explainable and CPI-comparable
- Autonomous daily ingest + watchdog workflow
- Test suite, live smoke-test workflow, CSV export, SVG summary cards

> Free tier: the first request wakes the instance, so give it a moment.

`Python` `FastAPI` `PostgreSQL` `Render`

[→ Repo](https://github.com/umutseve4/enflasyonum) · [→ Live](https://enflasyonum-7gcn.onrender.com)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### ▸ MakroQuest
**Economics detective game on real data**

- **LangGraph** agent + **pgvector** retrieval
- Real EVDS / TÜİK macroeconomic series
- Every clue cites its source — evaluation sits *beside* generation so unsupported answers can't hide

`Python` `LangGraph` `pgvector` `RAG` `FastAPI`

[→ Repo](https://github.com/umutseve4/makroquest)

</td>
<td width="50%" valign="top">

#### ▸ PulseGrid · PulseGrid 3D
**A data-reliability lab you can watch**

- Observable streaming pipelines: contracts, quarantine, replay, lineage, SLOs
- The 3D city is not decoration — height maps throughput, light density maps utilization
- **No WebGL? The full telemetry survives as text.**

`Python` `TypeScript` `Three.js` `data quality`

[→ Lab](https://github.com/umutseve4/pulsegrid) · [→ 3D](https://umutseve4.github.io/pulsegrid-3d/)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### ▸ Cosmic Econometric Observatory
**Provenance-first curriculum world engine**

- Deterministic knowledge graph: **147 nodes, 146 edges, 144 course records**
- Each course carries source id, view id, line position, SHA-256 digest
- Canvas is never the only information surface — HTML + SVG keep an equal identity set

`TypeScript` `provenance` `a11y`

[→ Repo](https://github.com/umutseve4/cosmic-econometric-observatory) · [→ Live](https://umutseve4.github.io/cosmic-econometric-observatory/)

</td>
<td width="50%" valign="top">

#### ▸ EkoDiff · Akademik Zaman Makinesi
**Versioned curriculum snapshots + local-first what-if engine**

- Diffs curriculum versions so a change is visible, not rumoured
- Runs locally in the browser; no student data leaves the device
- Independent student project — **not** an official university service

`JavaScript` `local-first` `verify CI`

[→ Repo](https://github.com/umutseve4/ekodiff) · [→ Live](https://umutseve4.github.io/ekodiff/)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### ▸ homefront-universe
**Universe-scale space RTS, zero dependencies**

- Raw **WebGL2 + hand-written GLSL**, procedural ship meshes, generative textures, GPU instancing
- Headless deterministic simulation path
- Frames stamped with engine-state checksums — reproducible, not decorative

`WebGL2` `GLSL` `JavaScript`

[→ Repo](https://github.com/umutseve4/homefront-universe)

</td>
<td width="50%" valign="top">

#### ▸ Çanakkale 1915 · Gallipoli 1915
**Commemorative WebGL sequences**

- Single-file Three.js scenes — no build step, no bundler, no tracking
- Turkish and English editions kept as separate surfaces rather than a language toggle bolted on
- Reduced-motion path is a real path, not a disabled animation

`Three.js` `WebGL` `a11y`

[→ TR](https://umutseve4.github.io/canakkale-1915-webgl/) · [→ EN](https://umutseve4.github.io/gallipoli-1915-webgl/)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### ▸ UludagFormula
**Original 3D racing sim**

- **Unreal Engine 5.8 + Blender 5.2 LTS**
- Custom vehicle physics
- Python-scripted editor automation

`UE5` `Blender` `Python` `C++`

[→ Repo](https://github.com/umutseve4/UludagFormula)

</td>
<td width="50%" valign="top">

#### ▸ ZİFT — brand system
**One vector master, every raster generated**

- `brand/zift.svg` is the only hand-authored file; CI renders 17 files into `brand/` plus the repo-root favicon, 18 in all
- A legibility gate measures the signal-red slits at 32px and **fails the build** if the mark stops reading
- Icons and link previews are injected into the site head by the same workflow, so surfaces cannot drift

`SVG` `Actions` `Pillow` `rsvg`

[→ Guide](https://github.com/umutseve4/umutseve4.github.io/blob/main/brand/README.md)

</td>
</tr>
</table>

<details>
<summary><b>&nbsp;⌗ &nbsp;More of the workshop &nbsp;— &nbsp;<i>further public repositories</i></b></summary>

<br/>

| Repo | One line |
|---|---|
| [RevisionLedger](https://github.com/umutseve4/RevisionLedger) | Bitemporal ledger on ALFRED GDPC1 — *what was known when the decision was made?* |
| [data-reliability-lab](https://github.com/umutseve4/data-reliability-lab) | Failure-simulation lab: data contracts, idempotency, quarantine/replay, lineage, SLOs |
| [tcmb-policy-rag-pipeline](https://github.com/umutseve4/tcmb-policy-rag-pipeline) | Incremental, versioned TCMB PPK ingestion with citation-backed retrieval |
| [data-economic-lab](https://github.com/umutseve4/data-economic-lab) | Reproducible TR macro pipeline: ingest → validate → SQLite → analyze → report |
| [eko-rasathane](https://github.com/umutseve4/eko-rasathane) | Evidence-driven study operating system for BUÜ Ekonometri students |
| [tercih-atlasi](https://github.com/umutseve4/tercih-atlasi) | Explainable 2026 campus & career decision atlas |
| [local-market-scanner](https://github.com/umutseve4/local-market-scanner) | Scores digital presence of Bursa health-sector businesses from public OpenStreetMap data |
| [ledgerpilot](https://github.com/umutseve4/ledgerpilot) | Zero-dependency freemium invoicing SaaS — quota paywall, 14 headless smoke tests |
| [structurecraft](https://github.com/umutseve4/structurecraft) | Fabric 1.20.1 mod; CI builds the jar **and** boots a real dedicated server every push |
| [btk-sql-lab](https://github.com/umutseve4/btk-sql-lab) | Codespaces SQL Server 2022 lab — coursework runs in a browser on a machine that can't host it |
| [scanline](https://github.com/umutseve4/scanline) | Software rasterizer with no GPU: clipping, z-buffer, PCF shadows, ACES — CI proves it draws pixels |
| [neon-lunapark-webgl](https://github.com/umutseve4/neon-lunapark-webgl) | Single-file Three.js night carnival: coaster train, ferris wheel, three lighting modes |
| [the-merge-launch](https://github.com/umutseve4/the-merge-launch) · [threejs-multilevel-chess](https://github.com/umutseve4/threejs-multilevel-chess) | Single-file experiments: launch atlas microsite, three-level 3D chess |
| [neon-overdrive](https://github.com/umutseve4/neon-overdrive) | **Placeholder — no code committed yet.** Listed because the repository is public, not because it runs |

</details>

<br/>

<!-- ────────────────────────────  04 / ARSENAL  ──────────────────────────── -->
<div align="center">

`04 / ARSENAL`

### **Tools, not trophies.**

**Data & AI**

<img src="https://img.shields.io/badge/Python-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=python&logoColor=FF4D4F" alt="Python" />
<img src="https://img.shields.io/badge/PostgreSQL-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=postgresql&logoColor=FF4D4F" alt="PostgreSQL" />
<img src="https://img.shields.io/badge/SQLite-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=sqlite&logoColor=FF4D4F" alt="SQLite" />
<img src="https://img.shields.io/badge/FastAPI-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=fastapi&logoColor=FF4D4F" alt="FastAPI" />
<img src="https://img.shields.io/badge/dbt-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=dbt&logoColor=FF4D4F" alt="dbt" />
<img src="https://img.shields.io/badge/DuckDB-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=duckdb&logoColor=FF4D4F" alt="DuckDB" />
<img src="https://img.shields.io/badge/Parquet-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=apache&logoColor=FF4D4F" alt="Parquet" />
<img src="https://img.shields.io/badge/pandas-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=pandas&logoColor=FF4D4F" alt="pandas" />
<img src="https://img.shields.io/badge/LangGraph-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=langchain&logoColor=FF4D4F" alt="LangGraph" />
<img src="https://img.shields.io/badge/pgvector-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=postgresql&logoColor=FF4D4F" alt="pgvector" />
<img src="https://img.shields.io/badge/pytest-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=pytest&logoColor=FF4D4F" alt="pytest" />

**Engineering & Ops**

<img src="https://img.shields.io/badge/Git-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=git&logoColor=FF4D4F" alt="Git" />
<img src="https://img.shields.io/badge/GitHub-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=github&logoColor=FF4D4F" alt="GitHub" />
<img src="https://img.shields.io/badge/GitHub_Actions-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=githubactions&logoColor=FF4D4F" alt="GitHub Actions" />
<img src="https://img.shields.io/badge/Docker-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=docker&logoColor=FF4D4F" alt="Docker" />
<img src="https://img.shields.io/badge/Linux-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=linux&logoColor=FF4D4F" alt="Linux" />
<img src="https://img.shields.io/badge/VS_Code-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=visualstudiocode&logoColor=FF4D4F" alt="VS Code" />
<img src="https://img.shields.io/badge/Streamlit-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=streamlit&logoColor=FF4D4F" alt="Streamlit" />
<img src="https://img.shields.io/badge/Render-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=render&logoColor=FF4D4F" alt="Render" />

**Graphics differentiator**

<img src="https://img.shields.io/badge/WebGL2-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=webgl&logoColor=FF4D4F" alt="WebGL2" />
<img src="https://img.shields.io/badge/GLSL-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=opengl&logoColor=FF4D4F" alt="GLSL" />
<img src="https://img.shields.io/badge/Three.js-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=threedotjs&logoColor=FF4D4F" alt="Three.js" />
<img src="https://img.shields.io/badge/GPU_Instancing-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=nvidia&logoColor=FF4D4F" alt="GPU Instancing" />
<img src="https://img.shields.io/badge/Unreal_Engine-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=unrealengine&logoColor=FF4D4F" alt="Unreal Engine" />
<img src="https://img.shields.io/badge/Blender-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=blender&logoColor=FF4D4F" alt="Blender" />
<img src="https://img.shields.io/badge/TypeScript-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=typescript&logoColor=FF4D4F" alt="TypeScript" />
<img src="https://img.shields.io/badge/JavaScript-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=javascript&logoColor=FF4D4F" alt="JavaScript" />
<img src="https://img.shields.io/badge/C++-0B0B0B?style=flat-square&labelColor=0B0B0B&logo=cplusplus&logoColor=FF4D4F" alt="C++" />

</div>

<br/>

<!-- ────────────────────────────  05 / TELEMETRY  ──────────────────────────── -->
<div align="center">

`05 / TELEMETRY`

<img height="165" src="https://github-readme-stats.vercel.app/api?username=umutseve4&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&bg_color=0B0B0B&title_color=FF4D4F&icon_color=FF4D4F&text_color=F5F2EA" alt="GitHub stats" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=umutseve4&layout=compact&langs_count=8&hide_border=true&bg_color=0B0B0B&title_color=FF4D4F&text_color=F5F2EA" alt="Top languages" />

<br/>

<img height="165" src="https://github-readme-streak-stats.herokuapp.com/?user=umutseve4&hide_border=true&background=0B0B0B&ring=FF4D4F&fire=FF4D4F&currStreakLabel=FF4D4F&stroke=FF4D4F&sideNums=F5F2EA&sideLabels=F5F2EA&currStreakNum=F5F2EA&dates=9A9A9A" alt="Contribution streak" />

<br/><br/>

<img width="96%" src="https://github-readme-activity-graph.vercel.app/graph?username=umutseve4&bg_color=0B0B0B&color=F5F2EA&line=FF4D4F&point=FF4D4F&title_color=FF4D4F&area=true&hide_border=true&custom_title=Contribution%20Telemetry" alt="Contribution telemetry" />

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/umutseve4/umutseve4/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/umutseve4/umutseve4/output/github-snake.svg" />
  <img alt="contribution snake" src="https://raw.githubusercontent.com/umutseve4/umutseve4/output/github-snake.svg" width="100%" />
</picture>

</div>

<br/>

<!-- ────────────────────────────  06 / CONTACT  ──────────────────────────── -->
<div align="center">

`06 / HANDOFF`

### **Let's build something measurable.**

Open to **data engineering internships**, junior roles, and engineering collaboration.

<a href="https://www.linkedin.com/in/umut-sever-7851b73a6/"><img src="https://img.shields.io/badge/LINKEDIN-0B0B0B?style=for-the-badge&logo=linkedin&logoColor=FF4D4F" alt="LinkedIn" /></a>
<a href="https://umutseve4.github.io"><img src="https://img.shields.io/badge/PORTFOLIO-0B0B0B?style=for-the-badge&logo=githubpages&logoColor=FF4D4F" alt="Portfolio" /></a>
<a href="https://x.com/umutseve4"><img src="https://img.shields.io/badge/X-0B0B0B?style=for-the-badge&logo=x&logoColor=FF4D4F" alt="X" /></a>

<br/><br/>

<img src="https://umutseve4.github.io/brand/zift-mark-128.png" width="76" alt="ZİFT" />

**tested > claimed · deployed > demoed · evidence > adjectives**

<sub>Motion here is decoration; the proof lives in the linked pipelines, ledgers and limitation notes.</sub>

</div>
