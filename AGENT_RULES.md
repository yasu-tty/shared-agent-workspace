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

ファイルを変更する作業では、最初の non-plan file 編集前に `plans/*.md` を作成または更新する。既存の active plan の scope 内であれば、その plan を更新してよい。

既定で許可する例外は以下だけとする。

- read-only の調査
- `plans/*.md` の作成または更新そのもの
- ファイルを書き換えない検証コマンド

docs-only、formatter、生成物更新、小さな1ファイル修正であっても、ファイルを書き換える場合は plan を作成または更新する。

特に以下では、実装前に `plans/*.md` を作成または更新する。

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

- 明示承認なしに destructive 操作、不可逆操作、広範囲削除、履歴改変、秘密情報の露出につながる操作をしない
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

## 8. 作業時の core rules と workflow rehydration

このセクションは、常時失ってはいけない短い core と、必要時に戻る参照先を定義する。README や setup docs は入口案内であり、required order を再定義しない。

常時保持する core:

- 安全制約、destructive 操作の禁止、秘密情報・データ取扱い、明示承認が必要な操作
- file-changing work では、最初の non-plan file 編集前に `plans/*.md` を作成または更新すること
- file-changing work では、主要 workflow skill として `feature-planning` を使うこと
- file-changing work 開始時と session resume 時は、導入先 repo 固有の安全制約を確認するため `docs/agent/PROJECT_CONTEXT.md` を読むこと
- 共通事実と現在状態は、会話履歴ではなく `plans/` と `docs/agent/` に残すこと
- active plan、checkpoint、正本文書へ戻る導線を失わないこと

`feature-planning` を明示的に再呼び出す条件:

- file-changing work を始めるとき
- context compaction 後に再開するとき
- session resume 時
- agent handoff の送受信時
- agent の参加・離脱時
- review feedback / review result を受け取る、または対象 plan のレビュー結果を作成するとき
- scope expansion が必要になったとき
- planning から implementation へ移るとき
- implementation から validation へ移るとき
- blocker 解消後に再開するとき
- completion / handoff checkpoint を作るとき

状態復元時は、まず active plan または checkpoint を読み、current actor、participating agents、target files、locked files、completed work、current status、next action、unresolved decisions、blockers、review findings、validation results、handoff checkpoint、last updated を復元する。file-changing work 開始時または session resume 時は、non-plan file 編集前に `docs/agent/PROJECT_CONTEXT.md` を読み、データ取扱い、外部ツール利用、承認が必要な操作、明示承認なしに変更してはいけない範囲を確認する。その後、現在の trigger に必要な reference だけを読む。

review feedback / review result を受け取る、または対象 plan のレビュー結果を作成する場合は、口頭応答だけで終えず、findings、採用/見送り/保留、対応要否、次担当、validation results、handoff checkpoint を active plan または checkpoint に記録する。ユーザーが read-only review only を明示した場合は、PLAN 更新を行わず、その制約を応答に明記する。

必須または必要時に読む reference:

- plan 仕様: `.agents/PLANS.md`, `plans/README.md`, relevant `plans/*.md`
- repo 固有安全制約: `docs/agent/PROJECT_CONTEXT.md` は file-changing work 開始時と session resume 時に読む
- ownership / roles: `docs/agent/OWNERSHIP.md`, `docs/agent/AGENT_ROLES.md`
- handoff: `docs/agent/HANDOFF_PROTOCOL.md`
- routing / execution mode: `docs/agent/COORDINATION_GATE.md`
- testing / validation: `docs/agent/TESTING_POLICY.md`
- project setup / inventory: `docs/agent/SETUP.md`, `docs/agent/COMPONENT_INVENTORY.md`
- agent-specific entrypoints: `AGENTS.md`, `CLAUDE.md`
