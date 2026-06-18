---
name: feature-planning
description: Create or update plans/*.md for file-changing, broad, risky, or multi-step work in this repo.
license: Apache-2.0
metadata:
  author: "Yasu (@yasu-tty)"
  version: "0.1.0"
allowed-tools: Read(*),Edit(*),Write(*),Glob(*),Grep(*),Bash(git status),Bash(git diff *)
---

# Feature Planning

Use this skill for plan creation and for workflow rehydration. Reinvoke it when starting file-changing work, resuming after context compaction, resuming a session, sending or receiving handoff, receiving review feedback or review results, producing review results for a target plan, handling agent participation changes, expanding scope, moving from planning to implementation, moving from implementation to validation, resuming after a blocker, or preparing a completion / handoff checkpoint.

Do not treat chat history as the source of truth for current work state. For existing work, read the active plan or checkpoint before loading detailed references and recover:

- current actor
- participating agents
- target files / paths
- locked files
- completed work
- current status
- next action
- unresolved decisions
- blockers
- review findings
- validation results
- handoff checkpoint
- last updated information

Then follow this procedure:

When review feedback or review results are received, or when producing review results for a target plan, do not finish with only an oral response. Record findings, accepted / rejected / deferred status, required action, next owner, validation results, and handoff checkpoint in the active plan or checkpoint. If the user explicitly requests read-only review only, do not update the plan and state that constraint in the response. Use the plan's `Review findings`, `Work file activity`, `Progress log`, `Validation`, and the `Routing and execution` `Handoff checkpoint` field where available.

When starting file-changing work or resuming a session, read `docs/agent/PROJECT_CONTEXT.md` before the first non-plan file edit and check repository-specific data handling, external tool usage, approval-required operations, and areas that must not be changed without explicit approval.

1. Read `AGENT_RULES.md`
2. If an active plan or checkpoint exists, perform the state recovery pass above before selecting detailed references
3. When starting file-changing work or resuming a session, read `docs/agent/PROJECT_CONTEXT.md`
4. Read `.agents/PLANS.md`
5. For new plans or material plan updates, read `plans/template.md` and `plans/README.md`
6. For ownership, file ownership, locked files, or scope expansion, read `docs/agent/OWNERSHIP.md`
7. For handoff, review feedback, producing target plan review results, or agent participation / withdrawal, read `docs/agent/HANDOFF_PROTOCOL.md`
8. For routing, execution mode, parallel execution, or implementation readiness, read `docs/agent/COORDINATION_GATE.md`
9. For validation decisions, read `docs/agent/TESTING_POLICY.md`
10. For file-changing work, create or update `plans/*.md` before the first non-plan file edit; the only default exceptions are read-only investigation, plan creation / update itself, and validation commands that do not modify files
11. Inspect related files and existing plans
12. Create or update `plans/*.md` from `plans/template.md` when needed
13. Include or update `## Status` according to `.agents/PLANS.md`; use `Implementation complete` before final review, validation, commit, or merge is done
14. When changing `State`, check that Summary, Status / Result / Remaining work, Agreement summary, Agreement matrix `State` / `Blocks implementation` / `Next action`, Scope, Routing and execution, Work file activity, Review findings, Rollback notes, and Validation match the new current state
15. Treat Decision log and Progress log as historical surfaces; do not rewrite valid history only because current State changed, and update current-state surfaces when they conflict with historical wording
16. Fill `Agreement summary`, `Agreement matrix`, and `Decision log`; never infer `agreed` without explicit user / human maintainer evidence
17. Track unresolved decisions in Agreement matrix, not a standard Open questions section
18. Fill `Routing and execution`; check agent availability, do not auto-route work, and record execution mode, parallel allowance, file ownership claims, locked files, handoff checkpoint, and routing notes
19. Fill `Work file activity` with actor, role, task, files / paths, operation, status, conflict risk, last update, and next action
20. Capture ownership area, planned files, out-of-scope files, affected agents, review owner, conflict risk, handoff notes, scope expansion rule, tests, and rollback
21. Update Work file activity and Progress log at interruption-safe boundaries, review feedback receipt, or handoff points
22. Treat `Draft`, `planning-only`, executorless, file-ambiguous, locked, stale-agreement, or unresolved-blocking-agreement plans as non-executable; do not edit non-plan files from an ambiguous `Implement the plan` instruction until scope, routing, and agreement state are confirmed in the plan
