<div align="center">

# Umut SEVER

### Data systems with evidence. Visual systems with a pulse.

Economics Engineering student building at the intersection of **data reliability**, **economic software**, and **real-time graphics**.

[Portfolio](https://umutseve4.github.io/) · [Selected repositories](#selected-systems) · [LinkedIn](https://www.linkedin.com/in/umut-sever-7851b73a6/) · [Email](mailto:2404005065@ogrenci.sbu.edu.tr)

</div>

---

## Two tracks, one engineering mindset

<table>
<tr>
<td width="50%" valign="top">

### Data & Reliability Systems

I turn economic questions into inspectable pipelines, ledgers, APIs, and retrieval systems. The recurring concerns are provenance, data contracts, quality gates, replay, and the difference between **tested**, **deployed**, and **production-ready**.

`Python` `SQL` `PostgreSQL` `DuckDB` `dbt` `FastAPI` `RAG`

</td>
<td width="50%" valign="top">

### Graphics & Simulation Systems

I explore the same systems problems through deterministic simulations, Three.js worlds, raw WebGL2, and hand-written GLSL: explicit state, bounded loops, reproducible behavior, and graceful fallback.

`TypeScript` `Three.js` `WebGL2` `GLSL` `Canvas` `Simulation`

</td>
</tr>
</table>

## Selected systems

### [econ-lakehouse](https://github.com/umutseve4/econ-lakehouse)

A medallion-architecture warehouse for Turkish macroeconomic data: Python ingestion into Parquet Bronze, dbt + DuckDB Silver/Gold models, data-quality gates, orchestration, API, and an inspectable Streamlit surface.

**Why it matters:** lineage and failure boundaries stay visible across layers instead of being hidden behind one successful chart.  
[Repository](https://github.com/umutseve4/econ-lakehouse) · [Deployment](https://econ-lakehouse-umut.streamlit.app/)

---

### [RevisionLedger](https://github.com/umutseve4/RevisionLedger)

An evidence-first bitemporal ledger for a question ordinary dashboards often erase: **what was known at the historical decision time?**

**Why it matters:** revised economic values remain queryable without overwriting the information set that existed earlier.  
[Repository](https://github.com/umutseve4/RevisionLedger)

---

### [PulseGrid](https://github.com/umutseve4/pulsegrid) × [PulseGrid 3D](https://github.com/umutseve4/pulsegrid-3d)

A reliability laboratory and its cinematic Three.js projection, built around observable flow, failure, quarantine, replay, lineage, and recovery.

**Why it matters:** failure is treated as a first-class state to inspect and explain—not an exception hidden from the interface.  
[Core system](https://github.com/umutseve4/pulsegrid) · [3D experience](https://github.com/umutseve4/pulsegrid-3d)

---

### [Cosmic Econometric Observatory](https://github.com/umutseve4/cosmic-econometric-observatory)

A deterministic, provenance-first world engine for projecting curriculum knowledge graphs into accessible interactive scenes.

**Why it matters:** the visible world remains downstream of explicit graph and provenance contracts; the roadmap is not presented as shipped behavior.  
[Repository](https://github.com/umutseve4/cosmic-econometric-observatory)

---

### [Homefront Universe](https://github.com/umutseve4/homefront-universe)

A universe-scale space RTS experiment built with raw WebGL2, hand-written GLSL, procedural geometry, GPU instancing, and a deterministic simulation path.

**Why it matters:** visual output can be tied back to reproducible engine state rather than existing only as a screenshot. Headless evidence does not replace real browser/GPU validation.  
[Repository](https://github.com/umutseve4/homefront-universe)

---

### [Enflasyonum](https://github.com/umutseve4/enflasyonum)

A personal inflation index and API that compares a household spending basket with official CPI categories through an explainable data pipeline.

**Why it matters:** the result exposes its calculation path, automation contract, tests, and hosting boundaries instead of presenting a single opaque number.  
[Repository](https://github.com/umutseve4/enflasyonum) · [Deployment](https://enflasyonum-7gcn.onrender.com/)

## How I work

```text
model the boundary → build the smallest vertical slice → automate checks
→ expose evidence → publish limitations → iterate
```

- **Evidence before adjectives:** repositories and reproducible checks carry more weight than self-assigned titles.
- **No black boxes by default:** I want to understand state, failure, timing, and data lineage.
- **Accessibility is architecture:** keyboard support, reduced motion, and graceful fallback belong in the design phase.
- **Honest status language:** CI evidence, deployment evidence, and production readiness are separate claims.

## Focused toolkit

| Layer | Tools |
|---|---|
| Data systems | Python, pandas, SQL, PostgreSQL, SQLite, DuckDB, dbt, Parquet |
| Services & retrieval | FastAPI, REST APIs, RAG, citation-backed retrieval, evaluation |
| Reliability | testing, CI/CD, data contracts, quality gates, quarantine/replay, SLO thinking |
| Graphics | TypeScript, JavaScript, Three.js, WebGL2, GLSL, Canvas, deterministic simulation |
| Workflow | Git, GitHub Actions, Docker, Linux |

## Contact

I am open to **internships, junior opportunities, and ambitious collaborations** across data engineering, economic software, and interactive systems.

- **Portfolio:** [umutseve4.github.io](https://umutseve4.github.io/)
- **LinkedIn:** [Umut SEVER](https://www.linkedin.com/in/umut-sever-7851b73a6/)
- **Email:** [2404005065@ogrenci.sbu.edu.tr](mailto:2404005065@ogrenci.sbu.edu.tr)

> Tested is not the same as deployed. Deployed is not the same as production-ready. The boundary should always be visible.
