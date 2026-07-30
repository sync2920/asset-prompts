# 16. 植物園のカフェテラスでアイスコーヒーを一口飲んだ余韻（参照画像ベース）

`ideas/README.md` の人物参照方針に準拠し、人物の顔、髪、肌、体型、身長感、プロポーションなどの身体的特徴は添付画像から忠実に保持する。髪型だけは、参照由来の肩ウェーブボブ・シースルーバング・後れ毛を維持したまま、髪紐（細い生成りのコットン/リネンコード）でハーフアップにまとめる形へ変更する。`expression/02-summer-heat-realism.md` の「暑さは空気・小道具・素材で表現する」手法を使い、結露したグラスと木陰の斑光で午後の涼を伝える。

- **アスペクト比:** 4:5 縦長
- **見せ場:** ボリュームのあるハーフアップから垂れる生成りの紐、カメラへ向けた親密な笑顔、結露したアイスコーヒーのグラス、Vネックのデコルテ
- **髪型:** 耳線より上の髪全体を後ろで一つにまとめ、トップを軽くほぐして丸いボリュームを出す。細い生成りコードで結び両端を長く垂らす。下のウェーブ・前髪・後れ毛は参照のまま下ろし、上下の対比を明確に
- **構図:** 対面の席からの正面寄りPOV。被写体はカメラ（向かいの相手）をまっすぐ見て、会話中にこぼれる親密な笑顔
- **衣装:** 15踏襲。ペールミントのVネックリブニット × オフホワイトアイボリーのミニ。下には何も着用しない
- **文脈:** 植物園併設カフェテラスの午後 × 一口飲んだ余韻 × 結露と斑光の素材研究

---

## プロンプト

```text
A highly detailed photorealistic portrait of the person from the reference image. 4:5 vertical aspect ratio,
a seated cafe-terrace portrait including the subject, the iced coffee glass, and the greenery behind her.
Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender
presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and
texture, facial features, hair color and texture, and all physical characteristics including chest and hip
shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference,
kept accurate through the fit and drape of the clothing. The bust sits high and supported on the ribcage, as
if wearing a well-fitted bra: its fullest point is level with the mid-upper arm, roughly at armpit height,
with only a short distance between the collarbones and the top of the curve — never sagging low toward the
waist. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating,
or reshaping. Never add or hardcode physical features that are not present in the reference image.

  Hair: Keep the reference hairstyle's identity exactly — the same shoulder-length softly waved bob, the same
milky ash-brown tone, the same wispy see-through fringe across the brow, and the same loose face-framing
strands — but build a clear, generous half-up style from it. Gather the entire top half of the hair,
everything above the ear line (the crown, the sides above the ears, and the upper layers at the temples), back
into one full half-up bundle at the back of the head, leaving a visibly rounded, lifted volume on top rather
than a thin skim of strands. Lightly loosen the gathered crown so it puffs up with soft air and height, the
way a half-up is teased for volume. Fasten the bundle with a thin natural off-white cotton-and-linen cord,
knot it once, and let its two long ends hang freely down the back, past the shoulders, swaying slightly with
the loose waves beneath. The bottom half of the hair — from the ear line down — stays fully released and
waved as in the reference, falling around the shoulders so the contrast between the pulled-up top and the
loose bottom is obvious and reads unmistakably as a half-up. The fringe and the face-framing strands are
untouched. The cord reads as a soft handmade accent, not a stiff hair tie.

  Pose: The shot is taken from the seat directly across the small round cafe table, as if by the companion
sitting opposite her, so the subject faces the camera almost frontally with only a slight, natural tilt of the
shoulders. She is seated at the table on an outdoor terrace, leaning in just a touch toward the person across
from her, the easy closeness of someone comfortable in the company. She has just taken one sip of her iced
coffee and lowered the tall glass to about chest height, holding it upright in one hand with the fingers
wrapped gently around the cold, beaded surface. The straw stays in the glass but is lifted clear of her lips —
she is not drinking in this frame, the sip is already over. Her other arm rests relaxed, the forearm on the
table edge or the hand resting lightly on her lap. Her legs are settled comfortably in the chair, the skirt
draping naturally over the seated thighs.

  The subject looks straight at the companion across the table — that is, directly into the camera — and
breaks into a warm, unguarded smile, the kind that slips out mid-conversation when the person you like says
something nice. The smile is genuine and reaches the eyes, the corners crinkling softly; it feels intimate and
a little shy, a private "girlfriend across the table" moment rather than a posed photo smile. Her head tilts
slightly to one side, the loose fringe and the half-up cord ends framing the face. The full face reads clearly
and frontally: both eyes, the bridge of the nose, the smiling mouth. Candid, unposed, caught mid-moment.

  Outfit: A fully opaque, soft fine-knit V-neck top in a pale mint green with short sleeves, fitted naturally
without compression. The V opens to the mid-sternum, the fabric following the natural curve of the bust and
framing the décolletage with a clean, unadorned line. Pair it with a high-waisted A-line mini skirt in a warm
off-white ivory opaque woven fabric (a soft cream-tinged white, clearly distinct from any white in the
background), short enough that the hem rests at mid-thigh. While seated, the skirt draws gently taut across the
seated thighs, the woven fabric holding its shape and falling in a few soft folds at the hip. Nothing is worn
beneath the skirt. Simple low-profile walking shoes in a neutral tone. Keep the palette restrained and
daytime-appropriate.

  The clothing must follow the reference physique faithfully. Nothing is carried or crossed in front of the
chest except the single glass held to one side at chest height. The knit fabric curves naturally over the bust
and falls from its outermost point with gentle, physically plausible tension lines, preserving the reference
silhouette without exaggeration.

  Background: The outdoor terrace of a small cafe attached to a botanical garden, mid-afternoon. A round
wooden or pale-stone table and a simple chair sit in dappled shade beneath overhead trees. Behind the subject,
a soft wall of green hedge, potted plants, and a glimpse of the garden path recedes into a gentle blur.
Filtered sunlight falls through the leaves in irregular patches across the table, the subject's shoulder, and
the glass. On the table, beside the glass she holds, sits only a plain paper or cork coaster with a faint ring
of water; no other clutter. The iced coffee is in a tall clear glass: clear angular ice cubes, deep amber
coffee with a thin swirl of milk just beginning to marble through it, and fine condensation beading the outer
wall, a few drops gathering at the base. No text, no logo, no brand name anywhere in the frame. The terrace
feels quiet, shaded, and cool against the warm afternoon outside the tree line.

  Camera: 50mm lens at f/2.0, positioned at the seat directly across the table, facing the subject almost
frontally with only a slight off-axis angle, at roughly her seated eye-to-chest height — level with her, never
below the table line and never looking upward beneath the skirt. The framing reads as the companion's point of
view from the opposite chair. Frame the face and the half-up cord in the upper third and the beaded glass held
in her hand lower in the frame, so the warm gaze meeting the lens and the cold glass form the two anchors of
the composition. The subject is shown from the top of the head to just below the seated knees. The face, the
cord ends, the hand, and the glass share sufficient focus; the greenery behind falls into a soft natural blur.
Realistic daylight, natural skin texture, restrained highlights, and fine sensor grain.

  Avoid: low-angle or upward-looking framing, under-skirt visibility, exposed underwear, the straw touching or
entering the lips, an open or distorted drinking mouth, hidden face, extra limbs, extra fingers, or malformed
hands, and any text or logo on the glass or surroundings.

  Format: 4:5 portrait orientation, vertical composition.
```

---

## 設計メモ

### 髪型の設計（A: ハーフアップ＋垂らし紐、ボリューム強化版）

- 参照由来の肩ウェーブボブ・ミルクティーアッシュ・シースルーバング・後れ毛はすべて維持する。
- まとめる範囲を「耳上〜こめかみの薄め」から「耳線より上の髪全体」へ拡大し、トップを軽くほぐして丸く持ち上げる。薄い一束ではなく、上にふくらみのある塊としてハーフアップ感を明確化する。
- 下半分（耳線より下）は完全に下ろしたまま残し、引き上げた上と下ろした下の対比をはっきりさせることで「 unmistakably half-up」にする。
- 紐は細い生成りのコットン/リネンコード。一度結んで両端を長く垂らし、下のウェーブに沿わせて揺らす。オフホワイトのスカートとトーンを揃え、ミントとも喧嘩しない。

### 対面POVと彼女感の笑顔

- カメラを「向かいの席の相手の視点」に固定し、被写体をほぼ正面から捉える。three-quarterの横顔設計から正面寄りへ転換。
- 視線はカメラ（＝向かいの相手）へまっすぐ。会話中にこぼれる、目まで笑う親密で少し照れた笑顔。ポーズ指定の笑顔ではなく内心ベースの演技記述で具体化。
- 頭を片側に少し傾け、前髪と垂らし紐で顔をフレーム。正面顔（両目・鼻筋・笑う口）がはっきり読める。

### アイスコーヒーの破綻対策

- 「一口飲んだ直後」に固定し、ストローはグラスに差さったまま唇から離す。咥えたままの口元破綻を避ける。
- グラスは垂直に保持、片手だけ。もう片方の手はテーブルか膝に置き、役割を分ける。
- 結露・角氷・ミルクのマーブル・コースターの水の輪を具体で指定し、涼を肌の汗ではなく小道具で出す（`expression/02`）。

### 衣装と際どさの継続

- 15のペールミントVネック×オフホワイトミニを踏襲。座り姿勢なのでスカートの挙動は「太ももに沿って張る＋腰で数本の折り目」程度に留め、15のようなヘムの持ち上がりは強調しない。
- 下には何も着用しない設定を継続。ローアングルとunder-skirtをAvoidで明示。

### 既存案との差

- `15` は植物園の小道で野草を見つめる深いしゃがみ、花を受け止める手が主役。
- `14` はベランダの朝顔、指先と横顔を同一水平線に置く近距離構図。
- `16` は植物園カフェテラスの座り姿勢、結露したグラスとハーフアップの垂らし紐が主役。しゃがみ・花受け・霧・風鈴は使用しない。
