# 5000字以内・圧縮版（可愛い顔に固定）

`expanded.md` のプロンプトは 5982字 / 6553字、`en-prompts.md` の指示版は 5100字あり、
文字数制限のあるサービスで弾かれる。内容を落とさず圧縮し、さらに**顔を可愛い系に固定**した版。

| | 文字数 | 用途 |
|---|---|---|
| A. 日本語版 | 約1,900字 | ChatGPT / Gemini / Qwen。**最も余裕がある** |
| B. 英語版 | 約3,700字 | 海外系モデル、英語のほうが追従が良い場合 |
| C. `{a\|b\|c}` 版 | 約4,500字 | SD WebUI / ComfyUI |

> **字数制限があるなら日本語版（A）を使うこと。**
> 計測すると同じ内容で英語の約1/3に収まる（1,900字 ⇔ 5,100字）。
> 画像生成モデルは日本語の指示も問題なく解釈する。

---

## 圧縮の方法

スロットも項目数も削っていない（組み合わせ数は約5.8億通りのまま）。

1. 番号付き改行リスト → スラッシュ区切りの1行に
2. 冗長な英文（`a full bust that gives the silhouette a soft curve`）→ 名詞句（`full bust, soft curve to the silhouette`）に
3. 全項目で繰り返していた共通句を、末尾の共通指定に1回だけ書く

## 顔を可愛い系に固定した方法

**可愛さの「レベル」を振ると外れ顔が出る。振るのは「タイプ」だけにする。**

- 全生成に共通の土台を1行入れる
  → `日本のCMやドラマに起用されるレベルの可愛い顔立ち（アイドル・女優系）`
- そのうえで**可愛さのタイプ8種**（正統派アイドル/童顔/小悪魔/清楚女優/韓国アイドル/ハーフ顔/健康的/大人可愛い）を振る
- 輪郭・目のスロットからは、可愛く出にくい項目を除外した
  （旧版の `エラの張った四角い顔` `眠たげな重い一重` `眉骨の下に落ち窪んだ目` を削除）

⚠️ 注意：`beautiful` `gorgeous` のような賛美語を積むと、逆に**AI特有のツルツルした人形顔**になる。
土台の一文に `肌は綺麗だが加工しすぎない自然な質感` を必ず残すこと。これが効いている。

---

## A. 日本語版（約1,900字）

```
23歳の成人日本人女性、全身きちんと着衣、非性化された自然なシーンのファッション写真を1枚生成。
顔は必ず、日本のCMやドラマに起用されるレベルの可愛い顔立ち（アイドル・女優系）。目鼻立ちのバランスが良く、肌は綺麗だが加工しすぎない自然な質感。
各項目から毎回ランダムに1つ選ぶ。選んだ番号は言わず画像だけ出す。前回と同じ組合せは選ばない。

可愛さのタイプ:正統派アイドル顔で左右対称/童顔であどけない/小悪魔系でいたずらっぽい/清楚系の女優顔で落ち着いた品/韓国アイドル系のツヤ肌と平行眉/ハーフっぽく華やか/元気で健康的/大人可愛く甘さと落ち着きが同居
輪郭:小さめの卵型で顎が柔らかい/丸顔で頬がふっくら/逆三角で顎が細くシャープ/小顔で顎が尖ったV字/細面で首が長い/小顔で頬に自然な丸み
目:大きく丸いアーモンド型でキャッチライトが強い/やや目尻の上がった猫目/たれ目でやわらかく甘い/くっきり二重で長い睫毛/離れ気味の丸い目で人形のよう/細めで涼しげな一重で上品/笑うと三日月形になる/澄んだ大きな瞳で目尻がわずかに下がる
体格:152cm華奢でなで肩/158cm標準/172cm高身長モデル体型/引き締まった筋肉質/ふくよかで腕も顔も丸く健康的/高身長で肩幅広め/骨が細く鎖骨と手首が目立つ/バランス良くウエストがくびれる
バスト:平坦でまっすぐ/控えめ/標準/豊かでシルエットに柔らかい曲線/かなり豊かで背筋の伸びた姿勢
ヒップ:狭くまっすぐボーイッシュ/細めでなだらか/標準/丸みがありウエスト下で広がる/広くウエストのくびれが際立つ
髪色:漆黒/ダークブラウン/アッシュブラウン/栗色/プラチナブロンド/金髪/ミルクティーベージュ/カッパーレッド/バーガンディ/アッシュブルー※/ネイビー※/シルバー※/パステルピンク※/ラベンダー※
 ※印の色は「明らかに染めた髪、分け目に地毛の黒いプリンが見える」を必ず添える
髪型:切りっぱなし前髪のショートボブ/ミディアムレイヤー/センター分けロングストレート/ゆるふわパーマ/高めポニーテール/ゆるいお団子/片耳にかけた肩までの髪/ウルフカット/鎖骨ラインのワンレン/低い位置のツイン三つ編み

シーン（服・場所・光・仕草がセット。まとめて1つ選ぶ）
1 白リネンシャツをワイドパンツにイン、ホテルの大窓辺で静かに外を見る、レース越しの柔らかい光
2 綿の浴衣にニットショール、冬の温泉旅館の縁側、背後に湯気、青い夕闇と室内の暖色灯
3 黒ジャケットに白Tとストレートデニム、ガラス張りオフィス前を歩く途中、曇天のフラットな光と鋭い反射
4 くすんだミディ丈ワンピにレザージャケット、雨上がりの細い路地、濡れた路面のネオン反射、夜
5 袖をまくったオーバーサイズ白シャツにテーラードパンツ、ホテル窓辺で肩越しに振り返る、レース越しの朝光が顎を撫で部屋の奥は影
6 ダークなリブニットワンピにロングコート、薄暗いバーカウンターで頬杖、低い琥珀色のタングステン光と深い影
7 グレースウェットにスウェットパンツと厚手ソックス、ベッドにもたれ床に座り膝を立てる、寝起きの髪、薄いカーテン越しの朝の淡い光
8 ジャージ上下、手首にヘアゴム、夜のコンビニ外でレジ袋を持つ、蛍光灯の冷たい光が歩道に漏れる
9 小花柄サマーワンピにキャンバススニーカー、海の木の桟橋を歩き風に髪をなびかせ笑う、真昼の強い日差しと硬い影
10 ショート丈カーデにハイウエストのヴィンテージデニム、夕方の電車の窓にこめかみを預け何も見ていない、低い西日が車内を薙ぐ
11 無地のコットンTにゆるいスウェットパンツ、ベランダで腕を上げ洗濯物を干す、午後の強い逆光、背後で白いシーツが光る
12 色落ちデニムオーバーオールにボーダーT、昭和レトロな喫茶店のボックス席で両手でマグを持つ、暖色タングステン光とフィルムグレイン

カメラ:85mmで浅い被写界深度・上半身/35mmで環境込みの全身/ローアングル広角で空とパース/やや俯瞰で近い距離/横顔にピントで背景ボケ/3:4縦で人物をオフセンター

仕上げ:実写のRAW写真調、毛穴が見える自然な肌、スナップの空気感、シネマティックな色調、目にシャープなピント、3:4縦位置。アニメ調・イラスト・3DCG・プラスチックのような肌・人形顔・破綻した手指は避ける。
```

---

## B. 英語版（約3,700字）

```
Generate one professional fashion editorial photograph.
Subject: a 23-year-old adult Japanese woman, fully clothed in modest everyday clothing, natural non-sexualized scene.
Her face must always read as genuinely cute and idol-like, girl-next-door beauty cast in Japanese TV commercials. Well-balanced delicate features, clear skin that still looks natural and un-retouched.
Pick ONE at random per line. Don't state picks. Never repeat the previous combination.

CUTE TYPE: classic symmetrical idol / baby-faced and innocent / mischievous koakuma charm / demure actress-like poise / polished K-idol with glass skin and straight brows / striking mixed-look features / bright healthy sporty / mature-cute, sweet but composed
FACE SHAPE: small oval, soft jawline / round baby face, full cheeks / heart-shaped, slim sharp chin / small tapered, neat pointed chin / slim face, long neck / petite face, softly rounded cheeks
EYES: large round almond with a bright catchlight / slightly upturned cat-like, playful / gently downturned tareme, sweet and soft / crisp double eyelids, long lashes / wide-set round, doll-like / narrow elegant single lid, refined / crescent smiling eyes / big clear eyes, slightly downturned outer corners
BUILD: petite slim 152cm / average 158cm naturally proportioned / tall lean 172cm model / athletic toned / softly plump, rounded arms and full face, healthy / tall broad-shouldered / fine-boned, visible collarbones / balanced, defined waist
BUST: flat straight silhouette / small modest / average natural / full, soft curve to the silhouette / generous, balanced by upright posture
HIPS: narrow straight boyish / slim gentle line / naturally proportioned / softly rounded, widening below the waist / wide full, clearly defined waist above
HAIR COLOR: jet black / dark brown / ash brown / warm chestnut / platinum blonde / warm golden blonde / milk-tea beige / copper red / deep burgundy / ash blue* / deep navy* / silver gray* / pastel pink* / lavender*
 (*for starred colors add: obviously salon-dyed, natural dark roots at the parting)
HAIR STYLE: short bob blunt bangs / medium layered airy / long straight center-parted glossy / loose wavy perm / high ponytail loose strands / relaxed top bun stray hairs / shoulder-length tucked behind one ear / wolf cut choppy layers / blunt collarbone one-length / low twin braids

SCENE (wardrobe + place + light + action come as one set; pick one whole line)
1 crisp white linen shirt in wide beige trousers, by a tall hotel window looking out, lace-filtered soft window light
2 neatly tied cotton yukata with knit shawl, veranda of a winter hot-spring inn, steam behind her, cold blue dusk against warm indoor lamps
3 black blazer over white tee and straight denim, mid-stride past a glass-walled office entrance, flat overcast daylight, sharp reflections
4 muted midi dress under an oversized leather jacket, narrow alley after rain, neon reflecting on wet asphalt, night
5 oversized white shirt sleeves rolled, tailored trousers, at a hotel window glancing back over her shoulder, lace-filtered morning light raking her jawline, room in soft shadow
6 dark ribbed knit dress and long wool coat, dim bar counter, chin resting on one hand, low amber tungsten, deep shadows
7 oversized gray sweatshirt, track pants, thick socks, on the floor against her bed, knees drawn up, sleep-unstyled hair, pale morning light through thin curtains
8 soft jersey loungewear, hair tie on wrist, outside a convenience store at night holding a plastic bag, cold fluorescent spill on the pavement
9 small-print summer sundress and canvas sneakers, walking a wooden sea pier, laughing, hair in the wind, hard midday sun, crisp shadows
10 cropped cardigan over high-waisted vintage denim, temple against a train window in late afternoon, gazing at nothing, low warm sun through the carriage
11 plain cotton tee and loose sweatpants, hanging laundry on an apartment balcony, arms raised, strong afternoon backlight, white sheets glowing behind her
12 faded denim overalls over a striped tee, box seat of an old Showa-era coffee shop, holding a mug in both hands, warm tungsten, film grain

CAMERA: 85mm shallow DOF upper body / 35mm documentary full body with environment / low-angle wide, sky and perspective / slightly high angle, close / sharp side profile, background blurred / 3:4 vertical, off-center

FINISH: photorealistic raw photo, natural skin texture with visible pores, candid feel, cinematic color grading, sharp focus on the eyes, 8k, 3:4 vertical. Avoid anime, illustration, 3D render, plastic skin, doll-like face, malformed hands.
```

---

## C. `{a|b|c}` 版（約4,500字）— SD WebUI / ComfyUI

```
Professional fashion editorial photo. A 23-year-old adult Japanese woman, fully clothed in modest everyday clothing. A genuinely cute idol-like face, girl-next-door beauty cast in Japanese TV commercials, well-balanced delicate features, clear skin that still looks natural and un-retouched. Face: {classic symmetrical idol|baby-faced innocent|mischievous koakuma charm|demure actress-like poise|polished K-idol glass skin straight brows|striking mixed-look features|bright healthy sporty|mature-cute sweet but composed}, {small oval soft jawline|round baby face full cheeks|heart-shaped slim sharp chin|small tapered neat pointed chin|slim face long neck|petite face softly rounded cheeks}, {large round almond eyes bright catchlight|slightly upturned cat-like eyes playful|gently downturned tareme eyes sweet|crisp double eyelids long lashes|wide-set round doll-like eyes|narrow elegant single-lid eyes refined|crescent smiling eyes|big clear eyes slightly downturned outer corners}. Figure: {petite slim 152cm|average 158cm natural|tall lean 172cm model|athletic toned|softly plump rounded arms full face healthy|tall broad-shouldered|fine-boned visible collarbones|balanced defined waist}, {flat straight silhouette|small modest bust|average natural bust|full bust soft curve to the silhouette|generous bust upright posture}, {narrow straight boyish hips|slim hips gentle line|naturally proportioned hips|softly rounded hips widening below the waist|wide full hips defined waist}. Hair: {jet black|dark brown|ash brown|warm chestnut|platinum blonde|warm golden blonde|milk-tea beige|copper red|deep burgundy|ash blue salon-dyed dark roots|deep navy salon-dyed dark roots|silver gray salon-dyed dark roots|pastel pink salon-dyed dark roots|lavender salon-dyed dark roots} {short bob blunt bangs|medium layered airy|long straight center-parted glossy|loose wavy perm|high ponytail loose strands|relaxed top bun|shoulder-length tucked behind one ear|wolf cut choppy layers|blunt collarbone one-length|low twin braids}. {crisp white linen shirt in wide beige trousers, by a tall hotel window looking out, lace-filtered soft light|neatly tied cotton yukata with knit shawl, veranda of a winter hot-spring inn, steam behind her, cold dusk against warm indoor lamps|black blazer over white tee and straight denim, mid-stride past a glass-walled office entrance, flat overcast daylight|muted midi dress under an oversized leather jacket, narrow alley after rain, neon on wet asphalt, night|oversized white shirt sleeves rolled and tailored trousers, at a hotel window glancing back over her shoulder, lace-filtered morning light raking her jawline, room in soft shadow|dark ribbed knit dress and long wool coat, dim bar counter, chin on one hand, low amber tungsten, deep shadows|oversized gray sweatshirt track pants thick socks, on the floor against her bed knees drawn up, sleep-unstyled hair, pale morning light through thin curtains|soft jersey loungewear, outside a convenience store at night holding a plastic bag, cold fluorescent spill on pavement|small-print summer sundress and canvas sneakers, walking a wooden sea pier laughing, hair in the wind, hard midday sun|cropped cardigan over high-waisted vintage denim, temple against a train window in late afternoon, low warm sun through the carriage|plain cotton tee and loose sweatpants, hanging laundry on an apartment balcony arms raised, strong afternoon backlight, white sheets glowing|faded denim overalls over a striped tee, box seat of an old Showa-era coffee shop holding a mug, warm tungsten, film grain}. {85mm shallow DOF tight upper body|35mm documentary full body with environment|low-angle wide sky and perspective|slightly high angle close distance|sharp side profile background blurred|3:4 vertical subject off-center}. Photorealistic raw photo, natural skin texture with visible pores, candid feel, cinematic color grading, sharp focus on the eyes, 8k, highly detailed.
```

ネガティブ（欄がある場合のみ）:

```
anime, illustration, stylized, CGI, 3D render, plastic skin, doll-like face, mannequin, distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs, harsh flash, blown highlights, heavy makeup, watermark, text, logo, blurry, unflattering angle
```

---

## それでも入らないときの削り方

制限がもっと厳しい（2000字など）場合は、この順で削る。**下ほど絵への影響が小さい**。

1. **カメラ** を削り、末尾に固定で `85mm, shallow depth of field` と書く … −250字
2. **髪色を7色に半減**（漆黒/ダークブラウン/プラチナブロンド/金髪/カッパーレッド/アッシュブルー※/パステルピンク※）… −200字
3. **シーンを6つに半減**（1・4・5・7・9・12 がトーンの散らばりが良い）… −700字
4. **輪郭スロットを削除**（可愛さのタイプと目だけでも顔は十分ばらける）… −150字

逆に**削ってはいけない**のは冒頭2行:

- `23歳の成人日本人女性、全身きちんと着衣、非性化された自然なシーン`
  → 削ると安全フィルタに弾かれる（[safe.md](safe.md) 参照）
- `日本のCMやドラマに起用されるレベルの可愛い顔立ち…加工しすぎない自然な質感`
  → 削ると顔の当たり外れが大きくなる。可愛さを支えているのはこの1行
