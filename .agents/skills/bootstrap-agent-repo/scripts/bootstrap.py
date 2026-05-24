#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fnmatch
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


EXCLUDE_FROM_SELF_INSTALL = {
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
}

NON_DISTRIBUTED_TEMPLATE_PATHS = {
    "README.md",
}

PROJECT_OWNED_CREATE_ONLY_PATHS = {
    "docs/agent/PROJECT_CONTEXT.md",
}


@dataclass(frozen=True)
class CopyPlan:
    rel: str
    source: Path
    target: Path
    action: str
    reason: str


def as_posix(path: Path) -> str:
    return path.as_posix()


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def matches_any(rel: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, pattern) for pattern in patterns)


def should_copy(rel: str, includes: list[str], excludes: list[str]) -> bool:
    if includes and not matches_any(rel, includes):
        return False
    return not matches_any(rel, excludes)


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            rel = as_posix(path.relative_to(root))
            raise SystemExit(f"Refusing symlink in template source: {rel}")
        if path.is_file():
            files.append(path)
    return files


def check_root_sync(repo_root: Path, templates_dir: Path) -> int:
    mismatches = 0
    for source in iter_files(templates_dir):
        rel_path = source.relative_to(templates_dir)
        rel = as_posix(rel_path)
        if rel in NON_DISTRIBUTED_TEMPLATE_PATHS:
            print(f"FORBIDDEN_TEMPLATE {rel}")
            mismatches += 1
            continue

        root_file = repo_root / rel_path

        if not root_file.exists():
            print(f"MISSING {rel}")
            mismatches += 1
            continue

        if root_file.is_symlink():
            print(f"SYMLINK {rel}")
            mismatches += 1
            continue

        if not root_file.is_file():
            print(f"NOT_FILE {rel}")
            mismatches += 1
            continue

        if root_file.read_bytes() != source.read_bytes():
            if rel in PROJECT_OWNED_CREATE_ONLY_PATHS:
                print(f"PROJECT_OWNED_DIFF {rel}")
                continue
            print(f"DIFF {rel}")
            mismatches += 1

    if mismatches:
        print(f"root_template_sync=failed mismatches={mismatches}")
        return 1

    print("root_template_sync=ok")
    return 0


def build_plan(
    source_root: Path,
    target_root: Path,
    *,
    prefix: Path = Path(),
    force: bool,
    includes: list[str],
    excludes: list[str],
) -> list[CopyPlan]:
    plans: list[CopyPlan] = []

    for source in iter_files(source_root):
        if any(part in EXCLUDE_FROM_SELF_INSTALL for part in source.parts):
            continue

        rel_path = prefix / source.relative_to(source_root)
        rel = as_posix(rel_path)
        if rel in NON_DISTRIBUTED_TEMPLATE_PATHS:
            continue

        if not should_copy(rel, includes, excludes):
            continue

        target = (target_root / rel_path).resolve()
        if not is_relative_to(target, target_root):
            raise SystemExit(f"Refusing to write outside target: {rel}")

        if not target.exists():
            plans.append(CopyPlan(rel, source, target, "create", "missing"))
            continue

        if target.is_dir():
            plans.append(CopyPlan(rel, source, target, "skip", "target is a directory"))
            continue

        if rel in PROJECT_OWNED_CREATE_ONLY_PATHS:
            plans.append(CopyPlan(rel, source, target, "preserve", "project-owned; never overwritten"))
            continue

        if target.read_bytes() == source.read_bytes():
            plans.append(CopyPlan(rel, source, target, "identical", "same content"))
            continue

        if force:
            plans.append(CopyPlan(rel, source, target, "overwrite", "different content"))
        else:
            plans.append(CopyPlan(rel, source, target, "skip", "exists; use --force to overwrite"))

    return plans


def copy_file(plan: CopyPlan, *, backup_root: Path | None) -> None:
    if plan.action == "overwrite" and backup_root is not None:
        backup_path = backup_root / plan.rel
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(plan.target, backup_path)

    plan.target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(plan.source, plan.target)


def apply_plan(plans: list[CopyPlan], *, dry_run: bool, backup_root: Path | None) -> None:
    if dry_run:
        return

    for plan in plans:
        if plan.action in {"create", "overwrite"}:
            copy_file(plan, backup_root=backup_root)


def make_backup_root(target_dir: Path) -> Path:
    base = target_dir / ".agents" / "bootstrap-backups"
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    candidate = base / stamp
    suffix = 1
    while candidate.exists():
        candidate = base / f"{stamp}-{suffix:02d}"
        suffix += 1
    return candidate


def print_plan(plans: list[CopyPlan], *, mode: str, target_dir: Path, backup_root: Path | None) -> None:
    counts: dict[str, int] = {}
    for plan in plans:
        counts[plan.action] = counts.get(plan.action, 0) + 1

    print(f"[{mode}] target={target_dir}")
    if backup_root is not None:
        print(f"backup_dir={backup_root}")

    for action in ("create", "overwrite", "identical", "preserve", "skip"):
        print(f"{action}={counts.get(action, 0)}")

    for plan in plans:
        marker = {
            "create": "+",
            "overwrite": "!",
            "identical": "=",
            "preserve": "~",
            "skip": "-",
        }[plan.action]
        print(f"  {marker} {plan.rel} ({plan.reason})")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bootstrap a Codex + Claude Code AI agent coordination template.")
    parser.add_argument("--target", required=True, help="Target repository directory")
    parser.add_argument("--force", action="store_true", help="Overwrite files whose content differs")
    parser.add_argument("--backup", action="store_true", help="Back up overwritten files under .agents/bootstrap-backups")
    parser.add_argument("--dry-run", action="store_true", help="Show planned changes without writing anything")
    parser.add_argument("--list", action="store_true", help="List template files and exit")
    parser.add_argument("--check-root-sync", action="store_true", help="Verify root files match assets/templates and exit")
    parser.add_argument("--yes", action="store_true", help="Accepted for non-interactive startup flows; no prompts are used")
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="Only copy paths matching this glob. Can be repeated. Matches repo-relative POSIX paths.",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Skip paths matching this glob. Can be repeated. Matches repo-relative POSIX paths.",
    )
    parser.add_argument(
        "--no-self-skill",
        action="store_true",
        help="Do not install this bootstrap skill into .agents/skills/bootstrap-agent-repo",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    skill_dir = Path(__file__).resolve().parent.parent
    templates_dir = skill_dir / "assets" / "templates"
    target_dir = Path(args.target).expanduser().resolve()

    if not templates_dir.is_dir():
        raise SystemExit(f"Templates directory not found: {templates_dir}")

    if args.check_root_sync:
        repo_root = skill_dir.parents[2]
        return check_root_sync(repo_root, templates_dir)

    if args.list:
        for source in iter_files(templates_dir):
            rel = as_posix(source.relative_to(templates_dir))
            if rel in NON_DISTRIBUTED_TEMPLATE_PATHS:
                continue
            print(rel)
        if not args.no_self_skill:
            for source in iter_files(skill_dir):
                if "assets/templates/.agents/skills/bootstrap-agent-repo" in as_posix(source):
                    continue
                rel = Path(".agents/skills/bootstrap-agent-repo") / source.relative_to(skill_dir)
                print(as_posix(rel))
        return 0

    if not args.dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)

    if not target_dir.exists() and args.dry_run:
        print(f"[DRY RUN] target will be created: {target_dir}")

    plans = build_plan(
        templates_dir,
        target_dir,
        force=args.force,
        includes=args.include,
        excludes=args.exclude,
    )

    self_target = (target_dir / ".agents" / "skills" / "bootstrap-agent-repo").resolve()
    if not args.no_self_skill and self_target != skill_dir.resolve():
        plans.extend(
            build_plan(
                skill_dir,
                target_dir,
                prefix=Path(".agents/skills/bootstrap-agent-repo"),
                force=args.force,
                includes=args.include,
                excludes=args.exclude + ["*.pyc", "*/__pycache__/*"],
            )
        )

    backup_root = None
    if args.force and args.backup:
        backup_root = make_backup_root(target_dir)

    mode = "DRY RUN" if args.dry_run else "APPLY"
    print_plan(plans, mode=mode, target_dir=target_dir, backup_root=backup_root)
    apply_plan(plans, dry_run=args.dry_run, backup_root=backup_root)
    print("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
