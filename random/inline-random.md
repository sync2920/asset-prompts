# 画像生成AIに直接投げるランダムプロンプト

LLMに一度通さず、**生成AIのプロンプト欄にそのまま貼って、生成のたびに中身が変わる**形式。
ツールごとに仕組みが違うので3種類用意した。

| 形式 | 対象 | ランダムの実体 |
|---|---|---|
| ① `{a\|b\|c}` 版 | SD WebUI(A1111/Forge) + Dynamic Prompts、ComfyUI + 対応ノード | 1枚ごとに1つ抽選（本物のランダム） |
| ② `{a, b, c}` 版 | Midjourney | 全組み合わせを別ジョブとして一括生成 |
| ③ 自己完結文章版 | ChatGPT / Gemini / nano-banana 系 | モデル自身に選ばせる |

---

## 設計の肝：スロットを「束」にしてある

顔・体型・髪は何と組み合わせても破綻しないので独立スロットのまま。
一方、トーン・服・場所・仕草・光を独立にランダム化すると
「温泉旅館でテーラードブレザー」みたいな事故が必ず起きる。

なので **トーン＋服装＋場所＋仕草＋光を1つの「シーン束」にまとめて12種**用意し、
そこから1つ抽選する形にした。これで完全ランダムでも絵が破綻しない。

組み合わせ数 = 顔10 × 体型8 × 髪10 × シーン12 × カメラ6 = **57,600通り**

---

## ① `{a|b|c}` 版 — Stable Diffusion / Qwen-Image ほか

必要なもの:
- **A1111 / Forge**: 拡張機能「Dynamic Prompts」を入れる（Extensions → Available → sd-dynamic-prompts）
- **ComfyUI**: `comfyui-dynamicprompts` か Impact Pack の Wildcard Processor ノード
- 素の ComfyUI / 素のWebUI では `{}` はただの文字として扱われるので効かない

### 動作確認（先にこれを1回投げる）

```
a photo of a {red|green|blue} car
```

3回生成して色が変われば有効。全部同じ色なら拡張が入っていないか無効。

### 本体プロンプト

```
Photorealistic raw photo of a Japanese woman in her early 20s, {clean symmetrical idol-like features with large almond dark-brown eyes|cool mature features with sharp defined double eyelids and a high nose bridge|a round youthful face with soft downturned tareme eyes|feline upturned eyes and a small sharp chin|understated quiet features with single-eyelid eyes and minimal makeup|polished glass skin with straight brows and gradient lips|light freckles across her nose and a bare-faced natural look|high cheekbones and a long editorial face with strong bone structure|deep-set eyes and a defined brow line|a friendly open face with a small snaggletooth when she smiles}, {a slender petite build with narrow shoulders|a healthy natural build with relaxed posture|tall and long-limbed with an elongated silhouette|petite with a softly curved figure|an athletic toned build with defined shoulders|a soft gently rounded figure|a lean editorial model build with sharp collarbones|sloping shoulders and a fine delicate frame}, {jet-black short bob with blunt bangs|medium layered brown hair with airy movement|long glossy straight black hair center-parted|a loose wavy perm with soft volume around the cheeks|a high ponytail with loose strands at the temples|a messy top bun with stray hairs at the nape|dark hair with a hidden inner color peeking through|a wet-look wolf cut with damp strands framing her face|high-tone beige hair with slightly grown-out roots|shoulder-length hair pulled behind one ear}.
{Composed and elegant, wearing a crisp white linen shirt tucked into wide beige trousers, standing by a tall hotel window looking quietly outside, soft window light filtered through lace curtains falling across her face|Quietly refined, wearing a neatly tied cotton yukata with a knit shawl over her shoulders, sitting on the wooden veranda of a winter hot-spring inn with steam rising behind her, cold blue evening air against warm lamp light from indoors|Confident and editorial, wearing a tailored black blazer over a plain white tee and straight denim, walking mid-stride past a glass-walled office entrance in the city, flat cool overcast daylight and sharp reflections|Graphic and self-assured, wearing a muted midi dress under an oversized leather jacket, standing in a narrow alley after rain, neon signage reflecting on the wet asphalt around her at night|Calm and self-possessed, wearing an oversized white shirt and tailored trousers, standing at a hotel window and glancing back over her shoulder, lace-filtered morning light raking across her jawline while the rest of the room falls into soft shadow|Quiet and composed, wearing a dark ribbed knit dress and a long wool coat, sitting at a dim bar counter with her chin resting on one hand, low amber tungsten light and deep shadows|Relaxed and off-duty, wearing an oversized gray sweatshirt with relaxed track pants and thick socks, sitting on the floor against her bed with her knees drawn up, hair unstyled from sleep, pale early morning light through thin curtains|Tired and unposed, wearing a soft jersey loungewear set with a hair tie on her wrist, standing just outside a convenience store at night holding a plastic bag, cold fluorescent light spilling onto the pavement|Bright and energetic, wearing a summer sundress with a small delicate pattern and canvas sneakers, walking along a wooden pier over the sea and laughing with her hair caught in the wind, hard midday sun and crisp shadows|Languid and detached, wearing a cropped cardigan over high-waisted vintage denim, leaning her temple against a train window in the late afternoon gazing at nothing, warm low sun sweeping through the carriage|Half-awake and unstyled, wearing a plain cotton tee and loose sweatpants, hanging laundry on a small apartment balcony with her arms raised, strong afternoon backlight with the white sheets glowing behind her|Nostalgic 90s Japanese snapshot mood, wearing faded blue denim overalls over a striped tee, sitting in the box seat of an old Showa-era coffee shop holding a mug with both hands, warm tungsten light}.
{85mm portrait lens, shallow depth of field, tight upper-body framing|35mm documentary framing, full body with the environment visible|low-angle wide shot emphasizing perspective and sky|slightly high angle at intimate distance|sharp side profile with the background heavily blurred|3:4 vertical portrait, subject off-center on the rule of thirds}.
Photorealistic raw photo, natural skin texture with visible pores, authentic candid feel, cinematic color grading, sharp focus on the eyes, 8k resolution, highly detailed.
```

### ネガティブプロンプト（固定）

> ⚠️ **初版のネガティブは安全フィルタに弾かれる。** 詳細と修正版は [safe.md](safe.md) を参照。
> `minor` `nudity` 等は否定として解釈されず、そのまま検出対象になる。以下は差し替え済みの安全版。

```
anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like face, mannequin, distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs, harsh flash, blown highlights, heavy makeup, watermark, text, logo, low resolution, blurry
```

年齢・着衣の担保はネガティブではなく、**ポジティブ文の冒頭**で行う:

```
Professional fashion editorial photograph. A 23-year-old adult Japanese woman, fully clothed in modest everyday clothing, ...
```

### 回し方

- **Batch count を 8〜16 に上げて、Seed は -1（ランダム）** → 1クリックで全部違う子が出る
- Dynamic Prompts の「Combinatorial generation」を ON にすると全組み合わせを総当たりできる（数が爆発するので普段は OFF）
- 特定のトーンだけ回したい → シーン束から要らない選択肢を消すだけ

### 便利な追加構文

```
{2::A|1::B}        A が B の2倍出やすくなる（特定トーンを厚くしたい時など）
{1-2$$A|B|C}       1〜2個を選んで連結
__jp_face__        wildcards/jp_face.txt から1行ランダム抽選
```

毎回この長文を貼るのが面倒なら、各スロットを `wildcards/` 配下の txt に切り出して
`Photorealistic raw photo of a Japanese woman in her early 20s, __jp_face__, __jp_body__, __jp_hair__. __jp_scene__. __jp_camera__.`
の1行にできる。必要なら txt 一式も作る。

---

## ② `{a, b, c}` 版 — Midjourney

Midjourney の `{}` は**抽選ではなく全組み合わせを別ジョブとして生成する**（Permutation Prompts）。
組み合わせ数がそのままジョブ数になり、上限40。**束の中のカンマは `\,` でエスケープが必須**。

スロットを増やすとジョブ数が掛け算で爆発するので、実用上はシーン束の1スロットだけにするのが安全（下記＝6ジョブ）。

```
Professional fashion editorial photograph, a 23-year-old adult Japanese woman fully clothed in modest everyday clothing, natural skin texture, {an oversized white shirt with sleeves rolled past the elbows and tailored trousers\, standing at a hotel window glancing back over her shoulder\, lace-filtered morning light raking across her jawline, a crisp white linen shirt and wide beige trousers\, standing by a tall hotel window looking quietly outside\, soft diffused morning light, a tailored black blazer over a plain white tee\, walking mid-stride past a glass-walled office entrance\, flat cool overcast daylight, an oversized gray sweatshirt with track pants and thick socks\, sitting on the floor with her knees drawn up and hair unstyled from sleep\, pale early morning light, a summer sundress and canvas sneakers walking along a wooden pier over the sea\, laughing with her hair in the wind\, hard midday sun, faded denim overalls over a striped tee\, sitting in an old Showa-era coffee shop holding a mug\, warm tungsten light and film grain}, cinematic color grading, sharp focus on the eyes --ar 3:4 --style raw --no anime, illustration, 3d render, plastic skin, deformed hands, extra fingers, text, watermark
```

- 顔・体型・髪も変えたい場合は、そのぶんジョブ数が掛け算になる点に注意（6シーン × 3髪型 = 18ジョブ）
- 同じ設定でバリエーションだけ増やすなら `--repeat 4`（対応プランのみ）
- Midjourney は Seed 未指定なら毎回ランダムなので、同じプロンプトを再送するだけでも人物は変わる

---

## ③ 自己完結文章版 — ChatGPT / Gemini / nano-banana 系

これらは画像生成の前にモデルがプロンプトを読解するので、**「リストから1つランダムに選べ」という指示自体が効く**。1回貼るだけでよい。

```
以下の条件で写真を1枚生成してください。

各リストから毎回ランダムに1つずつ選んでください。選んだ番号は言わず、画像だけ出してください。
直前の生成と同じ番号は選ばないこと。

被写体: 20代前半の日本人女性（成人）

【顔】1.正統派で左右対称の整った顔、アーモンド型の大きな瞳 2.涼しげで大人っぽい二重、高い鼻筋 3.丸顔でたれ目、あどけない口元 4.猫目のつり目、小さく尖った顎 5.薄めの顔立ちで一重、メイクは最小限 6.ツヤ肌に平行眉、グラデーションリップ 7.鼻にうっすらそばかす、すっぴん感 8.高い頬骨と長い顔、骨っぽいモデル顔 9.彫りが深く眉骨がはっきりした顔 10.笑うと八重歯が見える親しみやすい顔

【体型】1.華奢で小柄、なで肩 2.標準的で自然な体型 3.168cmほどの高身長で手足が長い 4.小柄で柔らかな曲線 5.引き締まった運動部系 6.柔らかくふっくらした自然体 7.線の細いモデル体型 8.肩が下がった繊細な骨格

【髪】1.黒の短めボブに切りっぱなし前髪 2.茶のミディアムレイヤー 3.黒のロングストレート、センター分け 4.ゆるふわパーマ 5.高めのポニーテール、後れ毛あり 6.無造作なお団子、うなじに毛先 7.インナーカラーがのぞく暗髪 8.濡れ髪のウルフカット 9.ハイトーンベージュ、根元プリン 10.片耳にかけた肩までの髪

【シーン】※以下は一括で1つ選ぶこと（服・場所・光・仕草がセット）
1. 上品。白リネンシャツをワイドパンツにイン。ホテルの大きな窓辺で静かに外を見る。レースカーテン越しの柔らかい光
2. 上品。ゆったりした綿の浴衣にニットショール。冬の温泉旅館の縁側に座り、背後に湯気。冷たい青い夕暮れと室内の暖色灯
3. スタイリッシュ。黒テーラードジャケットに白T、ストレートデニム。ガラス張りのオフィス前を歩いている途中。曇天のフラットな光と鋭い反射
4. スタイリッシュ。くすんだスリップドレスにオーバーサイズのレザージャケット。雨上がりの細い路地。濡れたアスファルトにネオンが反射する夜
5. ちょい色っぽい（着衣のまま）。袖を肘までまくったオーバーサイズの白シャツ。ホテルの窓辺で肩越しに振り返る。レース越しの光が鎖骨と顎を撫で、部屋は影に沈む
6. ちょい色っぽい（着衣のまま）。ダークなリブニットワンピ。薄暗いバーカウンターで頬杖。低い琥珀色のタングステン光と深い影
7. だらしない。オーバーサイズのグレースウェットに脱げかけた厚手ソックス。ベッドにもたれて床に座り膝を抱える。寝癖のまま、薄いカーテン越しの朝の淡い光
8. だらしない。ジャージのセットアップ、手首にヘアゴム。深夜2時のコンビニの外でレジ袋を持って立つ。蛍光灯の冷たい光が歩道に漏れる
9. 元気。小花柄のサマーワンピース。海に突き出た木の桟橋を裸足で歩き、風に髪をなびかせて笑う。真昼の強い日差しとくっきりした影
10. 気だるげ。ショート丈カーディガンにハイウエストのヴィンテージデニム。夕方の電車の窓にこめかみを預けて何も見ていない。低い西日が車内を薙ぐ
11. 気だるげ。リブタンクトップにゆるいスウェットパンツ。アパートのベランダで腕を上げて洗濯物を干す。強い午後の逆光でシーツが透ける
12. レトロ。色落ちしたデニムオーバーオールにボーダーT。昭和レトロな喫茶店のボックス席で両手でマグを持つ。暖かいタングステン光とフィルムグレイン

【カメラ】1.85mmポートレート、浅い被写界深度、上半身寄り 2.35mmドキュメンタリー、環境が写る全身 3.ローアングルの広角、パースと空を強調 4.やや俯瞰、近い距離感 5.横顔にピント、背景は大きくボケ 6.3:4縦位置、三分割で人物をオフセンター

【共通】実写のRAW写真調。毛穴が見える自然な肌の質感、作り込みすぎないスナップの空気感、シネマティックな色調、目にシャープなピント、3:4縦位置。アニメ調・イラスト・3DCG・プラスチックのような肌・人形顔・強いフラッシュ・透かし・文字・破綻した手指は避ける。
```

> ⚠️ 冒頭に「23歳の成人女性」「全身着衣」「非性化されたシーン」と**肯定文で**書くこと。
> 「未成年を出すな」「裸体を出すな」と書くと逆に弾かれる。完成版は [safe.md](safe.md)。

**連投したいとき**は末尾に `これを4枚、毎回違う組み合わせで。` を足す。

### 注意

LLM系は乱数が偏りやすく、放っておくとリストの1番や無難な選択肢ばかり選ぶ。効く対策：

- `直前の生成と同じ番号は選ばないこと` を入れておく（上のプロンプトには入れてある）
- `シーンは7番で、他はランダム` のように軸を1つ指定して残りを振る
- `SEED=4821 として、各リストの項目数で割った余りで番号を決めて` と数式で決めさせる

---

## どれを使うべきか

- **手元にSD/ComfyUI環境がある** → ①。1枚ごとに本当にランダムで、バッチ16枚を放置できる。文句なしにこれが最良
- **Midjourney** → ②。ただし「抽選」ではなく「全部生成」なのでジョブ数に注意。人物のブレだけなら同じプロンプトを再送するだけでもいい
- **ChatGPT / Gemini しかない** → ③。ランダム性は本物ではなくモデルの気分次第だが、実用上は十分ばらける
