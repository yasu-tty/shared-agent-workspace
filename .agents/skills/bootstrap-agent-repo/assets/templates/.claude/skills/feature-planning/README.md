# feature-planning

## 概要

`feature-planning` は、ファイル変更を伴う作業、複数領域にまたがる変更、仕様変更、高リスク変更、長時間かかる変更について、`plans/*.md` の実装計画を作成または更新する skill です。このディレクトリは Claude Code から使うための adapter で、共有 plan 仕様、agreement tracking、coordination rules に従います。

## 使う場面

- ファイル変更を伴う作業を始める
- 複数ディレクトリや複数 ownership area にまたがる作業を計画する
- public API、schema、auth、billing、deployment、CI、shared component に影響する変更を扱う
- Codex と Claude Code の役割分担、handoff、parallel execution の可否を記録する
- 既存 plan の status、progress log、validation notes を更新する
- Agreement summary / matrix、Decision log、Work file activity、Review findings を整理する
- review feedback / review result を受け取る、または対象 plan のレビュー結果を作成し、findings、対応判断、次担当、validation / handoff 状態を active plan / checkpoint に記録する
- context compaction、session resume、handoff、scope expansion、validation 開始後に、active plan / checkpoint から作業状態を復元する

既定で許可する例外は、read-only の調査、`plans/*.md` の作成または更新そのもの、ファイルを書き換えない検証コマンドだけです。docs-only、formatter、生成物更新、小さな1ファイル修正であっても、ファイルを書き換える場合は plan を作成または更新します。

## 利用前提

- repo の共通規約として `AGENT_RULES.md` を先に確認すること
- plan 仕様として `.agents/PLANS.md` を確認すること
- ownership と handoff は `docs/agent/OWNERSHIP.md`、`docs/agent/AGENT_ROLES.md`、`docs/agent/HANDOFF_PROTOCOL.md` に従うこと
- routing と execution mode は `docs/agent/COORDINATION_GATE.md` に従って記録すること

## 基本的な使い方

1. 既存作業の再開・移行・handoff では、active plan / checkpoint から current actor、participating agents、target files、locked files、completed work、current status、next action、unresolved decisions、blockers、review findings、validation results、handoff checkpoint、last updated information を先に復元します。
2. 現在の trigger に必要な reference だけを読みます。新規 plan 作成や material update では `.agents/PLANS.md`、`plans/template.md`、関連する ownership / coordination / handoff docs を確認します。
3. 関連するコード、設定、文書、既存 plan を調査します。
4. `plans/template.md` を基に `plans/YYYY-MM-short-name.md` を作成します。
5. `## Status`、`## Agreement summary`、`## Agreement matrix`、`## Decision log`、`## Scope` を埋めます。
6. `## Ownership and coordination`、`## Routing and execution`、`## Work file activity`、`## Review findings`、`## Validation` を埋めます。
7. agent availability、execution mode、parallel execution allowed、file ownership claims、locked files を記録します。
8. `State` を変更するときは、Summary、Status、Agreement summary / matrix、Routing、Work file activity、Review findings、Rollback、Validation が新しい現在状態と矛盾しないか確認します。
9. review feedback / review result を受け取る、または対象 plan のレビュー結果を作成する場合は、`## Review findings`、`## Work file activity`、`## Progress log`、`## Validation`、`## Routing and execution` の `Handoff checkpoint` field の該当箇所に、findings、採用/見送り/保留、対応要否、次担当、validation / handoff 状態を記録します。ユーザーが read-only review only を明示した場合は、PLAN 更新を行わず、その制約を応答に明記します。
10. 実装中の発見や handoff は `## Progress log` に追記します。

## Codex / Claude Code 向け配置方法

Codex 向けには、canonical source を `.agents/skills/feature-planning/` に配置します。Codex の入口である `AGENTS.md` からは、計画作成・更新の手順化された作業として canonical skill を参照します。

Claude Code 向けには、この adapter を `.claude/skills/feature-planning/` に配置します。この adapter は共有 plan 仕様を参照するため、`.agents/PLANS.md` と `docs/agent/COORDINATION_GATE.md` も同じ repo に配置してください。

この skill を公開または別 repo に配布する場合は、Claude adapter だけを切り出さず、`.agents/skills/feature-planning/` と `.claude/skills/feature-planning/` をセットで配布してください。

## 含まれるファイル

- `SKILL.md`: Claude Code adapter としての skill 入口
- `README.md`: 利用者向けの説明
- `LICENSE.txt`: この skill adapter のライセンス

## ライセンス

この skill adapter は Apache License 2.0 で提供されます。詳細は `LICENSE.txt` を確認してください。

## 注意事項

- `SKILL.md` が agent 向け手順の正本です。この README は利用者向けの補助説明です。
- planning の正本は `.agents/PLANS.md` と `docs/agent/COORDINATION_GATE.md` です。
- `Draft`、`planning-only`、unresolved blocking decisions、または locked target files が残る plan は実装可能として扱いません。
- 会話履歴だけを現在状態の正本にせず、再開・handoff・validation 時は active plan / checkpoint を読み直してください。
- Decision log と Progress log は履歴です。State 変更時は、有効な履歴を書き換えず、Summary や Agreement summary など現在状態を表す section を更新してください。
- root と template の adapter 内容は同期対象です。保守時は bootstrap の `--check-root-sync` を実行してください。
