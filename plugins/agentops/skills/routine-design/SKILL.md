---
name: routine-design
description: >-
  Use when a recurring or event-triggered job is being set up, changed or
  questioned on any platform: a scheduled brief, digest, sync, review, watcher
  or webhook-driven task, or "can you run this every Monday". Decides whether
  it is a routine at all (versus a to-do, a small throwaway job, a skill or an
  agent), checks for a duplicate, then designs a short routine contract, names
  or drafts its method skill and writes the thin native job text. Also use to
  review a routine that has drifted or gone quiet, or to retire one. Drafts and
  proposes; never switches a job on without approval.
---

# Routine Design

Design the routine, not the cron job.

> A routine is recurring or event-triggered work with a defined output, one
> accountable owner and exactly one place it runs. Its contract is a short
> file; its method is a skill; the platform holds only a trigger and a short
> prompt that points at both.

Keeping the logic out of the scheduler is the whole point. A long prompt
pasted into a cron job drifts, can't be reviewed and dies with the platform.
A contract plus a skill can move to any platform that can run a skill on a
schedule.

## Modes

| Mode | Reach for it when |
| :--- | :---------------- |
| **design** | Someone wants something to run on a schedule or on an event |
| **reject** | The request isn't a routine: a to-do, a small throwaway job, a skill or an agent |
| **review** | A routine's output has stopped, drifted, or it's time to check it still earns its place |
| **retire** | The routine should stop: switch the job off, keep the record |

Not for a task you want done once, now, or for designing a persistent agent
(`agent-design`) or the full content of a method skill (`skill-design`).

## 0. Find the routines folder

Routines need one place where their contracts live, so you can see every
routine at a glance. Look for an existing folder (`routines/` in the repo or
notes vault the user works from). If there isn't one, recommend creating
`routines/` with one subfolder per routine and an `index.md` listing them.
Read the index before asking anything. Never invent routines, owners or
platforms that aren't there.

## 1. Interview

Ask one to three open questions at a time, each with a recommended answer,
and wait. Don't ask what the folder or the conversation already answers. Mark
genuine unknowns `[NEEDS DECISION]`. A full contract from one sentence of
intake is a failed interview, not a shortcut.

## 2. The gate: is this a routine?

A routine needs **all three**:

- **A trigger:** a schedule or an event, so it runs without being asked.
- **A defined output** someone uses: a brief, a report, an updated file, a
  decision prompt.
- **Durability:** it's meant to keep running, and someone would notice if it
  stopped.

If it fails, recommend the lighter home and stop:

| The need is really | Home |
| :----------------- | :--- |
| A to-do or a one-off reminder | The user's task tracker |
| A small watcher with an end date ("tell me if this price drops") | A **throwaway job** on the platform, unregistered: it ends on its own, delivers only to the person who asked, writes nothing important and contacts no one. Register it if it's still running after four weeks |
| A method someone runs on demand | A **skill** (`skill-design`) |
| A standing role with judgement across many tasks | A **persistent agent** (`agent-design`) |

"This is a throwaway job, not a routine" is a good outcome, not a failure.

## 3. Duplicate check

Compare against the index **by purpose, not name**. Two morning briefs are a
duplicate even if one is called `daily-note`. For each near match choose
explicitly: extend the existing routine, replace it (and retire the old one),
or say why both should exist.

## 4. The contract

Fill one section at a time. If a section needs more than about five lines,
the scope is wrong: split the routine or move detail into the method skill.

```markdown
---
id: <routine-id>
status: draft | active | retired
owner: <person or agent accountable for the output>
runs-on: <the one platform or instance that runs it> | none
revision: 1
---

# <Routine name>

## Outcome
Purpose (the useful result, for whom):
Output (what a run produces):
Noop (what a run that finds nothing does):

## Trigger
Schedule: human form + cron + IANA timezone (check which timezone the
  platform's scheduler uses)
or Event: source, event, filter, dedupe key

## Method
Skill: <existing skill> | <new skill, drafted> | inline (10 lines at most)
Inputs for one run:

## Access
Reads:
Writes: the output location and declared state files only
Connectors and operations: (name the operation, not just the product)
Must never:

## Delivery
Delivers to:
Report: filename pattern and where it's kept
On failure:
Stays quiet when:

## History
- <date>: created
```

Rules for the contract:

- **Skill first.** Use an existing skill if one does the job. Otherwise draft
  a short method skill with Inputs, Steps, Output and Quality bar, and no
  schedules, channels, platforms or permissions in it, so it works anywhere.
  Keep steps out of the contract; it names the skill and the inputs.
- **Every run writes a report, noops included,** so silence can be told apart
  from failure. Event routines whose filter rejects the event write nothing.
- **One place it runs.** Pick the platform last, and only one that can reach
  everything in Access. If none can, say what's missing rather than picking
  the closest. Test with a manual or dry run, never a second scheduled copy.
- **Risky access stays off by default.** Sending to people outside the team,
  spending money, deleting or publishing needs the owner's explicit yes,
  recorded in the contract.

## 5. The native job

The platform's job holds only the trigger, the delivery setting and a short
prompt like this:

```text
Run the <routine-id> routine. Read its contract at routines/<routine-id>/README.md
and follow it, using the <skill> skill for the method. Write the report where
the contract says, including when there is nothing to report.
```

Show the contract, the method skill (named or drafted), the job prompt and
the exact steps to create the job. Write files only after the user approves.
Create the job **switched off**, or hold it uncreated if the platform can't
create a disabled job, until the user says go. Then set `status: active` and
add the routine to the index.

## 6. Review and retire

**review.** Compare the contract with the live job: trigger, timezone,
delivery, access, and the prompt (is it still only the short pointer?). Check
the last report date against the schedule. Recommend exactly one: **keep**,
**revise** (with the specific change), **move** to another platform, or
**retire**.

**retire.** Propose switching the job off. Once the user confirms it's off,
set `status: retired`, `runs-on: none`, add a History line with the reason and
update the index. Keep the folder and its reports.

## Pitfalls

1. **Designing the cron job instead of the routine.** Start from the outcome,
   not the schedule or the prompt.
2. **Logic in the native prompt.** The platform holds a trigger and a pointer;
   the method is a skill.
3. **Steps in the contract.** A contract that restates the method drifts from
   the skill. Name the skill.
4. **Two copies running.** Trials use dry runs, never a second scheduled job.
5. **Registering a tiny watcher.** Paperwork for a price alert trains everyone
   to skip the routines folder.
6. **Switching it on without approval.** Drafting is this skill's job;
   enabling the job is the user's decision.

## Checklist

- [ ] Mode named
- [ ] Gate applied; lighter home recommended where it failed
- [ ] Duplicate check done by purpose against the index
- [ ] Contract complete, or open items marked `[NEEDS DECISION]`
- [ ] Method is a named skill, not steps in the contract
- [ ] One platform chosen last, and it can reach everything in Access
- [ ] Native job prompt is only the pointer; the job is held off pending approval
- [ ] Nothing written or switched on without the user's approval

## Method lineage

Part of the Inference agentops set with `skill-design` and `agent-design`:
each one decides first whether the need belongs to it at all.
