# bootstrap-agent-repo

## 概要

`bootstrap-agent-repo` は、新規または既存の repo に Codex と Claude Code の協調コーディング用テンプレート構成を展開する skill です。`AGENT_RULES.md`、`plans/`、`.agents/`、`.codex/`、`.claude/` などの標準構成を安全に追加または再適用する場面で使います。

## 使う場面

- 新しい repo に AI agent 用の標準構成を導入したい
- 既存 repo に共通の agent 規約、plan、adapter、skill 雛形を追加したい
- チーム標準の更新を別 repo に再適用したい
- 既存ファイルを壊さずに、まず dry-run で差分を確認したい

## 利用前提

- Python 3 が使えること
- repo ルートから実行すること
- 既存ファイルを更新する場合は、差分と backup の扱いを確認すること
- multi-agent work の前に `docs/agent/PROJECT_CONTEXT.md`, `docs/agent/OWNERSHIP.md`, `docs/agent/HANDOFF_PROTOCOL.md` を確認すること

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

Codex 向けには、この skill を `.agents/skills/bootstrap-agent-repo/` に配置します。Codex の入口である `AGENTS.md` からは、手順化された作業として `.agents/skills/` 配下の skill を優先して参照します。

Claude Code 向けには、adapter を `.claude/skills/bootstrap-agent-repo/` に配置します。Claude adapter は単体で完結するものではなく、canonical source と bootstrap script が `.agents/skills/bootstrap-agent-repo/` にある前提で動きます。

この skill を公開または別 repo に配布する場合は、少なくとも `.agents/skills/bootstrap-agent-repo/` を同梱し、Claude Code でも使う場合は対応する `.claude/skills/bootstrap-agent-repo/` adapter も同梱してください。

## 含まれるファイル

- `SKILL.md`: agent が参照する skill 本体
- `README.md`: 利用者向けの説明
- `LICENSE.txt`: この skill のライセンス
- `scripts/bootstrap.py`: テンプレート展開 script
- `assets/templates/`: 展開されるテンプレート本文
- `references/`: 詳細な使い方、layout、bootstrap 後チェックリスト

## ライセンス

この skill は Apache License 2.0 で提供されます。詳細は `LICENSE.txt` を確認してください。

## 注意事項

- `SKILL.md` が agent 向け手順の正本です。この README は利用者向けの補助説明です。
- デフォルトでは既存ファイルを上書きしません。
- `docs/agent/PROJECT_CONTEXT.md` は未作成時だけ作成し、再適用時は `preserve` として上書きしません。
- `--force` を使う前に dry-run と backup 方針を確認してください。
- root files と `assets/templates/` の同期が必要な変更では、必ず `--check-root-sync` を実行してください。
