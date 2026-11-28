---
name: relay-retro
description: "Review how an owner and their agents have been working together over a period: read the chat, threads, saved rules and skills, find the patterns with evidence (rules repeated or broken, friction, what worked), and deliver a short ranked set of changes, skills or playbooks to formalise, and transferable learnings. Use for 'how are we working', 'retro', 'relay-retro', 'what should we change in our process', or monthly. Analysis only: proposes, never changes instructions, memory, skills or code."
---

# Relay retro

A retrospective on the working relationship, not the product. Run it monthly, or
when the owner feels friction. It turns scattered irritations into a few changes
with evidence, and the changes into skills the owner can carry to other work.

## 0. Scope

Agree the window (default: since the last retro, or 30 days). Read the previous
retro, if any, and check which of its picks happened.

## 1. Gather

Read, in this order, and note dates and the owner's own words:

1. **The owner's messages** across the project chat in the window (all of them;
   page through, don't sample). Agent messages only where they explain an
   incident.
2. **Saved rules** (memory, feedback files, project instructions): each with its
   date and the reason it was written.
3. **The thread list**: how many, states, how long they ran, what was resolved
   and by whom.
4. **The skills in use** (the relay loop) and the routines that run on a schedule.
5. Cost signals the owner has mentioned (usage, limits hit, slow runs).

Use a script to page and filter; keep only quotes and counts in context.

## 2. Find the patterns

Look for, each with dated evidence:

- **Rules repeated or broken:** the same ask made twice or more; a saved rule
  followed by the same complaint. These are candidates for a check, not more
  words.
- **Friction:** waiting (tests, merges, the owner as bottleneck), lost context
  ("which thread?"), rework (built before shown), cost surprises.
- **What works:** structures that removed a whole class of complaints. Say why.

Count things (messages, threads, repeats). A pattern needs at least two dated
instances; one is an anecdote.

## 3. Write it

One document, readable in five minutes:

1. **Lead and summary:** five bullets, the answer first.
2. **Keep doing:** a table: practice, since when, evidence.
3. **Ranked recommendations:** for each, what, why (with quotes and dates),
   effort S/M/L. Prefer mechanisms (checks, schedules, skill steps) over new
   prose rules.
4. **Formalise:** candidate skills and playbooks: name, what it does, what it
   comes from, effort. Check the existing skills first and propose edits before
   new ones.
5. **Transferable learnings:** short numbered list the owner can use beyond this
   project.
6. **Sources and limits:** what was read, what wasn't.

Plain words, no internal codes, S/M/L not time.

## 4. Hand over

Post the five bullets with a link. Then let the owner pick. Implement only what
they pick, each in the right place (instructions, a routine, a skill edit in the
plugin repo as a PR). Record the picks so the next retro can check them.

## Hard rules

Analysis only until the owner picks. Never edit instructions, memory, skills or
code during the retro. Never claim a pattern without dated evidence.
