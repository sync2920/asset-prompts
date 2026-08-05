# 41. 劇場アニメ舞踏会・画風と人物IDの二参照分離

第1画像を世界観・衣装言語・照明・色彩・描画様式・顔のアニメ化強度だけの参照、第2画像を人物ID・年齢・髪・瞳・体格だけの参照として使用する。第1画像のキャラクター固有要素を移さず、第2画像の成人女性がそのアニメ映画世界に元から存在するように描く。

- **アスペクト比:** 3:4 縦
- **構図:** 腰上、ほぼ正面、顔を上三分の一、手は腰前で低く重ねる
- **画風参照:** `reference-world-style.png`
- **人物参照:** `reference-identity.png`
- **成人判定:** 第2画像は明確に成人として読めるため、指定のオフショルダー衣装を採用
- **見せ場:** 第2画像由来の髪と瞳を保った純アニメ顔と、琥珀の逆光が作る肩・デコルテの輪郭
- **参照分離:** 第1画像の金髪の編み上げ、赤いリボン、青い瞳、顔立ちは移さない
- **除外:** 第1画像左下のUIアイコン、二人目、写真質感、文字・ロゴ・透かし

## 生成画像

- `01-nighttime-ball-anime.png` — 第1画像に近い静かな劇場キービジュアル構図
- `02-nighttime-ball-anime.png` — 純アニメの顔比率と繊細な線を強調
- `03-nighttime-ball-anime.png` — 髪の琥珀色リムライトと赤い薔薇の陰影を強調
- `04-nighttime-ball-anime.png` — 深いプラム紫のサテン反射と宝石色の点光を強調

---

## 完成プロンプト

```text
Use case: stylized-concept
Asset type: prestige theatrical anime key visual
Input image roles:
- Image 1 is the WORLD, COSTUME-LANGUAGE, LIGHTING, PALETTE, RENDERING-STYLE, and FACIAL-STYLIZATION reference only.
- Image 2 is the sole IDENTITY, APPEARANCE, HAIR, EYE-COLOR, AGE, and PHYSIQUE reference for the resulting adult woman.
- Do not reproduce the small camera/UI icon visible at the lower-left edge of Image 1; it is not part of the artwork.

A highly detailed anime-style portrait of the person from the SECOND attached image, redrawn as a woman of the world shown in the FIRST attached image. 3:4 vertical aspect ratio.

Reference roles: the FIRST attached image is the world and style reference — its opulent candlelit hall, its jewel-tone palette, its evening-gown costume language, its painterly cinematic anime rendering, AND the degree of facial stylization: the result's face is drawn as fully anime as the character in the first image. The character herself must not appear in the result: never borrow her face shape, her blonde braided updo, her hair ribbon or her blue eyes. The SECOND attached image is the identity reference — the woman in the result is this person, living natively in that world's art style.

Infer apparent age from the second image and preserve it. Match the second image exactly for gender presentation, body shape and lines, height impression, proportions, overall build, and all physical characteristics including chest and hip shape and fullness, kept accurate through the fit and drape of the gown. The bust sits high and supported on the ribcage, as if held by a well-fitted bodice: its fullest point is level with the mid-upper arm, roughly at armpit height, with only a short distance between the collarbones and the top of the curve — never sagging low toward the waist. Keep her hair entirely her own from the second image — same color, length, texture, parting and bangs, worn down in its natural fall, softly arranged for the evening — and keep her eye color from the second image. Preserve her physique faithfully without age-shifting, exaggerating, or reshaping. Never add features that are not present in the second image beyond the outfit and jewelry described below. Use this outfit only if the reference is unambiguously adult; otherwise switch to a modest high-neck gown in the same palette. No extra limbs, extra fingers, or malformed hands.

Face: Draw her face at the SAME degree of anime stylization as the character in the first image — a true anime face, not a realistic one. Large, luminous anime eyes with layered painted highlights and soft lashes, in her own eye color from the second image; a delicate nose simplified to a short line with a touch of shading; a small, softly drawn mouth; smooth painterly anime skin with simple blush and shading, carrying no photographic texture; anime facial proportions — larger eyes, smaller nose and mouth — exactly as the first image's art style draws them. Her identity reads through the hair, the eye color, the soft gentle expression and the figure, not through photorealistic facial detail. She should look like a native character of the first image's film who happens to have the second image's hair, coloring and presence.

Pose: Waist-up, facing the viewer almost straight on, in the hush between two pieces of music — she has just turned her face back toward the viewer, chin lowered a fraction, hands in sheer white lace gloves gently folded low in front of her waist so nothing crosses in front of the chest. Her gaze meets the camera quietly; her lips stay together in the smallest warmth, as if she has just recognized the person looking at her. Composed but alive, caught mid-moment rather than stiffly posed.

Outfit: An evening gown in the first image's fashion: a fitted off-the-shoulder bodice in near-black plum with short, softly gathered ruffle sleeves resting just below the shoulders, a straight neckline that frames the collarbones and décolleté, and a full deep-violet satin skirt that catches the warm light in its folds. A single deep-purple rose corsage sits at one side of the bodice. Jewelry in the same manner as the first image: an ornate gold necklace holding one emerald-green stone at the centre of the chest, with small matching drop earrings. Sheer white lace gloves to the wrist. No other accessories and no hair ribbon — her hair stays entirely her own.

Background: The world of the first image at night — a grand hall lit by candles and warm lamps, the air amber and hazy with soft bloom. Towering gilded baroque frames catch the glow on one side; dark red roses sink into shadow on the other; out-of-focus candle flames drift as warm bokeh behind her. The background stays softly blurred and painterly so she carries the frame. One palette: amber gold and deep plum-violet, with emerald, ruby and sapphire as small jewel accents. A warm rim of light from behind and above traces her hair and bare shoulders; a soft warm fill from the front keeps her face clean and readable.

Style: Render the ENTIRE image — the woman and above all her face included — in the first image's art style: cinematic Japanese anime key-visual quality, delicate linework, luminous glossy eyes, painterly soft bloom around every warm light, rich jewel-tone color grading, and fine painted detail in the gold filigree, the gemstones, the lace and the satin. One coherent anime style across the whole frame; no photographic texture anywhere.

Avoid: a semi-realistic, 3D-CG or hybrid face caught between photograph and anime; photographic skin texture or pores on the face; the first image's character or any second person in the frame; her blonde braided updo, red hair ribbon or blue eyes carried onto the subject; any change to the subject's own hair color, length or texture; no text, no logo, no watermark.

Format: 3:4 vertical portrait, waist-up, subject centred with her face in the upper third of the frame.
```

## バリエーション差分

1. `stay closest to Image 1's quiet, balanced theatrical key-visual framing and painterly anime face construction while obeying every identity separation rule.`
2. `emphasize the fully hand-drawn anime facial proportions and delicate linework, with restrained candle bokeh and the same centred waist-up composition.`
3. `emphasize amber back-rim light through the subject's own loose hair and velvety shadows among the dark red roses, without changing any identity feature.`
4. `emphasize deep plum-violet satin reflections and tiny emerald, ruby, and sapphire accents while keeping the face softly readable and wholly anime.`

---

## 設計メモ

- 第1画像は画風供給元、第2画像は人物供給元として役割を反復し、参照の混線を抑える。
- 顔の写実的な同一性よりも、第1画像と同程度のアニメ化を優先しつつ、第2画像由来の髪・瞳・穏やかな存在感・体格で人物を読む設計。
- 第1画像の小さなUIアイコンは作品要素ではないため、生成時に明示的に除外した。
- 4枚とも全画面が統一されたアニメ描画で、金髪の編み上げ・リボン・青い瞳・二人目・UIアイコンの混入なし。

---

## 目の改善 v2 — 日本の劇場アニメの虹彩構造

初稿は眼形そのものはアニメだったが、虹彩が小さく内部の明暗層とキャッチライトが弱いため、自然な目に近く見えた。v2 では顔全体を幼くせず、目元だけを次の構造へ更新した。

- 眼裂を縦約10〜12%、横約5〜6%だけ拡大し、成人らしいアーモンド形を維持
- 虹彩径を約22〜25%拡大し、眼裂高の約68〜70%を占める比率へ変更
- 虹彩を「上部35%の濃い影／中間40%の固有色／下部25%の明るい弧」の三層で描画
- 上まぶた線を下線の約3倍の太さにし、下線は細く途切れさせる
- 同一のろうそく光源による大小2点のキャッチライトを左右で整合
- 人物参照由来の茶〜ヘーゼル系の瞳色を保持し、第1画像の青い瞳は移さない
- 血管・生物的繊維・コンタクトレンズ状の輪・濡れた実写眼球・3Dガラス玉の質感は使わない

### 改善画像

- `01-nighttime-ball-anime-eyes-v2.png` — 元の穏やかな表情への忠実度を優先
- `02-nighttime-ball-anime-eyes-v2.png` — 4枚中もっとも明確なアニメ眼
- `03-nighttime-ball-anime-eyes-v2.png` — **推奨:** 目の存在感と成人らしい顔のバランスが最良
- `04-nighttime-ball-anime-eyes-v2.png` — アニメ強度と元表情の中間

### 既存画像へ適用する局所編集プロンプト

```text
Use case: precise-object-edit
Asset type: stronger Japanese theatrical anime eye redesign

Input roles:
- Image 1 is the immutable EDIT TARGET.
- Image 2 supplies only Japanese anime eye drawing grammar and cinematic rendering strength; never copy its blue color or character identity.
- Image 3 supplies the adult woman's own eye color and identity presence.

Edit only both eyes and their immediately adjacent lash lines and eyelid creases. Keep every other element of Image 1 unchanged: exact canvas, crop, head position, face outline, apparent adult age, brows, nose, mouth, expression, skin shading, hair, anatomy, pose, hands, gown, jewelry, lighting, background, and color grade.

This must be a clearly visible eye redesign, not a subtle retouch:
- Increase each eye opening approximately 10–12% vertically and 5–6% horizontally while retaining an elegant adult almond shape. Do not move the eyebrows or change the rest of the face.
- Increase each iris diameter approximately 22–25% relative to Image 1, so the iris occupies roughly 68–70% of the eye opening's height. Hide its upper fifth beneath the upper lid and let its lower rim nearly meet the lower lid.
- Preserve exactly the brown/hazel eye color from Image 3. Never blue.
- Use crisp hand-painted cel-animation construction, not smooth realistic gradients. Divide the iris into a darkest upper 35% beneath the lid, a rich identity-color middle 40%, and a luminous warm golden-brown lower crescent across the bottom 25%. Add a clean dark outer ring and crisp pupil.
- Place one sharp warm-white primary highlight high on the shared candle-facing side and one much smaller secondary highlight. Both eyes obey one light source. Add only one restrained glossy arc.
- Make the upper lash line about three times heavier than the thin broken lower line, with clean tapered corners and only two or three delicate outer lower lashes.
- Keep warm ivory sclera with simple cel shading; no biological fibers, veins, wet texture, contact-lens ring, glass-marble depth, or 3D-CG gloss.
- Align both pupils precisely toward the viewer. No cross-eye, wall-eye, mismatched iris size, asymmetric light direction, or duplicated pupils.
- The eyes carry quiet recognition and restrained warmth and immediately read as prestige Japanese theatrical anime. Adult and elegant, never chibi, childish, doll-like, or exaggeratedly round.

No other edits. Exactly one adult woman. No text, logo, watermark, UI icon, or second person.
```

---

## 髪の改善 v3 — 一本描きではなく「毛束・面・線の階層」

ユーザー選定の `02-nighttime-ball-anime-eyes-v2.png` を編集元として固定。v2 の目はそのまま残し、髪だけを日本の劇場アニメで一般的な設計へ整理した。

元画像は毛先から前髪まで同じ強さの極細線が多数走り、繊細ではあるものの「一本ずつ描き込んだ高精細AIイラスト」に寄っていた。v3 では、繊細さを線数ではなく次の階層で作る。

- 外周のシルエット線を最も強くする
- 大きな毛束どうしの重なり線を中程度にする
- 毛束内部の流れ線は、幅の広い束に0〜1本程度へ絞る
- 明暗は細い光沢線ではなく、連結したセル影と帯状ハイライトの面で描く
- 外周の後れ毛だけを少数残し、内部の平行細線・繊維描写・縮れ線の網を使わない
- 髪色、長さ、質感、分け目、前髪、輪郭、ボリュームは参照画像から保持し、髪型そのものは変えない
- v2 の両目は、眼形、虹彩径、色、三層の明暗、瞳孔、二点ハイライト、視線まで変更しない

### 改善画像

- `02-nighttime-ball-anime-eyes-v2-hair-v3-01-conservative.png` — 内部細線を約60〜65%削減。元の細かなウェーブを比較的多く残す
- `02-nighttime-ball-anime-eyes-v2-hair-v3-02-balanced.png` — **推奨:** 内部細線を約75%削減。毛束・セル影・帯状ハイライトの均衡が最も自然
- `02-nighttime-ball-anime-eyes-v2-hair-v3-03-cel.png` — 内部細線を約85%削減。完成セル／原画寄りの簡潔な毛束設計
- `02-nighttime-ball-anime-eyes-v2-hair-v3-04-painterly.png` — 約70〜75%削減。毛束設計を保ちつつ、光のにじみをやや多く残す

### 既存画像へ適用する局所編集プロンプト

```text
Use case: precise-object-edit
Asset type: prestige Japanese theatrical anime key visual, localized hair-rendering correction

Input image roles:
- Image 1 is the immutable edit target and composition source.
- Image 2 supplies only the Japanese theatrical-anime grammar for grouping hair into designed locks and painted shapes. Never copy its character identity, eye color, hairstyle, braid, ribbon, or hair color.
- Image 3 supplies the adult woman's identity and confirms her own hair color, length, texture, parting, bangs, natural volume, and silhouette.

Change only the drawing treatment inside the existing hair region of Image 1. The current hair contains too many thread-thin individual marks. Redraw the same hair as deliberately designed Japanese anime hair: coherent tapered locks, readable overlapping masses, restrained interior lines, connected cel-shadow shapes, and one broad ribbon-like highlight. This is only a simplification of mark-making, never a haircut or restyle.

Preserve the exact canvas, crop, composition, head position, face outline, apparent adult age, identity, expression, eyebrows, nose, mouth, skin, anatomy, pose, hands, physique, gown, corsage, jewelry, lighting, background, and color grade from Image 1.

Most importantly, preserve both eyes from Image 1 exactly: the same adult almond openings, iris diameter, identity-derived color, dark upper iris shade, luminous lower crescent, pupils, two-point highlights, lash lines, gaze direction, symmetry, and quiet warmth. Do not redraw, resize, recolor, soften, or move either eye.

Preserve the hair exactly as derived from the identity reference: same color, length, loose texture, parting, bangs arrangement, outer silhouette, volume around the face and shoulders, and warm rim light. Keep it fully down with no ribbon, braid, bun, clip, or invented accessory. Keep the forehead and eyebrows revealed to the same degree; no lock may newly cover an eye.

Construct the hair as a limited hierarchy of major shapes. Use 6–8 clean tapered bang clumps, 3–4 broad flowing locks on each side, and simple rear masses. Make the outer silhouette line strongest, overlap seams medium, and use no more than zero or one thin flow accent inside most locks. Reduce the visible internal line density by roughly 75%. Fill each lock primarily as a clean color plane, with one connected cel-shadow family and one broad, irregular warm highlight band crossing several locks. Allow only a few intentional flyaways on the outer contour.

The result must retain delicate feature-film polish through controlled line weight, graceful curves, color shapes, and light—not through rendering every strand.

Avoid: hair-by-hair engraving, fiber simulation, dense parallel micro-lines, cross-hatching, frizz webs, photographic hair texture, hair cards, 3D-CG strand gloss, excessive flyaways, plastic helmet hair, blunt wig shapes, any change outside the hair, a second person, text, logo, watermark, or UI icon.
```
