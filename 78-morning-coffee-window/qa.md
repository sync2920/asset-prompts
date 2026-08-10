# QA — 朝のコーヒー、窓辺の余白

## Deterministic checks

All four requested slots exist and decode as RGB PNG, 1086×1448 (exact 3:4).

| Slot | Bytes | SHA-256 |
|---|---:|---|
| 01 | 2,185,916 | `f60289a5ecbafe03194c0cea21d6f0da9daaabad49d2f58f3fbe1811c81e850a` |
| 02 | 2,162,218 | `0ba72e5a42070aaffd1e63f7739a4a30181727b790323bec5cadc764a7fd319f` |
| 03 | 2,343,467 | `31f92084c5ab8ad132114407aded545854d7c04c2f0a8f0f26a1094f333af175` |
| 04 | 2,306,040 | `5772cca7d9e04b0e62f1ccf4b69d1ec1953d6548b32e3529600d3ac4dd44551f` |

## Generation path

- Built-in Codex `image_generation`, sole reference `main/_profile/01.png`.
- Initial full prompt call created no artifact and was rejected by output moderation (`sexual`).
- The successful calls used safer, less anatomical wording while retaining adult identity, natural appearance/proportions, the fully clothed shirt-and-trouser outfit, coffee action, and scene. Exact successful prompt snapshots are saved as `generator-prompt-01.txt` through `generator-prompt-04.txt`.
- Passthrough guarantee: 01–04 are the first four successfully generated artifacts, saved unchanged. No slot was silently regenerated, replaced, edited, or curated.

## Visual QA

Common passes across all four:
- clearly adult, one person, plausible match to the sole person reference;
- overall natural build and visible clothed silhouette are retained without obvious distortion;
- calm lowered gaze before the first sip;
- exactly one coffee cup held with both hands;
- ice-blue fine-stripe long shirt, rolled sleeves, and pearl-grey fluid trousers;
- compact pale-oak Japanese apartment window nook;
- diffuse side-front daylight, no branding, text, food, flowers, books, phone, or second cup;
- hands and cup are anatomically coherent in all four.

Slot notes:
- **01:** strong face scale and intimate mood. The cup is low enough and the shirt drape is readable. A hard sun patch appears across the lower shirt/lap despite the softer-light target; camera is slightly higher than requested.
- **02:** most environmental space and strongest visible steam. Pose is closer to frontal than a distinct three-quarter turn; steam crosses the shirt front but does not hide the face.
- **03:** clean balanced framing and good clothing readability. Cup sits slightly higher than the upper-waist target and visible steam is minimal.
- **04:** calmest, most symmetrical stillness and strongest body/clothing readability. Pose is near-frontal rather than clearly three-quarter; neckline opens deeper than the restrained target and visible steam is minimal.

All four are delivered without replacement as required. Deviations are annotations only.