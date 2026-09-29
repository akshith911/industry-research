# Quality audit and stop condition

Run before declaring an atlas complete, and before any opportunity analysis. The audit has a deterministic half (code) and a judgment half (an auditor agent that did not write the pages).

## Deterministic checks (must all pass)

```
python -m irs validate <slug>     # 0 errors
python -m irs coverage <slug>     # every dimension has units and verified claims
python -m irs saturation <slug>   # duplicate share over last 10 batches
python -m irs status <slug>       # unverified backlog = 0 for fact/estimate/reported_claim
python -m irs build <slug>
```

## Judgment checks (auditor answers each with evidence: claim ids / page links)

| Area | Question | Pass means |
|---|---|---|
| Coverage | Have we investigated every major participant category in the ontology? | Every entity_type has entities/companies and a participants page |
| Value chain | Can we explain how value moves from inputs to end use? | Value-chain page cites claims for each stage |
| Money | Who pays whom, for what, on what terms, who carries working capital and risk? | Money-flow page covers every major edge |
| Information | What information is generated, where does it go, where is it manual? | Information-flow page + workflows |
| Regulation | Major regulatory mechanisms per jurisdiction, mapped to participants? | Regulatory DB populated with tier-1 sources |
| Economics | How do major participants make and lose money? | Business-model and economics pages with metrics |
| Companies | Incumbents, mid-market, startups, infrastructure providers? | Company DB spans each role and stage |
| Workflows | How is work actually performed (trigger→resolution)? | At least the core workflows at operational depth |
| Technology | Major technology systems and their suppliers? | Technology pages + entities |
| Geography | Geographic differences considered? | Geography dimension covered; no mixed-geography metrics |
| Time | Historical vs current clearly separated? | Every metric has a period |
| Evidence | Can major claims be traced to sources? | Lint shows no uncited figures on narrative pages |
| Contradictions | Conflicts identified and explained? | Contradiction ledger reviewed; no silent picks |
| Unknowns | Documented what we cannot establish? | Knowledge-gap report + interview pack populated |
| Beginner | Could a newcomer understand the industry from the atlas? | Every major page has the five beginner sections; glossary covers every term used |

Each failed check becomes a research unit (`origin: gap_finder`) and the loop continues.

## Stop condition (all four, written down in `atlas/00-overview/research-log.md`)

1. Every dimension in `ontology.yaml` is covered and the audit passes.
2. New research produces mostly duplicates: duplicate share over the last 10 batches ≥ `research.stop_when_duplicate_share_above` in config.yaml, and the last gap-finder pass proposed no P0/P1 units.
3. Remaining unknowns need proprietary or interview data (they are in the interview queue).
4. The marginal value of more desk research is low, stated with the numbers above.
