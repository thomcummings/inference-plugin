# Trigger eval

## Contents

- [Why triggering is its own problem](#why-triggering-is-its-own-problem)
- [Writing the query set](#writing-the-query-set)
- [Running it](#running-it)
- [Reading the result](#reading-the-result)

Test 1 of the trial: does the skill fire on the work it owns, and stay quiet on
its neighbours' work? This is the cheap test and the one that catches the
failure that actually happens — in a library of any size, collision with a
neighbour is more common than a bad method.

## Why triggering is its own problem

The frontmatter description is the only thing in context when the decision to
consult a skill is made. The body cannot help: it loads afterwards. So a skill
with an excellent method and a vague description is a skill that never runs,
and nobody finds out, because a skill that does not fire produces no error —
just an ordinary answer that could have been better.

Two things worth knowing before writing queries:

- **Simple requests do not trigger skills.** A one-step task gets handled
  directly regardless of how well a description matches. "Read this file" is a
  useless test query. Make the queries substantive enough that consulting a
  skill is plainly worth it.
- **Under-triggering is the common failure.** Descriptions are usually too
  polite. That is why box 2 leans pushy — and why the boundary clause has to be
  explicit, since pushy without a boundary just steals from neighbours.

## Writing the query set

Aim for 20: 8–10 that should trigger, 8–10 that should not.

**Realistic, not abstract.** Write what the principal would actually type —
file paths, client names, a bit of backstory, lowercase, abbreviations, the
occasional typo. Vary the length.

- Weak: `"make a skill"`
- Strong: `"ok so every time a client sends over a new competitor to look at i
  end up doing the same four things in the same order and half the time i
  forget the pricing bit. can we make this a thing i can just run"`

**Positives: cover the phrasings, not the vocabulary.** Include formal and
casual versions of the same intent; cases where the skill is named and cases
where it is described; at least two where the principal does not use the
skill's own words at all; and one uncommon-but-legitimate use.

**Negatives: near misses only.** This is where the value is. A good negative
shares keywords or subject matter with the skill but needs something else —
work that belongs to an adjacent skill, a request one level up or down in
scope, phrasing where a naive keyword match would fire. Draw them from the
overlap audit: the neighbours named in §4 are the negatives.

The failure to avoid is an obviously irrelevant negative. "Write a fibonacci
function" as a negative for a proposal skill tests nothing, passes every time,
and creates false confidence in a boundary that was never probed.

Save the set as a JSON list, beside the skill in the repo and **not inside the
skill folder** — a run does not use it:

```json
[
  {"query": "…", "should_trigger": true},
  {"query": "…", "should_trigger": false}
]
```

## Running it

```bash
python3 scripts/trigger_eval.py \
  --skill ops:skill-design \
  --eval-set path/to/queries.json \
  --runs 3 \
  --model <the model the principal actually runs> \
  --out results.json
```

Triggering is stochastic, so each query runs several times and a query counts
as triggering when it fires in at least half of them. Use the model actually in
use — a description tuned against one model's judgement is not guaranteed to
transfer.

## Reading the result

The script reports accuracy, recall (of the positives, how many fired) and
precision (of everything that fired, how much should have). More useful than
any of them is the per-row line: on a failure it names **which skill fired
instead**.

| What the result shows | What it means | What to change |
| :-------------------- | :------------ | :------------- |
| Misses on positives | The description does not reach how people actually ask | Add the missed phrasings; make the opening clause more direct about the job |
| False fires on negatives | The boundary is too weak | Sharpen `do not use this for`, and name the neighbour that should win |
| A neighbour fired instead | Two descriptions overlap | Fix the pair, not just this one — the neighbour's description needs the reciprocal boundary |
| Everything passes first time | Usually the negatives were too easy | Rewrite them closer to the line before believing the score |

Change the description, re-run, and keep the version that holds up on queries
it was not tuned against. A description edited until it passes its own 20
queries and nothing else has been fitted to the test, not improved — when in
doubt, hold a few queries back and check against those at the end.

Where a failure turns out to be a genuine overlap rather than a wording
problem, it is a §4 finding, not a description problem: the right fix may be to
merge the two skills or to drop one.
