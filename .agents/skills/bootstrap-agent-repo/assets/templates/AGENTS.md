# Agent Instructions for Codex

この repo の共通規約の正本は `AGENT_RULES.md` です。必ず先に読んでください。

## Common reading order

作業時の共通参照順は `AGENT_RULES.md` を正とする。この Codex adapter では required order を重複定義しない。

## Planning policy

以下に当てはまる作業では、先に `plans/*.md` を作成または更新してください。

- 複数領域にまたがる変更
- 仕様変更を伴う変更
- 高リスク変更
- 長時間かかる変更

計画書の形式は `.agents/PLANS.md` に従ってください。
Plan status rules are defined in `.agents/PLANS.md`; use `Implementation complete` when code changes are done but review, validation, commit, or merge remains.
Plan 作成時は `docs/agent/COORDINATION_GATE.md` に従い、agent availability と execution mode を確認・記録してください。Codex は routing decision を自動確定せず、利用可能 agent、parallel execution、file ownership、locked files を plan に残してください。
Ownership、handoff、conflict prevention は共通ドキュメントを参照し、詳細ルールをこの adapter に重複させないでください。

## Skills

- 手順化された作業は `.agents/skills/` の skill を優先してください。
- repo 初期化は `bootstrap-agent-repo` skill を使ってください。
- 計画作成・更新は `feature-planning` skill を優先してください。

## Repository-specific expectations

- 変更は最小差分を優先する
- 既存構造に合わせる
- テスト・検証結果を残す
- agent 間で役割分担した場合も、共通 plan を更新する
- 非共有設定は `templates/nonshared/` から必要なものだけ採用する
- 参照者・責務分担・引き継ぎ・衝突防止は `docs/agent/OWNERSHIP.md`, `docs/agent/AGENT_ROLES.md`, `docs/agent/HANDOFF_PROTOCOL.md`, `docs/agent/COORDINATION_GATE.md` に従う
