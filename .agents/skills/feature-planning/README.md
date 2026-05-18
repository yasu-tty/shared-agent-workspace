# feature-planning

## 概要

`feature-planning` は、複数領域にまたがる変更、仕様変更、高リスク変更、長時間かかる変更について、`plans/*.md` の実装計画を作成または更新する skill です。実装前に scope、ownership、routing、validation、rollback を明確にするために使います。

## 使う場面

- 3ファイル以上を変更する作業を始める
- 複数ディレクトリや複数 ownership area にまたがる作業を計画する
- public API、schema、auth、billing、deployment、CI、shared component に影響する変更を扱う
- Codex と Claude Code の役割分担、handoff、parallel execution の可否を記録する
- 既存 plan の status、progress log、validation notes を更新する

## 利用前提

- repo の共通規約として `AGENT_RULES.md` を先に確認すること
- plan 仕様として `.agents/PLANS.md` を確認すること
- ownership と handoff は `docs/agent/OWNERSHIP.md`、`docs/agent/AGENT_ROLES.md`、`docs/agent/HANDOFF_PROTOCOL.md` に従うこと
- routing と execution mode は `docs/agent/COORDINATION_GATE.md` に従って記録すること

## 基本的な使い方

1. 関連するコード、設定、文書、既存 plan を調査します。
2. `plans/template.md` を基に `plans/YYYY-MM-short-name.md` を作成します。
3. `## Status`、`## Scope`、`## Ownership and coordination`、`## Routing and execution`、`## Validation` を埋めます。
4. agent availability、execution mode、parallel execution allowed、file ownership claims、locked files を記録します。
5. 実装中の発見や handoff は `## Progress log` に追記します。

## Codex / Claude Code 向け配置方法

Codex 向けには、この skill を `.agents/skills/feature-planning/` に配置します。Codex の入口である `AGENTS.md` からは、計画作成・更新の手順化された作業として `.agents/skills/feature-planning/` を優先して参照します。

Claude Code 向けには、adapter を `.claude/skills/feature-planning/` に配置します。Claude adapter は共有 plan 仕様を参照するため、`.agents/PLANS.md` と `docs/agent/COORDINATION_GATE.md` も同じ repo に配置してください。

この skill を公開または別 repo に配布する場合は、Codex 用の `.agents/skills/feature-planning/` を canonical source とし、Claude Code でも使う場合は対応する `.claude/skills/feature-planning/` adapter も同梱してください。

## 含まれるファイル

- `SKILL.md`: agent が参照する skill 本体
- `README.md`: 利用者向けの説明
- `LICENSE.txt`: この skill のライセンス

## ライセンス

この skill は Apache License 2.0 で提供されます。詳細は `LICENSE.txt` を確認してください。

## 注意事項

- `SKILL.md` が agent 向け手順の正本です。この README は利用者向けの補助説明です。
- `multi_agent = true` は parallel execution の自動許可ではありません。
- agent availability が不明な場合は、plan 作成時に確認して記録してください。
- 実装完了後も review、validation、commit、merge が残る場合は `State: Completed` ではなく `State: Implementation complete` を使います。
