# Registry row

Slug: `ops/registry/[name]`. One row per agent, skill or routine the team uses,
whatever platform runs it. On Notion it's a database row; on git a file with
this frontmatter; on Drive a row in the `registry` tab of the index Sheet.

```yaml
---
name: weekly-competitor-digest      # kebab-case, permanent
kind: routine                       # agent | skill | routine
what_it_does: "Monday summary of competitor moves for the PMM channel"
owner: "[NEEDS DECISION]"
status: trial                       # draft | trial | active | degraded | dormant | retired
review_date: 2026-12-27
where_it_runs: "GitHub Actions, Mon 08:00 Europe/London"
reads: [infra/start-here, core/competitive/landscape-map]
writes: [memory/runs, memory/reports]
instructions_live_in: "skills/competitive-scan"
uses: [competitive-scan]
---
```

## Body

- **Purpose:** the useful result, and who uses it.
- **Boundaries:** what it must never do.
- **No-change behaviour:** routines write a run note and post nothing.
- **Trial:** what "working" means, and the result at the review date.
- **History:** dated changes, newest first.

## Rules

- New rows enter at `trial` with a review date. A trial past its date with no
  review becomes `dormant`.
- Instructions hold no copy of store content: they name the rows to read (`reads`), so they can't drift.
- Instructions live in one place, named in `instructions_live_in`. A scheduler
  holds only the trigger and a short prompt that loads them.
- A routine runs exactly one skill and has one executor.
- An agent's routines are the routines whose owner is that agent; don't list
  them on the agent row, so they can't drift.
- Adding a cadence to the prose creates no schedule and no permission. A new
  cadence is a new routine row.
- Record laptop jobs honestly. They write no run notes, so their silence proves
  nothing.
