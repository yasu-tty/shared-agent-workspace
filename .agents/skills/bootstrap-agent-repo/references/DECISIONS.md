# Design decisions

## Shared rules

この skill は、Codex と Claude Code の **共通コアを先に置く** 方針です。判断に迷う場合は、まず `AGENT_RULES.md`, `docs/agent/`, `plans/`, `.agents/skills/` に寄せ、agent 固有ディレクトリには薄い adapter だけを置きます。

## Canonical source

- 共通規約の正本は `AGENT_RULES.md`
- startup skill の canonical source は `.agents/skills/bootstrap-agent-repo/`
- 展開されるテンプレート本文は `.agents/skills/bootstrap-agent-repo/assets/templates/`
- Claude 側の同名 skill は、shared skill を使いやすくするための薄いアダプタ

## Adapter boundary

- Codex 固有:
  - `AGENTS.md`
  - `.codex/config.toml`
  - `.codex/agents/*.toml`
  - `.codex/hooks.json.example`
- Claude Code 固有:
  - `CLAUDE.md`
  - `.claude/settings*.json.example`
  - `.claude/rules/*.md`
  - `.claude/agents/*.md`
  - `.claude/skills/*`
- 共通:
  - `AGENT_RULES.md`
  - `.agents/PLANS.md`
  - `.agents/skills/*`
  - `plans/`
  - `docs/agent/`
  - `.mcp.json.example`

## Safety defaults

- hooks, MCP, local settings は `.example` を優先する
- 既存ファイルはデフォルトで上書きしない
- 強い副作用がある操作は明示実行前提
- bootstrap の再適用は `--force --backup` を使う
- template source tree に symlink がある場合は拒否する
- template 保守時は `--check-root-sync` で root と `assets/templates/` の同期漏れを検知する

## Operational model

- 新規 repo では dry-run 後に `--yes` で適用する
- 既存 repo では skip / identical / overwrite の結果を確認してから `--force` を使う
- 共有できる規約や plan は共通コアに戻す
- 個人差分、権限が強い設定、環境依存の設定は nonshared sample に留める
