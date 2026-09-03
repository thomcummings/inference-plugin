# Inference Hub

A Claude Code plugin marketplace from [Inference](https://thisisinference.com) — a growing library of marketing plugins for the AI rebuild. 

## What's in the hub

| Plugin | What it does |
|--------|--------------|
| [`relay-loop`](./plugins/relay-loop) | Run an issue from a rough idea to a merge-ready PR through a disciplined, human-gated agent loop — spec, build, independent review, and fix rounds, each pass in a fresh context. |
| [`newsroom`](./plugins/newsroom) | Six-role newsroom pipeline that takes a rough concept to a publishable, fact-checked draft. Each role runs as an isolated subagent to prevent context convergence. |
| [`debate-room`](./plugins/debate-room) | Convene a room of opinionated expert personas to stress-test a question. Each persona is briefed as an independent subagent to prevent convergence, then the orchestrator maps tensions and synthesises a multi-viewpoint answer. |

More plugins land here as the library grows. See the roadmap below for what's in flight.

## Installation

Install the marketplace once:

```bash
/plugin marketplace add thomcummings/inference-plugin
```

Then install any plugin from it:

```bash
/plugin install newsroom@inference-plugin
```

To see all plugins available in the marketplace:

```bash
/plugin marketplace list inference-plugin
```

## What each plugin tends to have in common

A few design principles run through everything here:

- **Isolated agents over shared context.** Where plugins use multi-role pipelines, each role runs as a fresh subagent. Shared context makes roles converge and lose the distinct-perspective discipline that's the whole point of separating them.
- **Human-in-the-loop by default.** The plugins surface their thinking at checkpoints so the operator stays in charge of the judgement calls. Automation is a tool, not a replacement.
- **File-based state, minimal infrastructure.** Everything works against local markdown and JSON. No databases, no auth, no deployment overhead.
- **Voice-agnostic at the core, personalisation at the edges.** The pipelines produce clean, well-structured output. Voice and style are applied externally via style guides or downstream skills — not baked in.
- **Opinionated where it matters, flexible where it doesn't.** Each plugin has strong opinions about craft (what a good brief looks like, what fact-checking means, how headlines should be written) and stays out of the way on everything else.

## Roadmap

More plugins in development. Follow [Annotations by Inference](https://annotationsbyinference.substack.com/) on Substack to get them first.

If something here is useful to you, I'd love to hear about it. Feedback, issues, and pull requests are all welcome.

## About Inference

Inference is a marketing studio for the AI rebuild, founded by [Thom Cummings](https://thisisinference.com).
