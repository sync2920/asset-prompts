# 38. 窓辺の読書、名前を呼ばれて見上げる眼鏡姿（参照画像ベース）

`ideas/README.md` の人物参照方針に準拠し、人物の年齢、性別表現、顔、髪、肌、体型、胸と腰まわりの形と自然なボリューム、身長感、プロポーションなどを参照画像から精緻に保持する。静かな窓辺のテーブルで文庫本を読んでいる途中、友人に名前を呼ばれて顔を上げた自然な一瞬。参照人物の顔立ちを眼鏡店のフィッティングと同じ観点で読み、本人が日常的に選びそうな眼鏡を一組だけ加える。

- **アスペクト比:** 3:4 縦、上半身
- **見せ場:** 参照人物に合わせて選ばれた眼鏡と、透明レンズ越しに明瞭に見える目。読書から会話へ意識が切り替わる一瞬
- **構図:** 静かな窓辺のテーブル。開いた文庫本は卓上に置き、胸の前を空ける。座った目線の高さから会話距離で撮る
- **服装:** 柔らかなニュートラルカラーの完全不透明な細番手クルーネックニット。ロゴ、ジュエリー、眼鏡以外のアクセサリーなし
- **光:** 大きな窓からの柔らかな昼光を顔へ均一に回し、目とフレームを同時に明瞭にする
- **バリエーション:** 人物・場面・服装は共通。視点、顔を上げる瞬間、窓光の方向、眼鏡の似合わせ判断だけを自然に変える

---

## プロンプト

```text
Use case: photorealistic-natural
Input image: Image 1 is the sole identity and physique reference for the person. Generate a new scene; do not copy its outfit, accessories, props, food, or seaside setting.

A highly detailed photorealistic portrait of the person from the reference image.
3:4 aspect ratio. Infer apparent age from the reference image and preserve it.
Match the reference image exactly for gender presentation, ancestry, body shape and
lines, height impression, proportions, overall build, skin tone and texture, facial
features, hair, and all physical characteristics including chest and hip shape and
fullness. Reproduce the natural volume and silhouette of the bust and hips as seen
in the reference, kept accurate through the fit and drape of the clothing. The bust
sits high and supported on the ribcage, as if wearing a well-fitted bra: its fullest
point is level with the mid-upper arm, roughly at armpit height, with only a short
distance between the collarbones and the top of the curve — never sagging low toward
the waist. Preserve the subject's identity and physique faithfully without
age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode features
that are not present in the reference image — no invented hair colors, accessories,
uniforms, or props — with exactly one exception: the glasses specified below.

Glasses: Before drawing, study the reference person's face the way a skilled
optician would — face shape and width, brow line, eye spacing, nose bridge height,
skin undertone, hair color and style, and overall vibe — then choose exactly one
pair of glasses that flatters this specific person. Select the frame shape to
balance the face: angular or rectangular frames add definition to a soft round
face, rounded or oval frames soften a strong jawline, deeper frames balance a long
face, and an oval face suits almost any shape, so there decide by the person's
vibe instead. Match the frame width to the face width and let the top line of the
frame follow the natural brow line. Harmonize color and material with skin and
hair — warm undertones with gold, tortoiseshell or warm brown acetate, cool
undertones with silver, black or cool gray, frame thickness matched to the
strength of the features. These examples are loose inspiration only, not a fixed
menu — invent freely beyond them, and never default to the same plain black
rectangular frame for every person. Clear lenses only, no tint and no sunglasses:
the eyes, brows and natural expression stay fully visible and unchanged, with no
magnification or minification warping the face behind the lenses. The glasses sit
level on the nose bridge, temples running straight back to rest over the ears,
with a faint natural contact shadow on the skin and at most a subtle realistic
lens reflection that never hides the eyes. They must read as a pair this person
chose for themselves and wears every day, never a costume prop.

Pose: A candid upper-body moment at a quiet window-side table — paused while
reading a paperback, looking up toward the camera as if a friend has just called
their name, relaxed and unposed. The open paperback rests naturally on the tabletop
below the frame's chest line, with one hand lightly near the page; nothing is held
or crosses in front of the chest.

Outfit: A simple, fully opaque fine-gauge knit in a soft neutral tone that follows
the body naturally, with a modest crew neckline; no logos, no jewelry, no other
accessories — the glasses are the only accent.

Background: A calm, lived-in cafe or home interior by a large window in soft
daylight; gentle out-of-focus warmth behind, no other people, the light falling
softly and evenly across the face so the frames and eyes both read clearly.

Camera and realism: conversational seated eye level, natural perspective, realistic
skin texture and fine fabric texture, subtle sensor grain, restrained highlights,
no beauty filter and no HDR glow.

Avoid: extra limbs, extra fingers, malformed hands, duplicate or asymmetrical
glasses, tinted or opaque lenses, hidden eyes, warped facial features behind the
lenses, readable book text, logos, and watermarks.

Format: 3:4, vertical composition, upper-body portrait.
```

---

## 設計メモ

- 参照画像は人物のアイデンティティと身体特徴だけに使い、元画像の白い衣装、食事、海辺の店内、箸、グラス、ブレスレットは引き継がない。
- 眼鏡は参照にない唯一の例外。形・幅・ブリッジ・色・素材を固定せず、各生成で参照人物に対する似合わせ判断を行わせる。
- 本を卓上の胸線より下へ置いて、身体の前を遮らない。片手だけをページ付近に置き、読書中の自然さを残しつつ手指の破綻リスクを抑える。
- 既存 `16` は植物園カフェでアイスコーヒーと笑顔、`22` は朝のソファで寝ぼけながら読む場面。本案は、窓辺で名前を呼ばれて意識が切り替わる瞬間と、人物ごとに選ぶ眼鏡を主題にする。
