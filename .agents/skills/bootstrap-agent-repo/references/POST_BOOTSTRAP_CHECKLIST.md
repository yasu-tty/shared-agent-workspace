# Post Bootstrap Checklist

- [ ] `AGENT_RULES.md` を技術スタックとチーム運用向けに具体化した
- [ ] `docs/agent/COMPONENT_INVENTORY.md` が実際に採用する adapter と一致している
- [ ] `docs/agent/OWNERSHIP.md` の repository consumers と ownership matrix を repo 用に更新した
- [ ] `docs/agent/AGENT_ROLES.md` の placeholder role を multi-agent work 前に割り当てた
- [ ] parallel coding 前に `docs/agent/HANDOFF_PROTOCOL.md` の start/progress/completion/conflict protocol を確認した
- [ ] `docs/agent/TESTING_POLICY.md` をテスト戦略に合わせた
- [ ] `.codex/config.toml` を approval / sandbox / model 方針に合わせた
- [ ] `.codex/hooks.json.example` を有効化する場合は内容を確認してから `.codex/hooks.json` にコピーした
- [ ] `.claude/settings.json.example` から必要な設定だけを `.claude/settings.json` に反映した
- [ ] `.claude/settings.local.json.example` は個人設定として扱い、共有しない方針を確認した
- [ ] `.mcp.json.example` を必要な範囲だけ `.mcp.json` に反映した
- [ ] `templates/nonshared/` から採用するものを選び、共有 repo に直接入れないものを確認した
- [ ] 不要な adapter や skill を削除または簡略化した
- [ ] 最初の案件 plan を `plans/` に作成した
- [ ] `python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --dry-run` が期待通り `identical` または意図した差分だけを示す
- [ ] 既存 repo に `--force --backup --yes` で再適用した場合は、`.agents/bootstrap-backups/<timestamp>/` と更新後ファイルを比較し、repo 固有情報が消えていないことを確認した
- [ ] 再適用後に必要な汎用変更は `assets/templates/` へ移し、repo 固有変更は root 側だけに残す方針で切り分けた
- [ ] `python3 .agents/skills/bootstrap-agent-repo/scripts/bootstrap.py --target . --check-root-sync` の結果を確認し、意図的な root 固有差分がある場合は plan または docs に記録した
