# Health check: is our ABM working?

Read a running programme against its measurement spec (`abm-strategy`
`references/measurement.md`) and its failure modes (`abm-strategy`
`references/failure-modes.md`). Lead with the verdict: healthy, drifting or
broken, the one thing to fix, and who fixes it.

## What to read
| Area | Healthy looks like | Warning signs |
| --- | --- | --- |
| Outcome | Tier 1/2 accounts moving at least a stage per quarter, by tier | Movement only in Tier 3, or only from self-serve |
| List | One source, synced; Tier 1 within cap; monthly changes logged | Copies disagree; Tier 1 over cap; no changes in a month |
| Ownership | Every Tier 1 account has an accountable owner, a dated next step and a target stage | Blank owners; overdue steps trending up |
| Stages | Stages locked; confirmations logged; velocity tracked | Accounts stuck past threshold with no play or hold decision |
| Buying groups | Coverage meets the stage targets | Single-threaded accounts at Evaluating or Buying; procurement found at signature |
| Rhythm | Weekly meeting held, ending in top actions per function; marketing in the room | Meetings skipped; actions not recorded; marketing absent |
| Signals | Coverage reported; proposals reviewed by owners | Reports with no coverage line; unknowns shown as zero; ignored chat posts |
| Channels | Each channel has an ABM goal and owner; pipeline and mindshare scored separately | Content judged by traffic; events not logged by account; paid reach not split by target accounts |
| Measurement | Account movement is the headline; volume labelled as context | MQLs or sign-ups creeping back as the headline |

## Evidence
Name the evidence tier. Read the stage log, the list source and its sync status,
the command center, the last four weekly notes and the last recalibration. Where
something can't be seen, say so; don't infer it's fine.

## Output
- Verdict and the single biggest fix (max ~4 lines).
- The table above filled in, with evidence per row.
- Up to five fixes, each with an owner and a date.
- Anything that needs a design change goes back to `abm-strategy` (for example a
  stage model that doesn't fit, or a tier rule that keeps failing).
