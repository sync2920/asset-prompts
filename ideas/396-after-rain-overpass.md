# 396. 夕立あとの歩道橋

## 設計メモ

- **用途**: 夏の夕方投稿
- **比率**: 3:4 縦
- **見せ場**: 濡れた歩道橋に映る夕焼けと、雨上がりの風で動く髪・衣服
- **差し替え変数**: 夕焼けの色、雲の切れ方、傘の位置、歩行の瞬間
- **人物参照**: `../main/yukata-fireworks/178515459335a5.png`。明確に成人と判断できる。人物の同一性と体格だけを参照し、浴衣・髪飾り・花火は引き継がない。
- **既存案との差**: 261「夕立の一粒目」が降り始めを扱うのに対し、本案は雨が去った直後の水鏡、冷えた空気、橙色の残光を主役にする。歩道橋の長い導線と都市の遠景で、帰り道の余韻を加える。

## 完成プロンプト

```text
A highly detailed photorealistic editorial portrait of the adult person from the reference image.

Reference-image role: use the supplied image only to preserve the subject's identity and physique. Do not copy the yukata, hair ornament, fireworks, night setting, railing, or original pose.

3:4 aspect ratio. Infer apparent age from the reference image and preserve it.
Match the reference image exactly for gender presentation, ancestry, body shape and
lines, height impression, proportions, overall build, skin tone and texture, facial
features, hair, and all physical characteristics including chest and hip shape and
fullness. Reproduce the natural volume and silhouette of the bust and hips as seen
in the reference, kept accurate through the fit and drape of the clothing. Preserve
the subject's identity and physique faithfully without age-shifting, beautifying,
exaggerating, or reshaping. Never add or hardcode features that are not present in
the reference image — no invented hair colors, accessories, uniforms, or props.

Scene: A humid summer evening immediately after a brief rain shower. The subject is halfway across a quiet pedestrian overpass, pausing after noticing the sunset beyond the rooftops. The wet walkway reflects long bands of coral orange, muted violet, and deepening blue. Small droplets remain on the railings, while the distant city is softened by faint post-rain haze.

Pose: Capture a candid moment in mid-step. The body remains angled naturally along the walkway, with the face turned only slightly toward the glowing horizon, showing a calm three-quarter profile rather than a full turn toward the camera. One hand loosely carries a closed transparent umbrella beside the leg; the other rests near the railing without gripping it. The expression suggests a private moment of relief, as if the cooler air after the rain arrived at exactly the right time.

Outfit: A refined, fully opaque sleeveless rib-knit top in a soft neutral tone and high-waisted, fluid wide-leg trousers in a subdued cool color. The soft fabrics follow the natural body shape and drape from its outermost points without flattening or altering the reference physique. Nothing is held in front of the chest. The trousers and a few strands of hair move gently in the remaining breeze. Simple, practical summer footwear.

Lighting: Low evening sunlight breaks through the retreating clouds from behind and to one side, creating a fine warm rim around the hair and shoulders. Cool skylight fills the face evenly. Reflections from the wet ground add subtle amber light from below. Keep the sunset luminous but natural, with controlled highlights, no heavy lens flare, and no artificial HDR glow.

Camera: Professional editorial photography, 85mm prime lens at f/2.0, photographed from chest height at a slight side angle. Shallow depth of field keeps the face, silhouette, umbrella droplets, and nearest railing crisp while the city becomes soft bokeh. Natural perspective and accurate anatomy.

Quality: Real skin pores, individual hair strands, visible rib-knit fibres, fine water droplets, scratched metal railings, and realistic reflections on wet concrete. Natural sensor grain, restrained color grading, no beauty filter, no SNS compression, no extra limbs, extra fingers, or malformed hands.

Variation rule: Generate four distinct versions while preserving the same subject and central concept. Vary only the exact walking instant, cloud opening, sunset balance, umbrella swing, and breeze in the hair and trousers.

Format: 3:4 vertical composition. Place the subject slightly off-center and preserve enough open sky and reflective walkway to make the post-rain evening atmosphere the second subject of the image.
```
