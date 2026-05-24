# Setup

## 1. この文書の位置づけ

この文書は初期有効化ガイドである。作業時の共通参照順は `AGENT_RULES.md` の「作業時の共通参照順の正本」を正とする。

## 2. 安全な初期有効化

### Codex
- `.codex/config.toml` を調整する
- `.codex/hooks.json.example` は必要な場合だけ `.codex/hooks.json` にコピーする
- `.codex/agents/*.toml` を必要に応じて有効化・編集する

### Claude Code
- `.claude/settings.json.example` を必要なものだけ `.claude/settings.json` に反映する
- `.claude/settings.local.json.example` は個人用として使う
- `.claude/rules/` と `.claude/agents/` を必要に応じて調整する

### MCP
- `.mcp.json.example` を必要な範囲だけ `.mcp.json` にコピーする

## 3. Project context

Bootstrap 後、multi-agent work の前に `docs/agent/PROJECT_CONTEXT.md` を repo 用に更新する。
このファイルは導入先 repo が管理する共有コンテキストであり、bootstrap は未作成時に作成するが、再適用時は上書きしない。

`PROJECT_CONTEXT.md` には、導入先 repo が必要とするデータ取扱方針や、ログ出力・外部ツール利用などの repo 固有ルールを書く。
共有すべきでない値そのものは書かない。

## 4. startup skill

repo 初期化や標準構成の展開には、共通 canonical skill である
`.agents/skills/bootstrap-agent-repo/` を使う。

Claude 側では `.claude/skills/bootstrap-agent-repo/` が薄いアダプタとして同梱されている。

### 推奨コマンド

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --dry-run
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --yes
```

既存ファイルをテンプレートで更新する場合だけ、差分確認後に以下を使う。

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --force --backup --yes
```

古い skill 更新を既存 repo に再適用する場合は、まず `.agents/skills/bootstrap-agent-repo/references/USAGE.md` の再適用フローを使い、`--check-root-sync` と再適用後のバックアップ比較まで実施する。

bootstrap のテンプレート本文は `.agents/skills/bootstrap-agent-repo/assets/templates/` にある。
導入先 repo の root `README.md` はこの配布テンプレートに含めない。
`SKILL.md` は短い入口に留め、詳細な使用方法や設計判断は `references/` に置く。

Bootstrap 後、multi-agent work の前に `docs/agent/PROJECT_CONTEXT.md` を更新し、`docs/agent/OWNERSHIP.md` の placeholder を repo 用に置き換え、`docs/agent/HANDOFF_PROTOCOL.md` を確認する。
このテンプレート自体を保守する場合は、root files と `.agents/skills/bootstrap-agent-repo/assets/templates/` を同期させる。

## 5. 非共有サンプル

以下は commit 前提ではなく、必要時に各自が採用する。

- `templates/nonshared/user-home/`
- `templates/nonshared/project-local/`
- `templates/nonshared/admin/`
