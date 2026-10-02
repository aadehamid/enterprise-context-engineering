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
| Semantic layer owner | Ontology, taxonomy, SHACL shapes, mappings, competency questions | TBD — proposed: the Downstream Oil and Gas Ontology (from EPM) is the authoritative domain ontology; this project would import it and follow its governance (labels are presentation, slugs/IRIs are identity, SemVer per module). Pending open decision 3. |
| Corpus / generator owner | Scenario configs, decision ledger, generators, validation | TBD |
| Retrieval / evaluation owner | Index, graph build, question sets, rubrics, hidden-truth harness | TBD |

Decision rules:

- **Additive changes** (new scenarios, new artifact types, new questions) are
  approved by the area owner.
- **Breaking changes** — URI or schema changes, removals, redefined meaning —
  require the maintainer's approval. The test for "breaking" is the same as in
  the Downstream Oil and Gas Ontology: do existing queries and answers stay correct?
- **Versioning** follows SemVer per area: major = breaking, minor = additive,
  patch = wording/fixes. Deprecate with replacement pointers; never silently
  delete.
- **Downstream-originated proposals.** When PPC (or another downstream
  consumer) finds a generic context-engineering gap, the path is: proposal →
  ECE review → contract/ADR update → ECE release → downstream dependency
  update. Downstream projects must not silently redefine generic ECE concepts.
  Gaps in downstream business meaning go to EPM instead.
- **Nothing merges on assumption.** PRs carry reviewer notes; review is
  explicit, not implied.

## 4. Phases and milestones

**Phase 0 — Charter and semantic foundation** (in progress)
Exit conditions: charter approved; competency questions locked;
ontology/taxonomy skeleton in place; synthetic-data strategy finalized.
*Gate: maintainer approves the charter and the question set.*

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
*Gate: provenance and labeling criteria met on an expanded question set, and
hidden truth verified isolated from every store actually on the retrieval
path, including any shared platform store.*

**Phase 3 — Scale and release discipline**
More scenarios, harder ambiguity, full release process: manifests, checksums,
release notes, validation results, controlled exports, and versioned ECE
contract outputs that downstream consumers can pin.
*Gate: reproducibility and evaluation-isolation criteria enforced
mechanically in CI, including on any shared-platform stores in use.*

## 5. Dependencies and constraints

- **Cloudflare R2** holds all large generated data, document bundles, and
  graph exports (see `docs/strategy/cloudflare-r2-data-storage-and-agent-workflow.md`).
  Constraint: the storage client must go through the S3 API (boto3) so the
  endpoint stays swappable to any S3-compatible store. The exit plan is a
  design requirement to be validated in Phase 1 — the R2 strategy doc
  specifies the Cloudflare endpoint, not the migration procedure.
- **GitHub** holds source, schemas, generators, and docs. Hidden evaluation
  truth is never committed.
- **Downstream Oil and Gas Ontology (from EPM)** — the same artifact earlier
  called the "LSC ontology work"; Lagos Specialty Chemicals (LSC) remains this
  repo's worked-example scenario. **Proposed dependency rule** (pending open
  decision 3): import it, do not fork it. ECE would add only generic context
  semantics (EvidenceItem, Artifact, SourceAssertion, Claim, Decision,
  Constraint, Outcome, provenance).
- **Shared technical foundation.** Reusing the platform components described
  in `docs/architecture/shared-technical-foundation.md` is an implementation
  choice, not a scope expansion. A technology enters ECE only when an ECE
  requirement justifies it. Shared infrastructure must not weaken hidden-truth
  isolation.
- **PPC is an external proving-ground consumer, not an ECE runtime
  dependency.** ECE builds and validates its artifacts without PPC. ECE
  intends to publish versioned contracts (evidence-item schema, artifact
  manifest, source-assertion/claim model, decision-dossier schema, provenance
  and temporal-context models, evidence/inference/contradiction/unknown
  vocabulary, hidden-truth isolation rules, evaluation rubric); once
  published, PPC release manifests record the ECE versions they consume. None
  of these is published yet; timing is open decision 5. See
  `docs/architecture/epm-ece-ppc-operating-model.md`.
- **Compute** for generation, validation, and graph builds: TBD — sized at
  the Phase 1 gate.
- **Constraint:** every synthetic artifact carries synthetic provenance
  metadata (scenario, seed, generator version, release). No unlabeled
  synthetic content anywhere in the pipeline.

## 6. Risks

- **Hidden-truth coverage.** The ledger may under-represent ambiguity and
  contradiction, making evaluation easier than reality. Mitigation: controlled
  ambiguity cases are required in Phase 1, not optional.
- **Semantic drift.** This repo's vocabulary diverging from the Downstream Oil
  and Gas Ontology (from EPM) it draws on. Mitigation: single ownership of the
  semantic layer; reference the ontology, don't fork it.
- **Evaluation gaming.** Tuning against visible questions. Mitigation: hidden
  question sets and mechanical isolation checks in the pipeline.
- **Scope creep into agent frameworks.** The most likely failure mode for a
  project this ambitious. Mitigation: non-goals enforced at phase gates.
- **Downstream coupling.** PPC-specific concepts or infrastructure leaking
  into ECE core, or PPC redefining generic ECE concepts. Mitigation: the
  proposal path in Section 3, versioned contracts, separate buckets/releases/
  hidden-evaluation access, and a code-placement rule (code that makes sense
  without PPC's fictional company belongs in ECE).

## 7. Open decisions (for Hamid)

1. Final success-criteria targets (Section 1).
2. Named owners for the semantic, corpus, and retrieval/evaluation areas
   (Section 3) — or hold all three with the maintainer for now.
3. Whether the semantic layer lives here or is imported from the Downstream
   Oil and Gas Ontology (from EPM) (recommendation: import, don't duplicate).
   That ontology is the same artifact earlier called the "LSC ontology work";
   LSC remains this repo's worked-example scenario and is separate from PPC.
4. Timeline or "no dates, gates only" — the charter currently runs on gates.
5. When the first versioned set of ECE contracts is published for downstream
   use (proposed: Phase 3, with release discipline).
