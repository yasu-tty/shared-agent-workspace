# Component Inventory

Use this inventory before changing files. Keep the ownership areas aligned with `docs/agent/OWNERSHIP.md`.

| Path / Component | Purpose | Ownership area | Typical owner | Risk level | Notes |
|---|---|---|---|---|---|
| `AGENT_RULES.md` | Common operating rules and shared source of truth | Shared policy | Human maintainer / documentation agent | High | Check `.agents/PLANS.md` and ownership docs before policy changes |
| `.agents/PLANS.md` | Plan document specification | Planning process | Planning agent / review agent | High | Changes affect all future plans |
| `plans/` | Living plans and progress logs | Active work coordination | Current task owner | Medium | Update progress logs during handoff or scope change |
| `docs/agent/OWNERSHIP.md` | Repository consumers, ownership matrix, and permission levels | Ownership governance | Human maintainer / review agent | High | Replace placeholders in project repos before parallel work |
| `docs/agent/AGENT_ROLES.md` | Reusable agent role templates | Role assignment | Planning agent / human maintainer | Medium | Use when assigning agents or reviewers |
| `docs/agent/HANDOFF_PROTOCOL.md` | Work start, progress, completion, and conflict protocol | Handoff process | All agents | High | Required for multi-agent or cross-boundary work |
| `docs/agent/COORDINATION_GATE.md` | Plan-time agent availability, execution mode, parallel control, file ownership, locked files, and routing record | Planning process / coordination governance | Planning agent / review agent | High | Use with `.agents/PLANS.md`, ownership, roles, and handoff docs before implementation |
| `docs/agent/COMPONENT_INVENTORY.md` | Component map and risk levels | Shared documentation | Documentation agent | Medium | Keep ownership areas consistent with this table |
| `docs/agent/SETUP.md` | Setup and activation guide | Onboarding | Documentation agent | Medium | Check after changing bootstrap or adapters |
| `docs/agent/TESTING_POLICY.md` | Testing and validation expectations | Quality process | Test and quality agent | High | Required before changing test strategy |
| `.agents/skills/bootstrap-agent-repo/` | Canonical bootstrap skill and template source | Bootstrap template | Template maintenance agent | High | Keep root files and `assets/templates/` synchronized |
| `.agents/skills/feature-planning/` | Shared feature planning skill | Planning process | Planning agent | High | Must reflect `.agents/PLANS.md` requirements |
| `AGENTS.md` | Codex entry adapter | Codex adapter | Codex maintainer | Medium | Keep thin; reference shared docs instead of duplicating rules |
| `.codex/` | Codex project config, hooks, and agents | Codex adapter | Codex maintainer | Medium | Adapter only; shared policy belongs in `.agents/` or `docs/agent/` |
| `CLAUDE.md` | Claude Code entry adapter | Claude adapter | Claude maintainer | Medium | Keep thin; use `@` references to shared docs |
| `.claude/` | Claude settings, rules, agents, and skill adapters | Claude adapter | Claude maintainer | Medium | Shared skills remain canonical under `.agents/skills/` |
| `.mcp.json.example` | Shared MCP example | Tooling example | Human maintainer | Medium | Do not place secrets in shared examples |
| `templates/nonshared/` | User-home, project-local, or admin-only examples | Nonshared samples | Local user / admin | Low | Copy only what is needed; do not enable by default |
| `scripts/hooks/` | Optional hook scripts used by adapters | Tooling / quality | Tooling owner | Medium | Check hook side effects before enabling |

## Component categories

- Shared components: `AGENT_RULES.md`, `.agents/`, `plans/`, `docs/agent/`, and `.mcp.json.example`.
- Feature-specific components: project-specific source, tests, and docs added by adopting repositories; define their ownership in `docs/agent/OWNERSHIP.md`.
- Adapter components: `AGENTS.md`, `CLAUDE.md`, `.codex/`, and `.claude/`; keep these thin and point back to shared components.
- High-risk components: shared policy, plan specification, ownership docs, handoff protocol, testing policy, bootstrap script/assets, public contracts, schema, auth, billing, deployment, and CI.

## Shared core

- `AGENT_RULES.md`
  共通規約の正本

- `.agents/PLANS.md`
  計画書の仕様

- `plans/`
  案件ごとの計画と進捗

- `docs/agent/`
  setup, inventory, coordination gate, testing policy などの補助資料

- `.agents/skills/bootstrap-agent-repo/`
  startup / bootstrap 用の canonical skill

- `.agents/skills/feature-planning/`
  計画作成用 skill

- `.mcp.json.example`
  MCP 設定の共有サンプル。実設定は必要範囲だけ採用する

## Codex adapters

- `AGENTS.md`
- `.codex/config.toml`
- `.codex/agents/*.toml`
- `.codex/hooks.json.example`

## Claude adapters

- `CLAUDE.md`
- `.claude/settings.json.example`
- `.claude/settings.local.json.example`
- `.claude/rules/*.md`
- `.claude/agents/*.md`
- `.claude/skills/*`
  共通 skill への薄い adapter。canonical source は `.agents/skills/*`

## Nonshared samples

- `templates/nonshared/user-home/`
- `templates/nonshared/project-local/`
- `templates/nonshared/admin/`

## Canonical bootstrap source

- `.agents/skills/bootstrap-agent-repo/SKILL.md`
  明示起動向けの短い入口

- `.agents/skills/bootstrap-agent-repo/assets/templates/`
  target repo に展開されるテンプレート本文

- `.agents/skills/bootstrap-agent-repo/references/`
  詳細な使用方法、設計判断、bootstrap 後チェックリスト

- `.agents/skills/bootstrap-agent-repo/scripts/bootstrap.py`
  dry-run 対応、冪等、安全な上書き方針つきの展開 script
