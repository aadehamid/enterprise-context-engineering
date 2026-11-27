# ECE–EPM–PPC Repository Dependency and Operating Model

**Status:** Proposed  
**Purpose:** Define Enterprise Context Engineering's relationship to Enterprise Performance Model (EPM) and Pearland Petroleum Corporation (PPC).  
**Related:** [Shared Technical Foundation](shared-technical-foundation.md) defines which technologies ECE reuses.

## 1. Three responsibilities

**EPM:** defines what the downstream enterprise means and how performance is represented.

**ECE:** defines how trustworthy enterprise context is assembled, grounded, temporally bounded, traced to evidence and evaluated.

**PPC:** integrates both in a realistic fictional downstream enterprise.

```text
EPM ── semantic/performance contracts ──► PPC
ECE ── context/provenance/evaluation contracts ──► PPC
```

EPM and ECE do not require PPC to build or validate their core artifacts.

## 2. ECE remains executable

ECE executes its framework:

- canonical truth generation;
- distributed evidence generation;
- artifact manifests;
- provenance validation;
- temporal validation;
- context graph construction;
- retrieval products;
- grounding evaluation;
- hidden-truth isolation;
- release publication.

PPC executes the enterprise simulation.

## 3. Semantic dependency

ECE should not fork domain semantics when an authoritative domain ontology exists.

For downstream PPC use cases, EPM supplies downstream business/performance semantics, including the Downstream Oil and Gas Ontology, which ECE imports rather than forks. ECE supplies generic context semantics such as EvidenceItem, Artifact, SourceAssertion, Claim, Decision, DecisionOption, Constraint, Outcome and provenance.

PPC specializes/instantiates both.

## 4. Versioned ECE contracts

ECE should publish versioned reusable contracts for:

- evidence-item schema;
- artifact manifest;
- source-assertion and claim model;
- decision-dossier schema;
- provenance model;
- temporal-context model;
- evidence/inference/contradiction/unknown vocabulary;
- hidden-truth isolation rules;
- evaluation rubric.

PPC release manifests should record the ECE versions they consume.

## 5. Feedback loop

When PPC discovers a generic context-engineering gap:

```text
PPC proposal
→ ECE review
→ ECE contract/ADR update
→ ECE release
→ PPC dependency update
```

PPC must not silently redefine generic ECE concepts.

When the gap is downstream business meaning, the proposal goes to EPM instead.

## 6. Code-placement rule

If code makes sense without PPC's fictional company, ask whether it belongs upstream.

Examples that belong in ECE:
`artifact_manifest.py`, `decision_dossier.py`, `claim_provenance.py`, `temporal_validation.py`, `evaluate_grounding.py`.

Examples that belong in PPC:
`simulate_ppc_hurricane.py`, `calculate_ppc_margin.py`, `materialize_ppc_mysql.py`.

## 7. Shared infrastructure versus shared data

Reusable infrastructure/code is encouraged. Shared project truth is not.

ECE and PPC should have:
- separate R2 buckets;
- separate release manifests;
- separate hidden-evaluation access;
- separate graph namespaces/databases where practical;
- separate scenario identifiers.

## 8. Governing statement

> **EPM defines enterprise meaning. ECE defines trustworthy context. PPC proves that both can operate together.**

## 9. 2026-11-26 PPC canonical world-model and five-repository boundary

On 2026-11-26, PPC reconciled its baseline in `aadehamid/pearland-petroleum-corporation` (`ADR-0040` through `ADR-0056`, repo-rename alignment merged at commit `ebc226f`). Within the five-repository downstream ecosystem, ownership splits as follows:

- **PPC (`aadehamid/pearland-petroleum-corporation`)** owns the single canonical enterprise world model (Refinery A v1), runs the mechanistic refinery and enterprise simulation, isolates hidden world truth exclusively under `evaluation/hidden/`, and plans to publish `WorldExportBundle` in `WP-8B` (`ADR-0053`). `WorldExportBundle` is partitioned into `observable/` (consumed by operational pipelines and sister repositories) and `hidden_truth/` (restricted to replay grading and backcasting attribution).
- **EPM (`aadehamid/enterprise-performance-model`)** owns downstream business, process, and KPI semantics.
- **ECE (`aadehamid/enterprise-context-engineering`)** owns domain-neutral context, provenance, temporal-validity, hidden-truth isolation, and evaluation contracts. ECE keeps Lagos Specialty Chemicals (LSC) as its independent standalone worked example and does not duplicate PPC's Refinery A canonical world truth.
- **ICE (`aadehamid/industrial-context-engineering`, formerly `scada_harmonization`)** owns OT harmonization and Sparkplug B UNS patterns.
- **EDI (`aadehamid/engineering-drawing-intelligence`, formerly `Engineering_Drawing_to_Graph`)** owns engineering drawing and DEXPI topology graph patterns.

PPC consumes EPM, ECE, ICE, and EDI through commit-pinned provisional adapters (`ADR-0042`) so PPC implementation does not block on pending upstream releases. ECE remains independent of PPC and keeps its own contracts, R2 bucket, release manifests, and hidden-evaluation boundaries separate.
