---
name: feature-planning
description: ファイル変更を伴う作業、複数領域にまたがる変更、仕様変更、高リスク変更について、plans/*.md の実装計画を作成または更新する。
license: Apache-2.0
metadata:
  author: "Yasu (@yasu-tty)"
  version: "0.1.0"
---

# Feature Planning

## Goal

`.agents/PLANS.md` に沿って `plans/*.md` を作成または更新する。

## Planning trigger

ファイルを変更する作業では、最初の non-plan file 編集前に `plans/*.md` を作成または更新する。既存の active plan の scope 内であれば、その plan を更新してよい。

既定で許可する例外は、read-only の調査、`plans/*.md` の作成または更新そのもの、ファイルを書き換えない検証コマンドだけである。docs-only、formatter、生成物更新、小さな1ファイル修正であっても、ファイルを書き換える場合は plan を作成または更新する。

## Procedure

1. `AGENT_RULES.md` を読む
2. `.agents/PLANS.md` を読む
3. `docs/agent/OWNERSHIP.md` を読む
4. `docs/agent/HANDOFF_PROTOCOL.md` を読む
5. `docs/agent/COORDINATION_GATE.md` を読む
6. 関連コード・設定・文書・既存 plan を調査する
7. Scope, Discovery, Risks, Validation, Collaboration split を整理する
8. Ownership area, planned files, out-of-scope files, affected agents, review owner, conflict risk を整理する
9. Agreement summary, Agreement matrix, Decision log を整理する
10. user / human maintainer の明示合意なしに `agreed` を推定しない
11. unresolved decision は Agreement matrix に記録し、block する場合は `Blocks implementation: yes` と Agreement summary に row ID を反映する
12. Decision log に user / human maintainer の判断履歴を記録する。判断がない場合は `.agents/PLANS.md` の empty-state sentence を使う
13. Routing and execution として agent availability, execution mode, primary executor, reviewer / validator, parallel execution allowed, file ownership claims, locked files, handoff checkpoint, conflict resolution owner, routing decision notes を整理する
14. Work file activity に actor, role, task, files / paths, operation, status, conflict risk, last update, next action を記録する
15. agent availability が明示されていない場合はユーザーへ確認する。ただし、ユーザーが `Codex only`, `Claude only`, `Claude review only` などを明示している場合は再質問しない
16. 自動で Codex / Claude Code に作業を割り振らない。片方が `unavailable` または `unknown` の場合、その agent に実装を割り当てない
17. parallel execution は既定で禁止し、`docs/agent/COORDINATION_GATE.md` の許可条件を満たす場合だけ `parallel-isolated` または parallel allowed を記録する
18. scope expansion が必要になった場合の報告方法を決める
19. test command と rollback notes を決める
20. `plans/template.md` を基に計画書を作り、冒頭付近に `## Status` を必ず含める
21. 新規 plan の初期 `State` は原則 `Draft` または `Planned` にする
22. 実装または調査を開始したら `State: In progress` に更新する
23. 中断可能な大きな作業境界では Work file activity と Progress log を更新する
24. 実装完了後、レビュー・検証・commit / merge 前なら `State: Implementation complete` にする
25. レビュー、検証、commit / merge まで終わった場合のみ `State: Completed` にする
26. `State` を変更したら、Summary、Status / Result / Remaining work、Agreement summary、Agreement matrix の `State` / `Blocks implementation` / `Next action`、Scope、Routing and execution、Work file activity、Rollback notes、Validation が新しい現在状態と矛盾しないか確認する
27. Decision log と Progress log は履歴として扱い、現在状態が変わっても有効な履歴は書き換えない。現在状態との食い違いは current-state surfaces 側を更新する
28. 曖昧な点は `Assumptions` または Agreement matrix に明記する
29. agent 間の役割分担がある場合は `Collaboration split`, `Ownership and coordination`, `Routing and execution`, `Work file activity` に残す
30. `Draft`, `planning-only`, primary executor 未定、planned files 未定、locked files 未解除、stale agreement state、または unresolved blocking agreement がある plan は実装可能として扱わない。曖昧な `Implement the plan` 指示では non-plan file を編集せず、先に実装対象 scope、routing、agreement state を確認・更新する

## Output requirements

- `## Status` を含め、`.agents/PLANS.md` の State 候補に従う
- `Agreement summary`, `Agreement matrix`, `Decision log`, `Work file activity` を含める
- Agreement matrix の required columns と row state values に従う
- `agreed` は user / human maintainer の明示合意がある場合だけ使う
- `Remaining work` を空欄のままにせず、未完了作業がない場合は `None` と書く
- Summary が1段落で分かる
- Work breakdown が実行可能な粒度である
- Validation が具体的である
- リスク、緩和策、rollback がある
- 変更予定ファイルを明示する
- 触らない範囲を明示する
- ownership area を明示する
- `Routing and execution` を埋める
- `Work file activity` で作業者、対象ファイル、操作、状態、次 action を追跡する
- 実装可能条件を満たさない plan では non-plan file を編集しない
- 他agentへの依頼事項を明示する
- conflict risk を評価する
- scope expansion が必要になった場合の報告方法を書く
- test command と rollback notes を書く

## Coordination template

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

## Routing question template

```text
この plan の実行モードを確認してください。

Available agents:
1. Codex は使用できますか？ yes / no / unknown
2. Claude Code は使用できますか？ yes / no / unknown

Execution mode:
1. single-agent: 片方の agent のみで実装・検証
2. sequential-handoff: 一方が実装し、もう一方が review / validation
3. parallel-isolated: ファイル担当を分離できる場合のみ並行
4. planning-only: plan のみ作成し、実装担当は未決定

Parallel execution:
- no
- separate-files-only
- separate-worktrees-only
- yes

Planned file ownership:
- Codex:
- Claude Code:

Locked files:
-
```
