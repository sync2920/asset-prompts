# V2 QA — オーバーTと朝日の逆光

## Deterministic checks

All four requested passthrough slots exist and decode as RGB PNG.

| Slot | Dimensions | Bytes | SHA-256 |
|---|---:|---:|---|
| 01 | 1086×1448 | 1,902,188 | `fb35a01abe76a9c08232cdf3afce44cfd4e243d5be852caf817c96661d67c25f` |
| 02 | 1086×1448 | 2,010,244 | `62a52db098f04987defe9d7e336c196fe5ccabd145caf0dfb01c4e5c2c8d3036` |
| 03 | 1087×1447 | 2,025,420 | `41a9aec3edb58bdd8dd8864c291ece5d2c27153e379d02d96d6bfb93938ddf08` |
| 04 | 1086×1448 | 1,994,588 | `007b91a11a9c0f493b1d29a9650ec584d6a7eeaaecda43ab14d1b9c6391e6a09` |

01, 02, and 04 are exact 3:4. 03 is approximately 3:4 with a one-pixel-class dimension drift.

## Provenance

- Built-in Codex image generation; sole person reference `main/_profile/01.png` was attached first.
- Exactly four calls created four artifacts; no no-artifact moderation retry occurred.
- Exact successful generator prompts are saved as `generator-v2-prompt-01.txt` through `generator-v2-prompt-04.txt`.
- Each image is the first successful output for its slot and was copied unchanged. No image was ranked, edited, regenerated, or replaced.

## Common visual passes

- clearly adult; one plausible reference-matched person in every image;
- warm-ivory oversized crew-neck T-shirt with dropped shoulders and elbow-length sleeves;
- continuous hem fully covers the pelvis, seat, and upper thighs;
- no visible lower garment, underwear edge, intimate area, or wardrobe malfunction;
- compact Japanese living room with sofa, pale wood, large window, sheer curtain, and one coffee cup;
- warm morning backlight and readable near-frontal face;
- no obvious hand defects; hands are naturally hidden behind the body;
- no text, logo, second cup, or distracting extra prop.

## Slot notes

- **01:** longest and loosest shirt; strongest T-shirt-dress read and intimate portrait crop. The backlight and hair rim are clear. Torso transmittance is very restrained, so the requested body line is read mostly from drape rather than through-fabric visibility.
- **02:** cleanest full-body context and clearest no-visible-bottom styling. Shirt is the most opaque-looking of the four; body-line translucency is weaker than requested.
- **03:** balanced room composition and warm backlight. Shirt remains mostly opaque, with only faint transmission at sleeve edges; 1087×1447 rather than exact 3:4.
- **04:** strongest centered backlit silhouette and the most readable broad body line of the set, while remaining safely covered. Still subtler than a clearly sheer shirt; no precise anatomy is visible.

All four are delivered unchanged. The main deviation across the batch is **translucency being more subtle than requested**, especially in 02 and 03.