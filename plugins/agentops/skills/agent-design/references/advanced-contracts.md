# Advanced extension — the six-contract stack

The five-box canvas is the default. Escalate to the full stack only when real
risk or complexity warrants it. Escalating everything reintroduces the problem
the canvas exists to solve.

## When to escalate

**At least two** of:

- the agent is customer-facing or speaks to a client without review;
- it handles sensitive, personal, or regulated data;
- it moves money or creates financial obligations;
- it acts irreversibly (deletes, publishes, sends, commits);
- it coordinates several other agents rather than doing the work itself;
- a failure would be externally visible or hard to reverse.

Proactive cadence alone is not a reason to escalate — that criterion already
lives on the creation gate. If fewer than two apply, the canvas plus three
tests is sufficient. Say so explicitly rather than quietly adding ceremony.

## How to escalate — expand the boxes, don't start a parallel ontology

Keep the same Agent Card. Add fields; do not write six unrelated documents
unless the principal asks for them. Mapping:

| Canvas box | Add |
| :--------- | :-- |
| Job | Warrant: why not a human, skill, or routine; cost of the alternative. Charter extras: review cadence, retirement conditions. |
| Workspace | Data classification, boundary rules, injection / exfiltration exposure. |
| Powers | Per-action permission matrix, approval gates, credential scope, reversibility, rollback position. |
| Teamwork | Handoff packet fields, conflict-precedence, shared-context rules. |
| Deployment and proof | Cost and context budgets, observability, adversarial evals, degradation policy. |

The six contract names (warrant, charter, operating contract, trust envelope,
team contract, deployment/fitness) are labels for those expansions, not a
second filing system.

## Design principles worth keeping at both levels

- **Simplest workable architecture first.** Add a second agent, a tool, or a
  memory layer only when the current design demonstrably fails.
- **Explicit outcomes and boundaries over elaborate personas.** Behaviour is
  engineered, not described.
- **Bounded agency.** Every capability has a scope, an approval boundary, and a
  reversibility position.
- **Generated, not authored.** Instructions and configuration derive from the
  contract so they cannot silently diverge.
- **Evidence of fitness.** An agent earns continued operation with observable
  results, not with its own confidence.
- **Design the seams.** Handoffs, disagreements, and escalation paths fail more
  often than individual agents do.

## Failures the extension is meant to catch

- Excessive agency: an agent acting beyond the outcome it owns.
- Prompt injection or data exfiltration via retrieved content.
- Silent authority drift: local configuration quietly becoming canonical.
- Duplicated ownership producing conflicting actions on one outcome.
- Untested agents holding live powers with no expiry.
