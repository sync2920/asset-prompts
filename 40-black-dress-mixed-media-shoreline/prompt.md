# 黒いドレスへの衣装変更

## 参照画像の役割

- Image 1: 編集対象。構図、人物の位置・ポーズ・表情、海、空、夕日、砂浜、波打ち際、色彩、混合素材の質感、侵食表現を固定する。
- Image 2: 成人女性の本人性・顔・髪・体型・身体比率の参照。飲食店、料理、箸、アクセサリー、白い衣装などは持ち込まない。

## 共通プロンプト

```text
Use case: identity-preserve
Asset type: finished surrealist mixed-media cinematic artwork, landscape 16:9

Primary request:
Perform a surgical wardrobe-only edit on Image 1. Change only the adult woman's existing garment into an elegant, fully opaque black dress. The dress must be unmistakably readable as a dress within the existing crop: a clean sleeveless neckline, broad dress straps, a tailored fitted bodice, subtle princess seams, and natural fabric drape around her preserved body shape. Use deep matte black fabric with restrained grayscale edge highlights from the sunset so the silhouette and tailoring remain visible. Do not expand or crop the frame.

Input images:
Image 1 is the immutable edit target and scene master. Preserve its pixels, framing, camera viewpoint, horizon, sunset, clouds, shoreline, monochrome beach, colorful mixed-media ocean, every collage patch and wave texture, lighting, color distribution, and analog intrusion details as closely as possible.
Image 2 is identity and physique reference only for the adult woman. Do not import the restaurant, food, table, chopsticks, glass, bracelet, white dress, pose, daylight setting, or any other object from Image 2.

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
- Keep the woman's exact face, side profile, expression, gaze direction, hair shape and strands, head angle, neck, shoulders, body proportions, stance, scale, and placement from Image 1 unchanged.
- Keep her quiet, calm acceptance; no fear, surprise, smile change, or dramatic acting.
- Keep the woman and foreground beach in the same high-contrast monochrome treatment.
- Preserve the existing small colorful mixed-media invasion on her face, hairline, shoulder, and garment boundary in the same locations, scale, and colors.
- Keep the entire sea side, sky, sun, waves, shoreline, sand, collage, stained-glass, resin, mineral, impasto, paper-cut, liquid, pixel, and neon textures unchanged.
- Change only the visible garment construction and fabric into a black dress.

Dress specification:
Elegant minimalist black dress; fully opaque; sleeveless; broad straps; refined clean neckline; fitted tailored bodice; subtle dressmaking seams; realistic weight and drape; no logos, patterns, lace, mesh, transparency, cutouts, ruffles, bows, jewelry, necklace, earrings, bracelet, gloves, or added accessories. It must not look like a T-shirt, sweater, cloak, jacket, or generic black top.

Avoid:
Any face change, hairstyle change, body reshaping, pose change, camera change, reframing, crop change, background regeneration, ocean simplification, texture homogenization, color shift, extra objects, extra people, restaurant elements, food, tableware, text, signature, border, or watermark.

Output intent:
A high-resolution cinematic image that appears identical to Image 1 except that the adult woman is clearly wearing an elegant black dress.
```

## 4バリエーションの差分

1. マットな黒のスクープネック、幅広ストラップ、控えめなプリンセスシーム。
2. マットな黒の浅いスクエアネック、幅広ストラップ、端正なボディス。
3. 黒のサテン・クレープ、柔らかなボート寄りネック、光沢はごく控えめ。
4. 黒のクレープ、緩やかなハートネック、装飾なしの構築的なボディス。
