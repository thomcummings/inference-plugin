# thinking-tools

Skills for thinking a hard call through before you commit to it. They aren't tied to
marketing: use them on a positioning call, a hire, a pricing change, a product bet or a
plan you're about to take to the board.

## Install

```bash
/plugin marketplace add thomcummings/inference-plugin
/plugin install thinking-tools@inference
```

## Skills

| Skill | Use it when | What you get |
|---|---|---|
| `debate-room` | You want real disagreement on an open question, not one voice in five hats | A room of independent expert personas, a map of where they clash, and a synthesis that says what it weighted and why |
| `sharpen-strategy` | You have a plan and want it questioned until you and the agent understand it the same way | Short rounds of questions that leave a glossary of agreed terms and a decision log of the bets you made, each with how it could turn out wrong |
| `pressure-test` | One bet is about to be placed: a campaign, a channel, a launch, a hire, a big spend | A verdict you can act on today: kill, shrink, proceed with the cheapest proof, or not yet (fix this gap first) |

They hand off to each other. A broad question goes to `debate-room`, a whole plan goes
to `sharpen-strategy`, and a single move inside it goes to `pressure-test`.

More on how `debate-room` works, its rooms and its personas: [docs/debate-room.md](./docs/debate-room.md).

## Licence

MIT. See [LICENSE](../../LICENSE) at the root of this repository.
