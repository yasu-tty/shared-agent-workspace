---
description: 協調コーディング時の補助ルール
paths:
  - "**"
---

- 既存の `plans/*.md` があれば先に読む
- Plan status rules are defined in `.agents/PLANS.md`; Progress log を現在状態の代替にしない
- Ownership は `docs/agent/OWNERSHIP.md`、役割は `docs/agent/AGENT_ROLES.md` を参照する
- 作業開始・進捗・完了・衝突対応は `docs/agent/HANDOFF_PROTOCOL.md` を参照する
- plan 起票時の agent availability、execution mode、parallel execution、file ownership、locked files は `docs/agent/COORDINATION_GATE.md` を参照する
- 実装・検証・レビューで handoff した場合は progress log に残す
- 共通規約より agent 固有設定を優先しない
