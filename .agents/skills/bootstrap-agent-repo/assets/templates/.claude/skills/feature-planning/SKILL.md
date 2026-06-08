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

1. Read `AGENT_RULES.md`
2. Read `.agents/PLANS.md`
3. Read `docs/agent/OWNERSHIP.md`
4. Read `docs/agent/HANDOFF_PROTOCOL.md`
5. Read `docs/agent/COORDINATION_GATE.md`
6. For file-changing work, create or update `plans/*.md` before the first non-plan file edit; the only default exceptions are read-only investigation, plan creation / update itself, and validation commands that do not modify files
7. Inspect related files and existing plans
8. Create or update `plans/*.md` from `plans/template.md`
9. Include or update `## Status` according to `.agents/PLANS.md`; use `Implementation complete` before final review, validation, commit, or merge is done
10. When changing `State`, check that Summary, Status / Result / Remaining work, Agreement summary, Agreement matrix `State` / `Blocks implementation` / `Next action`, Scope, Routing and execution, Work file activity, Rollback notes, and Validation match the new current state
11. Treat Decision log and Progress log as historical surfaces; do not rewrite valid history only because current State changed, and update current-state surfaces when they conflict with historical wording
12. Fill `Agreement summary`, `Agreement matrix`, and `Decision log`; never infer `agreed` without explicit user / human maintainer evidence
13. Track unresolved decisions in Agreement matrix, not a standard Open questions section
14. Fill `Routing and execution`; check agent availability, do not auto-route work, and record execution mode, parallel allowance, file ownership claims, locked files, handoff checkpoint, and routing notes
15. Fill `Work file activity` with actor, role, task, files / paths, operation, status, conflict risk, last update, and next action
16. Capture ownership area, planned files, out-of-scope files, affected agents, review owner, conflict risk, handoff notes, scope expansion rule, tests, and rollback
17. Update Work file activity and Progress log at interruption-safe boundaries or handoff points
18. Treat `Draft`, `planning-only`, executorless, file-ambiguous, locked, stale-agreement, or unresolved-blocking-agreement plans as non-executable; do not edit non-plan files from an ambiguous `Implement the plan` instruction until scope, routing, and agreement state are confirmed in the plan
