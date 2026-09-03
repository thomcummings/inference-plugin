---
name: relay-spec
description: "Interview the user about a raw idea until confident, then file it in the configured tracker as one build-ready issue — or an ordered chain of them — under the right project. Use to run the Relay spec interview or plan a feature. Interactive — the user is present and owns every product decision; never runs unattended."
---

# Relay spec

Turns a raw idea into an issue so complete a build agent needs nothing beyond
it. Research (if a codebase is present), interview the user in rounds until
confident, draft, confirm, file. The user is the product brain; you are the
codebase brain. Never guess a product decision.

Everything you produce must be legible to a human skimming the tracker, not
just parseable by an agent: plain language, real sentences, no cryptic shorthand.

## 0. Load config
Read `relay.config.md` (repo root, then `./.relay/config.md`). If missing, ask
for tracker, team, `initiative`, `project`, and `loop_name`, then offer to save
it before continuing. Labels and skill/label prefixes come from `loop_name`.

`project` may be a fixed name or the sentinel `[varies]`. `[varies]` (or a
missing `project`) means the target project is resolved at file time from
`initiative` — see step 4. A fixed `project` skips resolution and files there.

## 1. Research before asking
If a codebase is present, read the relevant code and every guide in
`repo_guides` first — which files are involved, what patterns exist, what
constraints apply. Read the source plan/idea. Never ask what the codebase can
answer. If there is no codebase, skip to the interview.

## 2. Interview in rounds
Ask 1–4 questions per round, concrete options, your recommended option first.
Ask only genuine product decisions:
- Behaviour forks: who sees it, what happens, where it lives
- Scope boundaries: what is explicitly out
- Edge cases that change acceptance criteria: empty states, permissions, failures
- Data implications: existing records, migrations
- Policy: does any configured policy flag apply?

After each round, fold answers in and apply the confidence test:

> Could two different people read this spec and ship the same observable outcome?

Any fork remaining → another round. No cap: two questions for a small fix,
10–20+ for a big feature. Never stop early because it feels like a lot; never
add filler once the test passes.

## 3. Draft — one issue or a chain
Use schema v1 exactly (Context incl. one-sentence Outcome; Acceptance Criteria;
Non-goals; Policy flags; Dependencies; Relevant context; Test expectations; How
to verify; Source). Rules:
- Every AC observable with an immutable `AC-N`; every non-goal an immutable `NG-N`.
- No AC may require an `NG-N`. If one does, resolve with the user before filing.
- Include `Policy flags` only for policies in config. If any is yes, the human
  must ratify before the gate label is applied.
- Omit `Relevant context` when not in a repo.
- Size to `max_issue_size`. Work that fits → **one issue**. Work that doesn't →
  an **ordered chain** of small issues, each within `max_issue_size`, each
  schema-v1 complete on its own, each buildable from ONLY the merged output of
  the issues before it. Number them 1..N in build order.
- In a chain, state each issue's dependencies explicitly in its `Dependencies`
  section ("Depends on #1, #2") so they map to tracker relations at file time.
  No issue may depend on one later in the order. Keep the chain the minimum
  length — never split what fits in one issue.
- Every issue in a chain is a real, human-legible unit of work, not a fragment:
  a reader skimming the tracker should understand each one on its own.

### The title

The body is for the build agent; the title is for a human skimming the tracker.
The test is CLARITY, not brevity: could the reader tell what this is, and roughly
what shipping it means, without opening it? If that takes eleven words, use
eleven — a short title they have to open is worse than a longer one they don't.

- Start with the verb where the job is obvious: Build, Fix, Add, Cut, Decide,
  Spec, Sweep, Publish, Fold.
- Name the thing in the user's own words. Describe the job, not the mechanism —
  no file paths, symbol names or internal machinery.
- A clause after a dash is allowed for ONE purpose: making an unfamiliar name
  legible. Never for a second scope item, a justification, or a flourish. If the
  clause would still make sense as a bullet in the body, it belongs in the body.
- A numbered chain keeps its marker as a prefix ("Metrics 3/4 — ..."), and it
  doesn't count against the length.
- Most titles land at 4–8 words. Past about twelve, the title has started doing
  the body's job — cut the part that isn't the gist.

Good:  "Build v1 experiments capability"
       "Customer dossiers — reconstruct one of the client's accounts on a
        timeline"  (long, but the clause is what makes "dossier" mean anything
        to someone who hasn't read the issue)
Bad:   "Ergo goes and checks its own views — position self-checks on the hourly
        dispatcher"  (the clause describes the mechanism)
       "Sweep every skill for where a connected tool would change the answer —
        and where to push for the connection"  (the clause is a second scope
        item; belongs in the body)  

## 4. Resolve the target project
Skip this step when config gives a fixed `project`. When `project` is `[varies]`
or missing, resolve it before filing:
- List the projects under `initiative` on `team`.
- Exactly one clear match to the work → use it, and name it in the confirm step
  (step 5) so the user can veto.
- Ambiguous (several plausible matches) or no good fit → ask the user: pick from
  the candidates you list, or create a new project (offer a name and a one-line
  description). Never guess a project; never file into a mismatched one.
- A chain files entirely into ONE resolved project — that project is the
  container ("epic") for the whole set. Never scatter a chain across projects.

## 5. Confirm and file
Show the full draft in chat — every issue in the chain, in order, each with its
stated dependencies — plus the resolved project. Get one explicit go-ahead for
the whole set.

Then, in build order, for each issue: create it in the resolved `project` on
`team`, status Backlog, label `{loop_name}-draft`. In a chain, immediately after
creating each issue set its tracker dependency relation (blocked-by) on the
issues it depends on, using the real IDs the tracker just returned — never a
placeholder. Report every identifier and URL the tracker returns, in order;
later stages and the human gate use them, never a guess.

## Hard rule
Never apply `{loop_name}-ready`, on any issue in the set. A human applies it per
issue after a final read — that label is the boundary between "idea" and "an
agent builds it". A chain is readied one issue at a time, as each becomes the
next safe unit of work. This skill never runs unattended.
