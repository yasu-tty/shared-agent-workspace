# Handoff Protocol

## Purpose

This protocol defines what agents share at work start, during progress, when scope changes, and at completion. Use it to prevent silent overlap, unclear ownership, and unsafe conflict resolution.

## When to use this protocol

- More than one agent or human is working in the repository.
- A change touches multiple files, ownership areas, or shared components.
- Work is handed from planning to implementation, implementation to review, or implementation to test.
- A task affects public API, schema, auth, billing, deployment, CI, or test strategy.
- An agent finds an issue outside the assigned scope.

## Work start declaration

```text
[Work Start]
Agent:
Task:
Goal:
Planned files:
Owned area:
Out of scope:
Dependencies:
Expected tests:
Completion criteria:
Risk level:
```

## Progress update

```text
[Progress Update]
Agent:
Current status:
Files changed so far:
Unexpected findings:
Scope changes:
Questions for other agents:
Next step:
```

## Scope expansion request

```text
[Scope Expansion Request]
Agent:
Original scope:
Requested additional files/areas:
Reason:
Impact:
Risk:
Owner/reviewer needed:
Can proceed without approval: yes/no
```

## Blocker report

```text
[Blocker]
Agent:
Task:
Blocked on:
Files/areas affected:
What was tried:
Risk if ignored:
Owner/reviewer needed:
Suggested next step:
```

## Completion report

```text
[Completion]
Agent:
Summary:
Files changed:
Behavior changed:
Tests run:
Tests not run:
Known issues:
Follow-up tasks:
Handoff notes:
```

## Review handoff

```text
[Review Handoff]
Agent:
Change summary:
Files changed:
Ownership areas:
Risk level:
Specific review requests:
Tests and validation:
Known gaps:
Rollback notes:
```

## Conflict handling

- If multiple agents may edit the same file, confirm ownership and planned files before implementation.
- If a conflict happens, state which change intent takes priority before continuing implementation.
- If one side's change is discarded, record the reason.
- Do not resolve merge conflicts opportunistically without understanding both agents' intent.
- Do not hide conflict resolution inside unrelated formatting or refactoring.
- If intent is unclear, stop and request the primary owner or review owner decision.

## Examples

```text
[Work Start]
Agent: Feature implementation agent
Task: Add input validation for Example feature
Goal: Reject invalid Example payloads before persistence
Planned files: src/example/validator.*, tests/example/validator.*
Owned area: Example feature
Out of scope: Public API shape, database schema, shared UI components
Dependencies: Ownership matrix row for Example feature
Expected tests: Focused validator tests
Completion criteria: Invalid payloads fail with documented errors; existing valid cases pass
Risk level: Medium
```

```text
[Scope Expansion Request]
Agent: Test and quality agent
Original scope: Add regression tests for Example validator
Requested additional files/areas: Shared test fixture factory
Reason: Existing fixture cannot represent the invalid state under test
Impact: Shared tests may be affected
Risk: Medium
Owner/reviewer needed: Example owner and test owner
Can proceed without approval: no
```
