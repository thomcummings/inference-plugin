---
name: wrap
description: "Decide whether a working thread is safe to archive. Works across three modes it detects from the thread: Code/Relay (git, PRs, CI, repo rules), Project/ops (trackers and external state), and Conversation-only (promises, captures, decisions, unanswered questions). Reports a short verdict. Explicit invocation only."
disable-model-invocation: true
---

# Wrap

The user is asking one question: **can I close this thread?** Answer that first, in one
line. Everything else is supporting detail they may not read. A long list is a failed
pass — if you find eleven things, you have not filtered.

Report only. Never fix, commit, push, merge, file issues, or edit files in this
pass. Offer at the end; act only if asked.

## 0. Detect the mode

Before gathering evidence, read the thread and pick the mode that matches what
was actually done. This decides which sections below are load-bearing.

- **Conversation** — strategy, planning, writing, discussion, or anything with no
  code/commit, no tracker work, and no external state. Sections 2 and 4 apply;
  the repo and tracker steps are noise and can be skipped.
- **Project/ops** — work that mutates a tracker (Linear/Issue), a project, a
  notes vault or other external state without being a code commit. Sections 2, 4 and
  the tracker half of 1 apply; pure repo/CI steps are noise.
- **Code/Relay** — work in a repository against a branch/PR/CI. All sections
  apply.

When in doubt, run the cheap repo checks (working tree, stash, unpushed). If
they are clean and the thread never touched code, downgrade to Project/ops or
Conversation and say so in one clause.

Do not run `gh`, `git diff`, or CI checks in a thread that never touched a repo;
that politeness is what keeps `/wrap` useful for non-code work.

## 1. Gather evidence, don't rely on memory

**Tracker half (Project/ops and Code/Relay only).** For anything unambiguous on
this thread — an issue ID worked on explicitly, an item created, a project or
note written — compare what you just saw to the state recorded in the
thread. Only a contradiction is a finding:

- An item was created/promised as committed work but is not in the tracker → the
  capture never landed. Must-do: it degrades into chat-only memory.
- Tracker shows it open/backlog with no owner, branch or PR → an abandoned claim.
  Must-do: say so, because it never returns to a queue on its own.
- Anything consistent — created and verified, or closed behind a merged PR — is
  the `Clean:` line. No clear ID, or no tracker on this thread, skip it silently.

**Repo half (Code/Relay only).** Reconstruct from what's on disk, then add what
you remember:

```
git status --porcelain          # uncommitted + untracked
git stash list                  # forgotten stashes
git log --oneline @{u}..        # unpushed (skip cleanly if no upstream)
git diff <default-branch>...HEAD --stat   # what this branch actually changed
gh pr list --state open --head <branch>   # and `gh pr checks` on anything open
```

Detect the default branch; never assume `main`. Then read the diff itself — the
`--stat` tells you where to look, not what's wrong.

- Assigned, in a started state, no branch and no PR → an abandoned claim.
- PR merged, issue still open and carrying no `Closes` link → the auto-transition
  never fired. Minor — counts, doesn't get a line.

## 2. Then the half only this thread can answer

This section always applies, whatever the mode. Re-read the conversation for the
four things repos, trackers and memory can't show you:

- **Promised** — something you said you'd do next, or "worth doing later", and didn't.
- **Unverified** — something reported as done that was never actually run (typecheck,
  tests, the app). Ranks above everything else in this list.
- **Unanswered** — a question the user asked that got a sideways answer or none.
- **Undecided** — a choice made in chat that only exists in chat and should be written
  down (decision record, CHANGELOG, memory) before the thread disappears.

If the thread was compacted, say so in one clause and continue — do not imply
coverage you don't have.

## 3. Check the repo against its own rules

**Code/Relay only.** Read the repo's `AGENTS.md` / `CLAUDE.md` and test the branch
diff against the gates it sets — the ones routinely skipped at the end of a
session. Typical gates are a CHANGELOG entry, README honesty about the tree, a help
or FAQ page that's now stale, and release discipline. Every repo sets its own; read
theirs rather than assuming these.

Where a rule says a named person ratifies (customer-facing wording, client-visible flags),
flag that it's needed — never draft it as though settled.

## 4. Findings

A finding is one line: a tag, the file/PR, what to do. Tag from:

`[UNVERIFIED]` · `[PROMISED]` · `[UNANSWERED]` · `[UNCOMMITTED]` · `[OPEN PR]` · `[TRACKER]` ·
`[POLICY]` · `[LEFTOVER]` (debug logging, scratch files, TODOs added this session)

Must-do means the thread is not safe to archive without it. Everything else is
"also noted" and gets counted, not listed. Judgement, not inventory: a stray
`console.log` and an unpushed branch are not the same finding.

## 5. Output

Verdict line, then at most **five** must-do lines, then two summary lines. Nothing
else — no preamble, no restating what wrap does, no closing paragraph.

Verdict is one of:
- `Close it.` — nothing must-do.
- `Not yet — N things.` — something is incomplete or wrong.
- `Your call — N things.` — nothing is wrong, but a decision is parked (an open PR
  waiting on you, an undecided question).

```
Not yet — 2 things.
1. [UNVERIFIED] Said tests passed after the model-tiers change; never ran them.
2. [PROMISED] Said I'd check whether the help FAQ went stale. Didn't.

Also noted: 3 minor — say "more".
Clean: working tree, PR #164 (merged, green), CHANGELOG, README.
```

The `Clean:` line is one line however much you checked. Listing everything that
passed is the main way this skill turns into noise.

More than five must-dos means the thread genuinely isn't closeable: say that
outright, give the top five, and stop.

Close with a single offer — fix them, or expand the minor ones — and wait.