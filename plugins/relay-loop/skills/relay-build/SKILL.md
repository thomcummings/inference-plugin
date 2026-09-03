---
name: relay-build
description: "Claim the next safe gate-labelled issue from the configured tracker, implement it, and open a PR. Use to run the Relay builder or fix Relay review feedback. Designed for /loop; one pass does one unit of work."
---

# Relay builder

One pass = one unit of work: fix review feedback on one PR, or build one issue.
Write PR text and comments a human can read and trust, not just an agent.

## Writing rules for anything a human reads

Verdict first, detail after, and only as much detail as the decision needs.

- **Lead with the ask.** First line is the state and the one thing the human does
  next. If that's nothing, say nothing.
- **Bullets, not prose.** No paragraph over three sentences. One idea per bullet.
- **Detail nests.** A finding is one sentence; its evidence is a sub-bullet under
  it, not a longer sentence.
- **Cut throat-clearing.** Don't restate the PR title, don't summarise what you're
  about to say, don't explain why an empty section is empty.
- **Plain, not dumbed down.** Short words for ordinary things; keep the precise
  term where precision earns its place, and gloss it once.
- Sign off in one line.

## Lane discipline
Never run the reviewer. Building and reviewing are separate loops, and a builder
that reviews its own PR reads the contract through the code it just wrote — the
verdict then confirms the build's interpretation instead of testing it.

Every terminal path here ends the pass and leaves the PR for the review lane. If
a prompt asks you to review as well, do the build half, say the review lane owns
the rest, and end.

## Running more than one pass at a time
A cron trigger doesn't wait for the last run to finish, so passes can overlap.
This one mutates the working tree, which makes overlap destructive rather than
merely wasteful, so it is guarded at two levels:

- **The lane lock (step 0)** stops two passes sharing one workspace. It is
  per-workspace, so it does not stop passes in two different workspaces.
- **A plain non-forced `git push` (step 1)** stops those. If another pass fixed
  the same PR first, the push is rejected as non-fast-forward and you discard
  rather than reconcile. Git's own concurrency control, free.

Between them, nothing needs a claim comment or a new label.

## Signing what you post
Start every PR description, PR comment and tracker comment with this header, on
its own line:

> 🤖 Relay builder — automated. Posted with the account owner's token.

## Mirroring labels to the tracker
Whenever you add or remove a `{loop_name}-*` label on a PR, make the same change
on the issue named by `Closes {ID}` before ending the pass. The PR is where the
loop coordinates; the tracker is where a human looks for what needs them, and
the two drifting apart is how work goes quietly missing. Best-effort — if the
issue can't be updated, say so in the PR comment and carry on rather than
failing the pass.

An open PR carrying none of `{loop_name}-approved`, `-changes` or `-human` means
**awaiting review**. That is a valid resting state, not a dropped ball; the
review lane picks it up on its next pass.

## 0. Load config + preflight
Read `relay.config.md`; if missing, prompt and offer to save. Confirm the
intended repo, that `origin` is reachable, and that `gh auth status` is good —
under cron there is nobody to log in. Detect the default branch
(`default_branch: auto`); never assume main.

**Take the lane lock.** Write `$(git rev-parse --git-dir)/relay-build.lock`
holding the timestamp and what you are about to work on. That path resolves
correctly in both a clone and a linked worktree, and sits inside the git
directory, so the lock never shows up as a dirty file. If it already exists:

- **under 60 minutes old** → another pass is running here. Say so and end.
- **older than 60 minutes** → the previous pass died. Clean tree: clear the lock
  and carry on. Dirty tree: that is a crashed build — report the lock's contents
  and the dirty paths, and end without touching them.

Remove the lock on every exit path, including the early ones.

Require a clean working tree — if dirty, report paths and end. Never stash,
reset, or touch unrelated work. One narrow exception: a lockfile the toolchain
regenerates (`package-lock.json` and the like) carrying no version or dependency
changes is machine churn, not someone's work — save the diff somewhere
recoverable, restore the file, say plainly that you did, and continue. Anything
else dirty ends the pass.

## 1. Review feedback first
List open PRs labelled `{loop_name}-changes`. Skip any also carrying
`{loop_name}-human` or `{loop_name}-blocked`. Take the least recently updated:
read its linked issue and latest `Relay review of SHA` verdict, note that head
SHA, check out the branch, fix ONLY the "Must fix" items, run relevant checks.

Then push, and **never with `--force`**. A rejected non-fast-forward push means
another pass fixed this PR while you were working. Don't reconcile: drop your
commits (`git reset --hard origin/<branch>` — they are yours, not someone
else's, and leaving them makes the next pass end on a dirty tree), say what
happened, and end. On a clean push, remove `{loop_name}-changes`, comment what
changed, mirror the label change to the issue. End pass.

The verdict carries the reviewer's own ledger of what each `AC-N` demands, which
may read the contract differently from the PR's scope ledger. Where they differ,
the reviewer's reading governs the fix — it was written before the code was
read. Don't argue it in a comment; fix to it, or escalate.

If a fix would cross an `NG-N` or needs a product decision: comment the exact
conflict, add `{loop_name}-human`, remove `{loop_name}-changes`, mirror both,
end.

## 2. Pick
List `team` issues that are: labelled `{loop_name}-ready`, unassigned, not
`{loop_name}-blocked`, no unresolved blocker relation. Sort by priority then
oldest. Never invent work; never pick a blocked issue.

Empty → before ending, check for chain links that just came free: issues still
labelled `{loop_name}-draft` whose blocker relations have all resolved. List
them, each with what actually shipped in its blocker, and say they are waiting
on a human to ready them. Never apply `{loop_name}-ready` yourself. Then end.

## 3. Claim (cooperative lock)
Assign yourself, move to a started state (prefer In Progress). Claim before
reading deeply. Re-fetch; if now blocked, reassigned, or no longer
`{loop_name}-ready`, drop it and return to step 2. One builder loop per team.

## 4. Read
Fetch the full issue with comments and relations. Implement only its AC.
Non-goals are binding — compare every `AC-N` against every `NG-N` before
editing. Ambiguous AC, NG conflict, or unresolved blocker → step 8. Never guess.

An unratified proposal in the comments is not part of the contract. Build the AC
as written, and say in the PR that the proposal was left out and why — never
adopt it quietly, and never treat it as a blocker on its own.

If this issue was blocked by another that has since closed, read what actually
shipped there before building — the contract was written before its dependency
existed, and a chain link often assumes a shape the build didn't take. If the AC
no longer matches reality, that is step 8, not a judgement call.

## 5. Build
Fetch the latest default branch; create/resume `branch_pattern` with the real
ID. Implement in the repo's existing style and naming. Add/update tests when
logic, data flow, permissions, integrations, or user-visible behaviour change.
Honour every Policy flag per config `policies` (e.g. add the CHANGELOG entry if
client-visible is yes; don't touch brain files if brain is no). Preserve all
behaviour outside the contract.

## 6. Verify
Run the project's relevant lint, typecheck, build, and narrowest useful tests.
All checks attributable to this change must pass before a PR. Pre-existing
unrelated failure → run the targeted check, disclose both. Review
`git diff`/`git status`; stop on unrelated work or secrets.

A check you couldn't run is not a check that passed. Name it, say what blocked
it (missing env, no database, no API key), and write it up as a manual test step
instead of leaving the gap implied.

## 7. Ship
Open a PR whose description has, in plain language: what changed and why;
`Closes {ID}`; a scope ledger (one evidence line per `AC-N`, one preservation
line per `NG-N`, `Other behaviour changes: None`); numbered manual test steps;
checks run + results; Risk Low/Medium/High. If `Other behaviour changes: None`
isn't true, stop and get the issue amended first.

Keep `Closes {ID}` on its own line — the review lane extracts it from the body
without reading the rest.

Comment on the issue: the PR URL, and at most three bullets on anything decided
during the build that isn't in the PR description. Not a second write-up of the
work — the PR is that. Leave it with no `{loop_name}-*` terminal label: that is 
the awaiting-review resting state. Never merge or enable auto-merge. Never 
review it yourself. End.

## 8. Blocked
If anything has been written, push the branch first — a blocked pass still
leaves its work recoverable, and the workspace may not survive the wait.

Then comment one specific answerable question (exact decision, options, which
AC), add `{loop_name}-blocked`, unassign, and mirror the label to the PR if one
exists. Leave `{loop_name}-ready` in place — the pick query excludes blocked, so
it reappears only after a human answers and removes the label.
