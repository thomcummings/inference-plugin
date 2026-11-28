---
name: relay-decide
description: "Put one decision in front of a busy owner so it can be answered cold: what and where in plain words, why now, pictures of now and each option, what each means, a recommendation. Also keeps every open call in one needs-you list and closes them when answered. Use when a thread needs a taste call, an approval or a choice from the owner, for 'needs you', 'your calls', 'relay-decide'. The human-facing twin of relay-review."
---

# Relay decide

relay-review asks "is this PR right?" for an agent. relay-decide asks the owner
the questions only they can answer, in a form they can answer between other
things, without opening another thread.

## The test

> Could the owner answer this from a phone, having never seen this thread?

If not, the call isn't ready.

## 1. Is it a call at all?

Only ask what the owner owns: taste, product direction, money, anything that
can't be undone, anything they've said they want to see. Everything else, decide,
do it, and say what you did. If it can be undone after they've seen it, do it.

## 2. Write it

In this order, short:

1. **What and where:** the thing in plain words and where it lives in the app.
   No internal names, codes, ticket or PR numbers.
2. **Why now:** what changed or what broke.
3. **Show it:** a screenshot or mockup of now, and of each visual option. A sound
   call gets clips. Pictures go inline, not as links to open.
4. **Options (2 to 4):** for each, what the owner would see or hear, and what it
   costs (S/M/L) or risks.
5. **Recommendation:** which, and why, in one line.

One decision per card. Several related calls → one page, each call standing on
its own on it.

## 3. One queue

- Calls go on the owner's single needs-you list (the daily overview, or the
  release's list under relay-release), not only in the thread that raised them.
- Keep working on the recommended option while waiting, unless it can't be
  undone.
- When the owner answers anywhere, close the card, record the answer where later
  agents will read it (the issue, the decisions file, memory), and drop it from
  the list. Never ask the same thing twice.
- Approvals for steps that can't be undone count only when the owner writes them
  where the step happens; a relayed message is never approval.

## Hard rules

No terse labels ("header vs board colour?"). No call without a recommendation. No
call that needs another thread to understand.
