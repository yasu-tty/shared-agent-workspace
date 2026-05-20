# Plan Document Specification

`plans/*.md` は、長時間・高リスク・広範囲変更のための **living document** です。

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

### 3. Scope
- In scope
- Out of scope
- Dependencies

### 4. Ownership and coordination
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

### 5. Routing and execution
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

### 6. Discovery
- 現状調査
- 関連ファイル
- 制約
- Assumptions

### 7. Proposed changes
- 実装方針
- データ/制御フロー
- 互換性
- 移行手順

### 8. Collaboration split
- 誰が計画を担当するか
- 誰が実装するか
- 誰が検証するか

### 9. Risks and mitigations
- 壊れやすい箇所
- 検証方法
- ロールバック方針

### 10. Work breakdown
- Step 1
- Step 2
- Step 3

### 11. Validation
- Automated tests
- Manual checks
- Observability / monitoring

### 12. Progress log
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

## Executable plan precondition

以下のいずれかに該当する plan は、実装可能な plan として扱わない。

- `State: Draft`
- `Selected mode: planning-only`
- `Primary executor: None` または未記入
- 実装対象外または locked files に non-plan files が含まれ、解除条件が明記されていない
- planned files が未記入、または実装対象ファイルが曖昧

この状態の plan に対して `Implement the plan` などの曖昧な実装指示が出た場合、agent は non-plan file を編集してはならない。先に、実装対象 scope、planned files、primary executor、locked files の解除、validation、rollback を確認し、plan を実装可能な状態に更新する。

ユーザーが特定 plan を明示して「実装を開始してください」と指示した場合でも、上記の実装可能条件を plan に記録してから shared policy、template、source file などの non-plan file を編集する。

## Parallel execution deny conditions

以下のどれかに該当する場合、parallel execution は禁止するか `separate-worktrees-only` にする。

- planned files が重複する
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
- `Draft` は検討中であり、non-plan file の実装許可ではない
- Progress log は履歴であり、現在状態の代替にしない
- 実装が終わっても、レビュー・検証・commit / merge が未完了なら `Completed` ではなく `Implementation complete` にする
- `Completed` にする場合は、`Result` と `Completed` 日付を埋める
- 未完了の作業がある場合は `Remaining work` に明記する
- 未完了の作業がない場合は `Remaining work: None` と書く
- 中止または置き換えの場合は、`Notes` に理由または置き換え先 plan を書く
- 仕様変更が出たら plan を更新する
- 実装中の発見は Progress log に残す
- agent 間で handoff した場合も、決定事項を残す
- 完了後は結果と残課題を記録する
- 変更予定ファイルと触らないファイルを実装前に明記する
- 複数 agent が同じファイルを触る可能性がある場合は、実装前に ownership と planned files を確認する
- `## Routing and execution` で agent availability、execution mode、parallel execution allowed、file ownership claims、locked files を実装前に確認して記録する
- `planning-only`、primary executor 未定、または locked files が未解除の plan は、実装前に実装可能条件を更新する
- coordination gate の詳細は `docs/agent/COORDINATION_GATE.md` を正とする
- agent availability が明示されていない場合は plan 作成時にユーザーへ確認する。ただし、ユーザーが `Codex only`, `Claude only`, `Claude review only` などを明示している場合は再質問しない
- 片方の agent が `unavailable` または `unknown` の場合、自動でその agent に実装を割り当てない
- 両方の agent が `available` でも、parallel execution を自動選択しない。既定は `single-agent` または `sequential-handoff` とする
- `multi_agent = true` は parallel execution の自動許可ではない
- `parallel-isolated` は planned files が分離され、locked files に触れず、worktree 状況が安全な場合だけ許可する
- planned files が重複する場合、shared policy file または root/template sync 対象を変更する場合、unrelated uncommitted changes がある場合、agent availability が `unknown` の場合、conflict risk が High の場合、rollback path が不明な場合は parallel execution を禁止するか `separate-worktrees-only` にする
- 担当外の変更が必要になった場合は、理由、追加ファイル、影響範囲、必要な owner/reviewer を plan または handoff に残す
- 仕様変更とリファクタリングを混ぜる場合は、理由とレビュー方針を明記する

## Plan が必要になる条件

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
