# 採用した顎修正版へ黒いドレスを局所合成

## 原本

`../43-chin-localized-clean-edit/03-balanced-clean.png`

## 処理方針

1. 原本を参照して黒いドレス版を生成する。
2. 生成結果を全画面には使用しない。
3. 首元・肩・上半身・衣装だけをソフトマスクで原本へ合成する。
4. 採用済みの顔・顎・表情・髪・海・空・砂浜は原本画素を維持する。
5. 原本の肩にある色彩の侵食部分を抽出し、黒いドレスの上へ戻す。

## 局所合成の実装

- 衣装マスク: 左下の人物領域だけを覆う多角形を `12px` 相当でフェザー。
- 顔・顎・頭部: 原本を楕円マスクで再度重ね、採用済みの画素を復元。
- 肩の侵食: 原本の彩度成分と肩領域を掛け合わせ、周囲を少し拡張して再合成。
- 画面右側: `x >= 720` を原本で再度上書きし、海側を完全一致させる。
- 推奨1案目の差分は `692x484+28+457` 内だけ。顔領域・上端 `420px`・右側 `x >= 720` は原本と差分 `0px`。

## 共通プロンプト

```text
Use case: identity-preserve
Asset type: localized wardrobe replacement for a finished surrealist cinematic artwork, landscape 16:9

Image 1 is the immutable edit target, identity reference, physique reference, composition reference, and scene master.

Primary request:
Change only the adult woman's existing black garment into an elegant, fully opaque black dress. Within the existing upper-body crop it must clearly read as a dress through a refined neckline, dress straps or sleeves, a tailored fitted bodice, subtle princess seams, and natural fabric drape. Use deep black fabric with restrained grayscale edge highlights so the construction remains readable in the monochrome foreground.

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
- Keep the adopted face and chin profile exactly unchanged.
- Keep the expression, gaze, nose, lips, cheeks, eyes, head angle, neck length, hairstyle, every hair strand, body proportions, pose, scale, and placement unchanged.
- Keep the colorful analog-paint intrusion marks on the face, hairline, shoulder, and garment boundary in the same locations, scale, and colors.
- Keep the entire beach, shoreline, sea, every wave, sunset, sky, sun, collage layout, color distribution, and mixed-media textures unchanged.
- Change only the clothing construction and the small areas of shoulder/chest naturally revealed by the new neckline.

Dress specification:
Elegant minimalist black dress; fully opaque; tailored bodice; realistic weight and drape; subtle dressmaking seams; no logos, printed patterns, lace, mesh, transparency, cutouts, ruffles, bows, jewelry, necklace, earrings, bracelet, gloves, or added accessories.

Avoid:
Any face or chin change, hairstyle change, body reshaping, pose change, camera change, reframing, crop change, background regeneration, ocean change, texture homogenization, color shift, extra objects, extra people, text, signature, border, or watermark.

Output intent:
A high-resolution cinematic image identical to Image 1 except that the adult woman is clearly wearing an elegant black dress.
```

## 4バリエーション

1. マットブラック、スクープネック、幅広ストラップ。
2. マットブラック、浅いスクエアネック、端正なボディス。
3. 黒のサテン・クレープ、浅いボートネック、控えめな艶。
4. 黒のクレープ、控えめなハートネック、構築的なボディス。
