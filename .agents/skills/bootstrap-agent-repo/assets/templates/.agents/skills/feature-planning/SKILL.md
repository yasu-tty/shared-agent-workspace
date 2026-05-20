---
name: feature-planning
description: 複数領域にまたがる変更、仕様変更、高リスク変更について、plans/*.md の実装計画を作成または更新する。
license: Apache-2.0
metadata:
  author: "Yasu (@yasu-tty)"
  version: "0.1.0"
---

# Feature Planning

## Goal

`.agents/PLANS.md` に沿って `plans/*.md` を作成または更新する。

## Procedure

1. `AGENT_RULES.md` を読む
2. `.agents/PLANS.md` を読む
3. `docs/agent/OWNERSHIP.md` を読む
4. `docs/agent/HANDOFF_PROTOCOL.md` を読む
5. `docs/agent/COORDINATION_GATE.md` を読む
6. 関連コード・設定・文書・既存 plan を調査する
7. Scope, Discovery, Risks, Validation, Collaboration split を整理する
8. Ownership area, planned files, out-of-scope files, affected agents, review owner, conflict risk を整理する
9. Routing and execution として agent availability, execution mode, primary executor, reviewer / validator, parallel execution allowed, file ownership claims, locked files, handoff checkpoint, conflict resolution owner, routing decision notes を整理する
10. agent availability が明示されていない場合はユーザーへ確認する。ただし、ユーザーが `Codex only`, `Claude only`, `Claude review only` などを明示している場合は再質問しない
11. 自動で Codex / Claude Code に作業を割り振らない。片方が `unavailable` または `unknown` の場合、その agent に実装を割り当てない
12. parallel execution は既定で禁止し、`docs/agent/COORDINATION_GATE.md` の許可条件を満たす場合だけ `parallel-isolated` または parallel allowed を記録する
13. scope expansion が必要になった場合の報告方法を決める
14. test command と rollback notes を決める
15. `plans/template.md` を基に計画書を作り、冒頭付近に `## Status` を必ず含める
16. 新規 plan の初期 `State` は原則 `Draft` または `Planned` にする
17. 実装または調査を開始したら `State: In progress` に更新する
18. 実装完了後、レビュー・検証・commit / merge 前なら `State: Implementation complete` にする
19. レビュー、検証、commit / merge まで終わった場合のみ `State: Completed` にする
20. 曖昧な点は `Assumptions` として明記する
21. agent 間の役割分担がある場合は `Collaboration split`, `Ownership and coordination`, `Routing and execution` に残す
22. `Draft`, `planning-only`, primary executor 未定、planned files 未定、または locked files 未解除の plan は実装可能として扱わない。曖昧な `Implement the plan` 指示では non-plan file を編集せず、先に実装対象 scope と routing を確認・更新する

## Output requirements

- `## Status` を含め、`.agents/PLANS.md` の State 候補に従う
- `Remaining work` を空欄のままにせず、未完了作業がない場合は `None` と書く
- Summary が1段落で分かる
- Work breakdown が実行可能な粒度である
- Validation が具体的である
- リスク、緩和策、rollback がある
- 変更予定ファイルを明示する
- 触らない範囲を明示する
- ownership area を明示する
- `Routing and execution` を埋める
- 実装可能条件を満たさない plan では non-plan file を編集しない
- 他agentへの依頼事項を明示する
- conflict risk を評価する
- scope expansion が必要になった場合の報告方法を書く
- test command と rollback notes を書く

## Coordination template

```md
## Coordination

- Ownership area:
- Primary owner:
- Review owner:
- Affected agents:
- Planned files:
- Out of scope:
- Conflict risk:
- Handoff notes:
- Scope expansion rule:
- Test command:
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
