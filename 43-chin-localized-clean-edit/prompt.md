# 顎先だけを局所修正し、背景ノイズの累積を防ぐ

## 原本

`../39-identity-swap-mixed-media-shoreline/01-identity-swap-candidate.png`

## 処理方針

1. 原本から顔周辺を `360x400+330+80` で切り出す。
2. 切り出しだけを画像生成で編集し、顎先の前方突出をわずかに抑える。
3. 生成結果のうち顎周辺だけを、約 `90x85px` のフェザー付きマスクで原本へ合成する。
4. 海、空、髪、服、身体、顔の大部分は原本画素をそのまま残す。生成結果を全画面へ再適用しない。

## 生成プロンプト

```text
Use case: identity-preserve
Asset type: localized facial-profile correction patch for an existing surrealist cinematic artwork

Image 1 is the EDIT TARGET and sole identity/style reference. It is a crop from the immutable master image.

Primary request:
Perform a surgical micro-edit confined to the adult woman's chin-tip silhouette. Reduce only the excessive forward projection of the bony chin point by a very small amount, drawing the frontmost contour slightly backward into a naturally balanced profile. Keep the same chin height, jaw length, jaw angle, lower lip, mouth, expression, and identity. Blend the corrected contour into the existing monochrome skin texture, shadow, rim light, and the abstract mixed-media background immediately behind it.

Identity and physique lock:
Match the reference image exactly for gender presentation, ancestry, body shape and
lines, height impression, proportions, overall build, skin tone and texture, facial
features, hair, and all physical characteristics including chest and hip shape and
fullness. Reproduce the natural volume and silhouette of the bust and hips as seen
in the reference, kept accurate through the fit and drape of the clothing. Preserve
the subject's identity and physique faithfully without age-shifting, beautifying,
exaggerating, or reshaping. Never add or hardcode features that are not present in
the reference image — no invented hair colors, accessories, uniforms, or props.

Hard invariants:
- Change only the outer contour of the chin tip and its immediately adjacent lower-face silhouette.
- Keep the nose, nostril, philtrum, upper lip, lower lip, mouth position, expression, cheek, eye, brow, forehead, ear, jaw angle, neck, head angle, gaze, hair, and every visible strand unchanged.
- Keep all grayscale skin texture, existing analog-paint intrusion marks, lighting, and the mixed-media sea behind the face consistent with the input crop.
- Keep the crop framing and subject placement unchanged.

Avoid:
A receding or weak chin, shortened jaw, V-line reshaping, pointed doll-like chin, double chin, altered lips, altered nose, altered cheek, face slimming, generalized beautification, age shift, expression change, hairstyle change, reframing, texture simplification, color shift, extra objects, text, signature, border, or watermark.

Output intent:
The crop must remain visually identical at first glance, with only a subtly less projecting and more naturally balanced chin tip.
```

## 4バリエーション

1. Ultra subtle: 前方突出を約3%抑える。
2. Subtle: 前方突出を約5%抑える。
3. Balanced: 前方突出を約6%抑え、顎先を自然に丸める。
4. Soft contour: 前方突出を約5%抑え、最前点だけを柔らかくする。
