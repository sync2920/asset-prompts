# 46. 夏の海辺・風に揺れるリネンドレス（劇場アニメ）

`41-nighttime-ball-anime/02-nighttime-ball-anime-eyes-v2-hair-v3-02-balanced.png` を、人物ID・目・髪・体格・アニメ描画だけの参照として使用。舞踏会の衣装と背景は移さず、夏の海辺へ場面を全面的に差し替えた。

- **参照画像:** `reference-anime-identity.png`
- **成人判定:** 明確に成人として読める
- **比率:** 3:4 縦
- **構図:** 膝上、海岸を歩く途中、顔を上三分の一
- **衣装:** 淡いシーグラスブルーの不透明なリネン混ノースリーブ・ミディドレス
- **見せ場:** 海風がスカートと大きな毛束だけを動かす一瞬
- **髪の方針:** 一本描きへ戻さず、毛束・重なり線・セル影・帯状ハイライトで構成
- **除外:** 舞踏会のドレス、宝飾、手袋、薔薇、夜景、水着、二人目、文字

## 生成画像

- `01-clear-morning.png` — 正面寄りの朝光。元参照の穏やかな顔への近さを優先
- `02-cinematic-shoreline.png` — 海岸線の奥行きと横風を強調
- `03-clean-cel.png` — **推奨:** 目の存在感と、細線を抑えた毛束・セル作画の均衡が最良
- `04-airy-late-morning.png` — 少し近い構図と、雲越しの柔らかな光

---

## 完成プロンプト

```text
Use case: stylized-concept
Asset type: prestige Japanese theatrical anime summer key visual

Input image role:
- Image 1 is the sole reference for the adult woman's identity, apparent age, gender presentation, ancestry, face, eye construction and eye color, body shape, proportions, physique, skin tone, hair, and balanced hand-drawn anime rendering language.
- Do not carry over Image 1's ballroom gown, gloves, rose corsage, necklace, earrings, baroque hall, candles, or nighttime palette. Those belong only to the old scene.

Primary request: Place this same adult woman at a quiet summer seaside in a genuinely cool, breathable daytime outfit, rendered as a coherent frame from a prestige Japanese animated feature. 3:4 vertical portrait.

Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. The bust sits high and supported on the ribcage, as if held by a well-fitted bodice: its fullest point is level with the mid-upper arm, roughly at armpit height, with only a short distance between the collarbones and the top of the curve—never sagging low toward the waist. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode physical features that are not present in the reference image beyond the outfit and seaside environment described below.

Face and eyes: Preserve the exact adult anime face and distinctive eye design from Image 1: the same elegant eye openings, iris size, identity-derived eye color, upper and lower iris value structure, crisp pupils, coordinated highlights, lash-line weight, gaze alignment, and quiet warmth. Keep the face adult and recognizable, never chibi or childlike.

Hair: Keep her own hair exactly from Image 1—same color, length, texture, parting, bangs, volume, and silhouette. Let the sea breeze move the existing locks naturally without changing the cut. Preserve the balanced Japanese-anime hair construction: a limited hierarchy of coherent tapered lock groups, clean outer silhouette, medium overlap seams, sparse interior flow accents, connected cel-shadow shapes, and one broad highlight band. Do not return to drawing hundreds of individual strands. No ribbon, braid, bun, clip, hat, or invented hair accessory.

Pose and composition: Knee-up vertical framing, the woman occupying the centre with her face in the upper third. She is walking slowly along the edge of the surf, caught naturally between steps, torso turned slightly toward the viewer and gaze meeting the camera. Her shoulders are relaxed; both arms hang or swing naturally low at her sides, and nothing crosses in front of the chest. The moment feels candid and alive rather than posed. Hands are anatomically correct, with no extra limbs, extra fingers, or malformed hands.

Outfit: A cool summer dress made from breathable, fully opaque linen-cotton in a pale sea-glass blue. Broad shoulder straps, a softly squared neckline, and a gently shaped, supportive bodice; a clean waist seam and a light A-line midi skirt that catches the sea breeze in broad folds. The bodice follows the body accurately and the skirt drapes from the natural outer lines without compressing or reshaping her physique. Bare lower legs; simple flat pale sandals only if visible. No transparency, no swimsuit, no cover-up, no jewelry, no gloves, no bag, and no other accessories. The only visual focus of the outfit is the wind moving the light skirt.

Scene and atmosphere: A quiet summer coast with clear turquoise-blue water, pale sand, a thin line of white foam, bright sky, and a few soft white clouds. A fresh onshore breeze gives the air a cooling clarity. Show summer through moving air, sunlit water, softened linen folds, and sea spray—not through excessive sweat. Exactly one woman; no other people, boats, buildings, signs, or clutter.

Style: Carry the same coherent Japanese theatrical-anime quality across the entire image: delicate but controlled linework, luminous layered eyes, smooth cel-shaped facial shading, painterly ocean and sky, clean color separation, subtle atmospheric bloom, and cinematic depth. Use a daylight palette of sea-glass blue, turquoise, white foam, pale sand, and a small amount of warm sunlight. Hair delicacy comes from designed locks and line hierarchy, not individual-strand engraving. No photographic skin or hair texture and no 3D-CG finish.

Avoid: any change to identity, apparent age, eye color or eye construction, hair color, length, texture, parting, bangs, body shape, or proportions; individual-hair fiber rendering, dense parallel hair micro-lines, frizz webs, ballroom clothing or jewelry, swimsuit styling, a second person, text, logo, watermark, or UI icon.

Format: 3:4 vertical, knee-up portrait, subject centred, face in the upper third, seaside clearly readable behind and around her.
```

## バリエーション差分

1. `Balanced clear morning: gentle front three-quarter angle; a small receding wave; soft 8 a.m. edge light and clean blue-sky fill.`
2. `Most cinematic: she has just turned her face back while continuing parallel to the shoreline; one broad diagonal skirt curve and a long turquoise reflection on wet sand.`
3. `Clean cel-animation clarity: nearly front-facing, pausing for half a step; the cleanest two-tone hair and dress construction, minimal interior lines, high clear horizon, restrained bloom.`
4. `Airy late-morning key visual: slightly closer framing; a white cloud softens direct sun; cool luminous facial fill and only a few separated outer hair locks.`

## 設計メモ

- `02-balanced` の画風を昼光へ翻訳し、琥珀・深紫からシアン・白・淡青へ配色を切り替えた。
- 「涼しい格好」は水着ではなく、風と素材の挙動が読める不透明なリネン混ドレスとして具体化した。
- 夏らしさは汗ではなく、海風、白い泡、水面反射、柔らかくなったリネンの折れで表現した。
- 髪は風で動かしても、外周の少数毛束と大きな面を優先し、一本ずつの繊維描写へ戻さない。

---

## 画風調整 v2 — 少女漫画の記号を抑えた現代キャラクターアニメ

ユーザーの「京アニ方面が好み」という方向性を、特定スタジオの画風名を生成指示へ直接入れず、次の一般的な描画要素へ分解した。

- 目の縦幅を約10〜15%、虹彩径を約8〜12%抑え、横長寄りの成人眼へ
- 虹彩の光を主反射1つ＋小さな補助1つへ整理し、多数のきらめきを使わない
- 黒いまつ毛の塊をやめ、肌・髪・服ごとの色付き輪郭線を使う
- 尖りすぎたV字顎を線の置き方だけで穏やかにし、幼児化はしない
- 髪は8〜12個の大きな毛束、3〜5本の外周後れ毛、二値中心のセル影で構成
- 完璧な左右対称のポスター立ちから、歩行中の肩差と視線の戻りを感じる日常芝居へ
- ロマンチックな光彩、唇の艶、装飾的なカール、過剰なブルームを弱める
- 海と雲は写真的にせず、距離・空気・反射を観察した緻密なアニメ背景として描く

### 改善画像

- `03-style-v2-01-gentle.png` — 目を約10%縮小した穏やかな移行版。元画像への近さを優先
- `03-style-v2-02-everyday.png` — **推奨:** 目・顎・毛束・日常芝居・背景密度の均衡が最良
- `03-style-v2-03-clean-tv.png` — 目と光を最も絞り、二値セル影を強めたテレビアニメ寄り
- `03-style-v2-04-film-natural.png` — 目は抑えつつ、海の反射色と背景描写を少し豊かにした映画寄り

### 既存画像へ適用する画風編集プロンプト

```text
Use case: style-transfer
Asset type: modern Japanese character-animation summer key visual, localized whole-frame style correction

Input image roles:
- Image 1 is the edit target. Preserve its exact 3:4 canvas, seaside location, framing, adult woman, pale-blue summer dress, body proportions, pose, shoreline geometry, sky, ocean, and overall palette.
- Image 2 supplies only the same adult woman's identity, apparent age, physical characteristics, eye color, hair color, hair length, hair texture, parting, bangs, and physique. Do not copy its ballroom clothing, jewelry, lighting, background, or romantic glamour rendering.
- Do not imitate or name any particular studio, franchise, film, or artist. Translate the direction into the original visual grammar described below.

Restyle Image 1 away from romantic shoujo-manga glamour and toward restrained, high-end modern Japanese character animation: observational everyday acting, compact natural facial construction, moderately sized expressive eyes, clean colored linework, economical cel shading, designed hair clumps, physically coherent daylight, and a richly observed but non-photographic seaside background.

Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode physical features that are not present in the reference images. Keep her unmistakably adult.

Face and eyes:
- Keep the woman's identity and gaze, but reduce each eye opening vertically by approximately 12% while preserving most of its horizontal width, giving the eyes a calmer, wider-than-tall adult shape.
- Reduce iris diameter approximately 10%; each iris occupies about 58–62% of the eye-opening height rather than dominating it. Preserve the identity-derived eye color.
- Use a clear pupil, a single dark upper iris shade, one restrained midtone, and a small lighter lower area. Keep one coherent primary reflection plus one tiny secondary point per eye. No constellations of sparkles, flower or star highlights, wet glass-marble depth, or contact-lens rings.
- Draw the upper eyelid in soft dark-brown or muted charcoal colored linework, only about twice the weight of the broken lower line. Shorten and reduce the outer lashes by about one third; no black wedge eyeliner and no fan of decorative lashes.
- Keep the brows readable and close enough to the eyes to carry subtle acting. Simplify the nose and mouth; remove glossy lipstick shine. Lips remain together in a tiny, unperformed warmth.
- Preserve the face structure, but remove any excessively sharp V-shaped manga taper: let the chin read as softly compact and naturally rounded through line placement, without changing identity or apparent age. No baby face.

Everyday acting: The woman is still caught mid-step on the beach, but the performance is observational rather than posed. One shoulder is naturally a little ahead of the other, the head has only a slight practical turn, and her eyes have just returned to the viewer as if she heard someone nearby. Avoid perfect fashion-poster symmetry, coy head tilts, glamour posing, or an invitation-like expression. Nothing crosses the chest. Keep hands anatomically correct.

Hair: Preserve the exact identity-derived color, length, texture, parting, bangs, and overall silhouette. Organize it into 9–11 readable major clumps with colored contours, medium overlap seams, broad two-tone shapes, and only a few interior flow accents. The sea breeze moves whole locks, not individual fibers. Keep only 3–5 intentional outer flyaways around the whole head. Use one quiet broken highlight band; no silky ribbon curls, dense strand engraving, frizz web, or ornamental halo of floating hairs.

Line, color, and shading:
- Use clean hand-drawn colored contours rather than uniformly heavy black lines: warm muted brown on skin, a cool identity-compatible neutral on hair, desaturated blue on the dress, and blue-green on distant water.
- Use two main cel values plus a small selective third accent where form needs it. Face shading is shape-based and restrained, with no airbrushed beauty gradient.
- Reduce romantic bloom, lens-like glow, glitter, and sparkling bokeh. Let clarity, local color, reflected sky light, and small changes in shadow temperature create richness.
- Keep the ocean and clouds painterly and carefully observed, with atmospheric perspective and believable scale, but never photographic texture. The background feels like a meticulously painted animation background supporting an everyday moment.
- Preserve the existing cool summer palette. Keep sunlight physically coherent and the face clearly readable.

Keep the same opaque linen-cotton sleeveless dress, broad straps, square neckline, fitted supportive bodice, waist seam, and moving A-line skirt. Preserve its fit and the woman's natural physique exactly. Keep the same empty summer shore, water, foam, sand, and clouds. No jewelry, hat, bag, swimsuit, new props, or second person.

Avoid the observed shoujo markers: vertically oversized eyes, huge irises, dense black lashes, multiple decorative highlights, pointed V-jaw, glossy lips, ornamental curls, floating hair filaments, fashion-poster symmetry, romantic haze, glitter overlays, photographic texture, 3D-CG rendering, text, logo, watermark, or UI icon.

Format: 3:4 vertical. Exactly one clearly adult woman. Preserve the scene and outfit while changing the character-animation grammar across the whole frame.
```
