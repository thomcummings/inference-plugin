---
name: relay-wrap
description: "Close the book on a relay-orchestrated issue: verify the loop reached a terminal state, surface anything left undone, and decide whether the thread is safe to archive. The counterpart to relay-spec — where relay-spec opens the book, relay-wrap closes it."
disable-model-invocation: true
---

# Relay wrap

The closing ritual for a relay-driven thread. Where relay-spec opens the book on
an issue (interviews it into a build-ready contract), relay-wrap closes it: it
checks that the loop actually landed in a terminal state, catches anything the
loop's own discipline could not see (promises, unverified claims, unanswered
questions), and answers the operator's one question — **can I archive this
thread?**

Report only. Never fix, commit, push, merge, file issues, or edit files in this
pass. Offer at the end; act only if asked.

## 0. Confirm this is a relay thread

Read the thread. A relay thread is one that ran (or was meant to run) through
the relay loop: it names an issue ID, references a PR or a `relay-*` label, or
invoked relay-spec / relay-build / relay-review / relay-orchestrate.

If the thread is NOT a relay thread, say so in one line and stop — this skill is
deliberately narrower than general thread hygiene. A strategy conversation, a
writing session, or an ops task that never touched the loop doesn't belong here;
use your runtime's ordinary close-out instead.

Then find the issue ID the thread was built around and read its **current**
state from the tracker — never from memory, never from what the thread claims.

## 1. Verify the loop reached a terminal state

The relay loop has exactly three terminal states for an issue. Check which one
this thread actually reached, against the live tracker and PR:

- **Merged and closed.** The PR merged and the issue is Done (or closed behind
  the PR's `Closes` link). This is the only fully clean terminal state.
- **Parked for a human.** The issue or PR carries `{loop_name}-human` (or
  `{loop_name}-blocked`). The loop stopped on purpose — a decision is waiting.
  The thread is closeable only if that decision is captured *somewhere the
  operator will see it* (a tracker comment, an assigned issue), not just in
  this chat.
- **Abandoned mid-loop.** The issue is still `{loop_name}-ready` / unassigned /
  In Progress with no PR, or a PR is open with no terminal `{loop_name}-*`
  label and no review in flight. The thread died before the loop finished.

Findings from this check:

- Loop not in a terminal state (abandoned, or still mid-flight) → **[LOOP]** —
  the thread is not safe to archive until the issue is either built, parked, or
  explicitly dropped.
- Issue Done but PR not merged (or PR merged but issue not Done) → the mirror
  drifted. **[TRACKER]** minor — counts, gets a line only if it would strand
  work.
- Issue carries `{loop_name}-ready` but nothing ever claimed it → the thread
  ended before the build started. **[PROMISED]** — it never returns to a queue
  on its own unless someone readies it.

## 2. Then the half only this thread can answer

Whatever the terminal state, re-read the conversation for the four things
trackers and PRs cannot show you:

- **Promised** — a follow-up you said you'd do, or a "worth doing later" that
  didn't happen. In a relay thread this is often a fix the review flagged but
  the cap stopped before it was made, or a follow-up issue you said you'd file.
- **Unverified** — something reported as done that was never actually run
  (checks claimed green that never ran, a build reported shipped that has no
  PR). Ranks above everything else in this list.
- **Unanswered** — a question the operator asked that got a sideways answer or
  none, especially a `{loop_name}-human` escalation that never got answered.
- **Undecided** — a choice made in chat that only exists in chat (a scope call,
  a non-goal waived, a ratify-this wording decision) and should be recorded on
  the issue before the thread disappears.

If the thread was compacted, say so in one clause and continue — do not imply
coverage you don't have.

## 3. Findings

A finding is one line: a tag, the thing, what to do. Tag from:

`[LOOP]` (loop never reached a terminal state) · `[UNVERIFIED]` · `[PROMISED]` ·
`[UNANSWERED]` · `[UNCOMMITTED]` · `[TRACKER]` · `[POLICY]` (a repo rule the
thread skipped) · `[LEFTOVER]` (scratch files, debug logging, stray branches)

Must-do means the thread is not safe to archive without it. Everything else is
"also noted" and gets counted, not listed. Judgement, not inventory: an
unanswered `relay-human` escalation and a stray debug log are not the same
finding.

## 4. Output

Verdict line, then at most **five** must-do lines, then two summary lines.
Nothing else — no preamble, no restating what relay-wrap does, no closing
paragraph.

Verdict is one of:

- `Close it.` — the loop reached a terminal state and nothing is left undone.
- `Not yet — N things.` — the loop didn't finish, or something is unverified.
- `Your call — N things.` — the loop is parked on a decision that's captured
  for the operator, or a minor item is left.

```
Not yet — 2 things.
1. [LOOP] Issue INF-123 is still relay-ready; the build pass never ran. File it
   or drop it before archiving.
2. [UNVERIFIED] Said "tests pass" in the thread; the review noted CI was never
   green. Confirm before closing.

Also noted: 1 minor — say "more".
Clean: PR merged, issue Done, no stray branches.
```

The `Clean:` line is one line however much you checked. Listing everything that
passed is the main way this skill turns into noise.

More than five must-dos means the thread genuinely isn't closeable: say that
outright, give the top five, and stop.

Close with a single offer — fix the must-dos, or expand the minor ones — and
wait.
