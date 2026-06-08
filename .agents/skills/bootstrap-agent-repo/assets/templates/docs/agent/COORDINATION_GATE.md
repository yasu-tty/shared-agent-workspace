# Coordination Gate

## Purpose

The coordination gate is a plan-time check for Codex, Claude Code, and human maintainers. Use it before implementation starts to ask, confirm, and record which agents are available, which execution mode is selected, whether parallel execution is allowed, which files each agent may touch, and which files are locked.

This gate does not route work automatically. It does not enable hooks, create lock files, run an external orchestrator, or dispatch work to Codex or Claude Code. If only one agent is available, the plan must still work in `single-agent` or `planning-only` mode.

`multi_agent = true` means the repo may support multi-agent collaboration. It is not permission for parallel execution.

## File-changing task gate

For file-changing work, create or update `plans/*.md` before the first non-plan file edit. Updating an existing active plan is acceptable when the work is clearly within that plan's scope.

The default exceptions are read-only investigation, creating or updating the plan itself, and validation commands that do not modify files. Docs-only edits, formatter writes, generated-file updates, and tiny one-file fixes are not exceptions when they change files.

## Plan-time record

Every plan that gates file-changing work must include `## Agreement summary`, `## Agreement matrix`, `## Decision log`, `## Routing and execution`, and `## Work file activity`.

The agreement sections must record:

- Overall agreement state
- Blocking unresolved decisions
- Required approvers / reviewers
- Matrix status
- Agreement matrix rows for current proposed, agreed, rejected, blocked, or superseded decisions
- Decision log entries for explicit user / human maintainer decisions

`## Routing and execution` must record:

- Available agents:
  - Codex: `available`, `unavailable`, or `unknown`
  - Claude Code: `available`, `unavailable`, or `unknown`
- Selected execution mode:
  - `single-agent`
  - `sequential-handoff`
  - `parallel-isolated`
  - `planning-only`
- Primary executor
- Reviewer / validator
- Parallel execution allowed:
  - `no`
  - `separate-files-only`
  - `separate-worktrees-only`
  - `yes`
- File ownership claims:
  - Codex planned files
  - Claude Code planned files
- Locked files
- Handoff checkpoint
- Conflict resolution owner
- Reason for routing decision
- Work file activity rows for active, paused, handoff-ready, reviewing, validating, done, or blocked work

## Execution modes

### `single-agent`

One agent performs planning, implementation, and validation. This is the default when only one agent is available.

### `sequential-handoff`

One agent implements, then updates the plan Status, Progress log, validation notes, and handoff notes before another agent reviews or validates. Simultaneous editing is not allowed.

### `parallel-isolated`

Multiple agents may work at the same time only when planned files are clearly separated and locked files are not touched. Do not use this mode for shared policy files, matching root/template files, or files that require a single design decision.

### `planning-only`

The plan is created, but implementation ownership is not decided. Use this when agent availability is unknown or a user decision is required.

## Implementation ambiguity gate

Before editing any non-plan file, confirm that the active plan is executable. A plan is not executable when any of these are true:

- `State` is `Draft`
- selected execution mode is `planning-only`
- primary executor is `None`, blank, or undecided
- planned files are blank or do not identify the non-plan files to edit
- locked files include the target non-plan files and the plan does not record an explicit unlock decision
- `Blocking unresolved decisions` is not `None`
- Agreement matrix has an unresolved row with `Blocks implementation: yes`
- an owner decision required for implementation is still unresolved
- `Matrix status` is `needs-update`
- `Matrix status` is `not-yet-backfilled`
- `Matrix status` is `omitted-by-user` without explicit user / human maintainer evidence for omitting it

The agreement gate is intentionally minimal here. The detailed Agreement matrix, Decision log, row state, matrix status, and evidence rules live in `.agents/PLANS.md`.

If a non-executable plan receives an ambiguous instruction such as "Implement the plan", do not edit non-plan files. First confirm the exact implementation scope and update the plan with execution mode, primary executor, planned files, locked files, validation, and rollback.

If the user explicitly names a plan and asks to start implementation, record that approval in the plan before editing shared policy, templates, source files, or other non-plan files. For plans that use agreement tracking, record the approval in Status notes, Decision log or Progress log, and Work file activity as appropriate.

## Availability rules

- If agent availability is not stated, the planner must ask during plan creation.
- If the user already states "Codex only", "Claude only", "Claude review only", or equivalent, record that decision and do not ask again.
- If an agent is `unavailable` or `unknown`, do not assign implementation work to that agent.
- If both agents are `available`, do not automatically choose parallel execution. Default to `single-agent` or `sequential-handoff` unless `parallel-isolated` is explicitly safe.

## Parallel execution controls

Parallel execution is forbidden or must be limited to `separate-worktrees-only` when any of these are true:

- planned files overlap
- `AGENT_RULES.md` changes
- `.agents/PLANS.md` changes
- `plans/template.md` changes
- `README.md` changes
- both `AGENTS.md` and `CLAUDE.md` receive design changes
- `docs/agent/OWNERSHIP.md` changes
- `docs/agent/AGENT_ROLES.md` changes
- `docs/agent/HANDOFF_PROTOCOL.md` changes
- `docs/agent/COMPONENT_INVENTORY.md` changes
- `.agents/skills/bootstrap-agent-repo/**` changes
- `.agents/skills/bootstrap-agent-repo/assets/templates/**` changes
- root/template synchronized files change
- bootstrap scripts change
- hook scripts change
- the worktree has unrelated uncommitted changes
- any agent availability is `unknown`
- conflict risk is High
- Agreement matrix has unresolved blocking decisions
- rollback path is unclear

Use `parallel-isolated` only when planned files are separated, locked files are respected, worktree state is safe, and the plan records file ownership for each agent.

## Locked files and ownership claims

Locked files are files or paths that no agent may edit during the plan unless the plan is updated first. Use locked files for high-risk shared policy, root/template sync pairs, hook scripts, generated files, or any path that would create unsafe overlap.

File ownership claims must list the files each agent plans to touch. If a file is needed by both agents, do not proceed in parallel. Switch to `single-agent`, `sequential-handoff`, or ask the user for a decision.

## Handoff and conflict owner

For `sequential-handoff`, the implementing agent must update the plan Status, Progress log, validation notes, and handoff checkpoint before review or validation starts.

For any conflict, the plan must name a conflict resolution owner. Do not resolve conflicts opportunistically when the design intent is unclear.

## Question template

Use this wording when availability or execution mode is not already clear:

```text
この plan の実行モードを確認してください。

Available agents:
1. Codex は使用できますか？ yes / no / unknown
2. Claude Code は使用できますか？ yes / no / unknown

Execution mode:
1. single-agent: 片方の agent のみで実装・検証
2. sequential-handoff: 一方が実装し、もう一方が review / validation
3. parallel-isolated: ファイル担当を分離できる場合のみ並行
4. planning-only: plan のみ作成し、実装担当は未決定

Parallel execution:
- no
- separate-files-only
- separate-worktrees-only
- yes

Planned file ownership:
- Codex:
- Claude Code:

Locked files:
-
```

## Safe examples

- Codex implements, then Claude Code reviews after the plan handoff checkpoint is updated.
- Claude Code updates `.claude/*` while Codex updates `.codex/*`, with no shared files and no root/template sync.
- Codex creates the plan only because Claude Code availability is unknown.
- Codex records an explicit implementation approval in the plan before editing shared policy or template files.

## Unsafe examples

- Codex and Claude Code both edit `README.md`.
- Codex edits a root file while Claude Code edits the matching `assets/templates/` copy.
- One agent validates while another continues editing the same files.
- A plan assigns work to Claude Code when Claude Code availability is unknown.
- A plan selects parallel execution for `AGENT_RULES.md` or `.agents/PLANS.md`.
- An agent infers `agreed` from existing policy or from the absence of unresolved questions.
- An agent edits non-plan files while `Matrix status` is `needs-update`.
