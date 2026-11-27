# Agent Card template

Canonical artifact for a persistent agent. Copy the block, fill it, and keep it
in the roster path resolved by the skill (default `system/agents/`). Everything
else (instructions, platform profile, prompt) derives from this card.

Keep each box to roughly five lines. If a box needs more, the scope is wrong.

Show the filled card first, then propose writing it. Never silently overwrite
an existing card.

---

```markdown
# Agent Card — <Agent Name>

- **Agent ID:** <stable, platform-independent, lowercase-hyphenated>
- **Status:** proposed | trial | active | degraded | dormant | retired
- **Owner (accountable human):** <name>
- **Canonical revision:** <n>

## 1. Job

- **Role:** <what kind of thing this is>
- **Outcome it owns:** <the durable outcome>
- **Also owns:** <secondary outcomes, or "none">
- **Does not own:** <explicit exclusions and who does own them>

## 2. Workspace

- **Core context:** <the standing context it must know>
- **Folders / repositories:** <paths, read/write>
- **Memory scope:** <what persists about it as an agent>
- **Sources of truth:** <systems, and precedence when they disagree>
- **Must not read:** <boundaries, or "none">

## 3. Powers

- **Skills:** <skill IDs it relies on>
- **Tools / connectors:** <product — allowed operations>
- **Can do:** <list>
- **Must ask before:** <list>
- **Must never do:** <list>

## 4. Teamwork

- **Receives work from:** <who/what>
- **Can delegate to:** <agents, humans, systems>
- **Hands off when:** <trigger>
- **Reports back with:** <the report contract>
- **Escalation route:** <blocked work, conflicts>

## 5. Deployment and proof

- **Platform / runtime:** <where it runs>
- **Default model:** <chosen after the role, not before>
- **Channels:** <where it speaks>
- **Trial period:** <start → review date>
- **Test 1 — core job:** <representative work + expected result>
- **Test 2 — boundary:** <out-of-scope request + expected refusal/reroute>
- **Test 3 — authority:** <consequential action + expected approval request>
- **Pass condition:** <what "good enough to activate" means, judged by the owner>
- **Review date:** <date; trials expire unless renewed>
```

---

## Routines are not part of the card

Do not list routines, schedules, methods or delivery rules anywhere in the card.
Ownership is one field, held on the routine itself in the routine registry:
`current agent owner`.

The agent's routine list is derived, never stored:

```text
routines owned by <agent-id>  :=  registry.filter(current_agent_owner == agent-id)
```

If a *report* shows the list for legibility, mark it
`derived from the routine registry — do not edit`. Adding, handing over or
retiring a routine then changes exactly one record. If there is no registry,
omit the snapshot.

## Generated instructions scaffold

Write the runtime prompt from the card. Keep it short and behavioural. Adjust
formatting to the runtime; do not add mandates, powers or relationships that are
not in the card. Do not paste a routine list. Do not paste the three tests.

```markdown
You are <Agent Name>. You own <outcome>.

You do not own <exclusion 1> or <exclusion 2>. When those arise, <handoff>.

You work from <sources of truth / context>. When sources disagree, <precedence>.

You can: <can do>.
You must ask <owner> before: <must ask before>.
You must never: <must never do>.

You receive work from <source> and report back with <report contract>.
You hand off when <trigger>. Escalate failures to <route>.

You own the routines currently assigned to you in the routine registry. Read the
registry for the current list, and read each routine's own contract before running
it — do not rely on a remembered schedule or method.

You are in trial until <review date>.
```

## Deployment entry scaffold

One entry per runtime that hosts the agent.

```yaml
agent-id: <agent-id>
canonical-revision: <n>
platform: <runtime>
native-identity: <profile / agent id / bot id>
model: <model>
enabled: true | false
local-overrides: <what legitimately differs here, or none>
known-divergence: <unresolved drift, or none>
last-reconciled: <date>
```

## Trial card scaffold

At **design** time, leave Result empty. Fill it only in **review**.

```markdown
# Trial — <Agent Name> (<start> → <review>)

| Test | Scenario | Expected | Result |
| :--- | :------- | :------- | :----- |
| Core job | | | |
| Boundary | | | |
| Authority | | | |

**Decision at review:** activate | revise (<change>) | retire
**If not reviewed by <date>:** trial expires; status becomes `dormant` and the
deployment entry is proposed `enabled: false`.
```

## Rejection scaffold

Used when the gate says no. This is a complete output.

```markdown
# Not an agent — <need in one line>

- **Mode:** reject
- **Durable outcome?** yes / no — <evidence>
- **Gate:** failed / human job
- **Recommended shape:** human | skill | routine | workflow | subagent | mode
- **Why not an agent:** <one short paragraph>
- **What to make instead:** <the actual next artefact>
- **Revisit if:** <the change that would flip the gate>
```
