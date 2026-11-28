# agentops

Skills for designing an agent setup. Each one decides first whether a need is a skill,
a persistent agent, a routine or a workflow, then designs, trials and places it.

## Install

```bash
/plugin marketplace add thomcummings/inference-plugin
/plugin install agentops@inference
```

## Skills

| Skill | What it does |
|---|---|
| `skill-design` | Decide whether a need is a skill at all, then design, trial and place it |
| `agent-design` | Decide whether a need is a persistent agent, then design its card, deployment and trial |
| `routine-design` | Decide whether a recurring job is a routine, then design its contract, method skill and native job text |
| `workflow-design` | Decide whether a job needs several agent passes, then design the stages, handoffs, independence and human gates |

## Licence

MIT. See [LICENSE](../../LICENSE) at the root of this repository.
