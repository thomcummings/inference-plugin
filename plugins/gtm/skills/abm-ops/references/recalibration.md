# Recalibration: monthly and quarterly

A target list decays: accounts go cold, others come into market, tiers ossify, and
Tier 1 creeps past its cap. Recalibration keeps the list honest. Tier rules, the
cap and promotion and demotion triggers come from `abm-strategy`
`references/tiering-and-selection.md`; list changes go through the one source of
truth set up by `abm-setup` (`references/list-source-and-sync.md`).

## Monthly recalibration (ABM owner, sales lead, marketing lead)
Inputs: the stage log, this month's signals, buying-group coverage, overdue next
steps, and the drift flags from the list routine.

1. **Tier 1 count and rank.** Within the cap? If not, rank and demote with reasons.
2. **Promote** Tier 3 (and Tier 2) accounts whose signals crossed the promotion
   trigger.
3. **Demote or retire** stalled accounts, with a reason each.
4. **Clusters.** Merge, split or rename; empty the "not sorted yet" cluster where
   you can.
5. **Stage velocity.** Accounts stuck in a stage longer than the agreed threshold.
   Each gets a play or a decision to hold.
6. **Buying-group coverage gaps** against the stage targets.
7. **Programs.** Keep, change or kill each one.
8. **List sync verified.** CRM tier property, segments, ad and visitor lists all
   match the source.

Output: a dated list of changes (account, from, to, reason, decider), written to
the list source, plus the open items with owners.

## Quarterly reset (leadership)
- Re-score the ICP (`icp` drift watch: are recent wins still the ICP we defined?).
- Reset "this quarter's wins".
- Set next quarter's stage-movement goals per tier, for marketing and sales.
- Review the pipeline and mindshare scorecards side by side; kill or change any
  program or event format that hasn't moved target accounts in two quarters.
- Start a new period-named tier property (for example `q2_target_tier`) so the old
  quarter's history survives.

## Rules
- Every change is logged with a date and a reason.
- A focus shift between sub-segments is a recorded decision, not a drift.
- Never re-tier from one week's noise: one hot week is a signal to review, not a
  promotion.
