# Project Charter — Enterprise Context Engineering

> **Status: DRAFT** — for Hamid's review. Nothing here is binding until approved.

This document makes the commitments the README doesn't. The README states the
vision, problem, principles, and build flow; this charter defines what success
looks like, what is out of scope, who decides what, the phases with gates
between them, and the dependencies the project rests on.

## 1. Success criteria

The project succeeds when a question-answering agent built on this
architecture can be *shown* — not claimed — to meet the following on the
golden evaluation set. Targets below are proposed; Hamid sets the final
numbers at the Phase 1 gate.

| Criterion | Measure | Proposed target |
|---|---|---|
| Claim-level provenance | Share of material claims in agent answers that resolve to a source artifact and precise location | ≥ 95% on golden set |
| No invented facts | Unsupported claims on the hidden-truth evaluation set | < 2%; every miss root-caused |
| Evidence / inference / unknown labeling | Answers explicitly label what is observed, inferred, contradictory, and unavailable | 100% of evaluated answers |
| Temporal correctness | Answers respect authoring/decision/effective time; superseded versions never presented as current | 100% on temporal test cases |
| Reproducibility | Any release regenerable from scenario config + seed + generator version; manifests and checksums verify | 100% of releases |
| Evaluation isolation | Hidden truth never supplied to the answering agent or used in tuning; mechanical check in the pipeline | Enforced, not sampled |

The guiding test, from the README: *an answer is trustworthy only when its
claims can be traced to evidence, its assumptions and inferences are visible,
its temporal context is respected, and unknowns remain unknown.* These
criteria are that sentence made measurable.

## 2. Non-goals

Explicitly out of scope — enforced at every phase gate:

- **Not a production system.** It is an architecture and evaluation workspace.
  No production data, ever.
- **Not a real-time OT/SCADA ingestion platform.** Historian/alarm summaries
  are evidence artifacts, not live feeds.
- **Not an autonomous agent framework.** This project builds the context
  layer agents consume; it does not define agency, planning, or tool use.
- **Not model training.** No fine-tuning; models are consumers of the
  context layer, not products of it.
- **Not a document repository or a generic vector database.** Retrieval
  serves evidence-grounded answers, not document search.
- **The synthetic corpus is not organizational history.** It must never be
  represented as factual about any real enterprise. All synthetic content
  carries synthetic provenance metadata (scenario, seed, generator, release).

## 3. Roles and decision rights

| Role | Responsibility | Held by |
|---|---|---|
| Maintainer | Approves releases, phase-gate sign-off, breaking changes to the semantic model or schemas, evaluation rubric changes | Hamid |
| Semantic layer owner | Ontology, taxonomy, SHACL shapes, mappings, competency questions | TBD — proposed: maintained in step with the LSC ontology work; changes follow that pipeline's governance (labels are presentation, slugs/IRIs are identity, SemVer per module) |
| Corpus / generator owner | Scenario configs, decision ledger, generators, validation | TBD |
| Retrieval / evaluation owner | Index, graph build, question sets, rubrics, hidden-truth harness | TBD |

Decision rules:

- **Additive changes** (new scenarios, new artifact types, new questions) are
  approved by the area owner.
- **Breaking changes** — URI or schema changes, removals, redefined meaning —
  require the maintainer's approval. The test for "breaking" is the same as in
  the ontology work: do existing queries and answers stay correct?
- **Versioning** follows SemVer per area: major = breaking, minor = additive,
  patch = wording/fixes. Deprecate with replacement pointers; never silently
  delete.
- **Nothing merges on assumption.** PRs carry reviewer notes; review is
  explicit, not implied.

## 4. Phases and milestones

**Phase 0 — Charter and semantic foundation** (current)
Charter approved; competency questions locked; ontology/taxonomy skeleton in
place; synthetic-data strategy finalized.
*Gate: maintainer approves charter and the question set.*

**Phase 1 — MVP corpus**
One business unit, limited asset/process scope, 10–20 decisions, 4–6 artifact
types per decision. Canonical hidden ledger built first; distributed evidence
artifacts generated from it; golden question set with expected evidence sets
and gold answers; hidden-truth evaluation harness runs green on the golden
set, including controlled ambiguity and contradiction cases.
*Gate: success criteria evaluated on the golden set; maintainer sign-off.*

**Phase 2 — Retrieval products**
Document index, semantic graph, metadata/catalog entries, vector
representations, and source-to-answer evidence links. Agent answers carry
claim-level citations and evidence/inference/unknown labels.
*Gate: provenance and labeling criteria met on an expanded question set.*

**Phase 3 — Scale and release discipline**
More scenarios, harder ambiguity, full release process: manifests, checksums,
release notes, validation results, controlled exports.
*Gate: reproducibility and evaluation-isolation criteria enforced
mechanically in CI.*

## 5. Dependencies and constraints

- **Cloudflare R2** holds all large generated data, document bundles, and
  graph exports (see `docs/strategy/cloudflare-r2-data-storage-and-agent-workflow.md`).
  Constraint: manifests and checksums make the store replaceable — the exit
  plan is to re-point the storage client at any S3-compatible store, not to
  redesign the pipeline.
- **GitHub** holds source, schemas, generators, and docs. Hidden evaluation
  truth is never committed.
- **Compute** for generation, validation, and graph builds: TBD — sized at
  the Phase 1 gate.
- **Constraint:** every synthetic artifact carries synthetic provenance
  metadata (scenario, seed, generator version, release). No unlabeled
  synthetic content anywhere in the pipeline.

## 6. Risks

- **Hidden-truth coverage.** The ledger may under-represent ambiguity and
  contradiction, making evaluation easier than reality. Mitigation: controlled
  ambiguity cases are required in Phase 1, not optional.
- **Semantic drift.** This repo's vocabulary diverging from the LSC ontology
  work it draws on. Mitigation: single ownership of the semantic layer;
  reference the ontology, don't fork it.
- **Evaluation gaming.** Tuning against visible questions. Mitigation: hidden
  question sets and mechanical isolation checks in the pipeline.
- **Scope creep into agent frameworks.** The most likely failure mode for a
  project this ambitious. Mitigation: non-goals enforced at phase gates.

## 7. Open decisions (for Hamid)

1. Final success-criteria targets (Section 1).
2. Named owners for the semantic, corpus, and retrieval/evaluation areas
   (Section 3) — or hold all three with the maintainer for now.
3. Whether the semantic layer lives here or is imported from the ontology
   workspace (recommendation: import, don't duplicate).
4. Timeline or "no dates, gates only" — the charter currently runs on gates.
