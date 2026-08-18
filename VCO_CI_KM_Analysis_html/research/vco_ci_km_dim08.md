# Dimension 08 — The Broken Closed Loop Between Lookback Insights and Planning/Optimization
**Research date:** 2026-07-18 | **Scope:** refining/downstream plan–do–check–act (PDCA), LP model maintenance, lookback→planning feedback, S&OP/IBP maturity, learning-organization theory, CI knowledge sustainability | **Method:** 30 independent web searches across academic literature, vendor/consultancy material, regulator (CSB/HSE) investigation reports, and job-market evidence of LP-model roles.

---

## 1. How refinery LP models are maintained: ownership, update cadence, stale assumptions, calibration/backcasting practice

### 1.1 Ownership is a dedicated, scarce, senior specialty role
Job-market evidence shows LP model ownership sits with a small cadre of "LP Modeling Engineers" / "Refinery Planning Engineers" — typically requiring 7–15 years' experience — with explicitly codified maintenance, backcasting, and "gatekeeping" duties:

> "Maintain the hydrocarbon LP models by adding or deleting process units and updating yields and stream properties… Perform 'back-casting' and issue a monthly report on the LP gap, along with required mitigations." — Saudi Aramco / S&P Global Refinery Planning Engineer job spec (identical wording appears in both postings) [^1^][^2^]

> "Participate in the LP gatekeeping process for wholly-owned refineries and the global MPIMS model. Review and approve LP model changes… Validate and calibrate LP models using historical data and refinery test runs. Ensure models reflect current and future operating conditions and constraints." — Aramco LP Engineer (Central Planning & Modeling Division) [^3^]

> "Perform back casting studies, product quality giveaway studies, model reconciliation studies… Perform model reconciliations with help from Refinery LP specialists to determine areas in the LP model that need improvement." — Aramco LP Engineer/Executor spec [^4^]

The corporate center acts as **"LP gatekeeper"** for site models [^3^][^4^] — i.e., model changes are a controlled, hierarchical process, not a continuous feedback-driven one. A Varo Refining "Asset Economist" role confirms the plan-vs-actual monitoring loop exists but is analytic/dashboard-based ("Develop and maintain Power BI dashboards to monitor plan vs actual performance… Analyze trends to identify recurring optimization potential") rather than an automated model-update mechanism [^5^].

### 1.2 Update frequency: annual-to-multi-year for vector regeneration; monthly backcasting is the aspiration, not the norm
AVEVA's "LP accuracy – Best Practices" deck (Izzi/Tatariya, AVEVA UC 2022) is the most direct evidence of actual industry practice:

> "**Back-Casting using LP / Retro Analysis** — Time consuming work process; Based on aggregated data (say monthly average); Entire refinery optimization — so hard to pinpoint causes of mismatches." [^6^]

> "Use of Rigorous Simulation tools to generate LP vectors. Require plant test runs and process model recalibration… **Normal Update frequency is once in a year or few years. Highly time consuming & person dependent process**." [^6^]

> "Process Engineer's monitoring: Periodically monitor plant yields and compare the aggregated values against monthly plan yields… Excel based and person dependent process — Different process engineers for different units." [^6^]

> "Current Non-Sustainable Approach: Many different work processes. Many different Excel sheets. Difficult for LP modeler to update." [^6^]

AVEVA's proposed remedy — a "Process Model Manager" to regress plant data into base-delta LP submodels — is explicitly pitched as moving from **"person dependent"** to **"system dependent"** practice, an admission that the prevailing loop depends on individual experts [^6^]. The ROMeo datasheet states the problem from the vendor side:

> "Refinery planners are facing the challenge of updating the LP vectors to reflect the constantly changing feed and operating conditions of the refinery or plant. **Without up-to-date LP vectors, the planning model will not reflect the real plant and may not capture the full potential.**" [^7^]

### 1.3 Evidence of stale assumptions causing suboptimal/unachievable plans
Emerson/HART "Smart Refinery" supplement:

> "The ability to compare actual vs. expected unit performance and 'back-cast' the LP models to predict the period that just completed **can be complex and time consuming. Model errors can cause planner results to be suboptimal or unachievable.**" [^8^]

An Austrian thesis doing a gap analysis of Aspen Petroleum Scheduler plans vs actuals found systematic yield-structure deviation between model and plant and recommended repeating the deviation analysis and adapting the models — i.e., calibration was a project, not a routine [^9^]. Academic literature confirms structural yield-model error is endemic: fixed-yield CDU models "do not give a true representation of the key component of the crude in the refinery planning model," and swing-cut approaches assume linearity "whilst the actual property distribution in crude oil is highly non-linear" [^10^][^11^].

Baker & O'Brien's insurance-claim case shows the practical staleness problem: a refiner's LP was replaced just before a fire, so "any analysis of the old historical monthly LP model data would not be meaningful since the prior LP model had been revised," forcing a bespoke "backcast" with the new model — backcasting was an expert-service exercise, not standard operating procedure [^12^].

---

## 2. Do lookback findings systematically update LP constraints/yields, logistics models, inventory policies, forecasts, pricing, contracts?

**Finding: the update mechanisms exist but are manual, periodic, person-dependent, and weakly institutionalized — the loop is open at almost every link.**

- **LP yields/constraints:** updated annually-to-"once in a year or few years" via test runs and simulation recalibration [^6^]; monthly "LP gap" backcasting reports exist in best-practice job specs [^1^][^4^] but are described as "time consuming" and "hard to pinpoint causes of mismatches" in practice [^6^].
- **Plan–schedule–execution link:** the industry acknowledges a persistent structural gap. A Digital Refining crude-logistics study found "the actual refinery margin can decrease, compared to the planning figure, **by up to 25%**," because "LP models assume the capability to process optimal crude mixes… while in fact feedstock availability depends on the supply schedule and the logistic constraints involve unforeseen quality contamination" [^13^]. Vendor claims of margin uplift from closing plan/schedule/actual gaps cluster at **$0.05–0.15/bbl (AspenTech/ARC)** [^14^] and **~$0.25/bbl (AIGC)** [^15^] — quantifying the standing value of the open loop. Reliance/Shell's GeCOS case lists "Gross Refinery Margin leakage between monthly planning, daily scheduling and actual operations" as the problem statement [^16^].
- **Actuals capture (production/yield accounting):** this is the most mature link — Sigmafine-class tools close daily mass balances and compare "reconciled vs. theoretical yields" (IPLOM case: "A posteriori analysis and comparison of reconciled and theoretical data lead to… Gasoil-diesel yields improvement of about 1%") [^17^][^18^]. But these tools feed accounting/KPIs; the documented benefit is unit-level improvement, not systematic LP vector refresh — that handoff still runs through engineers' Excel workbooks [^6^].
- **Inventory policies / forecasts:** generic supply-chain practice prescribes monthly-to-quarterly safety-stock parameter audits and forecast feedback loops ("Establish a closed-loop feedback system to refine model parameters, update assumptions…") [^19^][^20^], but this is best-practice prescription from consultants/vendors, not evidence of downstream adoption. Notably, high buffers are warned to "mask underlying issues such as poor master data, weak forecasting" [^19^] — the inventory analogue of an open learning loop.
- **Pricing/contracts:** no direct evidence found of lookback findings systematically restructuring pricing or contract terms in refining; the literature treats these as commercial domains outside the planning-model feedback loop. **Gap flagged.**

---

## 3. S&OP/IBP as a PDCA loop: theory vs practice; feedback-into-planning maturity

The theory positions S&OP/IBP as the closed management loop (monthly cycle: demand review → supply review → reconciliation → executive MBR, with scenario planning and continuous forecast improvement) [^20^][^21^]. Practice lags badly:

Implement Consulting's IBP Maturity Assessment Study (50 companies, 2020):

> "Early adoptions of S&OP/IBP struggle to reach more than 3 on the maturity scale… **no respondents with a relatively old process (10 years or more) have been able to increase their maturity more than companies working with the process for 3-4 years.** Does the process exit project mode and lose attention?" [^22^]

Typical pains reported: "Low forecast quality… Data quality or availability… Scattered views and reports (no unified data model)… Missing scenario planning… **Short term firefighting**… Missing formalisation of process" [^22^] — i.e., the "Check" and "Act" phases collapse into firefighting instead of feedback. The study's own question ("Does the process exit project mode and lose attention?") is direct evidence of CI knowledge-sustainability failure in planning processes.

Process-industry specifics: chemical-industry S&OP must reconcile long-horizon asset constraints with execution [^23^]; a Neste S&OE thesis documents that at a renewable-diesel refiner, "lack of adequate documentation concerning the process leads to **inconsistent execution of the optimized S&OP plans**… and potentially… inability to meet the defined S&OP targets," with plans carried out "by individual team members… responsible of steering their own product chains" [^24^]. Downstream commentary agrees: "Planning may optimize against one set of assumptions, while actual execution is constrained by crude availability, tankage… **The gap between planning and execution can erode value even when the underlying optimization logic is sound.**" [^25^]

APC is the one genuinely closed loop in the refinery — and even it decays: "the performance of controllers can degrade over time if they are not modified as plant equipment and operating conditions change… The most common cause of APC performance degradation occurs when the controller model no longer matches the actual plant performance" [^26^]. Sustained APC value requires the same detect–diagnose–correct discipline that is missing at the planning level [^26^][^27^].

---

## 4. Learning organization / CI theory applied to process industries

**Theory (Argyris/Schön):** single-loop learning corrects actions within existing assumptions; double-loop learning questions the governing variables themselves [^28^]. Most organizational "lessons learned" activity is single-loop: "many 'lessons learned' change tactics but leave governing beliefs and policies untouched" [^29^]. Edmondson & Moingeon: "the reasoning processes employed by individuals in organizations inhibit the exchange of relevant information in ways that make double-loop learning difficult – **and all but impossible in situations in which much is at stake**" [^28^]. Argyris's Model I defensive routines ("undiscussable" topics, "fancy footwork," "skilled incompetence" of senior experts) are self-sealing and "anti-learning" [^30^][^31^] — directly relevant to senior planner/engineer-owned LP models that embody years of unchallenged assumptions.

**Process-industry empirical work:** the EU "Ways of Organisational Learning in the Chemical Industry" study (incl. a refinery site, Company U) shows genuine organizational learning is possible — operator-written procedures (PCDM) created bottom-up double-loop flows where "data gathered by operators in the course of PCDM quite frequently guides technologists in the re-engineering of the plant" [^32^]. But it also documents the fragility: one company's organizational change "was a decision of the new plant manager and not the result of an organisational inquiry," and learning-from-environment was "not… systematic" [^32^]. The same study catalogs the driver: early-retirement programs causing "the loss of experience and know-how in the shift teams" [^32^].

**CI program sustainability:** failure-rate evidence is stark. A global survey of 201 LSS experts found "significant failure rates," top causes being "lack of commitment by top management, resistance to change, inadequate rewards…, inconsistent monitoring and control…, poor communication" [^33^]. 17% of respondents in a pilot study "believe that more than 50% of projects fail during the **control** phase, i.e. **results are not sustained over time**" [^34^]. Literature compilations: "at least 50% of improvement programmes are deemed by firms to be failures over the longer term and up to 70% fail to achieve all of their intended benefits"; "two out of three of these programmes simply grind to a halt"; "only 10% of lean implementations are successful" (Bhasin) [^35^]. McKinsey's 15-year program puts transformation success at ~31%; Bain's 24,000-initiative dataset at 12% achieving original ambitions; "only 12% of organizations maintained transformation goals for more than three years, with an average 42% of financial benefits lost in later implementation stages" [^36^]. OpEx-vendor material concedes: "While many organizations successfully launch Operational Excellence programs, **sustaining them over the long term remains a significant challenge**" [^37^].

---

## 5. Quantified/anecdotal evidence of recurring problems that lookbacks identified but never fixed

The hardest evidence comes from process-safety investigations, where the "lookback" (incident investigation/audit) is formal and its failures are documented:

- **BP Texas City (CSB 2007):** "Many of the safety issues that led to the March 2005 accident were **recurring safety problems that had been previously identified in internal audits, reports, and investigations**… both BP Group executives and Texas City managers became aware of serious process safety problems… beginning in 2002" [^38^]. "Many action items from previous hazard analyses and incident investigations — such as a **1994 action item** to review the adequacy of the ISOM blowdown system following two serious incidents that year — **were never completed**" [^39^]. A required relief-valve study "was **13 years overdue**"; an internal audit found missing relief-valve design calcs "had existed for nearly 10 years" [^40^]. Only 3 of 8 prior ISOM blowdown releases were ever investigated [^40^]. Over 30 years, 23 workers died at the site before the 15 killed in 2005 [^38^].
- **Repeat-cause findings across sites:** CSB "found that the facility had failed to learn from a similar 2019 incident at the same site" (Toledo) [^41^]; Grangemouth hydrocracker: root cause included "**Failure to learn (previous near miss incident)**" [^42^]; FCC Pascagoula MNT: "the lessons learned… were not applied to the existing MNT columns… **there was no system to apply evaluation results** from the batch process to continuous processing equipment" [^43^]; PEMEX Deer Park (CSB 2026): wrong-flange opening is "a recognized and recurring problem across the chemical and refining industries, yet no industry-wide standard currently exists" [^44^]. CSB added Preventive Maintenance to its "Most Wanted" list because deferred maintenance was "a **recurring root cause** of incidents investigated by the CSB" [^45^]. A US Senate hearing put it plainly: "This is just one example of **recurring actions** that have led to accidents, injuries and fatalities… Operating procedures are not being reviewed and updated" [^46^].
- **Lessons-learned systems as "black holes":** PMI: lessons "often get lost in some sort of 'lessons learned database' — as in, a '**black hole**' — that nobody ever looks at… companies fail to 'assimilate' the lessons… running the risk to repeat the same mistakes again and again" [^47^]. An oil-company benchmarking study found LL capture was manual Excel + share-folder archiving; PMs agreed archived lessons "will be ignored" when the next project differs; "The major limitation… is the **failure of employees to use the system despite its existence**" [^48^].
- **Refinery turnarounds (5–7-year cycle, i.e., the industry's biggest recurring "plan" event):** "Most refineries conduct post-event reviews to identify and document lessons learnt… Those enhancements are often made to the planning book, **only to be shelved for the next turnaround and forgotten or overlooked in the next turnaround cycle**" [^49^].
- **Planning-domain recurrence:** Varo's job spec institutionalizes "Analyze trends to identify **recurring** optimization potential" [^5^]; margin-leakage figures (up to 25% plan-to-actual; $0.05–0.25/bbl) [^13^][^14^][^15^] are themselves quantified, recurring, well-known losses that persist industry-wide because the feedback mechanisms (§1–2) are manual and person-dependent.
- **Knowledge loss as structural driver:** oil & gas KM failure patterns: "Knowledge is captured once and never updated… documentation grows stale after turnarounds, modifications, or operational changes"; tacit knowledge of departing experts "rarely make[s] it into any system" → "teams solve the same problems repeatedly without access to previous solutions" and "repeated incidents because lessons from past near-misses or failures aren't captured and shared" [^50^].

---

## Tensions and counter-evidence
1. **Vendor optimism vs practitioner reality.** Vendors sell "closed loop" integration (Aspen Unified, AVEVA PMM, Imubit closed-loop AI) claiming automated reconciliation and margin capture [^6^][^14^][^51^], while their own decks describe current practice as Excel-based, person-dependent, annual-at-best [^6^]. Both can be true: tooling exists; institutionalization lags.
2. **Backcasting is real at best-in-class operators** (Aramco monthly LP-gap reports, gatekeeping, SROP alignment) [^1^][^3^][^4^] — the loop *can* be closed — but this requires a dedicated central division; smaller refiners rely on one or two LP engineers, a key-person risk [^6^][^50^].
3. **Safety vs economics.** The "check-act" loop is far more codified for process safety (CSB recommendations, MOC, PHA) than for margin/planning — yet even there, recurrence is documented. If the loop breaks under regulatory compulsion, it is unsurprising it breaks for margin lookbacks with no external enforcer.
4. **Transformation-failure statistics are contested** ("The 70% failure figure has no empirical basis… studies use different definitions") [^36^], but every dataset agrees sustained improvement is the minority outcome.

---

## Key Findings
1. **LP model maintenance is a craft, not a system.** Ownership concentrates in a handful of senior LP engineers; corporate "gatekeepers" control changes; yield-vector updates run annually to every-few-years via test runs and simulation recalibration; monthly backcasting exists in best-practice job specs but is widely described as time-consuming, aggregated, Excel- and person-dependent [^1^][^4^][^6^].
2. **Stale planning-model assumptions are a documented, quantified value leak:** model errors make plans "suboptimal or unachievable" [^8^]; plan-to-actual refinery margin erosion reaches up to 25% [^13^]; vendors consistently price plan/schedule/actual closure at $0.05–0.25/bbl [^14^][^15^].
3. **Lookback→model-update is the weakest link.** Actuals capture (yield accounting/data reconciliation) is mature, but the handoff into LP vectors, logistics models, inventory policies, and forecasts is manual and episodic; no evidence found of systematic updating of pricing/contract structures from lookbacks [^6^][^17^][^19^].
4. **S&OP/IBP functions as PDCA in theory only.** Maturity plateaus at 3–4 years and never advances thereafter ("process exits project mode and loses attention"); dominant pains are short-term firefighting, poor data, and missing scenario/feedback formalization — the "Check" and "Act" phases collapse [^22^][^24^].
5. **Learning-theory explains the breakage:** most refinery learning is single-loop; double-loop inquiry is blocked by Model I defensive routines, senior-expert "skilled incompetence," and knowledge walking out with retirees [^28^][^30^][^32^][^50^].
6. **CI/op-ex knowledge does not sustain:** 50–70% of improvement programs fail long-term; >50% of LSS projects fail in the *control* phase (results not sustained); only ~12% of transformations sustain goals beyond 3 years [^33^][^34^][^35^][^36^].
7. **Recurring problems after formal lookbacks are extensively documented** in process safety (Texas City: audit findings ignored 1994–2005, 13-year-overdue studies, unclosed action items; Toledo, Grangemouth, Pascagoula, Deer Park: "failure to learn" as named root cause) and in turnarounds (lessons "shelved… and forgotten" each 5–7-year cycle) [^38^][^39^][^41^][^42^][^44^][^49^]. Lessons-learned databases are known "black holes" — capture happens, assimilation does not [^47^][^48^].

---

## Sources
- [^1^] Jobgether — Refinery Planning Engineer, S&P Global (RCMA). https://jobgether.com/offer/69d015625bd3b40540a7c88b-refinery-planning-engineer (accessed 2026-07-18; posting dated 2026-06-03)
- [^2^] S&P Global Careers — Refinery Planning Engineer. https://careers.spglobal.com/talent-network/jobs/318664 (2026-04-17)
- [^3^] Saudi Aramco Careers — Linear Programming (LP) Modeling Engineer. https://careers.aramco.com/expat_uk/job/Linear-Programming-%28LP%29-Modeling-Engineer/857096723/ ; LP Engineer https://careers.aramco.com/expat_us/job/Linear-Programming-%28LP%29-Engineer/855855423/
- [^4^] GulfTalent — LP Engineer User (Executor), Saudi Aramco (2024-05-10). https://www.gulftalent.com/saudi-arabia/jobs/lp-engineer-user-executor-389829
- [^5^] JobScout24 — Refinery / Asset Economist, Varo Refining (Cressier) (2026-02-21). https://www.jobscout24.ch/en/job/a86e4ba4-4ae1-490b-9df7-8901adff4997/
- [^6^] Izzi & Tatariya, "LP accuracy – Best Practices," AVEVA PI System UC 2022. https://cdn.osisoft.com/osi/presentations/2022-AVEVA-San-Francisco/UC22NA-03PS20-IZZI-Tatariya-LP-accuracy-Best-Practices.pdf
- [^7^] AVEVA — ROMeo Refinery Reactor Model Portfolio datasheet. https://www.aveva.com/content/dam/aveva/documents/datasheets/Datasheet_ROMeoRefineryReactorModelPortfolio_EN.pdf.coredownload.inline.pdf
- [^8^] Emerson / HART Energy — "Smart Refinery" supplement (Sharpe quotes). https://www.emerson.com/is/content/emerson/en/corporate/shared-assets/documents/smart-refinery-supplement-hart-energy.pdf
- [^9^] Montanuniversität Leoben thesis — Gap analysis, Aspen Petroleum Scheduler plan vs actual. https://pureadmin.unileoben.ac.at/ws/portalfiles/portal/3911200/AC13050042n01.pdf
- [^10^] "Aggregate Model for Refinery Production Planning," Computer Aided Chemical Engineering (Elsevier, 2012). https://www.sciencedirect.com/science/article/pii/B9780444595201500427
- [^11^] "A novel model for multi-plant mixed heavy crude oils refinery planning," Chinese J. Chem. Eng. (2017). https://www.sciencedirect.com/science/article/pii/S1004954116302920
- [^12^] Baker & O'Brien — "Refinery LP Models – Intimidating but Necessary" (2022-08-10). https://bakerobrien.com/case-study/refinery-lp-models-intimidating-but-necessary
- [^13^] Digital Refining — "Crude logistics scheduling." https://www.digitalrefining.com/article/1002637/crude-logistics-scheduling
- [^14^] ARC Advisory — "AspenTech's Unified Solution… Self-optimizing Plant" ($0.05–0.15/bbl margin leakage claim). https://www.arcweb.com/industry-best-practices/aspentechs-unified-solution-helps-users-move-toward-self-optimizing-plant
- [^15^] AIGC — Optimization & Modelling (25¢/bbl plan-schedule-actual claim). https://www.aigcom.com/Solution/optimization-modelling/
- [^16^] AIMMS — Reliance Industries GeCOS crude supply chain case (2021-07-27). https://www.aimms.com/story/reliance-industries-limited-optimizes-its-crude-supply-chain-with-aimms-based-tool/
- [^17^] OSIsoft/Pimsoft — "Yields reconciliation using Sigmafine in an agile refinery" (IPLOM, UC 2003). https://www.sigmafine.com/wp-content/uploads/2017/05/IPLOM-Yields-Reconciliation-Using-Sigmafine-in-an-Agile-Refinery-OSI-UC-2003.pdf
- [^18^] Pimsoft — Sigmafine in Refining solution brief. https://www.sigmafine.com/wp-content/uploads/2018/05/Solution-Brief-Sigmafine-in-Refining_Letter.pdf
- [^19^] ISM — "Mastering Safety Stock Calculations" (2025-11-25). https://www.ism.ws/logistics/how-to-calculate-safety-stock/
- [^20^] IBF — Demand Planning Advisory (closed-loop forecast improvement). https://ibf.org/demand-planning-advisory
- [^21^] OnePint — "What Is S&OP? Complete Guide" (2026-05-26). https://www.onepint.ai/insights/what-is-sales-operations-planning-sop-a-complete-guide-to-the-process-and-cycle
- [^22^] Implement Consulting Group — "The IBP Maturity Assessment Study 2020." https://cms.implementconsultinggroup.com/media/uploads/topics/Integrated-Business-Planning/the-ibp-maturity-assessment-study-2020.pdf
- [^23^] SAP Community — "End to End Supply Planning in the Chemical Industry" (2022-05-03). https://community.sap.com/t5/supply-chain-management-blogs-by-sap/end-to-end-supply-planning-in-the-chemical-industry/ba-p/13529746
- [^24^] Liimatainen, M. — "Developing Sales and Operations Execution Process" (Neste S&OE thesis, Theseus). https://www.theseus.fi/bitstream/10024/861671/2/Liimatainen_Mikko.pdf
- [^25^] GFM Review — "Upstream, Midstream, Downstream… Supply Chain Networks" (2026-07-04). https://www.gfmreview.com/commodities/upstream-midstream-downstream-lng-and-petrochemical-supply-chain-networks
- [^26^] AspenTech — aspenONE Advanced Process Control datasheet. https://datasheet.datasheetarchive.com/originals/crawler/aspentech.com/727539b2ddf9ead6b85ed64214c09d5e.pdf
- [^27^] PiControl — "Implementing Advanced Process Control for Refineries and Chemical Plants." https://lam.fkit.hr/static/LAM_Web_Implementing_Advanced_Process_Control_for_Refineries_and_Chemical_Plants.pdf
- [^28^] infed.org — "Chris Argyris: theories of action, double-loop learning and organizational learning." https://infed.org/dir/welcome/chris-argyris-theories-of-action-double-loop-learning-and-organizational-learning/
- [^29^] Umbrex — "Argyris Single- and Double-Loop Learning model" (2026-02-06). https://umbrex.com/resources/frameworks/organization-frameworks/argyris-single-and-double-loop-learning-model/
- [^30^] PubAdmin Institute — "Implementing Double-Loop Learning in Organizations" (2026-04-18). https://pubadmin.institute/administrative-thinkers/double-loop-learning-in-organizations-chris-argyris
- [^31^] Buteau — "Lessons from Chris Argyris" (2026-07-10). https://www.antoinebuteau.com/lessons-from-chris-argyris/
- [^32^] EU CORDIS — "Ways of Organisational Learning in the Chemical Industry" (HPSE-CT-1999-00041 final report). https://cordis.europa.eu/docs/projects/files/HPSE/HPSE-CT-1999-00041/82608191-6_en.pdf
- [^33^] Antony, Lizarelli & Fernandes — "A Global Study Into the Reasons for Lean Six Sigma [project failures]" (Heriot-Watt/IEEE). https://pure.hw.ac.uk/ws/portalfiles/portal/41828249/IEEE_Final_02072020.pdf
- [^34^] Antony & McFarlane — "A study into the reasons for process improvement project failures: results from a pilot survey" (Strathclyde, 2019). https://strathprints.strath.ac.uk/68367/1/Antony_McFarlane_2019_A_study_into_the_reasons_for_process_improvement_project.pdf
- [^35^] Massey University thesis — CI sustainability failure-rate literature compilation (Found, Venkateswarlu & Nilakant, Bhasin et al.). https://mro.massey.ac.nz/bitstreams/4ae509e6-bdbd-402e-a429-4d7e03b391b1/download
- [^36^] NSSG Consulting — "Why Process Improvement Projects Fail Before They Start" (2026-01-20; compiling McKinsey, BCG, Bain 2024, Industry Week/MPI 2007). https://nssg.consulting/insights/process-improvement-failure
- [^37^] KaiNexus — "How to Ensure Long-Term Sustainability of Operational Excellence Efforts." https://blog.kainexus.com/how-to-ensure-long-term-sustainability-of-operational-excellence-efforts
- [^38^] CSB — "Organizational and Safety Deficiencies at All Levels of the BP Corporation Caused… Texas City Disaster." http://www.csb.gov/u-s-chemical-safety-board-concludes-organizational-and-safety-deficiencies-at-all-levels-of-the-bp-corporation-caused-march-2005-texas-city-disaster-that-killed-15-injured-180/
- [^39^] CSB Texas City findings via Forensis Group timeline (2025-10-22). https://www.forensisgroup.com/resources/expert-legal-witness-blog/bp-texas-city-refinery-how-workplace-accidents-expose-process-safety-failures-and-corporate-oversight-gaps
- [^40^] WRP — "BP ignored safety warnings – US Chemical Safety Board report reveals." https://wrp.org.uk/features/bp-ignored-safety-warnings-us-chemical-safety-board-report-reveals/ ; Process Engineering — "Cost cutting BP bosses blamed." https://processengineering.co.uk/article/1298729/cost-cutting-bp-boss
- [^41^] Imubit — "Process Safety Management in Daily Plant Operations" (CSB Toledo/ITC Deer Park findings) (2026-04-15). https://imubit.com/articles/process-safety-management-daily-ops
- [^42^] EPSC/IChemE — "Learning Lessons from Major Incidents" (Peter Marsh, IChemE Centenary Ed. 2022). https://www.epsc.be/l/en/library/download/urn:uuid:1095a934-419f-44d0-9cfa-c86bbb526b73/2022.05_learning-lessons-from-major-incidents-v10.pdf
- [^43^] Jones & Modi, JCL Risk Services — CCPS "Call to Action" paper (CSB Giant & FCC Pascagoula findings). https://jclrisk.com/wp-content/uploads/sites/3/2018/04/David-A.-Jones-Kay-A.-Modi-JCL-Risk-Services-GCPS-Call-to-Action-Paper.pdf
- [^44^] McFarlane Law — "PEMEX Deer Park H2S Release: CSB Findings" (2026-03-06). https://www.mcfarlanelaw.com/pemex-deer-park-hydrogen-sulfide-csb-report-2026/
- [^45^] CSB — "Board Members Add Preventive Maintenance to Most Wanted Safety Improvement Program" (2016-07-15). https://www.csb.gov/csb-board-members-add-preventive-maintenance-to-most-wanted-safety-improvement-program/
- [^46^] US Senate hearing — "A Review of Process Safety Management in the Oil and Gas Industry" (2012). https://www.govinfo.gov/content/pkg/CHRG-111shrg57104/html/CHRG-111shrg57104.htm
- [^47^] PMI — "Lessons (Really) Learned? How to Retain Project Knowledge and Avoid Recurring Nightmares" (2025-10-18). https://www.pmi.org/learning/library/knowledge-management-lessons-learned-10161
- [^48^] "Benchmarking Projects' 'Lessons Learned' through Knowledge Management Systems: Case of an Oil Company," Open J. Business & Mgmt (SCIRP, 2021). https://www.scirp.org/journal/paperinformation?paperid=106963
- [^49^] Digital Refining — "Beyond turnaround planning / Keep best practices evergreen." https://cdn.digitalrefining.com/data/digital_magazines/file/1430011333.pdf ; https://www.resourcedev.com/PDF/TurnaroundArticle.pdf
- [^50^] Matterport — "Knowledge Management in the Oil & Gas Industry" (2026-05-29). https://matterport.com/blog/knowledge-management-oil-gas-industry
- [^51^] Imubit — "Reducing Gasoline Blending Giveaway with AI Optimization" (2026-05-01). https://imubit.com/articles/gasoline-blending
