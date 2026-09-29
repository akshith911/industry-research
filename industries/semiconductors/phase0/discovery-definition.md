# Phase 0 discovery: industry definition, boundaries and segmentation

Run: `disc-def-a1c4` · Research unit: RU-0001 · Date: 2026-09-29 · Batch: `staging/RU-0001-disc-def-a1c4/`

Every statement below is backed by a claim in the batch. Figures are nominal USD.

## 0. The boundary in one paragraph

The "semiconductor market" quoted in headlines (about US$0.8tn in 2025, forecast at US$1.51tn for 2026) is the **WSTS** figure. It counts sales of finished chips (packaged and tested, or tested die and wafers) in four groups: **integrated circuits** (logic, memory, analog, micro), **discretes**, **optoelectronics** and **sensors/actuators**. It does **not** count equipment (US$135bn, SEMI), materials (US$73bn, SEMI), EDA and IP software (about US$5.5bn a quarter, ESD Alliance) or LCD panels. Pure-play foundry revenue is most likely not counted separately: chips are counted when the company that designed them sells them. This is an inference we still need to confirm. Official industrial classifications (ISIC 2610, NAICS 334410) are **wider**. They put chips together with capacitors, printed circuit boards, display components and, in NAICS, solar cells. US CHIPS law, by contrast, treats equipment and materials as part of the industry.

## 1. Participant (entity) types found, for the ontology

| Proposed type id | One-line description | Evidence (URLs opened) |
|---|---|---|
| `idm` | Integrated device manufacturer: designs, fabricates, packages and tests its own chips | https://semiconductor.samsung.com/news-events/tech-blog/from-foundry-to-fabless-an-overview-of-the-semiconductor-ecosystem/ ; https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2024-08/5122725a56670882d777a8e8bfe0ed247cc55330/TSMC%202Q24%20Transcript.pdf |
| `fabless_company` | Designs and sells own-brand chips; outsources manufacturing | Samsung URL above; https://legacy.trade.gov/topmarkets/pdf/Semiconductors_Executive_Summary.pdf |
| `foundry` | Contract wafer manufacturer for other companies' designs | Samsung URL; https://www.trendforce.com/presscenter/news/20260312-12965.html ; TSMC 4Q25 report https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/00fe50f72b38d74e6b9b066398f020f337cd4e9d/4Q25%20Management%20Report.pdf |
| `design_house` | Design-services intermediary between fabless firms and foundries | Samsung URL |
| `osat` | Outsourced semiconductor assembly and test (back-end services) | Samsung URL; SEMI equipment back-end segments https://www.semi.org/en/SEMI-Reports-Global-Semiconductor-Equipment-Billings-Reached-135-Billion-in-2025 |
| `ip_vendor` | Licenses pre-designed chip blocks and cell libraries for fees or royalties | Samsung URL; https://www.semi.org/en/semi-press-release/esd-alliance-reports-electronic-system-design-industry-posts-5.5-billion-dollars-in-revenue-in-q4-2025 |
| `eda_vendor` | Sells chip and board design software (CAE, physical design and verification) | ESD Alliance URL above |
| `equipment_supplier` | Makes front-end (wafer processing) and back-end (test, assembly) manufacturing equipment | SEMI equipment URL; https://uscode.house.gov/view.xhtml?req=%28title%3A15+section%3A4651+edition%3Aprelim%29 |
| `materials_supplier` | Supplies wafer-fab materials (photomasks, photoresist, wet chemicals, wafers) and packaging materials (substrates, bonding wire) | https://www.semi.org/en/semi-press-release/global-semiconductor-materials-market-revenue-reaches-record-73.2-billion-dollars-in-2025-semi-reports ; SIA SOI 2025 https://www.semiconductors.org/wp-content/uploads/2025/07/SIA-State-of-the-Industry-Report-2025.pdf |
| `mask_maker` | Makes photomasks (TSMC counts it in "Foundry 2.0"; SEMI counts photomasks as a material) | TSMC 2Q24 transcript; SEMI materials URL |
| `industry_association` | Trade bodies that publish the reference statistics and lobby (SIA, SEMI, ESD Alliance, SEAJ, ESIA) | https://www.semiconductors.org/global-annual-semiconductor-sales-increase-25-6-to-791-7-billion-in-2025/ ; SEMI URLs |
| `statistics_body` | Collects member sales data and publishes the market statistic (WSTS) | https://www.wsts.org/61/OVERVIEW ; https://www.wsts.org/61/MARKET-STATISTICS |
| `market_research_firm` | Publishes independent market estimates (Gartner, TrendForce) | https://www.gartner.com/en/newsroom/press-releases/2026-01-12-gartner-says-worldwide-semiconductor-revenue-grew-21-percent-in-2025 ; TrendForce URL |
| `government_funder_regulator` | Grants incentives and sets rules, e.g. US Department of Commerce CHIPS guardrails | https://www.ecfr.gov/current/title-15/subtitle-B/chapter-II/subchapter-C/part-231/subpart-A ; USC URL |
| `statistical_classification_authority` | Maintains industry and trade codes (UNSD for ISIC, Statistics Canada and US Census for NAICS, WCO/Census for HS) | https://unstats.un.org/unsd/classifications/Econ/Structure/Detail/EN/27/2610 ; StatCan NAICS URL ; https://www.census.gov/foreign-trade/schedules/b/2022/c85.html |
| `end_market_customer` | Buyers of chips, grouped by end use: computer, communications, consumer, automotive, industrial, government/military | https://www.semiconductors.org/wp-content/uploads/2025/05/2025-SIA-Factbook-FINAL-1.pdf ; SIA 2023 end-use URL |

Types that probably exist but that I did **not** evidence in this pass: distributors (resale of chips), system companies that design custom chips in-house (for example hyperscalers), wafer (substrate) makers as a separate type, and standards bodies (JEDEC and others).

## 2. Key terms (all are in the glossary batch)

Semiconductor · integrated circuit · discrete · optoelectronics · sensors/actuators · logic · memory · DRAM · NAND flash · HBM · analog IC · micro (MPU/MCU/DSP) · DAO · WSTS · three-month moving average · end use · fabless · IDM · foundry · Foundry 2.0 · OSAT · semiconductor IP · EDA/ESD · semiconductor manufacturing equipment (front-end, back-end) · semiconductor materials · process node · legacy semiconductor · NRE · advanced packaging.

## 3. Segmentations found

- **Product (WSTS):** discretes, optoelectronics, sensors, and ICs split into analog, micro, logic and memory. There are 205 revenue categories in all. In 2025: logic US$299.5bn, memory US$230.0bn, analog US$86.5bn, micro US$84.9bn, opto US$43.0bn, discretes US$30.7bn, sensors US$20.9bn. In 2026 memory is forecast at about US$804bn, more than half of the market.
- **Region by where chips are sold (WSTS):** Americas, Europe, Japan, China, Asia Pacific/All Other in the monthly data. The forecasts use only four regions, with China inside Asia Pacific. The rule WSTS uses to assign a sale to a region is not public.
- **Region by where the selling company is headquartered (SIA):** US-headquartered firms had 50.4% of 2024 sales. This is a different quantity from the "Americas" regional market.
- **End use (WSTS End Use Survey, annual):** PC/computer (34.9% in 2024), communications, consumer, automotive, industrial, and government (which includes military). The exact 2024 shares for the middle four are not yet confirmed (see section 5).
- **Process node:** the TSMC split (3nm, 5nm, 7nm … 0.25µm) and the SIA/BCG capacity buckets (<10nm, 10–22nm, 28nm+, plus DRAM, NAND and DAO). US regulation sets "legacy" at 28nm or older for logic, DRAM with half-pitch above 18nm, and NAND below 128 layers. Node names are labels, not measurements.
- **Business model:** IDM, fabless, foundry (pure-play vs TSMC's Foundry 2.0), design house, OSAT, IP vendor, EDA vendor.
- **Value chain stage (CFR 231.116 and SEMI):** wafer production, then fabrication (front end), then packaging and test (back end). Design, EDA/IP, equipment and materials sit upstream.

## 4. Proposed follow-up research units (in the batch as `research_units`)

1. Market-sizing methodology: WSTS vs Gartner vs other publishers (P0)
2. End-market segmentation and the 2025–2026 AI/memory surge (P0)
3. Foundry market: definitions (pure-play vs Foundry 2.0), size and shares (P1)
4. Semiconductor manufacturing equipment: segments, size and geography (P1)
5. Assembly, test and advanced packaging (OSAT and in-house) (P1)
6. Official statistics mapping: NAICS, ISIC/NACE, HS codes and their limits (P1)
7. Semiconductor materials: segments and suppliers (P2)
8. EDA and semiconductor IP market (P2)
9. Boundary industries: displays, solar PV, passive components, PCBs and EMS (P2)

## 5. What I could not establish

- **How WSTS assigns sales to regions** (ship-to, bill-to or customer headquarters) and **how it treats non-member companies**. Neither is stated on its public pages. Added to the interview queue.
- **How foundry output and captive/custom chips are treated** in WSTS and Gartner totals. The foundry exclusion is an inference from WSTS's membership rule and a 2016 ITA footnote, not an explicit statement. Added to the interview queue.
- **Whether solar/PV cells are in the WSTS market.** The 2021 classification did not mention them. The 2023+ classification is behind SIA's subscriber login.
- **Exact 2024 end-use shares** for communications, consumer, automotive and industrial. The WebFetch tool mapped the values 33.0, 12.7, 9.9 and 8.4% to different labels on different calls. Someone needs to read the chart directly (SIA Factbook p.8, SIA SOI p.24).
- **The US NAICS 334413 and 333242 official text.** The census.gov pages are rendered by JavaScript and the NAICS manual PDF came back truncated. The EU Chips Act (Regulation 2023/1781) Article 2 definitions, OECD and CRS reports were blocked by robots.txt.
- **Why WSTS and Gartner differ on 2024** (US$630.5bn vs US$655.9bn), and why Gartner revised its 2024 figure from US$626bn to US$655.9bn. The public releases give no methodology.
- **Business-model shares** (for example the fabless share of IC sales) and the **OSAT market size**. Not researched because the web-search budget ran out.
