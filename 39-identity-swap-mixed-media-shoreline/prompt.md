# 39. 多素材の海辺・参照人物の厳密な差し替え

画像1を編集対象、画像2を人物ID参照として使用する。画像1の女性だけを画像2の成人女性へ置換し、人物シルエット外の海、空、太陽、砂浜、波打ち際、多素材の配置、色、光、画角を厳密に維持する。

- **アスペクト比:** 16:9 横長（画像1と同一）
- **編集対象:** 画像1の女性のみ
- **人物参照:** 画像2。見た目年齢、顔、髪、肌、体型、身体のライン、胸と腰まわりの自然な形とボリューム、身長感、プロポーションを保持
- **位置・ポーズ:** 画像1と同じ画面位置、サイズ、右向きの肩越し／横顔、視線方向、肩の高さ、クロップ
- **背景固定:** 画像1の人物シルエット外は変更しない
- **場面から除外:** 画像2の飲食店、窓、料理、皿、箸、グラス、テーブル、アクセサリー、昼光、ポーズ
- **馴染ませ方:** 画像1の高コントラストな白黒表現と夕日の縁取り光を人物へ適用し、多素材の侵食位置も画像1どおりに維持

## 生成画像

- `01-identity-swap-candidate.png`
- `02-identity-swap-candidate.png` — **推奨:** 人物のいない右側領域の元画像との差分が4候補中で最小
- `03-identity-swap-candidate.png` — 顔の同一性を強めた候補
- `04-identity-swap-candidate.png` — 顔・体型・元構図・肩の侵食位置のバランスを重視した候補

---

## 完成プロンプト

```text
Use case: identity-preserve compositing edit
Asset type: cinematic surrealist mixed-media artwork

Input roles:
- Image 1 is the EDIT TARGET and immutable base image.
- Image 2 is the IDENTITY AND PHYSIQUE REFERENCE for the replacement adult woman only.

Primary edit: Replace only the woman in Image 1 with the adult woman from Image 2. Keep the replacement woman in exactly the same screen position, scale, crop, body orientation, right-facing over-the-shoulder / side-profile pose, gaze direction, head angle, shoulder height, and silhouette footprint as the original woman in Image 1.

Identity preservation: Infer apparent age from Image 2 and preserve it. Match Image 2 exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in Image 2, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode features that are not present in Image 2 — no invented hair colors, accessories, uniforms, or props.

Reconstruct the same woman from Image 2 in a natural right-facing side profile consistent with her face, skull, jaw, nose, lips, eyes, cheeks, and hair as seen in Image 2. She must remain unmistakably the same adult person even though the camera angle changes. Preserve her natural physique and shoulder/chest proportions from Image 2 within the pose and crop of Image 1.

Scene adaptation: Apply Image 1's high-contrast monochrome treatment, deep charcoal shadows, grayscale skin rendering, and sunset rim light to the replacement woman. Keep the calm, accepting expression and relaxed posture of Image 1. Use a simple opaque dark garment that stays within the original woman's silhouette and follows the replacement woman's physique naturally. Preserve the small mixed-media invasion along the hair edge, cheek contour, and outer shoulder at the same locations, scale, colors, and materials as Image 1.

Immutable background: Outside the original woman’s exact silhouette region in Image 1, preserve the pixels and visual content as faithfully as possible. Do not redesign, repaint, regenerate, restyle, shift, crop, blur, simplify, or recolor any part of the sea, sky, sun, horizon, clouds, shoreline, foam, sand, neon accents, pixels, crystals, resin, liquid, cut paper, stained glass, oil paint, shadows, or mixed-media boundary. Keep every wave crest, material patch, color field, highlight, texture, and object at the same position and scale. Keep the original 16:9 framing and resolution.

Do not transfer scene content from Image 2: no restaurant, wooden interior, windows, daylight beach view, table, food, seafood, plates, bowls, glass, chopsticks, hand pose, jewelry, or dining clothing. Image 2 contributes only the woman's identity, facial structure, hair, skin, and physique.

Constraints: change only the woman; preserve Image 1 outside the woman; exactly one adult woman; maintain identity and physique from Image 2; maintain pose and composition from Image 1; no text, no logo, no watermark.

Avoid: blended identity between the two women; retaining the original woman's face or physique; generic substitute face; age shift; beautification; changed hair identity; altered body proportions; background drift; changed ocean textures; moved sun; changed horizon; new objects; restaurant elements; extra people; extra limbs; malformed hands.
```

---

## 設計メモ

- 画像1をベース、画像2を人物供給元に役割分離する。
- 人物以外を再生成対象として解釈させないため、人物シルエット外を不変領域として反復指定する。
- 画像2の正面寄りの顔から右向き横顔を再構成する一方、顔立ちの基準は画像2だけに限定する。
- 画像2の背景・小物・衣装・ポーズは持ち込まず、画像1のモノクロ照明と構図へ人物IDと体型だけを適合させる。
