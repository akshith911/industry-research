# Evidence rules and staging format

Every agent that produces data reads this file. The tooling (`python -m irs`) enforces it; a batch that breaks a rule is rejected whole.

## 1. Never write to `databases/` directly

Write a **batch folder** instead:

```
industries/<slug>/staging/<batch-name>/
  batch.yaml          # agent: <your run id>    research_unit: RU-0007
  sources.jsonl       # new records, one JSON object per line, no "id"
  claims.jsonl
  companies.jsonl ... # any database name from irs/db.py
  updates.jsonl       # changes to existing records: {"id": "CO-0003", "set": {"stage": "startup"}}
```

- `<batch-name>` = `<RU id>-<your run id>` (e.g. `RU-0007-res-7f3a`). Never reuse a name.
- Give a record `"key": "anything"` so other records in the same batch can point to it as `"@anything"`.
- Point to existing records by real id (`SRC-0012`, `CO-0003`). Look them up first (`grep` the JSONL).
- Duplicates are fine to submit: the merge reuses an existing source with the same URL, an entity/company/term with the same name or alias, and a claim with identical text.
- Check your batch before finishing: `python -m irs merge <slug> <batch-name> --dry-run`. Fix every error it prints. Do **not** run a real merge; the orchestrator does that.

## 2. Sources (`sources.jsonl`)

```json
{"key":"s1","url":"https://www.semiconductors.org/...","title":"2025 State of the U.S. Semiconductor Industry","publisher":"Semiconductor Industry Association","publication_date":"2025-07","source_type":"industry_body","tier":1,"key_document":true,"doc_type":"industry report","why_important":"Annual structural overview with value-chain shares","paywalled":false}
```

- The URL must be one you actually opened in this run. Never construct, guess or "fix" a URL.
- `tier` is fixed by `source_type` (irs/rules.py `TIER_BY_TYPE`): tier 1 = government, regulator, legislation, official_statistics, court_record, company_filing, annual_report, investor_presentation, company_documentation, industry_body, standards_body; tier 2 = research_firm, academic, financial_press, industry_press; tier 3 = everything else (news, blog, startup_database, forum, social, aggregator, encyclopedia, other).
- Classify honestly: a news article *about* a filing is `news`; the filing itself is `company_filing`. A company's marketing page is `company_documentation`, and a claim taken from it is a `reported_claim`.
- `publication_date`: `YYYY`, `YYYY-MM`, `YYYY-MM-DD` or `unknown`. Never guess.

## 3. Claims (`claims.jsonl`)

One atomic statement per claim. Split "X was founded in 1987 and has 60% share" into two claims.

```json
{"key":"c1","claim":"TSMC reported full-year 2025 revenue of NT$X trillion.","claim_type":"fact","entity_ids":["CO-0004"],"source_ids":["@s2"],"evidence":"\"<verbatim sentence from the source>\" (Annual report 2025, p. 12)","metric":{"name":"Annual revenue","value":123.4,"unit":"NTD bn","period":"CY2025","geography":"Global (company-wide)","population":"TSMC consolidated net revenue","methodology":"Audited financial statements"}}
```

**claim_type** (what kind of statement it is):

| type | use when | needs source |
|---|---|---|
| `fact` | an authoritative source states it as fact (statute, filing, official statistic) | yes |
| `reported_claim` | an entity says it about itself or its products; marketing; interview answers | yes |
| `estimate` | a modelled figure (analyst, association, government projection) | yes |
| `inference` | our reasoning from other claims; name them in `notes` | no |
| `interpretation` | our reading of what something means | no |
| `assumption` | a working premise we have not evidenced | no |
| `unknown` | we searched and could not establish it; say what was searched in `evidence` | no |

**evidence** = a verbatim quote (in quotation marks) plus its location (page, table, section). If the page tool summarised the page, ask it to quote the passage verbatim. If you can't get the exact words, write "paraphrase:" and the precise location. Never cite a source that only vaguely covers the topic.

**metric** (only for numbers): `name, value (or value_low/value_high), unit, period, geography, population, methodology`. Copy the unit and currency exactly (nominal vs real, USD vs local, 200mm-equivalent wafers, calendar vs fiscal year). `population` says exactly what was counted. `methodology` says how the source produced it, or "not disclosed".

**Do not set** `status`, `confidence`, `verified_by` or `last_verified`. Researchers' claims enter as `unverified`/`low`. Only an independent fact-check can raise them, and code computes confidence:

| confidence | rule (irs/rules.py) |
|---|---|
| high | verified by an independent checker against a tier-1 source (capped at medium for `reported_claim`) |
| medium | verified against tier-2, or corroborated by 2+ independent publishers; or partially verified against tier-1 |
| low | unverified, tier-3 only, inference/assumption, conflicting, or failed a check |
| unknown | documented absence of evidence |

## 4. Other records

- **companies**: descriptive fields only. **Every number** (revenue, funding, capacity, share, employees) is a claim, linked by `metric_claim_ids`. Omit unknown fields; never fill them with guesses. `roles` must be ontology entity_type ids.
- **entities**: `entity_type` must exist in `ontology.yaml`. If you find a genuinely new kind of participant, propose it in your report (section 6) instead of inventing a type.
- **relations**: `subject_id --predicate--> object_id` using ontology predicates, evidenced by `claim_ids`.
- **regulations**: name, authority, jurisdiction, instrument_type, status, affected_participants (ontology types), requirements, source_ids (prefer the legal text or the regulator's page).
- **glossary**: `simple_definition` must be understandable by someone with no industry background; `technical_definition` can be precise.
- **contradictions**: 2+ claim ids that disagree, `possible_reasons` (definition, period, currency, population, method), `comparable` (false if they measure different things), `more_defensible` (claim id or null) with `rationale`, `remaining_uncertainty`.
- **interview_queue**: unknowns that only a participant can answer.
- **research_units** (new units discovered while researching): full schema, `origin: researcher_discovery`, `origin_ref: <your RU>`, `status: queued`.

## 5. Hard prohibitions

No fabricated URLs, sources, statistics, company facts or quotes. No filling gaps with plausible numbers ("Publicly available evidence is insufficient to establish this" is a valid result: record it as an `unknown` claim). No mixing geographies, periods, currencies or populations in one claim. No treating marketing as verified fact. No hiding a disagreement between credible sources.

## 6. Your final message to the orchestrator

Keep it short (the data is in the batch):
1. Batch name and the dry-run result line.
2. Counts: claims by type, sources by tier.
3. Contradictions found.
4. New research units proposed (ids/titles) and new ontology types suggested, with the evidence.
5. The 3–5 most important things learned, in plain words.
6. What you could not find, and why (paywall, no public data, tool failure).
