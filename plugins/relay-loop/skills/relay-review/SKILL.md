---
name: relay-review
description: "Review open PRs against their linked issue contract and required checks, then post a three-group verdict with Relay labels. Use to run the Relay reviewer. Designed for /loop; never merges or pushes code."
---

# Relay reviewer

One pass = one PR reviewed. The verdict is written for a human deciding whether
to merge — clear summary, plain language — while the labels drive the loop.

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

## Running more than one pass at a time
Passes may overlap: a cron trigger doesn't wait for the last run to finish, and
you may run one by hand alongside the loop. Nothing here locks a PR, and nothing
needs to. Reviewing never writes to the working tree, so two passes can't corrupt
anything between them, and the only write — the verdict — happens at the very
end behind the check in step 4, which discards a verdict another pass beat you
to. The worst case is duplicated reading, which is cheaper than a lock.

## Signing what you post
Start every verdict comment and tracker comment with this header, on its own line:

> 🤖 Relay reviewer — automated. Posted with the account owner's token.

## 0. Load config
Read `relay.config.md`; if missing, prompt and offer to save. Confirm `gh auth
status` is good — under cron there is nobody to log in.

## 1. Find a PR needing review
List open non-draft PRs with their labels and check status in one call
(`gh pr list --json number,labels,statusCheckRollup`). Skip, in this order:

- any PR carrying `{loop_name}-human` or `{loop_name}-blocked` outright, new
  commits or not — it is parked for a human, and removing that label is how they
  hand it back;
- any PR whose checks are still running — it isn't reviewable yet, and will be
  next pass.

For what's left, find the latest comment starting `Relay review of SHA`. Skip
when that SHA equals the current head and the PR already has
`{loop_name}-approved` or `{loop_name}-changes`; re-review when commits landed
after the recorded SHA. Nothing to do → say so, end.

Selection is the only place a pass moves between PRs. Once it commits to one, it
finishes or it ends — never chain to another PR mid-pass, because the contract
and diff already in context would contaminate the next one's ledger.

On a re-review, reuse the reviewer's ledger from the prior verdict. Don't
re-derive it, and never derive it from the builder's fix comment.

## 2. Read the contract — and only the contract
Get the linked issue id WITHOUT pulling the PR body into context — the tracker
isn't GitHub, so `closingIssuesReferences` is empty and the id lives only in the
description. Filter it in the shell so just the match reaches you:
`gh pr view <N> --json body -q '.body' | grep -oiE 'closes +[A-Z]+-[0-9]+'`
Then fetch that issue fully.

No linked issue → look for the `no_ticket_label` named in config, if set. Carrying
it, this is deliberate human-authored work: skip the contract requirement, review
against the repo's own rules and the change's internal consistency instead, and
open the ledger by saying so — "no contract; checked against repo rules only, not
against agreed acceptance criteria." Without that label, escalate. A missing ticket
is never something the builder can fix — it is forbidden from inventing work — so
`{loop_name}-changes` only bounces it back to a human a pass later.

Then, BEFORE opening any code, write the **reviewer's ledger**: one line per
`AC-N` saying what it demands and what evidence would satisfy it, one line per
`NG-N` saying what must not have changed.

Do not read the diff, the changed files, or **the PR description** until it is
written. The PR body carries the builder's own scope ledger — its AC-by-AC
account of why the work is done. Read that first and you will check the
builder's ledger instead of the contract, which is the failure this step exists
to prevent. From the PR, take only the head SHA, checks and mergeability that
step 4 needs; never the body into context.

Never revise the reviewer's ledger after reading the code. Where the two ledgers
disagree, the disagreement is the finding.

## 3. Read the code against it
Read the full diff and every changed file in context. Review ONLY against the
linked issue: AC gaps, defects, broken data flow, unnecessary scope expansion,
security, missing loading/error states, code future agents will struggle to
modify. No unrelated suggestions unless severe.

Read read-only, from your own clone — never check out the PR's branch, and never
touch the builder's workspace, which may be mid-pass and dirty. `gh pr diff <N>`
for the diff; `git fetch origin pull/<N>/head` then `git show FETCH_HEAD:<path>`
to read any file whole at that commit, changed or not. Neither touches the
working tree, so an unrelated checkout can't block the pass. If you put the SHA
in a variable, brace it — `"${SHA}:path"`, not `"$SHA:path"`, which zsh mangles
into a path modifier.

Every must-fix finding starts with one of:
- `[AC-N]` unmet · `[DEFECT]` broken in-scope · `[SECURITY]` · `[CI]` failed check
- `[POLICY]` — a config `policies` rule is violated (e.g. brain files touched but
  brain flag is no; client-visible yes but no CHANGELOG entry)

Two contract findings escalate rather than asking for a fix:
- `[CONTRACT-AMBIGUOUS AC-N]` — your ledger and the builder's differ and the
  issue doesn't settle which is right. Not a defect: under the builder's reading
  it's met. Quote both readings, say what turns on the difference, escalate.
- `[SCOPE-CONFLICT AC-N ↔ NG-N]` — non-goals bind, so if a fix needs `NG-N`
  behaviour, record the exact contradiction and escalate.

## 4. Check merge evidence
Inspect head SHA, mergeability, required checks. Rare, since step 1 filters
these out, but checks can go pending mid-pass if the builder pushes:
pending/unknown → report waiting, end without verdict or label change. Failed
required check → `[CI]`. Merge conflict → `[DEFECT]`. No required checks
configured → escalate; never treat missing CI as green.

Immediately before posting, re-check two things: the head SHA is unchanged, and
no `Relay review of <that SHA>` verdict has appeared while you were working. If
either has moved, another pass got there first — discard yours silently and end.
Two verdicts on one SHA thrash the labels, and the loser's is the one that
sticks.

## 5. Post one verdict
One comment, this shape, in this order:

```
Relay review of <SHA> — <safe to merge | changes requested | needs you>

**You:** <the one thing to do next, one line — or "Nothing. Safe to merge.">
**CI** <green|failed> · **Mergeable** <clean|conflict>

### Must fix before merge
### Should fix soon
### Safe to merge
```

An empty group gets `None.` and nothing else. A group with findings gets one
bullet each, tagged as in step 2.

When the verdict is `needs you`, the escalation replaces the summary and gets
exactly three lines:

- **Deciding:** the question in one sentence.
- **Options:** the two or three real ones.
- **My read:** the recommendation, and why it's still the human's call.

The ledger is published so a human can see the independent read happened, and so
the next re-review has its own anchor. Reproduce it as written; don't tidy it up
against what the code turned out to do.

Then set labels (check existing before removing):
- No must-fix, no escalation → add `{loop_name}-approved`, remove
  `{loop_name}-changes`.
- Must-fix present → add `{loop_name}-changes`, remove `{loop_name}-approved`.
- Contract ambiguity, scope conflict, policy violation needing a human, no required
  CI, or a missing ticket without the `no_ticket_label` → add `{loop_name}-human`,
  remove both, set "Safe to merge" to `No — human decision required.`

## 6. Mirror the outcome to the linked issue
Labels so far are on the PR, but the tracker is where a human looks for what
needs them. After posting, mirror the same terminal state onto the issue from
`Closes {ID}`, adding one and removing the other two:
`{loop_name}-approved` · `{loop_name}-changes` · `{loop_name}-human`.

Comment the PR URL and a one-line reason on the issue with the escalating two
(`-human`, `-changes`) — not on approvals, which the label alone conveys.
Never change issue status; that is the builder's. Best-effort — if the issue
can't be updated, say so in the PR comment and continue rather than failing
the pass.

No linked issue at all → nothing to mirror. Say so in the verdict rather than
leaving the tracker side silently unaccounted for.

## 7. Hard limits
Never merge or enable auto-merge. Never push to the PR branch. Never check out
the PR branch. Never file a formal GitHub review (the loop may run on the
author's token). `{loop_name}-approved` is evidence for a human, not merge
authorisation.
