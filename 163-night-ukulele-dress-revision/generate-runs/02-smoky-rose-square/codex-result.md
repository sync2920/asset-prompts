Reading additional input from stdin...
OpenAI Codex v0.147.0
--------
workdir: /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision
model: gpt-5.5
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: xhigh
reasoning summaries: none
session id: 01a014b2-5f86-7482-805a-589e4c88a4ae
--------
user
Use the built-in image generation tool exactly once. Read the complete final prompt from /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision/generate-runs/02-smoky-rose-square/prompt.md and follow it verbatim. The attached first and only image is the identity reference. Save the first successful generated image exactly to /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision/generate-runs/02-smoky-rose-square/generated/01.png. Do not edit any prompt or generate a replacement. In your final reply report only the saved path and actual image format/dimensions.
hook: SessionStart
hook: SessionStart Completed
hook: UserPromptSubmit
hook: UserPromptSubmit Completed
hook: PreToolUse
hook: PreToolUse Completed
exec
/bin/bash -lc "pwd && sed -n '1,220p' /home/natrial/.codex/skills/.system/imagegen/SKILL.md && sed -n '1,260p' .claude/skills/image-ideas/SKILL.md && sed -n '1,260p' generate-runs/02-smoky-rose-square/prompt.md" in /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision
 exited 2 in 0ms:
/home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision
---
name: "imagegen"
description: "Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas."
---

# Image Generation Skill

Generates or edits images for the current project (for example website assets, game assets, UI mockups, product mockups, wireframes, logo design, photorealistic images, or infographics).

## Top-level modes and rules

This skill has exactly two top-level modes:

- **Default built-in tool mode (preferred):** built-in `image_gen` tool for normal image generation, editing, and simple transparent-image requests. Does not require `OPENAI_API_KEY`.
- **Fallback CLI mode:** `scripts/image_gen.py` CLI. Use when the user explicitly asks for the CLI/API/model path, or after the user explicitly confirms a true model-native transparency fallback with `gpt-image-1.5`. Requires `OPENAI_API_KEY`.

Within CLI fallback, the CLI exposes three subcommands:

- `generate`
- `edit`
- `generate-batch`

Rules:
- Use the built-in `image_gen` tool by default for normal image generation and editing requests.
- Do not switch to CLI fallback for ordinary quality, size, or file-path control.
- If the user explicitly asks for a transparent image/background, stay on built-in `image_gen` first: prompt for a flat removable chroma-key background, then remove it locally with the installed helper at `$CODEX_HOME/skills/.system/imagegen/scripts/remove_chroma_key.py`.
- Never silently switch from built-in `image_gen` or CLI `gpt-image-2` to CLI `gpt-image-1.5`. Treat this as a model/path downgrade and ask the user before doing it, unless the user has already explicitly requested `gpt-image-1.5`, `scripts/image_gen.py`, or CLI fallback.
- If a transparent request appears too complex for clean chroma-key removal, asks for true/native transparency, or local removal fails validation, explain that true transparency requires CLI `gpt-image-1.5 --background transparent --output-format png` because `gpt-image-2` does not support `background=transparent`, then ask whether to proceed. Run the CLI fallback only after the user confirms.
- The word `batch` by itself does not mean CLI fallback. If the user asks for many assets or says to batch-generate assets without explicitly asking for CLI/API/model controls, stay on the built-in path and issue one built-in call per requested asset or variant.
- If the built-in tool fails or is unavailable, tell the user the CLI fallback exists and that it requires `OPENAI_API_KEY`. Proceed only if the user explicitly asks for that fallback.
- If the user explicitly asks for CLI mode, use the bundled `scripts/image_gen.py` workflow. Do not create one-off SDK runners.
- Never modify `scripts/image_gen.py`. If something is missing, ask the user before doing anything else.

Built-in save-path policy:
- In built-in tool mode, Codex saves generated images under `$CODEX_HOME/*` by default.
- Do not describe or rely on OS temp as the default built-in destination.
- Do not describe or rely on a destination-path argument (if any) on the built-in `image_gen` tool. If a specific location is needed, generate first and then move or copy the selected output from `$CODEX_HOME/generated_images/...`.
- Save-path precedence in built-in mode:
  1. If the user names a destination, move or copy the selected output there.
  2. If the image is meant for the current project, move or copy the final selected image into the workspace before finishing.
  3. If the image is only for preview or brainstorming, render it inline; the underlying file can remain at the default `$CODEX_HOME/*` path.
- Never leave a project-referenced asset only at the default `$CODEX_HOME/*` path.
- Do not overwrite an existing asset unless the user explicitly asked for replacement; otherwise create a sibling versioned filename such as `hero-v2.png` or `item-icon-edited.png`.

Shared prompt guidance for both modes lives in `references/prompting.md` and `references/sample-prompts.md`.

Fallback-only docs/resources for CLI mode:
- `references/cli.md`
- `references/image-api.md`
- `references/codex-network.md`
- `scripts/image_gen.py`

Local post-processing helper:
- `$CODEX_HOME/skills/.system/imagegen/scripts/remove_chroma_key.py`: removes a flat chroma-key background from a generated image and writes a PNG/WebP with alpha. Prefer auto-key sampling, soft matte, and despill for antialiased edges.

## When to use
- Generate a new image (concept art, product shot, cover, website hero)
- Generate a new image using one or more reference images for style, composition, or mood
- Edit an existing image (inpainting, lighting or weather transformations, background replacement, object removal, compositing, transparent background)
- Produce many assets or variants for one task

## When not to use
- Extending or matching an existing SVG/vector icon set, logo system, or illustration library inside the repo
- Creating simple shapes, diagrams, wireframes, or icons that are better produced directly in SVG, HTML/CSS, or canvas
- Making a small project-local asset edit when the source file already exists in an editable native format
- Any task where the user clearly wants deterministic code-native output instead of a generated bitmap

## Decision tree

Think about two separate questions:

1. **Intent:** is this a new image or an edit of an existing image?
2. **Execution strategy:** is this one asset or many assets/variants?

Intent:
- If the user wants to modify an existing image while preserving parts of it, treat the request as **edit**.
- If the user provides images only as references for style, composition, mood, or subject guidance, treat the request as **generate**.
- If the user provides no images, treat the request as **generate**.

Built-in edit semantics:
- Built-in edit mode is for images already visible in the conversation context, such as attached images or images generated earlier in the thread.
- If the user wants to edit a local image file with the built-in tool, first load it with built-in `view_image` tool so the image is visible in the conversation context, then proceed with the built-in edit flow.
- Do not promise arbitrary filesystem-path editing through the built-in tool.
- If a local file still needs direct file-path control, masks, or other explicit CLI-only parameters, use the explicit CLI fallback only when the user asks for it.
- For edits, preserve invariants aggressively and save non-destructively by default.

Execution strategy:
- In the built-in default path, produce many assets or variants by issuing one `image_gen` call per requested asset or variant.
- In the CLI fallback path, use the CLI `generate-batch` subcommand only when the user explicitly chose CLI mode and needs many prompts/assets.
- For many distinct assets, do not use `n` as a substitute for separate prompts. `n` is for variants of one prompt; distinct assets need distinct built-in calls or distinct CLI `generate-batch` jobs.

Assume the user wants a new image unless they clearly ask to change an existing one.

## Workflow
1. Decide the top-level mode: built-in by default, including simple transparent-output requests; fallback CLI only if explicitly requested or after the user explicitly confirms a transparent-output fallback.
2. Decide the intent: `generate` or `edit`.
3. Decide whether the output is preview-only or meant to be consumed by the current project.
4. Decide the execution strategy: single asset vs repeated built-in calls vs CLI `generate-batch`.
5. Collect inputs up front: prompt(s), exact text (verbatim), constraints/avoid list, and any input images.
6. For every input image, label its role explicitly:
   - reference image
   - edit target
   - supporting insert/style/compositing input
7. If the edit target is only on the local filesystem and you are staying on the built-in path, inspect it with `view_image` first so the image is available in conversation context.
8. If the user asked for a photo, illustration, sprite, product image, banner, or other explicitly raster-style asset, use `image_gen` rather than substituting SVG/HTML/CSS placeholders. If the request is for an icon, logo, or UI graphic that should match existing repo-native SVG/vector/code assets, prefer editing those directly instead.
9. Augment the prompt based on specificity:
   - If the user's prompt is already specific and detailed, normalize it into a clear spec without adding creative requirements.
   - If the user's prompt is generic, add tasteful augmentation only when it materially improves output quality.
10. Use the built-in `image_gen` tool by default.
11. For transparent-output requests, follow the transparent image guidance below: generate with built-in `image_gen` on a flat chroma-key background, copy the selected output into the workspace or `tmp/imagegen/`, run the installed `$CODEX_HOME/skills/.system/imagegen/scripts/remove_chroma_key.py` helper, and validate the alpha result before using it. If this path looks unsuitable or fails, ask before switching to CLI `gpt-image-1.5`.
12. Inspect outputs and validate: subject, style, composition, text accuracy, and invariants/avoid items.
13. Iterate with a single targeted change, then re-check.
14. For preview-only work, render the image inline; the underlying file may remain at the default `$CODEX_HOME/generated_images/...` path.
15. For project-bound work, move or copy the selected artifact into the workspace and update any consuming code or references. Never leave a project-referenced asset only at the default `$CODEX_HOME/generated_images/...` path.
16. For batches or multi-asset requests, persist every requested deliverable final in the workspace unless the user explicitly asked to keep outputs preview-only. Discarded variants do not need to be kept unless requested.
17. If the user explicitly chooses or confirms the CLI fallback, then use the fallback-only docs for model, quality, size, `input_fidelity`, masks, output format, output paths, and network setup.
18. Always report the final saved path(s) for any workspace-bound asset(s), plus the final prompt or prompt set and whether the built-in tool or fallback CLI mode was used.

## Transparent image requests

Transparent-image requests still use built-in `image_gen` first. Because the built-in tool does not expose a true transparent-background control, create a removable chroma-key source image and then convert the key color to alpha locally.

Default sequence:
1. Use built-in `image_gen` to generate the requested subject on a perfectly flat solid chroma-key background.
2. Choose a key color that is unlikely to appear in the subject: default `#00ff00`, use `#ff00ff` for green subjects, and avoid `#0000ff` for blue subjects.
3. After generation, move or copy the selected source image from `$CODEX_HOME/generated_images/...` into the workspace or `tmp/imagegen/`.
4. Run the installed helper path, not a project-relative script path:
   ```bash
   python "${CODEX_HOME:-$HOME/.codex}/skills/.system/imagegen/scripts/remove_chroma_key.py" \
     --input <source> \
     --out <final.png> \
     --auto-key border \
     --soft-matte \
     --transparent-threshold 12 \
     --opaque-threshold 220 \
     --despill
   ```
5. Validate that the output has an alpha channel, transparent corners, plausible subject coverage, and no obvious key-color fringe. If a thin fringe remains, retry once with `--edge-contract 1`; use `--edge-feather 0.25` only when the edge is visibly stair-stepped and the subject is not shiny or reflective.
6. Save the final alpha PNG/WebP in the project if the asset is project-bound. Never leave a project-referenced transparent asset only under `$CODEX_HOME/*`.

Prompt transparent requests like this:

```text
Create the requested subject on a perfectly flat solid #00ff00 chroma-key background for background removal.
The background must be one uniform color with no shadows, gradients, texture, reflections, floor plane, or lighting variation.
Keep the subject fully separated from the background with crisp edges and generous padding.
Do not use #00ff00 anywhere in the subject.
No cast shadow, no contact shadow, no reflection, no watermark, and no text unless explicitly requested.
```

Do not automatically use CLI `gpt-image-1.5 --background transparent --output-format png` instead of chroma keying. Ask the user first when the user asks for true/native transparency, when local removal fails validation, or when the requested image is complex: hair, fur, feathers, smoke, glass, liquids, translucent materials, reflective objects, soft shadows, realistic product grounding, or subject colors that conflict with all practical key colors.

Use a concise confirmation like:

```text
This likely needs true native transparency. The default built-in path uses a chroma-key background plus local removal, but true transparency requires the CLI fallback with gpt-image-1.5 because gpt-image-2 does not support background=transparent. It also requires OPENAI_API_KEY. Should I proceed with that CLI fallback?
```

## Prompt augmentation

Reformat user prompts into a structured, production-oriented spec. Make the user's goal clearer and more actionable, but do not blindly add detail.

Treat this as prompt-shaping guidance, not a closed schema. Use only the lines that help, and add a short extra labeled line when it materially improves clarity.

### Specificity policy

Use the user's prompt specificity to decide how much augmentation is appropriate:

- If the prompt is already specific and detailed, preserve that specificity and only normalize/structure it.
- If the prompt is generic, you may add tasteful augmentation when it will materially improve the result.

Allowed augmentations:
- composition or framing hints
- polish level or intended-use hints
- practical layout guidance
- reasonable scene concreteness that supports the stated request

Not allowed augmentations:
- extra characters or objects that are not implied by the request
- brand names, slogans, palettes, or narrative beats that are not implied
- arbitrary side-specific placement unless the surrounding layout supports it

## Use-case taxonomy (exact slugs)

Classify each request into one of these buckets and keep the slug consistent across prompts and references.

Generate:
- photorealistic-natural — candid/editorial lifestyle scenes with real texture and natural lighting.
- product-mockup — product/packaging shots, catalog imagery, merch concepts.
- ui-mockup — app/web interface mockups and wireframes; specify the desired fidelity.
- infographic-diagram — diagrams/infographics with structured layout and text.
- scientific-educational — classroom explainers, scientific diagrams, and learning visuals with required labels and accuracy constraints.
- ads-marketing — campaign concepts and ad creatives with audience, brand position, scene, and exact tagline/copy.
- productivity-visual — slide, chart, workflow, and data-heavy business visuals.
- logo-brand — logo/mark exploration, vector-friendly.
- illustration-story — comics, children’s book art, narrative scenes.
- stylized-concept — style-driven concept art, 3D/stylized renders.
- historical-scene — period-accurate/world-knowledge scenes.

Edit:
- text-localization — translate/replace in-image text, preserve layout.
- identity-preserve — try-on, person-in-scene; lock face/body/pose.
- precise-object-edit — remove/replace a specific element (including interior swaps).
- lighting-weather — time-of-day/season/atmosphere changes only.
- background-extraction — transparent background / clean cutout. Use built-in `image_gen` with chroma-key removal first for simple opaque subjects; ask before using CLI true transparency for complex subjects.
- style-transfer — apply reference style while changing subject/scene.
- compositing — multi-image insert/merge with matched lighting/perspective.
- sketch-to-render — drawing/line art to photoreal render.

## Shared prompt schema

Use the following labeled spec as shared prompt scaffolding for both top-level modes:

```text
Use case: <taxonomy slug>
Asset type: <where the asset will be used>
Primary request: <user's main prompt>
Input images: <Image 1: role; Image 2: role> (optional)
Scene/backdrop: <environment>
Subject: <main subject>
sed: can't read .claude/skills/image-ideas/SKILL.md: No such file or directory

hook: PostToolUse
hook: PostToolUse Completed
codex
I’m reading the required prompt and the local workflow instructions first so the generation call can stay exactly within the requested constraints.
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse
hook: PreToolUse Completed
exec
/bin/bash -lc "rg --files -g 'SKILL.md' /home/natrial/_work/X/asset-prompts /home/natrial/_work/X 2>/dev/null | rg 'image-ideas/SKILL.md"'$'"'" in /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision
 exited 1 in 0ms:
hook: PostToolUse
hook: PostToolUse Completed
exec
/bin/bash -lc "sed -n '121,260p' /home/natrial/.codex/skills/.system/imagegen/SKILL.md" in /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision
 succeeded in 0ms:
Transparent-image requests still use built-in `image_gen` first. Because the built-in tool does not expose a true transparent-background control, create a removable chroma-key source image and then convert the key color to alpha locally.

Default sequence:
1. Use built-in `image_gen` to generate the requested subject on a perfectly flat solid chroma-key background.
2. Choose a key color that is unlikely to appear in the subject: default `#00ff00`, use `#ff00ff` for green subjects, and avoid `#0000ff` for blue subjects.
3. After generation, move or copy the selected source image from `$CODEX_HOME/generated_images/...` into the workspace or `tmp/imagegen/`.
4. Run the installed helper path, not a project-relative script path:
   ```bash
   python "${CODEX_HOME:-$HOME/.codex}/skills/.system/imagegen/scripts/remove_chroma_key.py" \
     --input <source> \
     --out <final.png> \
     --auto-key border \
     --soft-matte \
     --transparent-threshold 12 \
     --opaque-threshold 220 \
     --despill
   ```
5. Validate that the output has an alpha channel, transparent corners, plausible subject coverage, and no obvious key-color fringe. If a thin fringe remains, retry once with `--edge-contract 1`; use `--edge-feather 0.25` only when the edge is visibly stair-stepped and the subject is not shiny or reflective.
6. Save the final alpha PNG/WebP in the project if the asset is project-bound. Never leave a project-referenced transparent asset only under `$CODEX_HOME/*`.

Prompt transparent requests like this:

```text
Create the requested subject on a perfectly flat solid #00ff00 chroma-key background for background removal.
The background must be one uniform color with no shadows, gradients, texture, reflections, floor plane, or lighting variation.
Keep the subject fully separated from the background with crisp edges and generous padding.
Do not use #00ff00 anywhere in the subject.
No cast shadow, no contact shadow, no reflection, no watermark, and no text unless explicitly requested.
```

Do not automatically use CLI `gpt-image-1.5 --background transparent --output-format png` instead of chroma keying. Ask the user first when the user asks for true/native transparency, when local removal fails validation, or when the requested image is complex: hair, fur, feathers, smoke, glass, liquids, translucent materials, reflective objects, soft shadows, realistic product grounding, or subject colors that conflict with all practical key colors.

Use a concise confirmation like:

```text
This likely needs true native transparency. The default built-in path uses a chroma-key background plus local removal, but true transparency requires the CLI fallback with gpt-image-1.5 because gpt-image-2 does not support background=transparent. It also requires OPENAI_API_KEY. Should I proceed with that CLI fallback?
```

## Prompt augmentation

Reformat user prompts into a structured, production-oriented spec. Make the user's goal clearer and more actionable, but do not blindly add detail.

Treat this as prompt-shaping guidance, not a closed schema. Use only the lines that help, and add a short extra labeled line when it materially improves clarity.

### Specificity policy

Use the user's prompt specificity to decide how much augmentation is appropriate:

- If the prompt is already specific and detailed, preserve that specificity and only normalize/structure it.
- If the prompt is generic, you may add tasteful augmentation when it will materially improve the result.

Allowed augmentations:
- composition or framing hints
- polish level or intended-use hints
- practical layout guidance
- reasonable scene concreteness that supports the stated request

Not allowed augmentations:
- extra characters or objects that are not implied by the request
- brand names, slogans, palettes, or narrative beats that are not implied
- arbitrary side-specific placement unless the surrounding layout supports it

## Use-case taxonomy (exact slugs)

Classify each request into one of these buckets and keep the slug consistent across prompts and references.

Generate:
- photorealistic-natural — candid/editorial lifestyle scenes with real texture and natural lighting.
- product-mockup — product/packaging shots, catalog imagery, merch concepts.
- ui-mockup — app/web interface mockups and wireframes; specify the desired fidelity.
- infographic-diagram — diagrams/infographics with structured layout and text.
- scientific-educational — classroom explainers, scientific diagrams, and learning visuals with required labels and accuracy constraints.
- ads-marketing — campaign concepts and ad creatives with audience, brand position, scene, and exact tagline/copy.
- productivity-visual — slide, chart, workflow, and data-heavy business visuals.
- logo-brand — logo/mark exploration, vector-friendly.
- illustration-story — comics, children’s book art, narrative scenes.
- stylized-concept — style-driven concept art, 3D/stylized renders.
- historical-scene — period-accurate/world-knowledge scenes.

Edit:
- text-localization — translate/replace in-image text, preserve layout.
- identity-preserve — try-on, person-in-scene; lock face/body/pose.
- precise-object-edit — remove/replace a specific element (including interior swaps).
- lighting-weather — time-of-day/season/atmosphere changes only.
- background-extraction — transparent background / clean cutout. Use built-in `image_gen` with chroma-key removal first for simple opaque subjects; ask before using CLI true transparency for complex subjects.
- style-transfer — apply reference style while changing subject/scene.
- compositing — multi-image insert/merge with matched lighting/perspective.
- sketch-to-render — drawing/line art to photoreal render.

## Shared prompt schema

Use the following labeled spec as shared prompt scaffolding for both top-level modes:

```text
Use case: <taxonomy slug>
Asset type: <where the asset will be used>
Primary request: <user's main prompt>
Input images: <Image 1: role; Image 2: role> (optional)
Scene/backdrop: <environment>
Subject: <main subject>
Style/medium: <photo/illustration/3D/etc>
Composition/framing: <wide/close/top-down; placement>
Lighting/mood: <lighting + mood>
Color palette: <palette notes>
Materials/textures: <surface details>
Text (verbatim): "<exact text>"
Constraints: <must keep/must avoid>
Avoid: <negative constraints>
```

Notes:
- `Asset type` and `Input images` are prompt scaffolding, not dedicated CLI flags.
- `Scene/backdrop` refers to the visual setting. It is not the same as the fallback CLI `background` parameter, which controls output transparency behavior.
- Fallback-only execution notes such as `Quality:`, `Input fidelity:`, masks, output format, and output paths belong in the CLI path only. Do not treat them as built-in `image_gen` tool arguments.

Augmentation rules:
- Keep it short.
- Add only the details needed to improve the prompt materially.
- For edits, explicitly list invariants (`change only X; keep Y unchanged`).
- If any critical detail is missing and blocks success, ask a question; otherwise proceed.

## Examples

### Generation example (hero image)
```text
Use case: product-mockup
Asset type: landing page hero
Primary request: a minimal hero image of a ceramic coffee mug
Style/medium: clean product photography
Composition/framing: wide composition with usable negative space for page copy if needed
Lighting/mood: soft studio lighting
Constraints: no logos, no text, no watermark
```

### Edit example (invariants)
```text
Use case: precise-object-edit
Asset type: product photo background replacement
Primary request: replace only the background with a warm sunset gradient
Constraints: change only the background; keep the product and its edges unchanged; no text; no watermark

hook: PostToolUse
hook: PostToolUse Completed
exec
/bin/bash -lc "sed -n '1,260p' generate-runs/02-smoky-rose-square/prompt.md" in /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision
 succeeded in 0ms:
# 163-02: Smoky Rose Square — Night Ukulele Dress Revision (3:4 Vertical)

A highly detailed photorealistic portrait of the person from the reference image.
3:4 aspect ratio. Infer apparent age from the reference image and preserve it.
Match the reference image exactly for gender presentation, ancestry, body shape and
lines, height impression, proportions, overall build, skin tone and texture, facial
features, hair, and all physical characteristics including chest and hip shape and
fullness. Reproduce the natural volume and silhouette of the bust and hips as seen
in the reference, kept accurate through the fit and drape of the clothing. Preserve
the subject's identity and physique faithfully without age-shifting, beautifying,
exaggerating, or reshaping. Never add or hardcode features that are not present in
the reference image — no invented hair colors, accessories, uniforms, or props.

Scene: A quiet, atmospheric late-night outdoor music terrace under a clear indigo night sky. An adult woman is captured in a continuous full-length photorealistic editorial photograph as she sits comfortably on a wooden stool, holding a small four-string ukulele and playing the very first chord. Exactly ONE continuous full-frame photograph; strictly no collage, split panels, contact sheets, or multiple views.

Pose and Action: Seated naturally on a wooden stool in a three-quarter orientation, her posture relaxed yet attentive. Her right hand's index finger gently brushes downward across the top string of the ukulele near the soundhole, capturing the exact micro-instant of the initial strum. Her left hand cleanly holds the slim neck of the ukulele, her fingertips precisely fretting the first chord notes near the nut. Her face is clear and subtly illuminated by soft terrace ambient light, with a gentle, serene expression as her eyes rest on the instrument in quiet focus. Contact geometry is strictly preserved: valid hand anatomy with five distinct fingers on each hand, natural joint positioning, firm hand contact with instrument surfaces, and both silver-gray ballet flats rest flat on the wooden deck floor. The ukulele is held securely across her mid-torso, keeping her neck and square neckline completely unblocked.

Outfit: A muted smoky-rose square-neck bias crepe midi dress paired with silver-gray leather ballet flats. The dress features wide shoulder straps supporting a clean, modest square neckline that frames her collarbones elegantly with full upper coverage and no deep plunge. Designed with a gentle A-line bias drape that skims her waist without bodycon tightness, the dress cascades into a soft flared midi hem below the knees. Tailored from premium matte crepe fabric with a soft drape, the garment is fully lined for total opacity, delivering refined nocturnal music lifestyle styling free of sheer panels, cutouts, plunging necklines, thigh-high slits, bodycon compression, or visible underwear.

Ukulele Geometry: Exactly ONE compact four-string acoustic wooden ukulele with a smooth matte finish, a dark rosette around the central soundhole, and a slim wooden fretboard. The headstock features exactly four distinct tuning pegs (two per side). Exactly four clean, taut nylon strings stretch parallel along the fretboard from nut to bridge pins, plainly visible and distinct with zero extra strings or guitar features.

Lighting and Environment: An intimate permitted outdoor music terrace featuring warm dark wooden deck planks beneath her stool and a low wooden safety railing. The background opens to a deep indigo night sky accented by soft, distant amber bokeh lights from low garden fixtures. A subtle night air movement lightly lifts only the hair tips and skirt hem. Strictly no audience, no second person, no alcohol, no animals, no sheet music, no floating musical notes or visual soundwaves, no stage spotlights, no fireworks, no text, and no logos.

Camera and Framing: 3:4 vertical full-length editorial portrait capturing her head, body, hands, ukulele, and ballet flats on the terrace floor. Shot with an 85mm prime lens at f/2.8, achieving crisp detail on her facial expression, hands, crepe fabric texture, and ukulele strings, with soft depth-of-field blurring the dark terrace background. Authentic photorealism with natural skin texture and real night ambience; no digital smoothing, synthetic filters, or fantasy light effects.

Avoid: no collage, no split screen, no photo strip, no contact sheet, no multi-pose grid, no extra limbs, no extra fingers, no malformed hands, no pointing pose, no finger guns, no guitar geometry, no six strings, no extra tuning pegs, no duplicated instruments, no sheet music, no floating musical notes, no visual soundwaves, no stage lights, no alcohol, no crowds, no second person, no readable text, no logos, no brand markings, no watermarks, no sheer skin exposure, no plunging neckline, no cutouts, no thigh-high slit, no visible underwear, no chest obstruction, no bodycon compression.

hook: PostToolUse
hook: PostToolUse Completed
hook: PreToolUse
hook: PreToolUse Completed
exec
/bin/bash -lc "rg --files -g 'SKILL.md' /home/natrial 2>/dev/null | rg '("'^|/)image-ideas/SKILL.md$'"'" in /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision
 exited 1 in 117ms:
hook: PostToolUse
hook: PostToolUse Completed
hook: PreToolUse
hook: PreToolUse Completed
exec
/bin/bash -lc "rg --hidden --files -g 'SKILL.md' /home/natrial 2>/dev/null | rg '("'^|/)image-ideas/SKILL.md$'"'" in /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision
 succeeded in 339ms:
/home/natrial/_work/X/asset-prompts/.claude/skills/image-ideas/SKILL.md

hook: PostToolUse
hook: PostToolUse Completed
hook: PreToolUse
hook: PreToolUse Completed
exec
/bin/bash -lc "sed -n '1,260p' /home/natrial/_work/X/asset-prompts/.claude/skills/image-ideas/SKILL.md" in /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision
 succeeded in 0ms:
---
name: image-ideas
description: >-
  asset-prompts リポジトリでの画像生成プロンプトのアイデア出し・作成・派生・改良の標準ワークフロー。
  依頼に「アイデア」「案」「プロンプト」「画像生成」「この人物で」「朝投稿/昼投稿/夜投稿用」などの言葉が
  含まれるとき、人物の参照画像が添付・指定されたとき、既存案（番号指定を含む）の派生や手直しを
  頼まれたときは、スキル名が明示されていなくても必ずこのスキルを使う。人物参照を使わない
  ランダム系・季節系（random/, random2/, season/）のプロンプト依頼にもこのスキルを使う。
argument-hint: "[依頼内容 例: この画像の人物で朝投稿用の案を3つ / 人物参照なしで夏の案]"
---

# 画像生成アイデア出しワークフロー

このリポジトリは、特定人物（参照画像）の SNS 投稿用画像を生成するためのプロンプト集。
画像生成はここでは行わず、完成プロンプトを外部の生成AI（ChatGPT / Gemini など）へ参照画像と
一緒に貼り付けて行う。つまりプロンプトは単体で完結した成果物で、本文に書かれていない指示は
生成AIに一切届かない。
規約の本体はリポジトリ内の文書にあり、このスキルは「毎回どこを読み、何をしてから案を出すか」だけを定める。
規約そのものはここに複製しない。更新は常に `ideas/README.md` 側で行われるため、このスキルより
リポジトリ内の文書のほうが常に新しい。両者が食い違ったら文書側に従う。

## モード判定

- **人物参照モード（デフォルト）**: 参照画像が添付されている、パスで指定されている、または「この人物で」と
  言われた場合。人物の案を求められたら指定がなくてもこちらを前提にする。画像が見当たらなければ、
  作業を始める前にどの画像を使うか確認する（過去の参照画像が `main/` 以下に置かれていることもある）。
- **人物参照なしモード**: 「人物参照なし」「ランダム系」と明示された場合、または `random/`・`random2/`・
  `season/` のファイルを対象にした依頼。→「人物参照なしモード」のセクションへ。

### XワークフローからCodex生成へ引き渡す場合

- 人物を含む完成プロンプトは「入力された人物参照画像に写っている人物を使用し、同一人物として
  身体的特徴を保持する」形式にする。人物の具体的な外見を文章だけで固定しない。
- Codex CLIで実画像生成まで明示依頼された場合、人物参照の第1画像は
  `/home/natrial/_work/X/asset-prompts/main/_profile/01.png`とする。
- Codexの`--image <FILE>...`は可変長なので、初期プロンプトは`--image`より前へ置き、固定人物画像を
  `--image`の最初のファイルとして渡す。追加の背景・画風参照はその後ろへ役割順に並べる。
- ユーザーが同じ依頼で別人物を明示した場合のみ、その人物画像を先頭へ置いて固定画像を置き換える。
- プロンプト作成だけの依頼では画像生成しない。

## 人物参照モードの手順

### 1. 規約を読み込む（毎回・省略しない）

1. `ideas/README.md` を全文読む。身体特徴の保持方針、共通テンプレート、衣装とシチュエーションの基準、
   プロンプト記述の共通規約、アスペクト比の使い分けが全部ここに集約されており、これが唯一の正典。
2. `ls ideas/` で一覧を取り、既存案のテーマ（ファイル名でおおむね分かる）と現在の最大通し番号を把握する。
   似た主題の既存ファイルがあれば開いて中身を確認する。依頼が既存番号を指す場合（例: 「205 の派生」）は
   その番号を含むファイルを必ず先に読む。
3. 主題に応じて表現技法を読む:
   - 透け感・薄手の衣装・親密な場面 → `expression/01-sheer-skin-intimacy.md`
   - 夏の暑さ・実写感（プロカメラマン調） → `expression/02-summer-heat-realism.md`

### 2. 参照画像を厳密に読み取る

Read ツールで参照画像を実際に開いて観察する。複数枚あればすべて開く。印象で済ませず、
次の項目を一つずつ確認してメモする:

見た目年齢 / 性別表現 / 民族的な印象 / 顔立ち（骨格・目・眉・鼻・口・顎）/ 肌の色と質感 /
髪（型・色・長さ・前髪）/ 体型と身体のライン / 胸・腰まわりの自然なボリューム /
身長感とプロポーション / 全体の雰囲気（クール・柔らかい・あどけない 等）

- **成人判定を最初に行う。** 参照人物が明確に成人と判断できない場合、色気を含む衣装・演出は使わず、
  `ideas/README.md` の成人条件どおり健全な代替衣装・ポーズに切り替える。
- **読み取り結果は「案の設計」に使う。** 似合う衣装・場面・見せ場の選定、髪の長さと風・光の絡ませ方、
  人物の雰囲気に合うトーン選びに反映する。読み取らずに出した案は人物と噛み合わない。
- **保持の「指示」は毎回プロンプト本文に丸ごと書く。** プロンプトは外部の生成AIへ単体で貼られるため、
  本文にない指示は届かない。`ideas/README.md` の共通テンプレートにある保持ブロック
  （Match the reference image exactly for … including chest and hip shape and fullness /
  never add or hardcode … の一連）を、省略も要約もせずに全案へ含める。
- **一方、読み取った「中身」は本文に書き写さない。** 髪色や顔立ちをテキストで固定すると参照とズレた
  別人が出る（`04/prompt.md` で確立した運用）。中身は添付する参照画像そのものに語らせ、本文には
  保持指示だけを書く。同じ理由で、参照にない要素（髪色・アクセサリー・小物・キャラ設定）を
  ハードコードしない。

### 3. 案を設計する

- 依頼から用途を汲む: 投稿時間帯（朝・昼過ぎ・夜）、狙うトーン（上品な色気 / だらしない色気 / 健やか /
  かっこいい / 非日常・幻想 / 生活の余韻）、アスペクト比。指定がなければ案ごとにトーンと比率を散らす。
- 衣装を決める前に、現在日付を確認してウェブとXをライブ検索する。公式ブランドの現行コレクション・
  ルックブック・キャンペーン、公式ファッション媒体、ブランド／編集部の公式Xを優先し、元ページまたは
  元投稿を開いて公開日・対象シーズン・地域を確認する。個人投稿の出現頻度より公式側の今季の押し出しを
  優先する。根拠は原則2件以上、うち1件以上を公式一次情報にする。
- 参照画像の衣装は、ユーザーが明示していない限りコピーしない。直近12件の人物プロンプトの `Outfit` を
  検索して、READMEの8軸で比較し、各直近案および同時提案同士から最低4軸を変える。
- 明確に成人で場面に無理がなければ、胸元はREADMEの「少し谷間が自然に読める」を既定目標にする。
  ネックラインはトレンドと季節に合わせて変え、谷間を理由に同じキャミソールや深いVへ収束させない。
- `ideas/README.md` の基準に従って組む: 一着につき見せ場は一箇所、透け感には必ず構造、
  服の特徴を仕草へ接続、ポーズは動作の途中（candid）。
- 各案について「既存案との差」を一行で言えること。言えなければ既存案の派生として明示する。

### 4. 出力形式

案ごとに次をセットで出す（`ideas/197-199-morning-post.md` 以降の体裁に合わせる）:

- 見出し: 番号候補とタイトル
- 設計メモ: **比率** / **見せ場** / **差し替え変数** / **季節・気温・場所** / **公式トレンド根拠とURL** /
  **直近12件から変えた4軸以上** / **胸元の構造と成人条件** / **シーン接続**。必要なら例外事項
  （緩い服で隠す例外、透けの設計 等）も含める。
- 完成プロンプト全文（```text ブロック）: `ideas/README.md` の共通テンプレート骨格に沿った英語プロンプト。
  日本語プロンプトを求められた場合は `14-morning-balcony-morning-glory/prompt.md` の書式
  （人物参照ブロック＋節立て）に合わせる。どちらの言語でも、保持ブロック込みでそのまま貼り付けて
  単体で使える完全文になっているかを確認してから出す。

まずチャットで案を見せ、ユーザーの指示があってからファイルに保存する。最初から「保存して」と
言われている場合は直接保存してよい。

### 5. 保存

- アイデアのストックは `ideas/NNN-slug.md`。NNN は既存の最大通し番号 +1 から、slug は内容を表す
  英語ケバブケース。設計メモ（この案をどう組んだか、既存案との差）も同じファイルに書き残す。
- 保存したら `ideas/README.md` の「収録ファイル」一覧に、既存行と同じ文体で 1 行追記する。
- 生成実行まで進める運用（画像を作って残す）の場合は、リポジトリ直下の `NN-slug/prompt.md` 形式
  （`09`〜`14` と同じ、番号は直下の最大 +1）で新しいフォルダを作る。
- 実際の画像生成まで依頼された場合、ユーザーから別の枚数指定がなければ、同じ依頼から 1 回につき
  **4 枚**を生成する。4 枚は構図・瞬間・光・細部に自然な差を持つバリエーションとし、参照人物や
  中心コンセプトは共通に保つ。これはプロンプト案を必ず 4 案出すという意味ではない。

## 人物参照なしモード

人物の見た目もテキストで指定する方式。参照画像は読まない。

- 汎用スロット式: `random/prompt.md`（メタプロンプト本体）と `random/safe.md`（表現の整え方）。
- 季節特化・エモ版: `season/<季節>.md`（現行: `summer.md`）。冒頭の設計メモに「なぜこの構成か」が
  書かれているので必ず読んでから触る。
- これらの改良・派生を頼まれたら、対象ファイルの形式（スロット表・整合ルール・共通末尾）を
  保ったまま編集する。形式を壊すと「1回貼れば毎回違う組み合わせが出る」という用途が壊れる。
- 人物が主題でない依頼（風景・小物など）は通常のプロンプト設計でよいが、カメラブロックや
  画質指定の流儀は既存プロンプトの書き方に合わせる。

## 全モード共通の書き方

`expression/README.md` の言い回し規約を、生成するすべてのテキスト（プロンプト本文、設計メモ、
README への追記）で守る。描写は「素材・光・輪郭で間接的に表現する手法」として書き、
対立的・回避的な言い回しは使わない。理由も `expression/README.md` に書かれている。

hook: PostToolUse
hook: PostToolUse Completed
codex
I’m using the `imagegen` skill here because this is a built-in raster image generation request. The repository’s prompt workflow file is present at the parent `asset-prompts` level, and the requested prompt has been read as-is.
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/bin/bash -lc "sed -n '1,260p' /home/natrial/_work/X/asset-prompts/ideas/README.md" in /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision
 succeeded in 0ms:
# 画像生成アイデア集

`04/prompt.md` の運用（人物の年齢、性別表現、顔、髪、肌、体型、身体のライン、身長感、プロポーションなどは参照画像だけから推定・保持し、ポーズ・服・背景・アスペクト比をテキストで指定する方式）を前提としたバリエーション案。

## 収録ファイル

- [50-variations.md](50-variations.md) — 初期50案の原案アーカイブ。現在の生成には、衣装と場面を再設計した次の完成版を推奨。
- [001-050-full-prompts.md](001-050-full-prompts.md) — 日常、夜の街、小さな特別な日を中心に、上品な色気・生活の余韻・クールさ・幻想を織り交ぜた完成英語プロンプト50案。
- [181-engawa-watermelon.md](181-engawa-watermelon.md) — 単発1案（181）。夏の縁側でスイカ、着古したキャミソールの緩みを軸にしたドキュメンタリー調。設計メモ付き。
- [182-196-office-casual-cool.md](182-196-office-casual-cool.md) — オフィスカジュアル／かっこいい系15案（182〜196）。移動と通過、執務空間の余白、退勤と切り替えの3群。露出ではなく仕立て・光・重心で強さを出す設計。
- [100-viral-prompts.md](100-viral-prompts.md) — 新規100案（051〜150）。上品な色気25案、だらしない色気20案、四季と小さな特別な日20案、非日常・幻想20案、かっこいい堅実服15案。
- [197-199-morning-post.md](197-199-morning-post.md) — 朝投稿用3案（197〜199）。朝の斜光を主役に、キッチンの湯気／朝ラン後の自販機／旅先ホテルのカーテン開けの3場面。
- [200-morning-garden-mist.md](200-morning-garden-mist.md) — 朝投稿用1案（200）。裏庭で植物に水、ホースの霧が低い朝日を浴びて光の粒子の柱になる一瞬。霧（空気）と薄い布の二重の透過で輪郭を描く設計。
- [356-riverside-dawn-back-three-quarter.md](356-riverside-dawn-back-three-quarter.md) — 朝投稿用1案（356）。夜明けの河川敷を右横寄り斜めから捉えた歩行。マットなベージュ/クリーム系キャミ＋淡い花柄シフォンのミディ丈スカート＋ヌード系フラットサンダルでワントーンにまとめ、地平線から顔を出す朝焼けの逆光がシフォンを透かし脚の輪郭をぼやっと影絵として浮かべる。上の直接光・下の透過光を1主題に統一し、露の草むら・朝靄・遠景の鉄橋で河川敷の世界を埋めつつ人影ゼロの静けさを維持。振り返り・真横・後ろ寄りを避けた設計。
- [357-balcony-wind-laundry.md](357-balcony-wind-laundry.md) — 10時投稿用1案（357）。狭いベランダで白いシーツを干す動作の途中を9:16で捉える。両腕を頭上へ伸ばして二つ折りのシーツを竿にかける瞬間、タンクが脇から持ち上がり肋骨〜腰骨のサイドラインと脇の開きが10時の白い光に読まれる。片側を垂らしたままもう片側だけ手を離して風で帆のように膨らませ、干し方の物理を自然に。白リブタンク＋セージグリーンリネンのホットパンツで爽やかに。透けを使わず動作の幾何学だけで無防備さを出す設計。
- [358-library-stretch.md](358-library-stretch.md) — 15時ごろ投稿用1案（358）。現代の日本の公共図書館の個人閲覧席で、読書・作業のあと手を組んで真上に伸びる一瞬を3:4で捉える。机を右下から大きく入れてラップトップを右端で切る斜めローアングル、窓を背後に縦長、本棚を左奥。めがねはシーンに存在させず、ニットは完全不透明で透けを使わない。見せ場は伸びの幾何学と裾上がりで覗くへその上端。顔には窓の直接光を当てず天井と壁反射の間接光だけで均一に、他者は写さず左奥の閲覧席も無人の空席とする設計。
- [359-361-meteor-shower-anime-sky.md](359-361-meteor-shower-anime-sky.md) — 夜投稿用3案（359〜361）。みずがめ座δ南流星群（極大7/31 22時ごろ）とやぎ座α流星群のダブル極大の夜に、13の媒質混交方式を「空そのものがアニメ」へ転用したシリーズ。南低空のみずがめ座の放射点・やぎ座の火球・頭上の夏の大三角形と天の川・満月から欠け始めの月という実際の空を劇場アニメ背景として描く。丘のブランケット（9:16）・都会の屋上（3:4）・湖の桟橋（16:9）の3場面。361の初稿を21として採用し、銀白色の大きな月を追加済み。
- [362-371-refreshing-cool-ten.md](362-371-refreshing-cool-ten.md) — 清涼系10案（362〜371）。12（屋上ジュース）の「真夏の日常×一瞬の涼」のトーンを継承しつつ、涼の源を10種に分解して既視感を避けたシリーズ。水飲み場／クリームソーダ／クラゲ水槽／渓流足浸し（365 → `../28-afternoon-stream-feet-soak` として採用）／ハンモック／金魚すくい／湖の水切り／日傘／手水舎／牧場ソフトクリーム。
- [372-386-summer-morning-fifteen.md](372-386-summer-morning-fifteen.md) — 夏の朝投稿用15案（372〜386）。暑さが始まる前の光・水気・風を軸に、犬の散歩／朝のサーフィン／青空朝市／自然な目覚め／朝靄のSUP／茶畑／潮干狩り／波打ち際／山頂のご来光／田んぼ／温泉街／自転車／砂浜の絵／すだれの光／早朝ロープウェイへ展開したアイデア集。プロンプト未作成。
- [387-390-bikini-trends-one-piece.md](387-390-bikini-trends-one-piece.md) — 2026夏トレンド水着4案（387〜390）。'90sホルター×チェリーレッド花柄（3:4）・ワンショルダー×コバルト（9:16）・スカロップ×シェルモチーフ×白（4:5）・ビーズ×ミッドナイトブルー（16:9）のワンピース水着を、昼間の公共レジャー・引きの環境構図で設計。ChatGPT画像でビキニ版が4回連続で安全フィルタに弾かれた経緯と、ワンピース化・解剖学テンプレ削除などの回避策を設計メモに記録。
- [391-393-waterslide-spray-light.md](391-393-waterslide-spray-light.md) — 水滑り台×水飛沫×太陽光3案（391〜393）。
- [394-395-dusty-blue-embroidered-lingerie.md](394-395-dusty-blue-embroidered-lingerie.md) — 刺繍セット着用2案（394〜395）。1枚目=人物（既定参照）／2枚目=衣装写真（デザイン・パレット・モチーフの供給元）の2画像運用。v1・v2 停止、v3（レオタード）通過だが「ダサい」、v4（バレエ）もレオタード感が残る、v5（朝ベッド＋ブライダル＋友人スマホ枠）は失敗率上昇。v6（2026-08-07 現行）は最小トリガー版: 見た目は v5 維持（朝ベッド・ポーズ・下着見え・デュベ遮蔽・洗練仕様）のまま、ブライダル枠・友人スマホ枠・寝起き語・two-piece/top/bottoms 名詞を全削除し、文脈を無害なラウンジウェアルックブックの朝スチルへ。15時ごろの屋外ウォータープールの滑り台を滑る一瞬を、ド派手な水飛沫と飛沫に反射する西日を主役に切り取る。躍動感・爽快感・清涼感が趣旨。流行りのビキニは水着の直接語を削除し、expression/01の幾何学・光学言い回しで衣装と身体を輪郭として描き、水飛沫のヴェールを構図的遮蔽（布で見せないの水版）の主役にして衣装を「飛沫の中の色と線」に抽象化。衣装はユーザー指定でトップ＝ヴィンテージフローラル柄（クリーム地にバターイエローの花×ダークオリーブの芯・ブラッシュピンク・深緑の小葉）、下＝無地の白。差別化はトップのシルエット（ワンショルダー非対称／細いコード紐／パイピング＋ビーズ点）で行う。フローラル非対称ライン×急カーブ（9:16）・フローラル紐×ストレート正面（3:4・幾何学スリム版で検証済み）・フローラル点×着水の光の壁（16:9）。胸・腰のボリュームはユーザー指示により保持ブロックで参照どおり保持（圧縮版: サイズ保持2文＋布の挙動文のみ、高位文はトリガー表面積削減のため本文から外し任意付加オプション化）。文脈枠は `summer sportswear catalog feature — a clean, wholesome, energetic outdoor scene`。
- [396-after-rain-overpass.md](396-after-rain-overpass.md) — 夏の夕方投稿用1案（396）。夕立が去った直後の歩道橋で、濡れた路面に映る珊瑚色・紫・青の残光、閉じた透明傘、雨上がりの風を3:4縦で捉える。261の降り始めに対し、水鏡と冷えた空気を主役にした帰り道の余韻。
- [206-355-daily-thrill-fusion.md](206-355-daily-thrill-fusion.md) — 新規150案（206〜355）。不意のドキッ20案、生活の手元20案、気配のツーショット15案、天気の変わり目15案、一点だけの異変（静かなマジックリアリズム）20案、現実半分・空想半分15案、街の時間外20案、音・温度・匂いの可視化10案、手仕事と趣味15案。
- [205-rooftop-juice-short-shadow.md](205-rooftop-juice-short-shadow.md) — お昼過ぎ投稿用1案（205）。真夏の屋上で缶ジュース、頂光に近い午後一の太陽が足元に短い影を落とす構図。風でオーバーシャツが膨らみ布が体から離れる一瞬を、媒質変奏シリーズの「風による離反」として設計。
- [../expression/01-sheer-skin-intimacy.md](../expression/01-sheer-skin-intimacy.md) — 透け感や露出を素材・光・輪郭で間接的に描写する書き方。薄手の衣装や親密な場面の案を組むときの表現手法として参照。
- [../expression/02-summer-heat-realism.md](../expression/02-summer-heat-realism.md) — 夏の暑さと実写感（プロカメラマン撮影）を間接的に描写する書き方。暑さは空気・小道具・素材で出し肌の汗は控えめに、実写感はカメラブロックとディテール要求で出す手法。夏の案や実写感を強めたいときの表現手法として参照。

## 身体特徴の保持（全プロンプト共通の必須方針）

- **顔・胸・お尻を含む体型は、参照画像から必ず忠実に保持する。** 顔立ちはもちろん、胸と腰まわりの形とボリューム、身体のライン、身長感、プロポーションを参照どおりに再現することを全プロンプトの前提にする。
- 英文には `all physical characteristics including chest and hip shape and fullness` と、バスト・ヒップの自然なボリュームが服のフィットとドレープを通して正確に伝わる旨（`reproduce the natural volume and silhouette of the bust and hips as seen in the reference`）を含める。
- 若返り・加齢・美化・痩身化・誇張など、参照からの体型改変は一切行わない（`without age-shifting, beautifying, exaggerating, or reshaping`）。
- **胸が実際より小さく出るときの主因はポーズと生地。** 腕・鞄・フォルダが胸の前を横切ると潰れ、箱型で張りのある生地（crisp / boxy / oversized）は布が浮いてボリュームを消す。シルエットを見せる案では ①胸の前を空ける（nothing held in front of the chest）②体に沿う生地（soft, fluid weave that follows the body）③布の挙動の明示（curves over the bust, drapes from its outermost point, gentle tension lines）の3点を指定する。意図的に緩い服で隠す案は例外として明記する。
- **胸の位置は高く指定する。** 生成では胸が実際より下（ウエスト寄り）に描かれやすい。「支えられて高い位置にある」ことを基準点つきで英文に入れる: `the bust sits high and supported on the ribcage, as if wearing a well-fitted bra: its fullest point is level with the mid-upper arm, roughly at armpit height, with only a short distance between the collarbones and the top of the curve — never sagging low toward the waist`。脇の高さ・二の腕の中ほどなど、体の相対位置を基準にすると効きやすい。

## 衣装とシチュエーションの基準

- **人物参照画像は身体・同一性の資料であり、衣装の既定値ではない:** ユーザーが「この服を使う」と明示した場合を除き、参照画像の服、配色、アクセサリー、スタイリングをコピーしない。新しい案では、その投稿日・季節・時間帯・場所に合う別衣装を毎回設計する。
- **服装を決める前に、その時点のトレンドをライブ調査する:** ウェブ検索とX検索を使い、公式ブランドの現行コレクション／ルックブック／キャンペーン、公式ファッション誌・百貨店・セレクトショップの編集記事、ブランドまたは編集部の公式X投稿を優先する。個人投稿の単純な出現頻度より、公式側が今季に押し出している方向を強い根拠として扱う。根拠は原則2件以上、うち1件以上はブランドまたは編集媒体の公式一次情報とし、公開日、対象シーズン、地域を確認する。検索結果の要約だけで決めず、元ページまたは元投稿を開く。
- **トレンドは模写でなく要素へ分解して翻訳する:** 情報源からシルエット、ネックライン、レイヤリング、素材、色、丈、ディテール、靴・小物の方向だけを抽出し、特定商品の完全コピー、ロゴ、商標柄は避ける。日本で実際に着られる若々しい日常コーデへ再構成し、撮影シーンの動作と気温に整合させる。
- **直近案との重複を機械的に避ける:** 新案の前に直近12件の人物プロンプトの `Outfit` を確認し、①シルエット、②ネックライン、③袖、④素材、⑤レイヤリング、⑥丈・ボトム、⑦主色、⑧靴・小物の8軸で比較する。同じ衣装式を再使用せず、直近案のどれとも最低4軸を変える。同じキャミソール＋同じボトム、同じ白トップス＋リネン、同じワンピース形状などへの収束を禁止する。複数案を同時に出す場合も、案同士で最低4軸を変える。
- **若々しさは露出量ではなく今のスタイリングで出す:** 現行の丈バランス、レイヤリング、素材対比、配色、靴、小物、少しの意外性で20代向けの新鮮さをつくる。幼く見える制服風、過度な装飾、古い「モテ服」の定型、全身を同じブランド風に寄せる設計は避ける。
- **胸元は「少し谷間が自然に読める」を既定の目標にする:** 明確に成人と判断でき、場面と気温に無理がない場合、デコルテを開き、自然な中央の谷間が細く部分的に見えるネックラインを選ぶ。`a subtle, natural, partial central cleavage line` 程度を基準にし、胸全体を押し上げた深い谷間、極端なプランジ、はみ出し、下乳、横乳、下着見え、ワードローブ事故にはしない。胸は完全に支えられ、左右と下側が衣服内に安全に収まることを明記する。
- **谷間を見せてもネックラインを固定しない:** soft V、wrap V、wide scoop、sweetheart-square、draped cowl、structured square、開いたシャツの柔らかなVなどを、トレンド・季節・場面に合わせてローテーションする。寒い季節は室内、開いたアウター、ニットのカッティング、透けないレイヤーなどで自然に成立させ、季節感を犠牲にしない。胸元を一着の唯一の見せ場にした場合、脚・背中・腹部など別の露出は抑える。
- **一着につき見せ場は一箇所:** 背中、片肩、ウエスト、脚などの焦点を一つに絞り、残りは長い丈や端正な仕立てで引き算する。
- **透け感には必ず構造をつくる:** レース、シフォン、オーガンジーなどには不透明な裏地、ボディスーツ、インナーショーツなどを明記し、直接的な透け方にしない。
- **服の特徴を仕草へ接続する:** 背中開きなら振り返り、長い裾なら階段や風、緩んだカーディガンなら帰宅後のソファなど、衣装がその場面にある理由をつくる。
- **上品な色気:** 艶のある素材、精密なカッティング、光の境界、視線、距離感で表現し、露出箇所を増やすだけの設計にしない。
- **だらしない色気:** しわ、半端なタックイン、ずれた上着、ほどけかけの髪など「出来事のあと」の生活感で表現し、脱衣や露骨な描写にはしない。
- **堅実服は映画的な場面へ:** 端正なスーツ、トレンチ、ロングコートなどは、旅の途中、閉館後、式典帰り、雨のホテル玄関など、シルエットが意味を持つ状況で使う。
- **成人条件:** 色気を含む衣装・演出は、参照人物が明確に成人と判断できる場合だけ使用する。年齢が不明、または未成年に見える場合は、同じ配色と雰囲気を保った健全な代替衣装・ポーズへ切り替える。

### 衣装設計メモ（各案で必須）

完成プロンプトの前に、チャット回答または保存ファイルの設計メモへ次を短く残す。URLはプロンプト本文には入れない。

- **季節・気温・場所:** なぜその衣装が現実的か
- **トレンド根拠:** 参照した公式ソース名、公開日または対象シーズン、URL、抽出した要素
- **直近との差:** 直近12件と比べて変えた4軸以上
- **胸元の設計:** 採用したネックライン、見え方を上品に制限する構造、成人条件
- **シーン接続:** 衣装の素材・裾・レイヤーが、ポーズ、風、光、移動などへどうつながるか

## プロンプト記述の共通規約

181（チビドゥードルズ）の元ネタ検証と178派生の知見から一般化した、全プロンプト共通の書き方ルール。

- **参照にないものを足さない（ハードコード禁止）:** 「参照から推測して保持」だけでは、モデルが別キャラクターの特徴（髪色、アクセサリー、制服、小物）を勝手に持ち込むのを防げない。逆方向のガードとして `never add or hardcode features that are not present in the reference` を入れる。共通テンプレートに反映済み。
- **モデル任せの可変要素には収束癖ガード:** ポーズや仕草をモデルに発明させる場合、放置すると指差し・フィンガーガン・棒立ちに収束する。可変にした要素には `never a pointing or finger-gun pose` のように、収束しがちな定番を明示的に外す1句を添える。ポーズを固定指定する案には不要。
- **例示は「ゆるいインスピレーション」と宣言する:** 可変要素に例を並べると毎回先頭の例に収束しがち。例示リストには `loose inspiration only, not a fixed menu — invent freely beyond these` の但し書きを付ける。背景・小物・いたずら・ポーズなど、すべての可変リストに適用できる。
- **表情は形容詞でなく内心で書く:** `cute, shy` のような形容詞の羅列より、`half playing along and half wondering why` のような内心の一文の方が演技が具体化する。表情・リアクションの指定は内心ベースを基本にする。
- **手が目立つ構図には解剖学ネガ:** 手・指がフレーム内で主役級に写る構図（顔の横に手が来るポーズ、差し出す手、小道具を持つ手）では `no extra limbs, extra fingers, or malformed hands` を Avoid 行に入れる。
- **ネガは「観測した失敗」だけを具体で書く:** 否定形はモデルに無視されやすい（178派生の知見）。破綻対策はまず肯定形の描写で行い、それでも出る既知の失敗だけを具体的な語でネガに残す。「明らかなAIアーティファクトなし」のような抽象ネガは効かないので書かない。

## 共通テンプレート

各案は、以下の骨格の「ポーズ / 服装 / 背景 / フォーマット」ブロックを差し替えて使う。

```
A highly detailed photorealistic portrait of the person from the reference image.
[ASPECT] aspect ratio. Infer apparent age from the reference image and preserve it.
Match the reference image exactly for gender presentation, ancestry, body shape and
lines, height impression, proportions, overall build, skin tone and texture, facial
features, hair, and all physical characteristics including chest and hip shape and
fullness. Reproduce the natural volume and silhouette of the bust and hips as seen
in the reference, kept accurate through the fit and drape of the clothing. Preserve
the subject's identity and physique faithfully without age-shifting, beautifying,
exaggerating, or reshaping. Never add or hardcode features that are not present in
the reference image — no invented hair colors, accessories, uniforms, or props.

Pose: [ポーズ]
Outfit: [服装]
Background: [背景と光]
Format: [ASPECT], [縦/横] composition.
```

## アスペクト比の使い分け指針

| 比率 | 向き | 主な用途 |
|---|---|---|
| 9:16 | 縦（超縦長） | 全身と衣装の縦線を見せる、Reels / TikTok / Stories |
| 3:4 | 縦 | バストアップ〜膝上。人物と背景のバランスが最も取りやすい標準 |
| 4:5 | 縦 | Instagram フィードの最大表示。上半身主体 |
| 1:1 | 正方形 | 顔・上半身のクローズ。シンメトリな構図 |
| 4:3 | 横 | 人物＋周囲の状況を見せる。室内・生活シーン向き |
| 16:9 | 横（シネマ） | 風景に人物を溶かす。引きの画、映画的な余白 |

**判断の基準**：被写体を主役にするなら縦、環境を主役にするなら横。全身と長い衣装の流れを見せたいときは 9:16、それ以外の縦は 3:4 か 4:5 のほうが破綻が少ない。どの比率でも、参照由来の身長感や身体比率を変えない。

hook: PostToolUse
hook: PostToolUse Completed
exec
/bin/bash -lc "sed -n '1,240p' /home/natrial/_work/X/asset-prompts/expression/README.md" in /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision
exec
/bin/bash -lc 'mkdir -p generate-runs/02-smoky-rose-square/generated && file /home/natrial/_work/X/asset-prompts/main/_profile/01.png' in /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision
 succeeded in 0ms:
# 表現技法集（expression/）

画像生成プロンプトにおける**間接表現・抽象表現の手法**を蓄積する場所。薄手・透け感・露出・親密さなど、直接的な語彙を使わずに描写を成立させる書き方を、表現方法の一つとして整理する。

`ideas/` が「何を生成するか（シチュエーション・衣装・構図の案）」を扱うのに対し、このフォルダは「どう書くか（語彙・構造・文脈の作り方）」を扱う。両者は併用する。

## このフォルダの位置づけ

- ここは表現スタイルのカタログであって、運用ルールの告示ではない。各ファイルは「こう書くと描写が安定し、かつ上品に収まる」という観察の記録。
- ファイルは主題ごとに通し番号で増やしていく（`01-...md`, `02-...md`）。
- 記述は「回避」「突破」「制限をかいくぐる」のような対立的な枠組みではなく、**「間接的に表現する一手法」「素材・光・輪郭で語る書き方」** として書く。プロンプト本文や README にそのまま引用されても健全な文脈として読まれる言い回しを保つ。

## 収録ファイル

- [01-sheer-skin-intimacy.md](01-sheer-skin-intimacy.md) — 透け感・露出・親密さを、光学・幾何学・演出の語彙で間接的に描写する手法。語彙の置換対応表、光学語彙バンク、輪郭抽象化、布/枕/背向けによる構図の遮蔽、段階的な表現の強弱の順序、再利用テンプレート構造を含む。
- [02-summer-heat-realism.md](02-summer-heat-realism.md) — 夏の暑さと実写感（プロカメラマン撮影）を間接的に描写する手法。暑さは空気・小道具・素材で出し肌の汗は控えめに留める書き方、実写感はカメラブロックとディテール要求で出す書き方。語彙対応表、環境語彙バンク、カメラ語彙バンク、段階的な強弱の順序を含む。

## ideas/README.md への記載ルール

`ideas/README.md` からこのフォルダを引用するときは、**「表現方法の一つ」「間接表現の手法」** として書き、対立・回避のニュアンスを出さない。具体例：

> - [expression/01-sheer-skin-intimacy.md](../expression/01-sheer-skin-intimacy.md) — 透け感や露出を素材・光・輪郭で間接的に描写する書き方。薄手の衣装や親密な場面の案を組むときの表現手法として参照。

### 書いてよいこと

- 「間接的に表現する」「素材と光で語る」「輪郭として抽象化する」「構図で見せない」
- 「描写が安定する」「上品に収まる」「健全な文脈として読まれる」
- 手法そのもの（語彙、構造、構図）の説明

### 避けること

- 「制限を回避する」「審査を突破する」「フィルターを逃れる」「弾かれないようにする」
- 「NG語彙」「禁止語」「トリガー」という言葉の使用
- 対立的・闘争的な言い回し（モデル運営と対峙するような構え）

理由: これらの書き方が README やプロンプトに混入すると、別のAIがそのテキストを読んだときに「意図的に基準を迂回しようとしている」と解釈し、プロンプト自体を却下する可能性がある。表現選択の記録、という枠組みを保つことで、テキスト自体も健全な文脈に収まる。

## 各ファイルの書式

- 主題を表すタイトル（「〜を間接的に描写する手法」）
- 基本方針：なぜこの書き方が描写として成立するか
- 語彙対応表：直接寄りの表現 ↔ 間接表現
- 語彙バンク：そのまま使える言い回しセット
- 構図・構造の指針
- 段階的な強弱の順序（表現を強める/弱める順）
- 再利用テンプレート（あれば）
- 実例への参照（`ideas/` や `NN/` の該当案）
- 今後の観察メモ（モデル差など）
 succeeded in 0ms:
/home/natrial/_work/X/asset-prompts/main/_profile/01.png: PNG image data, 1086 x 1448, 8-bit/color RGB, non-interlaced

hook: PostToolUse
hook: PostToolUse
hook: PostToolUse Completed
hook: PostToolUse Completed
hook: PreToolUse
hook: PreToolUse Completed
hook: PostToolUse
hook: PostToolUse Completed
codex
The built-in generation completed successfully. I’m copying that first generated output to the exact requested project path and verifying the saved file metadata.
hook: PreToolUse
hook: PreToolUse Completed
exec
/bin/bash -lc 'cp /home/natrial/.codex/generated_images/01a014b2-5f86-7482-805a-589e4c88a4ae/call_SqHdEM1P3LSHSpqkn7mZMbZF.png /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision/generate-runs/02-smoky-rose-square/generated/01.png
file /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision/generate-runs/02-smoky-rose-square/generated/01.png' in /home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision
 succeeded in 0ms:
/home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision/generate-runs/02-smoky-rose-square/generated/01.png: PNG image data, 1086 x 1448, 8-bit/color RGB, non-interlaced

hook: PostToolUse
hook: PostToolUse Completed
codex
/home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision/generate-runs/02-smoky-rose-square/generated/01.png  
PNG, 1086 x 1448
hook: Stop
hook: Stop Completed
tokens used
51,157
/home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision/generate-runs/02-smoky-rose-square/generated/01.png  
PNG, 1086 x 1448
