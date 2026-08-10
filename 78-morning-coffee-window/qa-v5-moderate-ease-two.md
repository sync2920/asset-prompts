# V5 QA — オーバーサイズ部位分解＋胴体moderate ease（2枚）

## Deterministic checks

Both requested first-success passthrough slots exist and decode as RGB PNG, exact 1086×1448 (3:4).

| Slot | Bytes | SHA-256 |
|---|---:|---|
| 01 | 2,032,369 | `2a214ea02b228799d9aef07c274c43ba6a46f050941da7b1ac21c62a75f71232` |
| 02 | 1,896,061 | `77d204ea3c2a9fe6e9fb90b04d0e4926605166a2d09f99633bdc9d670cce564f` |

## Provenance

- Built-in Codex image generation; sole person reference `main/_profile/01.png` attached first.
- One Codex exec made two image-generation calls and saved the first successful artifact from each.
- No inspection, correction, regeneration, replacement, overwrite, or quality-driven retry occurred inside Codex.

## Visual QA

### 01

- **Adult/reference identity:** PASS — clearly adult and plausibly the same person; face, hair, and skin remain readable.
- **Scene/action:** PASS — seated living room, warm morning window light, and a real one-cup sip are clear.
- **Hands/cup:** PASS — cup and visible fingers are coherent without obvious duplication.
- **Coverage/safety:** PASS — the long ivory T-shirt is the only visible garment; central hem covers the pelvis and no underwear or intimate area appears. The textile is opaque-primary with no precise body tracing.
- **Moderate-ease upper torso:** **FAIL** — despite the revised instruction, the generated shirt still uses a visibly wide body block. The front panel descends as a broad, nearly flat surface from shoulder/neckline toward the abdomen.
- **Reference chest geometry:** **FAIL** — no decisive high foremost point, chest-level side-seam maximum, release line, or inward waist return is visible. The strongest garment volume and folds occur around the lower abdomen/lap. The reference width, forward projection, and chest-to-waist relation remain materially reduced.

### 02

- **Adult/reference identity:** PASS — clearly adult, plausible identity match, readable face and hair.
- **Scene/action:** PASS — sofa, one cup at the lower lip, and warm window light all read successfully.
- **Hands/cup:** PASS — coherent drinking hand and support hand; no obvious malformed or extra digits.
- **Coverage/safety:** PASS — continuous shirt hem covers the central pelvis; no lower garment, underwear, or intimate area is visible. No excessive transparency or hard-edged anatomical tracing.
- **Moderate-ease upper torso:** **FAIL** — the shirt again resolves to an oversized, straight body panel rather than a torso panel with moderate ease.
- **Reference chest geometry:** **FAIL** — the upper front is the flattest of the two. The apparent foremost envelope remains on the lower torso, and the outer silhouette does not widen high then return inward at the waist. Exact reference projection and width are not preserved.

## Overall

The V5 change successfully retains identity, scene, action, and safe full coverage, but the image model does **not** follow the requested separation of oversized shoulders/sleeves/length from moderate upper-torso ease. Both first-success outputs retain the dominant oversized-T-shirt prior and flatten the reference upper-torso geometry. No replacement or regeneration was performed; both outputs are delivered unchanged as requested.
