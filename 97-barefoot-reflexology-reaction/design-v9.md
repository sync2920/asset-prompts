# 足つぼマット・リアクション v9 デザイン設計ノート

本設計は、画像参照元（`main/_profile/01.png`）の成人同一性・プロポーションをベースに、v8の**アウター仕立てビスチェ × リラックスストレートデニム**のコーディネートと朝のリビング設定を完全維持した上で、ユーザー指定の3点（カメラ高度・黒ローライト・バスト微増）に絞って精密に調整した3:4縦構図の最終改訂版である。

---

## 1. v9 における改訂内容（3大変更点）

1. **カメラ高度・角度・距離の微調整（ハイ・オブリーク全身ショット）**:
   * **レンズ物理高**: 被写体の頭頂部より**20〜30cm高い位置**（目線からではなく頭頂部基準でさらに引き上げ）。
   * **撮影距離**: **3.0〜3.4m**（引きを十分に確保）。
   * **見下ろし角**: 下向き**18〜22度**の緩やかな傾斜。
   * **構図効果**: 対角3/4の全身ショットとして、頭頂部上の適度なヘッドルームを保ちつつ、足元の素足とティール色足つぼマット全体を下部フレームに明瞭に収める。急角度の真上トップダウン（バードアイ）を厳格に禁止し、頭部肥大・脚の短縮（短足化）やパース歪みを完全に防止。

2. **ヘアスタイルの部分アップデート（極細ブラック・ローライトの追加）**:
   * 参照画像のベース（肩にかかる長さ・柔らかなウェーブ・シースルーバング・アッシュブロンド基調）を100%保持。
   * トップレイヤーの内側（アンダーセクション）および顔周りの2束に、**視覚幅3〜5mmの細い黒メッシュ状ローライト**を控えめに追加。
   * 太いストライプやツートーン（半分黒髪）、別ヘアカット化を避け、サロン仕上げのようにベースカラーへ自然に溶け込む統合質感として指定。

3. **バストボリュームの微増（+10〜12% / 1段階の自然な強調）**:
   * 参照画像から約1段階（約10〜12%）のわずかなボリュームアップを指定。
   * ビスチェの立体カップ容量の拡大、幅広のサイドパネル、生地の自然なテンション（張力）によって実現。
   * 肩幅、リブケージ、ウエスト、ヒップ、四肢、身長、全身プロポーションは参照と完全に同一を維持。
   * 極端なプッシュアップ、不自然な胸の巨大化、胴体比率の崩壊を排除し、中央の上品な浅い谷間の影（partial central cleavage）、脇と下部の完全なカバーを維持。

---

## 2. 厳密な保持要素と同一性保護

* **顔同一性と輪郭**:
  * 参照画像の顔立ち・目元・口元を忠実に保持。
  * 俯瞰アングルに伴いやすい「面長化（lengthening）」や「過度な小顔・細身化（narrowing）」をネガティブプロンプトおよび本文で明示的に防止。
* **表情・アイコンタクト**:
  * 顎をわずかに上げて見下ろしカメラのレンズを直視（上目遣いによる白目過多の防止）。
  * 口を閉じた温かく愛嬌のある微笑み（「痛いけれど平気」という自嘲的ニュアンス）。
  * 眉間のわずかな緊張と片足への荷重シフトのみで足つぼ刺激を表現し、激しいしかめ面・絶叫・跳躍を完全排除。
* **衣装・シーン・小道具**:
  * **トップス**: Warm Ivoryの厚手コットンツイル外着ビスチェ（幅2.5cmストラップ、浅いスウィートハートネック、4本プリンセスシーム、お腹の露出ゼロ）。
  * **ボトムス**: Washed Matte Blackのハイライズ・リラックスストレートアンクルデニム（くるぶし上丈で素足・10本の足指を完全に露出）。
  * **マット**: 独立したソリッドなMuted Teal（くすみ青緑）ラバーマット、丸みを帯びた低めの突起。
  * **シーン**: 8月14日の夏の夜明け、自然な木目フローリングの日本の明るいリビング。

---

## 3. 生成リスクと安全設計

| リスク項目 | 発生しやすい崩壊 | プロンプトでの対策・ガード |
| :--- | :--- | :--- |
| **カメラ高度上昇によるパース崩壊** | 見下ろし角の増加に伴う頭部肥大・極端な短足化 | `20-30cm above the top of her head`, `3.0-3.4m away`, `downward 18-22 degrees`, `no steep overhead, no bird's-eye view, no large-head foreshortening, no compressed leg distortion` |
| **メッシュ指定の過剰反応** | 髪全体が黒くなったり太い縞模様・別髪型になる | `sparse, narrow black mesh-like lowlight strands (3-5mm visual width)`, `concentrated beneath top layer and face-framing`, `integrated salon lowlights, no chunky stripes, no half-black hair` |
| **バスト強調の過剰反応** | 不自然な巨大化・露骨な露出・ランジェリー化 | `approximately one modest visual step or 10-12% additional fullness`, `larger cup volume and supportive side panels`, `no extreme push-up, no oversized chest, sides and underside fully covered` |
| **顔のプロポーション変化** | 見下ろしによる顎の尖りすぎ・面長化・細顔化 | `strictly avoiding narrowing or lengthening her face`, `chin slightly raised`, `authentic reference proportions and soft contour` |
| **足指とマット突起の癒着** | 引きの構図での素足・足指の潰れ・突起との融合 | 踏み込み足（指の軽い屈曲）と浮かせ足（踵上げ）の個別記述、`all ten distinct well-formed toes`, `no toe clipping or fusion` |

---

## 4. 保存ファイル

* [`prompt-v9-higher-black-lowlights-fuller-bust.txt`](file:///home/natrial/_work/X/asset-prompts/97-barefoot-reflexology-reaction/prompt-v9-higher-black-lowlights-fuller-bust.txt): コピー用完成プロンプト（英語テキスト単体）
* [`design-v9.md`](file:///home/natrial/_work/X/asset-prompts/97-barefoot-reflexology-reaction/design-v9.md): 本設計ノート（日本語解説）
