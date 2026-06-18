# Agent Instructions for Codex

この repo の共通規約の正本は `AGENT_RULES.md` です。必ず先に読んでください。

## Common reading order

作業時の共通 core と workflow rehydration の導線は `AGENT_RULES.md` を正とする。この Codex adapter では詳細な required order を重複定義しない。
Codex は最初に `AGENTS.md` を読む前提なので、必要な場面で `AGENT_RULES.md`、active plan、workflow skill へ戻る。

## Planning policy

ファイルを変更する作業では、最初の non-plan file 編集前に `plans/*.md` を作成または更新してください。既存の active plan の scope 内であれば、その plan を更新してよい。

特に以下に当てはまる作業では、必ず先に `plans/*.md` を作成または更新してください。

- 複数領域にまたがる変更
- 仕様変更を伴う変更
- 高リスク変更
- 長時間かかる変更

計画書の形式は `.agents/PLANS.md` に従ってください。
Plan status rules are defined in `.agents/PLANS.md`; use `Implementation complete` when code changes are done but review, validation, commit, or merge remains.
Plan 作成時は `docs/agent/COORDINATION_GATE.md` に従い、agent availability と execution mode を確認・記録してください。Codex は routing decision を自動確定せず、利用可能 agent、parallel execution、file ownership、locked files を plan に残してください。
Ownership、handoff、conflict prevention は共通ドキュメントを参照し、詳細ルールをこの adapter に重複させないでください。

## Workflow rehydration

file-changing work では、主要 workflow skill として `feature-planning` を明示的に使ってください。

次の場合は、active plan または checkpoint を読み直し、`feature-planning` を明示的に再呼び出してください。

- context compaction
- session resume
- agent handoff
- agent participation or withdrawal
- review feedback / review result の受領または対象 PLAN レビュー結果の作成
- scope expansion
- planning から implementation への移行
- implementation から validation への移行
- blocker 解消後の再開
- completion / handoff checkpoint の作成

再取得時は、会話履歴だけに依存せず、plan/checkpoint から current actor、participating agents、target files、locked files、completed work、current status、next action、unresolved decisions、blockers、review findings、validation results、handoff checkpoint、last updated information を復元してください。review feedback / review result を受け取る、または対象 PLAN のレビュー結果を作成する場合は、findings、採用/見送り/保留、対応要否、次担当、validation results、handoff checkpoint を active PLAN/checkpoint に記録してください。ユーザーが read-only review only を明示した場合は、PLAN 更新を行わず、その制約を応答に明記してください。

## Skills

- 手順化された作業は `.agents/skills/` の skill を優先してください。
- repo 初期化は `bootstrap-agent-repo` skill を使ってください。
- 計画作成・更新は `feature-planning` skill を優先してください。
- file-changing work の開始・再開・handoff・review feedback 受領・対象 PLAN レビュー結果の作成・scope expansion・validation 開始・completion / handoff checkpoint 作成では、`feature-planning` を明示的な再取得ポイントとして使ってください。

## Repository-specific expectations

- 変更は最小差分を優先する
- 既存構造に合わせる
- テスト・検証結果を残す
- agent 間で役割分担した場合も、共通 plan を更新する
- 非共有設定は `templates/nonshared/` から必要なものだけ採用する
- 参照者・責務分担・引き継ぎ・衝突防止は `docs/agent/OWNERSHIP.md`, `docs/agent/AGENT_ROLES.md`, `docs/agent/HANDOFF_PROTOCOL.md`, `docs/agent/COORDINATION_GATE.md` に従う
