# 29. 薄暗い白スタジオで、注いだ水がステンドグラスのひまわり畑になる（参照画像ベース）

`ideas/README.md` の人物参照方針に準拠し、人物の顔・髪・肌・体型・身長感・プロポーションなどの身体的特徴は参照画像から忠実に保持する（髪を含む身体特徴は本文にハードコードしない）。チャット上で反復改良した作業版をそのまま実生成用として採用した案（`ideas/` に設計元ファイルはなし）。非日常・幻想系の一手で、13・21 が「空」を別媒質（劇場アニメ）に差し替えたのに対し、本案は床側で**現実の物質そのもの（水）が別媒質（鉛線入りステンドグラス）へ変質する**。媒質変奏シリーズの観点では 28 の「水そのものへの接触」に続く「水そのものの変質」。薄暗い白スタジオで中型のガラスジャグから水を注ぐと、着地点で無音のままステンドグラスに変わり、その一点から放射状に扇形のガラス面が育って画面下半分を埋める。ガラスの中には現実には存在しないひまわり畑（内側から発光する花・金の光の川・オーロラと金箔の星空）が一枚ごとに描かれ、部屋で唯一の光源として素足と白い裾を金色に染める。

- **アスペクト比:** 16:9 横（床のガラス面と空間ごと見せる引きの画。人物は中央に全身）
- **見せ場:** ①接地点から放射状に「育つ」ステンドグラス — 同心円の鉛線、爪サイズ→大判へのパネルのサイズ勾配、鉛線を伝って外へ流れる熔けた色 ②ガラス内のひまわり畑 — 提灯のように内側から光る花、アンバーの宝石の花芯、太陽から流れ出す金の光の川、緑紫のオーロラと金箔の星々 ③下からの大聖堂光 — 宝石色のコースティクスが素の床と壁に揺れ、素足・足首・白い裾を金色に照らす
- **構図:** 人物は画面中央に全身、接地点は足元の一歩前。ガラスの扇は接地点を要として手前へ開き、左右下の三辺からフレームアウト。絵柄の太陽を接地点に一致させ、光と成長の起点を一点に束ねる
- **服装:** ミモレ丈の白ワンピース（完全不透明・体に沿う流れる織り・慎ましい襟元と短袖）。両足は常に見える丈
- **小道具:** 丸くふくらんだ胴・短い首・注ぎ口・ガラスの取っ手付きの中型ガラスジャグ（両手に自然に収まるサイズ）。片手は取っ手、もう片手は胴に添える
- **照明:** 低照度の白スタジオ（壁も床も柔らかい影に沈む）。床のステンドグラス自体が部屋で最も明るい唯一の主光源
- **文脈:** 非日常・幻想。夜投稿向き。透けを一切使わない健全案
- **差し替え変数:** ガラス内の風景（ひまわり畑 ↔ 彼岸花の川辺・オーロラの雪原・朝日の海）、ガラス内の空（トワイライト＋星 ↔ 純粋な星夜）、ワンピース色（白 ↔ 生成り）

---

## プロンプト

```text
Create a polished photorealistic full-body image from the uploaded reference.
Faithfully preserve the subject's apparent age, identity, exact face, skin,
hairstyle, body proportions, visible accessories, and shoes. Match the
reference exactly for body shape and lines, including chest and hip shape and
fullness, and reproduce the natural volume and silhouette of the bust and
hips through the fit and drape of the dress; the bust sits high and supported
on the ribcage, as if wearing a well-fitted bra: its fullest point is level
with the mid-upper arm, roughly at armpit height, with only a short distance
between the collarbones and the top of the curve — never sagging low toward
the waist. Do not beautify, reshape, age-shift, or invent personal details,
and never add personal features that are not present in the reference beyond
the dress described below.

Outfit: one elegant white dress in a soft, fluid weave that follows the body.
A modest neckline and gentle short sleeves; the bodice curves over the bust
and drapes from its outermost point with soft tension lines; the skirt flows
to mid-calf so both feet stay fully visible. The fabric is fully opaque with
a quiet sheen, and its white hem catches the jewel-colored light rising from
the glass on the floor.

Scene: in a dim, hushed white studio — plain white walls, a plain white
floor, nothing else in the space — the subject stands at the center of the
frame, holding a clear glass water jug with two natural hands: one hand on
its glass handle, the other cupped gently against its rounded body to steady
it. The jug is an elegant, softly rounded pitcher — a generously curved
belly, a short neck, a neat pouring spout, and a simple smooth glass handle —
of a modest medium size that sits naturally in her two hands, neither
oversized nor tiny, its crystal-clear walls catching faint sparks of the
jewel-colored light from the floor. She holds it low at waist level and
slightly forward, away from the chest, tipping it so a thin stream of plain
clear water falls from the spout toward the floor. The room is lit only by
soft, low ambient light, so its white surfaces fall into gentle shadow. The
water starts transparent, but in its lower reach, a short distance above the
floor, it begins to shimmer with iridescent opalescent color — the change
from water into stained glass already awakening in midair.

The stream lands on the bare floor a short step in front of her feet,
quietly and without any splash: the falling water is drawn into the glass
the instant it touches, melting into a small pool of glowing molten color,
as if the floor were gently drinking it. That single contact point is the
origin of everything: the stained glass visibly grows outward from this one
point and from nowhere else. Behind the contact point — around her feet and
back toward the walls — the floor stays bare dim white. The glass spreads
only forward, away from her, as one clean fan: a sector of a great circle
centered exactly on the contact point, its two straight edges radiating
crisply from that point, opening toward the camera and widening until it
runs off the left, right, and bottom edges of the frame, so the entire lower
half of the image becomes one continuous field of stained glass from edge to
edge.

Every detail of the glass shows that it grew from the contact point. At the
contact point the newest glass is still being born: the water melts
seamlessly into glowing molten glass, and threads of luminous color flow
visibly outward from it along the dark lead lines, feeding the farther panes
like veins of light. The lead came lattice is arranged radially around the
contact point — the nearest lead lines curve as tight concentric arcs, like
ripples frozen on quiet water — and the individual panes grow steadily
larger as the fan opens, from fingernail-sized chips beside the contact
point to broad jeweled panes at the frame edges.

Within the lattice it is unmistakably real leaded glass: dozens of separate
panes of handmade colored glass, each with its own ripples, seeded bubbles,
streaks, and opalescent swirls, some panes shifting between teal and violet
like dichroic glass, others holding flecks of gold leaf fused inside.
Together the panes form one continuous landscape, painted across the glass
so its lines continue over the lead divisions: an otherworldly sunflower
field that could never exist in this world, composed to radiate from the
contact point. A huge glowing low sun sits exactly at the contact point on a
tiny level horizon, so the point where the water lands is the sun of the
world inside the glass, and everything grows out from it: rays of light,
slow swirling cloud currents, and curving rows of towering sunflowers all
fan outward from the sun toward the viewer. The sunflowers glow from within
like paper lanterns, light veining their petals, each flower's center set
with a faceted amber glass jewel; the blooms nearest the camera are the
largest and face the viewer. A winding river of molten-gold light threads
out from the sun between the flower rows, and bright pollen lifts off the
field as drifting flecks of gold. Above the horizon the twilight sky holds
ribbons of green-violet aurora and a field of stars rendered as gold-leaf
flecks and tiny glass jewels, with one shooting star trailing gold across
several panes.

The glass is translucent and luminous as if lit from below — a cathedral
window at sunset laid flat on the floor — with jewel-like color pooling
along the lead lines, and it is the brightest thing in the room. Its light
spills beyond its edges: soft jewel-colored reflections and rippling caustic
patterns wash across the surrounding bare floor and faintly up the dim white
walls, and a warm golden glow rises over her bare feet, ankles, and the
white hem of the dress. The fan stays on the floor in front of her: it never
touches her feet and never climbs onto or merges with the dress. Show the
glass jug, the entire stream with its iridescent lower reach, the quiet
contact point, and both feet standing on the dim white floor clearly, with
the stained glass filling the whole lower frame. The space stays empty — no
furniture, no props, no other objects, nothing except the subject, the
water, and the stained glass.

Hero visual: in a dim white room, plain water poured from a rounded glass
jug turns iridescent in midair and blooms, from its single quiet point of
contact with the floor, into a great radiant fan of leaded stained glass —
ripple-arcs of lead spreading from the landing point, molten color still
flowing outward along the lead lines, and an entire impossible sunflower
field alive pane by pane, its glowing sun sitting exactly where the water
lands. The glass is the brightest thing in the room: its warm golden light
washes across the dim floor, the subject's feet, and the hem of the white
dress, while the white walls fall back into soft shadow. Format: 16:9, wide
horizontal composition. No laboratory beaker, measuring cup, or plain
straight-sided tumbler; no splash crown, flying droplets, or spray at the
contact point; no amoeba-shaped or blobby outline, no scattered separate
puddles, no paint splash, no flat printed picture, carpet, rug, or photo
decal on the floor, no rectangular sheet of glass, no glass behind her heels
or wrapping around her feet, no uniform grid of same-sized panes, no bright
even studio lighting, no furniture or props, no miniature model, portal
ring, floating island, second person, text, logo, watermark, extra limbs, or
malformed hands.
```

---

## 投稿文例

> 床にお水をあげてみました。  
> ひまわりが咲きました。  
>
> 明日もあげたら、増えるでしょうか。

---

## 設計メモ

### 経緯と位置づけ

- チャット上で反復改良した作業版プロンプトを、そのまま 29 として採用（`ideas/` に設計元ファイルはない直接採用）。
- **13・21（アニメの空）との差:** あちらは「空」を別媒質に差し替える媒質混交。本案は床側で、現実の物質（水）そのものが別媒質（鉛線入りステンドグラス）へ変質する。
- **28（渓流足浸し）との差:** 28 は水は水のまま、冷たさと反射光を運ぶ「接触」。本案は水が固体の発光媒質へ変わる「変質」。媒質変奏シリーズ（199 布透過 → 200 霧透過 → 11 ガラス透過 → 12 風離反 → 28 水接触）の次の一手。
- **17（夜の庭イルミネーション）との差:** どちらも「夜・唯一の光源」だが、本案は光源を自分が注いだ水から生む。人物が光の作り手になる。

### 成長の可視化（v1 の観測失敗と対策 — 本案の核心）

初回生成では、ガラスが足元を回り込んで広がり、均一サイズのパネルが並ぶ「敷かれた絨毯/デカール」に見えた（=接地点から広がった感じがしない）。対策として「すべてのディテールが接地点起源を証言する」構造に組み替えた:

- 接地点を「唯一の起源」と宣言（`the origin of everything … from this one point and from nowhere else`）し、**足元と背後の床は素の白床のまま**と肯定形で固定。
- 扇の幾何を「接地点を中心とする円の扇形」（`a sector of a great circle centered exactly on the contact point`）と再定義。
- 鉛線の格子自体を放射状に: 接地点近傍は**波紋のような同心円アーチ**、そこから外へ向かって放射。
- パネルの**サイズ勾配**: 接地点そばは爪サイズ → フレーム端で大判（`from fingernail-sized chips … to broad jeweled panes`）。格子の構造だけで成長方向が読めるようにする。
- 進行形の描写: 接地点では最も新しいガラスが生まれつつあり、**熔けた光る色が鉛線を伝って外周のパネルへ流れ込んでいる**（`threads of luminous color flow visibly outward … feeding the farther panes like veins of light`）。
- 絵柄の**太陽を接地点に一致**させ（水の落ちる点=ガラス内世界の太陽）、光線・雲の渦・ひまわりの列がすべてそこから放射。明るさの勾配と成長の起点が一点に束なる。
- ネガに観測失敗を具体で追加: 絨毯/ラグ/フォトデカール、長方形シート、踵の後ろへの回り込み、均一グリッド。

### 幻想度の強化（v1 からの追加）

- **ガラス工芸のディテール:** 金箔の封入、見る角度で青緑↔紫に転ぶダイクロイックガラス、ひまわりの花芯にファセットカットのアンバーガラスの宝石、気泡・ストリーク・オパールセントの渦。
- **風景:** 提灯のように内側から光り花弁に光の葉脈が走るひまわり（手前ほど巨大で正面向き）、太陽から花列の間を縫って流れ出す熔けた金の光の川、立ちのぼる金の花粉、緑紫のオーロラのリボン、金箔と小さなガラス宝石で描いた星々、数パネルを横切って金を曳く流れ星。
- **部屋への波及:** 「夕日の大聖堂の窓を床に寝かせた」下からの光、宝石色のコースティクスが素の床と薄暗い壁に揺れ、素足・足首・白い裾に金色の照り返し。部屋で最も明るいのはガラス、という光源の主従を明記。

### 器の改訂履歴

- `one clear glass cup` → **ビーカーに見える**失敗を観測 → 細身のカラフェ → ユーザー提供の参照画像により**丸くふくらんだ胴・短い首・注ぎ口・ガラス取っ手付きの中型ジャグ**に確定。
- サイズは「大きすぎず小さすぎず」の要請を肯定形で固定: `a modest medium size that sits naturally in her two hands, neither oversized nor tiny`。
- 持ち方を役割固定: 片手=取っ手、もう片手=丸い胴に添える。ジャグは腰の高さ・体の前方（胸から離す）で保持し、胸前を横切らせない（README の胸潰れ対策）。
- ネガに観測失敗を追加: `no laboratory beaker, measuring cup, or plain straight-sided tumbler`。

### 着地の静音化（飛沫の抑制）

- 「着地点の水飛沫を抑えたい」要請に対し、着地を**無音・無飛沫の吸い込まれ**に置換: `quietly and without any splash: the falling water is drawn into the glass the instant it touches … as if the floor were gently drinking it`。
- splash 系の語彙（splash crown 等の肯定描写）を本文から全除去し、比喩も `ripples frozen on quiet water` へ差し替え。
- ネガに `no splash crown, flying droplets, or spray at the contact point` を追加。28 が飛沫を「強化」した案なのに対し、本案は逆方向の調整。

### 破綻対策

- **手:** `two natural hands` ＋取っ手/胴の役割固定。手が主役級に写るため Avoid に `extra limbs / malformed hands`。
- **足:** ミモレ丈で両足常時可視、`both feet standing on the dim white floor clearly`。ガラスは足にも裾にも触れない・登らない・混ざらないを明記。
- **シルエット:** アメーバ状/ぶよぶよの輪郭、散らばった水たまり、ペンキの飛沫を引き続き除外。扇の直線エッジは `radiating crisply` で保つ。
- **光:** 明るい均一なスタジオ光を除外し、「薄暗い部屋で床のガラスが最も明るい」光の主従を肯定形＋ネガの両面で固定。

### 共通規約の適用

- 保持ブロックは本案系統の文言（`Create a polished photorealistic full-body image from the uploaded reference …`）だが、README 必須要素をすべて含む: `chest and hip shape and fullness`、フィットとドレープ経由のボリューム再現、バスト高位保持ブロック全文、美化・年齢改変・改変の禁止、参照にない個人的特徴の追加禁止。
- 参照にない要素のハードコードなし（ドレスとジャグはシーン指定物として明示。髪色・顔立ち等は参照画像に語らせる）。
- ネガは観測した失敗だけを具体で記載（ビーカー化・飛沫・絨毯化・回り込み・均一グリッドはいずれも実際の生成/要請で観測済み）。
- 透けなしの健全案のため expression/01・02 は不使用。

### 参照

- `ideas/README.md` — 保持方針・記述規約・アスペクト比指針
- `13-fullmoon-lake-anime-reflection/` `21-lakeside-meteor-shower-anime-sky/` — 幻想系（媒質混交）の先行
- `28-afternoon-stream-feet-soak/prompt.md` — 媒質変奏シリーズの前段（水接触）と本フォルダ体裁の直近例
