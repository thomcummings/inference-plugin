# The target list: one source of truth

Lists multiply. A sheet, a CRM property, a dashboard and an agency each end up holding a slightly different list, and agencies model different list sizes. Pick one source and sync outward. Tiering rules and the cap are in `abm-strategy` `references/tiering-and-selection.md`.

## One source, synced outward

Pick one source of truth for list membership and tier (a sheet or a CRM list), then sync outward:

```
List source (sheet, one tab per tier, or a CRM list)
   └─ sync script or routine →  CRM company property "target tier (period)"
                             →  CRM segments per tier
                             →  web visitor tool lists
                             →  ad platform matched audiences
                             →  ABM command center accounts
```

Rules:
- Name the tier property with its period (for example `q1_target_tier`), so history survives re-tiering.
- Never hardcode the list in a script. If the source read fails, stop.
- Where an account exists in the CRM, the CRM is the source of truth for its facts. The ABM hub only enriches it.
- Log every add, remove and re-tier with a date and a reason.
- Agree one list with any agency before spend, and check their audience matches the source.

## Drift checks
A routine or a person can flag drift: accounts that no longer match the ICP, ICP-fit accounts missing from the list, and differences between copies of the list. The monthly recalibration that acts on it is `abm-ops`.
