# 画像生成AIに直接投げるランダムプロンプト（第2弾・拡張版）

LLMに一度通さず、**生成AIのプロンプト欄にそのまま貼って、生成のたびに中身が変わる**形式。
[prompt.md](prompt.md) の拡張スロット（ムード12・シチュエーション24・時間帯・季節・天気・視点・L2.5）を、
そのまま貼れるように「シーン束13種」へまとめ直した直接投げ版。

> prompt.md はスロットを個別に振る正典、こちらは束にした簡略版。
> したがって項目数は一致しない（例: カメラは prompt.md が8、こちらが6）。
> 場面を増やしたいときは prompt.md のEスロットから束を足す。

| 形式 | 対象 | ランダムの実体 |
|---|---|---|
| ① `{a\|b\|c}` 版 | SD WebUI(A1111/Forge) + Dynamic Prompts、ComfyUI + 対応ノード | 1枚ごとに1つ抽選（本物のランダム） |
| ② `{a, b, c}` 版 | Midjourney | 全組み合わせを別ジョブとして一括生成 |
| ③ 自己完結文章版 | ChatGPT / Gemini / nano-banana 系 | モデル自身に選ばせる |

---

## 設計の肝：スロットを「束」にしてある

顔・体型・髪は何と組み合わせても破綻しないので独立スロットのまま。
一方、ムード＋服装＋場所＋仕草＋光を独立にランダム化すると
「温泉旅館でテーラードブレザー」みたいな事故が必ず起きる。

なので **ムード＋服装＋場所＋仕草＋光を1つの「シーン束」にまとめて13種**用意し、
そこから1つ抽選する形にした。さらに**時間帯・季節・天気・視点**を独立スロットとして追加。

束の番号は①②③で共通:
1-3 きっかけ / 4-5 生活の手元 / 6-7 気配のツーショット / 8-9 天気の変わり目 /
10-11 マジックリアリズム / **12-13 大人っぽい（L2.5）**

※第一弾(random/)の基本トーン（上品/スタイリッシュ/だらしない/元気/気だるげ/レトロ）は
第二弾から削除済み。第二弾は「きっかけ/生活の手元/気配のツーショット/天気の変わり目/
マジックリアリズム/大人っぽい」の6群のみ。両方を使うことで重複せずに幅が広がる。

組み合わせ数 = 顔タイプ10 × 顔特徴8 × 体型8 × 髪色4 × 髪型10 × シーン束13 × 時間8 × 季節8 × 天気8 × 視点5 × カメラ6
= **約51億通り**

> ⚠️ シーン束の中に時間帯・季節・天気がすでに含まれているものがある。
> その場合、独立スロットK/L/Mは束の指定を上書きせず補強する方向で解釈させるため、
> ③自己完結版には「シーン束に時間・天気の指定がある場合はそちらを優先し、独立スロットはそれに合うものを選ぶ」と書いてある。

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
Professional fashion editorial photograph. A 23-year-old adult Japanese woman, fully clothed in modest everyday clothing. Her face is at the level cast in Japanese TV commercials and dramas — girl-next-door idol looks, with occasional mature-beauty types mixed in. Well-balanced features, clear skin that still looks natural and un-retouched. Face type: {classic idol-type features|a round soft face with full cheeks|downturned eyes with a soft sweet expression|upturned cat-like eyes with a small sharp chin|K-idol polished styling|striking mixed-look features on Japanese bone structure|a bright healthy look with wide-set round eyes|an easy open face with a small snaggletooth|classic symmetrical beauty|cool composed mature beauty}, {large round eyes|double eyelids with long lashes|downturned eyes|upturned cat eyes|single-lid calm eyes|wide-set round eyes|crescent smiling eyes|a small snaggletooth when she smiles}, {a slender petite build|a healthy natural build with relaxed posture|tall and long-limbed with an elongated silhouette|petite with a natural figure|an athletic toned build|a soft natural build|a lean editorial model build|a fine-boned frame}, {jet-black|dark brown|beige|ash} {short bob with blunt bangs|medium layered hair with airy movement|long glossy straight hair center-parted|a loose wavy perm with soft volume around the cheeks|a high ponytail with loose strands at the temples|a messy top bun with loose ends|a wolf cut with choppy layers framing her face|a long blunt one-length cut|a half-up style|medium-length hair pulled behind one ear}.
{A moment of sudden flutter, her fingers stopped mid-motion in her hair as she notices the camera, half-lowered eyes catching the lens, standing in a doorway with warm afternoon light behind her|A moment of sudden flutter, tipping her face up to put in eye drops, lashes about to blink, window light across her face|A moment of sudden flutter, struggling with a necklace clasp, holding her hair up and asking for help with a glance, seen from behind|A quiet ritual, tasting miso soup from a small dish with eyes closed, steam rising from the pot beside her, a kitchen lit by low morning sun through a window|A quiet ritual, drawing something on a fogged winter window with her finger, the outside visible only through the lines she draws|The camera is someone beside her, holding out a melting ice cream bar toward the lens with one hand while digging in her bag with the other, not looking at the camera, a summer street in dappled shade|The camera is someone beside her, running toward the lens with a self-timer, a few steps before she arrives, hair beginning to blur, laughing, an evening park|The threshold of weather, looking down at the first raindrop on dry asphalt then up at the sky, a still-dry strand of hair, an empty street just before the downpour|The threshold of weather, standing at an unattended crossing where the tracks dissolve in heat shimmer, waiting at the lowered barrier, midsummer white haze|A perfectly ordinary photo with one small impossible thing: a normal morning breakfast table, but the steam from the tea rises as a tiny cumulus cloud, floating|A perfectly ordinary photo with one small impossible thing: a sunny sidewalk, but her shadow on the ground is holding an umbrella while she walks empty-handed|Mature and composed, a white blouse and a long pleated skirt, standing by a tall studio window, backlight glowing at the fabric's edge, the rest of the studio in clean white shadow|Mature and composed, a matte silk-blend dress with a high neckline, seated on a chair, morning light from a hotel window, the fabric falling quietly, a quiet and refined mood, the room softly lit and bright}.
{early dawn with the sky barely blue|morning with low slanting light|midday with the sun high|early afternoon|late afternoon golden hour|evening blue hour|night with artificial light|deep night mostly dark}, {early spring still cold but light returning|spring with cherry-blossom softness|rainy season damp and green|summer hot and bright|late summer with humid haze|autumn with crisp air and warm colors|late autumn with bare branches|winter cold and quiet}, {clear sky|overcast|rain|just after rain with wet surfaces|snow|fog|strong wind|heat shimmer}, {a third-person observer watching from across the street|a passerby's fleeting glance as she walks past|the camera is someone beside her, the viewpoint of intimacy|a high static surveillance angle slightly distant|her own gaze in a mirror selfie or held-at-arm's-length shot}, {85mm portrait lens, shallow depth of field, tight upper-body framing|35mm documentary framing, full body with the environment visible|low-angle wide shot emphasizing perspective and sky|slightly high angle at intimate distance|sharp side profile with the background heavily blurred|3:4 vertical portrait, subject off-center on the rule of thirds}.
Photorealistic raw photo, natural skin texture with visible pores, authentic candid feel, cinematic color grading, sharp focus on the eyes, 8k resolution, highly detailed.
```

### ネガティブプロンプト（固定）

> ⚠️ **ネガティブに `minor` `nudity` 等を書くと、フィルタは否定を解釈せずその語自体を検出して弾く。**
> 詳細と対策は [safe.md](../random/safe.md)。

```
anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like face, mannequin, distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs, harsh flash, blown highlights, heavy makeup, watermark, text, logo, low resolution, blurry
```

### 回し方

- **Batch count を 8〜16 に上げて、Seed は -1（ランダム）** → 1クリックで全部違う子が出る
- L2.5の束（最後2つ = 束12・13）だけ回したい → シーン束から他を消す
- 特定ムードだけ回したい → 該当する束だけ残す（束の番号は「設計の肝」の対応表を参照）
- 季節を固定したい → 季節スロットから1つだけ残す

### 便利な追加構文

```
{2::A|1::B}        A が B の2倍出やすくなる（L2.5の束を厚くしたい時など）
{1-2$$A|B|C}       1〜2個を選んで連結
__jp2_scene__      wildcards/jp2_scene.txt から1行ランダム抽選
```

---

## ② `{a, b, c}` 版 — Midjourney

Midjourney の `{}` は**抽選ではなく全組み合わせを別ジョブとして生成する**（Permutation Prompts）。
組み合わせ数がそのままジョブ数になり、上限40。**束の中のカンマは `\,` でエスケープが必須**。

スロットを増やすとジョブ数が掛け算で爆発するので、実用上はシーン束の1スロットだけにするのが安全。
第2弾は束が13あるので、そのままでは13ジョブになる。以下はよく回す6束（1・12・4・6・8・10）に絞った版（6ジョブ）。

```
Professional fashion editorial photograph, a 23-year-old adult Japanese woman fully clothed in modest everyday clothing, natural skin texture, {her fingers stopped mid-motion in her hair as she notices the camera\, half-lowered eyes catching the lens\, warm afternoon light behind her in a doorway, a white blouse and a long pleated skirt\, standing by a tall studio window\, backlight glowing at the fabric's edge\, the rest of the studio in clean white shadow, tasting miso soup from a small dish with eyes closed\, steam rising from the pot beside her\, a kitchen lit by low morning sun, holding out a melting ice cream bar toward the lens with one hand while digging in her bag with the other\, not looking at the camera\, a summer street in dappled shade, looking down at the first raindrop on dry asphalt then up at the sky\, a still-dry strand of hair\, an empty street just before the downpour, a normal morning breakfast table\, but the steam from the tea rises as a tiny cumulus cloud floating}, cinematic color grading, sharp focus on the eyes --ar 3:4 --style raw --no anime, illustration, 3d render, plastic skin, deformed hands, extra fingers, text, watermark
```

- 13束全部回したい場合は `\,` エスケープを維持したまま束を追加する（13ジョブになる）
- 顔・体型・髪も変えたい場合は、そのぶんジョブ数が掛け算になる点に注意（6シーン × 3髪型 = 18ジョブ）
- Midjourney は Seed 未指定なら毎回ランダムなので、同じプロンプトを再送するだけでも人物は変わる

---

## ③ 自己完結文章版 — ChatGPT / Gemini / nano-banana 系

これらは画像生成の前にモデルがプロンプトを読解するので、**「リストから1つランダムに選べ」という指示自体が効く**。1回貼るだけでよい。

> シーン束に時間・季節・天気の指定がすでに含まれている場合、独立スロットの【時間】【季節】【天気】はそれに合うものを選ぶ（矛盾しないもの。束の指定を優先）。

```
以下の条件で写真を1枚生成してください。

各リストから毎回ランダムに1つずつ選んでください。選んだ番号は言わず、画像だけ出してください。
直前の生成と同じ番号は選ばないこと。
シーン束に時間・季節・天気の指定がすでに含まれている場合は、それを優先し、【時間】【季節】【天気】は矛盾しないものを選ぶこと。

被写体: 23歳の日本人女性（成人）、全身きちんと着衣、非性化された自然なシーン。顔は必ず、日本のCMやドラマに起用されるレベルの可愛い顔立ち（アイドル・女優系）を基準に、時々美人寄りも混ぜる。目鼻立ちのバランスが良く、肌は綺麗だが加工しすぎない自然な質感。場面のどこかに、成人であることが読み取れる要素を1つ入れる（仕事帰り／ひとり暮らしの部屋／運転席／休日の自宅 など）。

【顔タイプ】1.正統派アイドル系 2.丸顔であどけない 3.たれ目で甘い 4.猫目で小悪魔っぽい 5.韓国アイドル風 6.ハーフっぽく華やか 7.健康的で元気 8.八重歯がチャーミング 9.正統派美人 10.涼しげな大人っぽい美人

【顔の特徴】1.大きな丸い目 2.二重で長いまつ毛 3.たれ目 4.つり目 5.一重で涼しげ 6.離れ気味の丸い目 7.笑うと三日月 8.八重歯

【体型】1.小柄 2.標準 3.高身長 4.小柄 5.引き締まった体型 6.自然体 7.モデル体型 8.華奢な骨格

【髪色】1.黒 2.ダークブラウン 3.ベージュ 4.アッシュ

【髪型】1.ショートボブ 2.ミディアムレイヤー 3.ロングストレート 4.ゆるふわパーマ 5.ポニーテール 6.お団子 7.ウルフカット 8.ロングのワンレン 9.ハーフアップ 10.ミディアムで片耳にかけた髪

【シーン束】※以下は一括で1つ選ぶこと（ムード・服・場所・仕草・光がセット）
※基本トーン（上品/スタイリッシュ/だらしない/元気/気だるげ/レトロ）は第一弾(random/)にあるので、第二弾ではそれ以外のムードを中心に構成。
1. きっかけ。髪を耳にかけようとした指が途中で止まる。こちらの視線に気づいて半分伏せた目だけがカメラへ。午後の光が入る扉口
2. きっかけ。目薬をさすため上を向いた顔と、まばたきするまつ毛。窓辺の光
3. きっかけ。ネックレスの留め金に苦戦し、後ろ髪を持ち上げたまま助けを求めて見る背中越しの構図
4. 生活の手元。味噌汁の味見。小皿に取ってひと口、目を閉じて味を確かめる横顔と、鍋から立つ細い湯気。朝の台所
5. 生活の手元。結露した冬の窓に指で何か書きかけ、外の景色が線の中にだけ見える
6. 気配のツーショット。溶けかけのアイスを「持ってて」とカメラに向かって差し出す手。財布を探す伏し目。カメラは受け取る側の視点。夏の木陰
7. 気配のツーショット。セルフタイマーに向かって走り込んでくる数歩手前。ブレ始めた髪と笑い声の顔。夕方の公園
8. 天気の変わり目。夕立の一粒目。乾いたアスファルトを見下ろし、空を見上げる。まだ乾いている髪。降り出す直前の街
9. 天気の変わり目。陽炎の無人踏切。線路の先が熱で溶け、遮断機の前で待つ。真夏の白いもや
10. マジックリアリズム。普通の朝の食卓。ただ紅茶の湯気が積雲のかたちで浮かんでいる
11. マジックリアリズム。快晴の歩道。本人は手ぶらなのに、足元の影だけが傘を差している
12. 大人っぽい。白いブラウスにロングプリーツスカート。高いスタジオ窓辺に立ち、逆光が布の縁で光る。残りは白い影
13. 大人っぽい。マットなシルク混じりのハイネックドレス。椅子に座り、ホテルの窓からの朝の光が当たる。布は静かに垂れ、上品で落ち着いた空気。部屋は明るい

【時間】1.明け方 2.朝 3.真昼 4.午後 5.夕方 6.宵 7.夜 8.深夜

【季節】1.早春 2.春 3.梅雨 4.夏 5.残暑 6.秋 7.晩秋 8.冬

【天気】1.晴れ 2.曇り 3.雨 4.雨上がり 5.雪 6.霧 7.強風 8.陽炎

【視点】1.離れた観察者 2.通りすがりの一瞬 3.カメラは隣にいる誰か 4.高い位置の監視カメラ 5.彼女自身（鏡 selfie）

【カメラ】1.85mmポートレート、浅い被写界深度、上半身寄り 2.35mmドキュメンタリー、環境が写る全身 3.ローアングルの広角、パースと空を強調 4.やや俯瞰、近い距離感 5.横顔にピント、背景は大きくボケ 6.3:4縦位置、三分割で人物をオフセンター

【共通】実写のRAW写真調。毛穴が見える自然な肌の質感、作り込みすぎないスナップの空気感、シネマティックな色調、目にシャープなピント、3:4縦位置。アニメ調・イラスト・3DCG・プラスチックのような肌・人形顔・強いフラッシュ・透かし・文字・破綻した手指は避ける。
```

> ⚠️ 冒頭に「成人女性」「全身着衣」「非性化されたシーン」と**肯定文で**書くこと。
> 「未成年を出すな」「裸体を出すな」と書くと逆に弾かれる。詳細は [safe.md](../random/safe.md)。

**連投したいとき**は末尾に `これを4枚、毎回違う組み合わせで。` を足す。

### 注意

LLM系は乱数が偏りやすく、放っておくとリストの1番や無難な選択肢ばかり選ぶ。効く対策：

- `直前の生成と同じ番号は選ばないこと` を入れておく（上のプロンプトには入れてある）
- `シーンは7番で、他はランダム` のように軸を1つ指定して残りを振る
- `SEED=4821 として、各リストの項目数で割った余りで番号を決めて` と数式で決めさせる
- 束12・13（大人っぽい）を多く出したい → `シーン束は12・13から多めに選んで` と指示する

### Geminiで弾かれるときの注意（実測）

Geminiは文脈を見ず、プロンプト内の語彙を合算スコアで判定する。以下の現象を実測:

1. **同じプロンプトでも、チャット（セッション）が違うと結果が変わる** — 累積スコア判定の揺れ。同じ内容でも通ったり弾かれたりする。
2. **長いプロンプトほど弾かれやすい** — 内容語が多いほど合算スコアが上がる。コードブロックだけを貼ること（説明文は貼らない）。
3. **Geminiが検出する語** — `透け` `色気` `薄暗い` `ベッド` `ドキッ` `振り返る` `脱げかけ` 等を、文脈不問で弾く。本ファイルではこれらをすべて除去済み。

**Geminiで弾かれたら:**
1. 新しいチャットで試す（セッションの累積をリセット）
2. それでも弾かれるなら、シーン束を1-11だけに減らす（L2.5の束12・13を外す）
3. さらに減らすなら、シーン束を3-4個だけ残す

---

## L2.5（大人っぽい）の使い方

シーン束の12・13が「大人っぽい」の束。色気は服の仕立てと光だけで出す。

**ChatGPTとGeminiは「厳しさの軸」が違う（重要）:**
どちらが厳しいかではなく、判定の仕方が違う。両方で通すには両方の条件を同時に満たす必要がある。

- **ChatGPT** … 文脈を読む。シーン全体が何を狙っているかで判定するため、表現の総合的な強度に敏感。
  健全な文脈（撮影現場・エディトリアル・生活の一場面）に置けば、光学的な言い回しも通ることが多い。
  （`expression/01` の「ChatGPT画像が最も表現に敏感」はこの軸の話）
- **Gemini** … 文脈を読まない。プロンプト内の語彙を合算スコアで判定するため、単語1つで即弾きされる。
  `expression/01` の光学言い回し（透け感/暗示/散乱/ブライダル/chaise longue/ドレープ）はここで落ちる。

→ したがって本ファイルでは、**Geminiの語彙フィルタを通る語だけ**を
**ChatGPTの文脈判定を通る健全な文脈**に置く、という方針で組んである。

**効いている語彙（Gemini通過済み）:**
- `a white blouse and a long pleated skirt`（白いブラウス+プリーツスカート）
- `backlight glowing at the fabric's edge`（逆光が布の縁で光る）
- `a matte silk-blend dress with a high neckline`（ハイネックで露出を抑える）
- `morning light tracing the line of her jaw`（顎のラインを光でなぞる）
- `the fabric falling quietly`（布が静かに垂れる）

**常時使わない語彙（レベル問わず）:**
- 透け / 透け感 / translucent / sheer（文脈不問で即弾き）
- sensual / seductive / lingerie / bare legs / unmade bed / 色気 / 脱げかけ

**L2.5のときだけ避ける語彙（L1/L2では使ってよい）:**
単体では健全だが、L2.5の文脈語（布・光・大人っぽい）と同居すると合算スコアが閾値を超える。
- 暗示 / hint / suggest（形態暗示の意図で使うと弾かれる）
- 散乱 / scatter / weave scattering（光の物理描写も弾かれる）
- ブライダル / bridal（色気文脈と判定される）
- chaise longue / シャゼロング（寝そべり=色気と判定される）
- ドレープ / drape（布の動きも色気語と判定される）
- body's line / contour / shoulder / collarbone（部位関連語）
- ベッド / bed、薄暗い、振り返る、ドキッ

**L2.5での言い換え表:**

| 元の表現 | L2.5での言い換え |
|---|---|
| 肩越しに振り返る | カメラの方へ視線だけを向ける（体は向こう向きのまま） |
| 鎖骨までの長さの髪 | ロングのワンレン |
| 肩までの髪 | ミディアムの髪 |
| ベッドに寝そべる | 椅子に座る |
| 薄暗い | 明るく柔らかい光 |

### Geminiで弾かれたときの切り分け（実測値）

| 束 | 弾かれた語 | 通った言い換え |
|---|---|---|
| 12（白いブラウス） | 透け感のある / 形体をほのかに暗示 / 織りが入射光を散乱 | 白いブラウス / 逆光が布の縁で光る のみ |
| 13（ハイネックドレス） | ラグジュアリーブライダル / シャゼロング / ドレープ | ハイネックドレス / 椅子に座り / 布は静かに垂れ のみ |

### 弾かれたら

1. まず 束12・13 を外して残りの11束で回す
2. ChatGPTなら光学言い回し版（expression/01準拠）に戻せるが、Geminiでは上記の安全語彙版を使う
3. それでも弾かれるなら、そのサービスは人物写真に厳しい。`safe.md` の「それでも弾かれたときの切り分け」参照

---

## どれを使うべきか

- **手元にSD/ComfyUI環境がある** → ①。1枚ごとに本当にランダムで、バッチ16枚を放置できる。文句なしにこれが最良
- **Midjourney** → ②。ただし「抽選」ではなく「全部生成」なのでジョブ数に注意。人物のブレだけなら同じプロンプトを再送するだけでもいい
- **ChatGPT / Gemini しかない** → ③。ランダム性は本物ではなくモデルの気分次第だが、実用上は十分ばらける
