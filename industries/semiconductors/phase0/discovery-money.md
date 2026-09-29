# Phase 0 discovery: money flows and business models

Run `disc-money-c3f9`, research unit RU-0001, staging batch `RU-0001-disc-money-c3f9`, 2026-09-29.
Every figure below belongs to **one company for one fiscal period**. None is an average for its category. Claims are in the batch and are unverified until a fact-check.

## 1. Participant types and business models found

| Participant type (proposed) | How it makes money | Representative evidence (company, period) | Sources |
|---|---|---|---|
| **Fabless chip company** | Designs chips, sells them to OEMs, ODMs, cloud providers and distributors. Pays foundries for wafers and OSATs for packaging and test. | NVIDIA FY2026: revenue $215.9bn, GAAP gross margin 71.1%, $95.2bn supply commitments. Qualcomm's QCT is fabless and names TSMC, Samsung and GF as foundries and ASE, Amkor, SPIL and STATS as OSATs. | [NVIDIA 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm), [NVIDIA CFO commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26cfocommentary.htm), [Qualcomm 10-K](https://www.sec.gov/Archives/edgar/data/804328/000080432825000085/qcom-20250928.htm), [CRS R47508](https://www.congress.gov/crs_external_products/R/PDF/R47508/R47508.5.pdf) |
| **Foundry (leading-edge)** | Makes wafers to customer designs. Takes customer prepayments ("temporary receipts") to reserve capacity. | TSMC 2025: revenue NT$3,809bn, gross margin 59.9%, capex NT$1,272bn (about 33% of revenue), largest customer 19%, North America 75%. | [TSMC 4Q25 report](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/00fe50f72b38d74e6b9b066398f020f337cd4e9d/4Q25%20Management%20Report.pdf), [TSMC 20-F](https://investor.tsmc.com/sites/ir/sec-filings/2025_20F%20Report.pdf) |
| **Foundry (specialty / mature node)** | Makes wafers. Signs LTAs in which customers commit volume in return for reserved capacity, with penalties for GF if it fails to deliver. | GlobalFoundries 2025: revenue $6.791bn, gross margin 24.9%, 2.345m 300mm-equivalent wafers (about $2,900 revenue per wafer, an upper bound on its wafer price). | [GF 20-F](https://www.sec.gov/Archives/edgar/data/1709048/000170904826000022/gfs-20251231.htm), [GF 4Q25 release](https://www.sec.gov/Archives/edgar/data/1709048/000170904826000012/globalfoundries4q2025earni.htm) |
| **IDM: logic / analog** | Designs and makes its own chips and sells them direct or through distributors. | TI 2025: more than 80% of revenue sold direct, gross margin 57.0%, capex about 26% of revenue. Intel 2025: gross margin 34.8%, gross capex $17.7bn with $4.9bn from partners (SCIP); Intel Foundry had an operating loss of $10.3bn. | [TI 10-K](https://investor.ti.com/static-files/7a676084-0b6d-479d-80bb-b193f27135f4), [Intel Q4 release](https://www.intc.com/filings-reports/all-sec-filings/content/0000050863-26-000009/q425earningsrelease.htm) |
| **IDM: memory** | Makes commodity-like DRAM and NAND. Prices in LTAs are renegotiated periodically. | Micron FY2025: gross margin 39.8%, gross capex about 42% of revenue. Annual DRAM average selling prices moved by roughly ±40% over five years. | [Micron 10-K](https://www.sec.gov/Archives/edgar/data/723125/000072312525000028/mu-20250828.htm), [Micron FY25 release](https://www.globenewswire.com/news-release/2025/09/23/3155077/14450/en/Micron-Technology-Inc-Reports-Results-for-the-Fourth-Quarter-and-Full-Year-of-Fiscal-2025.html) |
| **EDA vendor** | Sells time-based licences and subscriptions (mostly network licences), upfront licences for some products and hardware, and maintenance. | Synopsys FY2025: $3.49bn time-based, $2.01bn upfront, $1.55bn maintenance; R&D about 35% of revenue. Cadence FY2025: 80% recurring revenue, GAAP gross margin 86.4%. | [Synopsys 10-K](https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm), [Synopsys release](https://news.synopsys.com/2025-12-10-Synopsys-Posts-Financial-Results-for-Fourth-Quarter-and-Fiscal-Year-2025), [Cadence CFO commentary](https://s206.q4cdn.com/597110084/files/doc_financials/2025/q4/Q4-2025-CFO-Commentary-FINAL.pdf) |
| **Semiconductor IP licensor** | Charges multi-year licence fees plus a royalty on every chip that contains its IP. Synopsys design IP is charged per design, sometimes with royalties. | Arm FY2026: royalties $2.61bn, licensing $2.31bn. | [Arm annual report](https://investors.arm.com/static-files/219a3b28-f209-4d74-8bc6-f9e026d55a95), [Arm results](https://newsroom.arm.com/news/arm-q4-fye26-results) |
| **Patent licensor (device-level)** | Charges a royalty equal to a percentage of the device's wholesale price, with caps and minimums, paid quarterly by OEMs. | Qualcomm QTL. | [Qualcomm 10-K](https://www.sec.gov/Archives/edgar/data/804328/000080432825000085/qcom-20250928.htm) |
| **Equipment maker** | Sells systems, plus services, upgrades and spares to the installed base, much of it as subscriptions. | ASML 2025: sales €32.7bn, of which installed base €8.2bn; gross margin 52.8%; R&D about 14% of sales; capex about 5%. Applied Materials FY2025: services $6.4bn of $28.4bn, more than two-thirds of service revenue from subscriptions. Market: $135.1bn of equipment billings in 2025. | [ASML release](https://www.asml.com/en/news/press-releases/2026/q4-2025-financial-results), [ASML AR](https://www.asml.com/en/investors/annual-report/2025/financials), [AMAT release](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-fourth-quarter-and-fiscal-year-2025/), [AMAT remarks](https://ir.appliedmaterials.com/static-files/4d5a62a2-1796-4d11-ae7c-848c1ed7ea27), [SEMI](https://www.semi.org/en/SEMI-Reports-Global-Semiconductor-Equipment-Billings-Reached-135-Billion-in-2025) |
| **OSAT** | Packages and tests chips as a service. Customer wafers are consigned (the customer keeps title). Customers give no binding volume commitments but pay for unused materials bought to their forecasts. High fixed costs. | Amkor 2025: gross margin 14.0%, top 10 customers 72% of sales (Apple 29.8%). ASE 2025: gross margin 17.7% overall and 23.5% in ATM; equipment capex $3.4bn. | [Amkor 10-K](https://www.sec.gov/Archives/edgar/data/1047127/000104712726000014/amkr-20251231.htm), [Amkor release](https://ir.amkor.com/news-releases/news-release-details/amkor-technology-reports-financial-results-fourth-quarter-and-11), [ASE release](https://www.prnewswire.com/news-releases/ase-technology-holding-co-ltd-reports-its-unaudited-consolidated-financial-results-for-the-fourth-quarter-and-the-full-year-of-2025-302679779.html) |
| **Franchised distributor** | Buys and resells, earning a margin. Supplier agreements protect it against price erosion and obsolescence and give it return rights. | Avnet FY2025: gross margin 10.7%, semiconductors 78% of sales. Microchip sold 45% of FY2025 sales through distributors; TI sold less than 20%. | [Avnet 10-K](https://www.sec.gov/Archives/edgar/data/8858/000000885825000028/avt-20250628x10k.htm), [Microchip 10-K](https://ir.microchip.com/sec-filings/all-sec-filings/content/0000827054-25-000077/mchp-20250331.htm) |
| **Governments** | Pay grants, loans and tax credits, and now hold equity. | US CHIPS Act: $39bn appropriated; up to $30.7bn awarded to 19 companies by January 2025, paid out on milestones; 48D tax credit of 35%. Germany: up to €5bn to ESMC. US government took 9.9% of Intel. | [CRS R49031](https://www.everycrsreport.com/files/2026-07-14_R49031_157331cbaf561ee49780ef5b60b2f38407b33cde.html), [26 USC 48D](https://uscode.house.gov/view.xhtml?req=%28title%3A26+section%3A48D+edition%3Aprelim%29), [EC ESMC](https://digital-strategy.ec.europa.eu/en/news/commission-approves-eu5-billion-german-state-aid-measure-support-esmc-setting-new-semiconductor), [Intel 8-K](https://www.sec.gov/Archives/edgar/data/50863/000005086325000129/a08222025form8-kex991.htm) |

In the companies sampled, gross margins run from about 11% (distributor) and 14% (OSAT), through 25–60% (foundries, IDMs and equipment makers), to 71% (fabless) and 86% (EDA). This is a reading of about a dozen companies, not a set of category norms. RU "Cross-model financial benchmark" is proposed to test it.

## 2. Money-flow edges (payer → payee: for what, basis)

| Payer → payee | For what | Basis | Status |
|---|---|---|---|
| Fabless → foundry | Wafers made to the customer's design | Priced per wafer (assumed). Capacity is secured through prepayments, deposits or premiums and LTAs. | **Partly evidenced.** The relationship and the prepayments are evidenced (TSMC, NVIDIA, GF). The per-wafer price basis and actual prices are **unknown**. |
| Fabless → OSAT | Packaging and test of consigned wafers | Service fee. Customers bear the cost of unused materials; no binding volumes. | **Evidenced (Amkor).** Pricing unit (per unit, per package) **unknown**. |
| Chip designers (fabless, IDM, foundry) → EDA vendor | Design software | Time-based licences, subscriptions, upfront licences, maintenance | **Evidenced (Synopsys, Cadence).** Seat prices **unknown**. |
| Chip designers → IP licensor | Right to use design blocks | Licence fee (per design or multi-year) plus a royalty per chip | **Evidenced (Arm, Synopsys).** Royalty rates **unknown**. |
| Device OEMs → patent licensor | Patent rights | Percentage of the device's wholesale price with caps and minimums, paid quarterly | **Evidenced (Qualcomm).** |
| Foundries, IDMs, OSATs → equipment makers | Tools, upgrades, service | Capital purchase plus service subscriptions | **Evidenced (ASML, AMAT, SEMI).** Down payments on tools **unknown**. |
| Chipmakers → distributors → OEMs | Components | Distributor buy/resell margin, with supplier price and obsolescence protection | **Evidenced (Avnet).** Ship-and-debit mechanics **unknown**. |
| OEMs, cloud providers → chipmakers | Chips | Direct sales or through distributors | **Evidenced** (TI direct share, Microchip distributor share, NVIDIA partner network). |
| Chip vendor → cloud providers | Cloud capacity | Multi-year cloud service agreements ($27bn at NVIDIA) | **Evidenced (NVIDIA).** Purpose not detailed. |
| Governments → fabs (US, Germany) | Building fabs | Milestone-reimbursed grants, loans, a 35% investment tax credit with direct pay, and equity (Intel) | **Evidenced** (CRS, statute, filings, EC). |
| Governments → fabs (Japan, Korea, China, Taiwan, India) | Same | Same | **Unknown.** The METI fetches returned empty pages. |
| Financial investors → IDM fabs | Co-funding fab capex for minority stakes | SCIP partner contributions ($4.9bn net at Intel in 2025) | **Evidenced (Intel).** Deal terms **unknown**. |
| Suppliers of materials, wafers, gases, chemicals → fabs | Inputs | Not researched | **Unknown** (outside this pass). |

**Working capital and risk.** Foundries get cash in advance through prepayments. Fabless buyers commit to non-cancellable orders and pay premiums when supply is tight. OSATs carry high fixed costs, have no backlog and depend on utilisation. Distributors hold inventory but are protected by suppliers.

**Cyclicality.** The cycle shows in several places:
- Market sales fell 8.2% in 2023 and rose 25.6% in 2025 (SIA/WSTS).
- Memory swung hardest: down about 29% in 2023 by WSTS figures, or 37% by Gartner's estimate.
- DRAM average selling prices moved by roughly ±40% a year.
- Microchip's sales fell 42% in FY2025 during an inventory correction.
- Avnet's inventory relative to sales was elevated.
- GF's LTAs were stretched over longer commitment periods.

SIA reports that R&D and capex as a share of sales have not moved with the cycle for US firms.

## 3. Key terms (in the glossary)

Fabless, foundry, IDM, OSAT, EDA, semiconductor IP, licence fee, royalty, time-based licence, wafer, 300mm-equivalent wafer, gross margin, capital intensity, R&D intensity, capex, long-term agreement (LTA), capacity reservation, temporary receipts, take-or-pay (defined, but not found under that name in the filings), consigned wafer, installed base management, franchised distribution agreement, price protection, distribution inventory days, backlog, CHIPS Act, 48D advanced manufacturing investment credit, direct pay, SCIP, equipment billings, inventory correction, ATM, EMS.

## 4. Proposed follow-up research units (origin: researcher_discovery, from RU-0001)

1. Foundry commercial terms: wafer pricing, LTAs and capacity prepayments (P0, unit_economics)
2. Memory business model and price cycle (P0, dynamics)
3. Distribution channel economics (P1, business_models)
4. Government money flows into semiconductors by country (P1, capital)
5. Equipment makers' commercial model: systems, services, down payments (P1, business_models)
6. Packaging and test value pool, including advanced packaging (P1, unit_economics)
7. Cross-model financial benchmark on consistent periods (P1, unit_economics)
8. Design-IP and patent-licensing royalty economics (P2, business_models)

**Suggested entity types for ontology.yaml.** Each is evidenced in the batch: fabless_company, foundry, idm, osat, eda_vendor, ip_licensor, patent_licensor, equipment_maker, distributor, government_funder. A co_investor or financial-partner type may also be needed (Intel SCIP).

## 5. What could not be established

- **Foundry wafer prices by node and the pricing method.** Not stated in the TSMC 20-F; no GF ASP found.
- **Customer-prepayment balances** at TSMC and GF, and **ASML down payments**. The fetch tool did not return the financial-statement notes.
- **Distributor ship-and-debit and stock-rotation mechanics**, and OSAT pricing units.
- **Some R&D figures.** TSMC and NVIDIA R&D were not extracted.
- **Other governments.** Subsidy amounts for Japan, Korea, China, Taiwan and India were not found. The METI pages returned empty, and the shared web-search budget (200 calls) ran out.
- **Items to verify at fact-check:**
  - The Cadence revenue unit was rendered as "$5,297 billion"; it is read as millions.
  - The SIA memory sentence says "in 2024" in the 2025 release.
  - The Intel R&D line may include MG&A.
  - Several table figures were extracted by the fetch tool's summariser rather than quoted verbatim.
