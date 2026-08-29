<div align="center">

# Umut SEVER

**AI & Data Engineering · Economics · Reliability · Real-time Graphics**

[![Portfolio](https://img.shields.io/badge/Portfolio-umutseve4.github.io-0D1117?style=for-the-badge&logo=githubpages&logoColor=00E5FF)](https://umutseve4.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Umut_SEVER-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/umut-sever-7851b73a6/)
[![GitHub](https://img.shields.io/badge/GitHub-umutseve4-0D1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/umutseve4)

</div>

## About me

I am an **Economics Engineering student at Uludağ University** building toward **AI and Data Engineering**. My portfolio centers on real economic data, reproducible pipelines, retrieval-backed AI, CI/CD, and explicit reliability boundaries.

I use a simple standard: **measured evidence over absolute claims**. A green workflow proves the checks it actually ran—not production readiness, browser/GPU behavior, or a deployment unless those were independently exercised.

**Current direction**

- Production-grade RAG and agent evaluation
- MCP and secure tool integrations
- Asynchronous, type-safe Python services
- Retrieval quality, citation accuracy, error analysis, and hallucination mitigation
- Monitoring, governance, guardrails, and cost-aware cloud architecture
- PostgreSQL, Docker, and cloud data engineering

## Featured systems

### [enflasyonum](https://github.com/umutseve4/enflasyonum) · [Live](https://enflasyonum-7gcn.onrender.com)

Personal inflation index compared with official TÜİK CPI.

- FastAPI + PostgreSQL ingestion and API pipeline
- 13 ECOICOP sub-indices, CSV export, SVG summaries, and history charts
- Scheduled daily EVDS ingestion and a scheduled `/health` watchdog
- A verified 100+ automated-test milestone; CI covers Python 3.11, 3.12, and 3.13

**Boundary:** workflow schedules document the automation contract; they do not by themselves prove uninterrupted daily execution or production readiness.

`Python` `FastAPI` `PostgreSQL` `GitHub Actions` `Render`

---

### [MakroQuest](https://github.com/umutseve4/makroquest) · [Live](https://makroquest.onrender.com)

Economics detective game with source-citing retrieval over World Bank open macroeconomic data.

- FastAPI vertical slice with a deterministic, network-free RAG evaluation path
- 30-question golden set
- Recorded evaluation: **hit-rate@3 100%**, **citation accuracy 96.67%**, **keyword coverage 83.33%**
- LangGraph, pgvector, and expanded TÜİK coverage remain architecture/roadmap directions where not yet exercised by the current deterministic evaluation

**Boundary:** citation and retrieval metrics reduce unsupported output risk; they are not a zero-hallucination guarantee.

`Python` `RAG` `FastAPI` `Retrieval Evaluation` `Docker`

---

### [econ-lakehouse](https://github.com/umutseve4/econ-lakehouse) · [Live](https://econ-lakehouse-umut.streamlit.app)

Medallion lakehouse for Turkish macroeconomic data.

- Python ingestion into Parquet bronze data
- dbt + DuckDB silver/gold transformations
- Data-quality gates and scheduled automation

`Python` `dbt` `DuckDB` `Parquet` `Streamlit`

---

### [RevisionLedger](https://github.com/umutseve4/RevisionLedger)

Bitemporal revision ledger built around ALFRED GDPC1: *what was known when the decision was made?*

`Python` `Bitemporal Data` `Evidence-first Engineering`

---

### [data-reliability-lab](https://github.com/umutseve4/data-reliability-lab)

Failure-simulation laboratory for data contracts, idempotency, quarantine/replay, lineage, and reliability SLOs.

`Python` `Data Quality` `Reliability` `SLO`

---

### [tcmb-policy-rag-pipeline](https://github.com/umutseve4/tcmb-policy-rag-pipeline)

Incremental, versioned ingestion of TCMB policy decisions with citation-backed retrieval.

`Python` `RAG` `Versioned Ingestion` `Citations`

## Engineering range

### [homefront-universe](https://github.com/umutseve4/homefront-universe)

Deterministic space-fleet simulation and renderer written with raw WebGL2 and hand-written GLSL.

- Empty `dependencies` and `devDependencies`: zero npm runtime/build packages
- Procedural meshes, GPU-instancing code paths, and deterministic Node-based contract tests

**Boundary:** Node/fake-WebGL checks and headless SVG evidence do not prove real browser GPU shader compilation or interactive rendering.

### [UludagFormula](https://github.com/umutseve4/UludagFormula)

Original racing-simulation project targeting Unreal Engine 5.8 and Blender 5.2 LTS, with C++, Python-driven asset/editor automation, and deterministic validation tooling.

**Boundary:** hosted CI validates repository contracts and Blender-side automation; it does not prove current Unreal compilation, playtesting, physics, or visuals.

### [StructureCraft](https://github.com/umutseve4/structurecraft)

Fabric 1.20.1 Minecraft mod with blueprint structures and rideable/flyable entities.

- CI builds the JAR and boots a real headless Fabric dedicated server as a smoke test

**Boundary:** server boot does not replace in-game gameplay and visual validation.

### [LedgerPilot](https://github.com/umutseve4/ledgerpilot)

Zero-package vanilla JavaScript invoicing prototype using `localStorage`.

- Invoices, clients, expenses, reports, quotas, and a simulated checkout flow
- **14 headless smoke assertions** covering store and billing behavior

**Boundary:** payments are simulated; data is browser-local rather than a production SaaS backend.

## Toolbox

- **Data & AI:** Python, pandas, PostgreSQL, SQLite, FastAPI, RAG, retrieval evaluation, Parquet
- **Engineering:** Git, GitHub Actions, Linux, Docker, REST APIs, testing, CI/CD
- **Graphics:** JavaScript/TypeScript, WebGL2, GLSL, Unreal Engine, Blender, C++
- **Learning next:** production agent evaluation, MCP, GCP/Vertex AI, secure enterprise integrations, monitoring and governance

## Contact

- [LinkedIn](https://www.linkedin.com/in/umut-sever-7851b73a6/)
- [Portfolio](https://umutseve4.github.io)
- [GitHub](https://github.com/umutseve4)

> Tested > claimed. Measured > absolute. Deployment evidence is stated separately from CI evidence.
