# RU-0226 notes (res-RU-0226-4248)

## Enumeration sources by jurisdiction (as checked 2026-10-01)

| System | Operator | Filings | Language | Access | Semiconductor code usable to enumerate | Official count found |
|---|---|---|---|---|---|---|
| SEC EDGAR | US SEC | 10-K/10-Q/8-K; 20-F/6-K for foreign issuers; XBRL | English | Free, keyless JSON APIs + nightly bulk ZIP; undeclared bots blocked | SIC 3674 (misses Lam/ASML 3559, KLA 3827, Teradyne 3825, Entegris 3089, EDA 7372, Avnet 5065) | Not obtained (paging blocked) |
| MOPS / e-MOPS | TWSE + TPEx under FSC | Monthly revenue (before 10th), quarterly (45 days), annual (3 months) | Chinese + English UI | Free web; static monthly HTML tables | Industry group 24 "Semiconductor Industry" | 91 TWSE + 111 TPEx + 34 ESB = 236 stocks |
| DART / OpenDART | Korea FSS | Periodic reports, XML originals, XBRL | Korean (+English portal) | API key (40 chars), ~20k calls/day | induty_code field (classification not confirmed) | Not found |
| EDINET | Japan FSA | Annual + half-year securities reports (quarterly abolished Apr 2024) | Mostly Japanese | API v2 with key | None in JPX 33 sectors (Electric Appliances 3650 etc.) | Not applicable |
| CNINFO / SSE / SZSE | CSRC-designated | Annual (4 mo), interim (2 mo), quarterly (1 mo) | Chinese prevails | Free web, JS-heavy | CAPCO classification (major class only) | STAR IC: 119 (Jun 2025, SSE); 128 (2026, news) |
| HKEXnews | HKEX | Annual (4 mo, English + Chinese), prospectuses, DI notices | English + Chinese | Free web | HSICS 703010 / 703020 | Not found |
| AFM register | Dutch AFM | Annual + semi-annual reports | English/Dutch | Free register | None | — |
| TASE MAYA | TASE / ISA | All filings | Hebrew; English voluntary | Free web | Not checked | — |
| NSE/BSE | NSE Indices | — | English | Free PDF | None (no semiconductor basic industry, Jul 2023) | Not found |

## Tooling issue found
`irs.merge._find_existing` matches entities/glossary by normalised name or alias. Aliases written only in CJK script (e.g. "公開資訊觀測站") normalise to the empty string, so every such record "matches" every other one and gets silently merged. I moved CJK-only aliases into the description text to avoid this. Suggest fixing `_name_keys` to drop empty keys.

## Tier note
The merge tool does not fill in `tier` for sources, although the schema requires it. I set it from `irs/rules.py` TIER_BY_TYPE (same as earlier merged batches).
