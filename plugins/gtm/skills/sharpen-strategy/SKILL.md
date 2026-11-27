---
name: sharpen-strategy
description: >-
  Sharpen a strategy or plan (marketing, GTM, events, product, org, a hire's
  first six months) by questioning it in short rounds until the user and Claude
  mean the same thing by it, writing a glossary of agreed terms and a log of the
  key bets as the session goes. Use when someone says "sharpen this plan",
  "grill me on this", "interrogate this strategy", "poke at this until it's
  clear", "make sure we actually agree on what this means", "what haven't we
  decided yet", "let's define our terms before we build the plan", or brings a
  strategy doc and wants it tightened before it is committed or shared with a
  team. Also use to pick up an earlier session or check a plan against an
  existing glossary and decision log. Not for a go/no-go on one proposed move
  (pressure-test), a panel of expert viewpoints (debate-room), building
  positioning from scratch (positioning), turning agreed strategy into a
  committed, budgeted plan (marketing-plan), or creative, naming and copy work,
  where constant questioning kills momentum.
---

# Sharpen Strategy

Most strategies fail quietly, not loudly: two people read the same plan and
picture different things. This skill closes that gap. It questions a strategy
in short rounds until you and the user describe it the same way, and leaves two
working documents behind: a **glossary** of the terms you agreed and a
**decision log** of the bets you made.

Two things make strategy different from a spec, and they shape the method.
Strategic decisions are bets, not facts you can check, so every recorded
decision says how it could turn out wrong. And a strategy usually needs other
people to act on it, so the session ends by working out who else has to agree.

## 0. Before the first question

Get these straight first. Work out what you can from what's in front of you,
and only ask about the rest.

1. **The plan and the decision.** Say in one sentence what plan you're
   sharpening and which decision it feeds.
2. **Where the documents live.** Use the first of these that exists:
   - a shared context store: decisions in `memory/decisions/`, glossary at
     `evergreen/glossary.md`. pressure-test, naming and release-gtm use the same
     decisions folder, so a bet recorded here is visible to them.
   - a glossary or decision log somewhere else: a Notion page, a doc, a note.
   - otherwise, `GLOSSARY.md` and `decisions/` in the working folder.

   Read any existing documents in full before starting, and stay consistent
   with them. Entries marked `canonical` are agreed. Entries marked `working`
   are still open. Don't create a file until you have its first entry.
3. **Anything left open last time.** If the decisions folder holds an
   `open-questions.md`, read it. Those questions come first.
4. **What evidence you can reach.** List the sources available through
   connectors or files: CRM, analytics, call notes, past plans, audits. This is
   what you check claims against.
5. **Who has to agree.** Ask who needs to sign off on or act on the result. That
   changes how the session ends. If it's only the user, say so: the output is a
   hypothesis to test with buyers or the market, not a team agreement.

## 1. Question in rounds

A strategy is a chain of choices, and later choices lean on earlier ones. A
common order is goal, then audience or ICP, then positioning, motion, channels
and programmes, resourcing, and measurement. Follow the actual order of the plan
in front of you; that list is only a starting guess.

In each round:

- **Ask only what's ready.** A question is ready when everything it depends on
  is already settled. If its answer would change depending on something still
  open, save it for a later round.
- **Number the questions** (Q1, Q2 and so on) and give your own answer to each
  under **Recommend:**. Phrase it so the user can accept it with a single "yes".
- **Show your working.** Each recommendation names the evidence behind it (a
  number, an earlier decision, a call) and grades it: validated, hypothesis or
  assumption. With no evidence, mark it `(guess)`. Generic best practice dressed
  up as the user's own situation anchors them on something nobody checked.
- **Keep rounds short:** about seven questions, fewer when each needs real
  thought. If more are ready, ask the ones with the biggest consequences first.
- **Wait for the answers.** Then see which questions they've unlocked, and
  start the next round with those.

**Look things up rather than asking.** If a question turns on something the
evidence can answer ("how many deals came from events last quarter?"), find it
yourself, with a subagent if you can so the round keeps moving. Put only
choices, priorities and judgement calls to the user. If a fact can't be found,
call it unknown and make it a research task. Never pass off an estimate as data.

## 2. Push on the weak spots

- **Loose words.** When the user leans on a vague word ("engaged", "qualified",
  "community", "enterprise", "influenced"), offer a tight definition and confirm
  it before moving on.
- **Clashes with the glossary.** If the user's meaning for a term differs from an
  existing entry, point it out straight away and ask which meaning they want.
- **Claims about how things work.** When the user says something like "most
  customers find us through X", check it against the evidence and say plainly
  if the evidence disagrees, with the source.
- **Test cases.** Make up a specific awkward case to find the edge of a
  definition: "A target account's engineer signs up self-serve, then sales gets
  involved. Is that marketing-sourced?"
- **Unspoken assumptions.** Name the assumption a decision rests on and ask
  whether it's known or hoped.
- **The cost of yes.** For every "yes", ask what the plan is giving up.

Push back when an answer is vague, contradicts the evidence or ducks a
trade-off. Questioning that only agrees adds nothing. Raise a doubt once,
clearly, then move on: repeating it every round tires the user without
improving the plan.

## 3. Keep the glossary as you go

Write an entry the moment a term is agreed, not at the end, so a session that
stops early still leaves its definitions behind. The glossary holds only
definitions: no plans, tactics or decisions.

```markdown
### <Term>
<One or two sentences, precise enough to settle edge cases.>
- Counts: <example>
- Doesn't count: <example>
- Measured by: <metric and source, if it has one>
- Not to be confused with: <nearby term>
- Status: working | canonical · Agreed: <date>
```

New entries stay `working` until the user confirms them at the end.

## 4. Record only the bets that matter

Most decisions in a session don't need a record. Write one only when the
decision is all three of these:

1. **Expensive to undo.** Changing course later would cost real money, time,
   reputation or a relationship.
2. **Odd-looking from outside.** Someone who joins in six months would ask why
   on earth you did it.
3. **A real choice.** Other options were genuinely on the table, and the reasons
   for this one can be written down.

Ask the user before writing each one, and save it as `<date>-<slug>.md` in the
decisions folder.

```markdown
# <The decision, as a short instruction>
Date: <date> · Status: proposed | accepted | superseded by <file>
Owner: <name> · Source: sharpen-strategy

## Context
<What forced the decision, and the key evidence with sources and grades.>

## Decision
<What we'll do, and what we won't.>

## Alternatives considered
- <Option>: <why not>

## The bet
We believe <hypothesis>. If we're right, we'll see <leading indicator> by <date>.

## When to revisit
We look again if <signal or threshold>. Review date: <date>.
```

Records stay `proposed` until the user confirms them at the end.

## 5. Wrap up

You're done when no ready questions are left and nothing important has been
assumed without saying so. If you have to stop earlier, write the questions
still waiting to `open-questions.md` in the decisions folder, each with your
current recommendation, so the next session can start there.

Then:

1. Sum up the decisions made, the terms defined, and anything **parked**, with
   the reason.
2. Ask the user to confirm you now describe the strategy the same way. Once they
   do, mark the glossary entries `canonical` and the records `accepted`. Don't
   build anything on the strategy before that.
3. If other people have to agree, offer a **team questionnaire** covering the
   open or contested decisions, ready to paste into a doc or channel:

   ```markdown
   ## <Decision to make>
   Options: A) <option> · B) <option> · C) <option>
   Recommendation: <option>, because <evidence, graded>
   Your view: [A / B / C / other] · Why:
   ```

4. Name the next step: a single contested bet goes to pressure-test, and an
   agreed strategy goes to marketing-plan. If a task or calendar tool is
   connected, offer to add the review dates to it.

## Before you call it done

Check that:

- every **Recommend:** named its evidence and grade, or said `(guess)`;
- every glossary entry has a "counts" and a "doesn't count" example;
- every decision record meets all three tests and has a review date;
- every number in either document came from a named source;
- no ready questions are left, or the rest are saved in `open-questions.md`.

## Method lineage

Inspired by Matt Pocock's open-source grilling skills (github.com/mattpocock/skills),
which question a software design in rounds and keep a glossary and decision
records as they go. This skill takes that idea to strategy, where decisions are
bets: recommendations are graded against evidence, records carry revisit
criteria, and the session ends by working out who else has to agree.
