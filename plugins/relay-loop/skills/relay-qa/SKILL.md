---
name: relay-qa
description: "Run a release-candidate QA sweep: several cheap tester agents, each with one lens, try to break the real build and file evidence-backed reports; one Opus auditor dedupes, reproduces and files only confirmed bugs. Use for 'run QA on the release', 'relay-qa', 'try to break the release branch'. Never fixes code during the sweep."
---

# Relay QA

The step between relay-build/relay-review and relay-release. relay-review checks a
diff against its contract; relay-qa checks the **assembled release** against a
player. It runs once per release, when the release branch is feature-complete,
so the human's own testing time goes on feel, not on finding crashes.

Shape: **N testers → 1 auditor → a short list for the human.**

- Testers are cheap (Haiku by default), fresh, and independent. Each gets one
  lens and a hard budget. They find and evidence; they never judge severity,
  never fix, never file.
- The auditor is Opus. It trusts nothing a tester says until it has reproduced
  it itself. Only reproduced bugs leave the sweep.
- The human gets confirmed bugs (in the tracker), design calls (in the clear-call
  format), and a listening list. Nothing else.

## Writing rules for anything a human reads

Same as relay-review: result first, bullets, one idea each, evidence nested, no
throat-clearing. Every call stands alone: what it is and where in plain words, why
now, a screenshot, the options with what each costs, a recommendation.

## 0. Load config

Read `relay.config.md` (repo root, then `./.relay/config.md`), section `qa`:

- `target`: how to reach the build. Prefer **serving the release branch head
  locally** (the exact SHA, built with the repo's own build step) over a hosted
  preview: previews are often behind a login a headless browser can't pass, and
  a pinned SHA makes every report reproducible. Record the SHA in every report.
- `lenses`: the menu of tester lenses (below is the default menu).
- `budget`: per-tester cap (browser actions and wall time), auditor cap, and the
  sweep's total token ceiling.
- `tracker`: team, project, labels (`qa` plus a severity label), where evidence
  is attached.
- `known`: the list of known issues and open design calls, so testers don't
  re-file them.

Missing config → ask once, offer to save it.

## 1. Plan the sweep (auditor, before any tester starts)

Write a one-screen plan and keep it in the sweep folder:

- the SHA and how it's served;
- which lenses run (2–3 for a trial, up to 6 for a full sweep) and each one's
  scope: the screens and features it owns, so lenses don't overlap;
- the budgets;
- what's out of scope (sound quality, real devices, anything `known` lists).

Pick lenses for what changed in this release (`git log main..release`), not the
whole app. A lens with nothing new to test is waste. Prefer more lenses over more
testers per lens; device-size and round-trip lenses find the most per token,
while open-ended "break it" lenses on cheap models find the least.

### Default lens menu

| Lens | Plays as | Looks for |
|---|---|---|
| first-run | someone opening the app for the first time | dead ends, unclear first steps, copy that doesn't match the controls, empty states |
| chaos | an impatient player | double taps, fast repeats, undo/redo spam, open/close races, add-remove-add, stuck states |
| small-screen | a phone in portrait, then landscape | clipped or overlapping UI, targets under 44 px, scroll traps, sheets that won't close |
| round-trip | someone saving their work | save, reload, load, share code, import/export: does what comes back match what went in |
| scale | a power user | the tested limits (parts, wires), long sessions, CPU readout, slowdowns |
| themes | someone who changes the look | every theme and dark mode: contrast, missing tokens, unreadable states |

## 2. Run the testers

One **fresh agent per lens**, in parallel, cheap model, background. Each tester's
brief contains only: the target URL and SHA, its lens and scope, the budget, the
`known` list, the report format, and the browser recipe. Not the other lenses,
not the plan's reasoning, not the code. Testers drive the real page in a browser
(Playwright, or whatever headless browser the platform has), never the source.

Testers are the one place the loop uses sub-agents rather than fresh top-level
passes: they are short, read-only probes that change nothing, so a hung tester
costs only its budget. The auditor and any later fix pass follow the normal
rule (AGENTS.md non-negotiable 2). Where your platform's
sub-agents are unreliable, dispatch testers as top-level passes instead.

Give testers a **starter helper** for the app (open fresh, load a preset, switch
view, open the main menus, collect console errors, screenshot), checked by the
auditor before the sweep. In the first trial most tester tokens went on finding
locators, not on testing. Name the app's real menu roles and labels in it.

Tester rules (put these in the brief verbatim):

1. Stay in your lens and scope. Stop at the budget, even mid-idea.
2. A finding needs **numbered repro steps from a fresh page load**, expected vs
   actual, and evidence: a screenshot, and the console errors if any. Reproduce
   it once yourself from a fresh load before reporting. No repro, no report.
3. Report what you saw, not why. No guesses at causes, no severity, no fixes.
4. Notes that aren't bugs (confusing, slow, ugly) go under `observations`, kept
   apart from `findings`.
5. Don't touch the repo, the tracker or GitHub.
6. Write the report to `<sweep>/<lens>/report.json` and screenshots beside it;
   return only a five-line summary.

Report format:

```json
{ "lens": "chaos", "sha": "…", "viewport": "1280x800", "actions_used": 37,
  "findings": [ { "title": "…", "steps": ["…"], "expected": "…", "actual": "…",
                  "evidence": ["shot-03.png"], "console": ["…"], "reproduced_twice": true } ],
  "observations": [ "…" ] }
```

Record each tester's tokens, tool calls and wall time from the agent's result.

## 3. Audit (Opus, fresh context)

Read every report. Observations are not reproduced: skim them once for
candidate `call`s and drop the rest. Then, for each finding:

1. **Dedupe** across lenses (same root symptom = one item; keep the best repro).
2. **Check `known`** and the tracker. Already filed → add the new evidence as a
   comment, don't refile.
3. **Reproduce it yourself** from the steps, on the same SHA, from a fresh load.
   Not reproduced → `noise` (say why in one line: couldn't repeat, tester
   misread the UI, intended behaviour, out of scope).
4. **Classify** what's left:
   - `bug`: broken against the app's own rules or the design system. Severity:
     S1 crash, lost work or silence; S2 a feature doesn't work; S3 cosmetic or
     rare.
   - `call`: works as built, but a player would trip on it and fixing it changes
     the design. That's the human's, never the auditor's.
   - `listen`: anything only ears can judge.
5. **File** each `bug` in the tracker: plain-words title, repro, expected/actual,
   screenshot attached, SHA, lens, label `qa` + severity. Agent detail goes in a
   collapsible notes section.

The auditor does **not** fix during a sweep. Fixing is a separate, ordinary
relay-build pass on the filed issues, after the human has seen the list.

## 4. Report to the human

One message:

- **Result line:** N confirmed bugs (S1/S2/S3), M calls, the listening list,
  noise rate.
- **Bugs:** one line each with its tracker link, S1 first.
- **Calls:** each in the clear-call format, with screenshots.
- **Listening list:** 3–6 short things to play by ear, each with where and what to
  listen for.
- **Cost:** tokens and wall time per tester and for the audit; confirmed bugs per
  100k tokens; per-lens yield. This is what decides the next sweep's lenses.

## 5. Hard limits

Never merge. Never push. Never fix during a sweep. Never file an unreproduced
report. Never judge sound. Never let a tester see another tester's report. Stop
the sweep at the total token ceiling and report what you have.
