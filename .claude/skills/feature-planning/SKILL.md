---
name: feature-planning
description: Create or update plans/*.md for broad, risky, or multi-step work in this repo.
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
6. Inspect related files and existing plans
7. Create or update `plans/*.md`
8. Include or update `## Status` according to `.agents/PLANS.md`; use `Implementation complete` before final review, validation, commit, or merge is done
9. Fill `Routing and execution`; check agent availability, do not auto-route work, and record execution mode, parallel allowance, file ownership claims, locked files, handoff checkpoint, and routing notes
10. Capture ownership area, planned files, out-of-scope files, affected agents, review owner, conflict risk, handoff notes, scope expansion rule, tests, and rollback
