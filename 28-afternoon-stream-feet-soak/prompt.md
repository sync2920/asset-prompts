# 28. 渓流に足を浸しておにぎり、木漏れ日と水しぶき（参照画像ベース）

`ideas/README.md` の人物参照方針に準拠し、人物の顔・髪・肌・体型・身長感・プロポーションなどの身体的特徴は参照画像から忠実に保持する（髪を含む身体特徴は本文にハードコードしない）。`ideas/362-371-refreshing-cool-ten.md` の 365 を実生成用フォーマットに展開した案。媒質変奏シリーズ（199 布透過 → 200 霧透過 → 11 ガラス透過 → 12 風による離反）の次の一手として、媒質が光を運ぶのではなく**冷たさと反射光を直接運ぶ「水そのものへの接触」**を主題にする。真夏の渓谷で大きな岩に座り、流れに足を浸しながら、小さな手作りおにぎりをちょっと口に含んでにこっとする一瞬。「おいしい」が滲むが派手ではない、お淑やかな微笑み。足元の流れは踵と水中石に当たって、元気な飛沫となって立ちのぼる。全体のトーンは明るめ（ハイキー寄り）、影は深くせず明るい緑の陰に留める。「本当にこの一瞬を抜き取った」感を出すため、decisive moment の指示をカメラブロックに明記。透けは一切使わない健全な清涼案。

- **アスペクト比:** 9:16 縦（岩の上の全身から水面まで、縦の落差を収める）
- **見せ場:** ①小さなおにぎりをちょっと口に含んでにこっとする顔（お淑やかな「おいしい」） ②足元に立ちのぼる元気な水飛沫と、すねに当たる流れ ③水面反射のクールな下光が脚と顎の裏に揺れる。木漏れ日の光の玉が全体に散る
- **構図:** 水面近くのローアングル、下流側の斜め前から。前景に明るい水面のぼけ、背景は滝筋と明るい緑のボケ。全身を縦に収め、顔は上三分の一
- **服装:** バブルヘムのコンパクトトップ（白・完全不透明。胸元はフィット、裾だけバルーン状にギャザーする今季のトレンドシルエット）＋ペールダスティブルーの膝丈コットンスカート（前裾はウエストに一度タックして固定）。サンダルは脱いで乾いた岩の上
- **照明:** 渓谷の木漏れ日（直射はシャフトと光の玉）＋水面からのクールな反射下光（356 の二光源デバイスの転用）。全体は明るめのトーン（ハイキー寄り）、影は潰さず明るい緑の陰に。顔には硬い直射帯を当てない
- **文脈:** 真夏の渓流ピクニック（足浸し＋おにぎり）、健全な清涼。汗は描かず、涼は水・影・緑で出す（`expression/02` 準拠）
- **差し替え変数:** スカート色、時間帯（午前 ↔ 午後）、渓流の規模（せせらぎ ↔ 本流筋）、トップス候補（フロントリボン半袖カーデ × キャミ ↔ ポロ衿コンパクトニット）

---

## プロンプト

```text
A highly detailed photorealistic portrait of the person from the reference image. 9:16 vertical aspect ratio, an ultra-realistic editorial photo study of midsummer coolness on a forest mountain stream. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode features that are not present in the reference image — no invented hair colors, accessories, uniforms, or props. Use the trend top described below only if the reference is unambiguously adult; otherwise replace it with a fully opaque relaxed white tee in the same scene. Avoid: no extra limbs, extra fingers, malformed hands, or duplicated objects.

Scene: A clear, cold mountain stream in a forested ravine, early afternoon in midsummer. Large pale-grey boulders, one broad flat rock at the water's edge where she sits. The current runs clear and shallow over smooth pebbles, ankle-deep where her feet rest, with a small murmuring cascade upstream. A dense green canopy closes overhead and breaks the sun into scattered shafts and drifting coins of light; beyond the ravine the day is glaring midsummer, but here the air is cool and damp with spray. Moss rims the stones at the waterline. Her simple flat leather sandals sit paired on the dry rock behind her, beside a small lunch cloth opened flat with a second small rice ball waiting on it. No other people, no signs, no man-made structures — only water, stone and green.

Pose: Caught in the first second of a cold soak, in the middle of a streamside lunch. She sits on the broad flat rock with her feet dipped into the current, calves and shins bare above the waterline, both feet clearly visible through the clear shallow water, toes relaxed on the pebbles. Her knees are raised a little and held loosely together, the skirt's front hem tucked once into its own waistband so it stays gathered above her knees on its own, freeing both hands. In one hand she holds a small handmade rice ball — petite, a two-bite size resting in her curled fingers — raised to her mouth with just its bitten corner held between her lips, crisp nori still half-wrapping the rice. Her other palm rests flat on the dry rock beside her hip, holding her light lean. The cold has just registered at the same moment as the taste of the rice — her shoulders are beginning to rise at the chill, her chin dips a little, and she watches her own feet in the water with a soft smile forming. Three-quarter profile against the soft green shade. Around her ankles the current presses and splits, and where the water strikes her heels and the submerged stones it kicks up in lively little fountains — droplets springing up around her feet and rising past her shins toward her knees, hanging bright in the shaft of light, ripples V-ing away downstream. Candid, unposed, unaware of the camera — a friend watching from the bank.

Outfit: Simple summer clothes for a picnic by the stream. A compact short-sleeve bubble-hem top in clean white — the current trend silhouette: the bodice is a soft fine knit that follows her body, curving over the bust and draping from its outermost point with gentle natural tension, the front of the garment smooth and uninterrupted, nothing held or crossing in front of the chest; then below the bust the fabric flares lightly and gathers into a rounded balloon hem that cinches in at the natural waist, the rounded fold resting softly over the skirt's waistband. Fully opaque, no sheerness anywhere. The bust sits high and supported on the ribcage, as if wearing a well-fitted bra: its fullest point level with the mid-upper arm, roughly at armpit height, with only a short distance between the collarbones and the top of the curve — never sagging low toward the waist; the balloon volume begins only below it, so the reference-derived silhouette stays readable through the bodice. Below, a pale dusty-blue knee-length full cotton skirt, light and softly worn, its front hem tucked once into the waistband to stay gathered above her knees and clear of the water while she eats, the rest of the skirt spilling over the rock. No jewelry, no logos, no styling. Bare feet, her sandals off on the rock.

Expression: A little of the rice ball held in her mouth, and a soft, quietly delighted smile forming around it — the bitten corner just inside her lips, the corners of her mouth gently lifting around the bite, eyes softened into a warm happy squint: the small private thought, plain on her face, that it tastes wonderful. Nothing exaggerated — no wide grin, no open-mouthed delight; the pleasure stays small, demure and graceful. The first cold of the stream on her feet and the taste of the rice arriving together, a small honest smile that arrives before any pose, not a camera smile. Her face tips down toward her feet, softened by the reflected light off the water.

Hair: Maintain and translate the reference subject's hairstyle, hair colour, fringe and silhouette features exactly. A light upstream breeze lifts a few strands at the temples and nape; the rest rests naturally along her jaw and shoulders. Drifting coins of dappled light move on the hair without changing its reference-derived colour.

Lighting: Early-afternoon midsummer sun broken by the ravine canopy into shafts and drifting coins of light, the whole scene kept bright and airy — a light, high-key-leaning tonality where even the shade stays luminous and pale green, shadows open and gentle, never heavy or crushed. She sits where one broad shaft falls — bright dappled patches on her top, her skirt, the rock and the water — while the ravine around her rests in a light, luminous green shade. The water surface throws a cool trembling reflected light up under her chin, along her shins and onto the underside of the rock's edge — a soft underlight bounced off the stream. The rising spray and hanging droplets catch the shaft as a scatter of bright points — lit by the light, not light sources themselves. Direct sun never strikes her face as a hard band; her features are modeled by the dappled light and the water's bounce. Bright, refreshing and clear at first glance. No sweat anywhere — the cool reads through water, shade and green, not through skin. No HDR glow, no artificial fill, no heavy moody contrast.

Camera: 35mm prime lens at f/2.8, set low near the water surface a couple of metres downstream and slightly off to one side, looking gently up at her — a professional photographer's quick catch, the shutter pressed the exact second the moment happened: an unrepeatable stolen frame with deliberate composition and controlled light, not a posed setup. Her full figure from hair to dipped feet sits on the rock in the middle of the frame, the near foreground filled with a soft out-of-focus ribbon of bright water, the cascade and canopy dissolving into bright green bokeh above. Shallow depth of field: her softly smiling face, the petite rice ball at her lips, the tucked skirt hem, her shins and the rising spray tack-sharp; foreground water and background foliage soft. Natural perspective for hands and feet — a believable hand size, no exaggerated foreshortening. The overall exposure is bright and clean, whites luminous without blowing out, the green shade lifted and readable. True photographic realism in every respect — real light, real texture, real timing: natural sensor grain, no beauty filter, no SNS compression, no plastic skin.

Format: 9:16 portrait orientation, vertical full-body composition from hair to feet in water. Pro-grade detail: skin pores, individual hair strands, the fine knit of the bodice and the gathered folds of the balloon hem, the cotton weave of the skirt, water clarity with pebbles visible through it, the rice grains and crisp nori of the petite rice ball, the rising spray and droplets on her shins, the rock's grain and waterline moss — the depth, air and unposed truth of a single real frame caught by a professional photographer on a midsummer mountain stream.
```

---

## 投稿文例

> 渓流でおにぎりです。  
> 足は冷たい、おにぎりはあったかい。  
>
> 外で食べると、なんでもおいしいです。

---

## 設計メモ

### 既存案との差

- **12（屋上・缶ジュース）との差:** 12 は「冷たい缶を唇に当てる」小道具経由の涼、コンクリートの上の暑さ。本案は山の冷気の中で水そのものに足先を浸ける、容器なしの涼。体に触れる冷たさの部位を「唇」から「足先」へ移す（飲み物の代わりにおにぎりが口元に来るが、涼の担い手ではなく食べ物）。
- **18/356（河川敷の夜明け歩行）との差:** あちらは開けた河川敷を歩く動作と夜明けの逆光。本案は渓谷の岩に座って静止し、水に浸かる。
- **200（朝の庭・ホースの霧）との差:** 200 は水が「霧」として空気中に漂う透過の涼。本案は水に直接触れる接触の涼。
- **181（縁側スイカ）との差:** 夏の食べ物×涼という接点はあるが、181 は着古しキャミソールの緩みが主題のドキュメンタリー調。本案はバブルヘムのトレンド服と渓谷の水接触が主題。

### 媒質変奏シリーズにおける位置（水そのものへの接触）

- 199: **布**を通る逆光。200: **空気（霧）＋薄布**の二重透過。11: **ガラス**を通る朝光。12: **風**による布の離反。
- 28: **水そのもの**に足を浸ける。媒質が光のフィルターではなく、冷たさと反射光を直接運ぶ媒体になる。透過・離反に続く「接触」の一手。

### 二光源デバイス（356 の転用）

- 上からは木漏れ日のシャフトと光の玉（直接光の斑点）、下からは水面が跳ね返すクールな揺れる下光。356 が「上の直接光・下の透過光」を1主題に統一したのと同型を、渓谷の「木漏れ日・水面反射」に転用。顔には硬い直射帯を当てないガード入り。

### おにぎりの組み込み（手の再配置）

- 旧ポーズは両手が塞がっていた（裾を持つ＋岩に掌）。裾をウエストに一度タックして自立させることで手を解放し、片手＝おにぎり・片手＝岩に役割を再固定。服の特徴と仕草の接続（README 基準）は「裾を持つ」から「裾をタックして食事に備える」へ置き換わる。
- おにぎりは「角をひと口かじったあと」の出来事の途中。海苔半巻き・具は見せず白いご飯と海苔だけにし、包装・ブランド要素を排除。
- 予備のおにぎりを敷いたランチクロスを岩の上に添えて出処を自然にし、`duplicated objects` を Avoid に追加しておにぎりの増殖を防ぐ。

### 表情とおにぎりのサイズ（改訂履歴）

- 履歴: 咀嚼（頬の膨らみ）→ 微笑み（少しニコッ）→ 口に含んで笑う → 口に含んで「にこっ」→ **にこっに「おいしい」の内心を足し、お淑やかさで上限を固定**（最終）。`the small private thought, plain on her face, that it tastes wonderful` で美味しさの内心を滲ませつつ、`no wide grin, no open-mouthed delight; the pleasure stays small, demure and graceful` の収束ガードで大げさ化を防ぐ。
- 頬は膨らませないガードを併記（`cheeks easy and natural, never puffed`）。口に含んでいても頬が歪まないようにして顔崩壊を防ぐ。
- 作り笑顔への収束は `a small honest smile that arrives before any pose, not a camera smile` でガード（内心ベースの表情規約）。
- おにぎりは二口サイズの小ぶり（`petite, a two-bite size resting in her curled fingers`）を維持。顔と手の主役度を上げすぎず、微笑みと渓谷が主題のままにする。

### 飛沫の強化（改訂）

- 「足元の水飛沫をもう少し上げたい」要請に対し、流れが踵と水中石に当たって**小さな噴水状に立ちのぼる**指定へ強化（`kicks up in lively little fountains — droplets springing up around her feet and rising past her shins toward her knees`）。高さの目安を「膝に向かう」まで明示。
- 飛沫は木漏れ日のシャフトに照らされて明るい点の群れになる（`a scatter of bright points`）。発光体化ガード（`lit by the light, not light sources themselves`）は継続。
- カメラの焦点リストと Format のディテール要求にも `the rising spray` を連動させ、ボケずに描写させる。

### トーンの明るさ（改訂）

- 「コントラストは明るめに」の要請に対し、Lighting をハイキー寄りの明るいトーンに変更。渓谷の影は `deep` ではなく `light, luminous green shade` に緩和し、影の床を持ち上げる。
- 明暗の対比構造（木漏れ日のシャフト × 影）は残しつつ、影側を潰さない `never heavy or crushed` と、ムーディー化の抑制 `no heavy moody contrast` を明記。Camera にも露出の明るさ（`bright and clean, whites luminous without blowing out, the green shade lifted and readable`）を連動。

### 抜き取りの一瞬感（decisive moment）の強化

- 「本当にこの一瞬を抜き取った」感を出すため、カメラブロックに `the shutter pressed the exact second the moment happened: an unrepeatable stolen frame` を追加。プロのカメラマンの「早抜き」の一コマであることを明示。
- 抽象ネガ（AIっぽさの否定）は効かないので使わず（`ideas/README.md`「ネガは観測した失敗だけを具体で書く」）、`real light, real texture, real timing` の肯定形で実写感を積む。Format の締めも `the unposed truth of a single real frame` に強化。

### トップスのトレンド選定（バブルヘム）

- 「いつも同じ白リブフィット」からの変更依頼に対し、2025〜26年トレンドのバブルヘム（バルーン裾）を採用。胸元は従来どおり体に沿うソフトニットで、保持ルール（布が浮いてボリュームを消さない）と互換のまま、裾だけがギャザーで丸く膨らむ。
- バルーンのボリュームはウエストより下だけに限定し、`the balloon volume begins only below it` と明記して胸のシルエット潰れを防ぐ（`ideas/README.md`「箱型で張りのある生地は布が浮いてボリュームを消す」への配慮）。
- 不採用の2候補（フロントリボン半袖カーディガン × キャミ、ポロ衿コンパクトニット）は差し替え変数として保持。

### 涼の描写（expression/02 準拠）

- 汗は一切描かない。涼は水（流れ・飛沫・滴）、影（深い緑の渓谷）、光（木漏れ日の対比）で出す。渓谷の外が真夏のギラつきであることを一文で示し、中の冷気を対比で立たせる。

### 破綻対策

- **水中の足:** 「透き通った浅い水を通して両足がはっきり見える」「つま先は小石の上でリラックス」と指定し、水没した足の消失・変形を防ぐ。手と足に自然な遠近（no exaggerated foreshortening）を明記。
- **手の役割固定:** 片手は小さなおにぎりを口元に、もう片手は岩の上に平らに。手が目立つ構図（口元のおにぎり）なので冒頭の Avoid に `no extra limbs, extra fingers, malformed hands`。
- **胸潰れ対策:** 胸の前に何も来ないことを Pose/Outfit に明記（おにぎりは体の斜め横の口元へ）、ボディスは体に沿うニットでドレープ指定。バスト位置は共通テンプレートの高位保持ブロックを全文使用。

### 共通規約の適用

- 保持ブロック（Match the reference image exactly 〜 never add or hardcode 〜）を冒頭に全文配置。髪・顔・体型の中身は本文に書かず参照画像に語らせる。
- 成人条件の条件文を配置（`Use the trend top described below only if the reference is unambiguously adult`）。
- 表情は形容詞でなく内心（`the small private thought, plain on her face, that it tastes wonderful`）。
- 透けは一切使わない健全案（体を見せる要素なし）。

### 参照

- `ideas/362-371-refreshing-cool-ten.md` — 本案（365）の設計元。涼の源をばらすシリーズの全体方針
- `ideas/205-rooftop-juice-short-shadow.md` / `12-afternoon-rooftop-juice/prompt.md` — トーンの継承元（真夏の日常×一瞬の涼）
- `ideas/356-riverside-dawn-back-three-quarter.md` — 二光源デバイスの転用元
- `expression/02-summer-heat-realism.md` — 涼・暑さを環境で出す手法、実写感をカメラで出す手法の根拠
