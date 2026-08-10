# V3 QA — ソファで朝のコーヒー（2枚）

## Deterministic checks

Both requested passthrough slots exist and decode as RGB PNG, exact 1086×1448 (3:4).

| Slot | Bytes | SHA-256 |
|---|---:|---|
| 01 | 2,442,767 | `eb4d67407ce7c1b99c49d96101da9be3ce19ed72178d006862c480f67663c4ca` |
| 02 | 2,320,076 | `7d647fa804f7fb30b9e666c503702852a8f2c231b1c8d3bb8471bec9e08aa51b` |

## Provenance

- Built-in Codex image generation; sole person reference `main/_profile/01.png` attached first.
- Two calls created two artifacts; no moderation retry.
- Exact successful prompts are `generator-v3-prompt-01.txt` and `generator-v3-prompt-02.txt`.
- Both are the first successful provider outputs and were saved unchanged. No replacement or quality-driven regeneration.

## Visual QA

### 01

- **Adult/reference face:** PASS — plausible identity match, readable near-frontal three-quarter face.
- **Sofa/living room/morning backlight:** PASS — clearly seated on sofa with strong warm window light and rim light.
- **Coffee action:** PASS — cup at lower lip, one hand on handle, other hand safely supports on sofa; fingers and cup are coherent.
- **Oversized T-shirt/no visible lower garment:** PASS WITH NOTE — oversized ivory T-shirt is the only visible garment; no underwear or lower garment appears. Hem covers the central pelvis, though it is shorter across the near thigh than the fully draped-lap target.
- **Seated proportions:** PARTIAL — the near knees/thighs are closer to the camera and look enlarged relative to the reference; this is a camera/pose deviation.
- **Requested chest-size preservation:** **FAIL** — the broad boxy front panel visually bridges over and conceals/ flattens the reference chest volume. Exact natural width, projection, position, and chest-to-waist relation are not legible and the result reads smaller/straighter than the reference.
- **Slight transmittance/body line:** FAIL — torso fabric reads essentially opaque; body line is carried mostly by outer drape rather than backlight transmission.

### 02

- **Adult/reference face:** PASS — plausible identity match, good face size and soft gaze.
- **Sofa/living room/morning backlight:** PASS — convincing warm window backlight and simple living room.
- **Coffee action:** PASS — cup at lower lip, fingers and handle coherent.
- **Oversized T-shirt/no visible lower garment:** PASS — continuous shirt hem covers the central seated pelvis and upper thighs; no lower garment or intimate area is visible.
- **Seated proportions:** PASS/PARTIAL — more controlled than 01, knees together and angled; camera still gives substantial thigh area but without obvious wide-angle distortion.
- **Requested chest-size preservation:** **FAIL** — the T-shirt remains boxy and visually flattening. The reference chest's natural projection and width are not preserved/readable; it again looks materially smaller/straighter.
- **Slight transmittance/body line:** PARTIAL/FAIL — slight light transmission appears at the sleeve and side edge, but the torso remains nearly opaque.

## Overall

The requested scene, cup action, living room, morning light, shirt-only styling, and coverage are successful. **The user's highest-priority correction—maintaining the reference chest size—is not achieved in either image.** Both are delivered unchanged because this was a fixed two-image passthrough batch; the failure is annotated rather than hidden or replaced.