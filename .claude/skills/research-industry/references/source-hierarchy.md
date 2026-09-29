# Source hierarchy and search tactics

## Tiers

**Tier 1: primary.** Governments, regulators, legislation and official gazettes, official statistics, court/tribunal records, company filings (10-K/20-F/annual reports, exchange filings), investor presentations and earnings transcripts published by the company, official product documentation, industry bodies and standards organisations.

**Tier 2: high-quality secondary.** Reputable research firms (often paywalled; public summaries/press releases are usable and must be labelled as such), peer-reviewed academic work, established financial press, specialist industry press.

**Tier 3: discovery.** News, blogs, startup databases, forums, social media, aggregators, encyclopedias. Use these to *find* things, then trace the claim to tier 1/2. Anything important that rests only on tier 3 stays low confidence.

## Rules

1. **Go to the origin.** If an article cites a report, open the report. If a report cites a statistic, find the statistical release. Cite what you actually read.
2. **Marketing is a reported claim.** A company describing itself ("leading", "fastest", "X customers") is `reported_claim`, even on its own official site.
3. **Estimates are estimates.** Market sizes from research firms or associations are `estimate`, with the method recorded. Two firms' market sizes usually measure different populations, so check before calling it a contradiction.
4. **Dates matter.** Record the publication date and the period the data describes. Label historical data as historical.
5. **Paywalls.** Do not cite the contents of a paywalled report you could not read. You may cite a publicly released summary or press release (cite *that* URL) and mark `paywalled: true` on the full report if it is listed as a key document.
6. **Geography.** Record the geography of every number. Never merge figures from different geographies without saying so.

## Search tactics (tools in this environment)

- **WebSearch** to find candidates; prefer queries that target primary sources: `site:gov`, `site:europa.eu`, `site:sec.gov`, `"annual report" filetype:pdf`, the regulator's name, the association's name.
- **WebFetch** returns a *summary made by a smaller model*, not the raw page. Always ask it for the specific fact **and a verbatim quote** of the supporting passage with its location. If it cannot quote, treat the evidence as a paraphrase.
- Use WebSearch/WebFetch for all web access, not curl/requests from the shell (in cloud sessions the shell is blocked from most sites anyway).
- For pages WebFetch cannot render, or pages that need a login the user has, note it for the orchestrator; a browser may be available.
- Follow references: glossary terms, cited reports, named regulators and companies are leads for new claims and new research units.

