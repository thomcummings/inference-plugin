# Newsroom

A Claude Code plugin that takes a rough content idea through a six-role newsroom pipeline to produce a fact-checked, publishable draft.

Modelled on the craft standards of publications like the New York Times, New Yorker, and Guardian — where a story gets interrogated by five different people before anyone writes the lede. Each role in this pipeline runs as an isolated subagent, which prevents context convergence (the failure mode where every role starts sounding like the same voice).

## What it does

You give it a rough concept. It gives you a publishable draft.

In between, six specialist roles do their distinct jobs:

1. **Assignment Editor** — interrogates the concept, finds the sharpest angle, writes a commissioning brief
2. **Researcher** — casts wide across the topic, produces a structured dossier (landscape, evidence, counter-arguments, gaps)
3. **Interviewer** — extracts primary material from you or a third party; can run live in chat or as a shareable HTML artefact
4. **Writer** — synthesises brief, dossier, and interview into a first draft; never invents material
5. **Editor** — three-pass editing (structural → line → headline) plus 3-5 headline options
6. **Fact-checker** — convergent verification of every claim; produces the final draft

Each stage pauses at a checkpoint for your review before moving on.

## Why a pipeline and not one prompt

Most AI content collapses five jobs into one pass: researching, drafting, editing, fact-checking, and headline-writing all happen simultaneously. The result is generic because each of those jobs needs a different mindset, and doing them at once means doing none of them well.

This plugin separates the jobs. Each role runs as a fresh subagent with only the artefacts it needs. A fresh Editor reads the draft cold, like a reader would. A fresh Fact-checker sees a claim and goes to verify it, not the evidence-gathering context in which it was found. The separation is the quality mechanism.

## Installation

The plugin ships as a standard Claude Code plugin. Install it via your preferred mechanism:

- From a marketplace: `/plugin install newsroom`
- From a local directory: `/plugin marketplace add /path/to/newsroom-plugin` then `/plugin install newsroom`
- From a git repository: follow your marketplace's pattern

Once installed, the slash commands below are available.

## Usage

### Full pipeline (recommended)

```
/newsroom "MQL-to-SQL conversion rates measure the wrong handoff"
```

Runs the full six-role pipeline with checkpoints between each stage. You'll be asked 3-5 context questions up front (audience, length, publication, constraints, style guide), then each role produces its artefact in turn and hands off to the next.

### With a style guide

```
/newsroom "concept" --style-guide=/path/to/style.md
```

The style guide informs the Writer and Editor. Pass multiple `--style-guide=` flags to stack them; later guides override earlier ones on conflict.

### Individual roles (escape hatches)

For when you already have part of the pipeline done:

```
/newsroom-commission "<concept>"       # Assignment Editor only
/newsroom-research <story-slug>        # Researcher (requires brief)
/newsroom-interview <story-slug>       # Interviewer (requires brief + dossier)
/newsroom-draft <story-slug>           # Writer (requires brief + dossier + interview)
/newsroom-edit <story-slug>            # Editor (requires draft-v1)
/newsroom-factcheck <story-slug>       # Fact-checker (requires draft-v2)
```

### Resuming

```
/newsroom-resume <story-slug>
```

Picks up from the last completed stage. Useful when you've stepped away mid-pipeline or want to continue a piece on a different day.

## File structure per story

Each story gets its own folder under `stories/<slug>/`. Nothing overwrites — revisions create new versions, and every artefact persists for traceability:

```
stories/mql-to-sql-conversion-reality-check/
├── story.json              # Machine-readable pipeline state
├── brief.md                # Assignment Editor's commissioning brief
├── dossier.md              # Researcher's findings + source list
├── interview-plan.md       # Interviewer's planning doc
├── interview.md            # Interview transcript + interviewer notes
├── interview-artefact.html # Interactive interview tool (if artefact mode)
├── draft-v1.md             # Writer's first draft
├── edit-notes.md           # Editor's change log
├── draft-v2.md             # Editor's revised draft
├── headlines.md            # 3-5 headline options
├── claims-check.md         # Fact-checker's claims table
└── final.md                # Publishable draft
```

## Configuration

### Optional API keys

The Researcher and Fact-checker use Claude's native `web_search` / `web_fetch` as their primary tools. Two optional tools extend their capabilities:

- **Perplexity Sonar** (`PERPLEXITY_API_KEY`) — fast cited synthesis for landscape sweeps
- **Firecrawl** (`FIRECRAWL_API_KEY`) — deep extraction for JS-heavy or complex sources

If neither key is set, both roles fall back to native Claude tools and announce the fallback explicitly. No silent degradation — you'll always know which tool produced which evidence.

Get keys:
- Perplexity: https://www.perplexity.ai/settings/api
- Firecrawl: https://www.firecrawl.dev/app/api-keys

Both offer free tiers sufficient for moderate personal use.

### No configuration required

Out of the box, with no API keys, the plugin runs on Claude's native web tools. The research may be slightly slower than with Perplexity/Firecrawl available, but the pipeline is fully functional.

## What this plugin is not

Deliberate scope decisions worth knowing:

- **No voice layer.** The pipeline produces clean, neutral-but-good prose. Voice and personalisation happen externally — either through a style guide (passed at invocation) or by running a separate voice skill on `final.md` afterwards. Keeping the pipeline voice-agnostic makes it reusable across writers and publications.

- **No publishing.** The pipeline stops at the publishable draft. Getting it to your blog, newsletter, LinkedIn, or CMS is your decision and your tooling.

- **No proactive story generation.** The pipeline is reactive — you provide the concept, it produces the piece. A companion Scout role (proactive story candidate generation) is architected for but not built.

- **No autonomous mode.** Every stage waits for your approval before continuing. A future `--autonomous` mode is designed for but requires a Managing Editor role (quality gate) before it can ship safely.

## Architecture

### Subagent isolation

Each role runs as a Claude Code agent (in `agents/`), which means each invocation gets its own fresh context, tool permissions, and turn budget. The orchestrator (the `newsroom` skill) is the only long-lived context — it holds pipeline state in `story.json` and spawns each agent via the Task tool with only the artefacts that role needs.

This matters because when all roles share context:

- The Editor defends the Writer's choices rather than reading the draft fresh
- The Fact-checker rubber-stamps claims because it watched the evidence being gathered
- All roles start sounding like each other — the distinct-perspective discipline that's the whole point collapses

Isolation is the quality mechanism. The plugin architecture enforces it at the platform level, not via prompt discipline.

### Model tuning per role

Agents are configured with different models and effort levels based on what the role needs:

| Role | Model | Effort | Tools |
|------|-------|--------|-------|
| Assignment Editor | sonnet | medium | file I/O |
| Researcher | sonnet | high | web search + fetch + bash |
| Interviewer | sonnet | high | file I/O |
| Writer | opus | high | file I/O |
| Editor | opus | high | file I/O |
| Fact-checker | sonnet | high | web search + fetch + bash |

The Writer and Editor get opus because prose quality is where model capability matters most. Researcher and Fact-checker get web tools because their jobs depend on source access. You can adjust these in each agent's frontmatter if you want to trade speed for capability or vice versa.

### Extensibility

The plugin is designed to accommodate roles that aren't built yet:

- **Scout** — proactive story candidate generation from monitored beats
- **Managing Editor** — autonomous-mode quality gate
- **Audience Analyst** — feedback loop from published piece performance

Adding these means writing new agent files and updating the orchestrator's pipeline logic; the rest of the architecture stays intact.

## Credits and philosophy

Built in the spirit of real newsrooms — where commissioning, researching, interviewing, writing, editing, and fact-checking are distinct crafts practised by different people, and the separation is what makes the work sharp.

The pipeline deliberately avoids what most AI content tools do: one model, one prompt, one pass, all roles collapsed. That pattern produces prose that's polished but soulless. This pattern aims for prose that's specific, evidenced, contrarian where it needs to be, and unmistakably written by someone with a point of view.

## Licence

(Add your preferred licence here.)
