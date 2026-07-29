# 151〜180 — 「次の型」を狙う新しい画像生成フォーマット30

壁の黒線ドゥードル、画風変換、フィギュア箱、粘土化、単純な分身や影絵の派生ではなく、**実写人物をフォトリアルのまま残し、写真・空間・光・素材の物理法則を一つだけ壊す**ことを共通ルールにした完成プロンプト集。

## 共通方針

- 参照画像だけを、人物の見かけの年齢、性別表現、民族的特徴、顔、髪、肌、体型、身体のライン、身長感、比率、見えるアクセサリー、衣装、全体的な雰囲気の根拠にする。
- 参照に存在しない固有の髪色、髪飾り、身体特徴、キャラクター設定をハードコードしない。
- 若返り、加齢、美化、体型変更、身体比率の誇張、別人化を行わない。
- 人物をイラストや別素材へ変換せず、毎回「壊す法則」を一つに絞る。ほかの部分は高品質な実写写真として自然に保つ。
- 一枚を見た瞬間に仕組みが伝わり、人物、素材、場所、色など一つの変数を差し替えてシリーズ化できる構成にする。
- 色気を含む178〜180は、参照人物が明確に成人と判断できる場合だけ上品で非露骨なファッション表現として使用する。年齢が不明、または未成年に見える場合は、同じ視覚構造を保った健全な衣装・構図へ切り替える。
- 全案で文字、ロゴ、ウォーターマーク、余分な手足や指、不自然な関節、重複人物、参照外のアクセサリーを避ける。

## 各案の読み方

- **固定ルール:** そのシリーズを同じ型として認識させる不変部分
- **差し替え変数:** 投稿ごとに変えて量産できる部分
- **見せ場:** サムネイルでも意味が通じる中心的な視覚
- 英語プロンプトは、それぞれ単体でコピーして使用できる。

---

## A. 写真の物理法則を壊す（151〜160）

### 151. 接触感染ポートレート
- **比率:** 4:5
- **固定ルール:** 人物が触れた一点を境に、人物と対象物の表面だけが双方向へ侵食する。
- **差し替え変数:** タイル、木、花、氷、金属、雲など、触れる対象と移る質感。
- **見せ場:** 指先の接点から、壁の質感と服の織り目が互いの領域へ広がる境界。

```text
Create a high-resolution photorealistic surreal portrait using the uploaded reference image as the sole source for the subject. Infer and faithfully preserve apparent age, gender presentation, ancestry, facial identity and proportions, eyes, nose, lips, skin tone and texture, hairstyle and color, body shape and lines, height impression, proportions, visible accessories, outfit, and overall recognizable presence. Do not beautify, age-shift, reshape, or substitute the person.

Scene: a clean contemporary interior with a pale glazed-tile wall and a neutral floor. The subject stands close to the wall and touches one tile with the fingertips of one hand. At that single contact point, the tile glaze and geometric grout pattern spread organically across only the contacted fingertips, forearm, and one section of the reference outfit, while the outfit's exact fabric weave and sampled color spread in the opposite direction across the wall. Preserve the outfit's original silhouette, coverage, fit, and styling; only the surface material crosses the boundary. Keep the face, hair, exposed skin away from the contact point, body, pose, and the rest of the room completely photorealistic and unchanged.

Hero visual: one crisp bidirectional material-exchange boundary centered on the fingertips. The effect is tactile and elegant, never diseased, injured, melted, or horrific. Soft directional daylight, realistic contact shadows, 50mm lens, full or three-quarter body framing. Format: 4:5 portrait. Exactly one person, two natural hands, no extra limbs or fingers, no duplicate subject, no text, logo, watermark, doodle, cartoon, or ordinary cast-shadow gimmick.
```

### 152. 物性トレード
- **比率:** 3:4
- **固定ルール:** 人物と隣接する物体は形を保ち、材質の性質だけを交換する。
- **差し替え変数:** 布と石、髪と水、ガラスと煙、革と花弁などの組み合わせ。
- **見せ場:** 服は石の形状ではなく「石になった服」、壁は布の形状ではなく「布になった壁」として成立する。

```text
Create a highly detailed photorealistic fashion portrait from the uploaded reference image. Use the reference alone to preserve the subject's apparent age, gender presentation, ancestry, exact facial identity and proportions, eyes, nose, lips, skin, hairstyle and color, physique, body lines, height impression, visible accessories, clothing silhouette, coverage, fit, colors, and styling. Never beautify, age-shift, exaggerate, reshape, or replace the subject.

Scene: a minimalist gallery with one large pale stone wall. Apply one impossible rule only: the reference outfit and the wall have exchanged material properties while keeping their original shapes. The subject's clothing retains the exact cut, seams, folds, coverage, and fit seen in the reference, but its surface is now convincing carved limestone with subtle pores and weight. The wall retains its flat architectural shape, yet its entire surface behaves like soft woven fabric, sagging into broad realistic folds toward the floor. The person's face, skin, hair, body, pose, accessories, shoes, and anatomy remain fully natural and photorealistic.

Hero visual: the stone garment and cloth wall appear in the same frame so the material trade is understood instantly. Soft museum daylight, restrained neutral palette, realistic material response and shadows, 65mm full-length portrait. Format: 3:4. No statues, mannequins, second person, body hardening, cracked skin, horror, text, logo, watermark, extra limbs, bad hands, or unrelated surreal effects.
```

### 153. 重力の折り目
- **比率:** 4:5
- **固定ルール:** 部屋に一つだけ明確な折り目があり、その両側で重力方向が異なる。
- **差し替え変数:** 折る場所、角度、人物のポーズ、左右に置く小物。
- **見せ場:** 人物は一つの正常な身体のまま、髪と衣服の落下方向が折り目を境に変わる。

```text
Create a polished photorealistic surreal portrait of the person in the uploaded reference image. Preserve apparent age, gender presentation, ancestry, exact face and facial proportions, eyes, nose, lips, skin tone and texture, hairstyle and color, physique, height impression, body proportions, visible accessories, and the reference outfit exactly. Do not beautify, reshape, age-shift, or invent character details.

Scene: a simple cream-colored room that has been folded once like a thick sheet of paper, creating one clean ninety-degree crease across the architecture. The subject bridges the crease in a graceful, anatomically possible pose: both feet and the entire body remain connected and correctly proportioned, but the two sides of the room obey different gravity directions. Below the crease, shoes and loose objects fall toward the normal floor. Above the crease, the ends of the subject's hair, loose fabric, and a few lightweight objects fall sideways toward the adjacent wall. Do not split, bend, or deform the body itself.

Hero visual: one unmistakable architectural fold and two clearly different gravity directions, with everything else realistic. Soft natural window light, precise contact shadows, clean editorial composition, 45mm full-body view. Format: 4:5 portrait. No floating body parts, duplicate person, broken anatomy, impossible joints, extra limbs, text, logo, watermark, illustration, doodle, or multiple competing effects.
```

### 154. ピントを脱ぐ人
- **比率:** 4:5
- **固定ルール:** 被写界深度を半透明の薄膜として身体から脱ぐことができる。
- **差し替え変数:** 膜を脱ぐ位置、膜内のボケ量、背景、衣装。
- **見せ場:** 手でつまんだ膜の内側だけが強くボケ、その後ろの現実は鮮明に戻っている。

```text
Create a sophisticated photorealistic portrait using the uploaded reference as the only identity and styling source. Preserve the subject's apparent age, gender presentation, ancestry, face, facial proportions, eyes, nose, lips, skin, hairstyle and color, physique, height impression, body proportions, visible accessories, and reference clothing without beautification, age change, reshaping, or substitution.

Scene: a quiet daylight studio with a detailed but uncluttered background of shelves, plants, and a window. The subject is gently peeling a large transparent optical membrane from one shoulder with one natural hand, as if removing a thin shawl. This membrane is not fabric and is not a duplicate body: it is the physical embodiment of shallow depth of field. Every part of the background seen through the lifted membrane is strongly and naturally out of focus, while the same background immediately outside it is razor sharp. The subject's face, body, hair, and outfit remain fully sharp and unchanged. The membrane has a subtle edge highlight and realistic tension but no printed image.

Hero visual: the viewer can compare blurred and sharp versions of the same background across one lifted transparent sheet. Clean side light, realistic refraction, 70mm three-quarter portrait. Format: 4:5. No motion blur on the subject, no transparent clothing, no skin exposure changes, no second face, duplicate person, extra hands, text, logo, watermark, cartoon, or generic glass panel.
```

### 155. 光沢の抜け殻
- **比率:** 3:4
- **固定ルール:** 人物の形ではなく、表面のハイライトだけが剥がれて独立する。
- **差し替え変数:** サテン、革、髪、ジュエリーなど光沢を抜く対象と、浮かせる方向。
- **見せ場:** マットになった実物の隣に、銀色の薄いハイライトだけが立体的に浮遊する。

```text
Create a high-end photorealistic beauty and fashion portrait from the uploaded reference image. Preserve the subject's apparent age, gender presentation, ancestry, exact identity, facial geometry, eyes, nose, lips, skin tone and texture, hairstyle and color, body shape and lines, proportions, height impression, visible accessories, and reference outfit. Do not beautify, age-shift, reshape, or change the styling.

Scene: a dark neutral studio with one large soft light. Apply one surreal rule: specular highlights have peeled away from selected surfaces of the subject while the physical person remains intact. The hair, one glossy section of the reference outfit, and visible jewelry become unusually but realistically matte. Beside them float several paper-thin silver highlight fragments matching only the original curved streaks of reflected light—not the person's full silhouette, face, skin, or body. The fragments hover a few centimeters away and cast delicate realistic shadows onto the floor and background.

Hero visual: a fully photoreal person with matte surfaces beside an airy three-dimensional shell made only from extracted light. Controlled beauty lighting, precise silver reflections, 85mm three-quarter portrait, refined negative space. Format: 3:4. No metallic skin, body duplication, ghost, shadow twin, wings, liquid metal transformation, extra limbs, bad hands, text, logo, or watermark.
```

### 156. 多重重力ファッション
- **比率:** 3:4
- **固定ルール:** 身体と部屋は通常の重力に従い、既存の衣服のゆるい部分だけが三方向の重力へ分かれる。
- **差し替え変数:** 重力の角度、衣服のどの部分を担当させるか、背景色。
- **見せ場:** 一着の服が縫い目で切れずに、下・左上・右上へ自然に垂れている。

```text
Create a high-fashion photorealistic full-body portrait from the uploaded reference image. Treat the reference as the sole source for apparent age, gender presentation, ancestry, facial identity and proportions, eyes, nose, lips, skin, hairstyle and color, body shape and lines, height impression, visible accessories, and the exact outfit. Preserve the outfit's design, coverage, fit, colors, seams, and styling; do not invent extra fabric, redesign it, beautify the subject, alter age, or reshape the body.

Scene: a clean monochrome studio. The person, hair, floor, and room obey normal downward gravity. Only the already-existing loose portions of the outfit obey three simultaneous gravity directions: the main garment falls naturally downward, one suitable loose edge lifts and drapes toward the upper left, and another suitable loose edge drapes toward the upper right. The garment remains one continuous wearable piece with plausible tension radiating from its real seams and attachment points. Tight sections stay on the body and preserve coverage.

Hero visual: three clearly readable gravity vectors expressed by one unchanged outfit around one normal human body. Crisp editorial lighting, realistic fabric weight and shadows, 55mm lens, full body including shoes. Format: 3:4 portrait. No levitating body, flying hair, added cape, extra sleeves, exposed body, duplicate person, extra limbs, bad hands, text, logo, watermark, or unrelated surreal effects.
```

### 157. パーソナル重力場
- **比率:** 3:4
- **固定ルール:** 人物は変形せず、周囲の空間だけが人物の輪郭へ引き寄せられる。
- **差し替え変数:** グリッド、紙片、カーテン、砂など、曲がりを可視化する背景素材。
- **見せ場:** 人物の近くほど大きく湾曲し、画面端では正常に戻る背景。

```text
Create a photorealistic full-body portrait using the uploaded reference image as the only identity, body, hair, accessory, and wardrobe source. Preserve apparent age, gender presentation, ancestry, exact facial identity and proportions, skin, hairstyle and color, physique, height impression, body lines, visible accessories, and outfit. Do not beautify, age-shift, reshape, stretch, or replace the person.

Scene: a minimal pale room with a precise square-tile grid on the wall and floor, plus a few lightweight paper slips suspended in the air. The subject generates a localized personal gravity field. The grid lines, paper slips, curtain edge, and subtle light rays curve inward toward the subject's outer silhouette, with the curvature strongest within twenty centimeters of the body and gradually returning to straight, normal geometry at the frame edges. The subject's body, face, hair, outfit, and anatomy remain perfectly natural, rigidly undistorted, and in sharp focus.

Hero visual: the person appears to have real gravitational presence because the room bends toward them without touching or deforming them. Soft directional daylight, physically consistent refraction and shadows, 45mm full-body composition. Format: 3:4. Not a fisheye lens, liquify filter, vortex, black hole, aura, glow, duplicate, illustration, text, logo, watermark, extra limb, or bad hand.
```

### 158. 前後関係の編み替え
- **比率:** 4:5
- **固定ルール:** 人物と一枚の建築スクリーンの前後関係が、横方向の五帯だけ交互に入れ替わる。
- **差し替え変数:** スクリーンの素材、帯の太さ、人物のポーズ。
- **見せ場:** 同じ身体と同じ格子が連続したまま、「人物が前／格子が前」を五回だけ交互に繰り返す。

```text
Create a clean photorealistic surreal portrait from the uploaded reference. Faithfully preserve the subject's apparent age, gender presentation, ancestry, identity, facial proportions, eyes, nose, lips, skin, hair, body shape and lines, height impression, visible accessories, and exact outfit and styling. Do not beautify, alter age, change proportions, duplicate, or redesign the subject.

Scene: one person stands beside one continuous pale architectural lattice screen in a sunlit minimalist gallery. Rewrite only their occlusion order in exactly five broad horizontal bands from head to feet. In band one the person is visibly in front of the screen; in band two the same continuous screen is in front of the person; alternate this order through exactly five bands. Both the body and the screen remain physically continuous, correctly aligned, and anatomically intact across every boundary. The bands have no frames, gaps, seams, or color changes.

Hero visual: impossible woven depth created entirely by alternating front-and-back visibility, not by cutting the photograph. Soft museum daylight, precise edge occlusion, 70mm near-full-body view. Format: 4:5. No collage strips, sliced body, clone, mirror, portal, transparency, missing anatomy, extra limbs, text, logo, watermark, or other surreal effect.
```

### 159. 一人の身体・三つのカメラ
- **比率:** 3:4
- **固定ルール:** 一つの連続した身体を、頭・胴・脚だけ異なるカメラ位置と焦点距離で撮ったように統合する。
- **差し替え変数:** 三つの画角、接続位置、ポーズ。
- **見せ場:** 顔は正面、胴は斜め、脚は真横なのに、切れ目のない一人として成立する。

```text
Create a premium photorealistic editorial portrait using the uploaded reference image as the sole identity and styling source. Preserve apparent age, gender presentation, ancestry, exact face and facial proportions, skin, hairstyle and color, body shape and lines, height impression, visible accessories, and reference outfit without beautification, age change, body reshaping, or wardrobe replacement.

Show exactly one continuous person in one continuous room, but integrate three real camera viewpoints into the same uninterrupted body. Render the head and neck as if photographed frontally with an 85mm lens; the torso and arms as if photographed from a gentle three-quarter angle with a 50mm lens; and the hips, legs, and shoes as if photographed from a clean side angle with a 35mm lens. Blend the viewpoint transitions smoothly near the upper chest and hips so clothing seams, anatomy, light, and perspective connect without panels, cuts, repeated features, or misalignment. The pose should be natural and readable.

Hero visual: one recognizable person whose continuous anatomy contains three camera viewpoints. Neutral studio, soft window light, full body visible. Format: 3:4 portrait. No triptych, collage, cubist painting, multiple heads, duplicate limbs, twisted joints, panoramic distortion, text, logo, or watermark.
```

### 160. 色の沈殿
- **比率:** 4:5
- **固定ルール:** 生体以外の色だけが重力で沈み、物の下端へ堆積する。形・材質・明暗は変えない。
- **差し替え変数:** 室内、街、花畑などの場所と、沈殿させる色の組み合わせ。
- **見せ場:** 上部は自然に無彩色となり、服の裾や家具の脚元、床面に元の色が濃く積もる。

```text
Create a refined photorealistic portrait from the uploaded reference image. Preserve the subject's apparent age, gender presentation, ancestry, exact identity and facial proportions, natural skin, eye and lip colors, hairstyle and original hair color, physique, body lines, height impression, visible accessories, and exact outfit design and styling. Do not beautify, age-shift, reshape, or replace the subject.

Scene: a bright, orderly interior with several colored non-living objects. Apply one impossible law: chroma itself has weight and has slowly settled downward. On the outfit, furniture, walls, and props, the upper areas become naturally neutral gray while their original colors accumulate in increasingly saturated, thin sediment bands at hems, lower edges, furniture feet, and along the floor. Keep every object's form, texture, material, pattern, luminance, and shadow unchanged. Preserve all biological colors—skin, eyes, lips, and hair—exactly. Do not introduce any color not sampled from the original scene.

Hero visual: the viewer sees color pooled at the bottom of an otherwise fully realistic world. Soft clean daylight, accurate materials, 50mm three-quarter or full-body framing. Format: 4:5. No paint spill, liquid rainbow, dripping body, monochrome skin, color grading split, illustration, text, logo, watermark, duplicate, extra limbs, or bad hands.
```

---

## B. 画像そのものを物体化する（161〜170）

### 161. 世界の採取標本
- **比率:** 4:5
- **固定ルール:** 背景の一部を、現実と同じ縮尺・厚みのある縦長標本として手前へ引き出す。
- **差し替え変数:** 街、森、海岸、部屋などの採取場所と、切り出す位置。
- **見せ場:** 手前の標本と、背景に残った同形の空洞が遠近まで寸分違わず対応する。

```text
Create a high-resolution photorealistic full-body portrait using the uploaded reference as the sole source for the subject's apparent age, identity, facial proportions, skin, hair, physique, visible accessories, outfit, and styling. Preserve every recognizable detail and natural proportion; do not beautify, age-shift, reshape, or replace the person.

Scene: place the subject in a detailed real outdoor environment. A tall, narrow, full-scale cross-section slab of the surrounding world has been extracted and pulled exactly twenty centimeters toward the camera. The slab includes the same air, plants, ground, architecture, light, and depth that occupied that location; it is not a miniature, painting, jar, or diorama. The subject supports the lower edge naturally with both hands. Behind it remains one precisely matching vertical sampling slot, with correct perspective, parallax, and interrupted background lines. The slab and slot must align perfectly when mentally pushed back together.

Hero visual: one person physically holding a life-size sample of reality in front of the matching absence. Soft natural daylight, realistic thickness and contact shadows, 45mm full-body view. Format: 4:5. No portal, floating island, terrarium, duplicate person, severed body, collage frame, text, logo, watermark, extra limbs, or bad hands.
```

### 162. 景色を注ぐ人
- **比率:** 3:4
- **固定ルール:** 容器から液体ではなく、空・水平線・地面を含む完全な景色を連続して注ぐ。
- **差し替え変数:** 海岸、夜景、雪原、花畑などの景色と容器。
- **見せ場:** 注ぎ口から床まで続く細い景色が、着地点で本物の奥行きを持つ風景へ開く。

```text
Create a polished photorealistic full-body image from the uploaded reference. Faithfully preserve the subject's apparent age, identity, exact face, skin, hairstyle, body proportions, visible accessories, clothing, shoes, and overall styling. Do not beautify, reshape, age-shift, or invent personal details.

Scene: in a quiet neutral studio, the subject tips one clear glass pitcher with two natural hands. What pours from it is not water or paint but one continuous complete sunset coastline: sky at the top of the stream, a tiny level horizon through its center, moving sea below, and a narrow shore at its base. The stream descends without breaking and opens where it meets the floor into a slim but genuinely deep coastal landscape receding away from the subject. Show the pitcher, the entire stream, the landing point, and both feet clearly. Everything outside this single landscape flow remains a normal studio photograph.

Hero visual: a whole world retaining its horizon while being poured through a small spout. Warm sunset light from inside the landscape mixes realistically with soft studio daylight. Format: 3:4. No colored liquid, paint splash, waterfall dress, miniature model, portal ring, floating island, second person, text, logo, watermark, extra limbs, or malformed hands.
```

### 163. 自分の過去写真を着る
- **比率:** 4:5
- **固定ルール:** 一枚の写真そのものが、枠のない柔らかな布となって現在の人物の衣服の上へ巻かれる。
- **差し替え変数:** 使用する過去写真、巻き方、撮影場所。
- **見せ場:** 写真の場面と顔が、折り目やドレープに沿って立体的に曲がる。

```text
Use the uploaded reference image as the sole identity and wardrobe source for a high-quality photorealistic portrait. Preserve apparent age, exact facial identity and proportions, skin, hair, physique, visible accessories, and the original outfit underneath. Do not beautify, age-shift, reshape, or replace the person.

Create a current full-body portrait in a minimal daylight room. A separate supplied past photograph of the same person has become one flexible, borderless photographic cloth and is loosely wrapped once over the existing outfit like a removable sash or overskirt. The cloth must visibly reproduce the supplied past image, including its original perspective and colors, while bending naturally through folds and catching real light. It must not replace or alter the current outfit, skin, body, or identity. If no separate past photograph is supplied, print the current reference image on the cloth instead; never invent a younger face, childhood, event, or biography.

Hero visual: the present person literally wearing one intact photograph of themselves. 60mm full-body editorial framing, soft natural light. Format: 4:5. No Polaroid border, scrapbook, photo collage, face swap, duplicate living person, transparent clothing, text, logo, watermark, extra limbs, or bad hands.
```

### 164. キャンバス結び
- **比率:** 4:5
- **固定ルール:** 写真の左右端が幅広い帯として持ち上がり、画面中央で一度だけ結ばれる。
- **差し替え変数:** 背景、結び目の高さ、人物が持つ帯の端。
- **見せ場:** 平面だった景色が布のようにめくれ、人物と同じ空間で影を落とす大きな結び目。

```text
Create a photorealistic full-body portrait based strictly on the uploaded reference, preserving apparent age, exact identity and facial proportions, natural skin, hair, body shape and lines, visible accessories, outfit, footwear, and styling. Do not beautify, change age, reshape, or redesign the subject.

Scene: the person stands in a simple real location. One broad vertical strip of the photographed scene lifts inward from the left edge, and one matching strip lifts inward from the right edge, as if the image plane itself were flexible canvas. The two strips meet and form exactly one large, physically convincing knot at the center beside the person. The subject gently holds the two short tails of the knot with natural hands. The lifted strips retain the exact photographed scenery and perspective from their original positions; their reverse sides are plain neutral backing. The person remains in ordinary three-dimensional space, unchanged and unobscured.

Hero visual: the borders of the photograph tied together inside their own scene. Realistic canvas thickness, folds, tension, contact shadows, and soft daylight. Format: 4:5. No gift bow, portal, curtain, split screen, collage, duplicate subject, body wrapping, text, logo, watermark, extra limbs, or bad hands.
```

### 165. 現実を一針だけ縫う
- **比率:** 3:4
- **固定ルール:** 背景の空間にできた一か所の裂け目だけを、本物の針と糸で一針縫う。
- **差し替え変数:** 壁、空、霧などの背景と、糸の色、裂け目の位置。
- **見せ場:** 布ではない壁や空気が、縫い目の周囲だけ現実的に引きつれている。

```text
Create an elegant photorealistic portrait using the uploaded reference as the only source for the subject's apparent age, identity, face, skin, hair, body proportions, visible accessories, outfit, and styling. Preserve the person exactly without beautification, age change, reshaping, or wardrobe alteration.

Scene: a minimal pale interior with generous empty wall space. Beside—not on—the subject, there is one small clean tear in the background plane. The person holds one real oversized sewing needle and one continuous thick thread, completing exactly one visible stitch across that tear. Although the background is solid wall and air, it puckers subtly around the stitch like tensioned fabric while retaining plaster texture, depth, and normal lighting. The needle, thread, both hands, entry point, exit point, and single stitch are clearly readable. The person's body and clothing are untouched.

Hero visual: one calm human gesture repairing physical reality with a single stitch. Soft side daylight, precise macro-level material detail, near-full-body 65mm composition. Format: 3:4. No wound, blood, body sewing, horror, multiple stitches, embroidery scene, doodle line, portal, text, logo, watermark, duplicate, extra limbs, or bad hands.
```

### 166. 立体ピクセル摘出
- **比率:** 4:5
- **固定ルール:** 背景から一個だけ、画素が八センチ角の立方体として抜き取られる。
- **差し替え変数:** 抜く場所、背景、立方体が保持する色と景色。
- **見せ場:** 手の中の一画素と、背景に残った同じ色・同じ大きさの立方体状の穴。

```text
Create a high-detail photorealistic waist-up portrait from the uploaded reference image. Preserve the subject's apparent age, exact face and facial geometry, skin, hairstyle and color, physique, visible accessories, outfit, and styling. Do not beautify, age-shift, reshape, pixelate, or replace the person.

Scene: the subject stands before a richly textured but orderly real background. With one natural hand, they hold exactly one solid eight-centimeter cube extracted from the background beside their shoulder. The front surface of the cube contains exactly the color and tiny portion of scenery that occupied that location, while its side faces reveal realistic depth through the photographed environment. A precisely matching cubic socket remains in the background, with uninterrupted perspective lines proving where it came from. Everything else, especially the face, skin, hair, and clothing, remains continuous-resolution photography.

Hero visual: one physical pixel removed from an otherwise analog world. Soft daylight, crisp cube edges, realistic shadows and parallax, 85mm portrait. Format: 4:5. Exactly one cube and one socket; no pixelated face, mosaic, voxel body, Minecraft style, duplicate object, text, logo, watermark, extra fingers, or bad hands.
```

### 167. 現実の抜き型
- **比率:** 3:4
- **固定ルール:** 背景と空気を貫く一枚の形が、クッキー型のように正負一組で抜かれる。
- **差し替え変数:** 葉、鳥、鍵、花などの輪郭と、抜く位置。
- **見せ場:** 人物が持つ厚い「正の景色」と、背後に残る完全一致の「負の空白」。

```text
Create a polished photorealistic full-body portrait using the uploaded reference as the sole source for apparent age, identity, facial proportions, skin, hair, body shape, visible accessories, outfit, and styling. Preserve all recognizable details and do not beautify, age-shift, reshape, or replace the subject.

Scene: in a calm real environment, one large leaf-shaped slab has been cleanly punched through the background and the air in front of it. The subject holds the positive leaf-shaped piece with both natural hands. Its front shows the exact segment of the original scene, with convincing thickness along its edge. Behind it, the perfectly matching leaf-shaped negative opening remains in the original location and reveals only a quiet neutral unrecorded space—not another world. Background lines and lighting align exactly between the positive piece and the opening.

Hero visual: a matched positive and negative cutout of reality visible together beside one unchanged person. Soft natural daylight, clear depth, 50mm full-body view. Format: 3:4. No portal, mirror, miniature landscape, cardboard prop, body cutout, duplicate subject, text, logo, watermark, extra limbs, or malformed hands.
```

### 168. 透明レイヤー肖像
- **比率:** 4:5
- **固定ルール:** 一人分の写真情報を「色」「細部」「光と影」の三枚の透明層へ分離し、正面からだけ完全な人物に戻す。
- **差し替え変数:** レイヤー間隔、人物のポーズ、展示空間。
- **見せ場:** 斜めからは三枚、カメラ正面では参照人物が一人として精密に重なる。

```text
Create a refined mixed-media installation photograph using the uploaded reference as the only source for the subject's apparent age, identity, face, skin, hairstyle, body proportions, visible accessories, exact outfit, and styling. Preserve the person's natural appearance; do not beautify, age-shift, reshape, or invent details.

In a minimalist gallery, place exactly three frameless, perfectly clear, full-height transparent layers ten centimeters apart. Layer one carries only the subject's natural colors in soft translucent shapes. Layer two carries only fine information such as facial features, hair strands, fabric weave, seams, and accessories. Layer three carries only highlights, cast shadows, and tonal modeling. From the camera's selected viewpoint, all three layers align precisely to reconstruct one complete, photorealistic, recognizable person at full scale. A slight oblique glimpse at the layer edges reveals their physical separation. Do not show a separate real person outside the layers.

Hero visual: one portrait that exists only when three kinds of photographic information align. Soft gallery daylight, accurate transparent reflections, 70mm near-full-body composition. Format: 4:5. No duplicate faces, ghost, hologram, RGB glitch, UI panels, frames, text, logo, watermark, extra limbs, or anatomy errors.
```

### 169. 一本リボン宇宙
- **比率:** 3:4
- **固定ルール:** 人物が持つ一本のリボンの表面だけで、布から宇宙まで縮尺が連続変化する。
- **差し替え変数:** 始点の素材、途中の街、終点の天体風景。
- **見せ場:** 指先の布目が、道、都市、地球の大気、銀河へ切れずに発展する。

```text
Create a cinematic photorealistic full-body portrait based strictly on the uploaded reference. Preserve apparent age, exact facial identity and proportions, skin, hair, physique, body lines, visible accessories, outfit, and styling. Do not beautify, age-shift, reshape, or alter the person.

The subject stands in a clean dark studio holding the two ends of exactly one long, continuous ribbon. Along the ribbon's surface only, scale evolves smoothly from ordinary woven textile near the first hand, into a street seen from walking height, then an aerial city, then the curve of Earth's atmosphere, and finally a deep galaxy near the other end. Every stage flows continuously into the next without panels or hard cuts, and the ribbon retains consistent width, thickness, bends, and real fabric tension. All cities, planets, and stars remain confined inside the ribbon surface; the studio and person stay completely normal.

Hero visual: a single handheld strip containing a continuous journey from cloth scale to cosmic scale. Controlled rim light, realistic hand contact and shadows, 50mm full-body view. Format: 3:4. No floating planets outside the ribbon, multiple ribbons, portal, scarf transformation of the body, duplicate person, text, logo, watermark, extra arms, or bad hands.
```

### 170. UNDO写真
- **比率:** 4:5
- **固定ルール:** 写真内の一つの事故だけが逆再生され、人物と周囲の時間は通常のまま。
- **差し替え変数:** カップ、花瓶、紙袋など戻る物と、人物のリアクション。
- **見せ場:** 床から破片と滴が浮き上がり、空中で元の一個へ戻りつつある決定的瞬間。

```text
Create a high-speed photorealistic portrait using the uploaded reference as the sole source for the subject's apparent age, identity, facial proportions, skin, hair, physique, visible accessories, outfit, and styling. Preserve the person precisely without beautification, age alteration, reshaping, or wardrobe change.

Scene: in a bright minimal kitchen or studio, exactly one dropped ceramic cup and its spilled clear liquid are moving backward through time. Beneath the subject's open natural hand, ceramic fragments rise from the floor, rotate inward, and are midway through joining into one cup; droplets travel upward in clean trajectories toward the reforming rim. Show enough incomplete seams to make the reverse action obvious. The subject reacts with gentle surprise, while their hair, clothing, body, environment, dust, and every other object remain in ordinary forward time and natural gravity.

Hero visual: the unmistakable split second of a single accident undoing itself. Crisp daylight, frozen droplets, realistic ceramic edges, 70mm three-quarter framing. Format: 4:5. Exactly one cup; no rewind icon, clock, text, logo, watermark, duplicate person, multiple timelines, magical glow, extra limbs, or malformed hands.
```

---

## C. 見る人が参加する／ファッションへ展開する（171〜180）

### 171. 二距離ポートレート
- **比率:** 4:5
- **固定ルール:** 通常サイズでは自然な人物写真、縮小表示や遠目では画面全体が巨大な目になる。
- **差し替え変数:** 建築、家具、照明で作る目の形と、瞳になる人物の位置。
- **見せ場:** 描かれた目は一切ないのに、サムネイルへ縮めた瞬間だけ第二の像が現れる。

```text
Create a meticulously composed photorealistic environmental portrait using the uploaded reference as the only source for apparent age, exact identity and facial proportions, skin, hair, body shape and lines, visible accessories, outfit, and styling. Preserve the subject exactly; do not beautify, age-shift, reshape, or replace them.

Design one image that reads at two viewing distances. At normal size it is simply an elegant full-body portrait in a modern architectural interior with believable furniture, arches, window light, and negative space. When the complete image is viewed as a small thumbnail or from several meters away, those ordinary architectural elements collectively form one enormous calm human eye: curved ceiling and furniture edges suggest the eyelids, a circular pool of light suggests the iris, and the real subject stands naturally at its center as the pupil. The secondary eye must be created only through composition and tonal grouping, never painted, drawn, printed, or added as an object.

Hero visual: a normal portrait that reveals a second image only after shrinking. Balanced light-dark masses, clean negative space, 50mm lens. Format: 4:5. No literal giant eye, eye mural, face in clouds, collage, double exposure, duplicate person, text, logo, watermark, extra limbs, or bad hands.
```

### 172. 180度ポートレート
- **比率:** 1:1
- **固定ルール:** 正位置では一人の実写写真、画像を上下逆さまにすると背景だけで別の肖像が成立する。
- **差し替え変数:** 椅子、階段、植物、照明など、逆さの顔を構成する小道具。
- **見せ場:** スマートフォンを回転させる行為そのものが作品のオチになる。

```text
Create a square, rotation-responsive photorealistic portrait using the uploaded reference image as the sole source for the real subject's apparent age, exact face, skin, hair, physique, visible accessories, outfit, and styling. Keep exactly one real person and preserve their natural appearance without beautification, age change, reshaping, or replacement.

Upright orientation: the person poses naturally in a circular contemporary gallery among a curved chair, two short stair flights, restrained plants, and directional pools of light. It must read as a sophisticated ordinary portrait. Engineer the background arrangement so that after rotating the entire square image exactly 180 degrees, the chair, stairs, plant masses, and light patches combine through pareidolia into a second dignified human portrait. This inverted portrait must contain no real face and no single object shaped like a face; it exists only through the combined arrangement. Keep the real subject plausible in both orientations and away from critical facial features of the hidden image.

Hero visual: the viewer physically rotates the image and discovers a second portrait. Exact rotational composition, realistic materials and shadows. Format: 1:1. No second person, mirror, printed face, face mural, overlay, double exposure, text, logo, watermark, or anatomy errors.
```

### 173. 見えない何かを抱く写真
- **比率:** 4:5
- **固定ルール:** 抱かれている存在は完全に不可視で、周囲への物理的作用だけで体積と仕草を示す。
- **差し替え変数:** 大きさ、丸み、重さ、呼吸や動きの気配。
- **見せ場:** 腕の支え、袖の圧縮、髪の押し上げ、結露と滴だけで「そこにいる」と分かる。

```text
Create an intimate but fully clothed photorealistic portrait from the uploaded reference. Preserve the subject's apparent age, identity, facial proportions, natural skin, hairstyle, physique, visible accessories, outfit, and styling exactly. Do not beautify, age-shift, reshape, or expose additional skin.

The subject gently cradles one completely invisible, rounded living presence approximately the size of a large house cat. Do not render any body, silhouette, outline, glow, transparency, fur, eyes, or shadow for it. Reveal its volume only through physically consistent evidence: both forearms support a real unseen weight, one sleeve compresses at a contact point, a few hair strands are displaced upward, fine condensation and separate droplets cling to an unseen curved surface, and a nearby soft fabric cushion is indented. The person's expression is warm, curious, and believable; both hands and all fingers are naturally positioned.

Hero visual: viewers infer a lovable creature without ever seeing it. Soft window light, shallow depth of field, tactile detail, 70mm three-quarter view. Format: 4:5. No ghost, invisible-person outline, transparent animal, horror, floating props, extra limbs, text, logo, or watermark.
```

### 174. 奥行きで完成する隠し絵
- **比率:** 16:9
- **固定ルール:** 前景・中景・遠景の実物が、カメラの一点からだけ一つの巨大な図形へ揃う。
- **差し替え変数:** 蝶、花、鳥、仮面などの完成図形と、三層の素材。
- **見せ場:** 横から見れば無関係な物体が、正面の一視点で人物を中心に一枚絵になる。

```text
Create a wide photorealistic environmental portrait based strictly on the uploaded reference, preserving the subject's apparent age, exact identity, face, skin, hair, body proportions, visible accessories, outfit, and styling. Do not beautify, age-shift, reshape, or duplicate the person.

Build a real three-depth installation around the subject. In the near foreground, suspended translucent fabric arcs form only the outer tips of two wings. In the midground, separate curved branches and pale architectural panels form the central wing sections. In the distant background, natural window-light patches complete the inner markings. From one precise camera position, these unrelated physical elements align into one monumental butterfly surrounding the subject, who naturally becomes its central body. Their different focus, parallax, shadows, and scale must prove that the components occupy genuine foreground, midground, and background. Nothing is painted on a flat wall.

Hero visual: a hidden image completed by depth rather than drawing. Deep-focus cinematic daylight, subject full body and all wing edges visible. Format: 16:9. No mural, graphic overlay, collage, costume wings, actual giant butterfly, duplicate person, text, logo, watermark, or extra limbs.
```

### 175. 余白の第二肖像
- **比率:** 4:5
- **固定ルール:** 人物と小物の間に残る何もない空間だけで、横顔が形成される。
- **差し替え変数:** 椅子、植物、カーテン、腕など輪郭を作る要素と、横顔の向き。
- **見せ場:** 物ではなく「空白」を見た瞬間に、もう一人の横顔が現れる。

```text
Create a sophisticated photorealistic full-body portrait using the uploaded reference as the only source for the subject's apparent age, exact facial identity and proportions, skin, hair, physique, visible accessories, outfit, and styling. Preserve every recognizable feature without beautification, age change, reshaping, or substitution.

Place the subject in a minimal cream room with exactly one chair, one restrained plant, and one curtain. Compose the outer edge of the subject's pose, the chair back, selected leaf clusters, and one curtain fold so that the untouched blank wall between them forms a clean, readable side-profile portrait through negative space alone. The hidden profile should include forehead, nose, lips, chin, and neck, all made from the boundary of empty wall; do not place any eyes, marks, shadows, or objects inside it. At first glance the scene remains a believable editorial portrait.

Hero visual: a second face made entirely from absence. Soft even daylight, strong figure-ground separation, 65mm full-body view. Format: 4:5. No painted profile, silhouette person, cast-shadow face, reflection, collage, duplicate human, text, logo, watermark, extra limbs, or malformed hands.
```

### 176. 声の鋳造
- **比率:** 4:5
- **固定ルール:** 人物が発した一音を、波形ではない透明で重量のある立体として空間へ固定する。
- **差し替え変数:** 母音、声の強さ、ガラス・氷・樹脂などの透明素材。
- **見せ場:** 口元から生まれた複雑な音響地形が、台座へ重さを預けている。

```text
Create a high-end photorealistic portrait from the uploaded reference image. Preserve the subject's apparent age, exact identity and facial proportions, skin, hairstyle, body shape and lines, visible accessories, outfit, and styling. Do not beautify, age-shift, reshape, or replace the person.

Scene: in a quiet gallery, the subject is softly voicing one sustained open vowel. That single sound has been cast into a thick, clear, torso-sized glass acoustic topology extending from near the mouth and resting partly on a low stone plinth. Its form is an irregular three-dimensional pressure landscape with nested cavities, compressed ridges, and smooth interference surfaces derived from sound propagation; it is not a flat waveform, ribbon, text character, speech bubble, smoke, or decorative sculpture. The glass has convincing weight, refraction, caustics, and contact shadows. Keep the entire face visible and unobstructed.

Hero visual: an ephemeral voice behaving like a heavy transparent object. Soft museum daylight, realistic glass optics, 85mm three-quarter portrait. Format: 4:5. No visible letters, musical notes, neon wave, frozen breath, microphone, duplicate face, text, logo, watermark, extra limbs, or bad hands.
```

### 177. 空間の指紋
- **比率:** 3:4
- **固定ルール:** 指が触れた空気そのものに、巨大な指紋状のへこみが残る。
- **差し替え変数:** 指紋の大きさ、結露、埃、背景の模様。
- **見せ場:** 線を描かず、屈折と水滴だけで空間の凹凸として指紋が読める。

```text
Create a precise photorealistic portrait using the uploaded reference as the sole source for apparent age, exact identity, facial proportions, skin, hair, body proportions, visible accessories, outfit, and styling. Preserve the person naturally; do not beautify, age-shift, reshape, or substitute them.

Scene: the subject reaches one index fingertip into apparently empty air in a softly lit studio. At the contact point, empty space is physically indented into one giant torso-sized fingerprint relief, like a clear elastic membrane with no visible surface. Reveal the fingerprint ridges only through subtle background refraction, tiny condensation beads collecting along curved grooves, and delicate displaced dust particles. It must have real concave depth and perspective, strongest at the fingertip and fading cleanly at its outer boundary. Do not use drawn lines, ink, neon, projection, glass sheet, smoke, or a graphic overlay.

Hero visual: the person's small fingertip leaves a monumental tactile print in empty space. Raking daylight, crisp fingertip focus, 70mm three-quarter composition. Format: 3:4. No floating hand, extra fingers, aura, magic circle, text, logo, watermark, duplicate subject, or malformed anatomy.
```

### 178. 雨が見せる透明ドレス
- **比率:** 9:16
- **固定ルール:** 元の服は乾いたまま完全に保持し、その外側にある不可視の第二衣装を雨粒だけで見せる。
- **差し替え変数:** ガウン、コート、ケープなどの輪郭と、雨の強さ。
- **見せ場:** 空中で止まる雨粒と流れる水筋が、触れられない服の裾・袖・襟を描く。

```text
Create a tasteful, photorealistic vertical fashion portrait from the uploaded reference image. Use the reference alone to preserve the subject's apparent age, exact identity and facial proportions, natural skin, hairstyle, physique and body lines, visible accessories, original outfit, coverage, fit, and styling. Do not beautify, age-shift, reshape, change the original clothing, or reveal additional skin.

Scene: the subject stands in a clean outdoor rain shower, yet their original outfit, hair, and skin remain naturally dry. Around the outfit is a second completely invisible outer garment whose presence is shown only by rain beads resting on its unseen surface and thin streams flowing along its contours. If the reference clearly depicts an adult, make this invisible layer an elegant, non-revealing, floor-length couture gown with sculptural sleeves and a refined silhouette, floating several centimeters outside the original outfit. If adulthood is unclear, use a roomy, high-collar, long-sleeved, ankle-length invisible raincoat instead. The unseen garment never becomes transparent fabric; only water defines it.

Hero visual: rain draws an absent garment around an unchanged real person. Backlit soft daylight, crisp droplets, full body and complete hem visible. Format: 9:16. No wet-clinging clothing, nudity, see-through outfit, exposed body, body reshaping, water dress replacing the outfit, extra limbs, text, logo, or watermark.
```

### 179. 表裏同居ポートレート
- **比率:** 4:5
- **固定ルール:** 一人・一頭身・一つの身体のまま、顔と肩は正面、髪型と衣服だけは背面のディテールも同時に見える。
- **差し替え変数:** 背面の編み上げ、ボタン、リボン、髪のまとめ方など参照内で見える要素。
- **見せ場:** 鏡を使わず、一枚で服の前後を同時に読める違和感。

```text
Create a sophisticated photorealistic fashion portrait based solely on the uploaded reference. Preserve the subject's apparent age, exact identity, one face, one head, facial proportions, natural skin, hairstyle and color, one continuous body, visible accessories, and the exact outfit and styling. Do not beautify, age-shift, reshape, duplicate, or invent garment details not supported by the reference.

Show exactly one person in one seamless pose. The face, chest, and shoulders present naturally toward the camera, while the same continuous hairstyle and same continuous outfit simultaneously reveal their authentic back-facing construction—rear hair arrangement, back seams, closures, folds, or other details actually visible or safely inferable from the reference. Resolve the transition elegantly within fabric and hair flow, never by twisting flesh, adding a second head, reflecting the body, or creating another person. If the reference clearly depicts an adult, use restrained sensual couture lighting while keeping the original coverage; if age is unclear, use neutral high-coverage museum portrait lighting.

Hero visual: one believable person displaying the front and back grammar of the same styling at once. Clean studio, soft sculpting light, near-full-body 70mm view. Format: 4:5. No mirror, second face, rear face, extra torso, duplicated limbs, exposed back not present in the reference, text, logo, watermark, or anatomical distortion.
```

### 180. 触れないレースの第二衣装
- **比率:** 9:16
- **固定ルール:** 元の衣装を変えず、身体や布に一度も触れない空間構造だけで第二のレース衣装を作る。
- **差し替え変数:** レースの密度、外形、身体からの距離、光の色。
- **見せ場:** 五〜十五センチの空隙を保ったまま、人の動きに沿う自立したレースの殻。

```text
Create a premium photorealistic vertical fashion portrait using the uploaded reference as the sole source for the subject's apparent age, exact identity and facial proportions, natural skin, hairstyle, body shape and lines, visible accessories, original outfit, coverage, fit, and styling. Preserve everything recognizable without beautification, age shift, reshaping, wardrobe replacement, or additional exposure.

Around the person, construct one lace-like three-dimensional spatial garment made from extremely fine dark filaments suspended in air. It follows the general motion of the pose but remains five to fifteen centimeters away from the skin, hair, and original clothing at every point, with clearly visible air gaps. It never touches, wraps, prints onto, shadows into, or replaces the reference outfit. If the reference clearly depicts an adult, form an elegant, non-explicit spatial couture silhouette with a dramatic long hem and refined openwork density while preserving original coverage. If adulthood is unclear, form a roomy high-neck, long-sleeved floating cape and ankle-length outer shell. The filament structure casts real delicate shadows on the floor only.

Hero visual: a second garment made from organized empty space, orbiting an unchanged real person. Soft gallery rim light, full body and entire spatial hem visible. Format: 9:16. No embroidery on clothing, tattoo, body paint, projection, shadow twin, doodle, spiderweb bondage, nudity, transparent replacement outfit, extra limbs, text, logo, or watermark.
```
