# Skill conventions

*The canon for how a skill is built. A strong default, not a mandate — not
every skill needs every convention, but every departure should be a decision
rather than an oversight.*

## Contents

- [The three shapes](#the-three-shapes)
- [Structure](#structure)
- [Progressive disclosure](#progressive-disclosure)
- [File placement](#file-placement)
- [Writing](#writing)
- [What never goes in a skill folder](#what-never-goes-in-a-skill-folder)
- [Safety](#safety)

## The three shapes

### Simple — the default, and most skills

```
skill-name/
├── SKILL.md          # inputs, interview, method, self-check — all of it
└── templates/
    └── artifact.md   # the output's defined format
```

### Structured — earned by real complexity

```
skill-name/
├── SKILL.md          # orchestration: the numbered order + hard rules only
├── steps/            # topic-named, order-agnostic
│   ├── intake.md
│   ├── interview.md
│   ├── assemble.md
│   └── review.md     # the self-check
├── references/       # material this skill consults
├── scripts/          # anything the skill executes
└── templates/
```

### Phased — rare, do not start here

```
skill-name/
├── SKILL.md          # the numbered phase order + gates
└── phases/
    ├── outline/      # each phase orchestrates its own steps
    │   ├── PHASE.md
    │   └── steps/…
    └── review/…
```

Structure is earned, never added on spec. A simple skill that is whole beats a
structured one with stub files, every time.

## Structure

**Order lives in the orchestrator, not the steps.** The numbered sequence
exists in exactly one place: SKILL.md, or a phase's own file where there are
phases. Each numbered item names the step and points at its file. Step files
are therefore:

- **Unnumbered filenames** — `interview.md`, not `02-interview.md`.
- **Topic-only headings** — `# Interview the principal`, not `# Step 2 —
  Interview`.
- **Position-agnostic content** — no "in the previous step", no "before moving
  to step 4", no "you should already have". Cross-reference another step by
  name where genuinely necessary, never by number or position.

Why: steps get reordered, split, merged and dropped as a skill improves in
place. When order lives only in the orchestrator that is a one-file edit; when
it is baked into filenames and prose it is a rewrite, and any ordering language
left behind misleads silently.

**Shared instructions live once.** Anything used by several steps goes in one
file both point at, never duplicated into each.

**Executables go in `scripts/`.** If the method involves the same deterministic
transformation every run, write it once as a script the skill calls rather than
as prose the model re-implements each time. A strong signal: when several test
runs independently write the same helper, that helper belongs in the skill.

## Progressive disclosure

A skill loads in three levels:

1. **Frontmatter** — name and description, always in context. This is the only
   thing that decides whether the skill runs at all.
2. **The SKILL.md body** — loaded when the skill triggers. Keep it to
   orchestration, hard rules and the method, with detail pushed outward.
3. **Unpacked files** — loaded only when read. Effectively unlimited.

Structure for that:

- Keep the body lean. Past roughly 400–500 lines, add a layer of hierarchy
  rather than another section.
- **Link every unpacked file from SKILL.md** with a note on when to read it. A
  file nothing points at never gets read, and a file pointed at without a
  trigger gets read every time.
- Keep reference files **one level deep** — no references pointing at
  references.
- Give any reference file over ~100 lines a table of contents, so a preview
  reveals its full scope.

## File placement

- **This skill's material** — templates, examples, domain reference it alone
  consults — lives inside the skill.
- **Material several skills read** — voice, brand, positioning, client context
  — lives at the repo or workspace level. Skills never reach inside other
  skills; a skill that reads a neighbour's files breaks the moment that
  neighbour is restructured.
- **Test and eval material** lives beside the skill, not inside it. A run does
  not use it.

## Writing

**Imperative voice.** "Extract the text", not "you should extract the text" or
"the agent will extract the text".

**Explain why, rather than capitalising.** A capable model given the reasoning
will generalise to cases the skill never anticipated; the same model given a
stack of imperatives will follow them past the point where they help. Finding
ALWAYS or NEVER in caps is a signal that the reasoning has not been worked out
— reframe and explain instead. Reserve hard prohibitions for things that are
genuinely never right.

**Define the output format explicitly**, as a template rather than a
description of one:

```markdown
## Report structure
Use this structure:
# [Title]
## Executive summary
## Key findings
## Recommendations
```

**Use real examples.** One worked input-and-output pair drawn from real past
work aligns a skill's output better than three paragraphs describing the
desired result. Where past outputs of the process exist, mine the template from
them rather than inventing it.

**Write general, not narrow.** The skill will run on inputs nobody has seen. A
rule that fixes the three test cases in front of you and nothing else has made
the skill worse, not better — it has added length and false confidence. When
something is stubbornly wrong, try a different framing or metaphor before
adding a narrower rule.

**Keep it lean.** Every line that is not pulling its weight is competing for
attention with the lines that are. Reading the transcript of a real run shows
which parts sent the model somewhere unproductive; cut those.

## What never goes in a skill folder

No README, no changelog, no installation guide, no notes on how the skill was
made, no design rationale. A skill folder contains only the files its executing
agent uses to do the job. Everything else belongs in the repo around it.

## Safety

A skill must not contain malware, exploit code, or anything that compromises
the system it runs on, and its contents should not surprise someone who has
read its description. Do not build skills designed to mislead, to facilitate
unauthorised access, or to exfiltrate data. Roleplay and stylistic skills are
fine; a skill whose behaviour differs materially from what its description
implies is not.
