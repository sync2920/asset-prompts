# 356 — 夜明けの河川敷、マットキャミ＋透けシフォンスカートの横寄り歩行

197〜200 に続く朝投稿用の1案。既存の朝案が「斜光が湯気・霧・カーテンを照らす」媒質経由の光だったのに対し、本案は媒質を置かず、**朝焼けの光が体をどう読むか**を見せ場にする。上はマットなキャミで**直接光**が肩と鎖骨に乗る、下は透けシフォンのスカートで**透過光**が脚の輪郭を影絵としてぼやっと浮かべる — 同じ昇りかけの太陽の2つの振る舞いを1つの主題に統一する。太陽そのものが地平線から顔を出してフレーム内に見える構図、**右横寄りの斜め後ろ（side-biased three-quarter）**、振り返りなし。人物はベージュ〜クリーム〜ヌードのワントーンでまとめ、柔らかい光に溶けるナチュラル＆上品カジュアル。背景は露の草むら・朝靄・遠景の鉄橋・空のベンチで河川敷の世界を埋めつつ、人影ゼロの静けさを維持する。

## 共通方針（README 準拠）

- 人物の身体特徴（髪を含む）は本文にハードコードせず**参照画像だけ**から推定して保持（`including chest and hip shape and fullness`）。
- ポーズは「動作の途中」。`candid, unposed, caught mid-moment, unaware of the camera` を含める。
- **透け感には必ず構造をつくる**（README／expression/01）。シフォンの透けは輪郭が影絵としてぼやっと浮かぶ書き方。めくれ上がって下着が見える状態は禁止、肌色・下着は透かさず、影側の布は柄 intact。
- 色はワントーン寄り。人物＝ベージュ＋クリーム＋ヌードの一系統（小花も地色に近いトーンオン톤で差し色なし）。背景＝青灰＋露の銀＋アスファルトのチャコール＋太陽の暖金。
- `never add or hardcode features that are not present in the reference image` を入れる。

- **比率:** 9:16
- **見せ場:** 朝焼けの光の2態様 — 上の肩・鎖骨の直接暖光と、下のシフォン越しの透過光。右プロファイルがほぼ完全に読める（振り返りではない）。
- **差し替え変数:** 場所、キャミとスカートの地色、小花のトーン。

---

## 英語プロンプト

```text
A highly detailed photorealistic portrait of the person from the reference image. 9:16 vertical aspect ratio, full body in frame from hair to the sandals on the ground. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode features that are not present in the reference image — no invented hair colors, accessories, uniforms, or props. Use this scene only if the reference is unambiguously adult; otherwise switch to a plain crew-neck tee and an opaque midi skirt with the same palette and no translucency.

Pose: Walking toward the rising sun along a riverside path, seen from her right side and only slightly behind — a side-biased three-quarter view, closer to a side view than a back view, not a flat profile. Her head faces forward, never turning to the camera, so her right profile reads almost in full against the bright sky. Mid-stride, right foot pushing off, left leg swinging through, the chiffon skirt swaying lightly and airily but never lifting open; arms relaxed, right hand open and trailing at hip height. Shoulders loose, an unhurried stride. Hair at the length, cut and style of the reference, lifted and drifting back in a faint breeze, a few strands across the cheek and nape. The quiet private satisfaction of a walk when no one else is awake — solitary, content, performing for no one. Candid, unposed, caught mid-moment, unaware of the camera. Nothing in either hand.

Outfit: A delicate camisole in a soft matte fabric — a beige-cream blend with a dry, natural hand and no silk or satin sheen, no glossy highlight anywhere on the cloth — with thin spaghetti straps on the outer shoulders and a modest scoop neckline (front and a shallow back U). The straps frame the collarbones and bare shoulders as fine lines of skin without opening a wide chest area. It is neatly tucked into the skirt's waistband at the natural waist, so top and skirt read as two separate pieces with a clean waistline, not one dress. The soft matte fabric follows the body; from the side it curves over the bust to the tucked waist, matching the reference silhouette. The bust sits high and supported on the ribcage, fullest point at armpit height (mid-upper arm), never low toward the waist, its side swell clear in profile. Below, a midi-length skirt in a light, airy floral chiffon that ends a little above the ankle, with a faint pale tone-on-tone floral — the blossoms in a muted shade close to the ground colour so the print stays within one warm neutral family and the whole figure reads near-monotone. The chiffon is gently translucent: where the low backlight passes through it, the legs beneath read as soft hazy silhouettes within the cloth — thigh and the bend of the knee as blurred shadow-shapes, suggested and out of focus rather than sharply drawn — while the bare lower legs below the hem are simply bare skin warming in the light. The sheer layers sway lightly and catch the light as she moves, but the skirt never lifts or blows open enough to expose what is beneath the waistband; the translucency stays a soft outline, never a see-through to skin tone or underwear, and no lining reads through. The shadowed folds keep their pale floral print intact. On her feet, simple flat sandals in a beige-nude tone — one clean minimal strap across the toes and a thin ankle strap, the bare foot and toes fully visible and anatomically correct (five toes per foot, no extra toes, no malformed feet, no floating or doubled straps), planted or lifting on the path as she walks. No jewelry, no watch, no bag, no accessories at all. A quietly put-together, natural and refined one-tone look.

The outfit's show is the rising sun through the sheer chiffon: the low backlight makes the cloth glow and the legs beneath read as soft hazy silhouettes within it (as above), the bare shoulders and collarbone above taking the warm rim directly and reading clean and luminous — so the frame holds two kinds of light on the same body, direct warm light on the bare skin above and transmitted glowing light through the chiffon below, the body read by light rather than exposure.

Background: A real riverside path as the sun just breaches the horizon, full of quiet detail. The sun has crested the far waterline — a soft half-risen warm disc low over the distant treeline on the right, clearly in frame over the water, blooming gently at its edge without blowing out the sky; warm gold and peach around it grading up into cool blue-grey holding the last of night. Underfoot, paved path with seams, cracks, scattered leaves. Her outer side is a grassy embankment, not a railing — tall dewy reeds and grasses, tips catching the first light as tiny bright points. Below, the river flat and mirror-still, steel-blue near, a molten-gold reflection path from the horizon; a low band of mist over the water and through the grass. Far bank: soft trees and one steel truss bridge in haze; one unlit lamppost behind her and one empty bench at the side — signs of a place made for people at the hour it belongs to none. No people, bicycles, dogs or boats. Cool, near-still air. Palette: blue-grey, dew-silver, asphalt charcoal and sun-gold; the figure itself stays one warm neutral tone that melts into this soft light.

Lighting: The low sun ahead-right backlights her from the side. A warm rim traces the sun-facing edge of her right profile, bare shoulder, collarbone and outer arm; the far side falls into cool blue shadow — that warm-cool line down her side is part of the subject. The same sun, passing through the sheer chiffon, makes it glow with the hazy leg-silhouette inside (as above) — so the backlight both rims the bare skin above and transmits through the cloth below, the body read by light rather than exposure. Dew and mist glow in the same light; the sun disc blooms at the horizon. No fill, no reflector, no artificial flare; the shadow side stays genuinely cool.

Camera: 85mm at f/2.2, chest height, to her right and slightly behind for the side-biased angle. She fills the left-centre walking into depth toward the sun; the sun disc sits upper-right over the water as the second subject, the dewy embankment rises soft in the lower-right foreground, her long warm-edged shadow stretches back. Shallow depth: profile edge, bare shoulder, the soft leg-outline through the chiffon and the flat sandals on the ground tack-sharp; far bridge, trees and sun dissolve to glow. Natural grain, no HDR glow, no beauty filter; real skin texture — pores and fine peach-fuzz lit along jaw, shoulder, collarbone.

Format: 9:16 portrait orientation, vertical full-body composition, the figure walking into the just-risen sun.
```

---

## 日本語訳

参照画像の人物の、昇りかけた朝日へ向かって川沿いの遊歩道を歩く姿のフォトリアルポートレート。9:16 縦、髪から地面のサンダルまで全身。見た目の年齢・性別表現・民族的特徴・体型とライン・身長感・比率・肌の色と質感・顔立ち・髪・胸と腰の形とボリュームを含む全身体特徴を参照に忠実に保持し、改変せず、参照にない特徴を足さない。成人と判断できる場合のみ使用、否则同じ配色のクルーネックTと透けないミディスカートに切替。

**ポーズ:** 昇りかけた太陽へ向かって歩き、右側面・わずかに後ろ寄り（横寄りの斜め、後ろより横に近い、平面的プロファイルではない）から。頭は進行方向へ向けたままで振り返らず、右プロファイルがほぼ完全に明るい空に対して読める。歩幅の途中、右脚で蹴り出し左脚が振り抜け、シフォンスカートは軽やかに揺れるが決して開かず、腕はリラックス、右手は開いて腰の高さで後ろへ。肩の力の抜けた急がない歩幅。髪は参照の長さ・カット・スタイルのまま、かすかな風で持ち上がり後ろへ流れ、数本が頬とうなじを横切る。誰も起きていない時間の散歩の静かな私的な満足 — 孤独で満ち足り、誰のためにも演じない。作られていない偶然の瞬間。どちらの手にも何も持たない。

**服装:** 柔らかくマットな生地の繊細なキャミソール — ベージュ〜クリームのブレンドで、乾いた自然な手触り、シルクやサテンのテカリはなく、布のどこにも光沢のハイライトなし。外肩の細いスパゲッティストラップと控えめなスクープネック（前面と浅い背面U字）— ストラップは鎖骨と裸の肩を細い肌の線として框架し、胸の広い面は開かない。スカートのウエストバンドに自然なウエストですっきりインされ、トップとスカートは清潔なウエストラインで別の2ピースとして読め、一枚のワンピースには見えない。柔らかくマットな生地は体に沿い、横からは胸の上でカーブしインされたウエストへ繋がり、参照のシルエットに一致。胸は肋骨の上で支えられ高く、最も張り出す点は脇の高さ（二の腕の中ほど）で腰へ垂れず、側面のふくらみがプロファイルで明確。下はくるぶし少し上で終わるミディ丈の、軽くエアリーな花柄シフォンスカート。淡いトーンオン톤の小花 — 花は地色に近い抑えた色合いで、柄は一つの warm neutral 一系統に留まり、人物全体がほぼワントーンに読める。シフォンは優しく半透明：低いバックライトが通るところで、下の脚が布の中に柔らかくぼやけたシルエットとして読める — 太ももと膝の折れがぼやけた影の形として、シャープでなく暗示されフォーカス外。一方裾の下の素足の脚は、そのまま暖光に温まる裸の肌。シアーな層は動きに合わせて軽やかに揺れ光を拾うが、スカートはウエストバンドの下が露出するほど持ち上がったり開いたりしない。透けは柔らかい輪郭のままで、肌色や下着が透ける see-through には決してならず、裏地も透けない。影側のひだは淡い小花柄が intact のまま。足元はベージュ〜ヌード系のシンプルなフラットサンダル — つま先に清潔で最小限のストラップ1本と細いアンクルストラップ、裸の足とつま先は完全に見え、解剖学的に正しい（片足5本、余分な指なし、変形した足なし、浮いたり二重になったストラップなし）、歩くにつれ遊歩道に着地したり離れたり。宝石・時計・バッグ・アクセサリーは一切なし。静かに整えた、ナチュラルで上品なワントーンの佇まい。

**服装の見せ場は、透けシフォンを通る昇りかけの太陽。** 低いバックライトが布を輝かせ、下の脚を柔らかくぼやけたシルエットとして読ませる（上記どおり）。上の裸の肩と鎖骨は暖色のリムを直接受け、清潔で luminous。こうしてフレームは同じ体に2種類の光を宿す — 上の裸の肌には直接の暖光、下のシフォンには透過して輝く光 — 体は露出でなく光で読まれる。

**背景:** 太陽が地平線を越えようとする瞬間の本物の川沿い遊歩道、静かなディテールに富む。太陽は対岸の水面を越えたばかり — 遠くの樹木の上、右側の水面の上にフレーム内にはっきり見える、低く半分昇った柔らかい暖色のディスク、縁がほのかに bloom するが空は白飛びしない。周りは暖金とピーチ、上へ冷たい青灰へ。足元は継ぎ目・ひび・落ち葉のある舗装路。外側は柵でなく草の土手 — 露の葦と野草、先端が最初の光で小さな明るい点。下では川が平らで鏡のように静止、手前は鋼青、地平線から溶けた金の反射帯、水面と草の間に低い朝靄。対岸は樹木と霞の鉄骨トラス橋、背後に消灯した街灯1本、脇に空のベンチ1脚 — 人のための場所が誰のものでもない時間にある痕跡。人・自転車・犬・船なし。冷たくほぼ無風。パレットは青灰・露の銀・アスファルトのチャコール・太陽の暖金。人物そのものはこの柔らかい光に溶ける warm neutral 一系統。

**照明:** 前方やや右の低い太陽が側面からバックライト。暖色のリムが右プロファイルの太陽側・裸の肩・鎖骨・腕の外側をなぞり、反対側は冷たい青の影へ — 側面を縦に走る暖冷の線も主役の一部。同じ太陽が透けシフォンを通り、それを輝かせて中のぼやけた脚シルエットを読ませる（上記どおり）— つまりバックライトは上の裸の肌を縁取り、下の布を透過し、体は露出でなく光で読まれる。露と靄も同じ光で輝き、太陽ディスクは地平線で bloom。Fill・レフ板・人工フレアなし、影側は genuinely に冷たいまま。

**カメラ:** 85mm f/2.2、胸の高さ、右側・わずかに後ろ寄りの横寄りアングル。彼女は左〜中央を太陽の奥行きへ歩き、太陽ディスクが右上の水面に第二の被写体、露の土手が右下前景に柔らかく、暖色の長い影が後ろへ。被写界深度は浅く：プロファイルの縁・裸の肩・シフォン越しの脚輪郭・地面のフラットサンダルは tack-sharp、遠景と太陽は glow に溶ける。自然なノイズ、HDRグローなし、美肌フィルターなし、本物の肌質感 — 顎・肩・鎖骨の毛穴と産毛が光る。

**フォーマット:** 9:16 縦、全身縦構図、昇ったばかりの太陽へ歩く人物。

---

## 設計メモ

### 既存朝案（197〜200）との差

- 197〜200 はすべて「斜光が湯気・霧・カーテン・薄い布を照らす」**媒質経由**の光。本案は媒質を置かず、**朝焼けの光が体をどう読むか**を見せ場にする。上＝直接光、下＝透過光の2態様を1主題に統一。
- 角度も変えた：197 室内接写／198 正面寄り全身／199 後ろ寄り3/4＋振り返り横顔／200 横位置やや低め。本案は**右横寄り斜め・振り返りなし**で、右プロファイルがほぼ完全に読める。199 の「振り返りで横顔を見せる」とは明確に区別。

### 指摘反映の履歴

- 第1稿（真横プロファイル・素足・背景＝水面＋空＋柵一本）に対し「殺風景／河川敷感がない／靴を履いて／真横は変、斜め後ろなど工夫を」。
- 第2稿（右斜め後ろ・スニーカー・露の草むら等）に対し「タンクトップの方がいい／登ってくる朝日が見えている構図／もう少し横に近い角度」。
- 第3稿（普通のタンク・太陽ディスク・横寄り斜め）に対し「服装をおしゃれに／ややキャミ方の上／下は柄の可愛い麻のロングスカート／朝焼けでスカートが少し透けて輪郭がぼやっと」。
- 第4稿（キャミ＋小花リネン透けスカート）の生成結果に対し「服装が少し変／靴も」。生成で観測した3失敗を修正：①スカートの風めくれ → めくれ禁止＋透けを「布が脚に触れる部分でのみ」に限定。②上下同色でワンピース化 → 上下を色分け＋tuck でウエスト明確化。③マキシ丈で靴が白い塊に → ankle 丈＋靴を具体で指定。
- 第5稿に対し「プロンプトが長すぎる、冗長を削って」→ 重複の統合と列挙の短縮で英語プロンプトを概ね3〜4割圧縮。
- 第6稿＝本版：服装リストの指定を反映。①トップスをマットなベージュ/クリーム系キャミに（シルク/サテンのテカリを明示排除）。②スカートを透け感のある淡い花柄シフォンのミディ丈（くるぶし少し上）に、軽やかに揺れる。③足元を白いスニーカーからベージュ/ヌード系のフラットサンダルに変更、素足のつま先が出るため足の解剖学ネガを追加。④全体をワントーン寄りに統一し、小花を地色に近いトーンオン톤にして差し色を撤去、人物を warm neutral 一系統に。

### 透けの安全設計（README／expression/01 準拠）

- シフォンはリネンより透けやすいが、規約「透け感には必ず構造をつくる」を継承。透けは「輪郭が影絵としてぼやっと」に限定し、肌色・下着・裏地は透かさず、めくれ上がってウエスト下が見える状態を禁止（`never lifts or blows open enough to expose what is beneath the waistband`）。
- ミディ丈のため膝下は素足が出るが、これはスカート丈の結果であり意図的な露出設計ではない。見せ場の焦点は「シフォンの透け輪郭＋肩鎖骨の直接光」の2態様統一のまま。

### 見せ場一箇所原則との整合

- 露出箇所を2つ並べるのではなく、**「朝焼けの光が体をどう読むか」を1つの主題**とし、上＝直接光・下＝透過光で統一。本文に `the body read by light rather than exposure` と明記。上のキャミはネックライン控えめで裸の面を肩と鎖骨のラインに限定。

### ワントーン化と配色

- ユーザー指定「全体をワントーン寄りに」を反映。人物＝ベージュ＋クリーム＋ヌードの一系統、小花も地色に近いトーンオン톤で差し色なし。README「一系統＋差し色一点まで」の「まで」に適合（差し色ゼロも許容）。背景パレットの差し色記述も削除。

### 足元の解剖学ネガ

- フラットサンダルで素足のつま先・甲が主役級に写るため、README「手が目立つ構図には解剖学ネガ」の精神を足に適用：`five toes per foot, no extra toes, no malformed feet, no floating or doubled straps`。

### 観測した失敗とネガの方針

- 過去の観測失敗（めくれ・ワンピース化・靴の潰れ）は具体語で肯定文に織り込み済み。独立 Avoid 行は新設しない方針を維持。

### ハードコード精査

- 髪の長さ・型・色は参照依存。挙動だけ指定。プロファイル列挙は「何が読めるか」の指定で形・色の固定ではない。Camera の `fine peach-fuzz` は個人特徴でなくリアル肌のディテール要求。服装ブロック内の色・素材・柄・丈は「服装」指定であり身体特徴のハードコードではない。

### 共通規約の適用

- 胸は横寄りの角度でプロファイルのサイドスウェルとして読ませる。`curves over the bust to the tucked waist` と「胸の位置は高く」の基準文を入れる。手は両方とも単純（`Nothing in either hand`）。表情は内心ベース（solitary, content, performing for no one）。`never add or hardcode features not present in the reference` で勝手な特徴持ち込みを防止。

### 参照

- `expression/01-sheer-skin-intimacy.md` — 透けを光学言い回し＋影絵シルエットで書く手法、線状境界（細ストラップ）の根拠、除外欄を肯定文に織り込む方針
- `ideas/197-199-morning-post.md` / `ideas/200-morning-garden-mist.md` — 既存朝案と透けシルエットの先例（199・200）
- `ideas/README.md` — 共通テンプレート・身体特徴保持・透け構造・ハードコード禁止規約
