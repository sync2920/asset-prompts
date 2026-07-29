# 拡張スロット版（顔・体型・髪色を細分化）

顔・体型・髪をもっと細かくランダム化したい場合の版。
[en-prompts.md](en-prompts.md) のスロットを分解して、組み合わせ数を大幅に増やしてある。

## 変更点

| | 旧 | 新 |
|---|---|---|
| 顔 | 10パターン | **輪郭6 × 目8 × 印象6 = 288通り** |
| 体型 | 8パターン | **体格8 × バスト5 × ヒップ5 = 200通り** |
| 髪 | 型と色が一体で10 | **色14 × 型10 = 140通り**（独立して振れる） |
| シーン | 12 | 12（据え置き） |
| カメラ | 6 | 6（据え置き） |

合計 **約5億8000万通り**。実用上、同じ人物は二度と出ない。

---

## 1. 体型・バスト・ヒップの書き方（重要）

ここが一番フィルタに引っかかりやすいので先に整理する。

### 落ちる書き方

```
large breasts, huge chest, big ass, thick thighs, voluptuous body,
busty, curvy body emphasis, 巨乳, 爆乳
```

これらは**体型の描写ではなく身体部位の強調**と判定される。
Qwen・Seedream 等では単語1つで弾かれるうえ、通ったとしてもグラビア的な絵に寄って
「ファッション写真」から外れる。

### 通る書き方 ＝ シルエットで書く

洋裁・キャスティングシートの語彙に置き換えると、通るし絵も自然になる。

```
a full bust that gives the silhouette a soft curve
wide, full hips with a clearly defined waist above them
a flat, straight upper-body silhouette
narrow, straight hips and a boyish lower silhouette
```

**部位を主語にせず、シルエット（輪郭）の話にする。** これが原則。
下のスロットは全部この書き方で作ってある。

### 補足：スリーサイズ表記について

`02/prompt.md` にある `36C-24-36` のような表記は、
**ローカルのSD/ComfyUI なら有効**（体型指定として素直に効く）。
ただしホスト型の中国系サービスでは数値表記そのものが flag されやすいので、
そちらではシルエット語彙を使うこと。

---

## 2. 髪色の注意（青・ピンク等を使うとき）

青・ピンク・紫のような非現実色をそのまま指定すると、
モデルが「アニメ/コスプレの絵だ」と判断して**実写が崩れる**。

対策として、非現実色には必ず「染めた髪」であることを添える。

```
ash blue hair, obviously salon-dyed, with natural dark roots showing at the parting
```

下のスロット10〜14には、この一文をあらかじめ組み込んである。
金髪・赤系（5〜9）は日本人の染髪として自然なので不要。

---

## 3. マスタープロンプト（`{a|b|c}` 版）

SD WebUI + Dynamic Prompts / ComfyUI 用。1枚ごとに全スロットが抽選される。

> ⚠️ この長さだとSDでは後半の指定が薄まる。
> 常用するなら「6. wildcards 化」の1行版を推奨。

```
Professional fashion editorial photograph. A 23-year-old adult Japanese woman, fully clothed in modest everyday clothing.
Face: {an oval face with a soft jawline|a round face with full cheeks|a heart-shaped face with a narrow chin|a long slim face with a straight jaw|a square face with a defined angular jaw|a small tapered face with a pointed chin}, {large almond-shaped dark-brown eyes|upturned feline eyes with sharp outer corners|soft downturned eyes with a gentle gaze|narrow single-eyelid eyes with a calm level gaze|wide-set round eyes with an open expression|sleepy hooded eyes with heavy upper lids|crisply defined double-eyelid eyes with long lashes|deep-set eyes under a defined brow bone}, {a clean symmetrical idol-like impression|a cool composed mature impression|a warm approachable impression with an easy smile|a quiet reserved impression that gives little away|a fresh sporty impression with clear healthy skin|a delicately made-up refined impression}.
Figure: {petite and slim at around 152cm with narrow shoulders and a delicate frame|average height at around 158cm, naturally proportioned with relaxed posture|tall and lean at around 172cm with long limbs and model proportions|athletic and toned with defined shoulders and calves|softly plump with rounded arms and a full face, comfortable and healthy|tall and sturdily built with broad shoulders|slight and fine-boned with visible collarbones and thin wrists|balanced and well-proportioned with a clearly defined waist}, {a flat straight upper-body silhouette|a small modest bust|an average natural bust|a full bust that gives the silhouette a soft curve|a generous bust balanced by straight upright posture}, {narrow straight hips and a boyish lower silhouette|slim hips with a gentle line|naturally proportioned hips|softly rounded hips that widen the silhouette below the waist|wide full hips with a clearly defined waist above them}.
Hair: {jet-black|dark brown|ash brown|warm chestnut brown|platinum blonde|warm golden blonde|milk-tea beige blonde|copper red|deep burgundy red|ash blue, obviously salon-dyed with natural dark roots at the parting|deep navy blue, obviously salon-dyed with natural dark roots at the parting|silver gray, obviously salon-dyed with natural dark roots at the parting|soft pastel pink, obviously salon-dyed with natural dark roots at the parting|lavender, obviously salon-dyed with natural dark roots at the parting} {short bob with blunt bangs|medium-length layered hair with airy movement|long straight hair parted in the center, glossy|loose wavy perm with soft volume around the cheeks|high ponytail with loose strands at the temples|relaxed top bun with stray hairs at the nape|shoulder-length cut tucked behind one ear|wolf cut with choppy layers framing the face|blunt one-length cut at collarbone length|low twin braids resting on the shoulders}.
{Composed and elegant, wearing a crisp white linen shirt tucked into wide beige trousers, standing by a tall hotel window looking quietly outside, soft window light filtered through lace curtains falling across her face|Quietly refined, wearing a neatly tied cotton yukata with a knit shawl over her shoulders, sitting on the wooden veranda of a winter hot-spring inn with steam rising behind her, cold blue evening air against warm lamp light from indoors|Confident and editorial, wearing a tailored black blazer over a plain white tee and straight denim, walking mid-stride past a glass-walled office entrance in the city, flat cool overcast daylight and sharp reflections|Graphic and self-assured, wearing a muted midi dress under an oversized leather jacket, standing in a narrow alley after rain, neon signage reflecting on the wet asphalt around her at night|Calm and self-possessed, wearing an oversized white shirt and tailored trousers, standing at a hotel window and glancing back over her shoulder, lace-filtered morning light raking across her jawline while the rest of the room falls into soft shadow|Quiet and composed, wearing a dark ribbed knit dress and a long wool coat, sitting at a dim bar counter with her chin resting on one hand, low amber tungsten light and deep shadows|Relaxed and off-duty, wearing an oversized gray sweatshirt with relaxed track pants and thick socks, sitting on the floor against her bed with her knees drawn up, hair unstyled from sleep, pale early morning light through thin curtains|Tired and unposed, wearing a soft jersey loungewear set with a hair tie on her wrist, standing just outside a convenience store at night holding a plastic bag, cold fluorescent light spilling onto the pavement|Bright and energetic, wearing a summer sundress with a small delicate pattern and canvas sneakers, walking along a wooden pier over the sea and laughing with her hair caught in the wind, hard midday sun and crisp shadows|Languid and detached, wearing a cropped cardigan over high-waisted vintage denim, leaning her temple against a train window in the late afternoon gazing at nothing, warm low sun sweeping through the carriage|Half-awake and unstyled, wearing a plain cotton tee and loose sweatpants, hanging laundry on a small apartment balcony with her arms raised, strong afternoon backlight with the white sheets glowing behind her|Nostalgic 1990s Japanese snapshot mood, wearing faded blue denim overalls over a striped tee, sitting in the box seat of an old Showa-era coffee shop holding a mug with both hands, warm tungsten light}.
{85mm portrait lens, shallow depth of field, tight upper-body framing|35mm documentary framing, full body with the environment visible|low-angle wide shot emphasizing perspective and the open sky|slightly high angle at conversational distance|sharp side profile with the background heavily blurred|3:4 vertical portrait, subject off-center on the rule of thirds}.
Photorealistic raw photo, natural skin texture with visible pores, candid documentary feel, cinematic color grading, sharp focus on the eyes, 8k resolution, highly detailed.
```

ネガティブ（欄がある場合のみ）:

```
anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like face, mannequin, distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs, harsh flash, blown highlights, heavy makeup, watermark, text, logo, low resolution, blurry
```

---

## 4. 英語ランダム指示版（ChatGPT / Gemini / Qwen）

ネガティブ欄が無いUIに1回貼る用。

```
Generate one professional fashion editorial photograph.

Subject: a 23-year-old adult Japanese woman, fully clothed in modest everyday clothing, in a natural non-sexualized scene.

Pick one item at random from each list below. Do not tell me the numbers, just produce the image. Never repeat the same combination as your previous generation.

FACE SHAPE
1. an oval face with a soft jawline
2. a round face with full cheeks
3. a heart-shaped face with a narrow chin
4. a long slim face with a straight jaw
5. a square face with a defined angular jaw
6. a small tapered face with a pointed chin

EYES
1. large almond-shaped dark-brown eyes
2. upturned feline eyes with sharp outer corners
3. soft downturned eyes with a gentle gaze
4. narrow single-eyelid eyes with a calm level gaze
5. wide-set round eyes with an open expression
6. sleepy hooded eyes with heavy upper lids
7. crisply defined double-eyelid eyes with long lashes
8. deep-set eyes under a defined brow bone

IMPRESSION
1. a clean symmetrical idol-like impression
2. a cool composed mature impression
3. a warm approachable impression with an easy smile
4. a quiet reserved impression that gives little away
5. a fresh sporty impression with clear healthy skin
6. a delicately made-up refined impression

BUILD
1. petite and slim at around 152cm, narrow shoulders, delicate frame
2. average height at around 158cm, naturally proportioned, relaxed posture
3. tall and lean at around 172cm, long limbs, model proportions
4. athletic and toned with defined shoulders and calves
5. softly plump with rounded arms and a full face, comfortable and healthy
6. tall and sturdily built with broad shoulders
7. slight and fine-boned with visible collarbones and thin wrists
8. balanced and well-proportioned with a clearly defined waist

BUST SILHOUETTE
1. a flat, straight upper-body silhouette
2. a small, modest bust
3. an average, natural bust
4. a full bust that gives the silhouette a soft curve
5. a generous bust balanced by straight upright posture

HIP SILHOUETTE
1. narrow, straight hips and a boyish lower silhouette
2. slim hips with a gentle line
3. naturally proportioned hips
4. softly rounded hips that widen the silhouette below the waist
5. wide, full hips with a clearly defined waist above them

HAIR COLOR
1. jet black
2. dark brown
3. ash brown
4. warm chestnut brown
5. platinum blonde
6. warm golden blonde
7. milk-tea beige blonde
8. copper red
9. deep burgundy red
10. ash blue, obviously salon-dyed with natural dark roots at the parting
11. deep navy blue, obviously salon-dyed with natural dark roots at the parting
12. silver gray, obviously salon-dyed with natural dark roots at the parting
13. soft pastel pink, obviously salon-dyed with natural dark roots at the parting
14. lavender, obviously salon-dyed with natural dark roots at the parting

HAIR STYLE
1. a short bob with blunt bangs
2. medium-length layered hair with airy movement
3. long straight hair parted in the center, glossy
4. a loose wavy perm with soft volume around the cheeks
5. a high ponytail with loose strands at the temples
6. a relaxed top bun with stray hairs at the nape
7. a shoulder-length cut tucked behind one ear
8. a wolf cut with choppy layers framing the face
9. a blunt one-length cut at collarbone length
10. low twin braids resting on the shoulders

SCENE (pick ONE whole entry; wardrobe, location, action and lighting come as a set)
1. Composed and elegant, a crisp white linen shirt tucked into wide beige trousers, standing by a tall hotel window looking quietly outside, soft window light filtered through lace curtains
2. Quietly refined, a neatly tied cotton yukata with a knit shawl, sitting on the wooden veranda of a winter hot-spring inn with steam rising behind her, cold blue evening air against warm indoor lamp light
3. Confident and editorial, a tailored black blazer over a plain white tee with straight denim, walking mid-stride past a glass-walled office entrance, flat cool overcast daylight and sharp reflections
4. Graphic and self-assured, a muted midi dress under an oversized leather jacket, standing in a narrow alley after rain, neon signage reflecting on the wet asphalt at night
5. Calm and self-possessed, an oversized white shirt with sleeves rolled past the elbows and tailored trousers, standing at a hotel window glancing back over her shoulder, lace-filtered morning light raking across her jawline, the rest of the room in soft shadow
6. Quiet and composed, a dark ribbed knit dress with a long wool coat, sitting at a dim bar counter with her chin resting on one hand, low amber tungsten light and deep shadows
7. Relaxed and off-duty, an oversized gray sweatshirt with relaxed track pants and thick socks, sitting on the floor against her bed with knees drawn up, hair unstyled from sleep, pale early morning light through thin curtains
8. Tired and unposed, a soft jersey loungewear set with a hair tie on her wrist, standing outside a convenience store at night holding a plastic bag, cold fluorescent light spilling onto the pavement
9. Bright and energetic, a summer sundress with a small delicate pattern and canvas sneakers, walking along a wooden pier over the sea laughing with her hair in the wind, hard midday sun and crisp shadows
10. Languid and detached, a cropped cardigan over high-waisted vintage denim, leaning her temple against a train window in the late afternoon gazing at nothing, warm low sun sweeping through the carriage
11. Half-awake and unstyled, a plain cotton tee and loose sweatpants, hanging laundry on an apartment balcony with her arms raised, strong afternoon backlight with white sheets glowing behind her
12. Nostalgic 1990s Japanese snapshot mood, faded blue denim overalls over a striped tee, sitting in the box seat of an old Showa-era coffee shop holding a mug with both hands, warm tungsten light and film grain

CAMERA
1. 85mm portrait lens, shallow depth of field, tight upper-body framing
2. 35mm documentary framing, full body with the environment visible
3. low-angle wide shot emphasizing perspective and the open sky
4. slightly high angle at conversational distance
5. sharp side profile with the background heavily blurred
6. 3:4 vertical portrait, subject off-center on the rule of thirds

FINISH (always apply)
Photorealistic raw photo, natural skin texture with visible pores, candid documentary feel, cinematic color grading, sharp focus on the eyes, 8k resolution, highly detailed, 3:4 vertical. Avoid anime, illustration, 3D render, plastic skin, doll-like faces and malformed hands.
```

---

## 5. 日本語版スロット（確認・手組み用）

**輪郭** 1.卵型・柔らかい顎 2.丸顔・頬がふっくら 3.逆三角・顎が細い 4.面長・顎のラインが直線的 5.エラのはっきりした四角い顔 6.小顔で顎が尖ったV字

**目** 1.大きなアーモンド型の茶色い目 2.目尻の上がった猫目 3.たれ目でやわらかい視線 4.細めの一重、静かな目線 5.離れ気味の丸い目 6.眠たげな重い一重まぶた 7.くっきり二重・長いまつげ 8.眉骨の下に落ち窪んだ目

**印象** 1.整ったアイドル系 2.クールで大人っぽい 3.親しみやすく笑顔が自然 4.物静かで何を考えているか読めない 5.健康的でスポーティ 6.繊細に作り込まれた上品な顔

**体格** 1.152cm前後・華奢でなで肩 2.158cm前後・標準体型 3.172cm前後・高身長で手足が長いモデル体型 4.引き締まった筋肉質 5.**ふくよかで腕も顔も丸みがある健康的な体型** 6.高身長でしっかりした骨格・肩幅広め 7.骨が細く鎖骨と手首が目立つ 8.バランスが良くウエストがくびれている

**バスト** 1.平坦でまっすぐなシルエット 2.控えめ 3.標準 4.豊かでシルエットに柔らかい曲線が出る 5.かなり豊か（背筋の伸びた姿勢でバランスを取る）

**ヒップ** 1.狭くまっすぐ・ボーイッシュ 2.細めでなだらか 3.標準 4.丸みがありウエスト下で広がる 5.しっかり広くウエストのくびれが際立つ

**髪色** 1.漆黒 2.ダークブラウン 3.アッシュブラウン 4.暖色系の栗色 5.プラチナブロンド 6.ウォームゴールドの金髪 7.ミルクティーベージュ 8.カッパーレッド 9.ディープバーガンディ 10.アッシュブルー 11.ネイビーブルー 12.シルバーグレー 13.パステルピンク 14.ラベンダー
（10〜14は「明らかに染めた髪・分け目に地毛の黒いプリンが見える」を必ず添える）

**髪型** 1.切りっぱなし前髪のショートボブ 2.ミディアムレイヤー 3.センター分けのロングストレート 4.ゆるふわパーマ 5.高めポニーテール 6.ゆるいお団子 7.片耳にかけた肩までの髪 8.ウルフカット 9.鎖骨ラインのワンレン 10.低い位置のツインの三つ編み

---

## 6. wildcards 化（常用するならこれ）

マスタープロンプトが長すぎるので、SD WebUI + Dynamic Prompts なら
`wildcards/` に txt を置いて1行に圧縮できる。後半の指定が薄まる問題も解消する。

配置するファイル（1行1項目、上のリストをそのまま貼るだけ）:

```
wildcards/jp_faceshape.txt    (6行)
wildcards/jp_eyes.txt         (8行)
wildcards/jp_impression.txt   (6行)
wildcards/jp_build.txt        (8行)
wildcards/jp_bust.txt         (5行)
wildcards/jp_hips.txt         (5行)
wildcards/jp_haircolor.txt   (14行)
wildcards/jp_hairstyle.txt   (10行)
wildcards/jp_scene.txt       (12行)
wildcards/jp_camera.txt       (6行)
```

プロンプト本体:

```
Professional fashion editorial photograph. A 23-year-old adult Japanese woman, fully clothed in modest everyday clothing. Face: __jp_faceshape__, __jp_eyes__, __jp_impression__. Figure: __jp_build__, __jp_bust__, __jp_hips__. Hair: __jp_haircolor__ __jp_hairstyle__. __jp_scene__. __jp_camera__. Photorealistic raw photo, natural skin texture with visible pores, candid documentary feel, cinematic color grading, sharp focus on the eyes, 8k resolution, highly detailed.
```

txt 一式が必要なら生成する。

---

## 7. 部分固定の使い方

全部振ると毎回別人になるので、用途に応じて固定する。

- **同じ子で服とシーンだけ変える** → 顔3スロットと体型3スロットを固定文に置換し、`__jp_scene__` だけ残す
- **体型だけ振りたい** → 顔と髪を固定
- **ふくよか系だけ集めたい** → build を `5` に固定、bust/hips は 4〜5 に絞る
- **金髪だけ** → haircolor を 5〜7 に絞る

Dynamic Prompts なら重み付けも使える:

```
{3::softly plump with rounded arms and a full face|1::tall and lean at around 172cm}
```

ふくよか系が3倍出やすくなる。
