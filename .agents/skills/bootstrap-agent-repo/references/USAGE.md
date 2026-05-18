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

Dry-run has no filesystem side effects. It also reports whether files would be created, overwritten, skipped, or left unchanged.

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

Review the dry-run output before applying. After `--force --backup --yes`, compare `.agents/bootstrap-backups/<timestamp>/` with the overwritten files and confirm that repo-specific information was not erased by generic template content.

If the reapply reveals changes that should become part of the shared distribution, move those edits into `assets/templates/`. If a difference must remain only in the root repo because it is repo-specific, keep it out of `assets/templates/` and record that intentional drift in the active plan or repository docs.

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

Use this in review or CI when maintaining this template repo. It compares files in `assets/templates/` with their root counterparts and reports `MISSING`, `DIFF`, `INTENTIONAL_DIFF`, `SYMLINK`, or `NOT_FILE`.

`DIFF` is normally a maintenance failure for this template repo. The exception is an intentional root-only customization that should not be distributed generically; when that happens, leave the file out of `assets/templates/` and document the drift explicitly so later maintainers do not mistake it for an accidental sync miss.

`README.md` is an intentional content-diff exception. The root `README.md` describes this public project, while `assets/templates/README.md` is starter content that may be installed into a target repository. `--check-root-sync` reports this as `INTENTIONAL_DIFF README.md` and does not fail for that content difference. Missing files, symlinks, directories, and all non-README content differences still fail.

## What gets installed

- `AGENT_RULES.md`
- `AGENTS.md`
- `CLAUDE.md`
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
- Identical files are reported as `identical` and are not rewritten.
- Overwritten files can be backed up with `--backup` under a UTC timestamp with microsecond precision.
- The script refuses writes outside the target path.
- Symlinks in the template source tree are rejected instead of copied.
- Local, dangerous, or user-home examples stay under `.example` files or `templates/nonshared/`.
