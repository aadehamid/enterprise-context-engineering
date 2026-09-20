# Dimension 09 — KPI Misalignment & Inconsistent Metrics in Downstream
## How Conflicting KPIs and Metric Definitions Undermine Performance Evaluation in a Refiner/Marketer

**Study:** Value Chain Optimization (VCO), Lookback/Backcasting, and CI Knowledge Management
**Prepared:** 2026-07-18
**Analyst:** Deep-Research Sub-Agent (Dimension 09)
**Method:** 18 independent web-search queries (≥15 requirement met) across consultancies (BCG, KBC, Energy Aspects), benchmarking bodies (Solomon Associates, APQC), regulators/national agencies (EIA, IEA, EU, ACCC/AIP), academic theses and journals (RGU, Univ. of Gloucestershire, Journal of Tianjin University, arXiv, CNA), vendor/practitioner sources, and trade press. All evidence captured as verbatim excerpts with source, URL, date, and a confidence rating.

**Evidence template used per claim:** Claim / Source / URL / Date / Excerpt (verbatim) / Context / Confidence (high-med-low). Inline citations [^N^] map to the numbered Source List at the end. Tensions and contradictions between sources are flagged explicitly as **TENSION**.

---

# KEY FINDINGS (Summary)

1. **Functional silo optimization is structural, not accidental — the refinery "push" collides with the market "pull."** A refinery is economically driven to maximize throughput and cut unit cost, while depots chase fill rates and logistics chases freight cost — and these goals actively conflict. *"A refinery focuses on maximizing throughput and reducing unit costs. A distribution depot aims for high fill rates to ensure local service. These conflicting key performance indicators (KPIs) drive sub-optimal decisions. What benefits one location can harm the overall enterprise value."* [^1^] The fix proposed is *shared* KPIs that *"must focus on total enterprise value, not local optimization"* — e.g., balancing *"total delivered cost against service levels."* [^1^]

2. **"Margin," "availability," "utilization," and "OTIF" have no single agreed definition, so cross-asset and longitudinal comparison is systematically blocked.** Refining margin is variously gross (product value − crude), net (minus opex, depreciation, other), cash, variable, replacement-cost, or accounting-cost [^9^][^11^][^12^]. BP's own glossary distinguishes *Solomon "operational availability"* (availability net of turnaround + planned downtime) from *"refinery utilization"* (throughput ÷ crude distillation capacity) and *"replacement cost (RC) profit"* (excluding inventory holding gains/losses) — three different things that are routinely conflated [^12^].

3. **Benchmark margin series are region- and configuration-specific, so "margin-per-barrel" is not portable across regions.** The IEA/KBC indicator margins use *different crude benchmarks (WTI / Dated Brent / Dubai), different process configurations, and different cut-point/operating philosophies* — *"Middle distillate make is maximised in the European and Singapore cases while the American refineries have historically maximised gasoline"* — and explicitly warn the yields *"are not typical of modern refineries"* [^13^]. Regional crack conventions differ too (US 3:2:1, NW Europe 5:3:2, Singapore 2:1:1) [^15^][^50^].

4. **Solomon benchmarking tries to solve comparability with proprietary normalizers (EII, OA, CWB/CWT) — but these are themselves contested and incomplete.** EII=100 is "average" energy efficiency [^24^]; Operational Availability vs Mechanical Availability are distinct Solomon metrics, with world-class OA >97% [^25^]. Solomon's own "World's Best Refineries" uses a *balanced-scorecard* of four metrics (OA, EII, MEI, ROI) precisely *"to avoid too much focus on operating costs"* and adjusts for *"regional economic environments to avoid penalizing a refinery for its location"* — an admission that raw single-metric comparison misleads [^23^]. For GHG, Solomon built *complexity-weighted barrels/tonnes (CWB/CWT)* because *"not all refineries are created equal,"* yet *"EII alone cannot address the full range of issues since it focuses only on the combustion side."* [^18^]

5. **OTIF is a case study in definition fragmentation producing real money consequences.** There is *"no all-encompassing standard definition"*; on-time can mean retailer-requested vs manufacturer-promised date, delivery slot vs broad window; in-full can be order/line/case level [^16^]. Retailer windows differ (Walmart 30-min, Target 1-hr from appointment, Home Depot by date, Kroger 2-hr from unloading) — one supplier *"achieved 97% OTIF by internal metrics but only 82% according to their largest customer, resulting in $800,000 in unexpected penalties."* [^17^]

6. **Emissions-intensity baselines are non-comparable across studies and assets because of scope, allocation and boundary choices.** The EU Fuel Quality Directive impact analysis found the literature *"may rely on different assumptions and/or have differing scopes,"* and that *"different allocation approaches can result in as much as 10 g/MJ of difference"* — large enough to swamp the policy target [^19^]. Cross-facility LNG/refining GHG benchmarking is hampered because data are *"often not transparent... this introduces uncertainty to the comparisons,"* and co-production *"has the potential to introduce differences in the basis of comparison."* [^19b^]

7. **The Balanced Scorecard — the default framework deployed in oil & gas — is itself criticized for metric overload and weak links from local KPIs to enterprise results.** In UK offshore O&G, the BSC is described as a *"rational functionalist approach... scientific reductionism,"* with critics warning of *"the tyranny of the Balanced Scorecard"* and that *"if factors used in the BSC were invalid then the organization may focus on the wrong strategic aspects."* [^20^] Academic analysis contrasts BSC (top-down, proliferating KPIs, *"difficulty in correlating individual KPIs with the organizational result"*) with Theory of Constraints (a few bottom-up KPIs tied to the goal), citing Goldratt: *"the optimization of local KPIs does not automatically improve the system's performance."* [^29^]

8. **Goldratt's TOC is the canonical theoretical frame for why local optimization destroys system performance — and most KPI systems reward exactly the wrong thing.** *"Improving utilisation on a non-bottleneck machine is, strictly speaking, a loss. Yet this is exactly what most KPI systems reward, because they measure each machine in isolation."* [^28^] *"A system of local optimums is not an optimum system at all."* [^30^] Goldratt's aphorism — *"Tell me how you measure me, and I will tell you how I will behave"* — is the analytic hinge of the whole dimension [^31^].

9. **Misaligned KPIs produce conflicting interpretations of "good performance" and actively stall improvement via a self-reinforcing vicious cycle.** *"Local optimization creates competing priorities and therefore guarantees the whole system's failure... employees focus on their KPIs, even when this comes at the expense of other departments... everyone is defending their KPIs while the total system output decreases."* [^32^] When the same metric is computed in SQL, BI tools, spreadsheets and ETL simultaneously, *"the number of places a definition can drift grows faster than anyone's ability to police them"* — so meetings *"turn into debates about whose number is right instead of what action to take."* [^4^][^45^]

10. **Incentive design tied to local metrics is the transmission mechanism — Goodhart's Law in action — and it reaches the C-suite.** *"When a measure becomes a target, it ceases to be a good measure... when we use a measure to reward performance, we provide an incentive to manipulate the measure."* [^34^] Wells Fargo's *"products per household"* bonus metric drove ~2 million phony accounts, *"$185 million in fines... and a $3 billion federal settlement."* [^37^] Even in oil & gas, executive bonuses are explicitly benchmarked to *"first-quartile cost and schedule performance based on Solomon Associates benchmarking,"* hard-wiring a single external metric into pay [^39^]. The documented remedy in downstream is to redesign *"incentive systems"* as one of the core levers of margin integration — worth **US$0.2–0.6/bbl** between mid- and top-quartile players [^6^].

---

---

# SECTION 1 — FUNCTIONAL KPI CONFLICTS IN A REFINER/MARKETER
*(Trading vs Operations vs Logistics vs Marketing; margin vs throughput vs service level vs inventory vs emissions vs customer metrics)*

### Claim 1.1 — Refinery throughput/cost goals structurally conflict with depot service and logistics cost goals; each function optimizes a different KPI and destroys enterprise value.
- **Source:** Opsio Cloud — "Inventory Management for Oil and Gas"
- **URL:** https://opsiocloud.com/blogs/mastering-inventory-management-for-oil-and-gas-businesses/
- **Date:** 2025-05-14
- **Excerpt (verbatim):** "Different entities within a company often operate as isolated islands. A refinery focuses on maximizing throughput and reducing unit costs. A distribution depot aims for high fill rates to ensure local service. These conflicting key performance indicators (KPIs) drive sub-optimal decisions. What benefits one location can harm the overall enterprise value. This lack of coordination is a foundational flaw in many operations."
- **Context:** Direct statement of the classic silo-optimization problem the mission asks about (maximize refinery utilization vs minimize supply-chain cost). The "push-pull boundary" passage reinforces it: refinery economics "demand near-continuous production" (push) that "directly conflicts with the variable 'pull' of downstream market demand," forcing tank-top and demurrage costs.
- **Confidence:** High.

### Claim 1.2 — The proposed remedy is shared KPIs aimed at total enterprise value (total delivered cost vs service level), not local metrics.
- **Source:** Opsio Cloud — "Inventory Management for Oil and Gas"
- **URL:** https://opsiocloud.com/blogs/mastering-inventory-management-for-oil-and-gas-businesses/
- **Date:** 2025-05-14
- **Excerpt (verbatim):** "Siloed operations fail because incentives are misaligned. We must break down these barriers with a consistent framework of end-to-end processes. The key is implementing shared Key Performance Indicators (KPIs) across refineries, depots, and logistics teams. These KPIs must focus on total enterprise value, not local optimization. For example, a metric balancing total delivered cost against service levels fosters collaboration. It encourages a depot to work with logistics on smarter routing, not just maximize its own fill rate."
- **Context:** Names the two colliding KPI families explicitly — total delivered **cost** (logistics) vs **service level**/fill rate (depot/commercial) — and ties misalignment to *incentives*, linking Section 1 to Section 4.
- **Confidence:** High.

### Claim 1.3 — Margin integration across trading/chemicals/refining is a named source of value, and "incentive systems" are a core lever to capture it (BCG).
- **Source:** BCG (via Cuadernos Orkestra / emcombustion) — "The Oil and Gas value chain: a focus on oil refining"
- **URL:** https://emcombustion.es/wp-content/uploads/2018/12/orkestra_the-oil-gas-value-chain-refining-emcombustion1.pdf
- **Date:** undated (~2018; "Source: BCG experience")
- **Excerpt (verbatim):** "Increase in the level of integration/coordination across the value chain to optimize the integrated margin... In margin integration, the difference between mid- and top- players can vary approximately from US$0.2 to US$0.6/bbl... Companies can use a number of levers... focused on 1) Processes and coordinating mechanisms such as i) Processes/mechanisms to identify integration opportunities; ii) Transfer pricing/long-term contracts; iii) Joint linear programming; iv) **Incentive systems**; and v) Operating processes."
- **Context:** Quantifies the prize from cross-functional alignment (up to ~$0.6/bbl between mid and top performers) and explicitly lists *incentive systems* and *transfer pricing* as levers — confirming that KPI/incentive misalignment is the barrier between functions (trading, refining, chemicals).
- **Confidence:** High.

### Claim 1.4 — Value Chain Optimization is framed as the antidote to inward, product/own-organization KPI orientation.
- **Source:** KBC — "Value Chain Optimization Manifesto"
- **URL:** https://www.kbc.global/uploads/files/whitepapers/0095-VCOmani-MANI-US-092020.pdf
- **Date:** 2020-09 (file ref 092020)
- **Excerpt (verbatim):** "The implication of 'alignment' is a mindset shift from inward orientation focused on 'product' and own organizational needs, to outward orientation focused on market needs and customer experience. Only then can effective commercial optimization of the business occur."
- **Context:** The VCO thesis of the parent study: inward-looking functional KPIs ("product"/own-org) are the obstacle; outward, market/customer-facing metrics enable true optimization. Supports the trading/ops/marketing reframing.
- **Confidence:** Medium-High.

### Claim 1.5 — Multi-functional KPI systems create competing narratives and overload executives, obscuring trade-offs (academic).
- **Source:** Journal of Tianjin University (Tianjin Daxue Xuebao) — KPI systems in multi-functional organizations
- **URL:** https://tianjindaxuexuebao.com/dashboard/uploads/23.18885385.pdf
- **Date:** undated
- **Excerpt (verbatim):** "A primary challenge in multi-functional settings is KPI misalignment. Functional KPIs may optimize local efficiency while undermining enterprise-wide outcomes. For example, cost-focused operational indicators can conflict with sales-driven growth metrics, or financial efficiency measures may discourage investments necessary for long-term capability development. Without an integrated framework, executives face trade-offs that are obscured by siloed measurement systems rather than clarified by them."
- **Context:** Academic corroboration that (a) local KPIs undermine enterprise outcomes, and (b) misalignment *obscures* trade-offs at the executive level — the "conflicting interpretations of good performance" mechanism.
- **Confidence:** High.

### Claim 1.6 — In multi-functional organizations the *same* concepts (profitability, efficiency, customer) are reported with different methodologies and cycles, eroding trust.
- **Source:** Journal of Tianjin University (Tianjin Daxue Xuebao)
- **URL:** https://tianjindaxuexuebao.com/dashboard/uploads/23.18885385.pdf
- **Date:** undated
- **Excerpt (verbatim):** "Another issue in multi-functional organizations is inconsistency in measurement definitions and time horizons. Different functions may report similar concepts — such as profitability, efficiency, or customer performance — using distinct methodologies and reporting cycles. These inconsistencies complicate executive interpretation and can erode confidence in performance information. Standardized definitions and aligned reporting rhythms are therefore essential for effective KPI integration."
- **Context:** Bridges Section 1 (functional conflict) and Section 2 (definition inconsistency): the conflict is as much about *definitions and cadence* as about goals.
- **Confidence:** High.

### Claim 1.7 — Retail: the volume-vs-margin tension is real and quantified; low-volume sites must price higher to earn the same return, and price wars compress actual margins below nominal.
- **Source A:** Australian Institute of Petroleum (AIP) — "Facts About the Australian Retail Fuels Market and Prices" (citing ACCC)
- **URL:** https://aip.com.au/sites/default/files/download-files/2017-11/Facts%20About%20the%20Australian%20Retail%20Fuels%20Market%20and%20Prices.pdf
- **Date:** 2017-11
- **Excerpt (verbatim):** "The ACCC has found that if a typical country service station is selling around half the volume of a typical city service station then it needs to sell petrol at around 4 cents per litre more to earn the same return on sales."
- **Source B:** NBER — "General Characteristics of the Petroleum Industry and Its Price Problems"
- **URL:** https://www.nber.org/system/files/chapters/c5803/c5803.pdf
- **Date:** undated (historical)
- **Excerpt (verbatim):** "The nominal gross margins of retailers... have increased, but the intensifying of competition, characterized at times by price wars, has kept actual margins at a level substantially below nominal margins."
- **Context:** Quantifies the retail volume↔margin trade-off (throughput vs unit margin): a station chasing volume accepts thin cents/litre margins, while a low-volume site needs ~4 c/L more to match returns. Confirms "retail volume vs margin" as a live, measurable silo tension.
- **Confidence:** Medium-High.

---

# SECTION 2 — METRIC DEFINITION INCONSISTENCY
*(Refining-margin definitions; availability/utilization (Solomon vs internal); OTIF variants; emissions-intensity baselines; margin-per-barrel across regions; blockage of cross-asset & longitudinal comparison)*

## 2A — Refining "margin" has multiple competing definitions (gross / net / variable / cash; replacement vs accounting cost)

### Claim 2.1 — Gross vs Net refining margin are distinct; GRM excludes operating expense, NRM subtracts opex/depreciation/other.
- **Source:** University lecture (UoMus, Iraq) — "Refining Margins: Definition and Importance"
- **URL:** https://uomus.edu.iq/img/lectures21/MUCLecture_2025_22841197.pdf
- **Date:** 2025 (file ref)
- **Excerpt (verbatim):** "1. Gross Refining Margin (GRM): GRM = (Total Revenue from Products − Cost of Crude Oil) / Barrels of Crude Processed. It considers only crude oil costs and product revenue but excludes operating expenses. 2. Net Refining Margin (NRM): NRM = GRM − Operating Costs − Depreciation − Other Expenses. This is a more accurate measure of refinery profitability since it accounts for all expenses."
- **Context:** The same word "margin" spans a simple crack-spread proxy (GRM) and a full P&L measure (NRM). Comparing a GRM from one refinery to an NRM from another (or the same refinery across time as cost allocation changes) is meaningless without the definition.
- **Confidence:** High.

### Claim 2.2 — Even the *sign and composition* of a "crack spread" vary by author/region, and it is explicitly not the same as the operating margin.
- **Source A:** GlobalOilShock — "Refining Margin Explained"
- **URL:** https://globaloilshock.com/en/glossary/refining-margin/
- **Date:** undated
- **Excerpt (verbatim):** "Crack spread is the raw equation: (product prices) − (crude price). Refining margin is profit after opex (energy, chemicals, labor). The 3-2-1 spread runs 1–2 USD/bbl higher than actual operating margin because conversion losses and overhead subtract."
- **Source B:** "Commodity Option Pricing: A Practitioner's Guide" (textbook)
- **URL:** http://students.aiu.edu/submissions/profiles/resources/onlineBook/s5W5t9_commodity%20option%20pricing%20finance.pdf
- **Date:** undated
- **Excerpt (verbatim):** "One should be careful, however, as crack spreads are sometimes quoted as the difference between the price of the crude oil minus the price of the refined product... and sometimes... the refined product minus the price of the crude oil... Generally the applicable sign convention can be inferred from context."
- **Context:** Two definitional hazards in one: (a) crack spread ≠ realized margin (a 1–2 $/bbl systematic gap); (b) the sign convention itself is inconsistent across sources. **TENSION:** a "margin" number is unusable unless the exact convention (products included, sign, opex treatment) is pinned down.
- **Confidence:** High.

### Claim 2.3 — BP's glossary shows a single major internally distinguishing replacement-cost profit, Solomon operational availability, refinery utilization, and net cash margin — four different constructs often conflated.
- **Source:** BP Annual Report and Form 20-F 2018 — Glossary
- **URL:** https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/pdfs/investors/bp-annual-report-and-form-20f-2018-glossary.pdf
- **Date:** 2018
- **Excerpt (verbatim):** "Refining availability — Represents Solomon Associates' operational availability, which is defined as the percentage of the year that a unit is available for processing after subtracting the annualized time lost due to turnaround activity and all planned mechanical, process and regulatory downtime. ... Refinery utilization — calculated as annual throughput (thousands of barrels per day) divided by crude distillation capacity. ... Refining net cash margin per barrel — defined by Solomon Associates as the net margin achieved after subtracting cash operating expenses and adding any refinery revenue from other sources... expressed in US dollars per barrel of net refinery input. ... Replacement cost (RC) profit or loss — Reflects the replacement cost of inventories sold in the period and is arrived at by excluding inventory holding gains and losses from profit or loss."
- **Context:** This is the single most load-bearing primary source for the dimension. It proves that within one supermajor, "availability" (Solomon OA), "utilization" (throughput/capacity), "net cash margin," and "replacement-cost profit" are *distinct, separately-defined* metrics. **TENSION:** "replacement vs accounting cost" — RC profit explicitly strips inventory holding gains/losses, whereas IFRS/accounting profit includes them, so the same period shows different "performance."
- **Confidence:** High.

### Claim 2.4 — "Replacement cost" exists precisely because accounting (IFRS) profit is distorted by price-driven inventory gains/losses — a longitudinal-comparison problem.
- **Source:** BP Annual Report and Form 20-F 2018 — Glossary
- **URL:** https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/pdfs/investors/bp-annual-report-and-form-20f-2018-glossary.pdf
- **Date:** 2018
- **Excerpt (verbatim):** "Inventory holding gains and losses vary from period to period due to changes in prices as well as changes in underlying inventory levels. In order for investors to understand the operating performance of the group excluding the impact of price changes on the replacement of inventories, and to make comparisons of operating performance between reporting periods, BP's management believes it is helpful to disclose this measure."
- **Context:** Explicit admission that *accounting-cost* profit is not comparable period-over-period without the *replacement-cost* adjustment — a direct statement of the longitudinal-comparison blocker.
- **Confidence:** High.

## 2B — Availability / utilization: Solomon definitions vs internal variants

### Claim 2.5 — Solomon distinguishes Mechanical Availability from Operational Availability; world-class OA is >97%, and long turnaround intervals are traded against it.
- **Source:** Solomon Insight — "Turnaround Maintenance Insights"
- **URL:** https://www.solomoninsight.com/blog/turnaround-maintenance-insights
- **Date:** undated
- **Excerpt (verbatim):** "Mechanical Availability (MA) and OA are Solomon's primary metrics for measuring a refiners' availability performance. The world's best refineries consistently deliver greater than 97% OA... Targeting turnaround intervals between 4-6 years can deliver annual days down performance that enables achieving 97%+ Operational Availability."
- **Context:** Establishes that even the benchmarking authority maintains *two* availability metrics (MA vs OA). An internal "uptime" or "stream-day utilization" metric will not reconcile to either, so a refinery can be "best in class" internally and mid-pack on Solomon OA.
- **Confidence:** High.

### Claim 2.6 — "Utilization" can exceed 100% of nameplate (throughput > crude distillation capacity), a definitional artifact that confuses comparison.
- **Source:** Unlisted Zone — "Nayara Energies FY24 Results"
- **URL:** https://unlistedzone.com/nayara-energies-fy24-results-and-new-product-launch-report
- **Date:** undated (FY2023-24)
- **Excerpt (verbatim):** "achieving an impressive capacity utilization of 101.6%. Additionally, the overall operational availability of the refinery's key process units was 99.74%... In a global benchmarking study conducted by Solomon Associates for CY 2022, the refinery was recognized as one of the top performers."
- **Context:** A >100% "capacity utilization" (101.6%) coexists with a 99.74% "operational availability" — two different numbers for the same asset in the same paragraph. **TENSION:** which is "the" performance? Depends on denominator (nameplate vs demonstrated capacity) and on Solomon vs internal definition.
- **Confidence:** Medium-High.

### Claim 2.7 — YPF likewise reports a refinery "utilization rate of 104%," confirming the denominator ambiguity is industry-wide.
- **Source:** EarningsCall.biz — "YPF Q4 2025"
- **URL:** https://earningscall.biz/e/nyse/s/ypf/y/2025/q/q4
- **Date:** 2025 (Q4 2025 call)
- **Excerpt (verbatim):** "Last month, we beat our own record again, reaching 352,000 barrels per day, representing a utilization rate of 104%."
- **Context:** Independently confirms that "utilization >100%" is common because the denominator (design vs demonstrated vs economic capacity) is not standardized — a cross-asset comparison hazard.
- **Confidence:** Medium.

## 2C — OTIF / service-level variants

### Claim 2.8 — OTIF has no standard definition; "on-time" and "in-full" are each measured multiple ways (McKinsey-cited).
- **Source:** Tive — "What is OTIF..."
- **URL:** https://www.tive.com/blog/on-time-in-full-otif-what-is-otif-and-how-to-improve-metrics-with-technology
- **Date:** 2025-07-08
- **Excerpt (verbatim):** "However, there is no all-encompassing standard definition. Retailers and manufacturers often calculate OTIF in different ways... 'Because each retailer has a different definition, manufacturers must meet a variety of different delivery standards... Does "on-time" mean on the date requested by the retailer, or the date promised by the manufacturer? Does it mean within the specific delivery slot allocated to the shipment, or any time inside a broader, agreed-upon time window? Should "in-full" be measured at the level of complete orders, line-items or individual cases?' [attributed to McKinsey]"
- **Context:** OTIF is the supply-chain analogue of "refining margin": a ubiquitous KPI whose components are defined at least 2×2×3 = 12 ways. Directly evidences definition inconsistency blocking comparison.
- **Confidence:** High.

### Claim 2.9 — Definition fragmentation produces direct financial penalties; internal vs customer OTIF can diverge by 15 points.
- **Source:** GPX — "Maximizing On-Time In-Full (OTIF) In Supply Chain"
- **URL:** https://gpx.co/blog/on-time-in-full-otif-in-supply-chain/
- **Date:** 2026-01-30
- **Excerpt (verbatim):** "every retailer defines 'on-time' differently: Walmart: Requires delivery within a 30-minute window. Target: Uses a one-hour window based on appointment time... Home Depot: Considers an order on-time if delivered on the correct date. Kroger: Uses a two-hour window starting from when unloading begins... One electronics manufacturer discovered they achieved 97% OTIF by internal metrics but only 82% according to their largest customer, resulting in $800,000 in unexpected penalties."
- **Context:** A quantified, concrete case of the same metric yielding 97% vs 82% — the "conflicting interpretations of good performance" with a dollar consequence. **TENSION:** the firm thought it was performing; the customer's definition said otherwise.
- **Confidence:** High.

### Claim 2.10 — Academic literature likewise notes OTIF requirements and "in-full" thresholds differ across organizations (98% vs 100% fill).
- **Source:** Tilburg University repository (arno.uvt.nl) — thesis on OTIF / delivery reliability
- **URL:** http://arno.uvt.nl/show.cgi?fid=190924
- **Date:** undated
- **Excerpt (verbatim):** "OTIF requirements differ across organizations and industries, reflecting various tolerances for late deliveries... Most companies aim for an OTIF rate exceeding 97% at the SKU level... though definitions of 'in full' may vary, with some requiring a fill rate of only 98% while others insist on 100%."
- **Context:** Confirms in the academic supply-chain literature that even the *target threshold* for the same KPI is not standardized.
- **Confidence:** Medium-High.

## 2D — Emissions-intensity baselines are not comparable

### Claim 2.11 — Refinery GHG intensity cannot be judged on throughput alone; Solomon built CWB/CWT to normalize for complexity, and EII still misses non-combustion emissions.
- **Source:** Hydrocarbon Engineering — "Benchmarking methodologies"
- **URL:** https://www.hydrocarbonengineering.com/special-reports/05022015/Benchmarking-methodologies-193/
- **Date:** 2015-02-05
- **Excerpt (verbatim):** "It is therefore not sufficient to judge refinery emission performance on the basis of throughput alone. Although simple refineries might have the lowest emissions per barrel of oil processed, they might consume more energy considering complexity. A normalisation method that takes complexity into account is crucial... Solomon developed such customised metrics as complexity weighted barrels (CWB™) and complexity weighted tonnes (CWT™)... Although EII is a good proxy for benchmarking GHG emissions, a refinery's emission performance also depends on the type of fuel it burns... and the amount of byproduct CO2 it produces... neither of which is addressed in the EII... Sometimes EII alone cannot address the full range of issues since it focuses only on the combustion side of the equation."
- **Context:** Shows the *baseline* for emissions intensity is a deliberate modeling choice (throughput vs complexity-weighted), and that the industry's gold-standard EII is acknowledged to be an incomplete proxy. A refinery can look good on CO2/bbl and bad on CO2/CWT simultaneously.
- **Confidence:** High.

### Claim 2.12 — Lifecycle GHG-intensity estimates diverge by scope, coverage and allocation; allocation alone can swing results by ~10 gCO2e/MJ.
- **Source:** European Commission (circabc) — "Impact Analysis of Options for Implementing Article 7a of Directive 98/70/EC (Fuel Quality Directive)"
- **URL:** https://circabc.europa.eu/sd/a/8aaca016-9c12-4b85-8e3e-5561ff752bfd/MASTER_FQD%20IA%20Final%20Report%202%20Aug%20(2).pdf
- **Date:** undated
- **Excerpt (verbatim):** "The different literature may rely on different assumptions and/or have differing scopes... Allocation: How one study allocates total refinery emissions... may differ from the approach of another study, and lead to variation in total lifecycle emissions. Jacobs (2012) for example indicates that different allocation approaches can result in as much as 10 g/MJ of difference."
- **Context:** A 10 g/MJ spread purely from allocation choice — against a policy target of a 6% reduction from an 88.3 gCO2e/MJ baseline — shows emissions-intensity "performance" is an artifact of methodology, blocking cross-study and cross-asset comparison.
- **Confidence:** High.

### Claim 2.13 — Even within one company, GHG-intensity denominators differ by segment (per boe upstream, per utilized-equivalent-distillation-capacity refining, per tonne petchem), and co-production muddies facility comparison.
- **Source A:** ERIA — "Chapter 4: Efforts in the Majors" (citing BP 2022)
- **URL:** https://www.eria.org/uploads/media/Research-Project-Report/RPR-2022-15/12_Chapter-4-Efforts-in-the-Majors-Non-ASEAN-NOCs.pdf
- **Date:** undated (citing BP 2022)
- **Excerpt (verbatim):** "Scope 1 and Scope 2 GHG emissions in tCO2e from bp operated refineries per utilized equivalent distillation capacity... [upstream] per thousand boe... [petrochemical] per thousand tonnes of petrochemicals produced."
- **Source B:** Woodside — "North West Shelf Project Extension Environmental Review Document"
- **URL:** https://www.woodside.com/docs/default-source/current-consultation-activities/australian-activties/nws-project-extension-combined.pdf
- **Date:** undated
- **Excerpt (verbatim):** "The emission source information and data for LNG facilities is often not transparent... and this introduces uncertainty to the comparisons... data provided also include emissions associated with other co-produced products such as LPG and condensates. This has the potential to introduce differences in the basis of comparison... the intent of defining the emissions boundary is to achieve a 'like for like' comparison... this is not always possible."
- **Context:** Demonstrates that emissions-intensity baselines differ *by segment* and are undermined by co-production/boundary choices — so "emissions intensity" is not a single portable metric across a downstream portfolio.
- **Confidence:** Medium-High.

## 2E — Margin-per-barrel is not comparable across regions

### Claim 2.14 — IEA/KBC indicator margins use different crude benchmarks, configurations and operating philosophies per region, and the yields are explicitly "not typical of modern refineries."
- **Source:** IEA / KBC — "Refinery Margins: Methodology Notes"
- **URL:** https://iea.blob.core.windows.net/assets/cbf37dfc-5fe1-4854-b248-95e6a2e5240a/Refining_Margin_Supplement_OMRAUG_12SEP2012.pdf
- **Date:** 2012-09-12
- **Excerpt (verbatim):** "Regional differences: Operating philosophy and or operating variables are different depending on the geographical region... Middle distillate make is maximised in the European and Singapore cases while the American refineries have historically maximised gasoline... We wish to note that the yields assumed in these indicator cases are not typical of modern refineries... reported margins should be taken as an indication, or proxy, of changes in profitability for a given refining centre. No attempt is made to model... the relative economics of specific refineries."
- **Context:** The authoritative margin series itself warns that (a) regional margins embed different operating philosophies (gasoline-max US vs distillate-max Europe/Singapore) and (b) they are *proxies*, not refinery-specific economics. Cross-region "margin per barrel" comparison is therefore an approximation with known bias.
- **Confidence:** High.

### Claim 2.15 — Regional crack-spread conventions differ (US Gulf Coast coking 3:2:1, NW Europe cat-cracking 5:3:2, Singapore 2:1:1), so the headline "margin" is built on different product baskets.
- **Source:** Baidu Baike (EN) — "Integrated Refining Margin"
- **URL:** https://baike.baidu.com/en/item/Integrated%20Refining%20Margin/1673976
- **Date:** 2026-06-02
- **Excerpt (verbatim):** "The feedstock for the U.S. Gulf Coast region is set as WTI Crude Oil, employing the Coking Process and the '3:2:1' Rule. The feedstock for the Northwest Europe region is set as Brent Crude Oil, employing the Catalytic Cracking Process and the '5:3:2' Rule. The feedstock for the Singapore region is set as OPEC Crude Oil, employing the Catalytic Cracking Process and the '2:1:1' Rule."
- **Context:** Direct evidence that the canonical regional "margins" are computed on *different crude benchmarks, different process models, and different X:Y:Z product ratios*. Corroborated academically: *"Widely used crack spreads include 3:2:1, 5:3:2 and 2:1:1."* [^50^] **TENSION:** a "$/bbl margin" figure is not a like-for-like number across regions.
- **Confidence:** High.

### Claim 2.16 — Commercial margin providers model different regional crude slates and different gasoline/diesel configuration weightings, reinforcing non-comparability.
- **Source:** Energy Aspects — "Refining Margins" (service overview)
- **URL:** https://web-cdn.energyaspects.com/service_overviews/2020/energy_aspects_refining_margins_service_overview_2020_5e1473be343fd.pdf
- **Date:** 2020
- **Excerpt (verbatim):** "The cost of crudes is given by the regional benchmark (WTI for US, Dated Brent for Europe and Dubai for Singapore)... The breakdown sections... weighted averages of the two different configurations (gasoline-oriented and diesel-oriented) in each region according to the following ratios: Singapore 41%/59%; NWE 56%/44%; US Gulf Coast 71%/29%; US East Coast 87%/13%..."
- **Context:** A second, independent commercial methodology confirming the same point: regional margins blend different slates and different gasoline/diesel weightings, so a single global "$/bbl margin" conceals structural regional differences.
- **Confidence:** Medium-High.

## 2F — The net effect: cross-asset and longitudinal comparison is blocked

### Claim 2.17 — The same KPI defined in four places (SQL, BI tool, spreadsheet, ETL) drifts faster than anyone can police, destroying a single version of truth.
- **Source:** BluePes — "KPI misalignment: why teams report different numbers"
- **URL:** https://bluepes.com/blog/multiple-versions-of-truth-kpi-misalignment
- **Date:** 2026-02-23
- **Excerpt (verbatim):** "The divergence appears after the data lands, in the layer where business logic gets applied — and that logic tends to live in several places at once: SQL written for a specific report... transformation logic inside the BI tool or semantic model... spreadsheet calculations maintained outside any system of record... rules embedded in integration or ETL flows upstream... When the same metric is defined in four places, consistency depends on people remembering to keep four definitions identical... the number of places a definition can drift grows faster than anyone's ability to police them."
- **Context:** The mechanism behind "multiple versions of the truth": definition drift across tools and teams. This is the practical blocker to both cross-asset comparison (different sites compute differently) and longitudinal comparison (definitions change over time).
- **Confidence:** High.

---

# SECTION 3 — KPI FRAMEWORKS AND THEIR LIMITS
*(Balanced Scorecard in oil & gas; Solomon benchmarking metrics; APQC process classification; local vs system optimization / Goldratt TOC)*

## 3A — Balanced Scorecard in oil & gas: adopted widely, but criticized

### Claim 3.1 — The BSC became the default in oil & gas, but academic critics call it a reductionist "tyranny" that can focus the organization on the wrong things.
- **Source:** Spence (2020), Robert Gordon University — PhD thesis, "The influence of organisational typology... on UK offshore oil and gas industry safety performance"
- **URL:** https://rgu-repository.worktribe.com/preview/1358167/SPENCE%202020%20The%20influence%20of%20organisational%20typology.pdf
- **Date:** 2020
- **Excerpt (verbatim):** "By employing a BSC-based approach many Oil & Gas Operating companies adopted a rational functionalist approach that focuses on scientific reductionism resulting from dividing the organizational mission and strategy into constituent variables. However, research has concluded that such rational paradigms may fail when confronted with unpredictable and unstable environmental conditions... Flamholtz (2003) concluded that if factors used in the BSC were invalid then the organization may focus on the wrong strategic aspects with potentially damaging consequences. Voelpel et al. (2006:43) refer to 'The tyranny of the Balanced Scorecard in the innovation economy', concluding that the BSC has become obsolete..."
- **Context:** Locates the BSC critique *specifically in oil & gas*. The core limit: decomposing strategy into functional metrics assumes stability and can institutionalize the wrong measures.
- **Confidence:** High.

### Claim 3.2 — Practitioner literature lists BSC failure modes that map directly to KPI misalignment: wrong metrics, KPI overload, weak strategy links, poor data.
- **Source:** MadeToMeasureKPIs — "6 Disadvantages of a Balanced Scorecard"
- **URL:** https://madetomeasurekpis.com/blog/2024/11/18/6-disadvantages-of-balanced-scorecard/
- **Date:** 2025-03-11 (post 2024-11-18)
- **Excerpt (verbatim):** "1. Picking the Wrong Metrics — If you get the performance indicators wrong, the balanced scorecard can completely misrepresent how your organisation is performing... 2. Overloading on KPIs — Choosing too many KPIs can quickly overwhelm your team. When everything is measured, nothing stands out as a priority. This can cause gridlock... 5. Weak Links to Strategic Goals — when the metrics don't clearly tie back to strategic objectives."
- **Context:** "KPI overload → gridlock" and "weak links to strategic goals" are exactly the mechanisms by which a framework meant to create alignment produces conflicting interpretations of performance.
- **Confidence:** Medium-High.

### Claim 3.3 — Poorly/inconsistently defined metrics make a scorecard "vulnerable to criticism by people who want to avoid accountability."
- **Source:** BPM Institute — "Problems Implementing a Balanced Scorecard"
- **URL:** https://www.bpminstitute.org/resources/articles/problems-implementing-balanced-scorecard/
- **Date:** 2022-12-09
- **Excerpt (verbatim):** "Metrics need to be... defined in such a way that the measurement can be consistently applied across the firm, even if their targets of performance differ... A system that has sloppy or inconsistently defined metrics will be vulnerable to criticism by people who want to avoid accountability for results."
- **Context:** Connects framework failure directly to definition inconsistency (Section 2) and to the incentive/accountability behavior (Section 4): inconsistent definitions become an excuse to dispute results.
- **Confidence:** High.

## 3B — Solomon benchmarking metrics: the industry standard, with acknowledged limits

### Claim 3.4 — Solomon's own "World's Best Refineries" deliberately uses a balanced-scorecard of four metrics and adjusts for region — an admission that single-metric comparison misleads.
- **Source:** Solomon Insight — "World's Best Refineries Analysis Report"
- **URL:** https://www.solomoninsight.com/industries/refining/worlds-best-refineries
- **Date:** undated (2016/2018/2020 study cycles)
- **Excerpt (verbatim):** "Solomon evaluated key refinery financial metrics together with key operating metrics using a balanced scorecard approach to avoid too much focus on operating costs. We also considered regional economic environments to avoid penalizing a refinery for its location... a refinery had to attain first- or second-quartile performance in four Solomon metrics over three consecutive Fuels Study cycles: Operational Availability (OA), Energy Intensity Index (EII), Maintenance Cost Efficiency Index (MEI), and Return on Investment (ROI)."
- **Context:** Even the benchmarking authority refuses to crown a refinery on one metric — it needs four, sustained over six years, *and* a regional adjustment. This is the strongest evidence that any single KPI (cost, availability, energy, ROI) gives a conflicting/incomplete read of "good performance."
- **Confidence:** High.

### Claim 3.5 — EII is a relative, normalized index (100 = average), resource-intensive to compute, and hard to integrate with legacy systems.
- **Source:** boTec — "Solomon Energy Intensity Index (EII)"
- **URL:** https://botec.com/glossary/solomon-energy-intensity-index-eii/
- **Date:** 2025-10-28
- **Excerpt (verbatim):** "An EII score of 100 represents average energy efficiency, with scores below 100 indicating better-than-average performance... Key Challenges: Complex Metrics — Involves comprehensive calculations that demand precise data inputs. Resource Intensity — Requires dedicated resources for energy audits and consistent monitoring. Adapting Systems — Integration with legacy systems may pose challenges."
- **Context:** EII is the industry's energy benchmark, but it is (a) relative to a peer average (so "good" moves as the peer set changes), and (b) data-/resource-heavy — a barrier to consistent internal replication and longitudinal tracking.
- **Confidence:** High.

### Claim 3.6 — Solomon EII has been embedded in regulation (Washington State RACT; EU ETS benchmark via CONCAWE), so its definitional choices have compliance consequences.
- **Source A:** Solomon Insight — "Washington State Refineries to Use Solomon Benchmarking Methodology..."
- **URL:** https://www.solomoninsight.com/news/washington-state-refineries-to-use-solomon-benchmarking-methodology-to-help-control-greenhouse-gas-emissions
- **Date:** 2014-06-10
- **Excerpt (verbatim):** "a refinery will be considered compliant if it has a calculated EII equal to or more efficient than the EII value representing the 50 percentile EII of similar-sized United States refineries, based on 2006 performance data and the EPA EnergyStar Program's methodology."
- **Source B:** ResearchGate / CONCAWE report 9/12 — "Developing a methodology for an EU refining industry CO2 emissions benchmark"
- **URL:** https://www.researchgate.net/publication/292572306_Developing_a_methodology_for_an_EU_refining_industry_CO2_emissions_benchmark
- **Date:** 2012 (report 9/12)
- **Excerpt (verbatim):** "those economic sectors exposed to international competition, including oil refining, will still be granted a proportion of the required allowances free of charge according to a sectoral benchmark developed on the basis of the performance of the '10% most efficient installations'... CONCAWE, on behalf of the EU refining industry, cooperated with Solomon Associates... to [develop the CWT benchmark]."
- **Context:** When a benchmark becomes a regulatory threshold (50th-percentile EII; top-10% CWT for free allowances), the *definition* of the metric determines compliance and money — raising the stakes of every definitional choice and incentivizing lobbying over definitions.
- **Confidence:** High.

## 3C — APQC process classification: common language as the precondition for benchmarking

### Claim 3.7 — APQC's premise is that "effective benchmarking requires common definitions" — i.e., without a shared process/metric language, comparison is invalid.
- **Source:** APQC — "Process Classification Framework (PCF) — Petroleum Upstream (PDF)"
- **URL:** https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-petroleum-upstream-pdf
- **Date:** 2026-05-06 (page)
- **Excerpt (verbatim):** "Effective benchmarking requires common definitions and processes. Like a shared language, organizations need to make apples-to-apples comparisons to obtain accurate benchmarks and metrics. The original Process Classification Framework (PCF) provides a common language and open standard that allows organizations to see and discuss their activities from an industry-neutral viewpoint."
- **Context:** APQC's entire framework exists because metric/process definition inconsistency is the default state; the PCF is the antidote. Direct support for the dimension's premise.
- **Confidence:** High.

### Claim 3.8 — The Downstream Petroleum PCF explicitly spans refining, marketing, trading, logistics and hedging — the very functions whose KPIs conflict — under one taxonomy.
- **Source:** APQC — "PCF — Downstream Petroleum (v7.2.2)"
- **URL:** https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-downstream-petroleum-2
- **Date:** 2026-05-06
- **Excerpt (verbatim):** "The Downstream PCF addresses manufacturing, marketing, and trading of liquids and gases... This includes nomination, logistics, trading, hedging, and storage from the point of custody transfer to the downstream delivery location (e.g. refinery, gas plant, commercial or retail location...)."
- **Context:** Confirms the downstream PCF is the taxonomy meant to reconcile the exact set of functions (manufacturing/marketing/trading/logistics) whose KPIs this dimension shows are in conflict. Its existence underscores that these functions are normally measured in isolation.
- **Confidence:** Medium-High.

## 3D — Local vs system optimization: Goldratt / Theory of Constraints

### Claim 3.9 — TOC's core insight: improving a non-bottleneck step yields no system gain and can actively harm it — yet most KPI systems reward exactly that.
- **Source:** Symestic — "Production Optimization: Methods, Benchmarks & Common Traps"
- **URL:** https://www.symestic.com/en-us/what-is/production-optimization
- **Date:** 2024-09-22
- **Excerpt (verbatim):** "Eliyahu Goldratt's central insight from The Goal (1984) is still the most underused idea in production: the output of a system is governed by its slowest step. Improving any other step produces no gain at all — only the illusion of one. Worse, it can actively harm the system by building inventory in front of the constraint and starving it behind. The practical consequence: improving utilisation on a non-bottleneck machine is, strictly speaking, a loss. Yet this is exactly what most KPI systems reward, because they measure each machine in isolation."
- **Context:** The theoretical engine of the whole dimension. "Measure each machine in isolation" = functional/silo KPIs; the refinery maximizing its own utilization regardless of the downstream constraint is the downstream instance of this fallacy.
- **Confidence:** High.

### Claim 3.10 — "A system of local optimums is not an optimum system at all."
- **Source:** Flexciton — "The Theory of Constraints"
- **URL:** https://flexciton.com/blog-news/the-theory-of-constraints
- **Date:** 2023-07-13
- **Excerpt (verbatim):** "We shouldn't be looking at each local area and trying to trim it. We should be trying to optimize the whole system. A system of local optimums is not an optimum system at all."
- **Context:** Aphoristic but precise statement that summing local KPI maxima ≠ system maximum — the formal reason silo optimization fails.
- **Confidence:** High.

### Claim 3.11 — Academic comparison: BSC proliferates top-down KPIs that are hard to correlate to the enterprise result; TOC uses a few bottom-up KPIs tied to the goal, and accepts a *local* decrease if the *system* improves.
- **Source:** Thommes (B.), University of Gloucestershire — thesis on system-based performance management and employee motivation
- **URL:** https://eprints.glos.ac.uk/5367/1/Exploring%20the%20relationship%20between%20system%20based%20performance%20management%20systems%20and%20employees%20motivation%20-%20the%20case%20of%20mid-size%20enterprises%20-%20B.%20THOMMES.pdf
- **Date:** undated
- **Excerpt (verbatim):** "There are conflicting approaches between the recent PMMS such as the Balanced Scorecard and the Theory of Constraints. The BSC tries to encompass all the activities of an organization... each unit... develop[s] its own set of KPIs from the top down... This creates a complex system which... causes difficulty in correlating individual KPIs with the organizational result... Goldratt, E. et al. (1986) argue that the optimization of local KPIs does not automatically improve the system's performance. Within the PMMS KPIs must often be traded off per the system's requirements... a decrease in a local measurement can be accepted if the overall performance is improved."
- **Context:** Scholarly framing of the BSC↔TOC tension. Key VCO principle: a *local* KPI may need to get *worse* (e.g., refinery runs below max utilization) for the *system* margin to improve — which local-metric bonus schemes cannot tolerate.
- **Confidence:** High.

### Claim 3.12 — Goldratt's law of measurement: "Tell me how you measure me, and I will tell you how I will behave."
- **Source:** Quotlr — "Eliyahu M. Goldratt quotes"
- **URL:** https://quotlr.com/author/eliyahu-m-goldratt
- **Date:** 2024-01-24 (page)
- **Excerpt (verbatim):** "Tell me how you measure me, and I will tell you how I will behave. — Eliyahu M. Goldratt ... The goal is not to improve one measurement in isolation. The goal is to reduce operational expenses AND reduce inventories and increase throughput simultaneously."
- **Context:** The canonical statement linking measurement → behavior → (mis)incentive. The second quote gives Goldratt's multi-objective goal (throughput ↑, inventory ↓, opex ↓ simultaneously), which single local KPIs violate.
- **Confidence:** High.

---

# SECTION 4 — MISALIGNED KPIs STALL IMPROVEMENT; INCENTIVE-DESIGN PROBLEMS
*(Conflicting interpretations of "good performance"; bonuses tied to local metrics; Goodhart/Campbell gaming)*

## 4A — Misaligned KPIs produce conflicting interpretations and a self-reinforcing stall

### Claim 4.1 — Local optimization "guarantees the whole system's failure": employees rationally defend their KPIs while total output falls, and adding more/tighter KPIs deepens the spiral.
- **Source:** Stratflow — "The KPI Trap: Performance Metrics That Undermine What They Are Meant to Improve"
- **URL:** https://www.stratflow.com.au/post/2-the-kpi-trap-performance-metrics-that-undermine-what-they-are-meant-to-improve
- **Date:** 2025-10-27
- **Excerpt (verbatim):** "Employees focus on their KPIs, even when this comes at the expense of other departments. This is not out of malice but out of rational self-interest... When departments optimize locally, systemic problems occur, and overall performance decreases. Trust and cooperation decline because everyone is defending their KPIs while the total system output decreases... As the number of KPIs increases, greater conflicts in reasoning occur... The system fails not because anyone is incompetent, but because local optimization creates competing priorities and therefore guarantees the whole system's failure."
- **Context:** The clearest causal account of *how* misaligned KPIs stall improvement: a vicious cycle (local KPI focus → system decline → more/tighter KPIs → more conflict). The stated symptoms — "KPIs are green, but system flow is inconsistent"; "costs are creeping up despite efficiency improvements" — are exactly the "conflicting interpretations of good performance" the mission cites.
- **Confidence:** High.

### Claim 4.2 — When each team reports a different number for the same KPI, governance collapses into "whose number is right" rather than "what to do."
- **Source:** Gamblitude — "Conflicting KPIs"
- **URL:** https://gamblitude.ai/problems/conflicting-kpis/
- **Date:** 2025-11-20
- **Excerpt (verbatim):** "the same KPI often has three versions depending on who you ask... This is not a data volume issue – it is a definition and governance issue. When analytics is built without shared semantics, teams optimise against different goals, trust erodes and meetings turn into debates about whose number is right instead of what action to take... Each small variance is 'reasonable' on its own. Together they create a fog where analytics stops being a decision system and becomes a negotiation."
- **Context:** Though from iGaming, this is the crispest articulation of the *decision-stalling* effect of definition inconsistency: analytics becomes "a negotiation." Directly evidences improvement being stalled by metric conflict. (Cross-industry source; flagged as analogous, not downstream-specific.)
- **Confidence:** Medium.

### Claim 4.3 — Multi-site operations without standardized definitions cannot coordinate, compare, or hold anyone accountable.
- **Source:** Lean Data Point (LTS) — "Why Multi-Site KPI Management Creates Alignment Gaps Across Locations"
- **URL:** https://leandatapoint.com/blog/multi-site-kpi-management-alignment-gaps
- **Date:** 2026-03-25
- **Excerpt (verbatim):** "KPI misalignment occurs when teams interpret metrics differently, leading to conflicting priorities... Variations in multi-location performance metrics: Without standardisation, each site may define and measure KPIs differently, creating confusion... These organisational gaps make it hard to coordinate actions, compare performance across sites, and maintain accountability at scale."
- **Context:** Maps the definition-inconsistency problem onto the multi-refinery/multi-depot reality of a downstream organization: without standard definitions, cross-asset comparison and accountability break down.
- **Confidence:** Medium-High.

### Claim 4.4 — KPI overload and misalignment with strategy waste effort and "hamper the organization's growth and competitiveness."
- **Source:** Flevy — "10 Common Pitfalls in KPI Implementation"
- **URL:** https://flevy.com/blog/kpi-library-resource-10-common-pitfalls-in-kpi-implementation/
- **Date:** undated
- **Excerpt (verbatim):** "Misaligned KPIs can result in efforts that do not contribute effectively to the overall success of the organization... employees may be achieving their KPI targets but not making progress towards strategic objectives, indicating a misalignment."
- **Context:** The diagnostic signature of misalignment: *targets met, strategy not advancing*. This is the operational definition of "stalled improvement despite green KPIs."
- **Confidence:** Medium.

## 4B — Incentive design: Goodhart's Law and gaming of local metrics

### Claim 4.5 — Goodhart's Law: tying reward to a measure incentivizes manipulating the measure, sometimes reducing real performance while the metric improves.
- **Source:** CNA — "Goodhart's Law: Recognizing and Mitigating the Manipulation of Measures in Analysis"
- **URL:** https://www.cna.org/reports/2022/09/Goodharts-Law-Recognizing-Mitigating-Manipulation-Measures-in-Analysis.pdf
- **Date:** 2022-09
- **Excerpt (verbatim):** "when we use a measure to reward performance, we provide an incentive to manipulate the measure in order to receive the reward. This can sometimes result in actions that actually reduce the effectiveness of the measured system while paradoxically improving the measurement of system performance."
- **Context:** The formal mechanism behind bonus-driven gaming. CNA adds the analyst's distinction between hard-to-game Measures of Effectiveness (MOEs) and easy-to-game Measures of Performance (MOPs) — the exact gap local KPIs exploit.
- **Confidence:** High.

### Claim 4.6 — Goodhart's Law has a formal basis: optimizing a proxy can be useless (weak) or actively harmful (strong) to the true goal.
- **Source:** arXiv:2410.09638 — "On Goodhart's law, with an application to value alignment" (El-Mhamdi, 2024)
- **URL:** https://arxiv.org/abs/2410.09638
- **Date:** 2024-10-12
- **Excerpt (verbatim):** "'When a measure becomes a target, it ceases to be a good measure'... we introduce a distinction between a weak Goodhart's law, when over-optimizing the metric is useless for the true goal, and a strong Goodhart's law, when over-optimizing the metric is harmful for the true goal."
- **Context:** Peer-reviewed formalization establishing that proxy-metric optimization is not merely neutral but can be *harmful* — the mathematical version of "local optimization guarantees system failure."
- **Confidence:** High.

### Claim 4.7 — Real-world incentive gaming: Wells Fargo's "products per household" bonus metric produced ~2M phony accounts and $3B in settlements.
- **Source:** Sam Tomlinson — "Marketing Paradoxes"
- **URL:** https://www.samtomlinson.me/insights/marketing-paradoxes/
- **Date:** 2025-05-19
- **Excerpt (verbatim):** "Wells Fargo tied branch-staff bonuses to the number of new accounts opened per customer. The metric ('products per household') became the target – exactly as Goodhart warned. To hit impossible quotas, thousands of employees began creating CC, savings & deposit accounts without customer consent. By 2016 the practice had ballooned to more than two million phony accounts, triggering $185 million in fines, mass firings, and a $3 billion federal settlement. The headline KPI looked stellar on quarterly slides, yet the underlying behaviour torched shareholder value."
- **Context:** The canonical cautionary tale of a bonus tied to a local metric: green KPI, catastrophic real outcome. Analogous to a refiner/marketer bonus on a single volume or margin metric.
- **Confidence:** High.

### Claim 4.8 — Incentive-program guidance converges: reward balanced metric sets, not a single number, so employees can't "win the incentive while the company loses."
- **Source:** incentX — "Understanding Goodhart's Law in Employee Incentive Programs"
- **URL:** https://incentx.com/blog/employee-incentive-programs/
- **Date:** 2026-05-11
- **Excerpt (verbatim):** "Goodhart's Law says that when a measure becomes a target, it stops being a good measure... when people are rewarded for hitting a number, they may focus on hitting the number even if the behavior behind it is bad... If a manager is rewarded only for cutting costs, they may reduce spending in ways that hurt employees or customers. The metric improves, but the business gets worse... Effective employee incentive programs use balanced performance metrics... The goal is to stop employees from winning the incentive while the company loses."
- **Context:** Practitioner prescription matching the BCG finding (Section 1): incentives must span output + quality + customer + team + long-term, not one local metric. "The metric improves, but the business gets worse" is the incentive-level restatement of the dimension.
- **Confidence:** Medium-High.

### Claim 4.9 — Bonus-research caveat: most incentive studies *assume* a good target; in practice targets are "either outright dangerous or far enough from the truth that focusing on them may cause harm."
- **Source:** Agile Pain Relief — "Agile Bonuses: The Damage They Do"
- **URL:** https://agilepainrelief.com/blog/agile-bonuses-the-damage-they-do/
- **Date:** 2022-12-07
- **Excerpt (verbatim):** "researchers have a very narrow focus when studying bonuses. With a couple of exceptions, they assumed that the people designing the incentive had chosen a good target... most targets are either outright dangerous (e.g. velocity as a measure of throughput) or far enough from the truth that focusing on them may cause harm... many of the problems created by bonuses come from a lack of consideration to knock-on effects."
- **Context:** Explains *why* bad local KPIs persist in incentive plans: the design literature rarely questions the target itself, only the size of the reward. Systems-thinking ("knock-on effects") is the missing discipline — the TOC point restated for incentives.
- **Confidence:** Medium-High.

### Claim 4.10 — Even in oil & gas, executive pay is hard-wired to a single external benchmark (Solomon first-quartile), and bonus formulas are engineered to mute commodity swings — showing incentive design is a live C-suite issue, not just a shop-floor one.
- **Source:** ExxonMobil — DEF 14A (Proxy Statement)
- **URL:** https://content.equisolve.net/sec/0001193125-24-092545/d784249ddef14a.htm
- **Date:** 2024 (2023 proxy cycle)
- **Excerpt (verbatim):** "First-quartile cost and schedule performance based on Solomon Associates benchmarking and ExxonMobil analysis... Bonus program is based on estimates of year-end earnings... The purpose of the two-thirds adjustment in the formula is to mitigate the impact of commodity price swings on short-term earnings performance."
- **Context:** Demonstrates that (a) Solomon benchmarking is embedded directly in executive incentive metrics, and (b) the formula is deliberately adjusted to strip market noise — an implicit admission that unadjusted metrics (commodity-driven earnings) would mis-measure management performance. This is incentive design grappling with the margin-definition problem at the top of the house.
- **Confidence:** High.

### Claim 4.11 — Campbell's Law and the Cobra Effect generalize the risk: the sheer existence of a measure can trigger gaming, degrading trust and psychological safety.
- **Source:** PsychSafety — "Goodhart's Law, Campbell's Law, and the Cobra Effect"
- **URL:** https://psychsafety.com/goodharts-law-campbells-law-and-the-cobra-effect/
- **Date:** 2025-11-17
- **Excerpt (verbatim):** "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes [Goodhart]... if people are aware that they'll be rewarded for hitting a target or punished for missing it, they will optimise their behaviour to meet that target – even if that behaviour has other negative consequences... The reward doesn't even need to be significant: the sheer existence of the measure can be enough to invoke Goodhart's Law."
- **Context:** Reinforces that KPI misalignment is not just an analytical nuisance — it corrodes the learning culture (psychological safety, trust) that continuous improvement depends on. Links metric design to CI/knowledge-management outcomes.
- **Confidence:** Medium-High.

---

# SECTION 5 — CROSS-CUTTING TENSIONS & SYNTHESIS

- **TENSION A — "Maximize the asset" vs "optimize the system."** The deepest contradiction in the dimension: refinery economics push toward maximum utilization/throughput [^1^], while TOC holds that *"improving utilisation on a non-bottleneck machine is, strictly speaking, a loss"* [^28^] and *"a system of local optimums is not an optimum system at all"* [^30^]. A refiner can post best-in-class utilization while destroying enterprise margin (tank-tops, demurrage, discounted distress sales). The two "good performance" narratives are irreconcilable without a shared value-chain objective [^3^][^6^].

- **TENSION B — One word, many numbers.** "Margin" spans crack spread (products − crude, sign convention variable [^10^][^11^]), gross (excl. opex [^9^]), net (incl. opex/depreciation [^9^]), cash [^12^], and replacement-cost (excl. inventory holding gains/losses [^12^]). "Availability" spans Solomon OA, MA, and internal uptime [^12^][^25^]; "utilization" can exceed 100% depending on denominator [^12^]. Each is defensible in isolation; together they guarantee conflicting performance readings [^4^][^45^].

- **TENSION C — Benchmarks create comparability *and* new incomparability.** Solomon's EII/OA/CWB/CWT and APQC's PCF exist to force apples-to-apples [^24^][^26^][^27^], yet they are proprietary, relative to a moving peer average (EII=100 [^24^]), region-adjusted [^23^], and acknowledged as incomplete (EII "focuses only on the combustion side" [^18^]). Embedding them in regulation (Washington RACT 50th-percentile EII [^42^]; EU ETS top-10% CWT [^43^]) raises the stakes of every definitional choice.

- **TENSION D — Frameworks built to fix misalignment can reproduce it.** The Balanced Scorecard is the default remedy, yet oil-&-gas-specific scholarship warns of "scientific reductionism" and "tyranny" [^20^], metric overload → gridlock [^21^], and weak strategy links [^21^][^22^]; TOC explicitly positions itself against BSC's top-down KPI proliferation [^29^].

- **TENSION E — Incentives are both the problem and the prescribed cure.** BCG lists *"incentive systems"* as a lever to capture US$0.2–0.6/bbl of integration value [^6^], while Goodhart/Campbell evidence shows tying reward to a measure corrupts it [^34^][^35^][^37^]. ExxonMobil's proxy shows the tension managed, not solved: bonuses benchmarked to Solomon first-quartile, but formula-adjusted to strip commodity noise [^39^].

- **Synthesis.** Across ≥45 sources the pattern is consistent: (1) functions are given local KPIs; (2) those KPIs are defined inconsistently across assets and over time; (3) local optimization rationally follows, degrading system margin and stalling improvement [^32^]; (4) incentives hard-wire the behavior [^34^]; (5) the documented fixes are shared/enterprise-value KPIs [^1^], common definitions/process taxonomies [^27^], balanced multi-metric frameworks with regional normalization [^23^], constraint-aligned (system) metrics [^28^][^29^], and balanced incentive design [^36^][^6^].

---

# SEARCH LOG (18 queries executed; ≥15 requirement met)

1. refinery KPI conflict trading operations logistics silo optimization margin throughput
2. conflicting KPIs refinery operations vs trading value chain optimization
3. downstream oil gas KPI misalignment functional silos performance evaluation
4. gross refining margin vs net refining margin definition difference crack spread
5. Solomon Associates refinery utilization availability definition benchmarking EII
6. refinery utilization rate definition capacity Solomon operational availability
7. balanced scorecard oil and gas limitations criticism
8. Theory of Constraints local optimization vs system optimization Goldratt KPI
9. incentive design bonuses local metrics suboptimization silo *(returned 0; re-phrased)*
10. OTIF on-time-in-full definition variants measurement inconsistency supply chain
11. fuel retail volume vs margin tradeoff service station pricing strategy
12. Goodhart's law metric gaming bonus incentive measure becomes target
13. emissions intensity baseline inconsistency refinery GHG scope 1 2 benchmarking comparison
14. APQC process classification framework oil gas downstream benchmarking
15. KPI misalignment stall continuous improvement conflicting good performance interpretation
16. trading desk versus refinery operations tension integrated oil supply optimization incentive *(returned 0)*
17. maximize refinery utilization versus minimize total delivered supply chain cost tradeoff
18. refining margin per barrel regional differences US Europe Asia Singapore comparison benchmark

*Plus supplementary queries: downstream oil gas performance management silo (McKinsey/Bain/BCG); fuel retail volume margin tradeoff supermarket loss leader; bonus tied to refinery metric gaming incentive oil gas.*

---

# SOURCE LIST
*(Numbering matches inline [^N^] citations. Entries marked "consulted" informed context but are not all individually cited inline.)*

[^1^] Opsio Cloud — "Inventory Management for Oil and Gas" (2025-05-14). https://opsiocloud.com/blogs/mastering-inventory-management-for-oil-and-gas-businesses/
[^2^] Journal of Tianjin University (Tianjin Daxue Xuebao) — KPI systems in multi-functional organizations (undated). https://tianjindaxuexuebao.com/dashboard/uploads/23.18885385.pdf
[^3^] KBC — "Value Chain Optimization Manifesto" (2020). https://www.kbc.global/uploads/files/whitepapers/0095-VCOmani-MANI-US-092020.pdf
[^4^] Gamblitude — "Conflicting KPIs" (2025-11-20). https://gamblitude.ai/problems/conflicting-kpis/
[^5^] Lean Data Point (LTS) — "Why Multi-Site KPI Management Creates Alignment Gaps Across Locations" (2026-03-25). https://leandatapoint.com/blog/multi-site-kpi-management-alignment-gaps
[^6^] BCG (via Cuadernos Orkestra / emcombustion) — "The Oil and Gas value chain: a focus on oil refining" (undated, ~2018). https://emcombustion.es/wp-content/uploads/2018/12/orkestra_the-oil-gas-value-chain-refining-emcombustion1.pdf
[^7^] Australian Institute of Petroleum — "Facts About the Australian Retail Fuels Market and Prices" (2017-11). https://aip.com.au/sites/default/files/download-files/2017-11/Facts%20About%20the%20Australian%20Retail%20Fuels%20Market%20and%20Prices.pdf
[^8^] NBER — "General Characteristics of the Petroleum Industry and Its Price Problems" (undated). https://www.nber.org/system/files/chapters/c5803/c5803.pdf
[^9^] University lecture (UoMus, Iraq) — "Refining Margins: Definition and Importance" (2025). https://uomus.edu.iq/img/lectures21/MUCLecture_2025_22841197.pdf
[^10^] GlobalOilShock — "Refining Margin Explained" (undated). https://globaloilshock.com/en/glossary/refining-margin/
[^11^] "Commodity Option Pricing: A Practitioner's Guide" (textbook, undated). http://students.aiu.edu/submissions/profiles/resources/onlineBook/s5W5t9_commodity%20option%20pricing%20finance.pdf
[^12^] BP — "Annual Report and Form 20-F 2018 — Glossary" (2018). https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/pdfs/investors/bp-annual-report-and-form-20f-2018-glossary.pdf
[^13^] IEA / KBC — "Refinery Margins: Methodology Notes" (2012-09-12). https://iea.blob.core.windows.net/assets/cbf37dfc-5fe1-4854-b248-95e6a2e5240a/Refining_Margin_Supplement_OMRAUG_12SEP2012.pdf
[^14^] Energy Aspects — "Refining Margins" service overview (2020). https://web-cdn.energyaspects.com/service_overviews/2020/energy_aspects_refining_margins_service_overview_2020_5e1473be343fd.pdf
[^15^] Baidu Baike (EN) — "Integrated Refining Margin" (2026-06-02). https://baike.baidu.com/en/item/Integrated%20Refining%20Margin/1673976
[^16^] Tive — "What is OTIF, How to Calculate and How did it Come About?" (2025-07-08). https://www.tive.com/blog/on-time-in-full-otif-what-is-otif-and-how-to-improve-metrics-with-technology
[^17^] GPX — "Maximizing On-Time In-Full (OTIF) In Supply Chain" (2026-01-30). https://gpx.co/blog/on-time-in-full-otif-in-supply-chain/
[^18^] Hydrocarbon Engineering — "Benchmarking methodologies" (2015-02-05). https://www.hydrocarbonengineering.com/special-reports/05022015/Benchmarking-methodologies-193/
[^19^] European Commission (circabc) — "Impact Analysis of Options for Implementing Article 7a of Directive 98/70/EC (Fuel Quality Directive)" (undated). https://circabc.europa.eu/sd/a/8aaca016-9c12-4b85-8e3e-5561ff752bfd/MASTER_FQD%20IA%20Final%20Report%202%20Aug%20(2).pdf
[^19b^] Woodside — "North West Shelf Project Extension Environmental Review Document" (undated). https://www.woodside.com/docs/default-source/current-consultation-activities/australian-activties/nws-project-extension-combined.pdf
[^20^] Spence (2020), Robert Gordon University — PhD thesis, "The influence of organisational typology... on UK offshore oil and gas industry safety performance." https://rgu-repository.worktribe.com/preview/1358167/SPENCE%202020%20The%20influence%20of%20organisational%20typology.pdf
[^21^] MadeToMeasureKPIs — "6 Disadvantages of a Balanced Scorecard" (2025-03-11). https://madetomeasurekpis.com/blog/2024/11/18/6-disadvantages-of-balanced-scorecard/
[^22^] BPM Institute — "Problems Implementing a Balanced Scorecard" (2022-12-09). https://www.bpminstitute.org/resources/articles/problems-implementing-balanced-scorecard/
[^23^] Solomon Insight — "World's Best Refineries Analysis Report" (undated; 2016/2018/2020 cycles). https://www.solomoninsight.com/industries/refining/worlds-best-refineries
[^24^] boTec — "Solomon Energy Intensity Index (EII)" (2025-10-28). https://botec.com/glossary/solomon-energy-intensity-index-eii/
[^25^] Solomon Insight — "Turnaround Maintenance Insights" (undated). https://www.solomoninsight.com/blog/turnaround-maintenance-insights
[^26^] APQC — "Process Classification Framework (PCF) — Downstream Petroleum v7.2.2" (2026-05-06). https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-downstream-petroleum-2
[^27^] APQC — "Process Classification Framework (PCF) — Petroleum Upstream (PDF)" (2026-05-06). https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-petroleum-upstream-pdf
[^28^] Symestic — "Production Optimization: Methods, Benchmarks & Common Traps" (2024-09-22). https://www.symestic.com/en-us/what-is/production-optimization
[^29^] Thommes (B.), University of Gloucestershire — thesis on system-based performance management and employee motivation (undated). https://eprints.glos.ac.uk/5367/1/
[^30^] Flexciton — "The Theory of Constraints" (2023-07-13). https://flexciton.com/blog-news/the-theory-of-constraints
[^31^] Quotlr — "Eliyahu M. Goldratt Quotes" (2024-01-24). https://quotlr.com/author/eliyahu-m-goldratt
[^32^] Stratflow — "The KPI Trap: Performance Metrics That Undermine What They Are Meant to Improve" (2025-10-27). https://www.stratflow.com.au/post/2-the-kpi-trap-performance-metrics-that-undermine-what-they-are-meant-to-improve
[^33^] El-Mhamdi, E.M. (2024) — "On Goodhart's law, with an application to value alignment," arXiv:2410.09638. https://arxiv.org/abs/2410.09638
[^34^] CNA — "Goodhart's Law: Recognizing and Mitigating the Manipulation of Measures in Analysis" (2022-09). https://www.cna.org/reports/2022/09/Goodharts-Law-Recognizing-Mitigating-Manipulation-Measures-in-Analysis.pdf
[^35^] PsychSafety — "Goodhart's Law, Campbell's Law, and the Cobra Effect" (2025-11-17). https://psychsafety.com/goodharts-law-campbells-law-and-the-cobra-effect/
[^36^] incentX — "Understanding Goodhart's Law in Employee Incentive Programs" (2026-05-11). https://incentx.com/blog/employee-incentive-programs/
[^37^] Sam Tomlinson — "Marketing Paradoxes" (2025-05-19). https://www.samtomlinson.me/insights/marketing-paradoxes/
[^38^] Agile Pain Relief — "Agile Bonuses: The Damage They Do" (2022-12-07). https://agilepainrelief.com/blog/agile-bonuses-the-damage-they-do/
[^39^] ExxonMobil — DEF 14A Proxy Statement (2024). https://content.equisolve.net/sec/0001193125-24-092545/d784249ddef14a.htm
[^40^] ERIA — "Chapter 4: Efforts in the Majors / Non-ASEAN NOCs" (citing BP 2022, undated). https://www.eria.org/uploads/media/Research-Project-Report/RPR-2022-15/12_Chapter-4-Efforts-in-the-Majors-Non-ASEAN-NOCs.pdf
[^41^] Tilburg University repository — thesis on OTIF / delivery reliability (undated). http://arno.uvt.nl/show.cgi?fid=190924
[^42^] Solomon Insight — "Washington State Refineries to Use Solomon Benchmarking Methodology to Help Control Greenhouse Gas Emissions" (2014-06-10). https://www.solomoninsight.com/news/washington-state-refineries-to-use-solomon-benchmarking-methodology-to-help-control-greenhouse-gas-emissions
[^43^] CONCAWE / ResearchGate — "Developing a methodology for an EU refining industry CO2 emissions benchmark," report 9/12 (2012). https://www.researchgate.net/publication/292572306_Developing_a_methodology_for_an_EU_refining_industry_CO2_emissions_benchmark
[^44^] ExxonMobil — Transcript of Analysts Meeting (2005-03-09) *(consulted)*. https://investor.exxonmobil.com/sec-filings/all-sec-filings/content/0001193125-05-050581/dex991.htm
[^45^] BluePes — "KPI misalignment: why teams report different numbers" (2026-02-23). https://bluepes.com/blog/multiple-versions-of-truth-kpi-misalignment
[^46^] Vector — "OTIF: On Time In Full, Definition, Tracking And Measurement" (2025-04-08) *(consulted)*. https://www.withvector.com/blog/on-time-in-full-otif-definition-how-to-track-measure/
[^47^] Unleashed Software — "What is OTIF? Meaning, Calculation, & How to Improve" (2024-04-10) *(consulted)*. https://www.unleashedsoftware.com/blog/otif/
[^48^] Transpara — "10 Real-Time KPIs Every Oil and Gas Refining Operations Leader Should Be Watching" (2026-03-04) *(consulted)*. https://www.transpara.com/10-real-time-kpis-every-oil-and-gas-refining-operations-leader-should-be-watching/
[^49^] U.S. EIA — "Global refinery margins fall to multiyear seasonal lows in September" (2024-10-15) *(consulted)*. https://www.eia.gov/todayinenergy/detail.php?id=63447
[^50^] ScienceDirect — "Is the refining margin stationary?" (2016-07-01). https://www.sciencedirect.com/science/article/abs/pii/S1059056016300247

---

*End of Dimension 09 research file. All excerpts are verbatim from the cited sources; bracketed ellipses mark omitted text. Cross-industry sources (e.g., [^4^] iGaming, [^37^] banking) are used as analogous evidence for the incentive/definition mechanisms and are flagged as such in-line.*
