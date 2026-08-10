# V4 QA — 幾何学的ドレープ保持（2枚）

## Deterministic checks

Both requested first-success passthrough slots exist and decode as RGB PNG, exact 1086×1448 (3:4).

| Slot | Bytes | SHA-256 |
|---|---:|---|
| 01 | 2,187,639 | `bcfc442eb938db2d5852911b5340bd55a24429042b0bb1f0e1a3b51c5a228a8d` |
| 02 | 2,188,489 | `3c470f8fa7d172b74cef6f30abfe4cbcdd13751eb5331fec5c65f3f8e27af3f9` |

## Provenance

- Built-in Codex image generation; sole person reference `main/_profile/01.png` attached first.
- One Codex exec made two image-generation calls and saved the first successful artifact from each.
- No image was inspected, corrected, regenerated, replaced, or overwritten by Codex.

## Visual QA

### 01

- **Adult/reference face:** PASS — clearly adult, plausible identity match, readable face and preserved hair/skin family.
- **Sofa/living room/morning/coffee:** PASS — one cup at the lips, warm window light, sofa and contemporary room all read clearly.
- **Hands/cup:** PASS — coherent cup, handle, raised hand, and support hand; no obvious extra digits.
- **Coverage/safety:** PASS — the long ivory T-shirt is the only visible garment; the center hem covers the pelvis and no underwear or intimate area is visible. Fabric is opaque-primary with no precise body tracing.
- **Seated perspective:** PARTIAL — joined knees are prominent and the near lower body remains visually large, though less disruptive than V3-01.
- **Geometric chest preservation:** **FAIL/PARTIAL IMPROVEMENT** — there is a faint broad upper-torso curvature and the fabric is not molded into two domes, but the front still reads mostly as a broad planar panel from neckline/shoulders toward the lap. The foremost cloth envelope is not clearly high at the reference chest level, the tangent-release line is weak, and the side outline does not show a decisive chest-level outward bow followed by an inward return at the waist. The reference's natural width/projection still reads materially reduced.

### 02

- **Adult/reference face:** PASS — clearly adult and plausibly the same person; face, hair, and skin remain readable.
- **Sofa/living room/morning/coffee:** PASS — true sip, one cup, warm backlit room and sofa are successful.
- **Hands/cup:** PASS — both hands and cup are coherent without obvious duplication.
- **Coverage/safety:** PASS — continuous hem covers the central pelvis; no lower garment, underwear, or intimate area appears. No wet-cloth cling, artificial cup shapes, or excessive transparency.
- **Seated perspective:** PASS/PARTIAL — legs angle away more cleanly than 01, though thigh area remains substantial.
- **Geometric chest preservation:** **FAIL** — the shirt front remains a smooth, nearly planar A-line/curtain surface with its strongest drape volume lower on the abdomen. There is no clear high foremost point, release line, or chest-wide-to-waist-narrow silhouette. The result remains flatter and narrower than the reference.

## Overall

The consultation-driven V4 wording preserves scene, identity, action, and safe coverage, but **does not reliably recover the reference person's natural chest width, projection, position, or chest-to-waist relationship in either output**. Slot 01 shows only a slight improvement in broad cloth curvature; slot 02 repeats the planar-bridge failure. Both are delivered unchanged because the user requested exactly two first-success outputs with no replacement or quality-driven regeneration.
