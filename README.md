# Inference Hub

A Claude Code plugin marketplace from [Inference](https://thisisinference.com) — a growing library of marketing plugins for the AI rebuild. 

## What's in the hub

| Plugin | What it does |
|--------|--------------|
| [`relay-loop`](./plugins/relay-loop) | My agentic software development loop - run rough ideas through spec, build, review, fixes, and deploy through a disciplined, human-gated agent loop — each pass in a fresh context. |
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

## Roadmap

More plugins in development. Follow [Annotations by Inference](https://annotationsbyinference.substack.com/) on Substack to get them first.

If something here is useful to you, I'd love to hear about it. Feedback, issues, and pull requests are all welcome.

## About Inference

Inference is a marketing studio for the AI rebuild, founded by [Thom Cummings](https://thisisinference.com).
