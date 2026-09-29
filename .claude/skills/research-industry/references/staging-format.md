# Staging format (how agents hand results to the tooling)

Agents never edit `industries/<slug>/databases/`. Each agent run writes its own batch folder:

```
industries/<slug>/staging/<batch>/          # batch = w<wave>-<RU id>-<role>, e.g. w1-RU-0007-research
  sources.jsonl  claims.jsonl  companies.jsonl  entities.jsonl  regulations.jsonl
  relations.jsonl  glossary.jsonl  contradictions.jsonl  fact_checks.jsonl
  research_units.jsonl  interview_queue.jsonl  patches.jsonl  notes.md
```

Only create the files you need. One JSON object per line. Then the orchestrator runs `python -m irs merge <slug> <batch>`: it assigns ids, de-duplicates, resolves references, computes tier and confidence, validates everything, and writes nothing if anything is wrong.

## References

- Give each new record a local `"key"` (unique within your batch, e.g. `"s1"`, `"c12"`, `"tsmc"`). Never write `"id"`.
- Refer to records in your batch as `"@key"`; refer to records already in the databases by their id (`"SRC-0042"`, `"CO-0007"`). Look them up first with Grep in `databases/*.jsonl` to avoid duplicates.
- Sources are de-duplicated by URL and companies/entities/regulations/glossary terms by name and aliases automatically, so re-listing a known source is harmless.

## Field rules (full schemas in `schemas/`)

- Do **not** set: `id`, `tier`, `confidence`, `confidence_reason`, `verified_by`, `last_verified`. Code derives them.
- Claim `status` you may set: `unverified` (default), `inferred`, `assumption`, `unknown`. Never `verified`.
- `recorded_by` / `checker`: your batch name (e.g. `"w1-RU-0007-research"`). It is how independence is enforced.
- Dates: `YYYY-MM-DD`; publication dates may be `YYYY`, `YYYY-MM` or `unknown`.
- `evidence`: a verbatim quote (preferably) or an exact locator (page/table/section). Keep it under ~400 characters.

## Examples

`sources.jsonl`
```json
{"key": "s1", "url": "https://www.example.gov/stats/2025.pdf", "title": "Annual Statistics 2025", "publisher": "Example Statistics Office", "publication_date": "2025-06", "source_type": "official_statistics", "key_document": true, "why_important": "Official series for sector output", "research_units": ["RU-0007"]}
```

`claims.jsonl`: a metric claim, a reported claim and a documented unknown
```json
{"key": "c1", "claim": "Worldwide sales in the sector were USD 100 bn in CY2024 (per the statistics office).", "claim_type": "estimate", "entity_ids": ["ENT-0003"], "metric": {"name": "worldwide sector sales", "value": 100, "unit": "USD bn", "period": "CY2024", "geography": "World", "population": "member-reported sales, excludes captive production", "methodology": "aggregated member reports"}, "source_ids": ["@s1"], "evidence": "Table 1: total sales 2024 ... 100.0", "research_unit": "RU-0007", "recorded_by": "w1-RU-0007-research"}
{"key": "c2", "claim": "Company X says it serves more than 500 customers.", "claim_type": "reported_claim", "entity_ids": ["CO-0012"], "source_ids": ["SRC-0031"], "evidence": "'...trusted by over 500 customers worldwide'", "research_unit": "RU-0007", "recorded_by": "w1-RU-0007-research"}
{"key": "c3", "claim": "Publicly available evidence is insufficient to establish the average gross margin of distributors in this segment.", "claim_type": "unknown", "status": "unknown", "source_ids": [], "evidence": "", "research_unit": "RU-0007", "recorded_by": "w1-RU-0007-research", "notes": "Searched: annual reports of 3 listed distributors (no segment split); association site; no data."}
```

`companies.jsonl` (no numbers: link metric claims instead)
```json
{"key": "x", "name": "Company X Ltd", "aliases": ["Company X"], "roles": ["distributor"], "hq_country": "Japan", "founded": 1987, "ownership": "public", "listing": "TSE:0000", "stage": "incumbent", "business_model": "...", "metric_claim_ids": ["@c2"], "source_ids": ["SRC-0031"], "last_verified": "2026-09-29", "research_units": ["RU-0007"]}
```

`research_units.jsonl`: a newly discovered area
```json
{"key": "u1", "title": "Role of trading houses in materials procurement", "dimension": "participants", "why_it_matters": "Found repeatedly as an intermediary; not in the tree", "questions": ["What do trading houses do between material makers and fabs?"], "expected_outputs": ["claims", "companies"], "depends_on": ["RU-0007"], "wave": 2, "priority": "P1", "status": "queued", "origin": "researcher_discovery", "origin_ref": "RU-0007"}
```

`fact_checks.jsonl`
```json
{"claim_id": "CLM-0104", "checker": "w1-RU-0007-factcheck", "checked_at": "2026-09-29", "source_ids_checked": ["SRC-0031"], "original_interpretation": "Sales of USD 100 bn in 2024", "evidence_found": "Table 1 shows 100.0 for 2024, but labelled 'preliminary'", "verdict": "partially_verified", "correction": "Figure is preliminary; final release due 2026-03"}
```

`patches.jsonl`: corrections to descriptive fields of existing records (never claim status/confidence)
```json
{"id": "CO-0007", "set": {"founded": 1987}, "reason": "Annual report p.3 gives 1987; earlier record said 1978"}
```
