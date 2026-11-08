# Supplied KM baseline reference

The user supplied the [baseline diagram](km-baseline-reference.png) and an accompanying "KM Baseline Architecture Direction – Comprehensive Overview" during the architecture review on 2026-11-07, America/Chicago time. The image is retained unchanged. The excerpts below quote the accompanying text; they supplement the image's labels.

The user specified the implementation constraint:

> Note that we dont have to use tools listed on the image. We will stick with open source equivalent

The [proposed ECE architecture](../solution-architecture.md) interprets this material for ECE. Product names in the reference are baseline choices, not ECE recommendations. Names such as "RVCO Value Add" and "X/PPIMS" reproduce the supplied reference; they do not rename entries in ECE's existing source inventory.

## Human review and promotion

From "Human-in-the-Loop Expert Review (Silver → Gold Promotion)":

> Because the Contextualization Builder outputs drafts only, all newly contextualized records enter the Refined / Silver zone in a Draft lifecycle state.

> VCO CI Backcasters and VCO CI Managers (supported by low-confidence reporting in the Retrieval & Delivery layer) review, refine, and validate the extracted lessons, tags, and entity mappings.

> Once approved by a Manager or SME, the record's lifecycle state transitions from Draft → Approved, promoting it into the Core / Gold zone and instantiating its relationships in the Knowledge Graph.

From "Storage Layer (Medallion Architecture)":

> Core / Gold (Approved Records): Houses trusted, validated, and medium/high-confidence knowledge records that have passed expert/manager review and transitioned from Draft to Approved lifecycle status. These records are fully tagged with the governed taxonomy and exposed to the Retrieval & Delivery Layer.

From "Governance & Security Layer":

> High / Medium Confidence: Prioritized for validation and promotion to the Core / Gold layer for active retrieval.

> Low Confidence: Flagged and routed to Power BI Low-Confidence Reporting queues for mandatory VCO CI Backcaster and VCO CI Manager intervention.

## Sensitivity and live-source handling

From "Event-Driven Capture & Alerting (Synchronous / Real-Time)":

> Sensitivity (Hold for Review): Screens incoming artifacts for sensitive, confidential, or restricted content. Items flagged for sensitivity are placed on hold for administrative or SME review before broader platform exposure.

From "Supporting Storage Components":

> Direct to Source (Live, Current State): Structured outputs from Planning Systems (model outputs) and BI & Dashboards (plan vs. actual) are queried live at the source rather than duplicated into the medallion layers. This preserves a single system of record and ensures end users always interact with real-time, current-state data.

The ECE proposal qualifies the reference's synchronous and current-state language. Event delivery is asynchronous; source freshness must be checked. The proposal also requires retained evidence or immutable source versions when live observations support a historical decision. These are ECE design interpretations, not statements quoted from the baseline.
