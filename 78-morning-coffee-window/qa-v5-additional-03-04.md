# V5 Additional QA — 03/04

## Deterministic checks

Both additional first-success passthrough slots decode as RGB PNG, exact 1086×1448 (3:4).

| Slot | Bytes | SHA-256 |
|---|---:|---|
| 03 | 2,193,606 | `1112601bb8ac2a6489d472cca859603ce9f74b8108e07e86a5fc1b2db0cc8ed2` |
| 04 | 2,091,479 | `cb68608a3f872b9b1530de70b5c814686363434f36612248549e33bd8421ffc0` |

## Provenance

- Authorized by Discord message `1536517101982978139` after the user judged V5 01/02 better and requested two more.
- Same V5 prompt and sole person reference were used unchanged.
- One Codex exec made two additional image-generation calls and saved the first successful artifact from each as 03/04.
- No inspection, correction, regeneration, replacement, overwrite, or quality-driven retry occurred inside Codex.

## Visual QA

### 03

- Clearly adult, plausible identity match, coherent one-cup sip and hands.
- Morning sofa scene and warm window light pass.
- The shirt remains opaque-primary with no precise anatomical tracing or artificial paired shapes.
- **Coverage note:** the center hem generally covers the pelvis, but a small dark triangular region appears between the upper thighs directly below the hem. It may be deep seat/fabric shadow, but it is visually ambiguous and makes coverage less secure than 01/02/04. No explicit intimate anatomy is visible.
- **Physique:** FAIL — the torso panel is broad and nearly planar. The foremost cloth point, chest-level outward side-seam maximum, release line, and inward waist return remain unreadable. Reference width/projection is not preserved and is not an improvement over V5 01/02.

### 04

- Clearly adult, plausible identity, coherent coffee sip and hands.
- Continuous long hem safely covers the central pelvis; no lower garment, underwear, or intimate area is visible.
- No excessive transparency, hard-edged body tracing, artificial paired shapes, or enlargement.
- **Physique:** FAIL — the shirt front again reads as a straight oversized panel. A faint cloth highlight exists high on the torso but does not establish the reference's width or forward projection. The side silhouette does not reach a high maximum and return inward at the waist. It is broadly comparable to V5 01/02 rather than an additional improvement.

## Overall

The two additional outputs preserve the successful identity, scene, action, and overall styling of V5. Neither advances the highest-priority upper-torso geometry beyond 01/02. Slot 03 also carries an ambiguous dark under-hem gap; slot 04 has secure coverage. Both are delivered unchanged under the passthrough rule.
