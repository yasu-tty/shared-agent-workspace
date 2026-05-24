---
name: bootstrap-agent-repo
description: Bootstrap a repo with a Codex + Claude Code collaborative AI-agent template. Use for repo setup, standard directory scaffolding, and reapplying the common AI-agent starter structure.
license: Apache-2.0
metadata:
  author: "Yasu (@yasu-tty)"
  version: "0.1.0"
allowed-tools: Read(*),Write(*),Edit(*),Glob(*),Grep(*),Bash(python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py *),Bash(git status),Bash(git diff *)
---

# Bootstrap Agent Repo

This is a Claude Code adapter. The canonical startup skill lives in `.agents/skills/bootstrap-agent-repo/`.

1. Read `AGENT_RULES.md`
2. Read `.agents/skills/bootstrap-agent-repo/SKILL.md`
3. Read only the needed supporting file:
   - `.agents/skills/bootstrap-agent-repo/references/USAGE.md`
   - `.agents/skills/bootstrap-agent-repo/references/LAYOUT.md`
4. Prefer a dry run first:
   - `python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --dry-run`
5. Apply:
   - `python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --yes`
6. Use `--force --backup` only when replacing existing files is intended, and confirm dry-run does not include the target root `README.md`.
7. Review `.agents/skills/bootstrap-agent-repo/references/POST_BOOTSTRAP_CHECKLIST.md`
8. Review `docs/agent/PROJECT_CONTEXT.md` and `docs/agent/OWNERSHIP.md`, then assign or replace placeholder roles before multi-agent work.
9. Review `docs/agent/COORDINATION_GATE.md` and `docs/agent/HANDOFF_PROTOCOL.md` before parallel coding.
10. Keep root files and `.agents/skills/bootstrap-agent-repo/assets/templates/` synchronized when maintaining this template.
