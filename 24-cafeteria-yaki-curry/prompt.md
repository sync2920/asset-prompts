# 24. レトロなカフェテリアで焼きカレー、伸びるチーズの一口（参照画像ベース）

`ideas/README.md` の人物参照方針に準拠し、人物の顔、髪、肌、体型、身長感、プロポーションなどの身体的特徴は添付画像から忠実に保持する（髪を含む身体特徴は本文にハードコードしない）。ただし髪型は依頼指定でお団子へ変更し、`16`/`17` のハーフアップ方式（色・質感・前髪・顔まわりの後れ毛は参照から保持し、アレンジだけを変更する）を転用する。ちょっとレトロで明るいカフェテリアの窓際、焼きカレーのスプーンを口に運ぶまさにその瞬間を切り取る。器からスプーンへ伸びるチーズの糸と、窓からの斜光に浮かぶ湯気をヒーロー視覚にする。汗は `expression/02-summer-heat-realism.md` 準拠で「こめかみと生え際のうっすらした艶」までに固定し、暑さは湯気・冷水グラスの結露・窓外の硬い日差しで運ぶ。Tシャツは目の詰まった完全不透明で、汗で濡れても透けず湿った斑も出ないことを明記する。

- **アスペクト比:** 3:4 縦
- **見せ場:** 口に運ぶスプーンから器へ伸びるチーズの糸と、斜光を受けて立ちのぼる湯気。人物の表情（期待に目を細める＋うっすら汗）はこのヒーロー視覚のすぐ上。衣装の見せ場は作らず引き算。
- **構図:** テーブルの向かい側・右斜め前からテーブル高すぐ上で。茶フォルマイカのテーブル縁と楕円のグラタン皿を左下の前景に大きく入れ、スプーンとチーズの糸が中央を立ち上がり、顔を右上の三分点に。窓は左後方。
- **髪型:** 指定でお団子（ひとつ・高めの後頭部・柔らかくほぐしたボリューム・うなじに細い後れ毛）。色・質感・前髪・顔まわりの後れ毛は参照のまま。
- **服装:** 淡いアイスブルーの半袖ファインリブT（目の詰まった完全不透明、汗で透けない・斑が出ない）＋サンドベージュのコットンショーツ。涼しいカジュアル。
- **背景:** クリーム漆喰×ミントグリーンのタイル腰壁、茶フォルマイカ×クローム縁のテーブル、モザイクタイル床、ガラスケースのあるカウンターと文字の読めない手書きメニューボード。15時の白い西日が窓から差し、湯気に当たって光の筋になる。冷水グラスは結露。
- **照明:** 窓の斜光が主光（器・湯気・テーブル）。顔は光の筋から外し、室内の明るいバウンスで均一に。頬・鼻・額にハードな帯・ホットスポットを作らない。
- **文脈:** 熱いと分かっていても待てない一口 × レトロで明るい食堂 × 湯気とチーズの素材研究 × プロの一瞬

---

## プロンプト

```text
A highly detailed photorealistic portrait of the person from the reference image. 3:4 vertical aspect ratio. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode features that are not present in the reference image — no invented hair colors, accessories, uniforms, or props. Adult reference only; otherwise keep the same scene with the same fully opaque tee.

Hair: Keep the reference hairstyle's identity exactly — the same color and tone, the same texture and natural wave, the same wispy fringe across the brow, and the same loose face-framing strands — but change only the arrangement: gather all the remaining hair up into one rounded bun sitting high on the back of the crown, full and softly teased with airy volume rather than pulled tight, a few fine escaped strands at the nape. The fringe and the face-framing strands stay untouched. The bun reads as a casual summer updo, not a formal style.

Pose: Three in the afternoon in a slightly retro Japanese cafeteria, seated at a small window-side table, caught at the exact moment of carrying the first spoonful of yaki-curry to her mouth. She leans a touch forward over the oval gratin dish; the spoon rises from the dish to just in front of her opening lips, and a glossy strand of melted cheese stretches unbroken from the browned surface of the curry up to the spoon. Her eyes are on the spoon, bright and narrowing a little against the rising steam, brows lifted in anticipation — the face of someone who knows it is too hot and cannot wait anyway, half laughing at her own impatience. A faint, even sheen of perspiration sits at her temples and hairline, kept subtle; the summer heat reads mostly through the steam, the condensation on her water glass and the hard daylight outside. Her free hand rests at the table's edge — nothing held in front of the chest, the dish stays on the table below collarbone height. Candid, unposed, caught mid-moment, unaware of the camera. No extra limbs, extra fingers, or malformed hands; no beads of sweat, no drips.

Outfit: A short-sleeve fine-rib tee in pale ice blue — a soft but densely knitted cotton, completely opaque, and it stays that way even where the summer heat and her faint perspiration touch it: no damp patches, no translucent spots, the surface reading evenly dry with only the knit's texture and the play of light on it. The knit follows the body: it curves over the bust and drapes from its outermost point with gentle tension lines. The bust sits high and supported on the ribcage, as if wearing a well-fitted bra: its fullest point is level with the mid-upper arm, roughly at armpit height, with only a short distance between the collarbones and the top of the curve — never sagging low toward the waist. Sand-beige cotton shorts, casual and cool. No jewelry, no logos, no styling beyond the tee itself.

Background: A small, slightly retro Japanese cafeteria kept bright and cheerful at three in the afternoon. Cream plaster walls above a mint-green tile wainscot, brown formica table tops with slim chrome edges, wooden chairs, a mosaic tile floor, and a service counter with a glass case and hand-written menu boards whose lettering stays illegible — no readable text anywhere. A large wood-framed window behind and to her left pours in bright mid-afternoon sun, still high and white rather than golden, the light leaning in from the west; one visible shaft of daylight angles across the table and catches the steam rising from the dish, turning it into a glowing, textured ribbon between the dish and her chin. The other tables stand empty — no diners, no staff, no blurred figure, no silhouette, no human shape of any kind in the background or in the bokeh; the room's lived-in feel comes only from objects: a napkin holder and a sauce bottle on the table, the counter's glass case, a tall glass of iced water beside her sweating heavy condensation. Her face stays out of the direct sunbeam, lit by the room's bright, even bounce — no harsh streak, no hotspot or bright patch on the cheek, nose or forehead. Palette: cream, mint green, formica brown, golden browned cheese, pale ice blue, hard white daylight.

Camera: 50mm prime at f/2.0 from her front-right across the table, at just above table height. The brown formica edge and the oval gratin dish enter large from the lower-left foreground; the spoon and its stretching cheese strand rise through the centre; her face sits on the upper-right third with the bright retro interior soft behind. Shallow depth: the spoon, the cheese strand and her face tack-sharp, the steam carrying real wispy structure; the counter, menu boards and far tables melt to clean bokeh that contains no human figure of any kind. Real skin — pores and fine peach-fuzz along jaw, neck and collarbone, the faint sheen at her temples exactly as specified. Natural sensor grain, true color, no HDR, no beauty filter, no smoothing, no elongated body.

Format: 3:4 portrait orientation, vertical composition.
```

---

## 設計メモ

### 採用経緯
- 15時ごろ投稿用の依頼で、チャットに3案（並木道の日傘・公園の水飲み場・扇風機の前、365〜367候補）を提示したあと、仕様指定で「カフェテリアの焼きカレー」に決定。365候補として設計し、生成実行のため `24` として保存。保留の3案は未保存のまま。
- 依頼指定の反映: 人物参照＋髪型はお団子指定 / カフェテリアは室内・ちょっとレトロ・雰囲気は明るい / 少し汗を滲ませるが美味しい感じ / 汗で過度に透過しない服装 / 涼しいカジュアル / まさに口に運んでいる瞬間。

### 髪型指定の方法（16/17 方式の転用）
- 髪型の変更は「参照のアイデンティティ（色・質感・前髪・顔まわりの後れ毛）は保持し、arrangement だけを変える」と明文化するのが `16`（ハーフアップ）で確立した方式。これをお団子に転用し、ひとつ団子・高めの後頭部・柔らかいボリューム・うなじの細い後れ毛と指定。ツインお団子への変更は差し替え変数として残す。
- 髪色・髪質そのものは本文に書かず、添付する参照画像に語らせる原則は維持。

### 汗の設計（expression/02 準拠）
- 肌の汗は「こめかみと生え際のうっすらした艶（a faint, even sheen）」までに固定。`11` で汗の粒・一筋の汗・Tゾーンの湿り気を入れて「汗かきすぎ」の破綻が出た観察があり、今回も `no beads of sweat, no drips` を観測済みの失敗として具体的に否定。
- 暑さの主役は環境へ: 器から立ちのぼる湯気（窓の斜光で可視化）、冷水グラスの結露、窓外の硬い白い日差し。汗はあくまで仕上げの気配。

### 服装の透過防止
- 「涼しいカジュアルだが汗で透けない」の要件を、目の詰まったファインリブ編み＋完全不透明＋`no damp patches, no translucent spots` の明記で担保。淡いアイスブルーは汗ジミが目立ちにくい色として選定（グレー系は斑が読まれやすいので回避）。
- 見せ場は衣装に作らず、チーズの糸・湯気・表情に集約。ただしバストの高い位置指定と布の挙動（curves over the bust, drapes from its outermost point）はシルエット維持のため標準どおり残す。

### ヒーロー視覚と構図
- 「まさに口に運んでいる」を、器からスプーンへ切れ目なく伸びるチーズの糸で可視化。糸が器と口をつなぐことで動作の途中感が出る。湯気は顔の前ではなく器と顎の間を立ち上がらせ、窓の斜光の筋に乗せて光らせる。
- 表情は形容詞でなく内心（熱いのは分かっている、でも待てない。自分のせっかちに半分笑っている）。

### 顔の光対策（358 と同型）
- 窓の斜光は器・湯気・テーブルを照らす主光とし、顔は光の筋から外して室内の明るいバウンスで均一に。`no harsh streak, no hotspot or bright patch on the cheek, nose or forehead` を Background に明記。

### 文字の処理（22 と同型）
- 手書きメニューボードはレトロ感の要だが、AIの造語文字を防ぐため `lettering stays illegible — no readable text anywhere` と明記（`22` の本の背表紙と同じ処理）。

### 他者を写さない設計（358 と同型）
- 他のテーブルは空席とし、客・店員・ぼけたシルエット・人影を一切否定。生活感はナプキンホルダー・ソース瓶・ガラスケースなどの物だけで出す。

### 手の解剖学ネガ
- スプーンを持つ手が画の主役級になる構図のため、`no extra limbs, extra fingers, or malformed hands` を Pose 内に配置。

### 差し替え変数
- 焼きカレーの具（チーズの焦げ目・卵の有無）、Tシャツの色、タイルの色（ミント/クリーム）、窓の方位、汗の気配の強さ、お団子の数（ひとつ/ふたつ）。
