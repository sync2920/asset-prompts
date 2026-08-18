# Prompt-authoring task — 163 Night Ukulele Dress Revision

You are the **sole author** of the four final image-generation prompts for this run. Do **not** generate images. Read these canonical inputs before writing:

- `/home/natrial/_work/X/asset-prompts/AGENTS.md`
- `/home/natrial/_work/X/asset-prompts/.claude/skills/image-ideas/SKILL.md`
- `/home/natrial/_work/X/asset-prompts/ideas/README.md`
- `/home/natrial/_work/X/asset-prompts/expression/README.md`
- `/home/natrial/_work/X/asset-prompts/162-night-ukulele-first-chord/prompts/01-midnight-knit-polo.md`
- `/home/natrial/_work/X/asset-prompts/162-night-ukulele-first-chord/prompts/02-burnt-coral-satin.md`
- `/home/natrial/_work/X/asset-prompts/162-night-ukulele-first-chord/prompts/03-sheer-layered-t.md`
- `/home/natrial/_work/X/asset-prompts/162-night-ukulele-first-chord/prompts/04-sky-blue-slit-skirt.md`
- `/home/natrial/_work/X/asset-prompts/main/_profile/01.png` (identity only, and it must be the first input image during later generation)

## User’s current revision request

「おしゃれなドレスに近い感じにして。セクシーだけど上品でゆったりな雰囲気」

This is a revision of the already generated four-outfit **Night Ukulele First Chord** series. Create four fresh dress-adjacent alternatives, not shirts plus skirts. The task will later use Codex built-in image generation once per prompt; your work is only to write the final prompts.

## Shared scene contract — preserve exactly

- 3:4 vertical, exactly ONE continuous full-frame photorealistic adult lifestyle/music editorial photograph, full body from head to footwear.
- A quiet, permitted night outdoor wooden music terrace: dark wood deck, low railing, deep indigo sky, distant warm bokeh. No audience, other people, alcohol, animals, stage lighting, fireworks, legible text, logo, or sheet music.
- The adult woman sits naturally on one wooden stool in a three-quarter camera view. She is at the causal instant of the very first chord: camera-near right index finger makes one downward strum of exactly ONE small 4-string ukulele; left fingertips cleanly fret the first chord. Both hands, fingers, instrument, stool, deck contact, and footwear must read coherently.
- The ukulele stays at waist level and must not block the neck or chest area. Exactly four strings, exactly four tuning pegs, no guitar geometry.
- A restrained night breeze moves only hair ends and the lower dress hem. Her face is clearly lit and identity is preserved.

## Dress direction

All four must feel stylish, genuinely dress-like, relaxed but intentional, suitable for a warm August night terrace — polished and elegant rather than sleepwear, lingerie, or a formal red-carpet gown. Adult-safe understated sensuality may appear **only** through one controlled neckline/decolletage detail. Keep all bust support and coverage secure. No sheer skin exposure, visible underwear, plunging neckline, cutouts, thigh-high slit, bodycon compression, or extra bare-skin focal points.

Avoid thin spaghetti straps because they render poorly. Build the relaxed silhouette with real garment structure: wide shoulder bands, a shallow draped cowl / clean square neckline / shallow wrap-V / a light sleeved option, a defined but non-tight waist or bias drape, and a flowing midi-to-ankle hem. Require quality fabric behavior (matte silk, fluid crepe, soft viscose satin, or lined chiffon as appropriate), realistic seams and hems, and stable footwear.

Give all four variants a distinct silhouette, neckline, sleeve/shoulder treatment, primary color, fabric, length, and footwear; no repetitive black dress. The four variants:

1. **Ink Cowl** — ink-blue wide-band cowl-neck fluid satin midi, softly defined waist, low dark leather sandals.
2. **Smoky Rose Square** — muted smoky-rose square-neck bias crepe midi, wide shoulder straps, gentle A-line, silver-gray ballet flats.
3. **Deep Olive Wrap** — deep olive short-sleeve shallow wrap-V lined chiffon midi with a softly gathered waist, warm taupe low slingback flats.
4. **Night Plum Column** — night-plum wide-neck soft viscose column maxi with a side drape and a below-knee closed seam (not a slit), charcoal low-profile Mary Jane flats.

For each prompt write the canonical reference-identity preservation block from `ideas/README.md` **verbatim and complete**. Do not hardcode appearance details extracted from the reference photograph. Explicitly state adult status in the scene. Keep the prompt self-contained and in English. Include only specific Avoid clauses needed for prior observed risks: collage/multiple views, anatomy/hands, bad ukulele geometry, duplicated people/objects, readable text/logos, and the prohibited dress failures above. No trend URLs in prompts.

## Required output files

Write exactly these files, overwriting nothing outside this new run directory:

- `/home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision/prompts/01-ink-cowl.md`
- `/home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision/prompts/02-smoky-rose-square.md`
- `/home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision/prompts/03-deep-olive-wrap.md`
- `/home/natrial/_work/X/asset-prompts/163-night-ukulele-dress-revision/prompts/04-night-plum-column.md`

After writing, print a concise JSON object containing `conversation_id`, the four exact file paths, and a short statement that you read the inputs. Do not call any image generation tool.