# Inference plugins

Marketing skills and agent workflows for teams rebuilding marketing around AI. Open
source, built from years of experience running marketing at high-growth tech companies,
and written to make AI agents sharper marketing partners, not faster content machines.

## What's here

Four Claude Code plugins in one marketplace. Each skill turns a piece of marketing or
operating practice into a workflow an agent can run with you: it reads your context,
asks only for what's missing, and leaves you a working document you can act on.

| Plugin | For | Skills |
|---|---|---|
| [`gtm`](./plugins/gtm) | Marketing and go-to-market strategy | 33 |
| [`thinking-tools`](./plugins/thinking-tools) | Thinking a hard call through before you commit | 3 |
| [`agentops`](./plugins/agentops) | Building and running your own agent setup | 3 |
| [`relay-loop`](./plugins/relay-loop) | Shipping software through a human-gated agent loop | 12 |

## Start here

Pick the path that matches the job in front of you.

- **You need your story straight.** Run `/gtm:positioning`, then `/gtm:messaging-framework`.
  Positioning settles who it's for, what it beats and why it wins. Messaging turns that
  into words a team can use.
- **You have a plan and want it tested.** Run `/thinking-tools:sharpen-strategy` on the
  whole plan, then `/thinking-tools:pressure-test` on the biggest bet inside it.
- **You want agents doing real work, safely.** Run `/agentops:skill-design` before you
  build anything new, and `/relay-loop:relay-spec` to turn an idea into a build-ready
  issue.

Give the skills a context folder first (`/gtm:context-layer`) and every one of them gets
better.

## How these skills work

Five house rules run through every skill.

1. **Context before questions.** A skill reads what you already have before it asks you
   anything, and it asks only for what's missing.
2. **One job each.** Every skill does one thing and names the skill to use instead when
   your request belongs somewhere else.
3. **Assumptions are labelled.** Facts, your inputs, inferences and guesses are marked as
   such. Nothing is presented as evidence when it isn't.
4. **Working documents, not chat.** The output is something you can share, edit and come
   back to: a canvas, a plan, a decision log, a spec.
5. **Credit where it's due.** Where a skill builds on someone else's published method, it
   names the source in a method lineage section.

Opinionated by design. Each skill makes a recommendation, informs you about the
tradeoffs, and leaves the strategic judgement to you.

## Catalogue

### Marketing (`gtm`)

| Area | Skills |
|---|---|
| Foundations | `positioning`, `point-of-view`, `content-model`, `messaging-framework`, `language-market-fit`, `icp`, `competitive-scan`, `context-layer` |
| Brand | `brand-architecture`, `brand-archetype`, `brand-overview`, `essence-craft`, `naming`, `marketing-psychologist` |
| Growth | `growth-model`, `growth-bets`, `channel-map`, `campaign-brief`, `release-gtm`, `dev-mktg`, `pricing-packaging` |
| Plans and decisions | `marketing-plan`, `marketing-board-update`, `analyst`, `org-design`, `agentic-opportunity` |
| Sales and ABM | `selling-system`, `abm-strategy`, `abm-setup`, `abm-ops` |
| Content production | `news-angles` (finds the stories you could get covered for and grades news vs announcement), `newsroom` (a six-role pipeline from rough concept to fact-checked draft), `research-tooling` |

### Thinking tools (`thinking-tools`)

| Skill | What it does |
|---|---|
| `debate-room` | Convenes independent expert personas, maps where they clash and synthesises a sharper answer |
| `sharpen-strategy` | Questions a plan in short rounds until you and the agent mean the same thing by it |
| `pressure-test` | The go/no-go gate on one bet: kill, shrink, prove it cheaply first, or not yet |

### Agent operations (`agentops`)

| Skill | What it does |
|---|---|
| `skill-design` | Decides whether a need is a skill at all, then designs, trials and places it |
| `agent-design` | Decides whether a need is a persistent agent, then designs its card, deployment and trial |
| `handoff` | Packages working context so another session, agent or platform can pick up cleanly |

### Software delivery (`relay-loop`)

A disciplined loop that takes an issue from rough idea to merge-ready PR: spec, build,
independent review and fix rounds, each in a fresh context, with a human owning every
gate. Around it sit skills for decisions, UI design, QA sweeps, a weekly release and a
retro, and `relay-wrap` closes the book on a finished thread. See the [relay-loop README](./plugins/relay-loop/README.md).

## Install

Add the marketplace once:

```bash
/plugin marketplace add thomcummings/inference-plugin
```

Then install the plugins you want:

```bash
/plugin install gtm@inference
/plugin install thinking-tools@inference
/plugin install agentops@inference
/plugin install relay-loop@inference
```

Skills load namespaced by plugin, for example `/gtm:positioning` or
`/thinking-tools:debate-room`. Agents also pick them up on their own when your request
matches a skill's description.

To pull the latest versions:

```bash
/plugin marketplace update inference
```

Some skills hand off to others by name. A handoff to a skill you haven't installed is a
suggestion, not a requirement.

## Contributing

The most useful thing you can send is a real problem a skill didn't handle well: what you
asked, what it gave you, and where it fell short. Open an issue with that and we'll work
on the skill. Fixes to the skills themselves are welcome as pull requests.

If you're missing a skill for a problem you keep running into, [get in
touch](https://thisisinference.com).

## Use them with judgement

These skills are shared as they are, to help you think and work, not to do your thinking
for you.

- **Check the output.** AI models make mistakes, including confident ones. Review
  anything a skill produces before you act on it, publish it or show it to a client.
- **No promises.** Inference makes no guarantee that the skills are accurate, complete or
  fit for your situation, or that they work as described in every setup.
- **Things change.** Skills are written and tested against the models and tools of the
  day. New models, platform changes and a moving market can make parts of them out of
  date.
- **Your call, your responsibility.** Decisions you make with these skills are yours.
  Nothing here is legal, financial or other professional advice.

The MIT licence also applies: the software is provided "as is", without warranty of any
kind.

## Licence

MIT. See [LICENSE](./LICENSE). Where a skill builds on someone else's published method,
it credits them in its method lineage section.

## About Inference

[Inference](https://thisisinference.com) is an independent marketing studio for the AI
rebuild. These skills power our client work.
