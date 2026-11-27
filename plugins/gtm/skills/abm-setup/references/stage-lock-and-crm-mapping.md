# Locking stages and mapping them to the CRM

The stage model itself (six stages, entry, exit, the job, and how to define Aware) is in `abm-strategy` `references/funnel-stages.md`. This file covers making it the team's and wiring it into their systems.

## Mapping to the CRM and to sales views

Sales will often run its own pipeline view with more granular deal stages. Don't fight it: map it. Example mapping pattern:

| Account stage | Sales pipeline view | CRM deal stages (example) | Target-status field (if a list sheet has one) |
| --- | --- | --- | --- |
| Unaware | Prospecting | – | Not contacted |
| Aware | Awareness | – | Intro done |
| Engaged | Qualified | Early deal stages (1–3) | In contact |
| Evaluating | Technical evaluation | Mid deal stages (4–5) | Testing / SQO |
| Buying | Proposal / negotiation | Late deal stages (6–7) | – |
| Customer | Closed won → Customer, Expansion | Won | Customer |
| (Hold) | Hold | Any, paused | Paused |

Rules:
- **The board suggests and the owner confirms.** The command center suggests a stage from the target-status field and the open deal stage. An owner-confirmed stage overrides the suggestion and is logged with a date.
- When sources disagree, a later deal stage beats an earlier list status.
- Write the mapping into the Glossary. Unmapped statuses, such as an "intro done" with no stage, must be listed explicitly, not silently dropped.
- Log every stage change (account, from, to, date, who or what) so stage movement can be counted.

## Locking the definitions

At the workshop, show each stage as a card with Entry, Exit and Job, and mark each one "agreed" when the room accepts it. Unlocked stages are a named next step with an owner, typically the ABM owner plus a sales lead. Don't build KPI reporting on unlocked stages.

## Also lock
- **Tier 1 vs Tier 2 criteria**, written the same day, next to the tier cap.
- **The ICP rubric** in one canonical place (via `icp`).
- **The glossary:** target account, ABM stage, tier, PQL, core market, deal origin (definitions in `abm-strategy` `references/measurement.md`).
