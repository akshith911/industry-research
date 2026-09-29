# Research methodology

**Version 0.1.0** (2026-09-29). Every atlas records the version it was built with in its `config.yaml`.

## Purpose

Build, from zero prior knowledge, a navigable and auditable understanding of an industry: how it is structured, who participates, how money, goods and information flow, how work gets done, what rules govern it, where power sits, how companies make and lose money, what technology exists, where things fail, and what is changing. Priorities, in order: accuracy, evidence, coverage, traceability, understanding, structure, updateability, presentation.

## Principles

1. **First principles**: discover the structure from evidence; no imported template of "what matters".
2. **Evidence before conclusions**: no starting thesis; opportunity analysis only after the map passes audit.
3. **Source hierarchy**: tier 1 primary > tier 2 high-quality secondary > tier 3 discovery (`references/source-hierarchy.md`).
4. **Traceability**: every claim is atomic and links to sources with a verbatim evidence passage, publication and access dates, research unit and recording agent.
5. **Fact vs inference**: every claim is typed (fact, reported claim, estimate, inference, interpretation, assumption, unknown) and carries a verification status.
6. **Contradictions are data**: recorded in a ledger with reasons and remaining uncertainty; definitional differences are separated from true conflicts.
7. **Negative evidence counts**: small markets, weak problems, marginal participants and missing data are recorded.
8. **No manufactured precision**: gaps stay gaps ("publicly available evidence is insufficient to establish this").

## Process

| Phase | What happens | Output |
|---|---|---|
| 0. Scope & discovery | Parallel discovery researchers map the territory; planner derives ontology and first maps from their evidence | `ontology.yaml`, `phase0/*.md` |
| 1. Research tree | Planner writes 40–150+ research units; gap finder critiques the plan | `research_units` DB, research plan |
| 2. Waves | Researchers (parallel) → merge → independent fact-checkers → contradiction checker → gap finder (new units) → repeat | Claims, sources, companies, regulations, glossary, relations, interview queue |
| Stop | All dimensions covered, audit passes, new research mostly duplicates, remaining unknowns need interviews | Research log with the numbers |
| 3. Synthesis & audit | Synthesizers write beginner-first pages citing claims; independent audit; failures feed back to Phase 2 | Atlas pages, quality audit |
| 4. Opportunities (optional) | Evidence-grounded opportunities, red-team per opportunity, code-computed scores | Opportunity scores with explicit calculations |
| Update | Re-verify stale claims, scan for changes, diff against last tagged version | CHANGELOG entry |

## Division of labour: code vs agents

| Code (`irs/`, deterministic) | Agents (judgment) |
|---|---|
| Schema validation, referential integrity, id assignment | Decomposing the industry, ontology, research tree |
| Source tier from source type; URL normalisation and dedupe | Searching, reading, extracting atomic claims with quotes |
| Confidence from status + source tier (`irs/rules.py`) | Classifying claims and sources honestly |
| Enforcing independent verification (checker ≠ author) | Re-opening sources and judging support (fact-checker) |
| Duplicate and near-duplicate detection; saturation metric | Judging comparability; explaining contradictions |
| Dependency ordering of the research queue; cycle detection | Finding gaps, hidden participants, adjacent industries |
| Coverage report; citation lint on atlas pages | Beginner-first synthesis |
| Opportunity score arithmetic from config weights | Rating criteria with evidence; red-teaming |
| Generated database pages; diffs between versions | Update scans for what changed |

## Confidence model

Derived, never asserted (`irs/rules.py`): **high** = independently verified against a tier-1 source (self-reported claims capped at medium); **medium** = verified against tier-2, corroborated by 2+ independent publishers, or partially verified against tier-1; **low** = unverified, tier-3-only, reasoning (inference, interpretation, assumption), conflicting or failed checks; **unknown** = documented absence of evidence. Each claim stores the reason.

## Known limitations

- Web pages are read through a tool that summarises; fact-checkers therefore ask for verbatim passages, and verification is by an independent agent, not by string-matching the raw page.
- Paywalled research (many market-size reports, proprietary databases) is out of reach; its public summaries are cited as such.
- Desk research cannot establish private economics, internal workflows or intentions; these go to the interview queue, and interview answers are recorded as reported claims, not verified facts.

## Versioning

- Methodology: semantic version in this file; changes are logged in `CHANGELOG.md`.
- Atlas: `atlas_version` in each `config.yaml`; releases are git-tagged `atlas/<slug>/v<version>`; `python -m irs diff <slug> <tag>` lists added, removed and changed records.
- Every claim carries `recorded_at`, `last_verified` and its sources' `access_date`; `stale_after_days` flags claims for re-verification.
