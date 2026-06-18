# Claude Code Project Instructions

@AGENT_RULES.md
@docs/agent/COMPONENT_INVENTORY.md
@docs/agent/PROJECT_CONTEXT.md
@docs/agent/SETUP.md
@docs/agent/OWNERSHIP.md
@docs/agent/AGENT_ROLES.md
@docs/agent/HANDOFF_PROTOCOL.md
@docs/agent/COORDINATION_GATE.md
@.agents/PLANS.md
@plans/README.md
@docs/agent/TESTING_POLICY.md

## Claude-specific guidance

- shared rules は `AGENT_RULES.md` と `.agents/PLANS.md` を正とする
- repo 固有コンテキストは `docs/agent/PROJECT_CONTEXT.md` を確認する
- ファイルを変更する作業では、最初の non-plan file 編集前に `plans/*.md` を作成または更新する
- 計画書の形式は `.agents/PLANS.md` に従う
- Plan status rules are defined in `.agents/PLANS.md`; `Completed` はレビュー、検証、commit / merge まで終わった場合だけ使う
- Plan 作成時は `docs/agent/COORDINATION_GATE.md` に従い、agent availability と execution mode を確認・記録する
- Ownership と handoff は `docs/agent/OWNERSHIP.md` と `docs/agent/HANDOFF_PROTOCOL.md` に従う
- Claude Code 側も coordination gate に従い、自動 routing や parallel execution を独自判断で確定しない
- `.claude/rules/` に path-specific ルールがある場合は尊重する
- `.claude/skills/` の該当 skill があれば優先的に使う
- 個人用の差分は `CLAUDE.local.md` または `.claude/settings.local.json` に置く
- Codex と分担した場合も、共通の進捗と検証結果は `plans/*.md` に戻す
