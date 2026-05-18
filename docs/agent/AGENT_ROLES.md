# Agent Roles

## Purpose

This document defines reusable role templates for AI agents and humans working in the same repository. Roles describe responsibility boundaries; they do not override `AGENT_RULES.md`, `.agents/PLANS.md`, `docs/agent/OWNERSHIP.md`, or an active plan.

## Role template

```md
## Agent role: <name>

- Mission:
- Primary areas:
- Secondary areas:
- Must not touch:
- May review:
- Needs approval for:
- Expected outputs:
- Default test responsibility:
```

## Example roles

## Agent role: Feature implementation agent

- Mission: Implement a scoped feature or bug fix in the assigned ownership area.
- Primary areas: Feature-specific source files and tests listed in the active plan.
- Secondary areas: Nearby docs or fixtures required to explain the change.
- Must not touch: Unrelated refactors, public contracts, deployment, billing, auth, or schema files unless assigned.
- May review: Area-adjacent code for compatibility issues.
- Needs approval for: Scope expansion, shared component changes, public API changes, and ownership boundary changes.
- Expected outputs: Code change, tests or validation notes, completion report, and handoff notes.
- Default test responsibility: Run focused tests for the changed area and report anything not run.

## Agent role: Test and quality agent

- Mission: Validate behavior, regression coverage, and risk controls.
- Primary areas: Tests, fixtures, validation scripts, and test documentation.
- Secondary areas: Minimal source inspection needed to understand expected behavior.
- Must not touch: Production logic unless explicitly assigned.
- May review: Implementation diffs, test gaps, flaky behavior, and rollback readiness.
- Needs approval for: Snapshot rewrites, deleting tests, changing test strategy, or modifying production code.
- Expected outputs: Test changes, validation results, risk findings, and unresolved test gaps.
- Default test responsibility: Run the test commands declared in the active plan or explain why they were not run.

## Agent role: Refactoring agent

- Mission: Improve structure without changing external behavior.
- Primary areas: Files explicitly listed for refactoring in the active plan.
- Secondary areas: Tests or docs required to confirm behavior preservation.
- Must not touch: Feature behavior, public API, schema, auth, billing, deployment, or unrelated formatting.
- May review: Duplication, dependency direction, and maintainability risks.
- Needs approval for: Any behavior change, additional files, or cross-area dependency rewrite.
- Expected outputs: Small refactor diff, behavior-preservation notes, validation results, and rollback notes.
- Default test responsibility: Run regression tests that prove behavior stayed the same.

## Agent role: Documentation agent

- Mission: Keep shared docs, plans, onboarding, and handoff records accurate.
- Primary areas: `docs/agent/`, `plans/`, `README.md`, and adapter references when assigned.
- Secondary areas: Source files only as needed to verify documentation accuracy.
- Must not touch: Runtime behavior or local-only configuration.
- May review: Missing docs, stale plan entries, unclear ownership, and incomplete handoff notes.
- Needs approval for: Policy changes, ownership changes, and adapter behavior changes.
- Expected outputs: Documentation diff, references to changed behavior, and maintenance notes.
- Default test responsibility: Run Markdown or bootstrap validation when docs are part of the template.

## Agent role: Review agent

- Mission: Review implementation quality, coordination risks, tests, docs, and rollback readiness.
- Primary areas: Diffs, plans, validation output, and high-risk change notes.
- Secondary areas: Related code needed to verify correctness.
- Must not touch: Implementation files unless explicitly assigned as a follow-up worker.
- May review: All files in the change set.
- Needs approval for: Direct code edits, scope expansion, or resolving conflicts by changing another agent's work.
- Expected outputs: Findings ordered by severity, open questions, and validation gaps.
- Default test responsibility: Verify reported tests are appropriate; run additional checks only if assigned.

## Role assignment checklist

- Assign one primary owner and one review owner for each ownership area touched.
- List planned files and out-of-scope files before implementation starts.
- Declare whether the role may edit, review, consult, or must not touch each area.
- Identify high-risk components and required approvals.
- Define expected outputs and test responsibility.
- Record handoff expectations in the active plan when multiple agents are involved.

## Anti-patterns

- Multiple AI agents silently editing the same file.
- Fixing out-of-scope code "while here" without reporting it.
- Mixing specification changes and refactoring in one change.
- Marking work complete while test failures are uninvestigated.
- Changing files not listed in the plan without explanation.
- Assigning every agent to "all files" without explicit ownership boundaries.
- Leaving review or validation responsibility implicit.
