# bootstrap-agent-repo

## 概要

`bootstrap-agent-repo` は、新規または既存の repo に Codex と Claude Code の協調コーディング用テンプレート構成を展開する skill です。このディレクトリは Claude Code から使うための adapter で、共有 skill の考え方とテンプレート構成に従います。

## 使う場面

- 新しい repo に AI agent 用の標準構成を導入したい
- 既存 repo に共通の agent 規約、plan、adapter、skill 雛形を追加したい
- チーム標準の更新を別 repo に再適用したい
- 既存ファイルを壊さずに、まず dry-run で差分を確認したい

## 利用前提

- Python 3 が使えること
- repo ルートから実行すること
- canonical source は `.agents/skills/bootstrap-agent-repo/` にあること
- multi-agent work の前に `docs/agent/OWNERSHIP.md` と `docs/agent/HANDOFF_PROTOCOL.md` を確認すること

## 基本的な使い方

まず dry-run で展開内容を確認します。

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --dry-run
```

問題なければ適用します。

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --yes
```

既存ファイルをテンプレートで更新する場合だけ、backup 付きで強制適用します。

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --force --backup --yes
```

テンプレート保守時は root と `assets/templates/` の同期を確認します。

```bash
python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --check-root-sync
```

## Codex / Claude Code 向け配置方法

Codex 向けには、canonical source を `.agents/skills/bootstrap-agent-repo/` に配置します。Codex の入口である `AGENTS.md` からは、repo 初期化や標準構成の再適用時にこの canonical skill を参照します。

Claude Code 向けには、この adapter を `.claude/skills/bootstrap-agent-repo/` に配置します。この adapter は `.agents/skills/bootstrap-agent-repo/` の `SKILL.md`、`references/`、`scripts/bootstrap.py` を参照するため、canonical source と一緒に配置してください。

この skill を公開または別 repo に配布する場合は、Claude adapter だけを切り出さず、`.agents/skills/bootstrap-agent-repo/` と `.claude/skills/bootstrap-agent-repo/` をセットで配布してください。

## 含まれるファイル

- `SKILL.md`: Claude Code adapter としての skill 入口
- `README.md`: 利用者向けの説明
- `LICENSE.txt`: この skill adapter のライセンス

## ライセンス

この skill adapter は Apache License 2.0 で提供されます。詳細は `LICENSE.txt` を確認してください。

## 注意事項

- `SKILL.md` が agent 向け手順の正本です。この README は利用者向けの補助説明です。
- 実際の bootstrap script と詳細資料は canonical source の `.agents/skills/bootstrap-agent-repo/` にあります。
- root と template の adapter 内容は同期対象です。保守時は `--check-root-sync` を実行してください。
