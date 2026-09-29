# Information flows: what data moves between participants, in which systems

> Scope: the information generated along the chip value chain (design data, manufacturing and test data, demand signals, market statistics, regulatory data), who holds it and where it goes. Period: as of 2026-09-29. Geography: global.
> Built from research unit RU-0001 (mainly the technology lens, plus definition and regulation). Planner run `plan0-9c2e`.

**Evidence status.** All claims are unverified (low confidence). Much of the detail comes from companies describing their own systems (`reported_claim`, e.g. TSMC's portal). Flows marked **unknown** were not evidenced.

## What this means

Making a chip means passing a very large, very sensitive design between companies. The design goes to a mask shop and then to a fab. The fab and the test floors send data back about how the wafers came out. Separately, demand forecasts and orders travel up the chain. Officially, sales data flow to a statistics body that publishes the market size.

## Why it matters

- **Design data is the industry's most closely guarded IP.** Photomasks are made from each customer's confidential designs [CLM-0529]. Chip-design software is itself export-controlled [CLM-0409].
- **Manufacturing data decides yield**, and yield decides cost. Foundries share some of it and keep the rest [CLM-0451].
- **Demand information is poor.** GAO's experts said firms are reluctant to share information, so real demand is hard to see [CLM-0460]. In the 2021 shortage, median buyer inventory fell from 40 days to under 5 [CLM-0462].

## How it works

```mermaid
sequenceDiagram
  participant FND as Foundry
  participant DES as Designer (fabless / IDM / system co.)
  participant EDA as EDA / IP vendors
  participant MSK as Mask shop
  participant FAB as Fab (MES, FDC)
  participant BE as Wafer sort / OSAT / final test
  FND->>EDA: process tech files; certifies flows, validates IP
  FND->>DES: PDK (design rules, models, cell libraries) via portal
  EDA->>DES: tools, IP deliverables
  DES->>FND: tape-out: layout (GDSII/OASIS) via secure portal
  DES->>MSK: mask data (confidential design)
  MSK->>FAB: mask set (physical plates)
  FAB->>FAB: equipment data via SECS/GEM to host; FDC sensor data; lot genealogy in MES
  FND->>DES: WAT/PCM, wafer yield, lot status (3x/day), quality & reliability
  BE->>BE: wafer maps (SEMI E142) sort -> assembly -> final test
  BE->>DES: test results (STDF) to yield/product engineering
  Note over DES,FND: Demand forecasts / orders / allocation: format & system unknown
```

### Flow table

| Producer → consumer | What information | System / format | Status | Evidence |
|---|---|---|---|---|
| Foundry → designers | PDK: design rules, device models, cell libraries, EDA tech files | Foundry portal; PDK bundle | Contents evidenced (open SKY130 PDK). **Access terms unknown** | [CLM-0418] [CLM-0419] [CLM-0464] (INT-0016) |
| Foundry → EDA and IP vendors | Process files; certification of tool flows; silicon validation of IP | Foundry ecosystem programme (e.g. TSMC OIP) | Evidenced (TSMC describing itself) | [CLM-0420] |
| EDA/IP vendor → designer | Software and licensed design blocks | Licence deliverables | Evidenced; formats **unknown** | [CLM-0414] [CLM-0475] |
| Designer → foundry / mask shop | Final layout at tape-out | GDSII or OASIS (SEMI P39); secure transfer through the foundry portal | Evidenced | [CLM-0421] [CLM-0422] [CLM-0457] [CLM-0425] |
| Mask shop → fab | Mask set (physical plates); first layers sometimes needed within 24 hours | Mask data conversion; e-beam/laser writers | Evidenced | [CLM-0424] [CLM-0425] [CLM-0426] |
| Process tools → fab host / MES | Equipment state, events, recipes, sensor data (100–200 sensors per tool) | SECS/GEM (SEMI E30); FDC systems | Evidenced | [CLM-0453] [CLM-0450] |
| Fab MES (internal) | Lot and WIP tracking, genealogy, recipes, masks | MES | Evidenced (vendor's own description) | [CLM-0448] [CLM-0449] |
| Foundry → fabless customer | WAT/PCM, wafer yield, pilot lots, quality/reliability data; lot status for fab, assembly, test and shipping, updated 3 times a day | Foundry portal; system-to-system link | Evidenced (TSMC describing itself). **Defect and metrology data usually not shared** (one tier-3 source) | [CLM-0455] [CLM-0456] [CLM-0457] [CLM-0451] |
| Wafer sort → assembly/OSAT → final test | Die-by-die wafer and bin maps | SEMI E142 | Evidenced | [CLM-0454] |
| Testers → yield / product engineering | Test results per lot, wafer, part and test | STDF | Evidenced | [CLM-0447] |
| Chiplet / HBM suppliers → package integrator | Known-good-die test data | **unknown** | The requirement is evidenced; the actual flow is **unknown** | [CLM-0445] [CLM-0434] (INT-0017) |
| OEM ↔ chip supplier ↔ foundry / OSAT | Demand forecasts, orders, allocation | **unknown** (portals? EDI? spreadsheets?) | **unknown**. OSATs buy materials against customer forecasts [CLM-0233], which proves forecasts flow, but not how | [CLM-0460] [CLM-0461] (INT-0014, RU-0039) |
| Chip companies → WSTS | Monthly revenue by product and region | Data-collection agents | Evidenced. **Region-assignment rule unknown** | [CLM-0002] [CLM-0003] [CLM-0080] (INT-0001) |
| WSTS → SIA → public | Monthly sales as a 3-month moving average; forecasts; end-use survey | Press releases, Factbook | Evidenced | [CLM-0006] [CLM-0004] |
| Equipment makers → SEMI / SEAJ | Equipment billings | Member data submission | Evidenced | [CLM-0058] |
| Trusted suppliers ↔ US DoD | Design and manufacturing of sensitive ICs under confidentiality controls | DMEA accreditation | Evidenced (scope only) | [CLM-0458] [CLM-0459] |
| Listed manufacturers → SEC | Origin of conflict minerals | Form SD, annually by 31 May | Evidenced | [CLM-0326] |
| Exporters → BIS | Licence applications for controlled items to China (incl. H200-class chips with third-party testing) | BIS licensing | Evidenced (rules). **Process timelines unknown** | [CLM-0302] [CLM-0308] (INT-0010) |

## Evidence: where data is sensitive, manual or retained

- **Sensitive.** Design layouts and PDKs [CLM-0529] [CLM-0464]; GAAFET design tools are export-controlled [CLM-0409]; defence work requires trusted-supplier handling [CLM-0459].
- **Retained for a long time.** Manufacturing data must be kept for 5–15 years depending on customer and application (vendor estimate) [CLM-0452].
- **Manual steps.** These could not be established from public sources. The most likely candidates are forecast exchange and multi-die failure analysis, and both are in the interview queue (INT-0014, INT-0017).
- **Statistics are indirect.** Trade statistics are a poor guide to where chips are made, because overseas packaging and transshipment distort them [CLM-0010]. Official industry codes bundle chips with other components [CLM-0020].

## What we still don't know

- **PDK access terms** and how design data is protected in transit [CLM-0464].
- **Which foundry data customers actually receive beyond WAT/PCM** (INT-0013). The claim that defect data is withheld rests on a single tier-3 source [CLM-0451].
- **How demand forecasts and capacity reservations are exchanged**, over what horizon and how binding they are (INT-0014, RU-0039).
- **How known-good-die and failure-analysis data move** in chiplet and HBM packages (INT-0017).
- **How WSTS assigns regions** and how it treats non-member companies [CLM-0080] [CLM-0081].
