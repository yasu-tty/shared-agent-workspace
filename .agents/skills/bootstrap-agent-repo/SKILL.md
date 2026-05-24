---
name: bootstrap-agent-repo
description: 新規または既存 repo に、Codex と Claude Code の協調コーディング用テンプレート構成を展開する。repo 初期化、標準構成の再投入、AI agent 用ディレクトリ雛形の作成で使う。既存ファイルを壊したくない場合や副作用を避けたい場合は、先に dry-run で確認する。
license: Apache-2.0
metadata:
  author: "Yasu (@yasu-tty)"
  version: "0.1.0"
---

# Bootstrap Agent Repo

## Goal

Codex と Claude Code の AI agent 協調コーディング用テンプレートを、現在の repo に安全に展開する。

## Use this when

- 新しい repo に AI agent 用の標準構成を入れたい
- 既存 repo に `AGENT_RULES.md`, `AGENTS.md`, `CLAUDE.md`, `plans/`, `.agents/`, `.codex/`, `.claude/` の雛形を足したい
- チーム標準の更新を別 repo に再適用したい

## Procedure

1. 必要な詳細だけ `references/USAGE.md` と `references/LAYOUT.md` で確認する
2. まず dry-run する: `python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --dry-run`
3. 問題なければ適用する: `python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --yes`
4. 既存ファイルを更新する場合だけ、root `README.md` が対象に含まれないことを dry-run で確認してから `--force --backup` を追加する
5. テンプレート保守時は `--check-root-sync` で root と `assets/templates/` の同期を確認する
6. `references/POST_BOOTSTRAP_CHECKLIST.md` に従い、repo 固有コンテキストは `docs/agent/PROJECT_CONTEXT.md` に集約する
7. Bootstrap 後に `docs/agent/PROJECT_CONTEXT.md` と `docs/agent/OWNERSHIP.md` を確認する
8. Multi-agent work の前に placeholder agent roles を割り当てるか置き換える
9. Parallel coding の前に `docs/agent/COORDINATION_GATE.md` と `docs/agent/HANDOFF_PROTOCOL.md` を確認する
10. root files と `assets/templates/` を同期した状態に保つ

## Notes

- デフォルトでは既存ファイルを上書きしない
- 導入先 repo の root `README.md` は作成・上書きしない
- source tree 内の symlink はコピーせず拒否する
- `assets/templates/` が展開されるテンプレート本文
- この skill 自体は `.agents/skills/bootstrap-agent-repo/` に自己インストールされる
- Codex / Claude Code 固有設定は薄い adapter として扱う
- 危険な設定や個人設定は `.example` または `templates/nonshared/` に置く
- Coordination rules は `docs/agent/OWNERSHIP.md`, `docs/agent/AGENT_ROLES.md`, `docs/agent/HANDOFF_PROTOCOL.md`, `docs/agent/COORDINATION_GATE.md` を正とする
