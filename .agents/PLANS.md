# Plan Document Specification

`plans/*.md` は、ファイル変更を伴う作業の ownership、scope、agreement、routing、validation、rollback を残すための **living document** です。

## File-changing task gate

ファイルを変更する作業では、最初の non-plan file 編集前に `plans/*.md` を作成または更新する。既存の active plan の scope 内であれば、その plan を更新してよい。

既定で許可する例外は以下だけとする。

- read-only の調査
- `plans/*.md` の作成または更新そのもの
- ファイルを書き換えない検証コマンド

docs-only、formatter、生成物更新、小さな1ファイル修正であっても、ファイルを書き換える場合は plan を作成または更新する。

## 必須セクション

### 1. Summary
- 何を変えるか
- なぜ必要か
- 成功条件

### 2. Status
- State
- Started
- Last updated
- Completed
- Result
- Remaining work
- Notes

### 3. Agreement summary
- Overall agreement state
- Blocking unresolved decisions
- Required approvers / reviewers
- Matrix status
- Last agreement update

### 4. Agreement matrix
- 合意済み、未合意、却下、blocked、置き換え済みの論点
- 判断者、根拠、owner decision の要否、実装 block の有無
- 次に必要な action

### 5. Decision log
- user / human maintainer の判断履歴
- Agreement matrix row との対応
- 置き換え、却下、supersede の履歴

### 6. Scope
- In scope
- Out of scope
- Dependencies

### 7. Ownership and coordination
- Ownership area
- Primary owner
- Review owner
- Affected agents / owners
- Planned files
- Out-of-scope files
- Conflict risk
- Handoff notes
- Scope expansion rule
- Rollback notes

### 8. Routing and execution
- Available agents
- Selected execution mode
- Primary executor
- Reviewer / validator
- Parallel execution allowed
- File ownership claims
- Locked files
- Handoff checkpoint
- Conflict resolution owner
- Routing decision notes

### 9. Work file activity
- Actor
- Role
- Task
- Files / paths
- Operation
- Status
- Conflict risk
- Last update
- Next action

### 10. Discovery
- 現状調査
- 関連ファイル
- 制約
- Assumptions

### 11. Proposed changes
- 実装方針
- データ/制御フロー
- 互換性
- 移行手順

### 12. Collaboration split
- 誰が計画を担当するか
- 誰が実装するか
- 誰が検証するか

### 13. Risks and mitigations
- 壊れやすい箇所
- 検証方法
- ロールバック方針

### 14. Work breakdown
- Step 1
- Step 2
- Step 3

### 15. Validation
- Automated tests
- Manual checks
- Observability / monitoring

### 16. Progress log
- 日時
- 実施内容
- 発見
- 方針変更
- 担当

## Status template

```md
## Status

- State: Draft
- Started:
- Last updated:
- Completed:
- Result:
- Remaining work:
- Notes:
```

## State values

| State | Meaning |
|---|---|
| Draft | まだ検討中で、実装対象として確定していない |
| Planned | 実装方針は決まっているが、まだ作業開始していない |
| In progress | 実装または調査が進行中 |
| Blocked | 外部判断、依存作業、仕様未確定などで止まっている |
| Implementation complete | 実装は完了したが、レビュー、最終検証、commit、merge などが未完了 |
| Completed | レビュー、検証、commit / merge などを含めて完了 |
| Superseded | 別 plan に置き換えられた |
| Cancelled | 実施しないことが決まった |

## State transition consistency check

`State` を変更するときは、先に変更種別を確認する。主な種別は planning start、execution start、implementation completion、review / validation completion、blocked state、closure である。

`State` 変更後は、以下の current-state surfaces が新しい状態と矛盾していないか確認する。

- Summary
- Status / Result / Remaining work
- Agreement summary
- Agreement matrix の `State`, `Blocks implementation`, `Next action`
- Scope と planned / locked files
- Routing and execution
- Work file activity
- Rollback notes
- Validation

Decision log と Progress log は historical surfaces として扱う。現在状態が変わっても、有効な履歴は現在形に書き換えない。current-state surfaces と historical surfaces が食い違う場合は、現在状態を表す section を更新し、履歴は事実誤認がある場合だけ修正する。

## Agreement summary template

```md
## Agreement summary

- Overall agreement state: proposed
- Blocking unresolved decisions: AG-01
- Required approvers / reviewers:
- Matrix status: present
- Last agreement update:
```

## Overall agreement state values

| State | Meaning |
|---|---|
| proposed | まだ user / human maintainer の明示合意がない |
| partially-agreed | 一部の論点だけ明示合意されている |
| agreed | 実装を block する未解決判断がなく、必要な論点が明示合意されている |
| blocked | 実装を block する未解決判断がある |
| superseded | 別 plan または別判断に置き換えられた |

## Matrix status values

| Status | Meaning |
|---|---|
| present | Agreement matrix が存在し、現在状態を表している |
| omitted-by-user | user / human maintainer が明示的に matrix 省略を指示した |
| needs-update | matrix が存在するが、最新判断または scope 変更を反映していない |
| not-yet-backfilled | 新形式へ未移行の古い active plan で、次に触るときに backfill する |

## Agreement matrix template

```md
## Agreement matrix

| ID | Topic | Proposal | State | Decision owner | Evidence | Owner decision required | Blocks implementation | Next action |
|---|---|---|---|---|---|---|---|---|
| AG-01 |  |  | proposed | User / human maintainer |  | yes | yes |  |
```

## Agreement matrix rules

- Agreement matrix は全 plan で原則必須とする。
- Agreement matrix を省略できるのは、user / human maintainer が明示的に省略を指示した場合だけである。
- Agreement matrix がないこと、未解決判断が見当たらないこと、既存 policy に沿っていることを理由に、agent が `agreed` を推定してはならない。
- `Blocking unresolved decisions` は、matrix がある場合は block している row ID を列挙する。block する row がない場合は `None` と書く。
- matrix が user 指示で省略されている場合だけ、`Blocking unresolved decisions` に短い説明を書いてよい。
- Optional detail columns may be added when needed, such as agreed scope, not-yet-agreed scope, affected owners / agents, or blocking question.

## Agreement row state values

| State | Meaning |
|---|---|
| proposed | 提案中、または owner decision が必要 |
| agreed | user / human maintainer が明示合意した |
| rejected | user / human maintainer が却下した |
| blocked | 外部判断、依存作業、仕様未確定などで進められない |
| superseded | 別 row、別 plan、または新判断に置き換えられた |

## Agreement evidence rules

- `agreed` は user / human maintainer の明示的な合意だけを根拠にする。
- 既存 policy、既存 plan、issue / PR text、agent の推論や合理性だけでは `agreed` にしてはならない。
- owner decision が必要な場合は `State: proposed` のまま、`Owner decision required: yes` と書く。
- 実装を止める判断は `Blocks implementation: yes` とし、Agreement summary に row ID を反映する。

## Decision log template

```md
## Decision log

No user / human maintainer decision recorded yet.

| Date | Decision | Decided by | Evidence | Applies to | Matrix ID | Replaces / supersedes | Notes |
|---|---|---|---|---|---|---|---|
```

## Decision log rules

- Decision log は全 plan で必須とする。
- user / human maintainer の判断がまだない場合は、空 table の前に `No user / human maintainer decision recorded yet.` と書く。
- 判断が記録されたら、該当する Agreement matrix row ID を `Matrix ID` に書く。
- Decision log は履歴であり、現在状態の正本は Agreement matrix と Status である。

## Ownership and coordination template

```md
## Ownership and coordination

- Ownership area:
- Primary owner:
- Review owner:
- Affected agents:
- Planned files:
- Out of scope:
- Conflict risk:
- Handoff notes:
- Scope expansion rule:
- Rollback notes:
```

## Routing and execution template

```md
## Routing and execution

- Available agents:
  - Codex:
  - Claude Code:
- Selected mode:
- Primary executor:
- Reviewer / validator:
- Parallel execution allowed:
- File ownership claims:
  - Codex:
  - Claude Code:
- Locked files:
- Handoff checkpoint:
- Conflict resolution owner:
- Routing decision notes:
```

## Work file activity template

```md
## Work file activity

| ID | Actor | Role | Task | Files / paths | Operation | Status | Conflict risk | Last update | Next action |
|---|---|---|---|---|---|---|---|---|---|
| WF-01 |  | Planner |  |  | inspect | planned |  |  |  |
```

## Work file activity values

| Field | Values |
|---|---|
| Role | `Planner`, `Primary executor`, `Reviewer`, `Validator`, `Decision owner`, `Approver`, `Contributor`, `Observer` |
| Operation | `inspect`, `create`, `edit`, `review`, `validate`, `decide`, `approve`, `handoff` |
| Status | `planned`, `active`, `paused`, `handoff-ready`, `reviewing`, `validating`, `done`, `blocked` |

Use `Task` and `Next action` for role-specific details instead of inventing new role names.

## Executable plan precondition

以下のいずれかに該当する plan は、実装可能な plan として扱わない。

- `State: Draft`
- `Selected mode: planning-only`
- `Primary executor: None` または未記入
- 実装対象外または locked files に non-plan files が含まれ、解除条件が明記されていない
- planned files が未記入、または実装対象ファイルが曖昧
- `Blocking unresolved decisions` が `None` 以外で、summary に実装を block する未解決判断が残っている
- Agreement matrix に `Blocks implementation: yes` の未解決 row がある
- `Owner decision required: yes` の row が実装判断を block している
- `Matrix status: needs-update` で、実装対象 scope や判断が古い可能性がある
- `Matrix status: not-yet-backfilled` で、新形式への backfill がまだ完了していない
- `Matrix status: omitted-by-user` だが、省略を指示した user / human maintainer の evidence が Decision log または Notes にない

この状態の plan に対して `Implement the plan` などの曖昧な実装指示が出た場合、agent は non-plan file を編集してはならない。先に、実装対象 scope、planned files、primary executor、locked files の解除、agreement state、validation、rollback を確認し、plan を実装可能な状態に更新する。

ユーザーが特定 plan を明示して「実装を開始してください」と指示した場合でも、上記の実装可能条件を plan に記録してから shared policy、template、source file などの non-plan file を編集する。

## Parallel execution deny conditions

以下のどれかに該当する場合、parallel execution は禁止するか `separate-worktrees-only` にする。

- planned files が重複する
- Agreement matrix に未解決の blocking decision がある
- `AGENT_RULES.md` を変更する
- `.agents/PLANS.md` を変更する
- `plans/template.md` を変更する
- `README.md` を変更する
- `AGENTS.md` と `CLAUDE.md` の両方を同時に設計変更する
- `docs/agent/OWNERSHIP.md` を変更する
- `docs/agent/AGENT_ROLES.md` を変更する
- `docs/agent/HANDOFF_PROTOCOL.md` を変更する
- `docs/agent/COMPONENT_INVENTORY.md` を変更する
- `.agents/skills/bootstrap-agent-repo/**` を変更する
- `.agents/skills/bootstrap-agent-repo/assets/templates/**` を変更する
- root/template sync 対象のファイルを変更する
- bootstrap script を変更する
- hook scripts を変更する
- worktree に unrelated uncommitted changes がある
- agent availability が `unknown`
- conflict risk が High
- rollback path が不明

## ルール

- 各 plan は冒頭付近に `## Status` を持つ
- `## Status` は現在状態の正本である
- Agreement sections は `## Status` の直後に置く
- `## Work file activity` は `## Routing and execution` の直後に置く
- `Draft` は検討中であり、non-plan file の実装許可ではない
- Progress log は履歴であり、現在状態の代替にしない
- Open questions は標準セクションにしない。未解決判断は Agreement matrix に記録する
- 複雑な plan で別 index が必要な場合のみ `Open decisions` を追加してよいが、必ず Agreement matrix row ID を参照する
- 実装が終わっても、レビュー・検証・commit / merge が未完了なら `Completed` ではなく `Implementation complete` にする
- `Completed` にする場合は、`Result` と `Completed` 日付を埋める
- 未完了の作業がある場合は `Remaining work` に明記する
- 未完了の作業がない場合は `Remaining work: None` と書く
- 中止または置き換えの場合は、`Notes` に理由または置き換え先 plan を書く
- 仕様変更が出たら plan、Agreement matrix、Decision log を更新する
- 実装中の発見は Progress log に残す
- 中断可能な境界では Work file activity と Progress log を更新する
- agent 間で handoff した場合も、決定事項を残す
- 完了後は結果と残課題を記録する
- 変更予定ファイルと触らないファイルを実装前に明記する
- 複数 agent が同じファイルを触る可能性がある場合は、実装前に ownership と planned files を確認する
- `## Routing and execution` で agent availability、execution mode、parallel execution allowed、file ownership claims、locked files を実装前に確認して記録する
- `planning-only`、primary executor 未定、locked files が未解除、agreement state が未解決の plan は、実装前に実装可能条件を更新する
- coordination gate の詳細は `docs/agent/COORDINATION_GATE.md` を正とする
- agent availability が明示されていない場合は plan 作成時にユーザーへ確認する。ただし、ユーザーが `Codex only`, `Claude only`, `Claude review only` などを明示している場合は再質問しない
- 片方の agent が `unavailable` または `unknown` の場合、自動でその agent に実装を割り当てない
- 両方の agent が `available` でも、parallel execution を自動選択しない。既定は `single-agent` または `sequential-handoff` とする
- `multi_agent = true` は parallel execution の自動許可ではない
- `parallel-isolated` は planned files が分離され、locked files に触れず、worktree 状況が安全な場合だけ許可する
- planned files が重複する場合、shared policy file または root/template sync 対象を変更する場合、unrelated uncommitted changes がある場合、agent availability が `unknown` の場合、conflict risk が High の場合、rollback path が不明な場合は parallel execution を禁止するか `separate-worktrees-only` にする
- 担当外の変更が必要になった場合は、理由、追加ファイル、影響範囲、必要な owner/reviewer を plan または handoff に残す
- 仕様変更とリファクタリングを混ぜる場合は、理由とレビュー方針を明記する

## Existing plan migration

- New plans use this format.
- `plans/template.md` is the canonical starting point for new plans.
- Completed / Superseded / Cancelled plans are not backfilled by default.
- Active old-format plans are backfilled only when next touched.
- Backfilled plans must not mark rows `agreed` unless explicit user / human maintainer evidence exists.
- If the matrix has not been backfilled yet, use `Matrix status: not-yet-backfilled` until the plan is updated.

## Plan が必要になる条件

- ファイル変更を伴う作業
- 3ファイル以上変更する
- 複数の ownership area にまたがる
- 複数ディレクトリにまたがる変更
- 仕様変更を伴う変更
- public API を変更する
- database schema / migration を変更する
- authentication / authorization に影響する
- billing / payment に影響する
- deployment / CI に影響する
- shared component を変更する
- 既存テスト方針を変更する
- 高リスク変更
- 長時間かかる変更
