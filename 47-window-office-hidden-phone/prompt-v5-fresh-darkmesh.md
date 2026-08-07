# 47 v5 — 元参照から一発生成・顔と黒メッシュ・低ノイズ

この版は、生成済みオフィス画像を編集元として使わず、元参照から毎回独立して生成する。
`generated-v4-01-balanced-office.png` は身体を再描画するための元画像ではなく、ブラウス越しの胸の大きさを測る補助参照にだけ使用する。

## 入力画像の順番

1. `reference-face-dark-lowlights.png` — 顔の印象、髪型、髪色、黒いメッシュ状ローライトのみ
2. 人物ID参照画像 — 肌、体型、身体寸法、胸・腰まわりの形とボリュームのみ
3. `generated-v4-01-balanced-office.png` — 承認済みの胸の大きさとブラウス越しのシルエットのみ
4. `reference-desk-layout.png` — 窓・机・モニターの配置のみ

## 共通プロンプト

```text
Use case: photorealistic-natural
Asset type: fresh first-generation reference-guided Japanese office lifestyle photograph

Generate a completely new image directly from the source references. Do not edit, enhance, restyle, or continue any previous generated office image.

Input roles:
- Image 1 is the sole authority for the clearly adult woman's face, facial identity and overall facial impression, exact hairstyle, overall hair color, and darker woven mesh-like lowlights. Use only its face and hair; do not copy its clothing, body measurements, restaurant, food, pose, or camera.
- Image 2 is the sole authority for apparent age, skin, body shape, height impression, proportions, overall physique, and all physical characteristics including chest and hip shape and fullness. Do not copy its outfit, restaurant, food, or pose.
- Image 3 is used only as an exact visual measurement for the approved upper-torso size and blouse silhouette. Match its visible bust size, width, projection, position, and blouse volume exactly. Do not transfer Image 3's face, hair, digital texture, hands, office arrangement, lighting, or noise.
- Image 4 is the sole authority for desk geometry: the long desk axis projects inward at 90 degrees from the window wall, visually “window │──── desk,” never parallel to the windows.

Identity and physique fidelity:
Infer apparent age from Image 2 and preserve it. Match the references exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in Image 2, while matching the approved office-blouse presentation shown in Image 3. Keep this accurate through the fit and drape of clothing. Preserve the subject faithfully without age-shifting, beautifying, slimming, exaggerating, or reshaping. Never add or hardcode physical features absent from the references.

Face:
Closely preserve Image 1's facial identity and gentle facial impression. Adapt only the head direction and eyes to the monitor. Use a warm, natural closed-mouth smile with quietly amused brightness. The face and eyes remain clearly focused on the computer monitor, never the camera or phone.

Hair:
Match Image 1's hairstyle, bangs, part, shoulder length, overall color, and dark mesh-like lowlights. Make the darker lowlights visibly present as softly blended dimensional ribbons inside the roots, inner layers, and selected larger locks. They must create depth, not thin black outlines or zebra stripes.

Build the hairstyle from broad coherent softly curved locks with smooth tonal gradients, rounded ends, antialiased contours, and only a few flyaways. Keep fine detail within larger locks; never draw the whole hairstyle strand by strand.

Office scene:
A real contemporary Japanese open-plan office beside large windows. A pale-wood peninsula desk extends inward at a strict right angle from the window. Place a large monitor directly ahead of the subject near the window-side end. Include keyboard, mouse, open notebook, pen, restrained pen cup, sticky notes, and document tray arranged naturally. A few coworkers and desks are softly blurred in the background.

Pose:
Seat her upright at the office-side end, facing the monitor. One hand operates the mouse. The other holds one smartphone low beside the thigh, fully below the desktop and partly hidden by the desk edge. The screen is dim and blank. Keep both arms away from the front of the torso.

Outfit and approved size:
Use a fully opaque pale powder-blue long-sleeved office blouse and dark navy or charcoal high-waisted tailored trousers. The blouse has a centered non-wrap V-neck with a small, tasteful natural center opening. It uses a soft fluid weave with discreet shaping darts.

The blouse must match Image 3's approved upper-torso size and silhouette exactly. It follows the selected volume, curves naturally over it, and falls from its outer contour. Keep the same visible width and forward fullness as Image 3 rather than a flat, loose, boxy, tent-like, compressed, or undersized front. Do not enlarge beyond Image 3.

Clean optical rendering:
Clean low-ISO professional documentary photograph, quality 50mm lens at f/2.8, smooth continuous tones, gentle optical sharpness, restrained local contrast, natural skin, and a soft depth transition. The face, mouse hand, and phone hand remain readable without aggressive micro-detail.

No grain, digital noise, chroma speckling, HDR, clarity effect, oversharpening, edge enhancement, ringing, bright halos, crunchy texture, scratch-like lines, sawtooth hair outlines, isolated wiry strands, repeated zigzag curls, or synthetic high-frequency detail.

Composition:
3:4 vertical, slightly above seated eye level, monitor on the left foreground and woman on the right, top of head through upper thighs, hidden smartphone visibly below the desk.

Avoid:
identity drift; transferring face or hair from Images 2 or 3; transferring body from Image 1; desk parallel to windows; phone above desk; gaze away from monitor; direct eye contact; wrap blouse; diagonal crossover blouse; deep neckline; undersized, flattened, compressed, or enlarged upper torso; extra limbs or fingers; malformed hands; duplicate devices; readable text; logos; watermark; noisy hair or black outline strands.
```

## 4バリエーション

各バリエーションは上の共通プロンプトへ末尾指示として追加し、別々に初期生成する。

1. **balanced** — Broad diffused neutral afternoon light; front three-quarter angle; monitor large at left foreground; subject right; head through upper thighs.
2. **overcast** — Soft even overcast window light; slightly wider framing; more notebook and stationery visible; no rim light around hair.
3. **warm** — Restrained warm late-afternoon ambience with neutral ceiling fill; no hard sunlight and no backlit hair outline; monitor at left foreground.
4. **post-rain** — Cool post-rain daylight with a few soft window droplets; subdued cityscape; slightly elevated camera; hidden phone especially readable below desk.

