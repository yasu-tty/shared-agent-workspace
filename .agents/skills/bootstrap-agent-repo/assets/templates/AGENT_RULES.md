# Agent Rules

このファイルは **Codex と Claude Code の共通規約の正本**です。

## 1. 基本姿勢

- 既存コード・既存設定・既存文書を先に読む
- 推測より根拠を優先する
- 変更は小さく分け、意図を説明できる状態にする
- 既存パターンがある場合はそれを踏襲する
- 失敗時の戻し方を意識して進める

## 2. 協調コーディングの原則

- 計画、実装、テスト/検証は分担してよい
- ただし、**共通の事実**は `plans/` と `docs/agent/` に残す
- 役割分担をした場合も、共通規約と共通 plan に従う
- エージェント固有の判断は、必要なら plan や progress log に残す
- 参照者、責務分担、変更許可、handoff、衝突防止は `docs/agent/OWNERSHIP.md`, `docs/agent/AGENT_ROLES.md`, `docs/agent/HANDOFF_PROTOCOL.md` に残す
- plan 起票時の agent availability、execution mode、parallel execution、file ownership、locked files は `docs/agent/COORDINATION_GATE.md` に従い、実装前に確認・記録する

## 3. 計画が必須のケース

以下では、実装前に `plans/*.md` を作成または更新する。

- 3ファイル以上変更する
- 複数の ownership area にまたがる
- 複数ディレクトリにまたがる変更
- API / schema / contract の変更
- 認証・認可・権限まわりの変更
- billing / payment に影響する変更
- deployment / CI に影響する変更
- shared component を変更する
- 既存テスト方針を変更する
- 高リスクな migration
- 既存挙動を維持したい大規模 refactor
- 障害時の影響が大きい変更

## 4. 実装ルール

- public API を壊す変更は移行方針を plan に明記する
- 重複が定着するまで抽象化を増やしすぎない
- コメントは「なぜ必要か」を優先する
- 秘密情報・生成物・ローカル環境依存ファイルは commit しない
- 設定追加時はデフォルト値、影響範囲、失敗時挙動を明記する

## 5. テストと検証

- バグ修正には、再現テストまたは回帰防止テストを付ける
- 単体テストで足りない変更は統合テストまたは手動検証を追加する
- テスト不能な変更は、理由と代替検証を plan に残す
- 実装担当と検証担当を分ける運用は歓迎する

## 6. ドキュメント更新

以下では文書更新も行う。

- 新しい設定、CLI、ジョブ、hook、MCP の追加
- 依存関係更新で運用が変わる場合
- 開発・デプロイ・障害対応フローの変更
- shared skill や agent 設定の変更

## 7. レビュー観点

- 仕様の意図に沿っているか
- 既存パターンから逸脱しすぎていないか
- 保守コストを不必要に増やしていないか
- 失敗時挙動とロールバックがあるか
- テストと文書更新が十分か

## 8. 作業時の共通参照順の正本

作業時の共通参照順はこのセクションを正本とする。README や setup docs は入口案内であり、required order を再定義しない。

1. `AGENT_RULES.md`
2. `docs/agent/COMPONENT_INVENTORY.md`
3. `docs/agent/SETUP.md`
4. `docs/agent/OWNERSHIP.md`
5. `docs/agent/AGENT_ROLES.md`
6. `docs/agent/HANDOFF_PROTOCOL.md`
7. `docs/agent/COORDINATION_GATE.md`
8. `.agents/PLANS.md`
9. `plans/README.md`
10. 関連する `plans/*.md`
11. `docs/agent/TESTING_POLICY.md`
12. agent 固有の入口ファイル (`AGENTS.md`, `CLAUDE.md`)

`docs/agent/TESTING_POLICY.md` は共通参照順に含める。特にテスト方針・検証方針を変更する作業、または validation 判断を伴う作業では必ず確認する。
