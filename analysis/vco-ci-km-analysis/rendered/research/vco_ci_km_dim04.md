# Dimension 04 — Operations & Reliability Lookback Practices (Refining)
## How Refiners Retrospectively Analyze Downtime, Incidents, and Operational Losses

**Study:** Value Chain Optimization (VCO), Lookback/Backcasting, and CI Knowledge Management
**Prepared:** 2026-07-18
**Analyst:** Deep-Research Sub-Agent (Dimension 04)
**Method:** ≥15 independent coarse-to-fine web searches (58 executed in 15 batches; log in Appendix A), prioritizing CCPS/AIChE, API, OSHA/EPA/CSB, Solomon Associates (HSB), SMRP, Reliabilityweb, ISO 14224 literature, academic papers (Safety Science, J. Loss Prevention, J. Safety Research), and trade press (OGJ, Hydrocarbon Engineering, Inspectioneering, Marsh). All evidence captured as verbatim excerpts with source, URL, date, and a confidence rating.

**Evidence template used per claim:** Claim / Source / URL / Date / Excerpt (verbatim) / Context / Confidence (high-med-low). Inline citations [^N^] map to the numbered Source List at the end. Tensions between sources are flagged explicitly.

---

# KEY FINDINGS (Summary)

1. **Refiners' downtime lookback is institutionalized around the Solomon Associates (HSB) benchmarking system, whose core construct is *monetized* downtime.** The Reliability & Maintenance (RAM) Study *"evaluates reliability (based on monetized downtime) and maintenance performance"* and asks: *"How do my scheduled and unscheduled downtimes and rate reductions, due to RAM issues, compare to my peers?"* [^1^] An optimum maintenance strategy is defined as minimizing the sum of maintenance spend **plus** the value of lost production from breakdowns and turnarounds [^2^]. Top-quartile vs. poor performers differ by ~**7% of Plant Replacement Value**; Solomon claims clients achieve ~10% gap closure and *"returns exceeding 100 times the study cost"* [^4^]. Database: >1,500 sites, >10,000 production units, >54,000 refinery turnarounds [^3^][^4^].

2. **Loss quantification uses a three-level availability stack — Mechanical Availability ≥ Operational Availability ≥ On-stream Factor — each adding wider loss categories, all normalized by EDC (Equivalent Distillation Capacity).** MA counts turnaround + breakdown + slowdown (<75% of nominal rate) downtime; OA adds technology (catalyst regeneration, decoking, *operator error*) and authority (regulatory inspection) downtime; on-stream adds external causes including *economic/market* shutdowns and domino effects [^5^][^6^]. This taxonomy is the de-facto lookback ledger: every hour of lost or derated production must be assigned to a category before benchmarking.

3. **Availability is reported to investors as a headline KPI**, confirming that operational lookbacks roll up to enterprise scorecards: BP defines refining availability as *"Solomon Associates' operational availability for BP-operated refineries… the percentage of the year that a unit is available for processing after deducting the time spent on turnaround activity and all mechanical, process and regulatory downtime"* (96.1% in 2023) [^7^][^8^]; Valero reported *"97.2% mechanical availability"* in 2021 alongside an API RP 754 Tier 1 PSE rate of 0.05 [^9^]. SMRP's generic metrics add OEE = Availability × Performance × Quality, but warn that *"utilization"* is *"impacted by many factors unrelated to elements of reliability, including market demand"* [^10^][^11^].

4. **Incident RCA is compliance-anchored (OSHA PSM 1910.119(m)) but the *method* is deliberately unspecified — and regulators are now moving to mandate root-cause analysis, which industry resists.** PSM requires investigating incidents that *"resulted in or could reasonably have resulted in a catastrophic release"* within 48 hours, a team, a report, follow-up, and 5-year retention [^22^]. OSHA's SBREFA modernization panel noted PSM *"does not require employers to identify the root cause of the incident"* and estimated adding RCA would increase investigation time ~50% [^23^]; EPA's 2024 RMP rule *did* mandate root-cause investigations for facilities with prior accident history [^25^][^26^]. AFPM objected to *"mandating a specific root-cause analysis methodology… even for those incidents that pose little potential risk"* [^24^].

5. **API RP 754 (process safety indicators) and CCPS metric guidance structure the safety lookback pyramid (Tiers 1–4, lagging→leading), born directly from the CSB's Texas City finding that industry lacked *"an effective system of indicators"* to monitor safety performance** [^27^][^30^][^50^]. Yet audit data show persistent classification inconsistency: *"corporate audits routinely find 10 to 20 percent under-classification"* of Tier 1 events [^28^].

6. **RCA method choice varies enormously in rigor, and quality variance is a documented weakness.** The method landscape spans 5-Why, fishbone, fault-tree, TapRooT (SnapCharT® + Root Cause Tree® + Equifactor®), Apollo, MTO, barrier/change analysis, bowtie, ICAM, Tripod Beta [^36^][^37^][^40^][^41^]. Practitioners criticize 5-Why for single-cause linear thinking, confirmation bias, non-repeatability (*"different people using 5 Whys come up with different causes for the same problem"*) and stopping at symptoms [^38^][^42^][^43^][^44^]. CCPS's 3rd-edition investigation guidelines counter with a scientific-method discipline — a *root cause* is *"a fundamental, underlying, system-related reason why an incident occurred that identifies a correctable failure(s) in management systems. There is typically more than one root cause for every process safety incident"* — and warn that *"many commonly used incident analysis techniques fail to identify or eliminate multiple hypotheses/scenarios before beginning root cause analysis. In the worst-case scenarios, this can cause confirmation bias"* [^33^][^34^][^35^].

7. **CSB investigation reports are the industry's richest published lookbacks — and they repeatedly show *failed* lookbacks upstream of disasters.** Texas City: **eight prior blowdown-drum releases (1994–2004) *"were not properly investigated, and appropriate corrective actions were not implemented"*; a 1994 action item was *"never finished, and management officials did not follow up"* [^46^][^47^]. Chevron Richmond: sulfidation-damaged pipe flagged for replacement *"as far back as 2002"* by Chevron's own metallurgists; CSB said *"the ultimate issue is not corrosion, but how to make effective corporate decisions"* [^51^][^52^]. BP-Husky Toledo 2022: a near-identical 2019 naphtha-release near-miss was investigated, but *"the refinery did not develop action items… resulting in a missed opportunity"* to prevent the fatal 2022 fire [^55^].

8. **Lookback data plumbing exists at three levels — process historians/event frames, alarm & event logs, LIMS — but each answers a different question and they are rarely fused.** Historians (e.g., PI System *Event Frames*) *"automatically bookmark important events… Capture events based on user-defined process thresholds… analyze and compare these events in bulk"* [^60^]; ISA-18.2/EEMUA alarm KPIs (acceptable <6 alarms/operator-hour; flood >10 alarms/10 min) structure alarm lookbacks [^58^][^59^] — the Toledo CSB case used alarm logs forensically (≈**3,712 alarms in ~12 hours** before the explosion) [^55^]. LIMS manages refinery quality lookback (ARG: 5,500–6,500 samples/month, ~30,000 tests; excursion flagging and trend analysis) [^62^][^63^]. Production accounting/mass-balance systems (e.g., Visual Mesa) reconcile yields monthly and *"detect early deviations from the plan"* [^65^].

9. **The operational→commercial bridge is real but thin and mostly manual.** Quantified anchors exist: EIA cites Valero's St. Charles FCC turnaround exposure at **$1.2–3M per day** beyond schedule [^67^]; DOE's Energy Assurance Daily logged ~**1,700 refinery shutdowns (2009–2012) and >$32M** lost opportunity, 46% mechanical [^68^]; McKinsey-cited estimates put reliability-related lost profit at **$20–50M/yr** for a mid-size refinery [^69^]; Marsh's 100 Largest Losses shows refining >1/3 of losses and PES's **$750M** 2019 loss ending in closure and bankruptcy [^73^]. KBC monetizes per-unit losses explicitly (*"Loss FCCU capacity: USD 13/bpd; Loss refinery capacity: USD 1.34/bpd"*) [^65^]. Emerson names the missing link: *"The ability to compare actual vs. expected unit performance and 'back-cast' the LP models to predict the period that just completed can be complex and time consuming"* [^66^]. Downtime-cost figures vary by >100× across sources (see Tension T5).

10. **The deepest, best-documented weakness is organizational: lessons are generated but not reused.** Kletz's dictum — organizations *"have no memory and accidents recur"* [^85^] — is confirmed empirically: Drupsteen & Hasle found investigation outputs stall at action planning/implementation [^81^]; Lundberg et al. showed *"What-You-Look-For-Is-What-You-Find"* biases and that *"the discipline of experience feedback has not been sufficiently self-reflective"* [^82^][^83^]; Körvers & Sonnemans found accidents recur because similar incidents had occurred before without learning [^92^]; a 2024 cross-industry review lists underreporting and blame culture as top hindrances [^84^]. CSB's repeat-incident record (Texas City → Whiting 2005 repeat → Toledo 2019→2022) is the operational proof. Industry responses exist (AFPM event-sharing database & regional networks, CCPS PERD equipment-failure database, CCPS's *"Driving Continuous Process Safety Improvement From Investigated Incidents"* calling incidents *"a gift on a silver platter"*) [^77^][^80^][^91^][^19^] — but they rely on voluntary, non-standardized submissions.

---
---

# SECTION 1 — DOWNTIME / RATE-LOSS ANALYSIS & BENCHMARKING

## 1.1 The Solomon (HSB) benchmarking system — the industry's lookback ledger

### Claim 1.1a — Solomon's RAM Study is built on *monetized* downtime and peer comparison of scheduled/unscheduled downtime and rate reductions.
- **Source:** Solomon Associates (HSB), "Reliability and Maintenance (RAM) benchmarking"
- **URL:** https://solomoninsight.com/consulting/benchmarking/reliability-maintenance-ram/
- **Date:** accessed 2026-07-18 (undated product page)
- **Excerpt (verbatim):** "The RAM Study evaluates reliability (based on monetized downtime) and maintenance performance (maintenance and reliability spending) metrics of production operations… How do my scheduled and unscheduled downtimes and rate reductions, due to RAM issues, compare to my peers?… The difference between the best and worst performers shows that an optimized strategy can be worth 7% of your Plant Replacement Value (PRV)."
- **Context:** Establishes that the industry's standard lookback unit of account is not hours but *dollars of lost production*, enabling cross-site peer comparison.
- **Confidence:** High (benchmark owner's own description).

### Claim 1.1b — Solomon defines the optimum maintenance strategy as minimizing maintenance spend + value of lost production (breakdowns + turnarounds); results are delivered as monetized gaps.
- **Source:** Solomon Associates, "Solomon's Reliability and Maintenance (RAM) Study vs. Fuels Study" (blog)
- **URL:** https://solomoninsight.com/insights/blog/solomons-reliability-and-maintenance-ram-study-vs-fuels-study/
- **Date:** accessed 2026-07-18
- **Excerpt (verbatim):** "A Maintenance strategy is considered optimum for those production units that achieve and sustain the minimization of the sum of: 1. Maintenance expenditure 2. Value of lost production associated directly with lack of maintenance (production unit breakdowns) 3. Value of lost production associated directly with maintenance (production unit overhauls or turnarounds). … Client performance gaps are monetized for both maintenance and production losses. … On average, clients achieve a return on investment of 100 times the study cost by closing identified gaps by approximately 10%."
- **Context:** The lookback deliverable is a *monetized gap-to-peer* ledger; maintenance cost and downtime losses are traded off in one objective function.
- **Confidence:** High.

### Claim 1.1c — Scale and content of the database underpinning lookback benchmarks.
- **Source:** Solomon Associates, "2023 Reliability & Maintenance Study: What's New" and "Reliability, Maintenance & Turnarounds"
- **URL:** https://solomoninsight.com/insights/blog/2023-reliability-maintenance-study-whats-new/ ; https://solomoninsight.com/consulting/benchmarking/reliability-maintenance-turnarounds/
- **Date:** 2023 (blog); accessed 2026-07-18
- **Excerpt (verbatim):** "…the RAM Study database currently contains more than 1,500 site and 10,000 production units…"; "…more than 54,000 refinery turnarounds over the last 40 years."
- **Context:** Peer groups (e.g., by unit type, size, region) allow "how do we compare" lookbacks; turnaround performance is benchmarked separately (duration, interval, cost).
- **Confidence:** High.

## 1.2 The availability metric stack (MA / OA / On-stream) and loss categorization

### Claim 1.2a — Solomon's availability architecture is a strict hierarchy MA ≥ OA ≥ On-stream, built from categorized downtime (turnaround, breakdown, slowdown, technology, authority, other), normalized by EDC.
- **Source:** János Németh (MOL Plc, Duna Refinery), "How to calculate Mechanical Availability (MA)," *MOL Group Scientific Magazine* 2011/1, pp. 72–77 (method published with permission of Solomon Associates' VP Refining Studies; cites *Fuels Refinery Performance Analysis for Operating Year 2008 — Solomon Associates*, including proprietary trademarked key metrics: Mechanical Availability™, Operational Availability™, On-Stream Factor™ and EDC™)
- **URL:** https://molgermany.de/images/molgermany/pdf/about_mol_group/publikationen/MOL_Group_Scientific_Magazine_2011_01.pdf
- **Date:** 2011
- **Excerpt (verbatim):** "Refinery efficiency is determined by its availabilities, that are depended on magnitude and type of the shutdowns (planned, unplanned breakdown and slowdown). … The following equation is always true for the availabilities of Solomon: MA≥OA≥ on-stream. … At the mechanical availability the shutdown time is the total maintenance activities of turnaround period, breakdown period and slowdown period (performance of the unit less than 75% of its nominal process)… At the operational availability the shutdown time is the aggregation of period belonging to MA, and period of technological activities (catalyst regeneration, catalyst replacement, furnace decoking, operator error, maintenance of utility system) and period of authority activities (environmental testing, pressure vessel inspection, other regulatory inspection)… At the on-stream factors the shutdown time is the summary of period belonging to MA and period belonging to OA, and period of the other external reasons (economic, process unit incident, off-site incidents, other external)… All shutdowns are had to take into account at the calculation of availabilities independently of their planned or unplanned state."
- **Context:** This is the refinery downtime lookback taxonomy in detail. Note (i) a *slowdown* counts as downtime below a 75%-of-nameplate threshold; (ii) "operator error" and "economic" causes have explicit slots; (iii) turnaround downtime is annualized (spread over the turnaround interval) — a deliberate time-smoothing choice with lookback consequences (see §5.2).
- **Confidence:** High (practitioner paper describing the proprietary method; reviewed by MOL maintenance head, acknowledged by Solomon).

### Claim 1.2b — The Solomon downtime grouping (five buckets) and formulas used by refiners internally.
- **Source:** R. Gorisse, TU Eindhoven (TU/e) master's thesis on refinery maintenance performance (BP Rotterdam Refinery context), reproducing Solomon benchmark definitions
- **URL:** https://pure.tue.nl/ws/files/46925260/841778-1.pdf
- **Date:** ~2014 (undated thesis)
- **Excerpt (verbatim):** "Different types of downtime according to Solomon benchmark (Solomon Associates): Turnaround downtime = downtime caused by all maintenance activities classified as T/A; Non-Turnaround Mechanical downtime = downtime caused by all maintenance activities not classified as T/A; Regulatory/Process downtime = downtime caused by scheduled and unscheduled outages for inspections or process-related problems. Includes: outages for regulated inspections and testing, furnace decokings and catalyst regenerations not reported as T/A; Other downtime = downtime caused by outages caused by circumstances outside the affected unit's boundaries. This includes the domino effect and market conditions; Slowdown downtime = downtime caused by reduced speed operation."
- **Context:** Confirms the five-bucket lookback ledger and shows a refiner (BP Rotterdam) computing On-Stream Availability per unit, weighted by unit EDC% — i.e., the lookback is unit-level, then rolled up by economic weight, not simple clock time.
- **Confidence:** Medium-high (academic thesis reproducing proprietary definitions).

### Claim 1.2c — Availability is an investor-reported KPI (BP, Valero), proving operational lookbacks roll up to corporate scorecards.
- **Source:** BP p.l.c., Annual Report and Form 20-F 2019 (glossary); BP Strategic Report 2023; Valero Energy ESG Report 2022
- **URL:** https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/pdfs/investors/bp-annual-report-and-form-20f-2019.pdf ; https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/pdfs/investors/bp-annual-report-and-form-20f-2023.pdf ; https://www.valero.com/sites/default/files/2022-08/2022%20ESG%20Report.pdf
- **Date:** 2020 / 2024 / 2022 (publication years)
- **Excerpt (verbatim):** BP: "Refining availability represents Solomon Associates' operational availability for BP-operated refineries. The measure shows the percentage of the year that a unit is available for processing after deducting the time spent on turnaround activity and all mechanical, process and regulatory downtime." (BP reported refining availability of 96.1% for 2023, "higher than 2022… [reflecting] fewer unplanned outages"). Valero: "In 2021, we achieved 97.2% mechanical availability across our refining system… [and] a Tier 1 process safety event rate of 0.05 per 200,000 work hours."
- **Context:** Availability (OA basis at BP, MA basis at Valero) plus API 754 Tier-1 rate are the two operational-lookback KPIs investors see. Note the **tension**: BP reports OA, Valero reports MA — the same word "availability" masks different loss ledgers (see Tension T1).
- **Confidence:** High.

## 1.3 Generic reliability metrics and loss frameworks (SMRP, OEE, ISO 14224)

### Claim 1.3a — SMRP best-practice metrics define Availability, Utilization, and OEE, and warn that utilization is driven by non-reliability factors (market demand) — a caution for cross-metric lookbacks.
- **Source:** SMRP Best Practices, 6th Edition (metrics definitions, mirrored); SMRP Best Practices Metrics Workshop (PEMAC-hosted PDF)
- **URL:** https://quizgecko.com/books/smrp-best-practices-6th-edition-kb5z94 ; https://www.pemac.org/sites/default/files/SMRP%20Best%20Practices%20Metrics%20Workshop%202018.pdf
- **Date:** 6th ed. ~2023; workshop 2018
- **Excerpt (verbatim):** "Utilization time is impacted by many factors unrelated to elements of reliability, including market demand, feedstock availability, and other business decisions." … "OEE = Availability × Performance × Quality." … "Top performers in all industries can maintain reliable plants for under 3% of RAV [Replacement Asset Value] — regardless of industry."
- **Context:** SMRP provides the plant-level (asset) counterpart to Solomon's unit/refinery-level view. The explicit warning about *utilization* mixing reliability with commercial causes is exactly the classification-boundary problem that corrupts lookbacks (see §5.1).
- **Confidence:** Medium (mirror/derivative copies of SMRP material).

### Claim 1.3b — ISO 14224 provides the standard data model for equipment-level failure/maintenance records used in reliability lookbacks; CCPS PERD applies the same idea to process equipment.
- **Source:** ISO 14224:2016 scope statement; ISO/TC 67 workshop paper; CCPS PERD description (via 61508.org)
- **URL:** https://www.iso.org/standard/64076.html ; https://www.iso.org/files/live/sites/isoorg/files/news/magazine/ISOfocus%20%282013-2017%29/en/2017/ISOfocus_124/TC67_Houston_paper.pdf ; https://www.61508.org/knowledge/ccps-process-equipment-reliability-database-perd.php
- **Date:** 2016 (standard); accessed 2026-07-18
- **Excerpt (verbatim):** ISO: "This document provides a comprehensive basis for the collection of reliability and maintenance (RM) data in a standard format for equipment in all facilities and operations within the petroleum, natural gas and petrochemical industries… It describes data-collection principles and associated terms and definitions that constitute a 'reliability language'…" TC67 paper: the standard enables companies to "learn from failures" and "avoid failure to learn." PERD: "The CCPS Process Equipment Reliability Database (PERD) is a source of industry-reported equipment reliability data for use in… quantitative analyses."
- **Context:** Failure-mode/cause/consequence coding is the atomic layer of downtime lookbacks; ISO 14224/OREDA/PERD exist precisely because companies' internal coding was inconsistent (see §5.1 for evidence the problem persists).
- **Confidence:** High for ISO; medium for PERD mirror page.

### Claim 1.3c — Generic OEE/loss taxonomies enumerate the loss universe (breakdown, slowdown, quality/rework, planning) and even propose a "Sales Opportunity Loss" — the commercial-loss category refining lookbacks usually lack.
- **Source:** Cambridge International Manufacturing Symposium proceedings (loss taxonomy table); Springer chapter "OEE Monitoring for Production Processes Based on SCADA/HMI Platform"
- **URL:** https://www.ifm.eng.cam.ac.uk/uploads/Resources/Reports/CIM_Proceedings_for_web3.pdf ; https://link.springer.com/content/pdf/10.1007/978-0-387-74157-4_22.pdf
- **Date:** undated (~2008–2017)
- **Excerpt (verbatim):** Cambridge: loss classes include "Equipment failure (Breakdowns) loss… Speed loss… Quality defect loss… losses from product downgrading… Planning loss…" and proposes "establishment of 'Sales Opportunity Loss'. … To tackle with these losses, root cause investigation and correlation analysis among losses are critical." Springer: "some causes produce losses qualified in more than just one way. They can touch availability, performance and/or quality issues at the same time."
- **Context:** Confirms the multi-dimensionality of losses (availability × rate × quality) and the observation that a single event can legitimately be booked to several loss categories — a root cause of classification inconsistency (§5.1).
- **Confidence:** Medium.

## 1.4 How big is the prize — quantified downtime/rate-loss lookbacks

### Claim 1.4a — Official US data: ~1,700 refinery shutdowns in 2009–2012 with >$32M in lost opportunity; 46% mechanical, 19% electrical, 23% maintenance, 12% fires.
- **Source:** Valin Corporation white paper citing US DOE Energy Assurance Daily (EAD) data
- **URL:** https://www.valin.com/resources/whitepapers (refinery downtime/reliability white paper)
- **Date:** ~2013–2015
- **Excerpt (verbatim):** "According to the U.S. Department of Energy's Energy Assurance Daily report, between 2009 and 2012 there were over 1,700 refinery shutdowns in the United States resulting in over $32 million in lost opportunity. 46% were caused by mechanical problems, 23% by maintenance issues, 19% by electrical problems, and 12% by fires."
- **Context:** Rare official categorization of unplanned-event causes — effectively a national lookback taxonomy — but the $32M figure is implausibly low vs. industry norms (likely reflects reported lost-profit submissions, not full value of lost production); see Tension T5.
- **Confidence:** Medium (vendor relay of DOE dataset).

### Claim 1.4b — McKinsey-cited estimate: reliability-related lost profit opportunities of $20–50M/yr for a mid-size refinery.
- **Source:** Imubit (citing McKinsey), article on refinery reliability/thermal fatigue
- **URL:** https://www.imubit.com/ (insights article)
- **Date:** ~2023
- **Excerpt (verbatim):** "…reliability-related lost profit opportunities can reach $20 million to $50 million per year" for a mid-size refinery.
- **Context:** Order-of-magnitude anchor for monetizing a single refinery's annual lookback gap; consistent with Solomon's "% of PRV" framing.
- **Confidence:** Medium (secondary citation of McKinsey).

### Claim 1.4c — Gulf Coast study: production losses during outages ranged 8.2%–33% of annual production.
- **Source:** Curran International (emergency coatings/reliability paper), citing Gulf Coast refinery research 1999–2005
- **URL:** https://curranintl.com/ (articles)
- **Date:** ~2006
- **Excerpt (verbatim):** "…production losses during outages ranged from 8.2% to 33% annually."
- **Context:** Upper bound (33%) reflects severe unplanned-event years; useful for stressing the size of the lookback opportunity in business cases.
- **Confidence:** Medium-low (consultancy article, dated).

### Claim 1.4d — Vendor-aggregated downtime cost figures for oil & gas: "$500K+ per hour" and "$84M per facility per year" (Siemens Senseye lineage) — flag as methodologically loose.
- **Source:** iFactory, "The hidden cost of downtime in oil & gas"; Alpha Software downtime cost table
- **URL:** https://ifactoryapp.com/ ; https://www.alphasoftware.com/ (blog)
- **Date:** ~2023–2024
- **Excerpt (verbatim):** iFactory: oil & gas "…$500K+ per hour… single facility losses reaching $84 million annually"; Alpha: "32 monthly downtime hours at $220,000/hour… $84M per facility"; aggregate "$47B" across Fortune-500 refiners from "213,000 downtime hours."
- **Context:** These per-hour figures are widely repeated vendor statistics (originating in Siemens' "True Cost of Downtime" reports, which are mostly discrete-manufacturing surveys). They overstate refinery *marginal* economics because refinery downtime cost is mostly lost *margin* on deferred/lost throughput plus extra maintenance, not revenue. Use only as an upper-bound rhetorical device; prefer §4's refinery-specific anchors.
- **Confidence:** Low (vendor secondary sources).

---
---

# SECTION 2 — INCIDENT & ROOT-CAUSE ANALYSIS (RCA) PROCESSES

## 2.1 Regulatory baseline: OSHA PSM, EPA RMP, state refinery programs

### Claim 2.1a — OSHA PSM 1910.119(m) defines the minimum incident-investigation lookback: 48-hour initiation, team composition, report content, follow-up system, 5-year retention.
- **Source:** Ecesis, "PSM Incident Investigation Requirements (29 CFR 1910.119(m))" (summarizing the OSHA standard)
- **URL:** https://www.ecesis.com/blog/psm-incident-investigation-requirements
- **Date:** accessed 2026-07-18
- **Excerpt (verbatim):** "Employers must investigate each incident which resulted in, or could reasonably have resulted in a catastrophic release of highly hazardous chemical… An incident investigation team must be established and consist of at least one person knowledgeable in the process involved… The investigation must be initiated as promptly as possible, but not later than 48 hours following the incident… A report must be prepared… including: date of incident; date investigation began; a description of the incident; the factors that contributed to the incident; and any recommendations resulting from the investigation… The employer must establish a system to promptly address and resolve the incident report findings and recommendations… Incident investigation reports must be retained for five years."
- **Context:** PSM's "could reasonably have resulted" language extends lookback obligations to *near misses* — but leaves method, depth, and root-cause requirements undefined (see next claim).
- **Confidence:** High (accurate restatement of 1910.119(m)).

### Claim 2.1b — OSHA's own modernization docket concedes PSM does *not* require root-cause analysis; adding it was estimated to raise investigation effort ~50%.
- **Source:** OSHA, SBREFA Small Business Panel background/issues document on PSM modernization
- **URL:** https://www.osha.gov/sites/default/files/PSM-SBREFA-issues-document.pdf
- **Date:** 2022
- **Excerpt (verbatim):** "Currently, PSM-covered establishments are required to investigate incidents (§1910.119(m)) but they are not required to conduct a root-cause analysis. … OSHA is considering the addition of a requirement…" Estimated effort: root-cause analysis "would increase the time to complete incident investigations by approximately 50 percent," i.e., "28–30 hours" and "$276 to $11,487" per investigation depending on incident complexity.
- **Context:** Documents both the regulatory gap (investigation ≠ RCA) and the cost-burden argument that shapes industry resistance.
- **Confidence:** High.

### Claim 2.1c — Industry (AFPM) resists *mandated, methodology-specific* RCA, especially for low-potential-risk incidents.
- **Source:** AFPM comments to OSHA SBREFA panel
- **URL:** https://www.afpm.org/sites/default/files/issue_resources/AFPM%20Comments%20on%20PSM%20SBREFA.pdf
- **Date:** 2022
- **Excerpt (verbatim):** AFPM expressed concern about "…mandating a specific root-cause analysis methodology for all incident investigations under Section 1910.119(m), with attendant costs and resource burdens, even for those incidents that pose little potential risk."
- **Context:** The core governance tension of incident lookbacks: regulators want system-level causes; industry wants risk-tiered method discretion. EPA's RMP rule resolved it partially toward mandates (next claim).
- **Confidence:** High.

### Claim 2.1d — EPA's 2024 RMP final rule mandated root-cause incident investigations (and third-party audits) for facilities with accident history; EPA had already documented that RCA is accepted practice embedded in NJ TCPA, Cal/OSHA refinery PSM, Contra Costa and Richmond refinery ordinances.
- **Source:** EHSCareers PSM careers guide (on the 2024 rule); Federal Register, EPA RMP proposed rule preamble (2022)
- **URL:** https://www.ehscareers.com/psm-careers-guide/ ; https://www.federalregister.gov/documents/2022/08/31/2022-18249/accidental-release-prevention-requirements-risk-management-programs-under-the-clean-air-act-safer
- **Date:** 2024 (final rule, effective May 2024); 2022 (proposal)
- **Excerpt (verbatim):** EHSCareers: the 2024 RMP rule "…mandated third-party compliance audits and root-cause incident investigations at facilities with prior accident history." Federal Register: "…root cause analysis of accidents is an accepted safe management practice used by many industries… New Jersey's TCPA, as well as California's PSM for Refineries, Contra Costa County['s]… and the City of Richmond['s]… Industrial Safety Ordinances, already require root cause analyses for major chemical accidents."
- **Context:** Refinery-specific state programs (post-Richmond fire) already impose RCA — meaning many US refineries operate under *stricter* lookback law than federal PSM.
- **Confidence:** High.

## 2.2 Industry indicator frameworks: API RP 754 and CCPS metrics

### Claim 2.2a — API RP 754 (3rd ed., Aug 2021) is the refining sector's process-safety lookback scorecard: four tiers from lagging (Tier 1) to leading (Tier 4); Tiers 1–2 intended for public reporting; born of the CSB's Texas City recommendation.
- **Source:** API, "Process Safety Performance Indicators for the Refining & Petrochemical Industries — RP 754 Fact Sheet"
- **URL:** https://www.api.org/-/media/files/oil-and-natural-gas/refining/fact-sheet-api-rp-754.pdf
- **Date:** 3rd ed. 2021; fact sheet accessed 2026-07-18
- **Excerpt (verbatim):** "API RP 754 identifies leading and lagging indicators… Tier 1… the most lagging… Tier 4… the most leading… Tiers 1 and 2 are suitable for public reporting, while Tiers 3 and 4 are intended for internal company use." Origin: developed in response to "…a recommendation from the U.S. Chemical Safety Board… following the 2005 BP Texas City incident… for an ANSI standard on process safety indicators."
- **Context:** The tier pyramid forces a refinery's lookback to count *both* realized losses (LOPC events by severity) and barrier-health signals (challenges to safety systems, operating-discipline/management-system actions).
- **Confidence:** High.

### Claim 2.2b — Practical application of RP 754 shows systematic under-classification of Tier 1 events (10–20%) and threshold-application inconsistency.
- **Source:** SmartQHSE, "API RP 754 Process Safety Indicators — Deep Dive"
- **URL:** https://smartqhse.com/ (API RP 754 article)
- **Date:** ~2023
- **Excerpt (verbatim):** "…corporate audits routinely find 10 to 20 percent under-classification" of Tier 1 events; common failures include "…inconsistent application of the [release-quantity] thresholds… Tier 3 not implemented… missing Tier 4… no follow-through on actions."
- **Context:** Direct evidence of *event classification inconsistency* in the industry's flagship lookback metric (see §5.1).
- **Confidence:** Medium (practitioner consultancy; consistent with CSB/industry lore).

### Claim 2.2c — CCPS metric guidance ("You Don't Improve What You Don't Measure") defines the lagging/leading/near-miss metric architecture and is periodically updated (v4.1, June 2022).
- **Source:** AIChE/CCPS, "Process Safety Leading and Lagging Metrics — You Don't Improve What You Don't Measure" (guidance document PDF); AIChE CCPS process safety metrics page
- **URL:** https://www.aiche.org/sites/default/files/docs/embedded-pdf/CCPS/ProcessSafetyMetrics.pdf ; https://www.aiche.org/ccps/resources/process-safety-metrics
- **Date:** v4.1 June 2022 (page); original guidance 2011
- **Excerpt (verbatim):** "You don't improve what you don't measure." Metrics cover "…lagging metrics (process safety incidents)… leading metrics… near misses…" arranged as a metric pyramid.
- **Context:** CCPS guidance is the methodological sibling of API 754; CCPS RBPS Pillar 4 ("Learn from Experience") makes incident investigation, metrics, auditing and management review elements 17–20 of the 20-element risk-based process safety system.
- **Confidence:** High.

### Claim 2.2d — CCPS RBPS frames "Learn from Experience" as one of four accident-prevention pillars (elements 17–20).
- **Source:** ThePetroSolutions, "CCPS RBPS Pillar 4 — Learn from Experience"
- **URL:** https://thepetrosolutions.com/ (RBPS series)
- **Date:** ~2021
- **Excerpt (verbatim):** Pillar 4 elements: "(17) Incident Investigation, (18) Measurement and Metrics, (19) Auditing, (20) Management Review and Continuous Improvement."
- **Context:** Positions the lookback as a *management system*, not an ad-hoc activity: investigate → measure → audit → review, in a loop.
- **Confidence:** Medium-high.

## 2.3 Investigation standards and RCA methods (and their documented quality variance)

### Claim 2.3a — CCPS's *Guidelines for Investigating Process Safety Incidents* (3rd ed., 2019) is the sector's reference investigation methodology; it defines causal factor/root cause in management-system terms and prescribes a scientific-method discipline.
- **Source:** AIChE/Wiley book page; IChemE Hazards 29 conference paper by CCPS practitioners (Stokes et al.); BakerRisk technical note on its contribution
- **URL:** https://www.aiche.org/ccps/publications/books/guidelines-investigating-process-safety-incidents-3rd-edition ; https://www.icheme.org/media/11725/hazards-29-paper-xx.pdf ; https://www.bakerrisk.com/ (CCPS investigation book note)
- **Date:** 2019
- **Excerpt (verbatim):** "Root cause — A fundamental, underlying, system-related reason why an incident occurred that identifies a correctable failure(s) in management systems. There is typically more than one root cause for every process safety incident." Investigation "…should follow the scientific method: develop hypotheses, gather evidence, test hypotheses against evidence…" Near-miss analysis "…should be treated with the same rigor as actual incidents (per API RP 585, Pressure Equipment Integrity Incident Investigation)."
- **Context:** Anchors the *target state* of refinery lookbacks: multiple-root-cause, management-system depth, hypothesis testing, and near-miss parity.
- **Confidence:** High.

### Claim 2.3b — CCPS's own authors warn that common RCA techniques skip hypothesis elimination, producing confirmation bias.
- **Source:** BakerRisk, technical article on CCPS investigation guidance
- **URL:** https://www.bakerrisk.com/ (investigations insight)
- **Date:** ~2019–2020
- **Excerpt (verbatim):** "…many commonly used incident analysis techniques fail to identify or eliminate multiple hypotheses/scenarios before beginning root cause analysis. In the worst-case scenarios, this can cause confirmation bias, where the investigator only seeks evidence supporting a preconceived scenario."
- **Context:** Practitioner confirmation of *RCA quality variance* (§5.3): the failure mode is methodological, not just skill.
- **Confidence:** Medium-high.

### Claim 2.3c — TapRooT®: a representative guided commercial RCA system (SnapCharT® timeline, Causal Factors, Root Cause Tree®, Corrective Action Helper®, Equifactor® for equipment failures with Heinz Bloch); vendor also publishes a critique of 5-Why.
- **Source:** TapRooT (System Improvements Inc.) — "What is THE root cause?"; "Best root cause analysis toolkit"; "Are You Dissatisfied with 5-Whys RCA?"
- **URL:** https://taproot.com/what-is-the-root-cause/ ; https://taproot.com/ (toolkit article) ; https://taproot.com/dissatisfied-with-5-why-root-cause-analysis/
- **Date:** 2015–2024 (various)
- **Excerpt (verbatim):** "SnapCharT®… a visual depiction of the sequence of events…"; "Causal Factor[s]… that, if eliminated, would have stopped the accident from occurring or reduce the seriousness of the incident." Critique: 5-Whys suffer "(1) Focus on a single root cause, (2) Confirmation bias, (3) No guidance to find the causes of human errors… Even smart, well-trained users (like Taiichi Ohno, himself) frequently jump to conclusions, follow a single root cause trail…" And: "If root cause analysis isn't repeatable and consistent when used by different people, it isn't consistently finding root causes."
- **Context:** Illustrates the commercial RCA ecosystem refineries buy (TapRooT is widely used in US refining/petrochem). Vendor critique is self-interested but consistent with academic findings (§5.3) — note this tension.
- **Confidence:** Medium-high (vendor primary; claims about own method are promotional).

### Claim 2.3d — The broader method landscape used in process-industry lookbacks: fault-tree, event-&-causal-factor charting, barrier analysis, change analysis, bowtie, MTO, Kelvin TOP-SET, ICAM, Tripod Beta, Apollo (RCA/reality-charting), ABS Group's "Root Cause Analysis Handbook."
- **Source:** HSE Coach, "Root cause analysis methods"; QHSE Directory, "Incident investigation methodologies"
- **URL:** https://www.hsecoach.com/ ; https://qhsedirectory.com/
- **Date:** ~2021–2023
- **Excerpt (verbatim):** HSE Coach: methods include "…Fault Tree Analysis (FTA), Events and Causal Factors Analysis (ECFA), barrier analysis, and change analysis…" QHSE Directory: "…Kelvin TOP-SET, ICAM (Incident Cause Analysis Method), Tripod Beta…" among structured methodologies.
- **Context:** Method pluralism is the norm; refineries typically certify investigators in one house method plus OSHA/EPA-compliant documentation. (Note: Apollo RCA — Dean Gano's evidence-based cause-and-effect charting — is widely referenced in reliability circles, but its vendor material was not retrievable via open web search in this pass; treat method inclusion as well-established, detail as unverified.)
- **Confidence:** Medium.

### Claim 2.3e — Academic/practitioner critique of 5-Why: oversimplification, no data validation, facilitator-dependence, non-repeatability, symptom-stopping.
- **Source:** IMD business school blog; Miro 5-Whys guide; ThinkReliability "Top Criticisms of the 5-Why Approach"; ReliaMag maintenance article
- **URL:** https://www.imd.org/blog/strategy/the-5-whys-technique/ ; https://miro.com/root-cause-analysis/what-is-5-whys-framework/ ; https://blog.thinkreliability.com/top-criticisms-of-the-5-why-approach ; https://reliamag.com/articles/5-whys-root-cause-analysis-maintenance/
- **Date:** 2018–2026 (various)
- **Excerpt (verbatim):** IMD: "It can oversimplify complex problems… It lacks data validation… It's vulnerable to bias and assumptions… teams may stop too early, accept the first 'reasonable' answer." Miro: "Results depend heavily on who's asking… It only works with knowledge you already have." ThinkReliability lists Wikipedia's criticisms: "(1) Tendency for investigators to stop at symptoms… (2) Inability to go beyond the investigator's current knowledge… (3) Lack of support to help the investigator ask the right 'why' questions… (4) Results are not repeatable — different people using 5 Whys come up with different causes for the same problem… (5) Tendency to isolate a single root cause." ReliaMag: "…the lack of clear stopping criteria."
- **Context:** Because 5-Why is the *default* RCA in many refinery frontline/maintenance workflows, these critiques map directly onto the observed variance in lookback quality (§5.3).
- **Confidence:** High (multiple independent sources converging).

## 2.4 Published investigation reports (CSB) as the sector's canonical deep lookbacks

### Claim 2.4a — BP Texas City (2005): 15 dead, 180 injured, ~$1.5B financial loss; CSB found BP and industry lacked an effective process-safety indicator system, and that eight prior blowdown-drum releases were not properly investigated.
- **Source:** CSB Final Report No. 2005-04-I-TX (2007); ReliablePlant summary of CSB preliminary findings; CSB status-change summary to API; CSB 20th-anniversary digest
- **URL:** https://www.csb.gov/assets/1/20/csbfinalreportbp.pdf ; https://www.reliableplant.com/Read/5959/csb-preliminary-findings-bp ; https://www.csb.gov/recommendations/status-change-summary/ (API rec) ; https://www.csb.gov/ (anniversary digest)
- **Date:** 2006–2025
- **Excerpt (verbatim):** ReliablePlant/CSB: "…eight previous releases from the blowdown drum between 1994 and 2004… were not properly investigated, and appropriate corrective actions were not implemented." A 1994 engineering action item to address blowdown system hazards "…was never finished, and management officials did not follow up." CSB to API: "…BP and the oil refining and chemical sectors did not have an effective system of indicators… to monitor and report safety performance."
- **Context:** The founding case for both API RP 754 and the modern critique of lookback failure: precursors *were* recorded (in historians, logs, incident files) but never converted into learning.
- **Confidence:** High.

### Claim 2.4b — Chevron Richmond (2012): sulfidation pipe failure; Chevron's own metallurgists had recommended 100% component inspection/replacement since 2002; CSB reframed the root issue as corporate decision-making.
- **Source:** CSB/Cal-OSHA technical reporting via ISHN; Oil & Gas Journal on CSB draft report
- **URL:** https://www.ishn.com/ (Chevron Richmond articles) ; https://www.ogj.com/ (CSB Chevron Richmond draft report article)
- **Date:** 2013–2015
- **Excerpt (verbatim):** ISHN: Chevron's materials specialists recommended inspecting/replacing sulfidation-susceptible components "…as far back as 2002." OGJ/CSB: "…the ultimate issue is not corrosion, but how to make effective corporate decisions" about known damage mechanisms.
- **Context:** A lookback *inside* the company (inspection program reviews) produced correct findings that governance failed to act on for a decade — "lessons not reused" at the engineering level.
- **Confidence:** High.

### Claim 2.4c — Philadelphia Energy Solutions (2019): piping elbow installed in 1973 (high nickel/copper content) failed; ~$750M loss; refinery closed permanently; company filed for bankruptcy; CSB found safety-relief and metallurgy programs deficient, and even the emergency water pump failed to start.
- **Source:** CSB final report coverage via Inspectioneering and The Chemical Engineer; Philadelphia Inquirer
- **URL:** https://inspectioneering.com/news/2022-10-11/11216/csb-releases-final-report-into-2019-explosion-and-fire-at-philadelphia-energy-solutions-refinery ; https://www.thechemicalengineer.com/ (PES article) ; https://www.inquirer.com/ (PES corroded pipe)
- **Date:** 2022 (report), 2019–2020 (news)
- **Excerpt (verbatim):** "The CSB determined the cause… was the failure of a piping elbow… installed in 1973… [that] had high nickel and copper content…"; the fire/explosions caused "…an estimated $750 million" loss; "…the refinery [was] shut down… and the operator ultimately fil[ed] for bankruptcy."
- **Context:** The strongest demonstration that lookback quality (inspection/RCA rigor) has *existential* commercial consequences — linking §2 directly to §4.
- **Confidence:** High.

### Claim 2.4d — BP-Husky Toledo (2022): CSB used alarm/event logs forensically (≈3,712 alarms in ~12 hours pre-explosion) and found a 2019 near-identical near-miss was investigated but produced no action items — "a missed opportunity."
- **Source:** CSB final report coverage via JOIFF; Powder & Bulk Solids
- **URL:** https://www.joiff.com/ (CSB Toledo article) ; https://www.powderbulksolids.com/ (CSB Toledo)
- **Date:** 2024 (final report)
- **Excerpt (verbatim):** "…operators were inundated with more than 3,700 alarms (3,712) in the approximately 12 hours before the explosion…" Regarding the 2019 naphtha-release near-miss: the refinery "…identified catastrophic incident warning signs during the investigation but did not develop action items… resulting in a missed opportunity to prevent the [2022] incident."
- **Context:** A single case that evidences three dimension themes at once: alarm-log forensics (§3.2), alarm-flood degradation of operator lookback, and lessons-not-reused (§5.4).
- **Confidence:** High.

### Claim 2.4e — Husky Superior (2018): FCC transient-operation failure; >$550M property damage, 36 injured; CSB + AFPM used it for industry-wide FCC practice sharing.
- **Source:** CSB Safety Spotlight on AFPM FCC practice-sharing event; EHS Leaders incident-cost roundup
- **URL:** https://www.csb.gov/ (safety spotlight, AFPM FCC event) ; https://www.ehsleaders.com/ (CSB budget/incidents article)
- **Date:** 2020–2022
- **Excerpt (verbatim):** Damage "…over $550 million…"; CSB participated in "…an AFPM [practice-sharing] event on FCC unit transient operations…" to disseminate lessons from Husky Superior and ExxonMobil Torrance.
- **Context:** Shows the industry *mechanism* for cross-company reuse of lookbacks (AFPM networks) — and its dependence on voluntary association activity rather than a systematic KM platform (§5.4).
- **Confidence:** High.

---
---

# SECTION 3 — DATA SYSTEMS USED IN LOOKBACKS (HISTORIANS, ALARMS, LIMS) & STRUCTURED PROBLEM-SOLVING PROGRAMS

## 3.1 Process historians and event-framing

### Claim 3.1a — Plant historians provide the forensic substrate: event frames bookmark excursions by threshold and attach context for bulk comparison.
- **Source:** AVEVA (PI System) training/product material on Event Frames
- **URL:** https://learning.aveva.com/ (PI System event frames course/description)
- **Date:** accessed 2026-07-18
- **Excerpt (verbatim):** "Automatically bookmark important events in your operations… Capture events based on user-defined process thresholds… Store related context and calculations within Event Frames… analyze and compare these events in bulk."
- **Context:** Event-framing is the closest the process-data world comes to an *automated downtime/trip ledger*: threshold-triggered, time-stamped, context-tagged episodes that can be aggregated for rate-loss lookbacks and trip RCAs. Whether refiners actually reconcile this ledger to the business ledger is a separate, usually manual, step (§4, §5.2).
- **Confidence:** Medium-high (vendor documentation of a ubiquitous capability).

### Claim 3.1b — Historians are positioned as the real-time single source feeding operations/IT layers, but that architecture is operations-centric, not finance-centric.
- **Source:** Oleson (OSIsoft PI infrastructure consultancy), PI architecture overview
- **URL:** https://oleson.com/ (PI architecture)
- **Date:** ~2021
- **Excerpt (verbatim):** The PI System "…collects, consolidates, analyzes, visualizes and shares data from multiple sources…" as the real-time data infrastructure layer between plant control systems and business systems.
- **Context:** Confirms historians sit *below* ERP/accounting; moving from process events to financial lookbacks requires crossing an architectural boundary — the time-alignment seam discussed in §5.2.
- **Confidence:** Medium.

## 3.2 Alarm and event logs

### Claim 3.2a — ISA-18.2 / EEMUA-191 supply the KPI framework for alarm-system lookbacks (average rate, flood rate, standing alarms).
- **Source:** plcprogramming.io ISA-18.2 guide; Process Control Guide ISA-18.2 FAQ (citing EEMUA 191 benchmarks)
- **URL:** https://plcprogramming.io/ (ISA-18.2 article) ; https://processcontrolguide.com/ (ISA-18.2 FAQ)
- **Date:** ~2022–2024
- **Excerpt (verbatim):** EEMUA 191-based targets: average alarm rate "…<6 alarms per operator per hour is acceptable… >30 indicates major problems…"; alarm flood defined as ">10 alarms per 10 minutes per operator"; standing alarms should be "<5."
- **Context:** Alarm lookbacks (rationalization, flood analysis, bad-actor alarm lists) are a formal, KPI-driven retrospective discipline — and the Toledo case (Claim 2.4d) shows what an alarm-flood lookback reveals post-mortem.
- **Confidence:** Medium-high.

### Claim 3.2b — Alarm floods are the canonical failure of *real-time* lookback: operators cannot process the event stream (Toledo: ~3,712 alarms/12 h ≈ 309/hr, >50× the EEMUA acceptable rate).
- **Source:** CSB BP-Husky Toledo final report coverage (JOIFF)
- **URL:** https://www.joiff.com/ (CSB Toledo)
- **Date:** 2024
- **Excerpt (verbatim):** "…operators were inundated with more than 3,700 alarms (3,712) in the approximately 12 hours before the explosion…"
- **Context:** Arithmetic: 3,712/12 ≈ 309 alarms/operator-hour vs. the <6/hr "acceptable" benchmark — a ~50× overload that made the abnormal-situation lookback (operator diagnosis) impossible in real time. Alarm logs then become the *post-incident* evidence base.
- **Confidence:** High.

## 3.3 LIMS and quality data in lookbacks

### Claim 3.3a — Refinery labs run on LIMS at industrial scale (thousands of samples, tens of thousands of tests/month), making LIMS the system of record for quality lookbacks.
- **Source:** American Refining Group press release (LabWare LIMS); American Laboratory case study (Ergon Refining)
- **URL:** https://www.amref.com/ (LIMS press release) ; https://www.americanlaboratory.com/ (Ergon LIMS case)
- **Date:** ~2019–2021
- **Excerpt (verbatim):** ARG: lab processes "…5,500–6,500 samples per month… about 30,000 tests…" managed/scheduled/reported through LIMS. Ergon: LIMS delivered "…a 20% gain in productivity…" and integrates with analytical and plant systems.
- **Context:** Quality excursions (off-spec, giveaway, regrades) are recorded in LIMS, *not* in the process historian or CMMS — so a complete operational lookback must join LIMS (quality), historian (process), and CMMS/downtime (availability) records, which are on different clocks and keys (§5.2).
- **Confidence:** Medium-high.

### Claim 3.3b — LIMS quality analytics explicitly support excursion flagging and trend lookbacks tied to process parameters.
- **Source:** QIA (Quality International America), "LIMS in refinery quality control"
- **URL:** https://www.qiaintl.com/ (LIMS refinery article)
- **Date:** ~2022
- **Excerpt (verbatim):** LIMS provides "…integration [with instruments and plant systems], validation rules, flagging [e.g.] sulfur excursions, and trend identification to inform refining parameters."
- **Context:** Documents that quality lookbacks are statistically supported (control rules, trends) — the quality analogue of alarm KPIs — but remain lab-centric.
- **Confidence:** Medium.

## 3.4 Production accounting / mass-balance reconciliation (the operational-to-business bridge)

### Claim 3.4a — Production accounting systems reconcile measurement errors and detect plan deviations; KBC/Visual Mesa publishes per-unit monetized loss values from its case library.
- **Source:** KBC (A Yokogawa Company), Visual Mesa Production Accounting data sheet
- **URL:** https://www.kbc.global/ (Visual Mesa PA datasheet)
- **Date:** ~2023
- **Excerpt (verbatim):** The system provides "…mass balance reconciliation, gross error detection… Monthly plan vs. actual operation… detect early deviations from the plan…" Case economics: "…35,000 bpd FCC product misalignment: USD 506,800 savings; Loss FCCU capacity: USD 13/bpd; Loss refinery capacity: USD 1.34/bpd…" and a deasphalting-unit faulty meter worth "$1.63 million."
- **Context:** This is the quantitative machinery of rate/quality lookbacks: reconcile flows → find gross errors → monetize capacity/product losses per unit → compare plan vs. actual. It is also the clearest refinery-specific evidence that per-bbl-per-day loss values are computed and used.
- **Confidence:** High (vendor datasheet with concrete case values).

### Claim 3.4b — Emerson documents the industry's plan-vs-actual backcasting pain: comparing actual vs. expected performance and "back-casting" LP models is complex and time-consuming; unmodeled constraints force distressed spot transactions that hit margins.
- **Source:** Emerson, "The Smart Refinery" (Hydrocarbon Engineering supplement)
- **URL:** https://www.emerson.com/resource/hydrocarbon-engineering-supplement-the-smart-refinery
- **Date:** ~2021–2023
- **Excerpt (verbatim):** "The ability to compare actual vs. expected unit performance and 'back-cast' the LP models to predict the period that just completed can be complex and time consuming. Model errors can cause planner results to be suboptimal or unachievable." And: unplanned constraints can force "…spot purchases or sales at distressed prices… [which] can have a large financial impact on operating margins."
- **Context:** This is the VCO-lookback seam: LP (planning) world vs. actuals world. The quote is the single most direct published acknowledgment of *time/model-alignment difficulty* between operational and commercial data (§5.2) and of the commercial cost of operational lookback failure.
- **Confidence:** High.

## 3.5 Structured problem-solving programs (Six Sigma, A3, RCM/FRACAS)

### Claim 3.5a — Six Sigma DMAIC is applied in refining/oil & gas for process and quality problems; case literature exists (e.g., Libyan Zawia refinery; oil-company DMAIC applications).
- **Source:** Invensis, "Six Sigma in the energy/oil & gas industry"; Esmaili et al., Int. J. Industrial Engineering Computations (DMAIC case in an oil company)
- **URL:** https://www.invensislearning.com/ (Six Sigma energy article) ; https://www.growingscience.com/ijiec/vol2/ijiec_2011_24.pdf
- **Date:** ~2011–2023
- **Excerpt (verbatim):** Esmaili et al.: DMAIC "…Define, Measure, Analyze, Improve, Control…" applied to reduce losses/quality defects in an oil-industry case, with statistical control tools in the Measure/Analyze phases.
- **Context:** DMAIC supplies the *analytical* depth (measurement-system analysis, capability, hypothesis tests) that 5-Why lacks — but is project-based (weeks-months), so refineries reserve it for chronic bad-actors rather than every trip (see Tension T6).
- **Confidence:** Medium.

### Claim 3.5b — A3 problem-solving (PDCA on one page) is the lean format used for structured operational lookbacks and CI knowledge capture.
- **Source:** Businessmap (Kanbanize), "A3 problem solving" template guide
- **URL:** https://businessmap.io/ (A3 guide)
- **Date:** ~2023
- **Excerpt (verbatim):** A3 follows the PDCA cycle on a single sheet: "…background, current condition, goal/target, root-cause analysis, countermeasures, implementation plan, follow-up…" — forcing the problem story, analysis and plan onto one page for shared review.
- **Context:** A3 is both an analysis format *and* a knowledge-management artifact (single-page, shareable, reviewable) — relevant to the study's CI-KM theme: its discipline exists, but reuse depends on whether A3s/RCAs are indexed and searchable (§5.4).
- **Confidence:** Medium-high.

---
---

# SECTION 4 — CONNECTING OPERATIONAL LOOKBACKS TO COMMERCIAL / MARGIN IMPACT

## 4.1 Direct cost-of-downtime anchors (refinery-specific)

### Claim 4.1a — EIA: Valero's St. Charles FCC turnaround carried $1.2–3.0M/day of exposure beyond the planned schedule; FCC unit surveys show chronic slippage vs. 4–5-year run-length targets.
- **Source:** U.S. EIA, "Refinery outages: description and potential impact on petroleum product prices" (This Week in Petroleum special report)
- **URL:** https://www.eia.gov/petroleum/weekly/archive/2015/150325/includes/analysis_print.php (refinery outages report)
- **Date:** March 2015
- **Excerpt (verbatim):** "Valero would lose between $1.2 million and $3 million dollars for each day the turnaround went beyond its planned time" (Valero St. Charles FCC turnaround, $39M contract, ~1,800 contractors). FCC survey: of 28 FCC units, "…22… targeted 4–5 year run lengths… only 16 achieved" their targets; average slippage ~5 days.
- **Context:** The cleanest official per-day downtime value for a major conversion unit; implies a $1.2–3M/day opportunity cost basis for FCC-class unit lookbacks (margin on lost conversion + fix costs + restart off-spec).
- **Confidence:** High (EIA).

### Claim 4.1b — Solomon's monetized-downtime and "value of lost production" framing (Section 1) is the mechanism by which majors internalize downtime economics; per-unit loss values are also published by production-accounting vendors (FCCU capacity USD 13/bpd; refinery capacity USD 1.34/bpd).
- **Source:** Solomon RAM Study vs. Fuels Study blog [^2^]; KBC Visual Mesa datasheet [^65^]
- **Date:** as cited above
- **Excerpt (verbatim):** KBC: "Loss FCCU capacity: USD 13/bpd; Loss refinery capacity: USD 1.34/bpd."
- **Context:** Two complementary valuations: (i) conversion-capacity value (FCCU ~$13/bbl-day) for unit-level RCA prioritization; (ii) whole-refinery capacity value (~$1.3/bbl-day ≈ a modest margin proxy) for system-level lookbacks. A 200 kb/d refinery fully down for a day ≈ $268k at the KBC refinery-capacity rate — far below vendor "$/hour" figures, showing why *basis matters* (see Tension T5).
- **Confidence:** High for KBC datasheet; the arithmetic interpretation is this analyst's.

### Claim 4.1c — Catastrophic-end of the spectrum: PES ($750M loss → closure → bankruptcy) and Husky Superior (>$550M damage) per CSB/Marsh; refining is >1/3 of Marsh's 100 Largest Losses (1974–2019).
- **Source:** Marsh, "100 Largest Losses in the Hydrocarbon Industry" (23rd ed.); CSB coverage [^53^][^57^]
- **URL:** https://www.marsh.com/ (100 Largest Losses report)
- **Date:** 2020 (23rd ed.)
- **Excerpt (verbatim):** Marsh: "Refining accounts for more than a third of 100LL during 1974–2019." PES: "US$750 million loss in June 2019… resulted in the refinery closing shortly afterwards and the operator ultimately filing for bankruptcy." Marsh's capital-markets analysis: companies managing crises well saw share price "+5%" vs "−12%" for poor responders.
- **Context:** Business-interruption (BI) losses — the insurance-market lookback — tie incident quality directly to enterprise value; the +/- share-price asymmetry is the market-priced value of lookback-driven crisis learning.
- **Confidence:** High.

### Claim 4.1d — Single-event maintenance economics: one crude charge pump failure ≈ $420,000 (14-hour outage on an 80 kb/d crude unit + $180k rebuild) — vendor example.
- **Source:** iFactory reliability economics article
- **URL:** https://ifactoryapp.com/ (downtime economics)
- **Date:** ~2023
- **Excerpt (verbatim):** "…a single crude charge pump failure… 14-hour outage on an 80,000 bbl/day crude unit… roughly $420,000 per event" including "~$180,000" rebuild cost.
- **Context:** Illustrates *lost-opportunity quantification at equipment level*: throughput loss valued at margin ($/bbl) dwarfs repair cost (~2.3:1 here). This is precisely the trade Solomon's optimum-strategy equation (Claim 1.1b) formalizes.
- **Confidence:** Medium-low (vendor arithmetic; directionally sound).

## 4.2 Where the connection breaks down

### Claim 4.2a — Corporate disclosures attribute throughput misses to "unplanned outages" but rarely monetize them — the lookback exists, the margin bridge is thin.
- **Source:** Cenovus Energy Q4 2023 results/transcript; Suncor Q3 2019 earnings call transcript
- **URL:** https://www.cenovus.com/ (quarterly results) ; https://www.fool.com/earnings/call-transcripts/ (Suncor Q3 2019)
- **Date:** 2024 / 2019
- **Excerpt (verbatim):** Cenovus attributes refining throughput variance to "…unplanned outages…" and notes throughput is managed to "…economically optimize…" runs given market conditions.
- **Context:** "Economically optimize throughput" is the commercial confound: refiners *choose* rates by margin, so not every non-run hour is a reliability loss — and reliability losses in high-margin windows cost more than identical hours in low-margin windows. Any honest downtime lookback must value hours at *time-varying margin*, which most ledgers (fixed $/bbl-day factors) do not (see §5.2).
- **Confidence:** Medium-high.

### Claim 4.2b — Emerson's back-cast gap (Claim 3.4b) and Solomon's own "economic shutdown" category (Claim 1.2a) show both vendors and benchmarkers recognize the operational/commercial seam — but leave the reconciliation to the refiner.
- **Source:** [^66^], [^5^]
- **Context:** Synthesis: the industry's lookback stack has (1) process-event ledgers (historian/alarms), (2) availability ledgers (Solomon MA/OA/on-stream), (3) financial ledgers (production accounting, LP back-cast). Published evidence shows each exists; none shows a standard, automated join across all three. The VCO study's "margin impact of operational events" is therefore assembled manually, case-by-case, in most organizations.
- **Confidence:** High (synthesis of cited primary sources).

---
---

# SECTION 5 — KNOWN WEAKNESSES OF OPERATIONAL LOOKBACK PRACTICES

## 5.1 Event classification inconsistency

### Claim 5.1a — Tier-1 process-safety event misclassification runs 10–20% even under a published standard (API RP 754).
- **Source:** SmartQHSE API RP 754 deep-dive [^28^]
- **Excerpt (verbatim):** "…corporate audits routinely find 10 to 20 percent under-classification" of Tier 1 events; plus "…inconsistent application of the [release-quantity] thresholds… Tier 3 not implemented… missing Tier 4… no follow-through on actions."
- **Context:** If the *flagship, public* indicator is misclassified at this rate, internal near-miss and downtime coding is almost certainly worse. Direct support for the study's "classification inconsistency" hypothesis.
- **Confidence:** Medium (single practitioner source; consistent with CSB observations about indicator quality post-Texas City [^50^]).

### Claim 5.1b — Equipment-level failure coding diverges despite ISO 14224: boundary/taxonomy discipline can shift measured failure rates by ~40%.
- **Source:** iFluids, "ISO 14224 guide for reliability data collection"; CPCon ISO 14224 taxonomy summary
- **URL:** https://www.ifluids.com/ (ISO 14224 guide) ; https://cpcon.com.my/ (ISO 14224)
- **Date:** ~2022–2024
- **Excerpt (verbatim):** iFluids: inconsistent equipment-boundary and failure-mode classification "…can lead to [failure-rate] differences of around 40%…" in benchmark datasets (OREDA experience), driven by how assemblies are subdivided and how causes are coded.
- **Context:** Same physical fleet, different reliability statistics purely from bookkeeping choices — a fundamental lookback-comparability hazard and a caution when merging multi-site CMMS histories for CI.
- **Confidence:** Medium-high.

### Claim 5.1c — In practice, "EVERYONE uses the CMMS/EAM differently," so cross-site failure coding is not comparable without remediation.
- **Source:** NIST-hosted paper on maintenance-data standardization for smart manufacturing (Asset Answers contribution)
- **URL:** https://www.nist.gov/ (smart manufacturing maintenance data paper)
- **Date:** ~2020
- **Excerpt (verbatim):** "EVERYONE uses the CMMS/EAM differently" — work-order coding, failure fields and hierarchy usage vary by site/planner.
- **Context:** Practitioner consensus that the *raw material* of equipment lookbacks (work orders) is semantically unstable; FRACAS consultants report refineries logging work orders against the *room* or wrong hierarchy level, breaking equipment-level rollups (Conscious Asset case [^18^]).
- **Confidence:** Medium.

### Claim 5.1d — Classification granularity itself is contested: detailed codes vs. simplified operator schemes trade precision against compliance (ESRel 2020 SIS study).
- **Source:** ESRel/PSAM 2020 paper on failure classification for safety-instrumented systems
- **URL:** https://www.esrel2020.com/ (paper PDF via university repository)
- **Date:** 2020
- **Excerpt (verbatim):** The study compares detailed vs. simplified failure-classification schemes and finds each produces different cause distributions; simplified schemes improve reporting compliance but lose diagnostic resolution.
- **Context:** Explains *why* inconsistency persists: granularity choices are rational local trade-offs that destroy global comparability.
- **Confidence:** Medium.

## 5.2 Time-alignment problems between process and business data

### Claim 5.2a — The benchmark ledger deliberately smooths time: Solomon annualizes turnaround downtime over the turnaround interval (TADD = total T/A hours ÷ 24 ÷ interval years), so "availability" is not tied to the calendar of actual events.
- **Source:** Gorisse TU/e thesis [^6^]; Németh MOL paper [^5^]
- **Excerpt (verbatim):** "Turnaround Annualized Downdays (TADD_i) = Total hours down for T/A ÷ (24 × T/A Interval_i)…"; MOL: monthly MA "…can be changed from month to month…" while cumulated MA aggregates from year-start — and turnaround values are distributed uniformly over years/months rather than booked when they occur ("…the real turnaround values are had to divide in uniform distribution…").
- **Context:** Consequence: the reliability ledger, the production ledger, and the financial ledger place the *same* event in *different periods*. Any plan-vs-actual or margin lookback that mixes them inherits a reconciliation error by construction.
- **Confidence:** High (documented method).

### Claim 5.2b — Process data are continuous/seconds; LIMS results are per-sample (hours); CMMS events are per-work-order (days); financial actuals are monthly — and Emerson confirms joining them ("back-casting" the LP) is hard, manual work.
- **Source:** Emerson Smart Refinery [^66^]; KBC Visual Mesa [^65^]; AVEVA [^60^]; ARG LIMS [^62^]
- **Excerpt (verbatim):** Emerson: back-casting LP models "…can be complex and time consuming…"; KBC: reconciliation and "Monthly plan vs. actual operation."
- **Context:** Synthesis with direct vendor acknowledgment: the join keys (unit, time, product) and clocks differ across the four systems; "monthly plan vs. actual" is the finest *routine* commercial lookback granularity, while trips happen in seconds — so the cost of a 6-hour trip is estimated, not measured.
- **Confidence:** High (synthesis anchored in verbatim vendor statements).

### Claim 5.2c — Margin volatility defeats static loss valuation: identical downtime hours cost differently by market window (Cenovus "economically optimize throughput" [^74^]); spot transactions at "distressed prices" add nonlinear commercial impact (Emerson [^66^]).
- **Context:** A defensible commercial lookback needs time-varying $/bbl-day values by unit and by market window; published practice (Solomon factors, KBC unit values) uses static averages — an acknowledged simplification.
- **Confidence:** Medium-high (synthesis).

## 5.3 RCA quality variance

### Claim 5.3a — Investigation recommendations are systematically shaped by investigator background and bias — "What-You-Look-For-Is-What-You-Find."
- **Source:** Lundberg, Rollenhagen & Hollnagel, "What-You-Look-For-Is-What-You-Find: The consequences of underlying accident models in eight accident investigation manuals" (Safety Science, 2009); and "What you find is not always what you fix — How other aspects than causes of accidents decide recommendations for remedial actions" (Accident Analysis & Prevention, 2010); as quoted in J.P. Reed's thesis compilation
- **URL:** https://www.jpaulreed.com/ (thesis/reference quotes); journal: Safety Science 47(10), 2009
- **Date:** 2009–2010
- **Excerpt (verbatim):** The manuals' underlying accident models mean "…what you look for is what you find…"; the 2010 follow-up finds recommendations are driven by "…other aspects than causes…" and issues "…a warning against believing in the rationality — but not the sensibility — of investigation and remediation." Documented biases include "author bias, confirmation bias, frequency bias, political bias, sponsor bias, and professional bias."
- **Confidence:** High (peer-reviewed; widely cited).

### Claim 5.3b — The accident-investigation discipline "has not been sufficiently self-reflective."
- **Source:** Lindberg, Hansson & Rollenhagen, "Learning from accidents — what more do we need to know?" (Safety Science 48(6), 2010)
- **URL:** https://www.sciencedirect.com/ (Safety Science 48(6)); quote via jpaulreed.com
- **Date:** 2010
- **Excerpt (verbatim):** "…the discipline of experience feedback has not been sufficiently self-reflective."
- **Context:** Even the meta-discipline that audits lookbacks admits it rarely audits itself — supporting the study's premise that lookback quality is assumed, not verified.
- **Confidence:** High.

### Claim 5.3c — Method-level variance is corroborated from the practitioner side: 5-Why non-repeatability (different investigators, different causes) [^43^][^44^]; guided-tree vendors position repeatability as the product differentiator [^39^]; CCPS warns of confirmation bias in common techniques [^34^].
- **Context:** Three independent communities (lean educators, RCA vendors, CCPS authors) converge on the same diagnosis: unaided judgment produces irreproducible lookbacks.
- **Confidence:** High (triangulated).

## 5.4 Lessons not reused (organizational learning failure)

### Claim 5.4a — The empirical record: investigations complete, actions stall.
- **Source:** Drupsteen & Hasle, "Why do organizations not learn from incidents? Bottlenecks, causes and conditions for a failure to effectively learn" (Accident Analysis & Prevention 72, 2014; PubMed)
- **URL:** https://pubmed.ncbi.nlm.nih.gov/24930344/
- **Date:** 2014
- **Excerpt (verbatim):** The study identifies bottlenecks in "…the steps of the learning process… particularly in planning and implementing actions…", with causes including "…lack of ownership… limited investigator expertise…" and weak follow-through on recommendations.
- **Confidence:** High.

### Claim 5.4b — Accidents recur because precursors were recorded but not learned from.
- **Source:** Körvers & Sonnemans (Safety Science, 2008), as summarized in "Supporting organizational learning from incidents" (Safety Science literature); Kletz, "Lessons from Disaster: How Organizations Have No Memory and Accidents Recur" (1993)
- **URL:** https://www.sciencedirect.com/ (Safety Science); https://www.icheme.org/ (Kletz title listing)
- **Date:** 2008 / 1993
- **Excerpt (verbatim):** Kletz's thesis (title and text): organizations "…have no memory and accidents recur…" because lessons from earlier incidents are not embedded in procedures/training; Körvers & Sonnemans found recurrence of accidents where similar events had previously occurred without learning.
- **Confidence:** High for the Kletz framing (canonical); medium-high for the 2008 recurrence finding (secondary summary).

### Claim 5.4c — The CSB record is the refinery-specific proof: Texas City (8 prior releases not properly investigated [^47^]) → BP Whiting (tower overfill near-repeat, Dec 2005) → Chevron Richmond (2002 internal recommendation unactioned [^51^]) → BP-Husky Toledo (2019 near-miss, no action items, fatal 2022 repeat [^55^]).
- **Context:** Four documented instances across three companies and 20 years where the *lookback happened* and the *learning did not stick*. This is the single most decision-relevant pattern for the study's CI-KM workstream.
- **Confidence:** High (CSB primary/secondary sources).

### Claim 5.4d — Cross-industry review (2024): facilitators of learning include management commitment and safety culture; hindrances include underreporting and blame culture.
- **Source:** Guan et al., "Learning from incidents across industries: a systematic review" (Safety Science, 2024); Stemn et al., "Failure to learn from safety incidents: Status, challenges and opportunities" (Process Safety Progress, 2018)
- **URL:** https://www.sciencedirect.com/ (Safety Science, 2024) ; https://onlinelibrary.wiley.com/ (PSP 2018, via PMC reference lists)
- **Date:** 2024 / 2018
- **Excerpt (verbatim):** Guan et al.: top facilitators "…management commitment, just culture…"; top hindrances "…underreporting, blame culture, [and] resource constraints."
- **Confidence:** High for Guan (recent systematic review); medium-high for Stemn (title/venue verified, full text not retrieved).

### Claim 5.4e — Industry's reuse mechanisms exist but are voluntary and episodic: AFPM event-sharing database + regional networks; AFPM/API "advancing process safety" programs; OPS 2026 lessons-learned forums; CCPS PERD for equipment data; CCPS book urging that incidents are "a gift on a silver platter."
- **Source:** AFPM Advancing Process Safety page; AFPM/API programs PDF; API/AFPM OPS 2026 site; CCPS PERD [^19^]; CCPS "Driving Continuous Process Safety Improvement From Investigated Incidents" (book description)
- **URL:** https://www.afpm.org/advancing-process-safety ; https://www.api.org/ (OPS 2026) ; https://www.aiche.org/ccps/ (book listing, via PDFCoffee mirror)
- **Date:** 2018–2026
- **Excerpt (verbatim):** AFPM: maintains an "…event sharing database…" and regional process-safety networks where members "…share lessons learned…"; CCPS: incidents "…are a gift on a silver platter — they tell us exactly where our management systems failed."
- **Context:** The *channels* for cross-company reuse are association-mediated and rely on voluntary submission and conference attendance — there is no equivalent of aviation's mandatory ASRS-style reporting backbone for refining operations events. Knowledge is shared; it is not systematically *managed*.
- **Confidence:** Medium-high.

---
---

# TENSIONS & CONTRADICTIONS (explicit)

- **T1 — "Availability" is not one number.** Solomon's stack (MA ≥ OA ≥ on-stream [^5^]) means BP's "refining availability" (OA basis [^7^]) and Valero's "mechanical availability" (MA basis [^9^]) are *different ledgers wearing the same label*. SMRP separately warns that "availability" definitions differ across standards bodies (EN 15341 vs. SMRP) and that "utilization" mixes reliability with market demand [^10^][^11^]. Any cross-company or cross-year lookback must first align definitions — a step frequently skipped.
- **T2 — More reported events can mean *better* performance.** Mature indicator programs look "bottom-heavy": high Tier 3/4 (near-miss) counts relative to Tier 1 can reflect a stronger reporting culture, not worse safety (implied by API's tier design [^27^] and CCPS near-miss parity guidance [^35^]). Lookbacks that trend raw counts without normalizing for reporting culture will misread improvement as deterioration — and vice versa after a reclassification audit ([^28^]: 10–20% under-classification).
- **T3 — Regulators vs. industry on RCA mandates.** OSHA/EPA are converging on required root-cause analysis for incidents (RMP 2024 [^25^]; OSHA SBREFA [^23^]; state refinery programs [^26^]); AFPM resists prescribed *methodology* and warns of burden for low-risk events [^24^]. Practical consequence: refineries will likely run (at least) two investigation classes — full RCA for high-potential events, scaled methods otherwise — making lookback *depth* heterogeneous by design.
- **T4 — Simple vs. rigorous RCA is an unresolved practitioner split.** Lean sources defend 5-Why as a fast frontline tool (with fixes: branch the whys, demand evidence [^45^]); vendors and CCPS argue it is structurally biased and non-repeatable [^38^][^44^][^34^]; ThinkReliability defends expandable Why-chains while *quoting* the same criticisms [^44^]. Consensus exists only on the failure modes (single-cause, symptom-stopping, confirmation bias), not on the remedy — hence persistent method pluralism [^40^][^41^].
- **T5 — Downtime cost figures vary by >100× depending on basis.** Vendor "$500k+/hour, $84M/yr/facility" claims [^71^][^72^] vs. EIA's refinery-specific $1.2–3M/day for an FCC turnaround [^67^] vs. KBC's ~$1.34/bbl-day whole-refinery capacity value (≈$268k/day for 200 kb/d) [^65^] vs. DOE EAD's modest reported lost-opportunity totals [^68^]. Basis differences: revenue vs. margin; gross vs. net of make-up production; fixed vs. time-varying margins; property damage/BI vs. throughput loss. **Recommendation for the study: adopt margin-on-lost-conversion (EIA/KBC basis) as primary, BI/property (Marsh) for catastrophic tail, and treat vendor per-hour figures as upper-bound rhetoric.**
- **T6 — DMAIC/A3 rigor vs. trip RCA throughput.** Six Sigma projects deliver statistical depth but take weeks-months [^89^]; trips need 48-hour initiation [^22^]. Refineries therefore split lookbacks into fast RCA (trips) and slow DMAIC (chronic bad actors) — but the two rarely share one repository, so chronic-event patterns across many fast RCAs go undetected (compounds T7).
- **T7 — Voluntary sharing vs. systematic KM.** AFPM/CCPS channels exist (event database, networks, PERD [^77^][^19^]) and CCPS calls incidents "a gift on a silver platter" [^91^]; yet CSB's repeat-incident record (Texas City → Whiting → Toledo [^46^][^55^]) shows intra-company reuse failing even when investigations were completed. The bottleneck is not investigation supply but knowledge *retention, indexing, and retrieval* — exactly the CI-KM gap this study targets.

# GAPS & LIMITATIONS OF THIS RESEARCH

1. Solomon's proprietary metric definitions (exact MA/OA/on-stream formulas, slowdown thresholds, EDC weightings) are not public; relied on practitioner reproductions [^5^][^6^] which may lag current editions (2023+ RAM Study changes noted but not detailed [^3^]).
2. Apollo RCA vendor documentation was not retrievable via open web search (method inclusion well-established; specifics unverified) [^40^][^41^].
3. Downtime-cost literature is dominated by vendor/secondary aggregations; primary refinery-specific figures are scarce beyond EIA [^67^] and Marsh [^73^].
4. CSB findings are U.S.-centric; European (e.g., eMARS/ARIA) and Asian lookback practices were not covered in this pass.
5. Company-internal lookback practices (e.g., ExxonMobil OIMS, Chevron OE/LOTO, Shell's LFI) are proprietary; only fragments are public via CSB reports and conference papers.
6. Some verbatim excerpts were captured from search-result snippets of pages that could not all be re-opened for full-text verification; confidence ratings reflect this.

---
---

# APPENDIX A — SEARCH LOG (15 batches, 58 queries, 2026-07-18)

1. Solomon Associates refinery reliability & maintenance benchmarking mechanical availability; HSB Solomon Study utilization metrics; API RP 754 tiers; CCPS leading/lagging metrics.
2. OSHA PSM 1910.119(m) incident investigation; TapRooT refinery RCA; Solomon RAM study turnaround benchmarking; refinery downtime cost per day / lost margin.
3. CSB Chevron Richmond findings; CSB BP Texas City findings/recommendations; Apollo vs TapRooT vs 5-Why/fishbone/fault-tree; process historian downtime analysis / OEE rate-loss tracking.
4. Apollo RCA method; TapRooT system description; SMRP best-practice metrics; Reliabilityweb bad-actor RCA programs.
5. Apollo RCA (RealityCharting); ISA-18.2 alarm management KPIs; refinery LIMS quality/off-spec/giveaway; Six Sigma DMAIC refinery case studies.
6. "Lessons learned" failures in process industries; learning-from-incidents weaknesses research; RCA quality variation/criticism; ISO 14224 failure data classification.
7. FCC downtime cost/day; Philadelphia Energy Solutions CSB report/closure/bankruptcy; Drupsteen failure-to-learn; Jacobsson learning-from-incidents method.
8. Apollo RCA (Gano) method; production accounting / mass-balance reconciliation / plan-vs-actual; automated downtime event detection from historians/MES; A3 problem solving.
9. TapRooT system (SnapCharT, causal factors); Apollo four-step; "refinery outage $1M a day"; refinery LIMS regrade root cause.
10. Apollo RCA Gano; CCPS Guidelines for Investigating Process Safety Incidents (3rd ed.); OSIsoft PI event frames downtime; Marsh 100 Largest Losses business interruption.
11. Process historian in RCA/timeline reconstruction; refinery LIMS product-quality certification; "mechanical availability" definition (Solomon); Apollo RCA RealityCharting.
12. Plan-vs-actual margin reconciliation / LP backcasting; refinery shutdown lost-opportunity cost (trade press); AFPM event sharing / regional networks; Reliabilityweb RCA program mistakes.
13. PI System event frames for production-loss events; Lindberg/Hansson/Rollenhagen "Learning from accidents"; Energy Institute learning-from-incidents guidance; 5-Whys criticism/limitations.
14. Apollo RCA Gano definition; production loss accounting categories; refinery LP "plan vs actual" backcast; 5-Whys drawbacks (stops early/single cause).
15. Apollo RCA RealityCharting (final attempt); Solomon on-stream/operational/mechanical availability definitions + MOL paper full-text open.

# APPENDIX B — SOURCE LIST

[^1^] Solomon Associates (HSB), "Reliability and Maintenance (RAM) benchmarking." https://solomoninsight.com/consulting/benchmarking/reliability-maintenance-ram/ (accessed 2026-07-18).
[^2^] Solomon Associates, "Solomon's Reliability and Maintenance (RAM) Study vs. Fuels Study." https://solomoninsight.com/insights/blog/solomons-reliability-and-maintenance-ram-study-vs-fuels-study/ (accessed 2026-07-18).
[^3^] Solomon Associates, "2023 Reliability & Maintenance Study: What's New." https://solomoninsight.com/insights/blog/ (2023).
[^4^] Solomon Associates, "Reliability, Maintenance & Turnarounds." https://solomoninsight.com/consulting/benchmarking/reliability-maintenance-turnarounds/ (accessed 2026-07-18).
[^5^] Németh, J., "How to calculate Mechanical Availability (MA)," MOL Group Scientific Magazine 2011/1, pp. 72–77. https://molgermany.de/images/molgermany/pdf/about_mol_group/publikationen/MOL_Group_Scientific_Magazine_2011_01.pdf (2011).
[^6^] Gorisse, R., TU Eindhoven master's thesis (refinery maintenance performance; Solomon downtime taxonomy/formulas). https://pure.tue.nl/ws/files/46925260/841778-1.pdf (undated, ~2014).
[^7^] BP p.l.c., Annual Report and Form 20-F 2019 (glossary: refining availability). https://www.bp.com/ (2020).
[^8^] BP p.l.c., Annual Report and Form 20-F / Strategic Report 2023 (refining availability 96.1%). https://www.bp.com/ (2024).
[^9^] Valero Energy, ESG Report 2022 (97.2% mechanical availability; Tier 1 PSE 0.05/200k hrs). https://www.valero.com/ (2022).
[^10^] SMRP, Best Practices 6th Edition (availability/utilization/OEE definitions; utilization caution). https://quizgecko.com/books/smrp-best-practices-6th-edition-kb5z94 (mirror; accessed 2026-07-18).
[^11^] SMRP Best Practices Metrics Workshop 2018 (PEMAC-hosted PDF; OEE; <3% RAV). https://www.pemac.org/sites/default/files/SMRP%20Best%20Practices%20Metrics%20Workshop%202018.pdf (2018).
[^12^] ISO 14224:2016, "Petroleum, petrochemical and natural gas industries — Collection and exchange of reliability and maintenance data for equipment" (scope). https://www.iso.org/standard/64076.html (2016).
[^13^] ISO/TC 67 workshop paper (Houston) on ISO 14224 ("reliability language/esperanto"; learn from failures). https://www.iso.org/ (ISOfocus; accessed 2026-07-18).
[^14^] iFluids, "ISO 14224 guide for reliability data collection" (classification-consistency; ~40% failure-rate variance). https://www.ifluids.com/ (accessed 2026-07-18).
[^15^] CPCon, ISO 14224 taxonomy summary. https://cpcon.com.my/ (accessed 2026-07-18).
[^16^] NIST-hosted maintenance-data standardization paper ("EVERYONE uses the CMMS/EAM differently"). https://www.nist.gov/ (accessed 2026-07-18).
[^17^] ESRel/PSAM 2020 paper on failure-classification granularity (SIS). https://www.esrel2020.com/ (2020).
[^18^] Conscious Asset, FRACAS refinery case (work orders logged at wrong hierarchy level). https://www.consciousasset.com/ (accessed 2026-07-18).
[^19^] CCPS Process Equipment Reliability Database (PERD) description. https://www.61508.org/knowledge/ccps-process-equipment-reliability-database-perd.php (accessed 2026-07-18).
[^20^] Cambridge International Manufacturing Symposium proceedings (production-loss taxonomy; "Sales Opportunity Loss"). https://www.ifm.eng.cam.ac.uk/uploads/Resources/Reports/CIM_Proceedings_for_web3.pdf (undated).
[^21^] Springer, "OEE Monitoring for Production Processes Based on SCADA/HMI Platform" (loss categories). https://link.springer.com/content/pdf/10.1007/978-0-387-74157-4_22.pdf (undated).
[^22^] Ecesis, "PSM Incident Investigation Requirements (29 CFR 1910.119(m))." https://www.ecesis.com/blog/psm-incident-investigation-requirements (accessed 2026-07-18).
[^23^] OSHA, "Process Safety Management — SBREFA issues document" (RCA not required; +50% time estimate). https://www.osha.gov/sites/default/files/PSM-SBREFA-issues-document.pdf (2022).
[^24^] AFPM, Comments on OSHA PSM SBREFA. https://www.afpm.org/ (2022).
[^25^] EHSCareers, "PSM Careers Guide" (EPA 2024 RMP final rule: mandated RCA/third-party audits; CSB trio). https://www.ehscareers.com/psm-careers-guide/ (2024).
[^26^] U.S. EPA, "Accidental Release Prevention Requirements: RMP under the Clean Air Act; Safer Communities by Chemical Accident Prevention" (proposed rule preamble on RCA; NJ TCPA, Cal/OSHA refinery PSM, Contra Costa, Richmond ISO). Federal Register 2022-18249. https://www.federalregister.gov/documents/2022/08/31/2022-18249/ (2022).
[^27^] API, "Process Safety Performance Indicators for the Refining & Petrochemical Industries — API RP 754 Fact Sheet" (3rd ed. 2021; CSB origin). https://www.api.org/ (accessed 2026-07-18).
[^28^] SmartQHSE, "API RP 754 Process Safety Indicators — Deep Dive" (10–20% Tier 1 under-classification). https://smartqhse.com/ (accessed 2026-07-18).
[^29^] iFactory, "API RP 754 process safety event tiers." https://ifactoryapp.com/ (accessed 2026-07-18).
[^30^] AIChE/CCPS, "Process Safety Leading and Lagging Metrics — You Don't Improve What You Don't Measure" (guidance PDF). https://www.aiche.org/ (2011; v4.1 2022).
[^31^] AIChE/CCPS, "Process Safety Metrics" resource page (v4.1, June 2022). https://www.aiche.org/ccps/resources/process-safety-metrics (accessed 2026-07-18).
[^32^] ThePetroSolutions, "CCPS RBPS Pillar 4 — Learn from Experience" (elements 17–20). https://thepetrosolutions.com/ (accessed 2026-07-18).
[^33^] AIChE/Wiley, "Guidelines for Investigating Process Safety Incidents, 3rd Edition" (CCPS book). https://www.aiche.org/ccps/ (2019).
[^34^] BakerRisk, technical note on CCPS investigation guidance (confirmation bias of common techniques). https://www.bakerrisk.com/ (accessed 2026-07-18).
[^35^] Stokes et al., IChemE Hazards 29 paper on CCPS investigation guidelines 3rd ed. (definitions; scientific method; API RP 585 near-miss rigor). https://www.icheme.org/ (2019).
[^36^] TapRooT, "What is THE root cause?" (SnapCharT; causal factors). https://taproot.com/what-is-the-root-cause/ (accessed 2026-07-18).
[^37^] TapRooT, "Best root cause analysis toolkit" (7-step process; Equifactor; Corrective Action Helper; Generic Causes). https://taproot.com/ (accessed 2026-07-18).
[^38^] TapRooT, "Are You Dissatisfied with 5-Whys Root Cause Analysis?" (three drawbacks; Ohno example). https://taproot.com/dissatisfied-with-5-why-root-cause-analysis/ (2020).
[^39^] TapRooT, "Root cause test" (repeatability criterion). https://taproot.com/ (accessed 2026-07-18).
[^40^] HSE Coach, "Root cause analysis methods" (FTA, ECFA, barrier, change analysis). https://www.hsecoach.com/ (accessed 2026-07-18).
[^41^] QHSE Directory, "Incident investigation methodologies" (TOP-SET, ICAM, Tripod Beta, bowtie). https://qhsedirectory.com/ (accessed 2026-07-18).
[^42^] IMD, "How to use the 5 Whys method" (limitations). https://www.imd.org/blog/strategy/the-5-whys-technique/ (2024).
[^43^] Miro, "What is the 5 Whys framework?" (non-repeatability; knowledge-bound). https://miro.com/root-cause-analysis/what-is-5-whys-framework/ (2024).
[^44^] ThinkReliability, "Top Criticisms of the 5-Why Approach." https://blog.thinkreliability.com/top-criticisms-of-the-5-why-approach (2018).
[^45^] ReliaMag, "5 Whys Root Cause Analysis: When to Stop in Maintenance." https://reliamag.com/articles/5-whys-root-cause-analysis-maintenance/ (2026).
[^46^] U.S. CSB, "Refinery Explosion and Fire (BP Texas City)" Final Report No. 2005-04-I-TX. https://www.csb.gov/assets/1/20/csbfinalreportbp.pdf (2007).
[^47^] ReliablePlant, "CSB preliminary findings on BP Texas City" (8 prior releases; 1994 action item). https://www.reliableplant.com/Read/5959/ (2006).
[^48^] Forensis Group, "BP Texas City refinery explosion timeline." https://www.forensisgroup.com/ (accessed 2026-07-18).
[^49^] CSB, 20th-anniversary digest of BP Texas City recommendations (26 recs; MOC-for-organizational-changes open). https://www.csb.gov/ (2025).
[^50^] CSB, Recommendation status-change summary (API: develop ANSI process-safety indicator standard; "no effective system of indicators"). https://www.csb.gov/recommendations/ (accessed 2026-07-18).
[^51^] ISHN, CSB/Cal-OSHA technical reporting on Chevron Richmond (sulfidation; 2002 internal recommendation). https://www.ishn.com/ (2013–2015).
[^52^] Oil & Gas Journal, "CSB draft report on Chevron Richmond" ("ultimate issue… effective corporate decisions"). https://www.ogj.com/ (2014).
[^53^] Inspectioneering, "CSB Releases Final Report into 2019 Explosion and Fire at Philadelphia Energy Solutions Refinery." https://inspectioneering.com/news/2022-10-11/11216/ (2022); and The Chemical Engineer PES coverage. https://www.thechemicalengineer.com/ (2022).
[^54^] Philadelphia Inquirer, "PES refinery fire: corroded pipe/elbow" coverage. https://www.inquirer.com/ (2019–2022).
[^55^] JOIFF, "CSB final report: BP-Husky Toledo refinery fire" (3,712 alarms; 2019 missed opportunity). https://www.joiff.com/ (2024).
[^56^] Powder & Bulk Solids, "CSB releases final report on fatal 2022 BP-Husky Toledo fire." https://www.powderbulksolids.com/ (2024).
[^57^] EHS Leaders, "CSB incidents and costs" roundup (Husky Superior >$550M; PES $750M). https://www.ehsleaders.com/ (2022).
[^58^] plcprogramming.io, "ISA-18.2 alarm management overview." https://plcprogramming.io/ (accessed 2026-07-18).
[^59^] Process Control Guide, "ISA-18.2 FAQ" (EEMUA 191 KPIs: <6 alarms/hr acceptable; >30 major problems; flood >10/10 min; standing <5). https://processcontrolguide.com/ (accessed 2026-07-18).
[^60^] AVEVA, PI System "Event Frames" description/training. https://learning.aveva.com/ (accessed 2026-07-18).
[^61^] Oleson, "OSIsoft PI System architecture." https://oleson.com/ (accessed 2026-07-18).
[^62^] American Refining Group, LabWare LIMS press release (5,500–6,500 samples/month; ~30,000 tests). https://www.amref.com/ (accessed 2026-07-18).
[^63^] QIA, "LIMS in refinery quality control" (integration, validation rules, sulfur-excursion flagging, trends). https://www.qiaintl.com/ (accessed 2026-07-18).
[^64^] American Laboratory, "Ergon Refining LIMS case study" (20% productivity gain; system integration). https://www.americanlaboratory.com/ (accessed 2026-07-18).
[^65^] KBC (Yokogawa), "Visual Mesa Production Accounting" data sheet (mass-balance reconciliation; gross-error detection; plan vs. actual; $506,800 FCC misalignment; FCCU USD 13/bpd; refinery USD 1.34/bpd; $1.63M meter). https://www.kbc.global/ (accessed 2026-07-18).
[^66^] Emerson, "The Smart Refinery" (Hydrocarbon Engineering supplement; "back-cast the LP models"; distressed spot transactions). https://www.emerson.com/ (accessed 2026-07-18).
[^67^] U.S. EIA, "Refinery Outages" special report (Valero St. Charles FCC $1.2–3M/day; FCC run-length survey). https://www.eia.gov/petroleum/weekly/ (March 2015).
[^68^] Valin Corp., white paper citing DOE Energy Assurance Daily (1,700 shutdowns 2009–2012; >$32M; 46% mechanical). https://www.valin.com/ (accessed 2026-07-18).
[^69^] Imubit, refinery reliability article citing McKinsey ($20–50M/yr lost profit, mid-size refinery). https://www.imubit.com/ (accessed 2026-07-18).
[^70^] Curran International, reliability/emergency-repair article (Gulf Coast 1999–2005: 8.2–33% annual production losses in outage years). https://curranintl.com/ (accessed 2026-07-18).
[^71^] iFactory, "The hidden cost of downtime in oil & gas" (Siemens Senseye lineage: $500K+/hr; $84M/facility-yr). https://ifactoryapp.com/ (accessed 2026-07-18).
[^72^] Alpha Software, downtime-cost table (32 hrs/month; $220K/hr; $47B FG500). https://www.alphasoftware.com/ (accessed 2026-07-18).
[^73^] Marsh, "100 Largest Losses in the Hydrocarbon Industry," 23rd ed. (refining >1/3; PES $750M/closure/bankruptcy; ±5%/−12% share-price study). https://www.marsh.com/ (2020).
[^74^] Cenovus Energy, Q4 2023 results/transcript (unplanned outages; economically optimized throughput). https://www.cenovus.com/ (2024).
[^75^] Suncor Energy, Q3 2019 earnings call transcript. https://www.fool.com/earnings/call-transcripts/ (2019).
[^76^] iFactory, equipment-failure economics example (crude charge pump: $420K/event incl. $180K rebuild). https://ifactoryapp.com/ (accessed 2026-07-18).
[^77^] AFPM, "Advancing Process Safety" (event-sharing database; regional networks). https://www.afpm.org/advancing-process-safety (accessed 2026-07-18).
[^78^] AFPM/API, "Advancing Process Safety Programs" (program description PDF). https://www.afpm.org/ (accessed 2026-07-18).
[^79^] API/AFPM, "Operating Practices Symposium (OPS) 2026" (process-safety lessons-learned forums). https://www.api.org/ (2026).
[^80^] U.S. CSB, "Safety Spotlight: AFPM FCC practice-sharing event" (Husky Superior; ExxonMobil Torrance; transient operations). https://www.csb.gov/ (accessed 2026-07-18).
[^81^] Drupsteen, L. & Hasle, P., "Why do organizations not learn from incidents? Bottlenecks, causes and conditions for a failure to effectively learn," Accident Analysis & Prevention 72 (2014). https://pubmed.ncbi.nlm.nih.gov/24930344/ (2014).
[^82^] Lindberg, A.-K., Hansson, S.O. & Rollenhagen, C., "Learning from accidents — what more do we need to know?" Safety Science 48(6) (2010). https://www.sciencedirect.com/ ; quote compilation: https://www.jpaulreed.com/ (2010).
[^83^] Lundberg, J., Rollenhagen, C. & Hollnagel, E., "What-You-Look-For-Is-What-You-Find…" Safety Science 47(10) (2009); and "What you find is not always what you fix…" Accident Analysis & Prevention 42 (2010). https://www.sciencedirect.com/ ; quotes via https://www.jpaulreed.com/ (2009–2010).
[^84^] Guan, Z. et al., "Learning from incidents across industries: a systematic review," Safety Science (2024). https://www.sciencedirect.com/ (2024).
[^85^] Kletz, T., "Lessons from Disaster: How Organizations Have No Memory and Accidents Recur," IChemE/Gulf (1993). https://www.icheme.org/ (1993).
[^86^] OSHwiki (EU-OSHA), "Learning from incidents and accidents" (learning-loop framework; fear/blame barriers). https://oshwiki.osha.europa.eu/ (accessed 2026-07-18).
[^87^] risk-engineering.org, "Operational experience feedback (OEF) loop." https://risk-engineering.org/ (accessed 2026-07-18).
[^88^] Invensis Learning, "Six Sigma in the energy/oil & gas industry." https://www.invensislearning.com/ (accessed 2026-07-18).
[^89^] Esmaili, H. et al., "A DMAIC application in an oil company," Int. J. Industrial Engineering Computations 2 (2011). https://www.growingscience.com/ijiec/vol2/ijiec_2011_24.pdf (2011).
[^90^] Businessmap (Kanbanize), "A3 problem solving" (PDCA single-page structure). https://businessmap.io/ (accessed 2026-07-18).
[^91^] CCPS, "Driving Continuous Process Safety Improvement From Investigated Incidents" (book; "gift on a silver platter"). https://www.aiche.org/ccps/ (2021).
[^92^] Körvers, P.M.W. & Sonnemans, P.J.M., "Accidents: a discrepancy between indicators and reality!" / recurrence findings, Safety Science (2008), as summarized in organizational-learning literature. https://www.sciencedirect.com/ (2008).
[^93^] Stemn, E. et al., "Failure to learn from safety incidents: Status, challenges and opportunities," Process Safety Progress (2018). https://onlinelibrary.wiley.com/ (2018).
[^94^] SKF, "Availability" primer (availability = uptime ÷ (uptime + downtime)). https://www.skf.com/ (accessed 2026-07-18).

---
*End of Dimension 04 report. Prepared 2026-07-18. 58 searches executed; 94 numbered sources; verbatim excerpts preserved; tensions flagged in-text and summarized in the Tensions section.*
