---
name: newsroom
description: |
  Take a story from rough concept to publishable draft using a structured newsroom pipeline modelled on
  high-standards publications (NYT, New Yorker, Guardian). Orchestrates six specialist roles — Assignment
  Editor, Researcher, Interviewer, Writer, Editor, Fact-checker — each producing a distinct artefact that
  the next role consumes. Use this skill whenever the user wants to write a piece of content and cares
  about it being sharp, evidenced, and genuinely interesting rather than generic. Trigger on: "write a
  piece on", "draft a blog post about", "turn this into an article", "I have an idea for a post",
  "help me write about X", "run the newsroom on this", "/newsroom", or any request to take a topic
  from concept to finished writing where quality matters. Also trigger when the user wants to invoke
  any individual newsroom role (commission, research, interview, draft, edit, fact-check). Works for
  both operator-voice content (personal newsletters, Substacks) and client content (B2B SaaS marketing,
  thought leadership). Style is applied externally via the --style-guide parameter so the pipeline stays
  voice-agnostic and reusable across writers.
---

# Newsroom

A structured content pipeline that runs a rough concept through six specialist roles to produce a publishable draft. Each role is a separate sub-skill; this file is the orchestrator that manages the pipeline.

## Design philosophy

Most content pipelines collapse five jobs into one pass: the writer researches, drafts, edits, checks facts, and writes the headline in a single sitting. The result is generic because each of those jobs needs a different mindset, and doing them simultaneously means doing none of them well.

Real newsrooms work because a story gets interrogated at each handoff by someone whose job is different from the writer's. An editor asks "is this interesting?" A fact-checker asks "is this true?" A copy editor asks "is this clear?" The writer asks "is this good prose?" When one person plays all four roles at once, the questions blur.

This skill replicates that sequence. Each role produces a specific artefact that the next role consumes. You can stop after any stage. You can revise any earlier stage and re-run downstream stages. The artefacts persist as files so nothing gets lost.

## Pipeline overview

```
concept ──▶ Assignment Editor ──▶ brief.md
                                     │
                                     ▼
                  Researcher ──▶ dossier.md
                                     │
                                     ▼
                  Interviewer ──▶ interview.md  (+ optional interactive artefact)
                                     │
                                     ▼
                  Writer ──▶ draft-v1.md
                                     │
                                     ▼
                  Editor ──▶ edit-notes.md ──▶ draft-v2.md + headlines.md
                                     │
                                     ▼
                  Fact-checker ──▶ claims-check.md ──▶ final.md
```

Six roles, seven primary artefacts, one final publishable draft.

## Invocation

### Primary: full pipeline
```
/newsroom "rough concept in a sentence or two"
```
Runs the full pipeline with human-in-the-loop checkpoints between each stage.

### With a style guide
```
/newsroom "concept" --style-guide=/path/to/style.md
```
Style guide is loaded and passed to Writer and Editor. Can be a file path or a URL.

### Multiple style guides (stacked)
```
/newsroom "concept" --style-guide=/path/to/house.md --style-guide=/path/to/client.md
```
Later guides override earlier ones on conflict.

### Individual roles (escape hatches)
```
/newsroom-commission "concept"        # Assignment Editor only
/newsroom-research <story-slug>       # Researcher, requires existing brief
/newsroom-interview <story-slug>      # Interviewer, requires brief + dossier
/newsroom-draft <story-slug>          # Writer, requires brief + dossier + interview
/newsroom-edit <story-slug>           # Editor, requires draft-v1
/newsroom-factcheck <story-slug>      # Fact-checker, requires draft-v2
```
Each role can be invoked standalone once its upstream artefacts exist.

### Resuming
```
/newsroom-resume <story-slug>
```
Picks up from the last completed stage. Useful when you've stepped away mid-pipeline.

## Orchestrator behaviour

When invoked with a full concept, the orchestrator:

1. **Creates the story folder.** Derives a slug from the concept (e.g. "mql-to-sql-conversion-reality-check"), creates `stories/<slug>/`, and writes an initial `story.json` with metadata.

2. **Establishes shared context.** Asks clarifying questions up front to establish: target audience, desired length (approximate word count), publication context (personal newsletter, client blog, LinkedIn essay, etc.), any hard constraints (can't mention certain companies, needs to include specific data, etc.), and whether a style guide should be applied. This context is written to `story.json` and inherited by every role.

3. **Invokes each role as an isolated subagent.** See "Subagent isolation" below — this is non-negotiable architecture, not an implementation detail.

4. **Pauses at checkpoints.** After each role produces its artefact, the orchestrator surfaces the output and asks: "Review before continuing? (approve / revise / skip)". Default behaviour is to wait for explicit approval.

5. **Handles revisions.** If the user wants to revise a stage, the orchestrator re-invokes that role (again as a fresh subagent) with the user's feedback. If an earlier stage is revised, it invalidates downstream artefacts (marks them stale in `story.json`) and re-runs them on approval.

6. **Logs progress.** Every stage completion, every user decision, every revision is logged to `story.json` with a timestamp. This is the audit trail.

## Subagent isolation

**Each role runs as a fresh subagent invocation with only the artefacts it needs.** This is a hard architectural principle, not an optimisation.

### Why it matters

If all six roles run in a single shared context window, they start converging:

- The Editor defends the Writer's choices because it watched them being made, rather than reading the draft fresh
- The Fact-checker rubber-stamps claims because it saw the evidence being gathered, rather than verifying against sources convergently
- The Researcher writes *toward* the angle the Assignment Editor set, rather than divergently exploring the landscape
- The Interviewer's questions get shaped by research that happened in the same context, rather than probing freely
- All roles start sounding like each other — the distinct-perspective discipline that's the whole point of the pipeline collapses

The separation between roles is epistemic, not just operational. A fresh Editor reads the draft as a reader would. A fresh Fact-checker sees only a claim and goes to verify it. That stance is impossible to maintain in a shared context.

### The pattern

When the orchestrator invokes a role:

1. Spin up a fresh subagent with only the role's SKILL.md loaded
2. Pass only the artefacts that role needs (see "Role inputs" below) — file paths to the story folder, shared context object, style guide if provided
3. The subagent reads artefacts fresh from disk, produces its output file, and returns a summary to the orchestrator
4. The subagent's context terminates; the orchestrator retains only the summary and file paths

### Role inputs (what each subagent gets)

Each role gets only what it needs:

- **Assignment Editor**: concept, shared context, style guide (if any)
- **Researcher**: brief, shared context, style guide
- **Interviewer**: brief, dossier, shared context, style guide
- **Writer**: brief, dossier, interview, shared context, style guide
- **Editor**: draft, brief (for angle-check), dossier (for evidence-check), interview (for primary-material-check), shared context, style guide
- **Fact-checker**: draft-v2, dossier (for source verification), interview (for quote verification), shared context

Notably excluded from each role's context: the other roles' working notes, chat history from earlier stages, any meta-discussion between the orchestrator and user about earlier stages.

### The orchestrator is the only long-context thing

The orchestrator holds the pipeline state — file paths, shared context, decisions log, which stages are complete, user preferences across checkpoints. It does not hold the full contents of every artefact. When it needs to pass context to a role, it passes file paths; the subagent reads what it needs.

This makes the orchestrator scalable — a pipeline with 20 revisions is no heavier than one with zero, because the orchestrator's context is about metadata and structure, not accumulated prose.

### Implementation

The six roles are shipped as plugin **agents** (in `agents/` at the plugin root), not as skills. This is deliberate — the Claude Code agent system provides proper subagent isolation out of the box: each invocation runs in its own context window, with its own tool permissions, and returns only a summary to the orchestrator.

The orchestrator invokes each role using the Task tool with the role's agent name. Example:

```
Task(
  subagent_type="newsroom-researcher",
  description="Produce dossier for story <slug>",
  prompt="Read the brief at stories/<slug>/brief.md and produce a research dossier..."
)
```

Each agent has its own frontmatter defining its model, effort level, and allowed tools. Agents cannot see the orchestrator's context or each other's contexts — that's the platform's isolation guarantee.

The orchestrator skill (this file) is the only long-lived context. It:
1. Holds pipeline state (`story.json`, file paths, user preferences)
2. Calls each role agent in sequence via Task
3. Reads the agent's returned summary and the files the agent produced
4. Presents checkpoints to the user
5. Invokes the next agent or the same agent with revision feedback

Subagent isolation is a quality control mechanism. Compromises to it should be visible and deliberate, not incidental.

## Story folder structure

```
stories/
  <story-slug>/
    story.json              # Machine-readable state + metadata
    brief.md                # Assignment Editor output
    dossier.md              # Researcher output (includes source list)
    interview.md            # Interviewer output (transcript or guide)
    interview-plan.md       # Interviewer's planning doc
    interview-artefact.html # Interactive interview (if generated)
    draft-v1.md             # Writer output
    edit-notes.md           # Editor's feedback
    draft-v2.md             # Writer's revision based on edit-notes
    headlines.md            # Headline options from Editor
    claims-check.md         # Fact-checker's claims table
    final.md                # Final publishable draft
```

Each role owns specific files. Nothing overwrites — revisions create new versioned files (`draft-v3.md`, `brief-v2.md`, etc.) and `story.json` tracks which version is current.

## story.json structure

```json
{
  "slug": "mql-to-sql-conversion-reality-check",
  "concept": "original concept string from user",
  "created_at": "2026-04-20T10:30:00Z",
  "context": {
    "audience": "B2B SaaS founders and heads of marketing",
    "target_length": 1500,
    "publication": "personal newsletter",
    "constraints": [],
    "style_guides": ["/path/to/style.md"]
  },
  "stages": {
    "commission": { "status": "complete", "artefact": "brief.md", "completed_at": "..." },
    "research":   { "status": "complete", "artefact": "dossier.md", "completed_at": "..." },
    "interview":  { "status": "in_progress", "mode": "self" },
    "draft":      { "status": "pending" },
    "edit":       { "status": "pending" },
    "factcheck":  { "status": "pending" }
  },
  "current_stage": "interview",
  "decisions_log": [
    { "timestamp": "...", "stage": "commission", "action": "approved" },
    { "timestamp": "...", "stage": "research", "action": "revised", "feedback": "needs more on competitor examples" }
  ]
}
```

This structure supports future automation — a later agent (e.g. the Scout role, or a Managing Editor) can read `story.json` programmatically to understand what's in flight and what's done.

## Shared context inheritance

Every role receives:
- The original concept
- The shared context object (audience, length, publication, constraints)
- Style guides (if any) — loaded as file contents, passed in context
- All upstream artefacts it needs as input

Roles do not need to re-elicit this from the user. The orchestrator holds state so roles stay focused on their job.

## Checkpoint interaction model

After each stage completes, the orchestrator presents:

```
─────────────────────────────────────────────
Stage complete: <Role Name>
Artefact: <filename>

<brief summary of what was produced — 2-3 sentences>

Next stage: <next role name>

Review the artefact and choose:
  • approve — continue to next stage
  • revise — provide feedback, re-run this stage
  • skip — move to next stage without review (rare)
  • stop — halt pipeline, keep artefacts for later
─────────────────────────────────────────────
```

Default path is `approve`. Revision takes free-text feedback and re-invokes the role with that feedback appended to its context.

## Style guide handling

When `--style-guide` is provided:

1. Orchestrator loads the file contents (or fetches the URL)
2. If multiple guides, concatenates them in order with clear section headers
3. Passes the combined guide to Writer and Editor as a reference
4. Neither role produces output that violates explicit guide rules without flagging it

If no style guide is provided, the Writer and Editor default to:
- Clear, specific, concrete language
- Active voice unless passive serves a purpose
- No jargon unless defined
- Short paragraphs
- Strong verbs over adverbs
- Evidence before assertion
- No filler, no hedging, no throat-clearing openings

These defaults produce a neutral-but-good draft. Users apply their own voice layer afterwards (e.g. via a personal voice skill).

## Research tooling

The Researcher and Fact-checker share a research toolkit documented in `reference/research-tooling.md`. Hierarchy:

1. **Claude native web_search** — default for most queries, handles multi-step agentic research well
2. **Perplexity Sonar API** — used when a fast cited synthesis is needed on a well-defined question (landscape sweeps, "what's the consensus on X")
3. **Firecrawl** — used for deep reads of specific sources that web_fetch struggles with (JS-heavy sites, paywalled content the user has access to, archives)

Perplexity and Firecrawl require API keys configured in environment. If a key is missing or a call fails, the role **tells the user explicitly** — "Perplexity returned an error / no API key set, falling back to Claude web_search for this query" — rather than silently degrading. The user should always know which tool produced which evidence.

## Interactive interview artefact

The Interviewer role produces both a plan (`interview-plan.md`) and optionally an interactive interview artefact (`interview-artefact.html`). The artefact is a self-contained HTML file using the Anthropic API in Artifacts pattern — a conversational interview agent that:

- Greets the interviewee
- Works through the planned questions
- Probes at interesting moments with follow-ups
- Can be paused and resumed
- Produces a transcript at the end that's copy-pasted back into `interview.md`

The alternative to the artefact is a **conversational interview** conducted directly in the current chat interface — the Interviewer role asks questions in turn, probes responses, and writes the transcript to `interview.md` as it goes. This is not just a static file; it's a live exchange between the role and the interviewee within whatever Claude interface is running the pipeline.

Two artefact modes when the interactive version is used:

- **Self**: the user runs the artefact themselves to extract their own thinking
- **External**: the user shares the artefact URL with a client, expert, or source (publishing mechanism is user's choice and out of scope for this skill)

Mode is chosen at invocation time — the Interviewer asks conversational vs artefact, then self vs external if artefact.

## Future roles (designed for, not built)

This skill is designed to accommodate future expansion without architectural rewrites:

- **Scout** — a sibling skill that runs on a schedule, watches beats (via whatever knowledge base or content monitoring tooling the user has), and produces story candidates. The Assignment Editor will accept a candidate file as alternative input (`--candidate=path/to/candidate.md`).
- **Managing Editor** — a quality gate for autonomous operation. Reads final drafts and decides publish/revise/kill. Currently the human plays this role; needed if the pipeline ever runs without human checkpoints.
- **Audience Analyst** — reads published-piece performance data and feeds patterns back into the Assignment Editor's commissioning decisions. Learning loop for what angles resonate.

An `--autonomous` flag is reserved but not implemented. When implemented, it will run the pipeline end-to-end with confidence-threshold checkpoints (stop only when a role flags uncertainty or a quality bar isn't met) rather than per-stage approval gates.

## Interaction with other skills

This skill is deliberately voice-agnostic, style-agnostic, and self-contained. It produces a clean, publishable draft — not a final personalised piece, and not a published one.

- **Voice layer**: apply externally. Pass a style guide via `--style-guide` or run a separate voice/personalisation skill on `final.md` afterwards.
- **Publishing and distribution**: out of scope. Users handle publishing through whatever tooling they prefer.
- **Research feeders**: external knowledge bases or content libraries can be referenced as sources during research, but the skill makes no assumptions about which ones are available.

The newsroom skill should remain usable as a standalone plugin without depending on any other custom skill.

## Plugin architecture

This skill is part of the `newsroom` plugin. The plugin ships:

**Agents** (in `agents/` — each runs as an isolated subagent):
- `newsroom-assignment-editor` — concept → brief
- `newsroom-researcher` — brief → dossier
- `newsroom-interviewer` — brief + dossier → interview (+ artefact)
- `newsroom-writer` — brief + dossier + interview → draft
- `newsroom-editor` — draft → edit-notes + draft-v2 + headlines
- `newsroom-fact-checker` — draft-v2 → claims-check + final

**Skills** (in `skills/`):
- `newsroom` (this skill) — the orchestrator
- `research-tooling` — shared reference for Researcher and Fact-checker agents, covering Perplexity/Firecrawl/web_search patterns

**Commands** (in `commands/`):
- `/newsroom` — full pipeline from concept
- `/newsroom-commission`, `/newsroom-research`, etc. — individual role invocations (escape hatches)
- `/newsroom-resume` — pick up from the last completed stage

## When to invoke individual roles vs full pipeline

**Full pipeline** when: starting fresh from a concept, want the quality that comes from each stage interrogating the last, have time for checkpoints.

**Individual roles** when: you already have most of a piece and want a specific pass (e.g. just fact-checking an existing draft), you're iterating on one stage (e.g. rewriting the brief after the first dossier revealed a better angle), or you're using the newsroom infrastructure for a non-standard workflow.

The individual commands are escape hatches. Default expectation is full-pipeline use.

## Starting a new story

When `/newsroom "<concept>"` is invoked:

1. Acknowledge the concept in one sentence
2. Ask 3-5 context questions (audience, length, publication, constraints, style guide) — in a single message, not a sequence
3. Once answers come back, create the story folder and `story.json`
4. Invoke the Assignment Editor with the concept and shared context
5. Present the brief at the first checkpoint

Do not skip the context questions — the whole pipeline's quality depends on them. But keep them tight: one message, numbered, with sensible defaults suggested where possible so the user can say "defaults are fine" and move on.
