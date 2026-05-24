# Usage

Run commands from the target repo root unless you are bootstrapping another path.

## Basic

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --yes
```

## Dry run

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --dry-run
```

Dry-run has no filesystem side effects. It also reports whether files would be created, overwritten, preserved, skipped, or left unchanged.

## Reapply standards

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --force --backup --yes
```

Use `--force` only when you want the template to replace files whose content differs. Add `--backup` to save overwritten files under `.agents/bootstrap-backups/<timestamp>/`.

For a maintained repo that may still carry an older bootstrap skill version, use the full reapply flow:

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --dry-run
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --check-root-sync
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --force --backup --yes
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --dry-run
```

Review the dry-run output before applying. Confirm that the target root `README.md` is not listed for create or overwrite. After `--force --backup --yes`, compare `.agents/bootstrap-backups/<timestamp>/` with the overwritten files and confirm that `docs/agent/PROJECT_CONTEXT.md` remained preserved.

`docs/agent/PROJECT_CONTEXT.md` is project-owned. Bootstrap creates it when missing, then reports it as `preserve` on later runs and never overwrites it, even with `--force`.

The target root `README.md` is project-owned and is not distributed by bootstrap.

Keep repository-specific context in `docs/agent/PROJECT_CONTEXT.md`. Treat other unexpected differences as template maintenance work.

## Copy a subset

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --include 'docs/agent/*' --dry-run
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --exclude '.claude/*' --yes
```

Patterns are matched against repo-relative POSIX paths.

## Inspect the template

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --list
```

## Check root/template sync

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --check-root-sync
```

Use this in review or CI when maintaining this template repo. It compares files in `assets/templates/` with their root counterparts and reports `MISSING`, `DIFF`, `FORBIDDEN_TEMPLATE`, `PROJECT_OWNED_DIFF`, `SYMLINK`, or `NOT_FILE`.

`DIFF` is normally a maintenance failure for this template repo. Only move a change into `assets/templates/` when it is generic, shareable, and intended for all adopting repositories. Move repository-specific context into `docs/agent/PROJECT_CONTEXT.md`. Only documented exceptions such as `PROJECT_OWNED_DIFF docs/agent/PROJECT_CONTEXT.md` should remain.

`FORBIDDEN_TEMPLATE README.md` means root `README.md` was added back to distributed templates. Remove `assets/templates/README.md`; bootstrap must not create or overwrite an adopting repository's root README.

`docs/agent/PROJECT_CONTEXT.md` is a project-owned content-diff exception. The file must exist in both root and `assets/templates/`, but root content may diverge from the section-only template stub. `--check-root-sync` reports this as `PROJECT_OWNED_DIFF docs/agent/PROJECT_CONTEXT.md` and does not fail for that content difference. Missing files, symlinks, and directories still fail.

## What gets installed

- `AGENT_RULES.md`
- `AGENTS.md`
- `CLAUDE.md`
- `docs/agent/PROJECT_CONTEXT.md`
- `.agents/PLANS.md`
- `.agents/skills/bootstrap-agent-repo/`
- `.agents/skills/feature-planning/`
- `plans/README.md`
- `plans/template.md`
- `docs/agent/*`
- `.codex/config.toml`
- `.codex/hooks.json.example`
- `.codex/agents/*`
- `.claude/settings.json.example`
- `.claude/settings.local.json.example`
- `.claude/rules/*`
- `.claude/agents/*`
- `.claude/skills/*`
- `.mcp.json.example`
- `templates/nonshared/*`

## Safety

- Existing files are never overwritten unless `--force` is passed.
- The target root `README.md` is never created or overwritten by bootstrap.
- Project-owned create-only files such as `docs/agent/PROJECT_CONTEXT.md` are never overwritten and are reported as `preserve`.
- Identical files are reported as `identical` and are not rewritten.
- Overwritten files can be backed up with `--backup` under a UTC timestamp with microsecond precision.
- The script refuses writes outside the target path.
- Symlinks in the template source tree are rejected instead of copied.
- Local, dangerous, or user-home examples stay under `.example` files or `templates/nonshared/`.
