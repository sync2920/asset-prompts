# 178派生 — 雨の中の光るドレス（開発ログと最終プロンプト）

178「雨が見せる透明ドレス」から派生して検討した型。2026-07-27時点で一旦保留。

## コンセプトの到達点

- エロではなく「エロいように見えてエロじゃないかもしれない」曖昧さが核。
- 見る人によって「肌？」「光？」「ガラス？」と解釈が割れることで、リプ欄の考察が伸びるバズ構造を狙う。
- 最終形: **一枚の地続きのドレスが、上から下へ光のグラデーションを持ち、光が強まるほど透明感も増す**（光と物質のトレードを一本の法則に束ねる）。

## 試行錯誤で分かったこと（重要）

1. **条件付きの光学表現は一発生成では無理。** 「雨粒がかかった箇所だけ透ける」「レンズの水滴越しにだけ透けて見える」等の条件連動は、毎回破綻する（斑点柄になる、スカート全体が別素材化する、滴がスノードーム化して中に人物が入る）。
2. **モデルは服を意味単位（上身頃/スカート）で分割認識する。** ウエスト縫い目で光が分断されるのはこのため。対策は「服全体を一枚の連続した布として扱い、縫い目は光に影響しないただのステッチ」と服の定義段階で宣言すること。
3. **「光の中の淡い影」を明示的に描かせると濃い塊になって失敗する。** 布の襞が光を透かす自然な濃淡だけで曖昧さは十分成立するので、影は指示しない。
4. **変化軸は一つに絞る。** 透明度と発光を別パラメータにせず「光るほど透ける」の一本にすると分断・斑点が減る。
5. **素材は抽象値より実在の布名で指定する。**「密な絹 → 光るオーガンザ → 光の薄衣」のように。
6. **否定形はモデルに無視されやすい。** 破綻対策は否定の追加より、肯定形の描写（"clinging to the glass" 等）を増やす方が効く。
7. 全画面の魚眼レンズは安っぽくなるので不採用。レンズ付着の雨粒はボケた脇役に留めるのが良い。

## 安全設計（維持すること）

- 実在人物の参照写真を使う前提のため、**参照以上の肌の露出は絶対に増やさない**。透けた先は常に「形のない暖色の光」のみで、脚・身体の輪郭・解剖学的ディテールは描かせない。
- 成人と明確に判断できる場合のみこのコンセプトを使用。不明な場合は完全不透明にフォールバック。

## 最終プロンプト（案B: 一枚のドレス・光と透明の連動グラデーション）

```text
Create a photorealistic vertical portrait using the uploaded reference image as the sole source for the subject. Faithfully preserve apparent age, gender presentation, ancestry, exact facial identity and proportions, natural skin, hairstyle and color, body shape and lines, height impression, and visible accessories. The subject wears exactly and only the reference outfit, rendered as one single continuous dress — treat the entire outfit as one uninterrupted piece of cloth from neckline to hem, with any waistline or seam being mere stitching that has no effect on light or material. Same colors, patterns, and fit as the reference, no added layers. Do not beautify, age-shift, reshape, or replace the person. Exactly one person. Use this concept only if the reference clearly depicts an adult; if adulthood is unclear, keep the outfit fully opaque.

Scene: heavy, luminous blue-hour rain on a dark open plaza, one low warm amber light source hidden far behind the subject, a few soft water droplets on the camera lens near the frame edges. The subject stands calmly a few meters away, rain streaking down around them.

The single impossible rule — one law binding light and matter: along this one continuous dress, from top to bottom, the fabric gradually trades substance for light. The more the cloth glows, the more translucent it becomes, as one inseparable property. At the neckline and chest the fabric is fully ordinary: opaque, dry-looking, unlit. Descending the dress in one perfectly smooth, uninterrupted gradient, the cloth takes on a growing soft warm inner radiance, and in exact proportion its body thins toward translucency — first like dense silk warming with light, then like glowing organza, until at the hem the fabric is at its brightest and most transparent, a luminous veil barely holding its form, its lowest edge almost breathing into the rain. The garment's drape, folds, and flowing silhouette remain readable at every stage. Through the translucent lower stages the viewer sees only formless warm radiance: no legs, no body contour, no anatomical detail, no silhouette — impossible to resolve as light, thin glass, or a warmer presence. No bands, steps, spots, patches, or shadow shapes; the only tonal variation comes from the fabric's own folds doubling the light.

Atmosphere and finish: cool blue rain light against the hidden warm source, raindrops flaring as they pass close to the glowing fabric, a long soft reflection of the radiant hem in the wet ground, faint mist at ankle level. Full body visible with air below the hem. Format: 9:16 vertical. No visible light source or sun disc, no separately lit garment sections, no visible skin through fabric, no clear silhouette of legs or body, no wet clinging clothing, no nudity, no second person, text, logo, watermark, extra limbs, or malformed hands.
```

## 代替案A（ウエスト分断を演出として受け入れる版・差し替え段落）

第3段落をこれに差し替えると、光が裾から立ち上りウエストで滲んで消える設計になる。分断が「破綻」ではなく「光が尽きていく演出」として読まれる。

```text
The single impossible rule — a dress that glows in the rain: the skirt carries one single continuous inner light, as if a soft warm radiance lives in the hem and breathes upward through the cloth. The glow is brightest at the lowest edge of the skirt and rises smoothly up the garment. Near the waist it does not stop at the seam: it bleeds gently about ten centimeters past the waistline into the lower edge of the bodice, thinning like light soaking upward into dry cloth, and only then fades out completely. Above this soft dissolve, the chest and neckline are ordinary, opaque, dry-looking fabric. The transition must look like light gradually running out of reach — never like two differently lit garments meeting at a line. No bands, steps, spots, patches, or shadow shapes inside the light; the only variation comes from the fabric's real drape and folds showing as soft tonal ripples.
```

## 調整ノブ

- 裾をもっと消したい: "barely holding its form" → "dissolving into the rain"
- 溶けすぎて足元が崩れる: "at its brightest and most transparent" → "nearly transparent"
- 上下分断が再発する: 冒頭の "one uninterrupted piece of cloth" を強調、または案Aへ切り替え
- 肌寄り/光寄りの解釈バランス: 発光色の記述を "candlelit skin-warmth"（肌寄り）↔ "warm golden lamplight"（光寄り）で振る

## 完全版（粒越しだけ透ける）をやりたくなったら

一発生成では不可能。2段階ワークフローで行う:
1. 透け要素ゼロの「レンズ雨粒越しポートレート」をベース生成（安定して出る）
2. 領域指定編集（Nano Banana系 / 生成塗りつぶし）で、水滴と重なる部分だけ透け＋発光を加える
