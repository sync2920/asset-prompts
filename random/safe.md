# 検閲に弾かれない版（Qwen / Seedream / 国産系フィルタ対応）

`inline-random.md` の初版は安全フィルタに弾かれる。原因と修正版をここにまとめる。

> 12シーンを**1本ずつ完成形の英語プロンプト**にしたものは [en-prompts.md](en-prompts.md)。
> 単体でコピペして投げたい場合はそちらが早い。

---

## なぜ弾かれたか

エラー例:

> 该请求同时包含未成年/学生语境和性感、裸露或擦边描述，无法生成。
> 请改为明确成年主体、完整衣着和非性化场景后重试。

### 原因1（最重要）ネガティブプロンプトが自爆していた

Qwen・Seedream・Hunyuan 等の安全フィルタは、**プロンプトを否定込みで構文解析しない**。
テキスト全体を走査して、禁止語が「含まれているか」だけを見る。つまり:

```
Negative prompt: explicit nudity, minor, child, teenager, pornography, underwear focus
```

これは「これらを出すな」ではなく、フィルタから見れば
**「未成年・裸体・ポルノというワードを含むリクエスト」**そのもの。
除外のつもりで書いた語が、そっくりそのまま検出対象になっていた。

`minor / child / teenager` → 「未成年・学生語境」判定
`nudity / underwear / see-through / pornography` → 「性感・裸露・擦边」判定

エラーが両方を同時に指摘しているのは、両方が実際に文字列として存在していたから。

### 原因2 学生文脈の混入

`prompt.md` の服装リスト14番に `school-style navy cardigan and long skirt` を入れていた。
"adult version" と付けても無意味で、`school` の1語で学生判定される。削除済み。

### 原因3 感覚語の密集

`sensual` / `intimate` / `slip dress` / `bare legs` / `translucent` / `collarbone` /
`wet-look` あたりが1文に集まると、個々は無害でも合算スコアで閾値を超える。

---

## 修正の原則

| | 旧（弾かれる） | 新（通る） |
|---|---|---|
| 禁止事項の書き方 | ネガティブに `no nudity, no minor` | ポジティブに `fully clothed, adult woman` |
| ネガティブの中身 | 内容 + 技術が混在 | **技術的破綻のみ**（手指・CG感・画質） |
| 年齢表現 | `in her early 20s` | `a 23-year-old adult woman` ← 具体数字が強い |
| ジャンル宣言 | なし | `professional fashion editorial photograph` を先頭に |
| 雰囲気の出し方 | 身体・官能の語 | **光と構図の語**に翻訳する |

最後の行が肝。「色っぽさ」を身体の描写で書くと落ちるが、
**照明・陰影・レンズの語彙に置き換えると通るうえに、写真としての質も上がる。**

### 語彙の置換表

| 落ちる語 | 置換 |
|---|---|
| sensual / seductive / erotic | *削除*（moodは光で出す） |
| intimate | quiet, close, hushed |
| slip dress / lingerie-like | muted midi dress, silk-blend dress |
| bare legs / bare skin | *削除* → 具体的な衣類名を書く |
| see-through / translucent / sheer | backlit, glowing at the edges |
| collarbone / neckline / thigh | jawline, shoulder line, silhouette |
| wet-look hair | damp hair after a shower → `freshly washed hair` |
| barefoot | canvas sneakers, thick socks |
| school / student / uniform | *全面削除* |
| minor / child / teenager | *ネガティブにも書かない* |

---

## 修正版ネガティブプロンプト（内容語ゼロ）

```
anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like face, mannequin, distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs, harsh flash, blown highlights, heavy makeup, watermark, text, logo, low resolution, blurry
```

安全側の制約は**ポジティブ文の冒頭**で担保する:

```
Professional fashion editorial photograph. A 23-year-old adult Japanese woman, fully clothed in modest everyday clothing.
```

Qwen のWeb版のようにネガティブ欄が無いUIでは、ネガティブを本文に混ぜると危険度が上がる。
**欄が無いなら、ネガティブは貼らない。**上のポジティブ冒頭だけで足りる。

---

## 修正版 ①：`{a|b|c}` 版（SD / ComfyUI + Dynamic Prompts）

```
Professional fashion editorial photograph. A 23-year-old adult Japanese woman, fully clothed in modest everyday clothing, with {clean symmetrical features and large almond dark-brown eyes|calm mature features with defined double eyelids and a high nose bridge|a round youthful face with soft downturned eyes|feline upturned eyes and a small sharp chin|understated quiet features with single-eyelid eyes and minimal makeup|polished glass skin with straight brows and gradient lips|light freckles across her nose and a natural minimal-makeup look|high cheekbones and a long editorial face with strong bone structure|deep-set eyes and a defined brow line|a friendly open face with a small snaggletooth when she smiles}, {a slender petite build with narrow shoulders|a healthy natural build with relaxed posture|tall and long-limbed with an elongated silhouette|a petite frame with soft natural proportions|an athletic toned build with defined shoulders|a soft natural build and easy posture|a lean editorial build with a defined jawline|sloping shoulders and a fine delicate frame}, {a jet-black short bob with blunt bangs|medium layered brown hair with airy movement|long glossy straight black hair center-parted|a loose wavy perm with soft volume around the cheeks|a high ponytail with loose strands at the temples|a relaxed top bun with stray hairs at the nape|dark hair with a hidden inner color peeking through|a freshly washed wolf cut framing her face|high-tone beige hair with slightly grown-out roots|shoulder-length hair pulled behind one ear}.
{Composed and elegant, wearing a crisp white linen shirt tucked into wide beige trousers, standing by a tall hotel window looking quietly outside, soft window light filtered through lace curtains falling across her face|Quietly refined, wearing a neatly tied cotton yukata with a knit shawl over her shoulders, sitting on the wooden veranda of a winter hot-spring inn with steam rising behind her, cold blue evening air against warm lamp light from indoors|Confident and editorial, wearing a tailored black blazer over a plain white tee and straight denim, walking mid-stride past a glass-walled office entrance in the city, flat cool overcast daylight and sharp reflections|Graphic and self-assured, wearing a muted midi dress under an oversized leather jacket, standing in a narrow alley after rain, neon signage reflecting on the wet asphalt around her at night|Calm and self-possessed, wearing an oversized white shirt and tailored trousers, standing at a hotel window and glancing back over her shoulder, lace-filtered morning light raking across her jawline while the rest of the room falls into soft shadow|Quiet and composed, wearing a dark ribbed knit dress and a long wool coat, sitting at a dim bar counter with her chin resting on one hand, low amber tungsten light and deep shadows|Relaxed and off-duty, wearing an oversized gray sweatshirt with relaxed track pants and thick socks, sitting on the floor against her bed with her knees drawn up, hair unstyled from sleep, pale early morning light through thin curtains|Tired and unposed, wearing a soft jersey loungewear set with a hair tie on her wrist, standing just outside a convenience store at night holding a plastic bag, cold fluorescent light spilling onto the pavement|Bright and energetic, wearing a summer sundress with a small delicate pattern and canvas sneakers, walking along a wooden pier over the sea and laughing with her hair caught in the wind, hard midday sun and crisp shadows|Languid and detached, wearing a cropped cardigan over high-waisted vintage denim, leaning her temple against a train window in the late afternoon gazing at nothing, warm low sun sweeping through the carriage|Half-awake and unstyled, wearing a plain cotton tee and loose sweatpants, hanging laundry on a small apartment balcony with her arms raised, strong afternoon backlight with the white sheets glowing behind her|Nostalgic 90s Japanese snapshot mood, wearing faded blue denim overalls over a striped tee, sitting in the box seat of an old Showa-era coffee shop holding a mug with both hands, warm tungsten light}.
{85mm portrait lens, shallow depth of field, tight upper-body framing|35mm documentary framing, full body with the environment visible|low-angle wide shot emphasizing perspective and sky|slightly high angle at conversational distance|sharp side profile with the background heavily blurred|3:4 vertical portrait, subject off-center on the rule of thirds}.
Photorealistic raw photo, natural skin texture with visible pores, candid documentary feel, cinematic color grading, sharp focus on the eyes, 8k resolution, highly detailed.
```

ネガティブ欄には上の「修正版ネガティブプロンプト」だけを入れる。

---

## 修正版 ②：Qwen / ChatGPT / Gemini に1回貼る版

ネガティブ欄が無いUI向け。日本語で通る。

```
プロと同等のファッションエディトリアル写真を1枚生成してください。
被写体は23歳の成人女性（日本人）。全身きちんと着衣で、非性化された自然なシーンです。

各リストから毎回ランダムに1つずつ選んでください。選んだ番号は言わず、画像だけ出してください。
直前の生成と同じ番号は選ばないこと。

【顔】1.左右対称の整った顔とアーモンド型の大きな瞳 2.落ち着いた大人っぽい二重、高い鼻筋 3.丸顔でやわらかいたれ目 4.猫目のつり目、小さく尖った顎 5.薄めの顔立ちで一重、メイクは最小限 6.ツヤ肌に平行眉、グラデーションリップ 7.鼻にうっすらそばかす、ナチュラルメイク 8.高い頬骨と長い顔、骨格のはっきりしたモデル顔 9.彫りが深く眉骨がはっきりした顔 10.笑うと八重歯が見える親しみやすい顔

【体型】1.華奢で小柄、なで肩 2.標準的で自然な体型 3.168cmほどの高身長で手足が長い 4.小柄で自然なプロポーション 5.引き締まったスポーティな体型 6.やわらかく自然体な体型 7.線の細いモデル体型 8.肩が下がった繊細な骨格

【髪】1.黒の短めボブに切りっぱなし前髪 2.茶のミディアムレイヤー 3.黒のロングストレート、センター分け 4.ゆるふわパーマ 5.高めのポニーテール、後れ毛あり 6.ゆるいお団子、うなじに毛先 7.インナーカラーがのぞく暗髪 8.洗いたてのウルフカット 9.ハイトーンベージュ、根元プリン 10.片耳にかけた肩までの髪

【シーン】※服・場所・光・仕草がセット。一括で1つ選ぶこと
1. 上品。白リネンシャツをワイドパンツにイン。ホテルの大きな窓辺で静かに外を見る。レースカーテン越しの柔らかい光
2. 上品。きちんと着付けた綿の浴衣にニットショール。冬の温泉旅館の縁側に座り、背後に湯気。冷たい青い夕暮れと室内の暖色灯
3. スタイリッシュ。黒テーラードジャケットに白T、ストレートデニム。ガラス張りのオフィス前を歩いている途中。曇天のフラットな光と鋭い反射
4. スタイリッシュ。くすんだミディ丈ワンピにオーバーサイズのレザージャケット。雨上がりの細い路地。濡れたアスファルトにネオンが反射する夜
5. 落ち着いた佇まい。オーバーサイズの白シャツにテーラードパンツ。ホテルの窓辺で肩越しに振り返る。レース越しの朝の光が顎のラインを撫で、部屋の奥は影に沈む
6. 静かな大人の空気。ダークなリブニットワンピにロングコート。薄暗いバーカウンターで頬杖。低い琥珀色のタングステン光と深い影
7. リラックスしたオフの日。オーバーサイズのグレースウェットにスウェットパンツと厚手ソックス。ベッドにもたれて床に座り膝を立てる。寝起きのままの髪、薄いカーテン越しの朝の淡い光
8. 気の抜けた深夜。ジャージのセットアップ、手首にヘアゴム。夜のコンビニの外でレジ袋を持って立つ。蛍光灯の冷たい光が歩道に漏れる
9. 元気。小花柄のサマーワンピースにキャンバススニーカー。海に突き出た木の桟橋を歩き、風に髪をなびかせて笑う。真昼の強い日差しとくっきりした影
10. 気だるげ。ショート丈カーディガンにハイウエストのヴィンテージデニム。夕方の電車の窓にこめかみを預けて何も見ていない。低い西日が車内を薙ぐ
11. 生活感。無地のコットンTにゆるいスウェットパンツ。アパートのベランダで腕を上げて洗濯物を干す。強い午後の逆光、背後で白いシーツが光る
12. レトロ。色落ちしたデニムオーバーオールにボーダーT。昭和レトロな喫茶店のボックス席で両手でマグを持つ。暖かいタングステン光とフィルムグレイン

【カメラ】1.85mmポートレート、浅い被写界深度、上半身寄り 2.35mmドキュメンタリー、環境が写る全身 3.ローアングルの広角、パースと空を強調 4.やや俯瞰、会話するくらいの距離 5.横顔にピント、背景は大きくボケ 6.3:4縦位置、三分割で人物をオフセンター

【仕上げ】実写のRAW写真調。毛穴が見える自然な肌の質感、スナップの空気感、シネマティックな色調、目にシャープなピント、3:4縦位置。アニメ調・イラスト・3DCG・プラスチックのような肌・破綻した手指は避ける。
```

---

## それでも弾かれたときの切り分け

安全フィルタは合算スコア方式なので、「どの語が悪いか」は二分探索で特定するのが速い。

1. まず土台だけ投げる
   `プロのファッションエディトリアル写真。23歳の成人女性（日本人）、白いリネンシャツにワイドパンツ、ホテルの窓辺に立つ。柔らかい自然光。`
   → これが通らないなら、そのサービス自体が人物写真に厳しい
2. 通ったら **シーンを1つずつ**足して再送。落ちた瞬間の1文が原因
3. 原因文から上の置換表に該当する語を消す

経験的に落ちやすいのは **シーン5・6・7・11**（室内 + 部屋着 or 薄暗さ）。
この4つを外せば残り8シーンはほぼ確実に通る。

---

## 正直な線引き

- 上の修正で通るのは、元の設計でいう **L1〜L2まで**（着衣のまま、雰囲気は光で表現）。
  実写として質は落ちない。むしろ照明語彙に寄せたぶん写真らしくなる。
- **L3 は削除した。** あれはフィルタが弾くように作られている領域なので、
  言い換えでくぐらせる方向の調整はしない。表現を変えるのではなく、狙いを L2 に下げるのが正解。
- 逆に、L1〜L2 が弾かれるのは**フィルタの誤検知**（否定文を読めていない）なので、
  上の修正はその誤検知を消す作業であって、回避ではない。
