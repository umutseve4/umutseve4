"""Insert the missing Featured Builds into the profile README.

Anchored and idempotent, like every other rewrite in this audit. The README is
edited by a script running on the runner rather than transcribed through an
API, because retyping a file by hand to change four lines is how silent
one-character mistakes get made.

Exit codes: 0 patched, 0 already patched (no-op), 2 anchor drift.
"""
import io
import os
import sys

README = os.environ.get("README", "README.md")
ANCHOR = "</table>"
SENTINEL = "econ-lakehouse"

ROWS = """<tr>
<td width="50%" valign="top">

### econ-lakehouse
Medallion lakehouse for Turkish macro data. Python ingest to Parquet bronze,
dbt + DuckDB for silver/gold, data-quality gates, scheduled via Actions.

**Live:** https://econ-lakehouse-umut.streamlit.app
`Python` `dbt` `DuckDB` `Parquet`

</td>
<td width="50%" valign="top">

### RevisionLedger
Bitemporal ledger answering a question most dashboards quietly get wrong:
*what was known at the time the decision was made?* Built on ALFRED GDPC1.

`Python` `bitemporal` `evidence-first`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### data-reliability-lab
Failure-simulation lab for data contracts, idempotency, quarantine/replay,
lineage and reliability SLOs. Breaking pipelines on purpose to learn how.

`Python` `data quality` `SLO`

</td>
<td width="50%" valign="top">

### tcmb-policy-rag-pipeline
Incremental, versioned ingestion of TCMB PPK decisions with citation-backed
retrieval. Every answer carries the document it came from.

`Python` `RAG` `versioned ingest`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### btk-sql-lab
Codespaces-based SQL Server 2022 lab, built so the coursework runs from a
browser on a machine that cannot host it locally.

`SQL Server` `Codespaces` `Shell`

</td>
<td width="50%" valign="top">
</td>
</tr>
"""


def main():
    with io.open(README, "r", encoding="utf-8") as fh:
        text = fh.read()

    if SENTINEL in text:
        print("already patched; nothing to do")
        return 0

    n = text.count(ANCHOR)
    if n != 1:
        sys.stderr.write("anchor %r matched %d times, expected 1\n" % (ANCHOR, n))
        return 2

    text = text.replace(ANCHOR, ROWS + ANCHOR, 1)

    with io.open(README, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print("patched: inserted 3 rows before the single %s" % ANCHOR)
    return 0


if __name__ == "__main__":
    sys.exit(main())
