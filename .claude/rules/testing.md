---
description: テスト・検証関連ファイルに対する補助ルール
paths:
  - "tests/**"
  - "**/*test*"
  - "**/*spec*"
---

- 既存テストスタイルを踏襲する
- flaky になりやすい待機や時刻依存を増やさない
- 実装変更時は、失敗ケースも見直す
- テスト方針や snapshot を変える場合は `docs/agent/OWNERSHIP.md` と `.agents/PLANS.md` の owner/review owner を確認する
