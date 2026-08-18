# Dimension 07 — Data Fragmentation & Weak Decision-Context Capture (Downstream Refining & Marketing)

**Study context:** Value Chain Optimization (VCO), lookback/backcasting, and CI knowledge management for a downstream refining & marketing organization.
**Research date:** 2026-07-18. **Method:** 35 web queries across industrial data management literature, vendor whitepapers, ARC Advisory, academic papers, consultancies (≥15 independent searches; several zero-result queries re-phrased).
**Scope:** (1) typical downstream system stack and siloing evidence; (2) inconsistent keys/taxonomy/semantics and standards adoption gaps; (3) capture of decision context/rationale; (4) quantified impacts.

---

## Key Findings

1. **The downstream stack is structurally fragmented by design.** Data lives in SCADA/DCS, CMMS/EAM, engineering document systems, ERP, LIMS, terminal automation, ETRM, and POS/retail systems that "operate independently, with little to no integration" [^8^][^10^]. OT was built for uptime and safety, IT for transactions; the ISA-95 Level 3/Level 4 boundary is where translation chronically fails [^9^]. Historians (AVEVA/OSIsoft PI, AspenTech IP.21, Honeywell Uniformance) hold 10–20 years of operational data but are "completely isolated from modern analytics platforms" [^9^].
2. **No consistent keys or semantics across systems.** Asset hierarchies conflict between systems ("pump tags vs. P&ID diagrams") [^17^]; each organization keeps its own reference data libraries requiring translation at every handover [^21^]. Competing standards (ISO 15926 vs. MIMOSA OSA-EAI/CCOM) split the industry by vendor camp, and ISO 15926's Reference Data Library remains incomplete; adoption of lifecycle information standards "has been limited and the industry remains fragmented" [^19^][^20^][^22^].
3. **Decision context is systematically lost.** Decision rationale, assumptions and trade-offs live in unstructured artifacts — emails, meeting threads, paper logbooks, operators' heads — which is why oil & gas staff spend up to 80% of time searching unstructured data (vs. 30% cross-industry per IDC) [^4^]. ~80% of O&G logbooks are unstructured [^26^]; "how decisions were made, what details were noticed, and what options were considered" are captured, if at all, only in ad-hoc written summaries [^4^]. Structured "decision record" practice (ADRs/decision logs) is mature in software engineering but essentially absent from industrial planning/operations; even in software, practitioners warn "documenting decisions is not the same as governing them" [^27^][^29^].
4. **Quantified impacts are large and consistently directional.** Petroleum engineers/geoscientists spend >50% of time searching and assembling data [^3^]; only 32% of enterprise data is put to work (68% unleveraged — Seagate/IDC) [^33^]; on a typical oil rig only 1% of data from 30,000 sensors is examined, and that only for anomaly detection, not optimization (McKinsey) [^12^]; poor data quality costs ~$12.9M/yr per organization (Gartner) and ~$3.1T/yr in the US (IBM, 2016 — methodology questioned) [^14^][^15^]; refinery material imbalances of 1.5–2% on a 250 kbpd site are worth up to $5M/yr when closed by 0.5% [^35^]; manual tank-reading variations cause up to 3% inventory reconciliation differences, "millions in unexplained losses annually" [^37^].
5. **"Data contextualization" is the vendor-industry answer and an active market battleground.** Cognite and AVEVA define contextualization as continuously linking raw data to the physical/logical entities, relationships and workflows that produced it, building an "industrial knowledge graph" [^5^][^6^][^23^]. The Schneider/AVEVA–Cognite combination signals consolidation of the contextualization layer, raising portability/lock-in concerns [^25^]. Contextualization as practiced today covers *data* context (asset, condition, event) — **not decision context** (rationale, alternatives, assumptions); that remains an open gap directly relevant to lookback/backcasting.

---

## 1. The Typical System Stack: Evidence on Siloing & Integration Difficulty

### 1.1 The stack is fragmented across OT, ET and IT

> "A common and significant hurdle is the problem of data silos. In a typical facility, critical data is scattered across multiple, disconnected systems: Operational data lives in SCADA and DCS systems. Maintenance data is in the CMMS/EAM. Engineering data (P&IDs, datasheets) is in a document management system. Financial data is in the ERP. Lab data is in a LIMS. To perform any meaningful analysis, this data must be brought together."
— F7i.ai, "Oil & Gas Asset Management 2026: 7 Strategies for Profitability," 2025-07-16 [^8^]

> "OT was built for uptime and safety, not data sharing. Information Technology, SAP, Oracle ERP, CRM, WMS, was built for transactional business data. These two worlds almost never communicate in real time. That's by design. The ISA-95 model... defines exactly where this translation happens: between Level 3 (MES) and Level 4 (ERP/analytics)... The result: a maintenance engineer cannot correlate a quality defect with the specific machine parameter that caused it, because the data lives in systems that have never been connected."
— Kanerika, "Data Lakehouse for Manufacturing: What Actually Works," 2026-06-15 [^9^]

> "Most process manufacturers store 10 to 20 years of machine data in proprietary historians, OSIsoft PI (now AVEVA PI), AspenTech IP.21, or Honeywell Uniformance. These systems are deeply embedded and irreplaceable operationally. They are also completely isolated from modern analytics platforms."
— Kanerika, 2026-06-15 [^9^]

> "Data Silos: OT data locked in proprietary historians, inaccessible to IT analytics. Legacy System Hurdles: Incompatibility between PLC/DCS protocols and modern IT platforms."
— Infosys Engineering Services blog, "Reimagining Manufacturing Operations Through Agentic AI Led IT–OT Integration" [^10^]

> "Emissions monitors and ESG reporting tools... often remains disconnected from operational and financial systems... These systems typically operate independently, with little to no integration. As a result, manufacturers face missed opportunities for optimization, duplicated efforts in reporting, and significant delays in decision-making."
— Greenovative, "From Siloed to Smart: Unifying Energy Data for Industrial Efficiency," 2025-09-19 [^11^]

### 1.2 Terminal automation / logistics layer

> "Interoperability challenges arise from vendor proprietary systems that resist integration with competitor platforms, creating system silos that reduce operational visibility... Legacy equipment incompatibility requires middleware solutions and custom integration development... Data format standardization remains incomplete... API limitations restrict integration between terminal automation systems and enterprise resource planning systems... Open standards including OPC Unified Architecture (OPC UA) and IEC 62541 are gradually improving interoperability, but adoption remains incomplete across petroleum terminal market segments and geographic regions."
— Dataintelo, Oil and Gas Terminal Automation Market report [^13^]

### 1.3 Trading/commercial layer (ETRM/CTRM)

> "We help clients build robust energy data strategies that enable: Centralized trade and risk data models; Integration of structured and unstructured data; Elimination of data silos and reconciliation bottlenecks; Establishment of governance, lineage, and audit-ready controls."
— MidDel Consulting, ETRM/CTRM consulting services page, 2025-05-30 [^16^]
*(Vendor positioning that itself evidences the prevalence of silos and reconciliation bottlenecks across front/middle/back office.)*

### 1.4 Retail/POS layer (marketing)

> "Many of these approved POS systems come with proprietary restrictions on how data flows in and out of the system... This creates data silos that hurt operators in real, measurable ways. You can't get a unified view of your fuel and in-store margins. You can't easily benchmark across locations. You can't plug in best-of-breed inventory management or loss prevention tools because the POS vendor has walled off the data."
— Petrosoft, "How Much Does a C-Store POS System Really Cost?", 2026-03-04 [^18^]

### 1.5 Even "integrated" vendors acknowledge the problem

> "Bring together IT/ET/OT data — Eliminate organizational data silos and foster greater collaboration with a complete view of your industrial data." / "Organize and enrich raw data with relevant properties and metadata..."
— AVEVA, CONNECT Data management product page, accessed 2026 [^23^]

> "The scope and complexity of operational historians has expanded beyond the traditional historians that were primarily deployed on site and managed only real-time data for a particular plant... Historians will continue to evolve and will remain a critical part of the overall operational data architecture along with its integration and interoperability and expansion with enterprise data systems."
— ARC Advisory Group, "The Future of Operational Data Historians" (arcweb.com) [^24^]

---

## 2. Inconsistent Keys / Taxonomy / Semantics; Standards & Adoption Gaps

### 2.1 Master data & asset hierarchy inconsistency

> "Their critical asset information existed in silos, resulting in inconsistent equipment hierarchies between different systems (such as pump tags vs. P&ID diagrams), increasing safety incidents, and growing unplanned downtime. Their complex technology landscape – multiple ERPs, CMMS, SCADA systems, and GIS platforms – created an environment where traditional asset management approaches were failing."
— Data Catalyst case study, "How a major oil & gas operator achieved $25M annual savings through asset data transformation," 2025-10-23 [^17^]

> "Energy companies often have multiple departments, divisions, and geographically dispersed units, each with their own interpretations of data, processes, and sometimes systems... master data gets fragmented and becomes inconsistent across different parts of the organization... Data duplication, outdated records, incomplete information, and inconsistent formats are common issues... Most think that implementing robust enterprise resource planning will solve all master data problems. They find they are sorely mistaken when, after investing millions of dollars in a new accounting system, the data is still bad."
— JPT (SPE), "Data Dilemma: Unraveling the Challenges and Downsides of Data in Oil and Gas," 2023-08-09 [^30^]

> "In the manufacturing industry, every department like procurement, production lines, quality control, inventory management, sales, supply chain, etc has separate databases and systems. That creates isolated data silos, which disrupts the flow of data standardization and integration across enterprises and systems."
— Codasol, "Master Data Management: Process, benefits, and challenges," 2025-07-08 [^31^]

### 2.2 Competing standards — "so many of them"

> "The most significant issue is that different parts of the industry use competing standards for representing engineering assets—ISO 15926, and the MIMOSA Open Systems Architecture for Enterprise Application Integration (OSA-EAI)... engineering companies... generally use ISO15926. With certain exceptions, the maintenance side providers and control systems companies (e.g., IBM/MAXIMO, Microsoft, Rockwell Automation, Emerson, Yokogawa) use MIMOSA. Both sides have a significant code base and marketshare-driven vested interest in maintaining a separate platform."
— "Metamodel-Based Information Integration at Industrial Scale" (ResearchGate full text) [^19^]

> "Inconsistencies also exist in the engineering terminology used by various industry players and individual organizations. Each often have their own reference data libraries (RDLs), requiring this information to also be transformed when communicated during asset information handover... At present, many standard (and non-standard) reference models are used in process industries, but none are all-encompassing."
— Yokogawa, "Delivering Asset Data Integrity through Digitization..." (Gas Processing & LNG, Nov–Dec 2019) [^21^]

### 2.3 Adoption gaps for ISO 15926 / CFIHOS

> "Results obtained from this study show that the standard and its open-source tools are still under development and need some increments and modifications to meet user expectations. In particular, the ISO 15926 Reference Data Library (RDL) is not complete yet."
— Chalmers ODR, "Evaluating interoperability of ISO 15926 implementation" (IFSWorld case study), 2023 [^20^]

> "It was expected that these standards would be adopted by the industry, enabling facility life cycle management. However, due to their complexity, and the industry's current business processes, their adoption has been limited and the industry remains fragmented. For existing facilities coming out of commission, data is typically unstructured, unreliable and incomplete."
— Teesside University, "Information management for decommissioning of Oil & Gas facilities" [^22^]

### 2.4 OPC UA / legacy installed base

> "Legacy systems, which represent 65-70% of installed industrial equipment, increasingly require middleware layers to connect with modern cloud platforms and edge analytics systems." / "The complexity of OPC UA implementations... creates barriers to adoption among organizations lacking IT sophistication."
— MarketIntelo, OPC UA Market Research Report, 2026-06 [^32^]

---

## 3. Capture of Decision Context

### 3.1 Decision rationale lives (and dies) in unstructured data and people's heads

> "Ashild Hanne Larsen, the chief information officer and senior vice president for corporate information technology at Equinor, says that 80% of employee time in the industry is spent looking through unstructured data in order to inform decisions to get work done. The International Data Corporation puts that number at 30% across all industries, so oil and gas is spending nearly three times the general average... For example, how decisions were made, what details were noticed, and what options were considered are commonly recorded by people in written summaries and reports precisely because that unstructured data could be of value the next time a similar issue arises."
— JPT (SPE), "Oil and Gas Has a Problem With Unstructured Data," 2019-07-03 [^4^]

> "If a person does this manually, it takes a lot of time, and the information is probably lost the minute the engineer moves on to the next task." (On an engineer manually tracing a valve's P&ID context, specs, and maintenance history across coding-convention changes.)
— Cognite, "What is contextualization?" (SVP Terje Løken), accessed 2025 [^5^]

> "Structured data tells you what happened; unstructured data tells you why. Meeting transcripts, emails, and documents contain decisions, context, and institutional memory that no dashboard captures... But the decisions that drive those numbers — the email thread where the VP changed the pricing strategy... — live in unstructured data. And most organizations have no systematic way to capture, organize, or learn from it."
— VisionWrights, "Unstructured Data: The 80% You're Ignoring," 2026-04-05 [^34^]

### 3.2 Shift handover / operational logbooks — the frontline decision record

> "Over 40% of plant incidents at U.S. oil and gas facilities occur during start-up, shutdown, and shift change periods — despite those windows accounting for less than 5% of total operational time... Post-incident investigations consistently reveal that the incoming crew lacked knowledge that the outgoing crew possessed... 80% of oil and gas logbooks are unstructured and fail to capture safety-critical information consistently."
— iFactory, "Shift Handover Logbook and Safety Critical Knowledge Transfer," 2026-06-22 [^26^]

### 3.3 "Decision records" practice — mature in software, largely absent in industrial ops

> "An Architectural Decision Record (ADR) captures a single AD and its rationale... The collection of ADRs created and maintained in a project constitute its decision log. All these are within the topic of Architectural Knowledge Management (AKM), but ADR usage can be extended to design and other decisions ('any decision record')."
— adr.github.io (canonical ADR organization site) [^27^]

> "ADRs contain not just the decision, but also a brief rationale for the decision... it's valuable to explicitly list all the serious alternatives that were considered, together with their pros and cons... This kind of decision log creates a valuable historic record that can do much to explain why things are the way they turned out."
— Martin Fowler, "Architecture Decision Record" bliki [^28^]

> "In practice, many organizations discover that documenting decisions is not the same as governing them... Problems tend to appear later — when systems grow, teams change, and the original context begins to fade."
— ReflectRally, "Architecture Decision Records (ADRs): From Documentation to Decision Governance" [^29^]

> "Research shows that architectural knowledge vaporization is a real problem in software projects (Shahin et al., 2014). When important decisions are not documented, teams often rediscover the same problems, repeat past mistakes, or inadvertently violate architectural constraints."
— Marabesi.com ADR guide (citing academic literature), 2025-02-01 [^36^]

**Note for the study:** Decision Quality (DQ) practice *is* institutionalized in oil & gas capital strategy (SDG's multi-decade engagement embedding decision quality at Chevron — framing, scenarios, quantified uncertainties [^38^]), but it operates at the episodic, executive/capital-project level. There is no equivalent routine "decision record" infrastructure for day-to-day planning/scheduling/blending/logistics trade-offs — exactly the decisions a VCO lookback must reconstruct.

### 3.4 What "data contextualization" means in industrial analytics

> "Contextualization is the continuous process of identifying and connecting different pieces of information to show how they relate to each other in the real world." / "In the industrial setting, contextualization is the continuous process of linking and organizing industrial data so it reflects the relationships between equipment, systems, and workflows as they exist on the factory floor, oil rig, refinery, and beyond."
— Cognite, "What is Data Contextualization for AI?", 2025-03-20 [^6^]

> "Data contextualization is the process of adding structure, semantics, and relationships to raw data so it becomes understandable, trustworthy, and usable across analytics, operations, and AI workflows. Without contextualization, even the most advanced plant systems fall into the same trap: disconnected signals, duplicated effort, and insights that never scale."
— TDengine, "Understanding Industrial Data Contextualization," 2025-11-18 [^7^]

> "As a specialist in industrial software, AVEVA helps you attach meaningful contextual details to real-time data streams... the asset framework feature lets data users build their own, reusable data structures to represent physical assets or logical process flows."
— AVEVA, PI Data Infrastructure solution brief [^39^]

> "To maximize their data usage, enterprises must make it easy to not only share and access information but, more importantly, to contextualize it with meaningful insights... companies must build a data infrastructure using solutions that can integrate all sources of pertinent information, from engineering to operations to asset management to enterprise finance."
— AVEVA, "End unplanned downtime: Best practices for asset failure mitigation" [^40^]

> "Newer historians are beginning to use AI powered contextualization... The next-gen historian enhances the user experience for the new generation of workers who do not have the same skillsets or process knowledge as the generation that is retiring."
— ARC Advisory Group, "The Future of Operational Data Historians" [^24^]

> "Industrial automation is moving toward a 'data-first monopoly model,' where competitive advantage is defined by: Ownership of operational data models; Depth of asset contextualization... System integration complexity will shift from hardware to data semantics."
— PLCMasters on Schneider Electric's $3.1B Cognite acquisition, 2026-07-06 [^25^]

---

## 4. Quantified Impacts

| Metric | Figure | Source |
|---|---|---|
| Petroleum engineers/geoscientists time searching & assembling data | "over half of their time" | Brulé report, cited in Mohammadpoor & Torabi, "Big Data analytics in oil and gas industry," *Petroleum* (ScienceDirect), 2020 [^3^] |
| O&G employee time searching unstructured data (Equinor CIO) | 80% (vs. 30% all industries, IDC) | JPT/SPE, 2019-07-03 [^4^] |
| Oil & gas field service engineers citing "time spent looking for information" as least-favorite task | 22%; 25% say company doesn't make info easy to find | TrueContext / Service Council "2024 State of the Oil & Gas Market" [^2^] |
| Enterprise data actually put to work | 32% used / 68% unleveraged (n=1500 enterprise leaders) | Seagate "Rethink Data" (IDC), 2020-07-15 [^33^] |
| Oil rig sensor data examined | 1% of data from 30,000 sensors; used for anomaly control, "not for optimization and prediction" | McKinsey Global Institute, "The Internet of Things: Mapping Value Beyond the Hype," 2015 [^12^] |
| Industrial data never used (Siemens) | ~80% | aiassemblylines.com citing Siemens, 2026-06-12 [^41^] |
| EU industrial data never used | 80% | Numeum (French digital trade union), 2025-07-25 [^42^] |
| Organizational data that "sits unused" | ~97% (Gartner estimate, as cited) | Pantohealth blog citing Gartner/Digital Signage Today, 2025-05-07 [^43^] |
| Dark share of stored data | 55% dark (Splunk 2019); 85% dark+ROT (Veritas 2016) | Superkind synthesis of primary sources, 2026-06-12 [^44^] |
| Cost of poor data quality per organization | $12.9M/yr average (Gartner); some estimates $15M | Gartner, widely reported [^14^] |
| Cost of poor data quality, US economy | $3.1T/yr | IBM estimate (2016), via HBR (Redman) [^15^] |
| Revenue lost to bad data | 15–25% of revenue | Thomas Redman / MIT Sloan-Cork estimates [^45^] |
| Data scientists' time data wrangling | 50–80% | New York Times (2014), via agiledata.org [^45^] |
| Refinery material balance imbalance (250 kbpd) | 1.5–2% typical; closing by 0.5% ≈ up to $5.0M/yr | DigitalRefining, "Better yield accounting methods improve financial results" [^35^] |
| Yield accounting/reconciliation improvement value | "in excess of $8.5 million per year" for a 250 kbpd refinery | Invensys via Control Engineering / Process Industry Informer [^46^] |
| Manual tank reading reconciliation differences | up to 3%, "translating to millions in unexplained losses annually" | Kissflow (major downstream facility analysis), 2025-05-26 [^37^] |
| Workforce knowledge loss | "231,000 years of knowledge" lost to retirement (O&G study); ~400,000 US energy workers nearing retirement in next decade | Academia.edu KM-in-O&G study [^47^]; Energy Central, 2024-09-05 [^48^] |
| Users' time searching for data / questioning trustworthiness | 44% of time | IJRCAIT enterprise data architecture review (citing governance surveys) [^49^] |

---

## 5. Tensions, Caveats, and Contradictions

1. **The $3.1T IBM figure is contested and dated.** Integrate.io notes: "IBM research from 2016... estimated poor data quality cost the U.S. economy $3.1 trillion per year. While this figure is now dated and IBM was not transparent about methodology when questioned, it remains a frequently cited benchmark" [^15^]. Use Gartner's $12.9M/org/yr as the defensible line-item figure; treat $3.1T as boardroom orientation only.
2. **Internal inconsistency in the Seagate/IDC report:** headline says 68% unleveraged, but the body text also states "As much as 88% of data goes unleveraged" in one passage — an OCR/editorial artifact in the published PDF worth flagging if quoted precisely [^33^].
3. **Standards proliferation is itself the problem.** The "so many standards" adage is borne out: ISO 15926 vs. MIMOSA camps split along vendor lines with "marketshare-driven vested interest in maintaining a separate platform" [^19^]; CFIHOS, DEXPI, JIP33/IOGP and MIMOSA all maintain overlapping RDLs, "none are all-encompassing" [^21^]. Expect semantic-mapping, not single-standard, solutions.
4. **Vendor claims vs. independent evidence.** Cognite/AVEVA/Kanerika/iFactory/Kissflow materials are vendor marketing; their problem statements align with independent academic and trade-press evidence (SPE/JPT, Teesside, Chalmers, ARC), but their quantified savings should be treated as illustrative. Note AVEVA cites "43% of all collected industrial data remains largely unused" attributed to Seagate [^40^] — a different framing than Seagate's own 68% enterprise figure [^33^]; definitions (collected vs. available) matter.
5. **"Contextualization" ≠ decision-context capture.** Industrial contextualization (Cognite, AVEVA, ARC) links data to assets, events and processes — not to the *why* of human planning decisions. The software-engineering ADR/decision-log tradition [^27^][^28^] demonstrates the missing artifact type; its non-adoption in industrial planning is the core gap for lookback/backcasting and CI knowledge management.
6. **Adoption metrics for OPC UA come from a market-research vendor** (MarketIntelo), not a neutral body; the 65–70% legacy installed-base claim is plausible and consistent with terminal-automation reporting of "incomplete" OPC UA adoption [^13^][^32^].

---

## Sources

[^2^]: TrueContext, "2024 State of the Oil & Gas Market" (PDF), https://truecontext.com/wp-content/uploads/2024/07/2024-State-of-the-Oil-Gas-Market.pdf (2024)
[^3^]: Mohammadpoor & Torabi, "Big Data analytics in oil and gas industry: An emerging trend," ScienceDirect, https://www.sciencedirect.com/science/article/pii/S2405656118301421 (2020)
[^4^]: JPT (SPE), "Oil and Gas Has a Problem With Unstructured Data," https://jpt.spe.org/oil-and-gas-has-problem-unstructured-data (2019-07-03)
[^5^]: Cognite, "What is contextualization?", https://www.cognite.com/en/resources/blog/what-is-contextualization (2025-03-20)
[^6^]: Cognite, "What is Data Contextualization for AI?", https://www.cognite.com/en/resources/blog/what-is-data-contextualization (2025-03-20)
[^7^]: TDengine, "Understanding Industrial Data Contextualization," https://tdengine.com/understanding-industrial-data-contextualization/ (2025-11-18)
[^8^]: F7i.ai, "Oil & Gas Asset Management 2026," https://f7i.ai/blog/from-cost-center-to-profit-engine-the-definitive-2025-guide-to-oil-and-gas-asset-management (2025-07-16)
[^9^]: Kanerika, "Data Lakehouse for Manufacturing: What Actually Works," https://kanerika.com/blogs/data-lakehouse-for-manufacturing/ (2026-06-15)
[^10^]: Infosys, "Reimagining Manufacturing Operations Through Agentic AI Led IT–OT Integration," https://blogs.infosys.com/engineering-services/5g-edge/reimagining-manufacturing-operations-through-agentic-ai-led-it-ot-integration.html
[^11^]: Greenovative, "From Siloed to Smart: Unifying Energy Data for Industrial Efficiency," https://greenovative.com/centralized-energy-data-management-for-manufacturing/ (2025-09-19)
[^12^]: McKinsey Global Institute, "Unlocking the potential of the Internet of Things" / "An executive's guide to the IoT," https://aegex.com/images/uploads/white_papers/Unlocking_the_potential_of_the_Internet_of_Things___McKinsey__Company.pdf (2015)
[^13^]: Dataintelo, "Oil and Gas Terminal Automation Market," https://dataintelo.com/report/oil-and-gas-terminal-automation-market
[^14^]: DQLabs, "The Cost of Bad Data Quality," https://www.dqlabs.ai/blog/the-cost-of-bad-data-quality-real-numbers-from-enterprise-ai-projects/ (2026-06-09); Gartner "12 Actions to Improve Your Data Quality," cited via https://datacontentmanager.com/build-a-business-case-for-data-quality-improvement/
[^15^]: Integrate.io, "Data Quality Improvement Stats from ETL," https://www.integrate.io/blog/data-quality-improvement-stats-from-etl/ (2026-01-08)
[^16^]: MidDel Consulting, "Professional ETRM/CTRM Consulting Services," https://middelconsulting.com/professional-etrm-ctrm-consulting-services/ (2025-05-30)
[^17^]: Data Catalyst, "$25M annual savings through asset data transformation," https://www.datacatalyst.com/driving-precision-how-strategic-master-data-management-eliminated-2-8m-in-annual-waste-for-a-global-automotive-leader-6-2-2-2-3-2-2-2-2/ (2025-10-23)
[^18^]: Petrosoft, "How Much Does a C-Store POS System Really Cost?", https://petrosoftinc.com/blog/how-much-does-a-c-store-pos-system-really-cost-the-truth-nobody-tells-you/ (2026-03-04)
[^19^]: "Metamodel-Based Information Integration at Industrial Scale," ResearchGate, https://www.researchgate.net/publication/221223722_Metamodel-Based_Information_Integration_at_Industrial_Scale
[^20^]: Chalmers ODR, "Evaluating interoperability of ISO 15926 implementation," https://odr.chalmers.se/items/6a70cbbc-43a7-40ba-bf3e-6125ab734740 (2023-02-09)
[^21^]: Yokogawa, "Delivering Asset Data Integrity through Digitization and...," Gas Processing & LNG Nov–Dec 2019, https://web-material3.yokogawa.com/1/29692/files/5_Gas-Processing-and-LNG-Nov-Dec-2019-ePrint_final.pdf
[^22^]: Teesside University, "Information management for decommissioning of Oil & Gas facilities," https://research.tees.ac.uk/ws/files/9612050/Informationmanagement_for_decommissioning_of_Oil_Gas_facilities.pdf
[^23^]: AVEVA, "CONNECT – Data management," https://www.aveva.com/en/connect-experience/about-connect/data-management/ (accessed 2026)
[^24^]: ARC Advisory Group, "The Future of Operational Data Historians," https://www.arcweb.com/industry-best-practices/future-operational-data-historians
[^25^]: PLCMasters, "Schneider Electric's $3.1B Cognite Acquisition," https://www.plcmasters.com/blogs/news/schneider-electric-s-3-1b-cognite-acquisition-building-the-full-stack-industrial-ai-ecosystem-1 (2026-07-06)
[^26^]: iFactory, "Shift Handover Logbook and Safety Critical Knowledge Transfer," https://ifactoryapp.com/industries/oil-and-gas/shift-handover-logbook-knowledge-transfer-safety (2026-06-22)
[^27^]: adr.github.io, "Architectural Decision Records," https://adr.github.io/
[^28^]: Fowler, M., "Architecture Decision Record," https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
[^29^]: ReflectRally, "ADRs: From Documentation to Decision Governance," https://reflectrally.com/architecture-decision-logs/
[^30^]: JPT (SPE), "Data Dilemma: Unraveling the Challenges and Downsides of Data in Oil and Gas," https://jpt.spe.org/data-dilemma-unraveling-the-challenges-and-downsides-of-data-in-oil-and-gas (2023-08-09)
[^31^]: Codasol, "Master Data Management: Process, benefits, and challenges," https://www.codasol.com/mdm-process-benefits-and-challenges/ (2025-07-08)
[^32^]: MarketIntelo, "OPC UA Market Research Report 2034," https://marketintelo.com/report/opc-ua-market (2026-06-12)
[^33^]: Seagate, "Rethink Data: Put More of Your Data to Work—From Edge to Cloud" (IDC), https://www.seagate.com/files/www-content/our-story/rethink-data/files/Rethink_Data_Report_2020.pdf and press release https://investors.seagate.com/news/news-details/2020/Seagates-Rethink-Data-Report-Reveals-That-68-of-Data-Available-to-Businesses-Goes-Unleveraged/default.aspx (2020-07-15)
[^34^]: VisionWrights, "Unstructured Data: The 80% You're Ignoring," https://visionwrights.com/blog/unstructured-data-the-eighty-percent-youre-ignoring (2026-04-05)
[^35^]: DigitalRefining, "Better yield accounting methods improve financial results," https://www.digitalrefining.com/article/1000976/better-yield-accounting-methods-improve-financial-results
[^36^]: Marabesi, "Architectural Decision Records," https://marabesi.com/software-architecture/adr.html (2025-02-01)
[^37^]: Kissflow, "Tank Inventory Automation in Oil & Gas Industry," https://kissflow.com/solutions/oil-and-gas/tank-inventory-automation/ (2025-05-26)
[^38^]: SDG, "Embedding Decision Quality in Chevron's Culture," https://sdg.com/case-study/embedding-decision-quality-in-chevrons-culture-helps-them-outperform-the-competition/
[^39^]: AVEVA, "PI Data Infrastructure" solution brief, https://www.aveva.com/content/dam/aveva/documents/solution-brief/SolutionBrief_PIDataInfrastructure.pdf.coredownload.inline.pdf
[^40^]: AVEVA, "End unplanned downtime: Best practices for asset failure mitigation," https://www.aveva.com/content/dam/aveva/documents/articles/Article_AVEVA_PredictiveAnalytics_23-02.pdf.coredownload.inline.pdf
[^41^]: AIAssemblyLines, "Why Industrial AI Must Reach 99% Accuracy: Lessons From Siemens," https://aiassemblylines.com/post/industrial-ai-accuracy-standard-siemens-lessons (2026-06-12)
[^42^]: Numeum, "Industrial data: 80% still asleep," https://numeum.fr/en/public-affairs/industrial-data-80-still-asleep-can-europe-wake-up-in-time/ (2025-09-12)
[^43^]: Pantohealth, "Unlocking Industrial Data," https://pantohealth.com/blog/unlocking-industrial-data-global-trends-eu-perspectives-and-rail-industry-opportunities/ (2025-05-07)
[^44^]: Superkind, "Unstructured Data: The 80% of Company Knowledge Your Systems Cannot Read," https://superkind.ai/blog/unstructured-data (2026-06-12)
[^45^]: AgileData.org, "The Impact of Poor Data Quality," https://agiledata.org/essays/impact-of-poor-data-quality.html (2026-01-26)
[^46^]: Process Industry Informer, "Invensys Strengthens Refinery-Wide Optimization Solutions," https://www.processindustryinformer.com/invensys-strengthens-refinery-wide-optimization-solutions/ (2019-12-11)
[^47^]: "Challenges in Knowledge Management: Insights from Oil and Gas Industry," Academia.edu, https://www.academia.edu/44618407/ (2015)
[^48^]: Energy Central, "Cross-Generational Knowledge Transfer in the Energy Sector," https://www.energycentral.com/workforce/post/cross-generational-knowledge-transfer-energy-sector-bridging-gap-TUK3HY0r0X1Qq6F (2024-09-05)
[^49^]: IJRCAIT, "Enterprise Data Architectures: A Comprehensive Analysis," https://iaeme.com/MasterAdmin/Journal_uploads/IJRCAIT/VOLUME_8_ISSUE_1/IJRCAIT_08_01_243.pdf
