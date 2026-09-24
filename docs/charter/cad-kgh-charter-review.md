# CAD-KGH Charter — Review

**Reviewed:** 2026-09-24 (v3.0 import), 2026-09-24 (v3.1)  
**Source:** `docs/charter/cad-kgh-project-charter.md` (v3.1)  
**Verdict:** v3.1 closes the identity and corpus questions. Ship it. Remaining issues are spec bugs and M0/M5 execution risks, not direction.

---

## v3.1 closed

| v3 finding | v3.1 |
|---|---|
| `LSC-A` / `LSC-B` collide with inventory regions | Gone. `authoring_system_id` (`AS-SPPID-01`, `AS-P3D-01`) ≠ `site_code` (`NORTH`, `SOUTH`, `WEST`). CI collision guard. |
| No ECE / corpus interface | §4: separate graph, feed via versioned snapshots + JSON-LD extracts + PROV-O. Merge and unlink both rejected. Correct. |
| Path B had no home in the scenario | WEST is a brownfield drawing-only site. H1 is now NORTH/SOUTH vs WEST. |
| Isolation finder as implicit authority | Extracts carry `confidence` / `derivation`; WEST is explicitly reconstructed. |
| SQL in YAML; missing `key: PnPID`; Gephi | Excerpt is declarative. Gephi dropped. |
| H5 (license) unmeasured; corpus link unasked | H5 is now corpus-trace. H6 is license. M5 has contract-test exit criteria. |
| Open Q: feed vs parallel | Decided: feed via interface. |

The three-identifier model (tag / FLOC / equipment number) is the right one. Topology hangs off FLOCs; serialized kit moves with `INSTALLED_AT {from,to}`. That is how you keep an isolation decision valid after a pump swap.

---

## Spec bugs — fix in the next pass, before anyone implements §8

### 1. FLOC format string ≠ examples

§3.1 format is `{SITE3}-{UNIT}-{CLASS}-{SEQ}{TRAIN}` → `NTH-110-P-101A`.  
Every example is `NTH-110-P-101-A` (hyphen before train). Pick the hyphenated form and change the format string.

### 2. NORTH normalizer does not produce the documented FLOC

```
P-1101A  +  ^(?P<cls>…)-(?P<unit>\d{3})(?P<seq>\d)(?P<train>…)$
         +  NTH-{unit}-{cls}-{seq:03d}{-train}
         =  NTH-110-P-001-A
```

Rule 7 says `P-1101A` → `NTH-110-P-101-A`. Seq is one digit in the regex, three digits in the example. SOUTH (`21-P-101-A` → `STH-210-P-101-A`) is consistent. NORTH is not. Freeze a golden triple `(tag, site, asset_ref)` set in M1 or the normalizer will be fiction.

### 3. Isolation Cypher uses `LOCATED_ON`; the model dropped it

§7.3 has `CONNECTS_TO` onto valves. §7.4 still walks `[:CONNECTS_TO|LOCATED_ON|CONTINUES_AS*1..15]`. Either put `LOCATED_ON` back or delete it from the query. Do not leave both.

### 4. WEST has no `uid` scheme

`uid = hash(authoring_system_id, source_id)` and `authoring_system_id` is null for WEST. Need `hash("PATH-B", drawing, handle)` or a synthetic `AS-LEGACY-WEST` so re-parses stay stable.

---

## Still open (don't block the charter; do block M0/M5)

### Repo identity

§13 is still a standalone `cad-kgh/` tree. This repo is `enterprise-context-engineering`. Same as v3: packages land here (or you split deliberately). The placement note on the charter states that; §13 should say it too.

### NORTH/SOUTH/WEST are regions in the inventory, not plants

The knowledge-source inventory has multiple sites per region (NORTH: IKE, AJA, OJO, EPE; SOUTH: BAD, LEK; WEST: ABK, IBN, …). v3.1 treats each region as one P&ID `site_code`. Fine for a learning plant **if you say so** — “one representative unit per region.” Otherwise the asset master and the inventory will fight.

### M5 exit depends on a corpus that is out of scope

§2.2: corpus is a separate project. §10.1: M5 fails unless three corpus decisions resolve to snapshots. Stub those fixtures in *this* repo (`tests/contract/`) or M5 is blocked on a repo that does not exist.

### Snapshot determinism needs a serialization ADR

`snapshot_id = sha256(canonical graph serialization)` will drift on node order, float precision, and volatile props (`confidence` timestamps). M5 “same revision → same snapshot_id” is otherwise unmeetable.

### Copyleft still Low/Low

pyDEXPI is AGPL and still on the M5 path. Neo4j CE is GPL. LibreDWG is GPL and still in the stack. Unchanged from v3. M1 ADRs: isolate, one default graph store, DXF-only until LibreDWG is justified, project license.

### Scope still fat

Graph-RAG is optional and off the milestone path (good). Dual graph stores are still in the stack table. Sequence that tests the new H1/H5: NORTH extract → publish one isolation extract → WEST baseline → SOUTH join. Don’t compose AGE and Neo4j in M0.

---

## Smaller nits

| Item | Note |
|---|---|
| H3 “identical query results regardless of source” | Only NORTH vs SOUTH. WEST is a different derivation. Say so. |
| Line / pipe-run FLOCs | Equipment, valves, instruments REALIZE a FLOC. Lines? Spec-break extracts need a stable line identity. |
| Bitemporal | M5 says “bitemporal validity.” Define transaction time (load) vs valid time (drawing issue / revision) or you will hash the wrong clock. |
| `unmapped_policy: report` | Still not fail-vs-continue. Pick: land `:MappingException` and continue, except collision guard which already fails CI. |
| Success metrics | Still generator-relative. Footnote is there; table header should say “vs generated ground truth.” |
| Path B snapping | Dropped from the risk table while WEST became a first-class site. Put it back. |
| Isolation finder | Still a demo, not an operational boundary. The extract is evidence, not a permit. |

---

## Fit to ECE

| Principle | v3.1 |
|---|---|
| Evidence before fluency | Source-first + WEST as the honest baseline. Better than v3. |
| Claim-level provenance | Extracts + PROV-O `Decision → Extract → Snapshot → SourceRecord`. This is the missing layer. |
| Time-aware | Snapshots immutable; `as_of` on the extract API; `INSTALLED_AT {from,to}`; `floc_alias`. |
| Evidence / inference / unknown | `derivation` + `confidence` on WEST. SOUTH leftovers → `:MappingException`. |
| Separate truth from retrieval | Ground truth still eval-only. Keep it that way. |
| Governance | Isolation extract ≠ isolation authority. State that on the extract schema. |
