# Layout

## Shared core

Shared core is the source of truth for collaboration across agents.

- `AGENT_RULES.md`: common operating rules
- `.agents/PLANS.md`: plan document specification
- `.agents/skills/bootstrap-agent-repo/`: canonical startup skill
- `.agents/skills/feature-planning/`: shared plan creation skill
- `plans/`: living plans and progress logs
- `docs/agent/`: inventory, setup, ownership, roles, handoff protocol, testing policy, and supporting docs
- `.mcp.json.example`: shared MCP example, not enabled by default

## Codex adapter

Codex adapter files should stay thin and point back to shared core.

- `AGENTS.md`
- `.codex/config.toml`
- `.codex/agents/*.toml`
- `.codex/hooks.json.example`

## Claude Code adapter

Claude adapter files should stay thin and point back to shared core.

- `CLAUDE.md`
- `.claude/settings.json.example`
- `.claude/settings.local.json.example`
- `.claude/rules/*.md`
- `.claude/agents/*.md`
- `.claude/skills/*`

## Nonshared samples

Files under `templates/nonshared/` are examples for user-home, project-local, or admin-specific setup. They are copied as examples only and should not be treated as shared defaults.

## Template source

`assets/templates/` contains the files copied into target repos. The bootstrap skill itself is installed from `.agents/skills/bootstrap-agent-repo/` so the target repo can re-run or customize the same startup workflow later.
