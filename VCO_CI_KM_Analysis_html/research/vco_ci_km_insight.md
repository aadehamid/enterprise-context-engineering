# Phase 6 — Cross-Dimension Insights
**Study:** Downstream VCO lookback/backcasting & CI-focused Knowledge Management
**Date:** 2026-07-18 | **Derived from:** dim01–dim12 + cross_verification.md

---

## Insight 1 — The industry has industrialized *measurement* of the plan-vs-actual gap but not *learning* from it; the missing layer is knowledge infrastructure, not analytics
- **Derived from:** dim01, dim02, dim03, dim08 (H1, H2); dim12
- **Rationale:** Every layer of the VCO stack now produces variance artifacts — controller margin bridges, Solomon gap analyses, margin-capture KPIs, LP-gap backcast reports, plan-schedule-actual reconciliation tools. Yet the same evidence shows LP errors persisting "months or even years," project slip "remarkably constant" for a decade, and identical incidents recurring after documented investigations. The binding constraint is not the ability to quantify variance but the absence of a governed mechanism that converts variance explanations into updated models, constraints, policies, and reusable guidance.
- **Implications:** For COMPANY, incremental analytics/dashboard investment has diminishing returns; the high-leverage investment is the CI knowledge/context layer that closes plan–do–check–act.
- **Confidence:** High

## Insight 2 — Lookback and backcasting share one failure mode: both produce *episodic artifacts* whose context decays faster than the organization acts on them
- **Derived from:** dim03, dim06, dim08, dim10, dim11 (H2, H8, H10)
- **Rationale:** Lookbacks (monthly bridges, post-audits, RCAs) and backcasts (net-zero pathways, portfolio roadmaps) are both generated as point-in-time deliverables — decks, reports, models. Organizational memory of events fades in ~3 years; rotation removes owners in 2–3-year cycles; LP model regeneration happens annually; strategic milestones sit outside 10-year planning windows. Each cadence mismatch means the artifact's assumptions, rationale, and evidence are no longer recoverable when the next decision cycle needs them. The two disciplines are usually studied separately, but the decay mechanism is identical — which is why a single context-management foundation can serve both.
- **Implications:** COMPANY's KM scope should explicitly span *both* lookback and backcasting artifacts (as the brief states), because the root cause — context decay across decision cycles — is common.
- **Confidence:** High

## Insight 3 — "Context" in this problem space has three distinct layers that are conflated in practice: data context, decision context, and learning context — and only the first is addressed by current tooling
- **Derived from:** dim07, dim12; dim04, dim10
- **Rationale:** Industrial "contextualization" (knowledge graphs linking sensor data to assets/events — Cognite/AVEVA positioning) addresses *data context*. *Decision context* (rationale, alternatives considered, assumptions, trade-offs) has no established capture practice in industrial planning — the ADR/decision-record discipline exists only in software engineering. *Learning context* (why a lesson applies, its boundary conditions, source quality, review status) is what NASA LLIS and black-hole repositories demonstrably failed to retain. A CI-KM foundation that imports only data-contextualization practice will repeat the LLIS failure at higher cost.
- **Implications:** The taxonomy/contextualization framework and knowledge quality tiers in COMPANY's requirements must be designed around decision and learning context, with data context as an enabler — not the reverse.
- **Confidence:** High

## Insight 4 — The weakest links are all *interfaces*, and they map one-to-one onto KM requirements: finding→model, lesson→standard, pathway→plan, person→system
- **Derived from:** dim02, dim03, dim06, dim08, dim11, dim12 (H2, H3, H8, H11)
- **Rationale:** Each documented failure is an interface failure, not a component failure: lookback findings never reach LP vectors/safety stocks/pricing (finding→model); RCA outputs never convert into standards or verified-closed actions (lesson→standard); backcast milestones sit outside planning periods with no signposts/triggers (pathway→plan); elicitation of the retiring cohort fails because knowledge is person-held (person→system). Interface failures are precisely what governance (ownership, lifecycle states, refresh triggers, escalation) and context management (templates, metadata, tiering) are designed to fix — this gives a principled mapping from each §3 shortcoming to each §5 capability dimension.
- **Implications:** Report §5 should be organized as interface-closing capabilities, each traced to evidenced failure modes.
- **Confidence:** High

## Insight 5 — Variance is structurally misattributed because market-driven and execution-driven components are not separated; without decision context, lookbacks cannot tell bad luck from bad decisions
- **Derived from:** dim03, dim09, dim10 (M2, M5, H7)
- **Rationale:** Oil-price forecasts have ~37% 5-yr MAPE and professionals don't beat random walks — a large share of any margin variance is unforecastable market noise. At the same time, execution variance (LP decay, scheduling slippage, capture shortfalls) is controllable. Because decision rationales and planning assumptions are not captured (H5), and KPI definitions drift across functions (H7), monthly reviews cannot decompose "we were wrong about the market" from "we executed poorly" from "the model was stale" — so reviews default to narrative ("monthly autopsy") and defensive routines (Argyris). This is why lookbacks feel unproductive and lose sponsorship.
- **Implications:** A context foundation must capture *ex-ante* assumptions (prices, yields, constraints) versioned with the decisions they informed, enabling ex-post separation of forecast error, assumption bias, and execution error — the precondition for causal learning rather than blame.
- **Confidence:** High

## Insight 6 — Knowledge quality tiering is the keystone requirement: it simultaneously enables governance, reuse, and AI-readiness, and its absence explains why repositories become black holes
- **Derived from:** dim12, dim07, dim11 (H11, H12, H5)
- **Rationale:** The counter-examples that work (Schlumberger tiering, Admiralty-Code source/content ratings, KCS "reuse is review", CALL curation) all distinguish authoritative/validated knowledge from indicative material; the failures (NASA LLIS, project lessons databases) treat all captures as equal, so users cannot trust retrieval and stop searching. GenAI amplifies exactly this property: LLMs cannot distinguish authoritative from outdated content without metadata, so tiering/provenance is also the AI-readiness investment. One design element therefore serves governance (approval workflows), reuse (confidence signaling), and AI (grounding) at once.
- **Implications:** COMPANY's "knowledge quality tiers and confidence model" should be sequenced first among the capability dimensions; it de-risks every subsequent one.
- **Confidence:** High

## Insight 7 — CI-first is the correct entry point for KM because CI is the only function whose *output* is knowledge; everywhere else KM is overhead, in VCO/CI it is the product
- **Derived from:** dim01, dim02, dim08, dim11, dim12 (H1, H11; M1)
- **Rationale:** Generic enterprise KM programs die of unclear value capture. In VCO/CI, the value chain is short and monetized: a reused lesson changes an LP constraint, a safety stock, a pricing rule, or a milestone — with defensible $/bbl anchors ($0.05–0.50/bbl leakage components; $30–85M/yr VCO value pool; reliability gaps worth ~7% PRV). CI processes already generate the raw material (rationales, findings, recommendations) as a byproduct, so capture cost is marginal, and the sponsor pain (recurring issues, attrition risk) is acute. This explains why COMPANY's framing — KM *for CI* rather than enterprise KM — is structurally sound, and why AI enablement should ride on this foundation later.
- **Implications:** Report §6 should make this argument explicitly as the strategic justification for a CI-first KM foundation.
- **Confidence:** High

## Insight 8 — The culture problem and the systems problem are coupled: uncontextualized lessons feel like blame instruments, and blame suppresses the candor that generates lessons
- **Derived from:** dim10, dim11, dim12 (H9, H10)
- **Rationale:** Evidence shows variance reviews drift into "monthly autopsy" blame sessions; punitive dynamics push error underground (Dekker; Edmondson detection-vs-rate finding). A lesson record stripped of context ("investigator found operator error") reads as an accusation; a record with full decision context (constraints, information available, alternatives) reads as system analysis (Reason's local rationality). Therefore the *design of the knowledge artifacts themselves* — what context fields are mandatory — either reinforces or mitigates the culture barrier. KM design is culture design.
- **Implications:** COMPANY's capture templates and governance workflows are also psychological-safety instruments; requirement mapping should make this explicit (e.g., mandatory "context/constraints at time of decision" fields; system-cause framing).
- **Confidence:** Medium-High (well-grounded inference from safety-science evidence; the coupling mechanism itself is synthesized)
