# Competency Questions — Enterprise Context Engineering

**Status:** Proposed
**Purpose:** Define what a competency question is here, the template it follows, and how the set is governed. The charter's Phase 0 gate locks this set.
**Related:** [Shared Technical Foundation](../../docs/architecture/shared-technical-foundation.md) (semantic standards baseline), [Project Charter](../../docs/charter.md) (Phase 0).

## What a competency question is

A competency question is a question the semantic layer must make answerable. The set is the contract the ontology has to satisfy:

- Every ontology design decision (class, property, relation) must trace to at least one question.
- Every question must be answerable from the corpus evidence and graph, and must map to an evaluation case.

Questions are written in the stakeholders' own words, not in SPARQL or query syntax. Translation into queryable form happens when the ontology exists to answer them.

## The seed set

The [core questions in the repository README](../../README.md#core-questions) are the seed set. They arrive as unstructured prose; instantiate each one as a `CQ-` record below during Phase 0.

## Template

Each question is written against this template:

| Field | Meaning |
|---|---|
| ID | Stable identifier, `CQ-<area>-<nn>` (for example `CQ-kpi-01`). IDs are never reused. |
| Question | The stakeholder's question, one sentence, plain words. |
| Answerable-by | The ontology classes, properties, and relations that make it answerable. Empty until the ontology skeleton exists. |
| Evidence types | The artifact or record types that can support the answer (work orders, email threads, KPI definitions, historian windows, and so on). |
| Evaluation | How an answer is scored: gold answer, expected evidence set, or rubric reference. |
| Status | `draft`, `locked`, or `deprecated → CQ-<id>` (replacement pointer, per the deprecation rule in the charter). |

Records live as individual files named by ID, or one table per area file. Pick one format per area and keep it.

## Governance

- **Additive** questions (new question, new area) are approved by the semantic layer owner — see the charter's roles table.
- **Breaking** changes (redefined meaning of an existing question, removal) require the maintainer's approval, same as any semantic-model change.
- The Phase 0 gate locks the set; after lock, changes go through PR review with a rationale for re-opening the gate.
