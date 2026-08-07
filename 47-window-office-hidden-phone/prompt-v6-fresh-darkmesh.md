# 47 v6 — 元参照から独立再生成・胸部比率固定・黒メッシュ低ノイズ

生成済みの v5 / v6 画像は入力に使わず、毎回4枚の参照画像から独立して初期生成する。
`generated-v4-01-balanced-office.png` は画風や人物を引き継ぐ画像ではなく、承認済みのブラウス越しの胸部シルエットを測る補助参照にだけ使う。

## 入力画像の順番

1. `reference-face-dark-lowlights.png` — 顔の印象、髪型、髪色、黒いメッシュ状ローライトのみ
2. `../main/_profile/ChatGPT Image 2026年8月4日 15_41_32.png` — 成人年齢、肌、体型、身体寸法、胸・腰まわりの形とボリュームのみ
3. `generated-v4-01-balanced-office.png` — 承認済みの胸部サイズとブラウス越しのシルエットを測る補助参照のみ
4. `reference-desk-layout.png` — 窓・机・モニターの配置のみ

## 共通プロンプト

```text
Use case: photorealistic-natural
Asset type: fresh first-generation reference-guided Japanese office lifestyle photograph

Create a brand-new photograph directly from the four source references. Never edit, reuse, continue, denoise, sharpen, or transform any previously generated v5 or v6 image.

REFERENCE AUTHORITY — do not blend these roles:
1. Image 1 alone controls this clearly adult woman's facial identity, facial impression, bangs, part, shoulder-length hairstyle, overall hair color, and the naturally dark woven lowlights.
2. Image 2 controls apparent adult age, skin, full body proportions, physique, and natural chest and hip fullness. Do not copy its restaurant, clothing, pose, or food.
3. Image 3 is a hard size-calibration reference only. Match its approved office-blouse upper-torso silhouette exactly: the same apparent bust width relative to the head, the same forward fullness and projection, the same outer contour, and the same centered V-neck presentation. Do not copy its face, hair rendering, noise, hands, lighting, or office.
4. Image 4 controls only the perpendicular window-and-desk geometry: window wall | desk extending inward at 90 degrees.

HARD ACCEPTANCE PRIORITIES:
A. The face must immediately read as the same adult woman as Image 1, with its gentle natural facial impression. Change only head and eye direction so she looks at the monitor. Give her a warm, softly amused closed-mouth smile. Never look at the camera or phone.
B. Do not reduce, flatten, compress, hide, or resize the approved upper torso from Image 3. Keep Image 3's head-to-bust width ratio, visible side contours, forward fullness, and blouse volume. The fully opaque blouse follows and drapes from this natural volume without becoming boxy or tight. A centered non-wrap V-neck shows only a small, tasteful natural center opening; it is not deep or revealing. Never enlarge beyond Image 3.
C. Hair must be rendered as clean broad lock-scale shapes, not thousands of fibers. Reproduce Image 1's dark mesh effect as softly blended dark color panels and dimensional ribbons inside the roots, inner layers, and selected large locks. These are broad lowlight sections within the hair mass—not thin black strand lines, outlines, zebra stripes, or ink strokes. Use smooth tonal gradients, rounded ends, clean antialiased contours, and very few flyaways. Preserve detail inside broad coherent locks while suppressing scratchy microstrands and high-frequency texture.

Identity and physique fidelity:
Match the references exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in Image 2, while matching the approved office-blouse presentation shown in Image 3. Keep this accurate through the fit and drape of clothing. Preserve the subject faithfully without age-shifting, beautifying, slimming, exaggerating, or reshaping. Never add or hardcode physical features absent from the references.

Scene:
A real contemporary Japanese open-plan office beside large windows. A pale-wood peninsula desk extends inward at a strict right angle from the window wall, never parallel. A large monitor is directly ahead near the window-side end. Naturally place a keyboard, mouse, open notebook, pen, restrained pen cup, sticky notes, and document tray. A few coworkers and desks are softly blurred in the background.

Pose:
Seat her upright at the office-side end facing the monitor. One hand operates the mouse. The other holds one smartphone low beside her thigh, fully below the desktop and partly hidden by the desk edge. The phone screen is dim and blank. Keep both arms away from the front of the torso.

Wardrobe:
Fully opaque pale powder-blue long-sleeved office blouse, centered non-wrap V-neck, soft fluid weave, discreet shaping darts, and dark navy or charcoal high-waisted tailored trousers. Preserve the calibrated Image 3 silhouette through the blouse. No wrap front, crossover, camisole, jacket, scarf, or chest-obscuring accessories.

Optical quality:
Clean low-ISO professional documentary photography, quality 50mm lens at f/2.8, smooth continuous tones, gentle optical sharpness, restrained local contrast, natural skin, and soft depth transition. The face, mouse hand, and phone hand are readable without aggressive micro-detail.

Strictly exclude grain, luminance noise, chroma speckling, HDR, clarity effect, oversharpening, edge enhancement, ringing, halos, crunchy texture, scratch-like hair, sawtooth contours, wiry strands, repeated zigzag curls, synthetic pore detail, extra fingers or limbs, malformed hands, duplicate devices, readable text, logos, and watermarks.

Composition:
3:4 vertical, slightly above seated eye level, monitor at left foreground, woman at right, framing from top of head through upper thighs, hidden smartphone clearly readable below the desk.
```

## 4バリエーション

共通プロンプトの末尾へ1つずつ追加し、4枚とも別々に初期生成する。

1. **balanced** — Broad diffused neutral afternoon light; front three-quarter view; monitor large at left foreground. Treat the calibrated upper-torso silhouette and broad dark lowlight panels as non-negotiable.
2. **overcast** — Soft even overcast window light; slightly wider frame; notebook and stationery especially natural and visible; absolutely no rim light or fine halo around the hair. Treat the calibrated upper-torso silhouette and broad dark lowlight panels as non-negotiable.
3. **warm** — Restrained warm late-afternoon ambience with neutral ceiling fill; no hard sunlight, no backlit hair outline; monitor at left foreground. Treat the calibrated upper-torso silhouette and broad dark lowlight panels as non-negotiable.
4. **post-rain** — Cool post-rain daylight with a few soft window droplets and subdued cityscape; slightly elevated camera; hidden phone especially readable below desk. Treat the calibrated upper-torso silhouette and broad dark lowlight panels as non-negotiable.

## 運用上の注意

- 生成結果を次の入力画像にしない。必ず上記4参照へ戻る。
- 髪の黒メッシュは黒い細線ではなく、太い毛束の内部にある暗い色面として生成する。
- 胸部は具体的なカップ数に置き換えず、Image 3 の頭部に対する見かけ幅・前方の厚み・外周シルエットで合わせる。
- 出力側の安全判定で停止した場合は、身体部位の語を増やさず、`Image 3's approved professional garment silhouette and natural drape` と簡潔にして同じ元参照から再試行する。
