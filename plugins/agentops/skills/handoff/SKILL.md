---
name: handoff
description: >-
  Package working context so a fresh session, another agent or another platform can pick
  up cleanly. Invoke as "/handoff [what the next session is for]", or on "write a
  handoff", "hand this off", "brief another agent", "running low on context", "wrap this
  up for next time", or a long session ending mid-task; and on "pick up the handoff" /
  "continue from [project]" to resume. Two shapes: a rolling session handoff
  (`_HANDOFF.md`, one per project, overwritten) and a self-contained task brief
  (`BRIEF-[task].md`) with a mandatory close-out. Handoffs are scaffolding, not knowledge:
  lean, pointer-based, tailored to the next job, and archived when done. Not for durable
  project docs, stable facts, client deliverables, or routing and assigning work.
---

# Handoff

A handoff bridges one working session to the next. The governing idea: **it's transient working state, not knowledge.** Handoffs go stale within days but look authoritative, so a stale one makes the next session act on dead state. Keep them lean, tailored to the next job, and close them out.

Four rules:

- **Point, don't repeat.** Link the tracker issue, the files, the commits and the decision notes instead of restating them. A long handoff means a durable doc is underpowered; promote into it instead.
- **Tailor to the next job.** `/handoff <purpose>` names what the receiving session will do. Include what that job needs and nothing else.
- **Package, don't orchestrate.** A handoff never routes work, assigns it, creates a commitment, or edits canonical records. It describes; the receiving agent and the user decide.
- **Follow the workspace's rules.** If the workspace has a schema or a protected system folder, follow it. Prefer archiving to deleting.

## Pick the shape and the place

| Next reader | Shape | Where it goes                                                                                                                                                      |
| -------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The same platform, the next session, soon | paste-ready handoff in chat | the chat; a temp file outside the shared workspace if it's long                                                                                                               |
| Ongoing work in one project | rolling session handoff, `_HANDOFF.md` | next to that project's work, overwritten each time                                                                                                                 |
| Another agent or platform, one discrete task | task brief, `BRIEF-<task>.md` | next to the project it serves; if it serves no single project (estate or infrastructure work), `inbox/handoff/YYYY-MM-DD-<task>/` with any payload files beside it |

Another platform can only read what's in the shared workspace, so cross-platform briefs go there; the close-out keeps them from lingering. No dated variants of a rolling handoff: if an audit trail is wanted, that's a `_log/`. Standardise on HANDOFF (rolling) and BRIEF (task).

## Session handoff structure

Lean. Cut anything the next session can get from the README; carry only what's in motion.

```markdown
---
type: handoff-prompt
status: live
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [handoff, <domain>]
related_to: ["[[README]]"]
---

# Handoff: <project>

**Next session is for:** <the purpose given to /handoff>
**Where we are:** <1–2 sentences>

## State
**Done:** <only what's load-bearing for what's next>
**In flight:** <what's half-finished, and where it sits>
**Next actions:** <ordered, concrete>
**First action:** <the exact first thing the next session should do>

## Blocked or waiting
<blockers, and approvals needed from the user. Empty is fine.>

## Settled (don't reopen)
<decisions and constraints specific to this work, each with a pointer to where it was decided>

## Suggested skills
<skills the next session should load, by namespaced ID, and why>

## Pointers
<Tracker issues, files, commits, decision notes. Pointers, not summaries.>
```

## Task brief structure

Self-contained: a cold agent executes from this file alone. Don't fabricate; mark gaps as gaps.

```markdown
---
type: handoff-prompt
status: live
created: YYYY-MM-DD
tags: [handoff, <domain>]
---

# Brief for <agent or platform>: <task>

<One paragraph: what this is for and who approved it.>

## Context
<Only what the task needs, as pointers: tracker issue, files, commits, decisions.>

## Approved
<Exactly what the user approved for this task: named writes, pushes, PRs, job changes.
Anything not listed here still needs asking.>

## Steps
<Numbered. Each step says what to do and how to verify it.>

## Output
<Exactly what the result must contain, and where it goes.>

## Suggested skills
<Namespaced skill IDs, and which step each serves.>

## First action
<The exact first command or read.>

## Report back
<What to tell the user, and how briefly.>

## Close-out
<Set `status: archived` in this brief when done, and say so in the report. Name who
moves the folder to `archive/YYYY/briefs/` if the executing agent can't.>

## Don't
<The do-not-touch list.>
```

**The Approved section is binding in both directions.** The receiving agent may do what it lists without asking again, and must ask for anything it doesn't list. A brief can only record approvals the user actually gave in the session that wrote it.

## Close-out

A handoff written but never closed out is the default failure. Closing it out is half the job.

**Task briefs** must end with a Close-out section. The executing agent sets `status: archived` when the task is done and reports it. Whoever next works in the workspace moves an archived brief's folder to `archive/YYYY/briefs/`. The writer checks on the next session that an old brief was closed.

**Session handoffs**, on resume:

1. **Promote durable learnings out** to their canonical home (README/CONTEXT, a `decision` note, a resources folder, or the memory inbox).
2. **Reset the rolling file:** rewrite `_HANDOFF.md` to the new current state and bump `updated`. Overwrite, don't append.
3. **If fully done,** set `status: archived` and say so in your reply.

## When not to use

Durable project knowledge → README/CONTEXT. Stable facts → a resources folder or memory. A repeatable workflow → a skill. Recurring work → a routine (`routine-design`). Assigning or tracking work → the issue tracker. A client deliverable → edit-on-approval, not a handoff.
