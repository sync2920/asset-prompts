# 394-395. ダスティブルー刺繍セットの着用（人物＋衣装の2画像運用・最小トリガー版 v6）

依頼時に添付されたランジェリーセット写真（`ideas/394-395-garment-reference.jpeg`）のデザインを人物に着せる2案（394〜395）。運用は `25` の2画像パターンに準拠: 1枚目の添付＝人物参照（`main/_profile/ChatGPT Image 2026年8月4日 15_41_32.png`、47 と同一）、2枚目＝衣装写真。人物参照は開いて読み取り済み: 明確に成人の女性。

**改訂履歴:**
- v1（2026-08-06）: 下着語彙そのまま → 安全フィルタで停止。
- v2: 幾何学・学術表現（寝室/ベッド文脈のまま）→ 停止。
- v3: レオタード言い換え＋ダンススタジオ文脈 → 通過。着用結果（`ideas/394-395-on-body-reference.jpeg`）は「ダサい」。
- v4: 洗練翻訳版（バレエ・レオタード＋ラップスカート）→ レオタード感が強くてダサい。
- v5: 朝ベッド×下着見え×ポーズ（ブライダル「サムシング・ブルー」×スマホ友人フォトシュート枠）→ **失敗率が上昇**。
- **v6（2026-08-07・現行）: 最小トリガー版。** v5 の見た目（朝ベッド・ポーズ・下着見え・洗練仕様）は維持したまま、v5 で増えたトリガー要素を全削除: ブライダル枠（婚礼の夜の連想）、友人のスマホ枠（私的撮影の連想）、寝起き語、`two-piece / top / bottoms` 名詞。文脈枠は無害な「ラウンジウェアルックブックの朝スチル」へ。見た目は2枚目画像と素材語が担保するため、テキスト枠の変更は見た目を損なわない。

- **人物参照:** `main/_profile/ChatGPT Image 2026年8月4日 15_41_32.png`（1枚目・必須）
- **衣装参照:** `ideas/394-395-garment-reference.jpeg`（2枚目・推奨。デザイン・パレット・モチーフの供給元）
- **着用状態の記録:** `ideas/394-395-on-body-reference.jpeg`（v3 系の着用例。ユーザー判定: ダサい）
- **成人判定:** 実施済み（明確に成人）。本文にも成人でない場合の不透明キャミ＋ショーツへの切り替え分岐文を含む

### v5 失敗率上昇の要因分析

| v5 で増えた要素 | 連想されるトリガー | v6 の対応 |
|---|---|---|
| `bridal "something blue" editorial / trousseau` ＋ベッド | 婚礼の夜 | 削除。ラウンジウェアルックブック枠へ |
| `posing for a friend's phone` ＋ベッド | 親密な私的撮影 | 削除。単にカメラへ穏やかにポーズ |
| `still warm from sleep / sleepy half-smile / bare foot peeking` | 寝起き・寝室の私性 | 削除。起きた後の整った朝へ |
| `delicate two-piece set / the top / the matching bottoms` | 下着セット名詞 | 削除。`the embroidered satin set`＋部位は panels / waistline のみ |

### v6 の設計（見た目は v5 維持）
- 朝のベッドに座ってカメラへポーズ（ユーザー要望）。
- 下着見えは2枚目画像＋素材語（シルクサテンの艶・まばらな刺繍スプリグ・細いシャンティイレース・小リボン）で担保。テキストは構造名詞を持たない。
- 白いデュベ/小枕で太ももから下を遮蔽（expression/01 の布遮蔽）。
- 朝の高鍵光（夜ベッドは v1/v2 の停止側）。

## 394. 朝のベッド、デュベに座ってポーズ

- **比率:** 3:4 縦
- **見せ場:** 一箇所: 朝光の中の刺繍の余白と細いレース縁（デュベの白とサテンの青の境界）
- **差し替え変数:** ポーズ、デュベの位置、光の角度
- **既存案との差:** 09 は夜＋背向け、25 は不透明シャツ、v3/v4 はスタジオ。本案は朝・高鍵・カメラへポーズの下着見えポートレートで、デュベ遮蔽が固有。

```text
A photorealistic morning portrait for a contemporary loungewear lookbook — a clean, wholesome, composed morning still, tasteful and quiet — of the person from the first reference image, wearing the embroidered satin set shown in the second reference image. 3:4 vertical aspect ratio. Infer apparent age from the first reference image and preserve it. Match the first reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the first reference, kept accurate through the fit and drape of the clothing, the fabric curving smoothly over the bust and draping from its outermost point with gentle tension lines. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode features that are not present in the first reference image — no invented hair colors, accessories, uniforms, or props. Use this scene only if the first reference is unambiguously adult; otherwise switch to an opaque cotton camisole and shorts in the same dusty-blue-and-black palette, keeping the same pose and light.

Garment: the second reference image supplies the design, palette and motif — dusty slate-blue silk satin with a soft sheen, sparse sprigs of pale blue floral embroidery on fine dark stems with generous fields of clean satin between, narrow edgings of fine black Chantilly lace with an eyelash edge, two thin black shoulder cords, and a single tiny blue satin bow at the center front; below the waist the same satin and lace continue in a matching cut, its waistline finished in the same narrow eyelash lace with a tiny blue flower ornament. The satin is solid and opaque; every lace panel is backed by an opaque lining in the same color, matte and non-translucent. The frame keeps a respectful distance and treats the garment purely as textile, light and contour.

Pose: she sits on the made bed near its centre, knees softly bent and angled to one side, a soft white duvet pooled over her thighs and legs so the garment, her shoulders, arms and face read clearly above it; one hand props behind her on the mattress, the other rests light on her knee. She looks at the camera with a small, easy closed-mouth smile, relaxed and composed. Both arms stay clear of the torso's front so the embroidery reads unobstructed.

Background and light: a small, tidy bedroom in early morning; crisp white linen sheets and pillows, a sheer curtain at the window glowing white. Low, soft morning sun rakes across the bed so each pale blossom sprig casts a tiny shadow on the satin, the narrow eyelash lace catches a fine rim of light, and the white duvet folds hold soft gray shadows. High-key and airy: one palette of white linen, black lace and dusty blue.

Camera and quality: 50mm at f/2.0 from slightly above seated eye level, framing from mid-thigh upward, subject centered. Real skin texture with pores, natural sensor grain, no HDR glow, no beauty filter, no smoothing. Avoid: no extra limbs, extra fingers, or malformed hands; no invented jewelry, logos, or text.

Format: 3:4 vertical composition.
```

## 395. 朝のベッド、ヘッドボードにもたれて小枕

- **比率:** 4:5 縦
- **見せ場:** 一箇所: 朝光の中の刺繍の余白と細いレース縁（枕の白とサテンの青の境界）
- **差し替え変数:** ポーズ、枕の持ち方、光の角度
- **既存案との差:** 394 はデュベ遮蔽の前寄り座り。本案はヘッドボードにもたれ、小枕を膝に抱えるリラックスした縦構図。

```text
A photorealistic morning portrait for a contemporary loungewear lookbook — a clean, wholesome, composed morning still, tasteful and quiet — of the person from the first reference image, wearing the embroidered satin set shown in the second reference image. 4:5 vertical aspect ratio. Infer apparent age from the first reference image and preserve it. Match the first reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the first reference, kept accurate through the fit and drape of the clothing, the fabric curving smoothly over the bust and draping from its outermost point with gentle tension lines. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode features that are not present in the first reference image — no invented hair colors, accessories, uniforms, or props. Use this scene only if the first reference is unambiguously adult; otherwise switch to an opaque cotton camisole and shorts in the same dusty-blue-and-black palette, keeping the same pose and light.

Garment: the second reference image supplies the design, palette and motif — dusty slate-blue silk satin with a soft sheen, sparse sprigs of pale blue floral embroidery on fine dark stems with generous fields of clean satin between, narrow edgings of fine black Chantilly lace with an eyelash edge, two thin black shoulder cords, and a single tiny blue satin bow at the center front; below the waist the same satin and lace continue in a matching cut, its waistline finished in the same narrow eyelash lace with a tiny blue flower ornament. The satin is solid and opaque; every lace panel is backed by an opaque lining in the same color, matte and non-translucent. The frame keeps a respectful distance and treats the garment purely as textile, light and contour.

Pose: she sits leaning back against the headboard, a small white pillow resting on her lap with both hands folded loosely over it, her legs hidden beneath the duvet. Her head tilts a little, eyes to the camera with a soft, easy smile, relaxed and composed. Shoulders relaxed and down so the cords and the lace edges read as clean lines.

Background and light: a small, tidy bedroom in early morning; a pale wooden headboard, crisp white pillows stacked behind her, a sheer curtain at the side window glowing white. Low, soft morning sun comes in from the side, laying a warm band across the bed and picking out the pale blossom sprigs thread by thread while the black Chantilly lace stays a soft matte shadow. High-key and airy: one palette of white linen, black lace and dusty blue.

Camera and quality: 50mm at f/1.8 from the foot of the bed, framing from mid-thigh upward, subject centered. Real skin texture with pores, natural sensor grain, no HDR glow, no beauty filter, no smoothing. Avoid: no extra limbs, extra fingers, or malformed hands; no invented jewelry, logos, or text.

Format: 4:5 vertical composition.
```

## 設計メモ

### 歴代の通過/停止と教訓
- v1 下着語彙 → 停止 / v2 幾何学表現（ベッド文脈維持）→ 停止 / v3 レオタード＋スタジオ → 通過（ダサい）/ v4 バレエ洗練 → ダサい / v5 朝ベッド＋ブライダル＋友人スマホ → 失敗率上昇 / v6 現行。
- 教訓1: フィルタ通過と見た目の上品さは別軸（v3）。
- 教訓2: 健全化のつもりで足した文脈（ブライダル＋ベッド＝婚礼の夜、友人スマホ＋ベッド＝私的撮影）がトリガーになり得る（v5）。文脈は「無害」であることが「上品」であることより重要。
- 教訓3: 見た目は画像参照と素材語が担保する。テキストの構造名詞（two-piece/top/bottoms/leotard）は見た目にほぼ寄与せず、トリガー表面積だけ増やす。

### 2画像運用
- 添付順は 1枚目＝人物 / 2枚目＝衣装。`first / second` はこの順序に依存。
- 2枚目からはデザイン・パレット・モチーフのみ取得。フラットレイの並べ方・チュール背景・小物は無視。

### 弱める順序（v6 で弾かれた場合）
1. 判定のランダム性があるため 1〜2 回の再試行（391-393 観察）。
2. デュベ/枕の位置を腰まで上げ、下の見え方をウエストラインだけへ。
3. 衣装参照の添付をやめ、本文の素材記述のみで試す（画像入力側のトリガー切り分け。387-390 の知見: 画像入力は通常服ならトリガーにならないが、下着写真自体は切り分け未検証）。
4. 文脈枠を `loungewear lookbook` から無地の `quiet morning portrait` へ。
5. Gemini / Nano Banana など緩やかなサービスで試す。

### 任意付加オプション: 高位文
README の体型保持三点対策のうち「胸の高さ」の文はトリガー表面積が大きいため本文から除外済み。ベースが通り、かつ生成で胸が下がって出る場合のみ、保持ブロックの布の挙動文の直後へ次を挿入する:

`the bust sits high and supported on the ribcage, as if wearing a well-fitted bra: its fullest point is level with the mid-upper arm, roughly at armpit height, with only a short distance between the collarbones and the top of the curve — never sagging low toward the waist`

### 体型保持
- 圧縮版保持ブロック（サイズ保持2文＋布の挙動文）で参照どおりのボリュームを維持（391-393 現行版と同型）。
- ポーズはどちらの案も胸の前を空け（両腕は胴の前を横切らない）、体に沿う衣装そのものでボリュームを読ませる。
