# shared-agent-workspace

この repo は、**Codex と Claude Code が同じ repo を参照し、計画・責務分担・handoff・検証結果を共有しながら協調コーディングする**ための workspace です。

## この repo / 同梱 skill でできること

- 新規または既存 repo に、AI エージェント（Codex / Claude Code）用の共通構成を導入・再適用できる
- plan、ownership、handoff、validation の記録により、作業を中断しても途中から復帰できる

## 目的

- 共通の規約・計画・検証方針を **1つの repo** に固定する
- Codex / Claude Code の固有機能は **薄いアダプタ層** として追加する
- `bootstrap-agent-repo` skill で、協調コーディングに必要な shared core / adapter / plan / handoff 文書を安全に導入・再適用する
- `feature-planning` skill で、scope、ownership、routing、validation、rollback を実装前に明文化する
- 危険な設定や個人設定は `.example` や `templates/nonshared/` に分離する

## 初回導入

1. 管理対象プロジェクトに必要な skill をコピーする

```text
<target repo>/.agents/skills/bootstrap-agent-repo/
<target repo>/.agents/skills/feature-planning/
```

2. 管理対象プロジェクト root で AI エージェントを起動する

3. プロンプトで明示する

```text
以下を読んだうえで、このプロジェクトに協調コーディング用の構成を導入してください。

- .agents/skills/bootstrap-agent-repo/SKILL.md
- .agents/skills/feature-planning/SKILL.md
```

## 入口として見る場所

作業時の共通参照順は `AGENT_RULES.md` を正とする。初回理解の入口として、以下を確認する。

- `AGENT_RULES.md`
- `AGENTS.md`
- `CLAUDE.md`
- `docs/agent/SETUP.md`

## 主要構成

### 共通コア
- `AGENT_RULES.md`
- `.agents/PLANS.md`
- `plans/`
- `docs/agent/`
- `docs/agent/OWNERSHIP.md`
- `docs/agent/AGENT_ROLES.md`
- `docs/agent/HANDOFF_PROTOCOL.md`
- `docs/agent/COORDINATION_GATE.md`
- `.agents/skills/bootstrap-agent-repo/`
- `.agents/skills/feature-planning/`
- `.mcp.json.example`

### Codex アダプタ
- `AGENTS.md`
- `.codex/config.toml`
- `.codex/agents/*.toml`
- `.codex/hooks.json.example`

### Claude Code アダプタ
- `CLAUDE.md`
- `.claude/settings.json.example`
- `.claude/settings.local.json.example`
- `.claude/rules/*.md`
- `.claude/agents/*.md`
- `.claude/skills/*` （共通 skill への薄いミラー/アダプタ）

### 非共有サンプル
- `templates/nonshared/`

## Skill の配置方法

- Codex 向けの canonical skill は `.agents/skills/<skill-name>/` に配置する
- Claude Code 向けの adapter は `.claude/skills/<skill-name>/` に配置する
- Claude adapter が canonical source を参照する場合は、`.claude/skills/*` だけでなく対応する `.agents/skills/*` も同梱する
- `bootstrap-agent-repo` は `scripts/`, `references/`, `assets/templates/` を含む `.agents/skills/bootstrap-agent-repo/` が canonical source
- `feature-planning` は `.agents/PLANS.md` と `docs/agent/COORDINATION_GATE.md` などの共通 docs と一緒に使う

## 推奨運用

- 共通規約の正本は `AGENT_RULES.md`
- Codex の入口は `AGENTS.md`
- Claude Code の入口は `CLAUDE.md`
- 変更計画は `plans/*.md`
- 計画の仕様は `.agents/PLANS.md`
- 参照者・責務分担・handoff は `docs/agent/OWNERSHIP.md`, `docs/agent/AGENT_ROLES.md`, `docs/agent/HANDOFF_PROTOCOL.md`
- plan 起票時は `docs/agent/COORDINATION_GATE.md` で agent availability と execution mode を確認・記録する
- repo への導入・再適用は `bootstrap-agent-repo` skill で行う
- 導入・再適用される共有構成の配布元は `.agents/skills/bootstrap-agent-repo/assets/templates/`
- リスクのある設定は `.example` をコピーして有効化する

## 最初に整えること

以下は、`bootstrap-agent-repo` で共有構成を導入・再適用した導入先 repo で行う初期調整です。

1. `AGENT_RULES.md` を技術スタックとチーム運用に合わせて具体化する
2. `docs/agent/OWNERSHIP.md` の repository consumers と ownership matrix を repo 用に更新する
3. `docs/agent/AGENT_ROLES.md` で agent / human の責務を割り当てる
4. `.codex/config.toml` と `.claude/settings.json.example` を環境に合わせて調整する
5. `.mcp.json.example` の必要部分だけ有効化する
6. `plans/template.md` を使って最初の案件 plan を起こす
7. multi-agent work 前に `docs/agent/COORDINATION_GATE.md` と `docs/agent/HANDOFF_PROTOCOL.md` を確認する

## Bootstrap script

AI エージェントまたは保守者が bootstrap script を直接実行する場合:

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --dry-run
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --yes
```

既存 repo に古い `bootstrap-agent-repo` 更新を再適用する場合:

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --dry-run
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --check-root-sync
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --force --backup --yes
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --dry-run
```

再適用後は、`.agents/bootstrap-backups/<timestamp>/` と更新後ファイルを必ず比較し、repo 固有情報が汎用文書で消えていないか確認する。`--check-root-sync` が失敗しても、root 側だけに残す意図的な repo 固有差分であれば、plan や docs に明記して運用する。

詳細な再適用手順は `.agents/skills/bootstrap-agent-repo/references/USAGE.md` と `.agents/skills/bootstrap-agent-repo/references/POST_BOOTSTRAP_CHECKLIST.md` を参照する。
