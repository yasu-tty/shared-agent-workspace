# Ownership

## Purpose

This document records who reads this repository, which areas they own, and how agents or humans coordinate safe changes across boundaries. Keep shared ownership rules here instead of duplicating them in Codex- or Claude-specific adapter files.

## Repository consumers

Use this list to make visible who depends on this repository's instructions and templates.

| Consumer | Usage | Notes |
|---|---|---|
| Human maintainers | Define ownership, approve high-risk changes, review final output | Replace this placeholder with real team names when adopting the template |
| Feature implementation agents | Implement scoped changes in assigned ownership areas | Must follow the active plan and handoff protocol |
| Test and quality agents | Validate behavior, test coverage, and rollback readiness | May request clarification from area owners |
| Review agents | Review diffs for correctness, risks, and missing coordination | Should not silently expand implementation scope |
| Documentation agents | Update shared docs, plans, and onboarding materials | Keep adapter files thin and reference shared docs |

## Ownership matrix

Update this table before parallel or multi-agent work. The rows below are examples and should be replaced or refined for the target project.

| Area | Primary owner | Review owner | Allowed agents | Ask before changing | Notes |
|---|---|---|---|---|---|
| Authentication | Agent A / Human owner | Agent D | Agent A, Agent D | Public API, session model, permissions | Keep auth changes small and reviewed |
| Billing | Agent B / Human owner | Agent D | Agent B | External API, pricing, invoices | Treat as high-risk |
| UI | Agent C | Agent D | Agent C | Shared components, routing | Avoid unrelated refactors |
| Tests | Agent D | Area owner | All agents | Snapshot rewrites, flaky test changes | Test changes must explain intent |
| Documentation | Documentation agent | Area owner | All agents | Policy changes, ownership changes | Shared rules belong in `docs/agent/` or `.agents/` |
| CI / deployment | Human owner / Release agent | Review agent | Assigned agents only | Pipelines, secrets, release gates | Treat deployment-impacting changes as high-risk |

## Change permission levels

| Level | Meaning |
|---|---|
| Own | Freely change within the declared task scope and planned files for the assigned ownership area. |
| Review | May review, comment, suggest changes, or request tests, but should not directly modify unless assigned. |
| Consult | Must ask the primary owner or review owner before changing. |
| No-touch | Do not modify unless explicitly assigned in the plan or by the owner. |

## Cross-boundary change rules

- If you find a problem outside your assigned area, report it first instead of fixing it silently.
- If the change scope must expand, state the reason, additional files or areas, impact, and reviewer needed before editing.
- Do not mix specification changes and refactoring in the same change unless the plan explicitly allows it.
- Treat changes that affect public API, schema, authentication, authorization, billing, payment, deployment, or CI as high-risk.
- Do not change ownership metadata only to justify an already-made code change; update ownership before or during planning.
- Prefer small, reviewable handoffs over broad edits across unrelated ownership areas.

## Review responsibility

- The primary owner is responsible for intent, behavior, and area-specific correctness.
- The review owner is responsible for cross-area risk, consistency, and validation quality.
- Test ownership follows the changed area unless the plan assigns a dedicated test and quality agent.
- Documentation ownership follows the changed behavior or policy; shared process docs require review from the template maintainer or equivalent.

## Escalation rules

- Escalate when two agents need the same file, public contract, schema, auth, billing, deployment, or CI path.
- Escalate when the implementation requires changing files listed as out of scope in the active plan.
- Escalate when test failures are unexplained or appear unrelated to the current task.
- Escalate when a merge conflict would require choosing between two agents' design intents.
- Escalation should include the current task, affected files, risk, proposed next step, and owner or reviewer needed.

## Maintenance notes

- Update this document when new agents, teams, ownership areas, or high-risk components are introduced.
- Keep sample rows generic in templates; project-specific repositories should replace placeholders during onboarding.
- Keep `docs/agent/COMPONENT_INVENTORY.md` aligned with the ownership areas defined here.
- Keep plan documents aligned with this file by filling the ownership and coordination section in each active plan.
