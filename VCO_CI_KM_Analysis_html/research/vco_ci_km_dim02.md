# Dimension 02 — What "VCO" Means in Practice: The Downstream Planning & Optimization Stack

**Study:** Value Chain Optimization (VCO), lookback/backcasting, and CI knowledge management — downstream refining & marketing
**Dimension:** 02 — What "VCO" means in practice: planning & optimization stack
**Date compiled:** 2026-07-18
**Method:** 45 independent web searches (vendor documentation and whitepapers — AspenTech, AVEVA, Honeywell, SAP, Kalibrate, ION/Openlink, o9, Kinaxis; industry analysts — ARC Advisory Group; conference/professional literature — AFPM, ERTC/WRA, PTQ, DYCOPS, AIChE, Hydrocarbon Engineering, Processing Magazine; academic literature — Springer, arXiv, OIES, MILP/scheduling journals; operator job postings and training curricula as practice evidence). Sources without a visible publication date are marked "n.d. (accessed 2026-07-18)".
**Citation convention:** Inline `[^N^]` refers to the numbered source list at the end. Verbatim excerpts are quoted with source, URL, date, context, and confidence in the Evidence Register.

---

## KEY FINDINGS (summary)

1. **"VCO" in practice is a layered stack, not one tool.** The operating reality is a hierarchy: LP-based planning (monthly/weekly) → refinery scheduling and blending (days–weeks) → APC/DCS execution (real time), wrapped by supply/distribution network optimization, demand forecasting, retail price optimization, and ETRM/CTRM trading-risk systems. The central, explicitly named problem is the **"plan vs. actual" gap** (a.k.a. "margin leakage") between these layers; vendors and operators quantify it at up to **10% of crude margin** (Saudi Aramco Yanbu) and **> $1/bbl of unaccounted loss** even at well-run refineries.[^27^][^29^]

2. **Refinery planning runs on a small LP oligopoly.** Aspen PIMS, Honeywell RPMS, Haverly GRTMPS, and AVEVA Spiral/USC Plan (plus Chevron's internal PETRO) are the standard engines for crude selection/valuation, run plans and product slate, using successive/recursive LP with pooling and blending non-linearities.[^1^][^4^][^35^][^68^] **Multi-period and multi-site extensions are established practice**: RPMS multi-period property tracking; Aspen PIMS-AO and Aspen Unified Multi-site (feedstock sourcing, freight, inventory, product-location optimization); AVEVA USC Network "with full plant models when combined with Plan"; Galp's GRTMPS model optimizing refinery–depot–1,200-station connections.[^2^][^5^][^12^][^36^]

3. **Scheduling/blending is the bridge and the bottleneck.** Aspen Petroleum Scheduler claims use at **>45% of global refineries** (250+ plants); Honeywell's blending & movement suite claims installations **"representing over 25 percent of the world's refining capacity."** Event-based, multi-period, multi-blend optimization (Aspen MBO; Honeywell BLEND) is state of practice; Chevron deployed Aspen MBO at eight refineries with documented change-management effort.[^7^][^8^][^15^][^16^] Yet **Excel remains pervasive** in scheduling at many sites — a documented maturity floor.[^12^][^56^][^58^]

4. **S&OP/IBP is converging with classic LP planning.** SAP IBP (S&OP, Demand, Supply, Inventory modules positioned for refinery optimization and depot inventory), AspenTech's aspenONE SCM (Supply Chain Planner, Collaborative Demand Manager, "SCM Insights" to "digitally operationalize the monthly S&OP/IBP process"), o9 and Kinaxis are all pushing into O&G. The **ExxonMobil–Kinaxis co-development** (announced Oct 2024) of a purpose-built O&G concurrent-planning solution is the strongest signal that ERP-style planning is merging with the hydrocarbon planning stack — while ARC notes the industry "has historically relied on customized or semi-customized solutions, often involving numerous spreadsheets and manual processes."[^39^][^55^][^56^][^57^][^63^]

5. **Retail fuel pricing is a mature optimization island.** Kalibrate reports 600,000–760,000 prices/day to 65,000+ sites in 40+ countries, AI price optimization balancing volume vs. margin via elasticity, with claimed benefits of **$83–454 per site per week** and **+0.9–1.9% volume**. This layer is largely decoupled from refinery LP planning — a VCO seam.[^40^][^41^][^42^]

6. **Trading & risk (ETRM/CTRM) connects to planning mainly through prices, not closed loops.** ION Openlink Endur-class platforms run deal capture→risk→logistics→settlement; academic and textbook sources confirm hedging costs and price-risk of inventory differentials are (or should be) explicit cost elements in refinery supply-chain planning. Integration to LP planning is via price forecasts, crack-spread views, and crude valuation — not automated feedback.[^44^][^45^][^46^]

7. **Organizational models cluster into three patterns:** (a) **site-based planning teams** with a named LP-model custodian and economists (Shell "Economics Model Coordinator"); (b) **central supply/optimization groups** spanning crude supply, trading, planning and logistics (Valero's "Supply & Optimization"/"Refinery Planning & Economics"/"Crude, Feedstock Supply & Trading" career ladder; ExxonMobil's single supply-chain president with end-to-end planning + "DNA" analytics; PetroChina's 11-refinery standardized APS); (c) **national/integrated "hydrocarbon system" planning** (Saudi Aramco central LP Modeling Engineers producing Business-Plan LP runs and **monthly "back-casting" reports on the LP gap**).[^51^][^52^][^53^][^55^][^59^][^2^]

8. **Documented benefits are large but mostly vendor-reported.** AVEVA claims "effective economic optimization of hydrocarbon value chain can boost profitability by **$50–300 million per year for a typical oil refinery**"; ExxonMobil cloud planning "**improved profitability by 70¢/bbl**" and cut planning runs from 7+ hours to <4 minutes; BP: calculations from 7 hours to 4 minutes, optimization decisions from 2 days to 2 hours; LP accuracy alone is valued at **~$0.50/bbl** (> $50M/yr for a 300 kbpd refinery); closed-loop dynamic optimization **$4–10M/yr** (middle distillates). Independent analyst corroboration is more modest: ARC cites **$0.05–0.15/bbl** for closed-loop plan-schedule-APC integration.[^21^][^22^][^23^][^20^][^32^][^31^][^12^]

9. **Maturity is bimodal.** Frontier: unified multi-site cloud planning (BP, ExxonMobil on AVEVA), refinery-wide RTO closing plan-vs-actual (Yanbu), closed-loop AI optimization (Aspen GDOT, Imubit). Baseline: off-line LP + Excel schedules + manual handoffs ("the scheduler will then manually pass along these spreadsheets"), decaying LP accuracy ("Everyone is very busy, and nobody has time!"), and academic scheduling methods that remain impractical ("the short-term scheduling job of oil refinery processes is still done manually by planners").[^12^][^32^][^48^]

10. **Backcasting/lookback is an emerging, named discipline inside VCO.** Aramco's LP engineers "perform 'back-casting' and issue a monthly report on the LP gap along with required mitigations"; Shell institutionalizes Margin Variance Analysis (MVA) and LP "post-mortem analysis"; KBC deployed "advanced planning and backcasting tools [that] improved crude selection and operational alignment with the LP"; consultancies sell "Backcasting, Auditing, and Unit Model Validation"; AVEVA's VCO framework names "Prescriptive Performance (Plan vs. Actual)" and "Planning Model Tracking/Update" as distinct layers.[^52^][^51^][^34^][^66^][^24^]

---
## 1. Refinery LP models — crude selection, run plans, product slate

### 1.1 The standard engines and what they do

Refinery planning is built on successive/recursive linear programming. The market is an oligopoly of table-driven LP systems — **Aspen PIMS** ("Process Industry Modeling System"), **Honeywell RPMS** ("Refinery and Petrochemical Modeling System"), **Haverly GRTMPS**, and **AVEVA Unified Supply Chain – Plan** (formerly Spiral Plan); Chevron's PETRO is a notable proprietary system.[^1^][^4^][^35^][^68^] Popescu (2018): *"The most popular manufacturing optimization software used today by most refineries are RPMS (Honeywell License), PIMS (Aspen License), and GRTMPS (Harperly Systems License), all based on the LP-Linear Programming principles."*[^4^]

Core uses, per vendor and academic documentation:

- **Crude selection & valuation:** AspenTech: *"in determining which crudes to process, a refinery must consider at least their price and composition, how they affect the refinery's ever-changing production constraints and the yield and price of each potential product."*[^1^] RPMS answers *"key business questions related to raw material purchases, product specifications, plant operation, and distribution and logistics."*[^3^] Crude valuation practice uses LP-derived "relative value in use" / crude indifference values (OGJ notes the tension that market transactions rarely use LP valuations directly — see §6).[^50^][^54^]
- **Run plans & product slate across horizons:** RPMS is documented in use for *"strategic planning (long term over 5 years); medium-term planning (1–3 years); short-term planning (one month-quarter)"* plus evaluation of alternative feedstock offers and investment projects, maximizing marginal revenue subject to unit, quality and logistics constraints.[^4^] PIMS training curricula cover crude distillation tables, base-delta yield shifts with feed quality, pooling & recursion, blending, case stacking, marginal values and break-even analysis.[^71^]
- **Objective function:** LP optimizes Gross Refining Margin — *"The LP tool is an optimizer whose objective function is the GRM (Gross Refining Margin) of the refinery and attempts to maximize this GRM subject to many constraints."*[^49^]

### 1.2 Multi-period and multi-site extensions

- **RPMS:** *"advanced modeling capabilities that provide mixed integer programming, innovative property tracking techniques for multi-period models, fast recursions and streamlined recursion property calculation techniques"* — deployed as PetroChina's Advanced Planning System across **11 refining/petrochemical sites** for crude selection, production distribution and plant production.[^2^]
- **Aspen PIMS-AO:** proprietary solver with *"parallel processing, enhanced global optimization, feedstock basket reduction, and nonlinear modeling"* — "at least 8 times faster" per OMV validation; **Aspen Unified Multi-site for PIMS** *"optimizes the value chain to reduce cost and increase margin by selecting optimal product locations and feedstock sourcing, freight, and inventory usage."*[^20^][^12^]
- **AVEVA Unified Supply Chain – Network:** *"Supply and distribution network optimization with unified integrated analytics – Includes full plant models when combined with Plan."*[^5^] AVEVA's thesis-level description frames the suite as *"an integrated refinery planning, scheduling, and optimization tool… managing crude selection, production planning, operational scheduling, and supply chain logistics."*[^6^]
- **Haverly GRTMPS network models:** Galp's downstream planning *"is accomplished through an optimisation model developed through GRTMPS software… considers numerous inputs such as several international quotations (e.g. from Platts and Argus), distances between network facilities (refineries, depots and service stations) or demand across the network… The output of the model is a complex network of downstream supply. It provides the optimal connections between refineries, depots and service stations"* (1,200+ stations).[^36^]
- **Consultancy practice:** multi-period planning with inventory optimization is a standard deliverable (e.g., Bangchak, Thailand: *"Delivered multi-period planning model with inventory optimization… Custom excel template-based reports for monthly operating plan and crude indifference value (CIV)"*).[^68^]

## 2. Advanced planning & scheduling (APS), refinery scheduling & blending, S&OP/IBP

### 2.1 Refinery scheduling — the plan-execution bridge

Scheduling decomposes the LP's period-average plan into feasible daily/event-level operations. ARC describes the traditional baseline: *"Planners will often run an off-line linear program (LP) optimization model to develop an average operating plan across the planning period… Schedulers will break down the current planning period into a sequence of scheduled steps of the operation to ensure feasible management of inventories… Excel spreadsheets are often used to prepare a schedule. The scheduler will then manually pass along these spreadsheets with the operating targets to the unit control operator."*[^12^]

Commercial state of practice:

- **Aspen Petroleum Scheduler (formerly Orion[^9^]):** *"an event-based, single-blend optimization solution that supports the scheduling of all refinery activities for over 45% of global refineries. It integrates with Aspen PIMS to achieve greater profitability through more accurate planning and scheduling… extends beyond the refinery gate to include dock operations and pipeline movements."*[^7^] Azure Marketplace listing: *"trusted by more than 250 refineries and chemical plants globally… Aspen Petroleum Scheduler is positioned powerfully to enable more stable refinery operations and bring actual results closer to the optimal plan."*[^8^]
- **Aspen Unified Scheduling:** next-gen successor — *"Create a feasible schedule using the optimal plan results and capturing schedulers' valuable knowledge, improving margins and reducing emissions by closing the gap between plan and schedule… Develop a scheduling model from your existing Unified PIMS model."*[^11^]
- **AVEVA Spiral/USC Schedule:** shares *"the same plant definition and mathematical engine as… Plan… with easy comparison of plan vs. schedule… Integration with plant data… allows quick reconciliation of the schedule to understand differences between schedule vs. actual, and highlights issues with both modeling and execution."*[^25^]
- **Honeywell scheduling lineage:** UOP refinery scheduling/blending technology combined with Honeywell's *Production Scheduler for Refining* — *"a joint integrated refinery-wide scheduling and schedule optimization solution for crude oil receiving and blending, refinery process units and finished product blending."*[^18^][^19^]
- **In-house/hybrid practice:** ANCAP (Uruguay) runs RPMS for short/medium/long-term studies (crude purchases, contracts, production plans, investments) alongside in-house daily inventory-scheduling simulators over a one-year horizon, a crude-terminal scheduling model, and an LPG blending/scheduling model — *"Results from both planning and scheduling models support pricing decisions for products between the production and commercial areas."*[^13^]

### 2.2 Blending optimization — where margin becomes real

- **Aspen Refinery Multi-Blend Optimizer (MBO):** *"off-line blend scheduling and optimization capabilities for gasoline, distillates, fuel oil… event-based, multi-period, blend modeling systems"* for short/long campaigns with non-linear blending, tank constraints and rundown blending.[^10^] **Chevron deployed Aspen MBO at eight refineries** — *"It describes the successful deployment of Aspen MBO at eight Chevron refineries, the lessons learned and the benefits captured. The paper discusses the project timeline, the organizational structure and the change management process associated with a rollout of such scope."* (AFPM plant-automation session)[^16^]
- **Honeywell BLEND / BMA:** *"BLEND is multi-period, multi-blend optimization software for petroleum products… produces the optimum blending recipes for each batch"* plus Blend Performance Monitor, Blend Controller, Inventory Monitor, Movement Control/Monitor.[^14^] Installed base *"at hundreds of sites globally, representing over 25 percent of the world's refining capacity."*[^15^]
- **Quantified blending value:** ConocoPhillips Wood River — *"Optimal Gasoline Blending contributes more than half of the APC savings of the entire refinery"* (Honeywell BRC+BPC with NIR analyzers).[^16^] LUKOIL Nizhegorodnefteorgsintez (Honeywell Profit Blend Optimizer): *"the optimization… is estimated to have added profits equivalent to $0.12/barrel."*[^17^] Giveaway benchmarks: *"Industry benchmarks place average U.S. octane giveaway around 0.5 octane numbers and average RVP giveaway near 0.3 psi… multimillion-dollar annual losses."*[^30^]
- **Maturity ladder for blending:** RBC (regulatory ratio control) → ABC (analyzer-feedback advanced control) → OOPS (off-line optimization & planning): *"The third level… is the off-line optimization of a blend recipe taking into account the refining process as expected in advance… done on a Personal Computer (PC) by a refinery planner and then he downloads the optimized recipe to the online blend control (ABC) system."*[^70^]

### 2.3 S&OP / Integrated Business Planning in refining

- **AspenTech aspenONE SCM** explicitly maps products onto S&OP/IBP: Aspen Collaborative Demand Manager (forecasting), Aspen Supply Chain Planner (*"Maximize profitability in your supply chain network with an optimized supply plan that simultaneously considers all constraints and supports sales & operations planning"*), and Aspen SCM Insights to *"digitally operationalize the monthly Sales & Operations Planning (S&OP)/Integrated Business Planning (IBP) process."*[^63^]
- **SAP IBP for O&G:** positioned to integrate *"sales, operations, and finance plans into one unified process… Applying IBP's core modules — S&OP, Demand, Supply, and Inventory — to real industry use cases such as demand forecasting, refinery optimization, and depot inventory management."*[^39^] SAP's downstream logistics backbone remains IS-Oil/S4: TSW (Trader's & Scheduler's Workbench) for pipeline nominations and shipment tracking; SDR (Secondary Distribution & Replenishment) for terminal-to-retail delivery scheduling — plus HPM, TDP, EXG, TD, MAP, MCOE, MRN, BDRP modules.[^37^][^38^]
- **o9:** an unnamed supermajor customer *"had highly manual and Excel-driven planning processes with data challenges and a lack of inventory visibility… With o9, they obtained… full visibility over sales, inventory and supply chain planning on a single integrated… cloud native platform… Systems Replaced: Excel and Legacy Systems."* (KPIs: planning accuracy, inventory reduction, demurrage decrease.)[^58^]
- **Kinaxis–ExxonMobil:** co-development (announced 2024-10-16) *"to create supply chain technology solutions designed specifically for the energy sector"* using Kinaxis Maestro.[^57^] ARC's framing: *"it would seem no comprehensive supply chain management solution has really existed to help the oil and gas industry… achieve a unified view of their supply chain… Due to the complexity and scarcity of available solutions, such as advanced planning systems, the oil and gas industry has historically relied on customized or semi-customized solutions, often involving numerous spreadsheets and manual processes."*[^56^]

## 3. Supply/distribution networks, demand forecasting, pricing, trading & risk

### 3.1 Supply & distribution network optimization

Refining is framed as a constrained supply-chain node: *"A refinery is not merely a production plant. It is a highly constrained supply chain node that sits at the intersection of procurement, processing, blending, storage, transportation, and demand fulfillment… A margin-optimized refinery plan only creates value if the supply chain can execute it."*[^60^] Documented network-optimization practice: AVEVA USC Network (§1.2), Galp's GRTMPS refinery–depot–station model,[^36^] Aspen Petroleum Supply Chain Planner (case-comparison analytics; integration with Aspen IMOS for rail and Petroleum Scheduler for refinery-distribution coordination).[^72^] Textbook requirements (Stadtler & Kilger, ch. 24) include crude purchase decisions under long lead times, forecast accuracy per product, transport/storage capacities, and **price-risk/hedging costs as explicit planning cost elements**: *"A price risk exists, if there is a difference between planned inventories of crude oil and inventories of finished products. These price risks have to be secured on the market and these hedging costs or working capital costs have to be taken in the planning system as an element of costs."*[^46^]

### 3.2 Demand forecasting

ML is displacing econometric baselines at the market level: OIES (Nov 2024) applied XGBoost and N-HiTS across seven refined products and seven regions, achieving *"a Mean Absolute Percentage Error (MAPE) of less than 10% on average for monthly short-term forecasts extending one year out-of-sample,"* with N-HiTS preferred for maintainability (1 model/region vs. 167 for XGBoost); the paper itself uses *backcasting* plus Prophet to fill training data gaps.[^43^] At the operational level, demand forecasts feed S&OP/IBP and network models (§2.3, §3.1); crack-spread forecasting is explicitly linked to procurement optimization and hedging strategy in the refinery supply-chain literature.[^73^]

### 3.3 Retail fuel pricing engines

Kalibrate (market leader) documents the practice: rules engines (120+ rules/validations), patented AI for elasticity-based price optimization, POS/pump integration, mobile approvals: *"Kalibrate's patented AI recommends optimal fuel prices that balance volume and margin… Based on demand signals, price elasticity, and market shifts across your sites and network."*[^40^] Scale and claimed outcomes: *"600,000 prices a day to over 65,000 sites"* in 40+ countries; *"$331 avg weekly profit increase per site with AI optimization… 1.9% avg volume growth"*;[^40^][^41^] SIGMA profile: *"sell 1.4% more volume and increase gross profit by an average of $454 per site, per week."*[^42^] Notably, pricing engines sit downstream of the refinery VCO stack — connected through product supply costs and volume commitments, not through the LP.

### 3.4 Trading & risk (ETRM/CTRM)

ETRM platforms (ION Openlink Endur/RightAngle/Aspect class) cover *"deal capture, market connectivity, price curves, scheduling, risk modelling, hedging strategies, P&L reporting, settlements, regulatory reporting, and financial integration"* across crude, refined products, gas, power and emissions, with *"real-time and near real-time updates through APIs, event-driven messaging, DEX streams, and database-level synchronisation."*[^44^][^45^] The VCO linkage is two-way but thin in practice: (i) trading provides price curves/crack views and executes hedges around the LP plan's net exposures (Stadtler's hedging-cost framing above; refinery crack-spread hedging literature);[^46^] (ii) planners/traders share crude intelligence — BP's case shows planning-speed directly serving trading: *"individual calculation times have fallen from seven hours to four minutes, while optimization decisions that used to take two days now take two hours. This enables bp's trading teams to make more informed risk-based crude purchase decisions."*[^21^] Vendor/operator evidence of a fully automated ETRM↔LP closed loop was **not found** in this scan — a genuine gap.

---
## 4. VCO as a cross-functional operating system — functions and organizational models

### 4.1 What "VCO" spans

AspenTech's own definition anchors VCO as enterprise-wide adjustment: *"Value chain optimization is the strategic adjustment of a company's process to achieve optimal results within their value chain… maximizing margins… but increasing reliability, reducing energy usage, or improving operational efficiency are other frequent priorities."*[^62^] AVEVA's VCO framework (2022–2023 roadmaps) spans the full decision horizon stack — *"Long Term Business Planning / Corporate Planning / Investment Planning (1 year, fiscal targets) → Production Planning / Crude Management / Supply and Distribution Planning (1–3 months) → Scheduling / Logistics / Daily Scheduling (1–15 days) → Operations / Process Optimization / Energy Management / Offsite Management (current time) → Production Accounting / Planning Model Tracking/Update / Prescriptive Performance (Plan vs. Actual) (after operation)"* — explicitly including the lookback layer.[^24^][^23^]

AVEVA also documents that VCO is fundamentally about reconciling **conflicting functional targets**: the crude trader (processing experience, distress-cargo opportunities), refinery scheduler (*"are there margin leaks in plan v/s schedule v/s actual?"*), logistics planner (demand flexibility, supply-change impacts), production planner (model accuracy, robust plan), operations manager (safety, meeting plan targets).[^23^] Petronas frames the same ambition as *"synchronize all business and operations activities across the supply chain from feedstock selection to planning, scheduling, operations and distribution."*[^26^] Sustainability is now inside scope: BP runs *"commercial CO2 emission modeling for refinery operations using AVEVA supply chain optimization"*;[^21^] Aspen Unified PIMS won a 2024 Hydrocarbon Processing award for *"monitoring and predicting CO2 emissions while balancing operational efficiencies."*[^75^]

### 4.2 Organizational models observed

**(a) Site-based planning teams with a named LP custodian.** Shell's "Economics Model Coordinator" (Malaysia): *"Serve as the custodian of the planning/PIMS/LP model… Assists the economists in Monthly/Weekly Plan Handshakes, Crude Purchasing Nominations and Annual Business Plan activities… Assist in LP (PIMS) runs to assess site actual performance vs planned performance using the Margin Variance Analysis (MVA) process… develop/adopt techniques for post-mortem analysis and robust crude cargo analysis."* The role also owns "Basic Data" (mass balances, yields/capacities, blending correlations), crude assay intelligence shared with Trading, and Refinery Yield Accuracy assurance.[^51^]

**(b) Central supply & optimization organizations.** Valero's executive career paths reveal the function stack: *"Director-Supply & Optimization, Vice President-Refinery Planning & Economics, and Senior Vice President-Crude, Feedstock Supply & Trading"*; the Chief Commercial Officer has *"oversight of the company's crude supply and products trading, wholesale marketing, transportation and international commercial operations groups… Simmons directs the supply, trading and hedging activities for supply of crude oil to all Valero refineries, and oversees international operations and refinery systems optimization."*[^59^] ExxonMobil consolidated supply chain under one umbrella: *"we are organised to have supply chain end-to-end planning, which I actually own. We have logistics excellence, we have materials management, and we have the digital network and advanced analytics, which we call our DNA… we're under one supply chain president who reports to our management committee."*[^55^]

**(c) National/integrated "hydrocarbon system" planning.** Saudi Aramco LP Modeling Engineer: *"Run the oil & gas and refinery linear programing models to generate the Business Plan level of operations for the Hydrocarbon system… Perform 'back-casting' and issue a monthly report on the LP gap along with required mitigations… Work with different operations divisions to ensure that short range operating plans are aligned with the long term plans in terms of modeling accuracy."*[^52^] A parallel Aramco LP Engineer posting demands 15 years' refining LP experience, multi-configuration modeling, and *"a proven track record of applying linear programming models to drive significant improvements in refining margin, with specific quantified examples such as margin uplift, crude diet flexibility, product slate optimization, or energy cost reduction."*[^53^] PetroChina standardized one APS (Honeywell RPMS) across 11 sites.[^2^]

**(d) VCO / planning enablement roles in industry practice.** Training providers define the planner's span: *"Refinery Planning Business Processes… typical interactions and the challenges for planners… single-period LP models, multi-period & multi-location modelling, Crude & Product opportunity evaluation"* and the planning cycle *"Long Term / Strategic Plan → Annual / Budgetary Plans → Monthly / Weekly Operating Plans → Special case studies,"* including *"Back casting using LP"* and *"Crude indifference value analysis."*[^54^]

## 5. Documented benefits, maturity levels, and the plan-vs-actual problem

### 5.1 Benefits (as claimed by vendors/operators — see §6 caveats)

| Benefit area | Claim | Source |
|---|---|---|
| Whole hydrocarbon value chain optimization | "$50 to 300 million per year for a typical oil refinery" | AVEVA decks 2022[^23^][^74^] |
| Cloud unified supply chain planning (ExxonMobil) | "Reduced time from 7+ hrs. to <4 mins per planning model; Improved profitability by 70c/bbl" | AVEVA PI World 2021[^22^] |
| Process optimization/digital twin (unnamed major) | "$750MM/yr." program benefits | AVEVA PI World 2021[^22^] |
| Rapid reaction to market volatility | "$60–100MM in benefits per model run; $1 Billion in cumulative benefits over 3 years" | AVEVA PI World 2021[^22^] |
| Integrated APC + offsites + production accounting (7 sites) | "Incremental profit of ×$7MM/year in RBOB; Saving of ×$3MM by reducing octane and RVP giveaway by 0.1" | AVEVA PI World 2021[^22^] |
| BP cloud planning speed | 7 hours → 4 minutes per calculation; 2 days → 2 hours per optimization decision | AVEVA/BP case[^21^] |
| LP model accuracy | "approximately 0.50$/BBL improvement in margin"; >$50M/yr for 300 kbpd refinery | IZZI/AVEVA 2022[^32^] |
| LP assurance program (Suncor) | robust LP assurance as "a low-cost way to increase refining margins" | AIMod 2009[^33^] |
| Closed-loop plan-schedule-APC integration | "$0.05 to $0.15/bbl" | ARC Advisory (analyst, independent)[^12^] |
| Refinery-wide RTO (Saudi Aramco Yanbu) | plan-vs-actual gap "up to 10% of the crude margin"; "6% gap reduction in crude margin"; payback 3–6 months | Schneider/AVEVA case[^27^] |
| Dynamic optimization (GDOT-class) | "$4–$10 million annually in middle distillate refining and $6–$10 per ton of ethylene" | PTQ Q4 2025 (Axens)[^31^] |
| AI optimization layer | "10–15% production increases and 4–5% EBITA improvements" (process plants applying AI) | Imubit 2026[^30^] |
| Blend optimization | $0.12/bbl (LUKOIL); ">half of the APC savings of the entire refinery" (ConocoPhillips) | Processing Mag; AFPM[^17^][^16^] |
| Retail fuel price optimization | $83–454/site/week; +0.9–1.9% volume | Kalibrate/SIGMA[^40^][^41^][^42^] |
| Honeywell Business Flex suite | "increase production 3–6%, and decrease costs 2–3%" | Control Engineering[^19^] |
| Mataripe refinery transformation | ">$100 million in validated annualised benefits…"; ">$30M/yr in potential profits via PIMS LP upgrades" | KBC/Digital Refining[^34^] |
| Plan-vs-actual opportunity size | "even well run refineries can have more than $1/Barrel in unaccounted for loss from not meeting the planners forecast" | Refinery Profit Meter[^29^] |

### 5.2 Maturity levels (observed state of practice)

- **Level 0–1 (manual/spreadsheet):** Excel-based scheduling and manual planner→scheduler→console handoffs remain common (ARC: *"Excel spreadsheets are often used to prepare a schedule"*;[^12^] ARC/Kinaxis: industry *"historically relied on customized or semi-customized solutions, often involving numerous spreadsheets and manual processes"*;[^56^] o9's supermajor case replaced Excel).[^58^]
- **Level 2 (tool-enabled, siloed):** LP planning + dedicated scheduling/blending tools, but different models and little integration — *"many refinery planners, schedulers, and optimization engineers work independently using different data models with very little data integration."*[^12^]
- **Level 3 (integrated plan-schedule):** shared plant definition/engine across plan and schedule (AVEVA Spiral; Aspen Unified PIMS→Unified Scheduling model catalogs; shared assays, targets, blend libraries).[^25^][^11^][^7^] Multi-site/multi-period network optimization (§1.2).
- **Level 4 (execution-connected / closed loop):** RTO refinery-wide (Yanbu), GDOT closed-loop plan-schedule-APC with reconciled data and economic drivers,[^31^][^64^] AI optimization layers (Imubit closed loop; Aspen AVA advisor in PIMS).[^30^][^76^][^65^]
- **Level 4 enabler — benchmarking:** Solomon Associates institutionalizes external comparison: *"Margin Gap Analysis compares each refinery to the best worldwide performers (Pacesetters)."*[^67^]

### 5.3 The "plan vs. actual" problem — anatomy

- **Structural cause 1 — period averaging:** the LP sees only opening/closing monthly inventories; *"Just because PIMS found a plan in the model feasible, it does not mean it will be feasible in real life (scheduling) as well"* (arXiv 2605.15085, 2026, with a worked two-unit shutdown example).[^28^]
- **Structural cause 2 — linear/static approximations:** *"LP models assume fixed yields, linear process relationships, and stable conditions across the planning period. In practice, crude quality shifts between cargoes, catalyst activity declines between turnarounds, and market pricing moves hourly. Operators compensate by running conservatively, adding safety cushions…"*[^30^] PTQ (Q4 2025): *"Traditional planning strategies, driven by a monthly LP disconnect from live unit behaviour, will struggle to respond meaningfully… some refiners are already adapting by running their LP weekly, but limitations remain. Yield vectors are static and linear approximations; constraints are averaged or underrepresented. As a result, the gap between 'LP intent' and 'unit execution' remains wide."*[^31^]
- **Structural cause 3 — model decay & maintenance deficit:** *"For known reasons, LP process models become less accurate over time. In typical hectic work environment, significant LP errors can persist for months or even years… Everyone is very busy, and nobody has time!"* Causes: catalyst activity, operating-mode changes, revamps, spec changes, staff rotation/retirement.[^32^] AIMod/Suncor: *"As a refinery's LP prediction errors drift over time, the LP's ability to correctly forecast future operation decreases… refinery Planners often find themselves with limited time to attend to measuring and improving submodel accuracy, with the consequence that over time refinery margins suffer."*[^33^]
- **Structural cause 4 — the gap is usually an accounting artifact, not an operational signal:** *"The Plan vs Actual GAP is a measure of sub-optimality of the refinery operation with respect to the off-line economic optimization of the planner… In most refineries the economic GAP is an accounting measurement not an operational performance measurement."*[^29^] ARC: the gap is *"mainly due to modeling inaccuracy in both planning/scheduling and control models, and mismatches between planning, scheduling, and control constraints and targets."*[^12^]
- **Execution friction:** *"Planning may optimize against one set of assumptions, while actual execution is constrained by crude availability, tankage, product specifications, transportation capacity, or terminal congestion. The gap between planning and execution can erode value even when the underlying optimization logic is sound."*[^60^]

## 6. Tensions & counter-narratives (explicit)

1. **Vendor benefit inflation vs. independent estimates.** AVEVA's "$50–300M/yr per refinery" and "70¢/bbl" figures are marketing claims from vendor decks; the independent analyst figure for closed-loop integration is an order of magnitude smaller ($0.05–0.15/bbl, ARC).[^23^][^22^][^12^] KBC's "$100M validated" is consultancy-validated, not audited.[^34^] Treat all monetized benefits as directional.
2. **"'No comprehensive SCM solution has really existed' for O&G" (ARC, 2025)** — a direct counter-narrative to two decades of vendor "integrated supply chain" positioning; implies maturity claims should be discounted and explains the Kinaxis–ExxonMobil build.[^56^][^57^]
3. **AI/closed-loop vendors talk their book.** Imubit's critique of LP/APC limits is accurate in substance but argues for its own product; LP/APC remain the embedded, trusted stack and AI layers are additive, not replacements (Imubit itself concedes *"AI optimization layers on top of existing infrastructure rather than replacing it"*).[^30^] ERTC 2024 framing: AI's role in refining "remains a topic of debate."[^61^]
4. **LP-derived crude values vs. market practice.** OGJ: *"As a practical matter, product valuations directly based on LP simulations are rarely used in commercial transactions. Instead, a set of boiling-point defined distillation cuts represent the product yields to which corresponding product prices are applied to value the crudes."* — i.e., the LP's marginal economics and deal-making economics diverge.[^50^]
5. **Academic scheduling theory–practice gap.** Survey of crude-scheduling research: *"although progress in research in this field has been made, the techniques obtained are not applicable in the practice… the short-term scheduling job of oil refinery processes is still done manually by planners, because of the lack of such tools."*[^48^] Commercial schedulers (APS/Orion, Spiral) filled the gap with event-based simulation+optimization rather than the MILP/MINLP formulations dominant in academia.[^7^][^47^]
6. **Plan-vs-actual is contested even as a metric.** RPM argues it is usually an accounting measure, not operational;[^29^] AVEVA counters by productizing "Prescriptive Performance (Plan vs. Actual)" feedback;[^24^] Aramco/Shell institutionalize it via back-casting/MVA.[^52^][^51^] The lookback discipline exists but is unevenly formalized — an opportunity for CI knowledge management.
7. **Retail pricing optimization has governance limits.** Kalibrate itself notes optimization is not "one size fits all" — sites lacking competitor data or price variability fall back to rules-based pricing;[^41^] i.e., optimization coverage is partial even in the most mature island.
8. **Data quality undermines everything above.** PETROBRAS' reconciliation experience: *"poor data quality may in general lead to both bad corrective actions and significant deviations between estimated and actual process state, product and feedstock storage and daily KPIs."*[^77^]

---
## EVIDENCE REGISTER (Claim / Source / URL / Date / Excerpt / Context / Confidence)

### A. LP models & multi-site/multi-period planning

**E1 — Claim:** PIMS is the leading refinery LP planning tool for feedstock selection, product slate, plant design and operational execution.
- Source: AspenTech, Aspen PIMS brochure (AT-03906)
- URL: https://www.aspentech.com/-/media/aspentech/home/resources/brochure/pdfs/fy21/q3/at-03906-bro-aspen-pims.pdf
- Date: n.d. (FY21 brochure; accessed 2026-07-18)
- Excerpt: "Aspen PIMS is the most trusted refinery and olefins linear programming (LP) planning software, enabling companies to optimize feedstock selection, product slate, plant design and operational execution… in determining which crudes to process, a refinery must consider at least their price and composition, how they affect the refinery's ever-changing production constraints and the yield and price of each potential product."
- Context: Vendor product literature; defines PIMS' core VCO role (crude selection, slate, run plans).
- Confidence: High (capability claim, corroborated by training curricula [^71^] and job postings [^51^][^53^]).

**E2 — Claim:** RPMS is Honeywell's LP planning system with MIP and multi-period property tracking; PetroChina standardized it across 11 sites.
- Source: Control Engineering, "PetroChina to modernize and optimize refineries"
- URL: https://www.controleng.com/petrochina-to-modernize-and-optimize-refineries/
- Date: original announcement ~2001; page refreshed 2025-04-23
- Excerpt: "The RPMS modeling system includes advanced modeling capabilities that provide mixed integer programming, innovative property tracking techniques for multi-period models, fast recursions and streamlined recursion property calculation techniques. With RPMS, planners can integrate all of the constraints that affect their plan, using data from a variety of sources, to quickly and accurately develop the optimal solution."
- Context: Trade-press report of a Honeywell APS deployment for crude selection, production distribution and plant production at 11 PetroChina sites; evidence of centralized multi-site planning standardization.
- Confidence: High.

**E3 — Claim:** LP planning spans strategic (5+ yr), medium (1–3 yr) and short-term (month–quarter) horizons; solvers use recursive successive LP.
- Source: Popescu, C., "Software Implementation for Optimization of Production Planning within Refineries," Economic Insights – Trends and Challenges 1/2018, Petroleum-Gas University of Ploiești
- URL: http://upg-bulletin-se.ro/old_site/archive/2018-1/1-Popescu.pdf
- Date: 2018
- Excerpt: "The most popular manufacturing optimization software used today by most refineries are RPMS (Honeywell License), PIMS (Aspen License), and GRTMPS (Harperly Systems License), all based on the LP-Linear Programming principles… The RPMS Production Optimization Program is used in the following cases: strategic planning (long term over 5 years); medium-term planning (1-3 years); short-term planning (one month-quarter)… RPMS systems use recursive sequential linear programming(LP)."
- Context: Academic paper documenting RPMS usage patterns, OSL/Xpress-MP solvers, and marginal-revenue objective.
- Confidence: High (academic, method detail).

**E4 — Claim:** AVEVA Spiral/USC is an integrated crude-to-distribution planning/scheduling/optimization suite.
- Source: Aalto University master's thesis (CDU modeling in Spiral)
- URL: https://aaltodoc.aalto.fi/bitstreams/f4b702a3-222f-400f-ac93-d24eb6811d46/download
- Date: n.d. (~2024–25; accessed 2026-07-18)
- Excerpt: "AVEVA Unified Supply Chain (previously called Spiral) is an integrated refinery planning, scheduling, and optimization tool designed to enhance decision-making in the oil and gas industry. It provides refineries with a comprehensive suite of applications for managing crude selection, production planning, operational scheduling, and supply chain logistics."
- Context: Independent academic description of the AVEVA stack; also documents distillation modeling from mass-balance data.
- Confidence: High.

**E5 — Claim:** AVEVA Network extends plant LP planning to full supply & distribution network optimization.
- Source: AVEVA, "AVEVA Unified Supply Chain – Network" product page
- URL: https://www.aveva.com/en/products/network/
- Date: 2026-05-07 (page date; accessed 2026-07-18)
- Excerpt: "Supply and distribution network optimization with unified integrated analytics - Includes full plant models when combined with Plan… Refining Process Value Chain Optimization: Optimizing business value through increased yield and reduced energy requires a focus on anticipating, guiding, and negotiating performance alignment across all refinery facilities and organizations."
- Context: Vendor spec; evidence of network-level extension and AVEVA's explicit "Refining Process Value Chain Optimization" scenario naming.
- Confidence: High (capability), Medium (benefit implications).

**E6 — Claim:** Galp optimizes its downstream network (refineries–depots–1,200 stations) with a GRTMPS model fed by Platts/Argus quotes.
- Source: Extended abstract (Galp downstream logistics), Instituto Superior Técnico, Lisbon
- URL: https://fenix.tecnico.ulisboa.pt/downloadFile/1126295043838690/ExtendedAbstract_AL.pdf
- Date: n.d. (~2015; accessed 2026-07-18)
- Excerpt: "Currently, this downstream planning is accomplished through an optimisation model developed through GRTMPS software… it considers numerous inputs such as several international quotations (e.g. from Platts and Argus), distances between network facilities (refineries, depots and service stations) or demand across the network… It provides the optimal connections between refineries, depots and service stations."
- Context: Academic case documentation; the model is non-linear due to biofuel blending mandates.
- Confidence: High.

**E7 — Claim:** Aspen PIMS-AO / Unified Multi-site optimizes multi-plant value chains (product locations, feedstock sourcing, freight, inventory); solver ~8x faster.
- Source: AspenTech aspenONE V8.7 press release; ARC Advisory on Aspen Unified V12
- URL: https://www.aspentech.com/en/resources/press-releases/aspenonert-v8-7-software-release-sets-new-benchmark-for-manufacturing-and-supply-chai2147491452 ; https://www.arcweb.com/industry-best-practices/aspentechs-unified-solution-helps-users-move-toward-self-optimizing-plant
- Date: 2014-09-02; n.d. (~2023)
- Excerpt: "Aspen PIMS-AO software delivers on the latest advancements in optimization, including parallel processing, enhanced global optimization, feedstock basket reduction, and nonlinear modeling… at least 8 times faster" (OMV: "our results and potential profits are significantly higher") / "Aspen Unified Multi-site for PIMS optimizes the value chain to reduce cost and increase margin by selecting optimal product locations and feedstock sourcing, freight, and inventory usage."
- Context: Vendor release with named customer quote (OMV); independent analyst description of multi-site capability.
- Confidence: High (capabilities), Medium (speed/profit uplift).

**E8 — Claim:** LP use for refinery planning is near-universal since the 1990s.
- Source: AFPM AM-93-65, Larry Haverly (Haverly Systems), "Integration of Refinery Scheduling with Planning"
- URL: https://www2.afpm.org/forms/store/ProductFormPublic/am-93-65-integration-of-refinery-scheduling-with-planning
- Date: 1993 (store page accessed 2026-07-18)
- Excerpt: "Planning has gone from being 'back-of-the-envelope hand calculations' to the use of computers with optimization calculations to provide accurate, timely information on which to base decisions. The vast majority of refineries all over the world now use LP for planning."
- Context: Conference paper abstract by GRTMPS' creator; historical anchor for LP ubiquity.
- Confidence: High.

**E9 — Claim:** The LP objective is GRM maximization; a persistent LP-vs-actual gap is documented in academic literature.
- Source: American Journal of Scientific Research (scialert), "Optimal Design of Petroleum Refinery Topology…"
- URL: https://scialert.net/fulltext/?doi=ajsr.2011.95.113
- Date: 2011-02-26
- Excerpt: "The use of Linear Programming (LP) tools for both long-term planning and day to day scheduling is fairly common in any refinery; still there is a gap between the LP run results and the actual operations… The LP tool is an optimizer whose objective function is the GRM (Gross Refining Margin) of the refinery."
- Context: Peer-reviewed; also notes PIMS' successive-LP basis and MINLP needs for detailed scheduling.
- Confidence: High.

### B. Scheduling, blending, S&OP/IBP

**E10 — Claim:** Aspen Petroleum Scheduler is the dominant refinery scheduling tool; it exists to close plan-execution gap.
- Source: AspenTech, Aspen Petroleum Scheduler brochure (11-9079)
- URL: https://www.aspentech.com/-/media/aspentech/home/resources/brochure/pdfs/fy17/q4/11-9079-bro-aspen-petroleum-scheduler.pdf
- Date: n.d. (FY17; accessed 2026-07-18)
- Excerpt: "Since 1995, Aspen Petroleum Scheduler has provided a critical link between the refinery planning process and operations, helping customers across the globe achieve better operational alignment with the plan, which helps to prevent margin leakage in a volatile, competitive market… an event-based, single-blend optimization solution that supports the scheduling of all refinery activities for over 45% of global refineries."
- Context: Vendor brochure; also lists dock/pipeline scheduling and benefits (demurrage, quality giveaway, inventories).
- Confidence: High (adoption claim is broadly corroborated: "more than 250 refineries" per Microsoft Azure listing [^8^]; "over 200 refineries" per Hydrocarbon Engineering [^78^]).

**E11 — Claim:** AVEVA Spiral Schedule shares one engine with Plan and productizes plan-vs-schedule-vs-actual comparison.
- Source: AVEVA, Spiral Unified Supply Chain Management: Schedule datasheet
- URL: https://www.aveva.com/content/dam/aveva/documents/datasheets/Datasheet_SpiralUnifiedSupplyChainManagementSchedule_EN.pdf
- Date: n.d. (accessed 2026-07-18)
- Excerpt: "Sharing the same plant definition and mathematical engine as Spiral… Plan ensures consistency between different user groups… Integration with plant data via the Spiral… Staging Server allows quick reconciliation of the schedule to understand differences between schedule vs. actual, and highlights issues with both modeling and execution."
- Context: Vendor datasheet; direct evidence of "compare plan, schedule and actual" workflow.
- Confidence: High.

**E12 — Claim:** The traditional (low-maturity) workflow is offline LP + Excel schedules + manual handoff to console.
- Source: ARC Advisory Group, "AspenTech's Unified Solution Helps Users Move Toward the Self-optimizing Plant"
- URL: https://www.arcweb.com/industry-best-practices/aspentechs-unified-solution-helps-users-move-toward-self-optimizing-plant
- Date: n.d. (~2023, V12 era; accessed 2026-07-18)
- Excerpt: "Today, many refinery planners, schedulers, and optimization engineers work independently using different data models with very little data integration… Excel spreadsheets are often used to prepare a schedule. The scheduler will then manually pass along these spreadsheets with the operating targets to the unit control operator… there's a gap between plan vs. actual, often leaving significant money on the table. This gap is mainly due to modeling inaccuracy in both planning/scheduling and control models, and mismatches between planning, scheduling, and control constraints and targets."
- Context: Independent analyst; best single description of the plan-vs-actual mechanism and baseline maturity.
- Confidence: High.

**E13 — Claim:** Multi-period, multi-blend optimization is state of practice; Chevron rolled Aspen MBO out to 8 refineries with formal change management.
- Source: AFPM Plant Automation session descriptions (ConocoPhillips Wood River; Chevron/Aspen)
- URL: https://www2.afpm.org/forms/uploadFiles/24750000006EB.filename.PlantAutomationSessionDescriptions.pdf
- Date: n.d. (~2007; accessed 2026-07-18)
- Excerpt: "The tool used, Aspen MBO, is an event-based, multi-period and multi-blend solution that generates optimal blending schedules for both short- and long-term campaigns… It describes the successful deployment of Aspen MBO at eight Chevron refineries… the project timeline, the organizational structure and the change management process associated with a rollout of such scope." / "Optimal Gasoline Blending contributes more than half of the APC savings of the entire refinery."
- Context: AFPM (then NPRA) conference paper abstracts; evidence of enterprise rollout practice and blending value.
- Confidence: High.

**E14 — Claim:** Honeywell's BLEND/BMA suite covers multi-period blend optimization through in-line control; installed at sites representing >25% of world refining capacity.
- Source: Honeywell Forge, "Honeywell Blending and Movement"; Digital Refining BMA R400.1 news
- URL: https://www.honeywellforge.ai/us/en/products/industrial-operations/honeywell-blending-movement ; https://www.digitalrefining.com/news/1001074/honeywells-advanced-solutions-to-optimize-material-movement-and-blending-operations
- Date: n.d.; n.d. (~2012) (accessed 2026-07-18)
- Excerpt: "BLEND is multi-period, multi-blend optimization software for petroleum products. Using state-of-the-art technology, BLEND produces the optimum blending recipes for each batch." / "With applications installed at hundreds of sites globally, representing over 25 percent of the world's refining capacity, Honeywell is the leader in off-sites management."
- Context: Vendor claims; breadth of the blending/movement automation layer (BRC→BPC→BLEND).
- Confidence: Medium-High (capability High; market-share claim vendor-only).

**E15 — Claim:** LUKOIL's Honeywell Profit Blend Optimizer delivered ~$0.12/bbl and plan adherence.
- Source: Processing Magazine, "Making the best of blending through optimization" (Anosov, Kuvykin, Logunov)
- URL: https://www.processingmagazine.com/mixing-blending-size-reduction/article/15587076/making-the-best-of-blending-through-optimization
- Date: 2017-06-01
- Excerpt: "Overall, the optimization at LUKOIL-Nizhegorodnefteorgsintez's is estimated to have added profits equivalent to $0.12/barrel… eliminating giveaway and improving the reliability of blending enables operators to consistently keep to the refinery plan and drive overall optimization."
- Context: Practitioner-authored case (Honeywell APS team leader + refinery optimization head); continuous rundown blending without intermediate tanks.
- Confidence: Medium-High (named refinery, practitioner authors; figure is "estimated").

**E16 — Claim:** Blending automation maturity ladder: RBC → ABC → off-line optimization & planning (OOPS).
- Source: OMS eLearning Academy, "Advanced Closed-Loop Controls of Refinery Offsite Operations"
- URL: https://www.oms-elearning-academy.com/advanced-closed-loop-controls-of-refinery-offsite-operations/
- Date: 2026-01-28 (page date)
- Excerpt: "Three levels of blending control strategy have evolved over the last 15 years in the refining business… Regulatory Blend Control (RBC)… Advanced Blend Control (ABC)… Off-line Optimization and Planning System (OOPS): the off-line optimization of a blend recipe taking into account the refining process as expected in advance… by a refinery planner and then he downloads the optimized recipe to the online blend control (ABC) system."
- Context: Training academy describing industry-standard blending control hierarchy; useful as a maturity model.
- Confidence: Medium (secondary training source; consistent with vendor architectures [^14^][^69^]).

**E17 — Claim:** SAP IBP is positioned for O&G S&OP: unified sales/operations/finance plans, refinery optimization and depot inventory use cases.
- Source: Isaac Manuel (SAP expert), "SAP IBP for Oil & Gas Producers" course description
- URL: https://isaacmanuel.org/courses/sap-ibp-for-oil-gas-producers/
- Date: 2025-09-30
- Excerpt: "Integrating sales, operations, and finance plans into one unified process… Applying IBP's core modules — S&OP, Demand, Supply, and Inventory — to real industry use cases such as demand forecasting, refinery optimization, and depot inventory management… Oil & Gas companies can shorten planning cycles, reduce costs, improve forecast accuracy, and accelerate cash flow."
- Context: Practitioner training description of SAP IBP's O&G positioning (secondary but specific).
- Confidence: Medium.

**E18 — Claim:** SAP's downstream execution backbone (IS-Oil/S4): TSW nominations/shipments; SDR secondary distribution to retail.
- Source: LeverX, "SAP IS-Oil Modules: Downstream vs. Upstream Logistics Optimization"; SAP Community downstream overview
- URL: https://leverx.com/newsroom/sap-is-oil-modules ; https://community.sap.com/t5/sap-for-oil-gas-and-energy-blog-posts/downstream-industry-process-overview-amp-sap-solutions/ba-p/13148956
- Date: 2026-03-19; 2015-04-30
- Excerpt: "One example is the Trader's and Scheduler's Workbench (TSW). This component records pipeline nominations, plans shipments between facilities, and tracks deliveries across transport modes… Secondary Distribution and Replenishment (SDR). The system creates delivery schedules for tanker trucks, gathers sales information from fuel pumps, and keeps track of fuel inventory at retail locations."
- Context: Documents the transaction/execution layer beneath planning; TSW–IBP integration exists for demand planning.
- Confidence: High.

**E19 — Claim:** Kinaxis + ExxonMobil are co-building a purpose-built O&G concurrent planning solution; O&G historically relied on spreadsheets/custom tools.
- Source: ARC Advisory, "ExxonMobil and Kinaxis: Creating a Next Gen Supply Chain Management Solution for Oil & Gas"; TankTerminals/AJOT announcement
- URL: https://www.arcweb.com/industry-best-practices/exxonmobil-kinaxis-creating-next-gen-supply-chain-management-solution-oil ; https://tankterminals.com/news/exxonmobil-kinaxis-team-up-to-revolutionize-supply-chain-efficiency-for-the-energy-sector/
- Date: 2025-09-01; 2024-10-16
- Excerpt: "Despite this complexity… it would seem no comprehensive supply chain management solution has really existed to help the oil and gas industry… achieve a unified view of their supply chain… Due to the complexity and scarcity of available solutions, such as advanced planning systems, the oil and gas industry has historically relied on customized or semi-customized solutions, often involving numerous spreadsheets and manual processes."
- Context: Independent analyst; major counter-narrative to vendor "integrated suite" claims.
- Confidence: High.

**E20 — Claim:** ExxonMobil consolidated supply chain under one president with end-to-end planning + analytics ("DNA").
- Source: Supply Chain Strategy (interview with Kinaxis/ExxonMobil), "Kinaxis and ExxonMobil: Revolutionising supply chain management"
- URL: https://supplychainstrategy.media/blog/2025/03/18/kinaxis-and-exxonmobil-revolutionising-supply-chain-management/
- Date: 2025-03-19
- Excerpt: "we are organised to have supply chain end-to-end planning, which I actually own. We have logistics excellence, we have materials management, and we have the digital network and advanced analytics, which we call our DNA… we're under one supply chain president who reports to our management committee."
- Context: Named-executive interview; strongest primary evidence of a unified "supply chain" org model at an oil major.
- Confidence: High.

### C. Demand forecasting, retail pricing, ETRM/CTRM

**E21 — Claim:** ML now beats econometric baselines for refined-product demand forecasting; <10% MAPE at 12-month horizon.
- Source: Oxford Institute for Energy Studies, "Forecasting Global Oil Demand: Application of Machine Learning Techniques" (Aldabbagh, Economou, Christou)
- URL: https://www.oxfordenergy.org/wpcms/wp-content/uploads/2025/02/OIES-Paper-Forecasting-Global-Oil-Demand-Application-of-ML-Techniques-November-2024.pdf
- Date: November 2024
- Excerpt: "By achieving a Mean Absolute Percentage Error (MAPE) of less than 10% on average for monthly short-term forecasts extending one year out-of-sample, our methodology balances complexity (top down vs. bottom up) and accuracy in oil demand forecasting… By backcasting and utilizing Prophet, we maximized the number of observations in our training set."
- Context: Academic/research-institute paper; seven products × seven regions; also a backcasting usage in the forecasting literature.
- Confidence: High.

**E22 — Claim:** Retail fuel price optimization is AI/elasticity-based, rules-governed, deployed at massive scale with quantified per-site benefits.
- Source: Kalibrate Fuel Pricing page; Kalibrate product page; SIGMA State of the Industry profile
- URL: https://kalibrate.com/kalibrate-fuel-pricing-software/ ; https://kalibrate.com/products/software/kalibrate-pricing/ ; https://www.sigma.org/wp-content/uploads/2024/04/SRG_SIGMA_APRIL2024_WEB.pdf
- Date: 2026-07-10; 2025-11-19; April 2024
- Excerpt: "Kalibrate's patented AI recommends optimal fuel prices that balance volume and margin… Based on demand signals, price elasticity, and market shifts across your sites and network." / "600,000 prices a day to over 65,000 sites… Auto implementation 80/20 — automating 80% of fuel price decisions." / "Kalibrate helps fuel retailers sell 1.4% more volume and increase gross profit by an average of $454 per site, per week."
- Context: Vendor + trade-association profile; note vendor caveat that optimization doesn't fit every site (rules fallback).
- Confidence: Medium (vendor-reported benefits; scale claims plausible given market position).

**E23 — Claim:** ETRM platforms (Endur-class) run front-to-back physical+financial oil/products trading with real-time risk and logistics integration.
- Source: 6B Energy, "Openlink Endur Integration"; DevOpsSchool ETRM comparison
- URL: https://6b.energy/services/interoperability-and-integration/energy-trading-and-risk-management-etrm-system-integration/openlink-endur-integration/ ; https://www.devopsschool.com/blog/top-10-energy-trading-risk-management-etrm-features-pros-cons-comparison/
- Date: 2025-12-01; 2026-06-19
- Excerpt: "Endur supports deal capture, market connectivity, price curves, scheduling, risk modelling, hedging strategies, P&L reporting, settlements, regulatory reporting, and financial integration… modular architecture supports complex trading portfolios, operational logistics, and enterprise-wide risk management."
- Context: Integration consultancy documentation; describes ETRM scope relevant to the trading leg of VCO.
- Confidence: Medium-High.

**E24 — Claim:** Hedging/price-risk costs belong inside refinery supply-chain planning economics.
- Source: Stadtler & Kilger (eds.), "Supply Chain Management and Advanced Planning" (5th ed.), ch. 24 (oil industry case)
- URL: https://www.cur.ac.rw/mis/main/library/documents/book_file/2015_Book_SupplyChainManagementAndAdvanc.pdf
- Date: 2015
- Excerpt: "A price risk exists, if there is a difference between planned inventories of crude oil and inventories of finished products. These price risks have to be secured on the market and these hedging costs or working capital costs have to be taken in the planning system as an element of costs. Thus, the overall objective is maximizing revenues minus all variable supply chain costs."
- Context: Standard SCM textbook treatment of oil-industry planning; also stresses crude purchase as "the most important financial decision" and demand-forecast criticality.
- Confidence: High.

### D. VCO span, roles, and organizational models

**E25 — Claim:** AVEVA's VCO framework explicitly spans strategic→real-time→lookback layers, including "Prescriptive Performance (Plan vs. Actual)" and "Planning Model Tracking/Update."
- Source: AVEVA, "Value Chain Optimization Roadmap and Vision" (David Bleackley), AVEVA World San Francisco
- URL: https://cdn.mediavalet.com/eunl/content/2HRllLF2YUCH2U0W3jeWcA/tGlwu41StECXatFdq3T4iQ/Original/Production%20Optimization%20for%20Continuous%20Processes%20Roadmap%20%26%20Vision.pdf
- Date: November 2022
- Excerpt: "After Operation: Operations Analytics, Production Accounting, Planning Model Tracking/ Update, Prescriptive Performance (Plan vs. Actual)… 1 to 15 days: Operation Targets, Scheduling, Logistics, Daily Scheduling… 1 year: Fiscal Targets, Strategic Decisions, Long Term Business Planning, Corporate Planning, Investment Planning… Enterprise Crude Knowledge Management, Digital Workflows across tool boundaries, AI & Machine Learning for Enhanced Decision Support."
- Context: Vendor roadmap deck; the clearest single artifact of what vendors mean by end-to-end VCO, including the after-the-fact lookback layer.
- Confidence: High (as vendor intent/framework).

**E26 — Claim:** VCO must reconcile conflicting targets across crude trading, scheduling, logistics, planning, operations.
- Source: AVEVA (Katarzyna Juda), "Applying Artificial Intelligence to Scheduling," AVEVA World San Francisco
- URL: https://cdn.osisoft.com/osi/presentations/2022-AVEVA-San-Francisco/UC22NA-03PS30-AVEVA-Juda-AVEVA-Schedule-AI-Assistant-Applying-Artificial-Intelligence-To-Scheduling.pdf
- Date: November 2022
- Excerpt: "Effective economic optimization of hydrocarbon value chain can boost profitability by $50 to 300 million per year for a typical oil refinery… Conflicting Targets Across the Value Chain: CRUDE TRADER… REFINERY SCHEDULER — Accuracy: are there margin leaks in plan v/s schedule v/s actual?… LOGISTICS PLANNER… PRODUCTION PLANNER — Real capability: is my planning model accurate?… OPERATIONS MANAGER…"
- Context: Vendor deck; dual evidence: (i) headline benefit claim, (ii) role-by-role target conflicts that org design must manage.
- Confidence: High for role conflicts; Low-Medium for the $50–300M benefit claim.

**E27 — Claim:** Shell institutionalizes LP-model custodianship, Margin Variance Analysis and post-mortems at site level.
- Source: Shell plc job posting, "Economics Model Coordinator" (Selangor, Malaysia), via Built In
- URL: https://builtin.com/job/tech-specialist-mo-emc/3363360
- Date: 2024-11-13
- Excerpt: "Serve as the custodian of the planning/PIMS/LP model… Assist in LP (PIMS) runs to assess site actual performance vs planned performance using the Margin Variance Analysis (MVA) process… Support to economists in LP analysis, in particular develop/adopt techniques for post-mortem analysis and robust crude cargo analysis… Update planning and scheduling models with crude oil assay data consistent with information used by Trading for pricing."
- Context: Primary evidence of day-to-day VCO roles: LP custodian, basic-data ownership, trading-aligned crude intelligence, plan-vs-actual MVA.
- Confidence: High.

**E28 — Claim:** Saudi Aramco runs central "hydrocarbon system" LP modeling with monthly back-casting reports.
- Source: Saudi Aramco Careers, "Linear Programming (LP) Modeling Engineer" job details
- URL: https://careers.aramco.com/expat_uk/job/Linear-Programming-%28LP%29-Modeling-Engineer/857096723/
- Date: n.d. (accessed 2026-07-18)
- Excerpt: "Run the oil & gas and refinery linear programing models to generate the Business Plan level of operations for the Hydrocarbon system… Perform 'back-casting' and issue a monthly report on the LP gap along with required mitigations… ensure that short range operating plans are aligned with the long term plans in terms of modeling accuracy."
- Context: Primary evidence that backcasting is a named, recurring corporate process with formal reporting — directly relevant to the study's lookback/backcasting theme.
- Confidence: High.

**E29 — Claim:** Valero's org chart concentrates crude supply, trading, planning & economics, and systems optimization in commercial leadership.
- Source: Zippia, Valero Energy executives (career histories of Lane Riggs, Gary Simmons)
- URL: https://www.zippia.com/valero-energy-careers-12276/executives/
- Date: 2022-11-18
- Excerpt: "Director-Supply & Optimization, Vice President-Refinery Planning & Economics, and Senior Vice President-Crude, Feedstock Supply & Trading… Simmons directs the supply, trading and hedging activities for supply of crude oil to all Valero refineries, and oversees international operations and refinery systems optimization."
- Context: Secondary aggregator of company bios; consistent with independent-refiner central supply/trading model.
- Confidence: Medium-High.

**E30 — Claim:** ANCAP (Uruguay) combines RPMS planning with in-house scheduling simulators and links both to commercial pricing decisions.
- Source: Universidad de la República (Uruguay) thesis, "Scheduling problems… Decision-making process in ANCAP"
- URL: https://www.colibri.udelar.edu.uy/jspui/bitstream/20.500.12008/53769/1/Zim25.pdf
- Date: n.d. (~2024; accessed 2026-07-18)
- Excerpt: "Planning tools have been used at ANCAP for the past thirty years. The production planning model is implemented using the commercial software Refinery and Petrochemical Modeling System (RPMS) by Honeywell… applied in short, medium, and long-term studies to evaluate crude oil purchases, crude oil and product contracts, production plans, and investment decisions… Results from both planning and scheduling models support pricing decisions for products between the production and commercial areas."
- Context: Academic thesis; shows 30-year planning-tool continuity and the plan→commercial interface at a national oil company.
- Confidence: High.

### E. Benefits, maturity, plan-vs-actual, backcasting

**E31 — Claim:** ExxonMobil's AVEVA cloud planning cut model runs from 7+ hours to <4 minutes and improved profitability by 70¢/bbl.
- Source: AVEVA PI World 2021 presentation (Harpreet Gulati), "Enable Enterprise Agility & Sustainability"
- URL: https://cdn.osisoft.com/osi/presentations/2021-aveva-pi-world/UC21NA-D1OP040-AVEVA-Gulati-Enable-Enterprise-Agilty-Sustainability.pdf
- Date: 2021
- Excerpt: "Value Chain Optimization — Reduced time from 7+ hrs. to <4 mins per planning model. Improved profitability by 70c/bbl. Enabled by: Cloud powered AVEVA Unified Supply Chain." Also: "Rapid Reaction to Market Volatility — $60-100MM in benefits per model run; $1 Billion in cumulative benefits over 3 years."
- Context: Vendor customer-outcome deck (ExxonMobil named). Same deck: "$750MM/yr" process-optimization program benefits; "$7MM/yr RBOB + $3MM octane/RVP giveaway savings across seven sites."
- Confidence: Medium (vendor-reported, customer-named, not independently audited).

**E32 — Claim:** BP unified supply & distribution optimization in one cloud model; 7 hours→4 minutes; 2 days→2 hours; traders make better crude purchase decisions.
- Source: AVEVA customer case study, "bp sets up commercial CO2 emission modeling for refinery operations using AVEVA supply chain optimization"
- URL: https://www.aveva.com/content/dam/aveva/documents/perspectives/success-stories/SuccessStory_BP.pdf.coredownload.inline.pdf
- Date: n.d. (~2021–22; accessed 2026-07-18)
- Excerpt: "AVEVA Unified Supply Chain optimizes the entire value chain in one model… The time benefits are dramatic too — individual calculation times have fallen from seven hours to four minutes, while optimization decisions that used to take two days now take two hours. This enables bp's trading teams to make more informed risk-based crude purchase decisions."
- Context: Vendor case study; also evidence of sustainability (commercial CO2 modeling) entering the planning model scope.
- Confidence: Medium-High (named customer, plausible mechanism; figures vendor-reported).

**E33 — Claim:** Saudi Aramco Yanbu quantified the plan-vs-actual gap at up to 10% of crude margin and closed 6% via refinery-wide RTO; payback 3–6 months.
- Source: Schneider Electric/AVEVA case (Saudi Aramco Yanbu), via MAVESZ conference PDF
- URL: https://mavesz.hu/wp-content/uploads/14_25_MAVESZ-Juhasz-Marton-Schneider-AVEVA-Kollaboracio.pdf
- Date: n.d. (~2019; accessed 2026-07-18)
- Excerpt: "Optimize operations by closing the 'plan vs actual' performance gap… Close the 'plan vs actual' performance gap caused by the technology gap, which can amount up to 10% of the crude margin… First refinery-wide real-time optimization (RTO) in the Middle East… Project payback estimated between 3-6 months, with early results showing quick progress: 6% gap reduction in crude margin."
- Context: Operator case study with named Aramco quote; misalignment between planning, scheduling and APC objectives cited as root cause.
- Confidence: Medium-High (operator-authored, conference-presented).

**E34 — Claim:** LP model inaccuracy alone costs ~$0.50/bbl; errors persist for months/years due to workload and expertise loss.
- Source: IZZI Business Services (Anwar Tatariya), "LP Accuracy – Best Practices," AVEVA PI World San Francisco
- URL: https://cdn.osisoft.com/osi/presentations/2022-AVEVA-San-Francisco/UC22NA-03PS20-IZZI-Tatariya-LP-accuracy-Best-Practices.pdf
- Date: November 2022
- Excerpt: "For known reasons, LP process models become less accurate over time. In typical hectic work environment, significant LP errors can persist for months or even years… Typical refiner with multi-crude processing should expect to see approximately 0.50$/BBL improvement in margin… A midrange value of 0.50 US$/BBL for a 300 thousand bpd refinery results in a savings of over 50 million dollars a year."
- Context: Practitioner (22 yrs refining planning, ex-industry) at vendor conference; accuracy ranges by crude-switch severity ($0.10–1.00/bbl).
- Confidence: Medium (practitioner estimate; mechanism well corroborated by [^33^]).

**E35 — Claim:** Suncor treats LP assurance (systematic submodel tuning vs. actuals) as a low-cost margin lever.
- Source: AIMod, "A Better Way To Keep Your LP Accurate" (Suncor project paper)
- URL: http://aimod.com/papers/A%20Better%20Way%20to%20Keep%20Your%20LP%20Accurate.pdf
- Date: 2009-08-25
- Excerpt: "As a refinery's LP prediction errors drift over time, the LP's ability to correctly forecast future operation decreases… The refinery runs against wrong constraints; Sub-optimal crude selection… Make too much product- then sell excess at a loss… Suncor Energy sees a robust LP Assurance solution as a low-cost way to increase refining margins."
- Context: Consultancy project paper; lists drift causes (equipment issues, feed shifts, staffing rotation) and consequences — direct support for backcasting/LP-audit processes.
- Confidence: Medium-High.

**E36 — Claim:** PTQ documents that even weekly LP reruns leave a wide "LP intent vs unit execution" gap; GDOT-class closed loop worth $4–10M/yr.
- Source: PTQ Q4 2025 (Axens article on dynamic optimisation)
- URL: https://ptqmagazines.digitalrefining.com/PTQ-Q4-2025
- Date: Q4 2025
- Excerpt: "Traditional planning strategies, driven by a monthly LP disconnect from live unit behaviour, will struggle to respond meaningfully. In an increasingly volatile oil environment, some refiners are already adapting by running their LP weekly, but limitations remain. Yield vectors are static and linear approximations; constraints are averaged or underrepresented. As a result, the gap between 'LP intent' and 'unit execution' remains wide… implementations of GDOT have shown measurable financial benefits, including margin improvements of $4-$10 million annually in middle distillate refining."
- Context: Leading refining trade journal; vendor-authored but peer-reviewed by PTQ editors.
- Confidence: Medium-High.

**E37 — Claim:** Imubit: planned vs actual refinery margin rarely match because LP assumes linearity, updates on planning cycles, and no cross-layer coordination exists in the traditional stack.
- Source: Imubit, "Oil Refinery Optimization: How AI Builds on What LP Models Leave Behind"
- URL: https://imubit.com/articles/oil-refinery-roi-optimization
- Date: 2026-04-15
- Excerpt: "LP models assume linear relationships and update on planning cycles, not operating cycles. APC systems optimize individual units without visibility into plant-wide economics. Nothing in the traditional stack coordinates across layers against current market conditions… Industrial processing plants that have applied AI have reported 10–15% production increases and 4–5% EBITA improvements."
- Context: AI vendor perspective — structurally accurate critique, self-serving remedy; cites industry AI-impact stats.
- Confidence: Medium.

**E38 — Claim:** arXiv 2026: monthly-period LP cannot see intra-month inventory feasibility — plan feasible ≠ schedule feasible.
- Source: arXiv:2605.15085, "From Data to Action: Accelerating Refinery Optimization with AI"
- URL: https://arxiv.org/html/2605.15085v1
- Date: 2026-05-14
- Excerpt: "In refinery optimization, monthly plans are being created, which means one month is one period… PIMS only sees the beginning and end point of the month… Just because PIMS found a plan in the model feasible, it does not mean it will be feasible in real life (scheduling) as well."
- Context: Recent preprint with worked tank-inventory example of the planning/scheduling feasibility gap; also stresses need for operational viability checks of LP outputs.
- Confidence: Medium-High (preprint, not peer-reviewed; mechanism consistent with ARC [^12^]).

**E39 — Claim:** Even well-run refineries lose >$1/bbl to plan-vs-actual; the GAP is usually an accounting, not operational, measure.
- Source: Manutec, "Real-time Refinery Optimization through Opportunity Cost Visualization" (Refinery Profit Meter)
- URL: https://www.manutechnet.com/index.php?page=our-partners
- Date: n.d. (accessed 2026-07-18)
- Excerpt: "After accounting for unexpected operational problems even well run refineries can have more than $1/Barrel in unaccounted for loss from not meeting the planners forecast. The Plan vs Actual GAP is a measure of sub-optimality of the refinery operation with respect to the off-line economic optimization of the planner… In most refineries the economic GAP is an accounting measurement not an operational performance measurement."
- Context: Vendor concept note; useful for the distinction between accounting and operational gap measurement; forecasts month-end Actual vs Plan in real time.
- Confidence: Medium.

**E40 — Claim:** KBC's Mataripe (Acelen) transformation: >$100M validated annualized benefits; >$30M/yr from PIMS LP upgrades; backcasting tools improved crude selection and LP alignment.
- Source: KBC whitepaper / Digital Refining, "Transforming LATAM's refineries: profit, performance, and decarbonisation"
- URL: https://www.kbc.global/uploads/files/whitepapers/Transforming_Latin_Americas_Refineries_Profit_Performance_Decarbonization.pdf ; https://www.digitalrefining.com/article/1003335/transforming-latams-refineries-profit-performance-and-decarbonisation
- Date: n.d. (~2024–25; accessed 2026-07-18)
- Excerpt: "More than $100 million in validated annualised benefits across process, energy, reliability, and supply chain performance… More than $30M/yr in potential profits via PIMS LP upgrades… Advanced planning and backcasting tools improved crude selection and operational alignment with the LP."
- Context: Consultancy case study; explicitly names "backcasting tools" as part of the transformation — key lookback-discipline evidence.
- Confidence: Medium (consultancy-validated, not audited).

**E41 — Claim:** Backcasting/auditing/model validation is a sold consultancy service line for LP model maintenance.
- Source: Refining Advantage (Rany), Products/Services page
- URL: https://www.refiningadvantage.com/products
- Date: n.d. (accessed 2026-07-18)
- Excerpt: "Model maintenance includes Backcasting, Auditing, and Unit Model Validation… An Auto-Scheduling & Optimization solution can be developed and integrated with your current Refinery Scheduling tools to automate routine scheduling tasks."
- Context: Specialist consultancy (ex-refinery planners) servicing PIMS/APS/MBO, GRTMPS, RPMS, PETRO models; confirms backcasting as professional practice.
- Confidence: High (service existence), n/a for outcomes.

**E42 — Claim:** Solomon Associates' Margin Gap Analysis benchmarks each refinery against worldwide "pacesetters."
- Source: Solomon Associates, AIChE Fuels & Petrochemicals 2017 presentation
- URL: https://www.aiche.org/sites/default/files/community/aichecommunitysite/423541/solomonpresentationaichefuelspetrochemicals2017final.pdf
- Date: 2017
- Excerpt: "Margin Gap Analysis compares each refinery to the best worldwide performers (Pacesetters)."
- Context: Benchmarking methodology presentation; external lookback/benchmark practice distinct from internal backcasting.
- Confidence: High.

**E43 — Claim:** Academic scheduling research (MILP/MINLP) remains largely unapplied in refinery practice.
- Source: ResearchGate compilation (Xu & Chen et al.), including Wu et al. review statement; Shah (1996) crude scheduling
- URL: https://www.researchgate.net/publication/318805226_Energy_Efficiency_Optimization_in_Scheduling_Crude_Operations_of_Refinery_Based_on_Linear_Programming
- Date: accessed 2025-08-09 (underlying works 1996–2017)
- Excerpt: "It is a great challenge to find efficient tools for short-term scheduling of oil refinery processes. Although some, theoretical advancement has been made in this field, a gap between theory and applications exists. In practice, the short-term scheduling job of oil refinery processes is still done manually by planners, because of the lack of such tools."
- Context: Literature compilation; counter-narrative to academic optimization claims; commercial tools filled the practical gap differently.
- Confidence: Medium-High.

**E44 — Claim:** OGJ: LP-derived product values are rarely used in actual crude transactions.
- Source: Oil & Gas Journal, "Gravity and sulfur-based crude valuations more accurate than believed"
- URL: https://www.ogj.com/home/article/17230143/gravity-and-sulfur-based-crude-valuations-more-accurate-than-believed
- Date: n.d. (accessed 2026-07-18)
- Excerpt: "Linear-program (LP) models of individual refineries are routinely used to determine the relative use values among crudes… As a practical matter, product valuations directly based on LP simulations are rarely used in commercial transactions. Instead, a set of boiling-point defined distillation cuts represent the product yields to which corresponding product prices are applied to value the crudes."
- Context: Trade-press technical article; tension between planning-model economics and market deal practice.
- Confidence: Medium-High.

**E45 — Claim:** GFM Review: a margin-optimized plan only creates value if the supply chain can execute it; mature operators are unifying crude slate, scheduling, blending, inventory and distribution decisions.
- Source: GFM Review, "Upstream, Midstream, Downstream, LNG, And Petrochemical Supply Chain Networks"
- URL: https://www.gfmreview.com/commodities/upstream-midstream-downstream-lng-and-petrochemical-supply-chain-networks
- Date: 2026-07-04
- Excerpt: "A margin-optimized refinery plan only creates value if the supply chain can execute it… Planning may optimize against one set of assumptions, while actual execution is constrained by crude availability, tankage, product specifications, transportation capacity, or terminal congestion… The more mature downstream operators are connecting crude slate optimization, refinery scheduling, product blending, inventory positioning, and distribution planning into a more unified decision system."
- Context: 2026 market commentary; good current-state synthesis of VCO maturity direction.
- Confidence: Medium (commentary, no primary data).

**E46 — Claim:** ERTC 2024 themes: maximizing existing assets via digital tools; AI-enhanced multi-unit real-time optimization and digital twins — but AI's refining role "remains a topic of debate."
- Source: World Refining Association, "Key Themes at ERTC 2024"
- URL: https://worldrefiningassociation.com/speaker-articles/key-themes-at-ertc-2024/
- Date: 2024-10-08
- Excerpt: "AI is making waves across industries, but its role in the refining sector remains a topic of debate… The focus on AI-enhanced multi-unit real-time optimization and digital twin technology points to a broader theme of digital transformation within the industry."
- Context: Conference organizer's agenda synthesis; current industry agenda for the optimization stack.
- Confidence: High (agenda facts), n/a for outcomes.

**E47 — Claim:** AspenTech aspenONE SCM operationalizes S&OP/IBP monthly with collaborative demand, supply planning and SCM insights.
- Source: AspenTech, aspenONE Supply Chain Management page
- URL: https://www.aspentech.com/en/products/msc/aspenone-supply-chain-management
- Date: n.d. (accessed 2026-07-18)
- Excerpt: "Sales and Operations Planning/Integrated Business Planning — Create robust and optimized plans that holistically model the supply chain, manufacturing assets, constraints and financials while balancing emissions targets… Aspen Supply Chain Management Insights — Enable cross-functional stakeholder collaboration within one flexible environment designed to digitally operationalize the monthly Sales & Operations Planning (S&OP)/Integrated Business Planning (IBP) process."
- Context: Vendor product map; shows emissions targets now inside S&OP planning scope.
- Confidence: High (capability).

**E48 — Claim:** PETROBRAS institutionalized daily data reconciliation (Sigmafine) since 2005 because measurement errors corrupt plan-vs-actual and KPIs.
- Source: Computers & Chemical Engineering / ScienceDirect, "Data Reconciliation Practice at a Petroleum Refinery Company in Brazil"
- URL: https://www.sciencedirect.com/science/article/pii/S1570794609703505
- Date: n.d. (~2009; accessed 2026-07-18)
- Excerpt: "poor data quality may in general lead to both bad corrective actions and significant deviations between estimated and actual process state, product and feedstock storage and daily Key Performance Indicators (KPI). Data reconciliation… has being applied since August 2005 at several PETROBRAS petroleum refineries in Brazil."
- Context: Peer-reviewed; foundation layer for trustworthy plan-vs-actual/backcasting (garbage-in risk).
- Confidence: High.

**E49 — Claim:** AspenTech's closed-loop vision (GDOT/Unified) targets $0.05–0.15/bbl margin capture by integrating planning, scheduling and APC.
- Source: ARC Advisory Group (analyst) on AspenTech V12; AspenTech GDOT page
- URL: https://www.arcweb.com/industry-best-practices/aspentechs-unified-solution-helps-users-move-toward-self-optimizing-plant ; https://www.aspentech.com/en/products/msc/aspen-gdot
- Date: n.d. (~2023); n.d. (accessed 2026-07-18)
- Excerpt: "AspenTech claims that, by aligning these activities, a refinery could increases margin, capturing from $0.05 to $0.15/bbl by vertically integrating planning, scheduling, and advanced process control in a closed loop." / "Single Version of the Truth for Planning and Online Optimization — Share common models, flowsheet environment and data with planning and APC."
- Context: Analyst-reported vendor claim; the most credible quantification of integration value found.
- Confidence: Medium-High.

**E50 — Claim:** Refinery planning is embedding Industrial AI advisors (AVA) to guide planners inside the LP tool.
- Source: Engineering.com, "AspenTech Introduces aspenONE v14.3"; AspenTech AVA page
- URL: https://www.engineering.com/aspentech-introduces-aspenone-v14-3/ ; https://www.aspentech.com/en/products/msc/industrial-ai-for-planning-aspen-virtual-advisor-ava-for-unified-pims-aup
- Date: 2024-05-30; n.d.
- Excerpt: "Industrial AI is now incorporated in Aspen Unified PIMS with the availability of Aspen Virtual Advisor (AVA), which guides production planners to save time, make better decisions and explain the impact models have on performance and sustainability." (ARC's Peter Reynolds: "embedding technology into customer planning and scheduling models… improve plan effectiveness and reduce margin leakage.")
- Context: Current direction of the planning stack: AI-augmented planner workflow; supports CI/KM angle (capturing planner knowledge).
- Confidence: High (capability), Medium (outcomes).

---
## NUMBERED SOURCE LIST

*Dates in parentheses are publication dates where visible; "n.d." = no date shown, accessed 2026-07-18.*

[^1^] AspenTech, "Aspen PIMS" brochure AT-03906 — https://www.aspentech.com/-/media/aspentech/home/resources/brochure/pdfs/fy21/q3/at-03906-bro-aspen-pims.pdf (n.d.)
[^2^] Control Engineering, "PetroChina to modernize and optimize refineries" — https://www.controleng.com/petrochina-to-modernize-and-optimize-refineries/ (orig. ~2001; page dated 2025-04-23)
[^3^] Automation.com, "Honeywell enhances RPMS refining/petrochemical planning software" — https://www.automation.com/en-us/products/product08/honeywell-enhances-rpms-refiningpetrochemical-plan (2014-04-22)
[^4^] Popescu, C., "Software Implementation for Optimization of Production Planning within Refineries," Economic Insights – Trends and Challenges 1/2018, Petroleum-Gas University of Ploiești — http://upg-bulletin-se.ro/old_site/archive/2018-1/1-Popescu.pdf (2018)
[^5^] AVEVA, "AVEVA Unified Supply Chain – Network" — https://www.aveva.com/en/products/network/ (page dated 2026-05-07)
[^6^] Aalto University thesis (CDU modeling in AVEVA Spiral) — https://aaltodoc.aalto.fi/bitstreams/f4b702a3-222f-400f-ac93-d24eb6811d46/download (n.d.)
[^7^] AspenTech, "Aspen Petroleum Scheduler" brochure 11-9079 — https://www.aspentech.com/-/media/aspentech/home/resources/brochure/pdfs/fy17/q4/11-9079-bro-aspen-petroleum-scheduler.pdf (n.d.)
[^8^] Microsoft Azure Marketplace, "Aspen Petroleum Scheduler" — https://azuremarketplace.microsoft.com/it-it/marketplace/apps/aspentechnologyhq-1353108.aspen_petroleum_scheduler (2024-06-11)
[^9^] Refining Advantage (Rany), "About" (Orion→Aspen Petroleum Scheduler lineage) — https://www.refiningadvantage.com/about (n.d.)
[^10^] AspenTech, "Aspen Refinery Multi-Blend Optimizer" — https://home.aspentech.com/en/products/pages/aspen-refinery-multi-blend-optimizer (n.d.)
[^11^] AspenTech, "Aspen Unified Scheduling" — https://www.aspentech.com/en/products/msc/aspen-unified-scheduling (n.d.)
[^12^] ARC Advisory Group, "AspenTech's Unified Solution Helps Users Move Toward the Self-optimizing Plant" — https://www.arcweb.com/industry-best-practices/aspentechs-unified-solution-helps-users-move-toward-self-optimizing-plant (n.d., ~2023)
[^13^] Zimberger et al., ANCAP refinery planning & scheduling thesis, Universidad de la República (Uruguay) — https://www.colibri.udelar.edu.uy/jspui/bitstream/20.500.12008/53769/1/Zim25.pdf (n.d.)
[^14^] Honeywell Forge, "Honeywell Blending and Movement" — https://www.honeywellforge.ai/us/en/products/industrial-operations/honeywell-blending-movement (n.d.)
[^15^] Digital Refining, "Honeywell's advanced solutions to optimize material movement and blending operations" — https://www.digitalrefining.com/news/1001074/honeywells-advanced-solutions-to-optimize-material-movement-and-blending-operations (n.d., ~2012)
[^16^] AFPM, Plant Automation Session Descriptions (ConocoPhillips optimal gasoline blending; Chevron/Aspen MBO) — https://www2.afpm.org/forms/uploadFiles/24750000006EB.filename.PlantAutomationSessionDescriptions.pdf (n.d., ~2007)
[^17^] Processing Magazine, "Making the best of blending through optimization" (LUKOIL) — https://www.processingmagazine.com/mixing-blending-size-reduction/article/15587076/making-the-best-of-blending-through-optimization (2017-06-01)
[^18^] Automation.com, "Honeywell and UOP Announce Joint Solutions to Improve Refinery Profitability" — https://www.automation.com/article/honeywell-and-uop-announce-joint-solutions-to-impr (2003-12-15)
[^19^] Control Engineering, "Honeywell launches Business Flex software for process industries" (Production Scheduler for Refining; 3–6% production, 2–3% cost claims) — https://www.controleng.com/honeywell-launches-business-flex-software-for-process-industries/ (orig. ~2004; page dated 2025-04-23)
[^20^] AspenTech, "aspenONE V8.7 Software Release Sets New Benchmark for Manufacturing & Supply Chain Performance" — https://www.aspentech.com/en/resources/press-releases/aspenonert-v8-7-software-release-sets-new-benchmark-for-manufacturing-and-supply-chai2147491452 (2014-09-02)
[^21^] AVEVA customer case study, "bp sets up commercial CO2 emission modeling for refinery operations using AVEVA supply chain optimization" — https://www.aveva.com/content/dam/aveva/documents/perspectives/success-stories/SuccessStory_BP.pdf.coredownload.inline.pdf (n.d.)
[^22^] AVEVA (H. Gulati), "Enable Enterprise Agility & Sustainability," AVEVA PI World 2021 — https://cdn.osisoft.com/osi/presentations/2021-aveva-pi-world/UC21NA-D1OP040-AVEVA-Gulati-Enable-Enterprise-Agilty-Sustainability.pdf (2021)
[^23^] AVEVA (K. Juda), "AVEVA Schedule AI Assistant — Applying Artificial Intelligence to Scheduling," AVEVA World San Francisco — https://cdn.osisoft.com/osi/presentations/2022-AVEVA-San-Francisco/UC22NA-03PS30-AVEVA-Juda-AVEVA-Schedule-AI-Assistant-Applying-Artificial-Intelligence-To-Scheduling.pdf (2022-11)
[^24^] AVEVA (D. Bleackley), "Value Chain Optimization Roadmap and Vision" — https://cdn.mediavalet.com/eunl/content/2HRllLF2YUCH2U0W3jeWcA/tGlwu41StECXatFdq3T4iQ/Original/Production%20Optimization%20for%20Continuous%20Processes%20Roadmap%20%26%20Vision.pdf (2022-11)
[^25^] AVEVA, "Spiral Unified Supply Chain Management: Schedule" datasheet — https://www.aveva.com/content/dam/aveva/documents/datasheets/Datasheet_SpiralUnifiedSupplyChainManagementSchedule_EN.pdf (n.d.)
[^26^] TECHx Media, "AVEVA & Petronas strategically partner to deliver digital transformation" — https://techxmedia.com/en/aveva-petronas-strategically-partner-to-deliver-digital-transformation/ (orig. 2021; page dated 2025-04-17)
[^27^] Schneider Electric/AVEVA, Saudi Aramco Yanbu refinery RTO case study (via MAVESZ conference compilation) — https://mavesz.hu/wp-content/uploads/14_25_MAVESZ-Juhasz-Marton-Schneider-AVEVA-Kollaboracio.pdf (n.d., ~2019)
[^28^] arXiv:2605.15085, "From Data to Action: Accelerating Refinery Optimization with AI" — https://arxiv.org/html/2605.15085v1 (2026-05-14)
[^29^] Manutec, "Real-time Refinery Optimization through Opportunity Cost Visualization" (Refinery Profit Meter) — https://www.manutechnet.com/index.php?page=our-partners (n.d.)
[^30^] Imubit, "Oil Refinery Optimization: How AI Builds on What LP Models Leave Behind" — https://imubit.com/articles/oil-refinery-roi-optimization (2026-04-15)
[^31^] PTQ Q4 2025, Axens article on dynamic optimisation (GDOT) — https://ptqmagazines.digitalrefining.com/PTQ-Q4-2025 (Q4 2025)
[^32^] IZZI Business Services (A. Tatariya), "LP Accuracy – Best Practices," AVEVA PI World San Francisco — https://cdn.osisoft.com/osi/presentations/2022-AVEVA-San-Francisco/UC22NA-03PS20-IZZI-Tatariya-LP-accuracy-Best-Practices.pdf (2022-11)
[^33^] AIMod, "A Better Way To Keep Your LP Accurate" (Suncor Energy LP assurance) — http://aimod.com/papers/A%20Better%20Way%20to%20Keep%20Your%20LP%20Accurate.pdf (2009-08-25)
[^34^] KBC / Digital Refining, "Transforming LATAM's refineries: profit, performance, and decarbonisation" — https://www.kbc.global/uploads/files/whitepapers/Transforming_Latin_Americas_Refineries_Profit_Performance_Decarbonization.pdf and https://www.digitalrefining.com/article/1003335/transforming-latams-refineries-profit-performance-and-decarbonisation (n.d., ~2024–25)
[^35^] AFPM store, AM-93-65 "Integration of Refinery Scheduling with Planning" (L. Haverly) — https://www2.afpm.org/forms/store/ProductFormPublic/am-93-65-integration-of-refinery-scheduling-with-planning (1993)
[^36^] Instituto Superior Técnico (Lisbon) extended abstract on Galp downstream logistics optimization — https://fenix.tecnico.ulisboa.pt/downloadFile/1126295043838690/ExtendedAbstract_AL.pdf (n.d., ~2015)
[^37^] SAP Community, "Downstream Industry Process Overview & SAP Solutions" — https://community.sap.com/t5/sap-for-oil-gas-and-energy-blog-posts/downstream-industry-process-overview-amp-sap-solutions/ba-p/13148956 (2015-04-30)
[^38^] LeverX, "SAP IS-Oil Modules: Downstream vs. Upstream Logistics Optimization" — https://leverx.com/newsroom/sap-is-oil-modules (2026-03-19)
[^39^] Isaac Manuel (SAP expert), "SAP IBP for Oil & Gas Producers: Implementation, Modules, Challenges, and Best Practices" — https://isaacmanuel.org/courses/sap-ibp-for-oil-gas-producers/ (2025-09-30)
[^40^] Kalibrate, "Kalibrate Fuel Pricing Software" — https://kalibrate.com/kalibrate-fuel-pricing-software/ (2026-07-10)
[^41^] Kalibrate, "Kalibrate Fuel Pricing" product page — https://kalibrate.com/products/software/kalibrate-pricing/ (2025-11-19)
[^42^] SIGMA, State of the Industry Report (Kalibrate profile) — https://www.sigma.org/wp-content/uploads/2024/04/SRG_SIGMA_APRIL2024_WEB.pdf (2024-04)
[^43^] Oxford Institute for Energy Studies, "Forecasting Global Oil Demand: Application of Machine Learning Techniques" — https://www.oxfordenergy.org/wpcms/wp-content/uploads/2025/02/OIES-Paper-Forecasting-Global-Oil-Demand-Application-of-ML-Techniques-November-2024.pdf (2024-11)
[^44^] 6B Energy, "Openlink Endur Integration" — https://6b.energy/services/interoperability-and-integration/energy-trading-and-risk-management-etrm-system-integration/openlink-endur-integration/ (2025-12-01)
[^45^] DevOpsSchool, "Top 10 Energy Trading & Risk Management (ETRM)" — https://www.devopsschool.com/blog/top-10-energy-trading-risk-management-etrm-features-pros-cons-comparison/ (2026-06-19)
[^46^] Stadtler & Kilger (eds.), "Supply Chain Management and Advanced Planning" (5th ed.), ch. 24 oil industry — https://www.cur.ac.rw/mis/main/library/documents/book_file/2015_Book_SupplyChainManagementAndAdvanc.pdf (2015)
[^47^] Springer, "Refinery Planning and Scheduling: An Overview" — https://link.springer.com/chapter/10.1007/978-3-642-12067-1_8 (2010)
[^48^] ResearchGate compilation of refinery crude-scheduling literature (incl. Lee et al. 1996; Shah 1996; Wu et al. review) — https://www.researchgate.net/publication/318805226_Energy_Efficiency_Optimization_in_Scheduling_Crude_Operations_of_Refinery_Based_on_Linear_Programming (page accessed 2025-08-09)
[^49^] American Journal of Scientific Research (via scialert), "Optimal Design of Petroleum Refinery Topology using a Discrete Optimization Approach with Logical Constraints" — https://scialert.net/fulltext/?doi=ajsr.2011.95.113 (2011-02-26)
[^50^] Oil & Gas Journal, "Gravity and sulfur-based crude valuations more accurate than believed" — https://www.ogj.com/home/article/17230143/gravity-and-sulfur-based-crude-valuations-more-accurate-than-believed (n.d.)
[^51^] Shell plc (via Built In), "Economics Model Coordinator / Refinery Planner" job posting, Selangor, Malaysia — https://builtin.com/job/tech-specialist-mo-emc/3363360 (2024-11-13)
[^52^] Saudi Aramco Careers, "Linear Programming (LP) Modeling Engineer" job details — https://careers.aramco.com/expat_uk/job/Linear-Programming-%28LP%29-Modeling-Engineer/857096723/ (n.d.)
[^53^] GulfTalent, Saudi Aramco "LP Engineer" job posting — https://www.gulftalent.com/saudi-arabia/jobs/lp-engineer-587811 (2026-05-21)
[^54^] Petrogenium, Academy training booklet v11 (Refinery Planning; Scheduling & Logistics courses) — https://www.petrogenium.com/wp-content/uploads/2024/03/academy-web-booklet-v11.pdf (2024-03-19)
[^55^] Supply Chain Strategy, "Kinaxis and ExxonMobil: Revolutionising supply chain management" — https://supplychainstrategy.media/blog/2025/03/18/kinaxis-and-exxonmobil-revolutionising-supply-chain-management/ (2025-03-19)
[^56^] ARC Advisory Group, "ExxonMobil and Kinaxis: Creating a Next Gen Supply Chain Management Solution for Oil & Gas" — https://www.arcweb.com/industry-best-practices/exxonmobil-kinaxis-creating-next-gen-supply-chain-management-solution-oil (2025-09-01)
[^57^] TankTerminals.com / AJOT, "ExxonMobil + Kinaxis Team Up to Revolutionize Supply Chain Efficiency for the Energy Sector" — https://tankterminals.com/news/exxonmobil-kinaxis-team-up-to-revolutionize-supply-chain-efficiency-for-the-energy-sector/ (2024-10-16)
[^58^] o9 Solutions, "Oil & Gas Use Case" (unnamed supermajor) — https://o9solutions.com/case-studies/oil-and-gas (2024-09-18)
[^59^] Zippia, "Valero Energy CEO and Leadership" (executive career histories) — https://www.zippia.com/valero-energy-careers-12276/executives/ (2022-11-18)
[^60^] GFM Review, "Upstream, Midstream, Downstream, LNG, And Petrochemical Supply Chain Networks" — https://www.gfmreview.com/commodities/upstream-midstream-downstream-lng-and-petrochemical-supply-chain-networks (2026-07-04)
[^61^] World Refining Association, "Key Themes at ERTC 2024" — https://worldrefiningassociation.com/speaker-articles/key-themes-at-ertc-2024/ (2024-10-08)
[^62^] AspenTech, "Value Chain Optimization" explainer — https://www.aspentech.com/en/cp/value-chain-optimization (n.d.)
[^63^] AspenTech, "aspenONE Supply Chain Management" — https://www.aspentech.com/en/products/msc/aspenone-supply-chain-management (n.d.)
[^64^] AspenTech, "Aspen GDOT" product page — https://www.aspentech.com/en/products/msc/aspen-gdot (n.d.)
[^65^] Engineering.com, "AspenTech Introduces aspenONE v14.3" — https://www.engineering.com/aspentech-introduces-aspenone-v14-3/ (2024-05-30)
[^66^] Refining Advantage (Rany), "Products" (backcasting, auditing, unit model validation; auto-scheduling) — https://www.refiningadvantage.com/products (n.d.)
[^67^] Solomon Associates, AIChE Fuels & Petrochemicals benchmarking presentation — https://www.aiche.org/sites/default/files/community/aichecommunitysite/423541/solomonpresentationaichefuelspetrochemicals2017final.pdf (2017)
[^68^] IZZI Business Services LLP, company profile (LP/scheduling/blending services; multi-period planning deployments) — https://www.izzibs.com/pdf/izzibs_company_profile.pdf (n.d.)
[^69^] DYCOPS 2013 proceedings, "Integrated Product Blending Optimization for Oil Refinery Operations" — https://skoge.folk.ntnu.no/prost/proceedings/dycops2013-and-cab2013/media/DYCOPS/files/0072.pdf (2013)
[^70^] OMS eLearning Academy, "Advanced Closed-Loop Controls of Refinery Offsite Operations" — https://www.oms-elearning-academy.com/advanced-closed-loop-controls-of-refinery-offsite-operations/ (2026-01-28)
[^71^] AspenTech University, "Introduction to Refinery Planning using Aspen PIMS" course agenda — https://aspentech.my.site.com/customersupport/UniversityCourse?Id=a3p0B0000004YmzQAE (page dated 2026-04-10)
[^72^] AspenTech, "aspenONE V7.3 Manufacturing & Supply Chain Software" press release (Petroleum Supply Chain Planner; IMOS) — https://www.aspentech.com/en/resources/press-releases/aspentech-announces-release-of-aspenonert-v7-3-manufacturing-and-supply-chain-softwar6442451612 (2011)
[^73^] AB Academies, "Crack Spread Forecasting for Supply Chain Optimization" — https://www.abacademies.org/articles/crack-spread-forecasting-for-supply-chain-optimization-a-hybrid-model-using-time-series-and-deep-learning-with-bayesian-optimizati-16510.html (2023-12-14)
[^74^] AVEVA (D. Crisp), "The Future of AVEVA Unified Supply Chain," AVEVA World San Francisco — https://cdn.osisoft.com/osi/presentations/2022-AVEVA-San-Francisco/UC22NA-03PS50-AVEVA-Crisp-AVEVA-Calculation-Hub-Analysing-Complex-Networks-using-cloud-computing.pdf (2022-11)
[^75^] AspenTech, "Aspen Unified for Downstream Planning and Scheduling" — https://www.aspentech.com/en/products/msc/aspen-unified-for-downstream-planning-and-scheduling (n.d.)
[^76^] AspenTech, "AVA for Aspen Unified PIMS" — https://www.aspentech.com/en/products/msc/industrial-ai-for-planning-aspen-virtual-advisor-ava-for-unified-pims-aup (n.d.)
[^77^] Computers & Chemical Engineering / ScienceDirect, "Data Reconciliation Practice at a Petroleum Refinery Company in Brazil" (PETROBRAS, Sigmafine) — https://www.sciencedirect.com/science/article/pii/S1570794609703505 (n.d., ~2009)
[^78^] Hydrocarbon Engineering, "Supertanker – super savings" (dock scheduling; Aspen Petroleum Scheduler installed base) — https://www.hydrocarbonengineering.com/special-reports/11082014/Supertanker-super-savings-1025/ (2014-08-11)

---

## GAPS, LIMITATIONS & SUGGESTED FOLLOW-UPS

- **ETRM↔planning integration evidence is thin.** No public evidence of automated closed-loop links between ETRM (Endur-class) and refinery LP planning was found; the documented linkage is human/process-level (price curves, crude intelligence shared with traders, BP-style fast scenario runs). Recommend primary interviews.
- **Conference full texts are paywalled.** AFPM papers (e.g., Chevron MBO rollout; Haverly AM-93-65) and most ERTC technical papers are available only as abstracts; excerpts here are from abstracts/session descriptions.
- **Benefit figures are overwhelmingly vendor-reported.** Independent quantifications are scarce (ARC's $0.05–0.15/bbl closed-loop estimate; Solomon benchmarking methodology). All $/yr and $/bbl claims should be treated as directional, with confidence grades as marked.
- **Maturity data is anecdotal, not survey-based.** No public survey quantifying refinery planning-tool adoption/maturity distributions was found; the maturity ladder in §5.2 is synthesized from analyst descriptions, vendor installed-base claims, and job-posting evidence.
- **Kinaxis/o9 refining-specific depth is limited.** Their O&G material is supply-chain-generic; refinery LP-grade optimization remains with AspenTech/AVEVA/Honeywell/Haverly. The convergence signal (ExxonMobil–Kinaxis) is real but early-stage.
- **Several vendor pages carry no publication date**; where material, approximate era is inferred from release numbering (e.g., aspenONE V7.3≈2011, V8.7=2014, V12≈2023, v14.3=2024).

*Search log: 45 independent queries executed 2026-07-18 covering: PIMS/RPMS/Spiral/GRTMPS capability & usage; multi-site/multi-period LP; Aspen Petroleum Scheduler/MBO/Unified; Honeywell BLEND/BMA/Production Scheduler; AVEVA USC/Network/VCO decks; S&OP/IBP (SAP, aspenONE, o9, Kinaxis); retail fuel pricing (Kalibrate); ETRM (Endur/ION); demand forecasting (OIES); org models (Shell, Aramco, Valero, ExxonMobil, PetroChina, ANCAP, Galp); plan-vs-actual/backcasting (Aramco back-casting, Shell MVA, KBC, Refining Advantage, RPM, AVEVA prescriptive); benefits & maturity (AVEVA, KBC, IZZI, ARC, PTQ, Imubit, Yanbu); counter-narratives (OGJ crude valuation, academic theory–practice gap, ARC "no comprehensive SCM solution").*

*Prepared for Dimension 02 of the VCO / lookback-backcasting / CI knowledge management study. Analyst confidence in overall picture: High for stack composition and practices; Medium for quantified benefits; Low-Medium for maturity prevalence estimates.*
