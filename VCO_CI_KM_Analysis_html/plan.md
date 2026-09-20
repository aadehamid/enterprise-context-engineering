# Plan: Downstream VCO Lookback/Backcasting & CI Knowledge Management — Deep Research & Structured Analysis

## Objective
Produce a structured, detailed analysis (report) for a downstream refining & marketing organization covering:
1. Downstream value chain & VCO context
2. Current lookback & backcasting practices in industry
3. Systemic shortcomings/gaps limiting effectiveness (with concrete downstream examples)
4. COMPANY's CI/KM problem framing (interpretation)
5. CI-focused KM & context management requirements (no solution architecture)
6. Conceptual link: KM/contextualization ↔ VCO lookback effectiveness

Constraint: map the problem space — do NOT propose specific tools, vendors, or architectures.

## Stage 1 — Deep Research (skill: deep-research-swarm)
Route B (focused search with clear dimensions). Deploy parallel explore/research sub-agents:
- R1: Downstream value chain structure + VCO practice (LP, APS, S&OP, network/pricing optimization; industry references: Solomon, AP-Networks, Aspen PIMS/ Petroleum Scheduler usage patterns, S&OP in refining)
- R2: Lookback practices — margin decomposition/variance analysis, post-audit, reliability lookbacks, supply chain/OTIF reviews, commercial retrospectives; tooling (BI, historians, ERP, CMMS, TMS)
- R3: Backcasting practices — net-zero/energy transition backcasting, refinery of the future, capital/decarbonization roadmaps; integration with strategic planning
- R4: Shortcomings/gaps — data fragmentation, weak closed loop between lookback and planning models, KPI misalignment, causal inference weakness, organizational/tribal knowledge loss; lessons-learned system failures in process industries
- R5: Knowledge management & context management in process industries — lessons learned standards (API RP 754 / 75, CCPS, NASA LLIS as analog), knowledge quality tiering, governance/lifecycle, AI-readiness of KM, decision capture/decision records
Output: validated research brief per dimension saved to /mnt/agents/output/research/*.md with citations.

## Stage 2 — Synthesis & Writing (skill: report-writing)
Load report-writing SKILL.md. Design outline mirroring the 6 sections of the brief; write full report with sub-agents per chapter batch; integrate research citations; concrete downstream examples in §3.
Output: /mnt/agents/output/VCO_CI_KM_Analysis.agent.final.md

## Stage 3 — Formatting (skill: docx)
Convert final markdown to .docx deliverable.
Output: /mnt/agents/output/VCO_CI_KM_Analysis.docx
