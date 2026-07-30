# 画像生成AIに直接投げるランダムプロンプト（第2弾・拡張版）

別のメタプロンプトを経由せず、**生成先へ1ブロックのまま貼って、生成のたびに中身を変える**形式。
[prompt.md](prompt.md) の場面案を、直接投げでも矛盾しにくい24枚の **scene card** へまとめ直した。
①と③では同じ1〜24のカードを同じ順番で使い、②はそのうち6枚だけを示すサンプル。

> prompt.md は、有効候補を絞ってから服・光・時間・カメラ等を組み立てる正典。
> こちらは、それらをscene card内で確定させた直接投げ用の簡略版。

| 形式 | 対象 | ランダムの実体 |
|---|---|---|
| ① `{a\|b\|c}` 版 | SD WebUI(A1111/Forge) + Dynamic Prompts、ComfyUI + 対応ノード | 拡張機能の乱数で1枚ごとに1つ抽選 |
| ② `{a, b, c}` 版 | Midjourney | 全組み合わせを別ジョブとして一括生成 |
| ③ 自己完結文章版 | ChatGPT / Gemini / nano-banana 系 | モデル自身に選ばせる |

---

## 設計の肝：顔造作は独立、場面条件はscene cardに閉じる

顔は、**輪郭・目・眉・鼻・口・顎だけを記した中立な顔造作8種**から選ぶ。
年齢、顔のアクセント、体型、髪色、髪型はそれぞれ独立。顔造作に表情・視線・メイク・髪を含めないため、
scene cardが求める演技や仕草と競合しない。

一方、時間帯・季節・天気・視点・カメラ・主な焦点は、場面から切り離すと矛盾しやすい。
そこで **場面・仕草・光・環境条件・構図を1枚のscene cardにまとめて24種**用意した。
①のDynamic Promptsは意味を読んで矛盾を直せないため、これらを独立スロットには戻さない。
服装指定のないカードでは、場面・季節に合う無地の普段着を使う。

scene cardの番号は①②③で共通:
1-4 きっかけ / 5-9 生活の手元 / 10-14 気配のツーショット / 15-18 天気の変わり目 /
19-22 マジックリアリズム / **23-24 大人っぽい（L2.5）**

※第一弾(random/)の基本トーン（上品/スタイリッシュ/だらしない/元気/気だるげ/レトロ）は
第二弾から削除済み。第二弾は「きっかけ/生活の手元/気配のツーショット/天気の変わり目/
マジックリアリズム/大人っぽい」の6群のみ。両方を使うことで重複せずに幅が広がる。

直接投げ版のラベル付き抽選状態数 =
年齢4 × 顔造作8 × 顔アクセント8 × 体型8 × 髪色4 × 髪型10 × scene card 24
= **1,966,080状態**。

これは抽選ラベルの状態数であり、画像上の違いが同じ数だけ現れる、または均等に分散するという保証ではない。
顔アクセントの「なし」4枠は、アクセントを付けない確率を高くするための重み付け。

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
Professional fashion editorial photograph. A {23|24|25|26}-year-old adult Japanese woman, fully clothed.
Face anatomy: {a soft round face with full cheeks, large round eyes with narrow double lids, gently arched brows, a low straight nose with a rounded tip, a small mouth with softly full lips, and a short rounded chin|a balanced oval face, almond-shaped eyes with natural creases, straight medium-thickness brows, a slim straight nose, a defined cupid's bow, and a gently tapered jaw|a heart-shaped face with a slightly broad forehead, wide-set downturned eyes with shallow creases, softly curved brows, a short narrow nose, a fuller lower lip, and a small pointed chin|a softly square face, long monolid eyes, straight low-set brows, a straight nose with a low bridge and defined tip, a wider mouth, and a softly defined square jaw|a long narrow oval face, deep-set hooded eyes, slightly arched brows, a longer straight nose, thin well-defined lips, and a narrow rounded chin|a face with broad high cheekbones and a shorter lower half, narrow almond-shaped eyes with subtle double lids, horizontal brows, a compact nose with a rounded tip, a wide mouth, and a softly tapered jaw|a compact V-shaped face, upturned eyes with clear creases, gently angled brows, a high narrow nose bridge, a defined upper lip with a fuller lower lip, and a sharp small chin|a naturally asymmetric oval face, one eyelid slightly heavier than the other, brows at subtly different heights, a straight nose with a soft off-center tip, a slightly uneven lip line, and a gently defined jaw}.
Facial accent: {a small beauty mark under one eye|a small beauty mark near one corner of the mouth|faint freckles across the nose and upper cheeks|a single dimple visible only if the selected scene naturally includes a smile|no additional facial accent|no additional facial accent|no additional facial accent|no additional facial accent}.
Build: {a slender petite build|a healthy natural build with relaxed posture|tall and long-limbed with an elongated silhouette|petite with a natural figure|an athletic toned build|a soft natural build|a lean editorial model build|a fine-boned frame}.
Hair: {jet-black|dark brown|beige brown|soft ash brown} {short bob with blunt bangs|medium layered hair with airy movement|long glossy straight hair center-parted|a loose wavy perm with soft volume around the cheeks|a high ponytail with loose strands at the temples|a messy top bun with loose ends|a wolf cut with choppy layers framing her face|a long blunt one-length cut|a half-up style|medium-length hair pulled behind one ear}.
Unless the selected scene card specifies an outfit, she wears plain, unpatterned everyday clothing appropriate to that scene, season, and weather.
Scene card: {Her fingers stop halfway to tucking her hair behind one ear as she notices the camera, her half-lowered eyes catching the lens in a doorway. Clear late-spring afternoon, warm side light, intimate 50mm waist-up framing, focus shared by her face and the paused hand|She tips her face up to use eye drops, lashes just about to blink beside a window. Quiet overcast morning in early summer, soft neutral window light, 85mm close portrait, focus on the eyes and small bottle|She struggles with a necklace clasp, one hand resting at the nape while she asks for help with a glance. Autumn evening inside her apartment, warm neutral room light, medium rear three-quarter framing, focus on the clasp and her glance|She has just removed her glasses and holds them half-folded while her unfocused bare eyes search for the lens. Calm winter morning by a window, soft overcast daylight, intimate 85mm upper-body portrait, focus on her eyes and the glasses|She tastes miso soup from a small dish with her eyes naturally closed, a thin line of steam rising from the pot. Cold winter morning in a lived-in kitchen, low neutral sunlight, 50mm side-profile medium shot, focus on her face and steam|She draws an unfinished shape on a condensation-covered window, the outside visible only through the traced lines. Overcast winter afternoon, cool natural daylight, 50mm side view with the window and upper body visible, focus on fingertip and clear lines|She presses an iron across a white shirt as a brief burst of steam catches the light. Rainy-season morning in a tidy room, neutral window light, 50mm medium-wide documentary framing, focus on hands, iron, and steam|She pours hot water in a slow circle over hand-drip coffee during the bloom. Clear early-autumn morning in a quiet kitchen, warm neutral daylight, 50mm medium shot from beside the counter, focus on her hands and swelling grounds|She wipes the leaves of a houseplant one by one with a soft cloth. Mild spring afternoon, clean green-tinted window light, 50mm medium shot from across the room, focus on careful fingertips and leaf texture|From the viewpoint of someone beside her, she holds a melting ice-cream bar toward the lens while searching her bag without looking at the camera. Bright midsummer midday in dappled shade, 35mm close documentary framing, focus shared by her hand and face|She runs toward a self-timer a few steps before arriving, hair beginning to blur as she laughs. Clear summer evening in a park, camera fixed at waist height, 35mm full-body environmental frame, focus on motion and approaching figure|From the viewpoint of someone beside her, she offers one earphone, its cord setting the distance between them. Late-afternoon train seat in early autumn, soft neutral window light, 50mm intimate two-person viewpoint, focus on the earphone and her face|Across a cafe table, she holds out a spoonful one step before saying “ah” and starts laughing before it reaches the lens. Clear spring afternoon, soft cafe window light, 50mm seated medium shot, focus on the spoon and natural smile|She sleeps in the passenger seat while the car waits at a red light; the signal remains a small localized reflection outside the clean neutral cabin. Summer night, 85mm side-profile portrait, focus on her resting face, natural color balance without a red wash|She looks from the first raindrop on dry asphalt up toward the sky, her hair still dry. Late-summer afternoon just before a shower, overcast sky, 35mm full-body street documentary frame from across the road, focus on her movement and the first dark spot|She waits at an unattended crossing where the rails dissolve into heat shimmer. Clear midsummer noon, lowered barrier, high white daylight, 35mm environmental full-body frame, focus on the figure, tracks, and visible heat distortion|Her figure emerges from several meters away on a tree-lined road in dense fog, streetlights softened into pale spheres. Late-autumn dawn, long-lens full-body environmental frame, focus on her silhouette and the layered fog rather than a close facial portrait|She has ducked under an awning as hail bounces from the pavement, surprise halfway into laughter. Early-spring afternoon under a stormy overcast sky, 35mm medium-wide documentary frame, focus on her reaction and the white pellets|At an ordinary breakfast table, steam from a cup rises as one tiny floating cumulus cloud. Clear autumn morning, neutral window light, 50mm tabletop medium frame from across the table, focus shared by her face, cup, and impossible cloud|She walks empty-handed on a sunny sidewalk while only her shadow holds an umbrella. Clear spring midday, slightly high 35mm full-body frame with the complete shadow visible, focus on the relationship between her and the shadow|Beside a goldfish bowl in a bright daytime room, only the water inside the bowl contains a star-filled night sky. Quiet summer afternoon, neutral window light, 50mm medium composition including her and the entire bowl, focus shared by her reaction and the water|Inside an old elevator, one unfamiliar extra button appears on the floor panel and her fingertip pauses above it. Autumn evening under clean neutral interior light, close over-the-shoulder 50mm framing, focus on fingertip, button, and partial profile|Mature and composed in a white blouse and long pleated skirt, she stands beside a tall studio window as backlight glows along the fabric's edge. Clear spring morning, clean white studio shadows, 85mm three-quarter portrait, focus on her face and the garment silhouette|Mature and composed in a matte silk-blend high-neck dress, she sits beside a hotel window as the fabric falls quietly. Calm autumn morning, soft overcast daylight and a bright room, 85mm seated three-quarter portrait, focus on her face and the dress's clean lines}.
Photorealistic raw photo in natural color with realistic neutral color balance, natural skin texture with visible pores, authentic candid feel, clean frame edges, 3:4 vertical composition, highly detailed. Never black-and-white, monochrome, grayscale, or sepia. No red, orange, or magenta light leak, colored edge fog, or colored haze.
```

### ネガティブプロンプト（固定）

> ⚠️ **ネガティブに `minor` `nudity` 等を書くと、フィルタは否定を解釈せずその語自体を検出して弾く。**
> 詳細と対策は [safe.md](../random/safe.md)。

```
anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like face, mannequin, distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs, harsh flash, blown highlights, heavy makeup, black and white, monochrome, grayscale, sepia, red light leak, orange light leak, magenta light leak, colored edge fog, colored haze, watermark, text, logo, low resolution, blurry
```

### 回し方

- **Batch count を 8〜16 に上げて、Seed は -1（ランダム）** → 1クリックで全部違う子が出る
- L2.5のカード（最後2つ = 23・24）だけ回したい → scene cardから他を消す
- 特定の場面群だけ回したい → 該当するscene cardだけ残す（番号は「設計の肝」の対応表を参照）
- 特定の顔造作だけ回したい → Face anatomyの候補を1つだけ残す
- 季節を固定したい → その季節のscene cardだけ残す。独立した季節スロットは追加しない

### 便利な追加構文

```
{2::A|1::B}        A が B の2倍出やすくなる（特定のscene cardや顔造作を厚くしたい時など）
{1-2$$A|B|C}       1〜2個を選んで連結
__jp2_scene__      wildcards/jp2_scene.txt から1行ランダム抽選
__jp2_face__       wildcards/jp2_face.txt に顔造作候補を外出しして管理する場合はこちら
```

---

## ② `{a, b, c}` 版 — Midjourney

Midjourney の `{}` は**抽選ではなく全組み合わせを別ジョブとして生成する**（Permutation Prompts）。
組み合わせ数がそのままジョブ数になり、上限40。**card内のカンマは `\,` でエスケープが必須**。

スロットを増やすとジョブ数が掛け算で増えるので、実用上はscene cardの1スロットだけにするのが安全。
以下は24枚をすべて収録した版ではなく、scene card **1・5・10・15・19・23だけを使う6scene sample**。
顔造作・年齢・体型・髪のPermutationスロットは、このサンプルには含めていない。

```
Professional fashion editorial photograph, an adult Japanese woman fully clothed in plain unpatterned clothing appropriate to the selected scene and season, natural skin texture, natural color and neutral color balance, {her fingers stop halfway to tucking her hair behind one ear as she notices the camera\, clear late-spring afternoon\, warm side light\, intimate waist-up framing, she tastes miso soup from a small dish with her eyes naturally closed\, cold winter morning in a lived-in kitchen\, low neutral sunlight\, side-profile medium shot, from the viewpoint of someone beside her she holds a melting ice-cream bar toward the lens while searching her bag\, bright midsummer midday in dappled shade\, close documentary framing, she looks from the first raindrop on dry asphalt up toward the sky\, late-summer afternoon just before a shower\, full-body street frame, at an ordinary autumn breakfast table the steam from a cup rises as one tiny floating cumulus cloud\, neutral morning window light\, tabletop medium frame, mature and composed in a white blouse and long pleated skirt beside a tall studio window\, clear spring morning\, clean white shadows\, three-quarter portrait}, clean frame edges --ar 3:4 --style raw --no anime, illustration, 3d render, plastic skin, deformed hands, extra fingers, black-and-white, monochrome, grayscale, sepia, red light leak, orange light leak, magenta light leak, colored edge fog, colored haze, text, watermark
```

- 24枚全部を回したい場合は、①または③と同じ順番で残り18枚を追加する（24ジョブになる）
- 顔造作・体型・髪もPermutationへ足す場合は、そのぶんジョブ数が掛け算になる点に注意（6scene × 3顔造作 = 18ジョブ）
- Midjourney は Seed 未指定なら毎回ランダムなので、同じプロンプトを再送するだけでも人物は変わる
- `--c 15〜40`（chaos）を足すとグリッド4枚のあいだのばらつきが増える。`--weird` は写実が崩れやすいので非推奨

---

## ③ 自己完結文章版 — ChatGPT / Gemini / nano-banana 系

画像生成前のチャット推論で候補をサイレント抽選し、**選択済みの内容だけ**を画像生成ツールへ渡す1ブロック直投げ版。
候補一覧を別メッセージへ分ける必要はない。

```
以下の条件で写真を1枚生成してください。

【サイレント抽選と画像生成ツールへの受け渡し】
1. 会話内に【顔造作】1〜8と【scene card】1〜24の2つのshuffle bagを持つ。各bagを偏りなく並べ替えて先頭から1つずつ使い、使い切ったら全候補で新しいbagを作る。同じ依頼で複数枚作る場合も1枚ごとに1つ消費する。
2. 会話履歴や使用済み番号が参照できない場合は、【顔造作】8候補と【scene card】24候補をそれぞれ等確率として1つ選ぶ。リストの先頭を優先しない。
3. 【年齢】【顔のアクセント】【体型】【髪色】【髪型】は互いに独立した候補として、各リストから1つずつ偏りなく選ぶ。これらは直前と同じでもよい。
4. scene cardには時刻・季節・天気・視点・カメラ・主な焦点が含まれている。競合する別条件を追加しない。表情と視線もscene cardに従う。
5. 内部で選択を完了してから、選択済みの要素と【共通】だけを自然な一つの完成プロンプトへ書き直して画像生成ツールに渡す。候補一覧、未選択候補、番号、抽選手順、説明文は画像生成ツールへ渡さない。
6. 選んだ番号や完成プロンプトは表示せず、生成した画像だけを返す。

被写体: 23〜26歳の日本人女性（成人）。全身きちんと着衣した自然な生活または撮影シーン。肌は加工しすぎない自然な質感。顔造作は輪郭・目・眉・鼻・口・顎だけに反映し、性格・表情・メイク・髪を顔造作から推測しない。

【年齢】1.23歳 2.24歳 3.25歳 4.26歳

【顔造作】※各案は輪郭・目・眉・鼻・口・顎だけを指定
1. 柔らかな丸顔とふっくらした頬。狭い二重の大きな丸い目、緩いアーチ眉、低くまっすぐで先端の丸い鼻、小さく柔らかな厚みのある口、短く丸い顎
2. 均整の取れた卵型の輪郭。自然な二重のアーモンド形の目、まっすぐで中程度の太さの眉、細くまっすぐな鼻、上唇の山が明瞭な口、緩く先細りの顎
3. 額がやや広いハート形の輪郭。やや離れた少したれ目で浅い二重、柔らかな曲線眉、短く細い鼻、下唇に自然な厚みのある口、小さく尖った顎
4. 柔らかな四角形の輪郭。横長の一重の目、低くまっすぐな眉、低めの鼻筋と明瞭な鼻先、広めの口、柔らかく角の出た顎
5. 縦長で細い卵型の輪郭。奥行きがありまぶたのかぶさる目、少し弧を描く眉、長くまっすぐな鼻、薄く輪郭の明瞭な唇、細く丸い顎
6. 高く広い頬骨と短めの下顔面。細いアーモンド形で控えめな二重の目、水平な眉、先端の丸いコンパクトな鼻、広めの口、柔らかく先細りの顎
7. コンパクトなV字形の輪郭。自然な二重のつり目、緩く角度のついた眉、高く細い鼻筋、下唇に厚みのある輪郭の明瞭な口、小さく鋭い顎
8. 自然な左右差のある卵型の輪郭。片方だけわずかに重いまぶた、微妙に高さの違う眉、先端がごく軽く中心からずれたまっすぐな鼻、わずかに非対称な口元、自然に輪郭の出る顎

【顔のアクセント】
1.目の下の小さなほくろ
2.口元の小さなほくろ
3.鼻から上頬にかけてのごく薄いそばかす
4.選んだscene cardに自然な笑顔がある場合だけ見える片えくぼ。笑顔のないsceneでは表情を変えず、見えなくてよい
5.特になし
6.特になし
7.特になし
8.特になし

【体型】1.小柄 2.標準 3.高身長 4.小柄で自然な体つき 5.引き締まった体型 6.自然体 7.モデル体型 8.華奢な骨格

【髪色】1.黒 2.ダークブラウン 3.ベージュブラウン 4.柔らかなアッシュブラウン

【髪型】1.ショートボブ 2.ミディアムレイヤー 3.ロングストレート 4.ゆるいウェーブ 5.ポニーテール 6.ルーズなお団子 7.ウルフカット 8.ロングのワンレン 9.ハーフアップ 10.ミディアムで片耳にかけた髪

【scene card】※場面・仕草・光・時刻・季節・天気・視点・カメラ・主な焦点を一括で1つ選ぶ
※基本トーン（上品/スタイリッシュ/だらしない/元気/気だるげ/レトロ）は第一弾(random/)にあるので、第二弾ではそれ以外のムードを中心に構成。
1. きっかけ。髪を耳にかけようとした指が途中で止まり、半分伏せた目だけがカメラへ。晩春の晴れた午後、扉口の暖かな横光。親しい距離の50mm・腰上構図で、顔と止まった手の両方に焦点
2. きっかけ。目薬をさすため顔を上げ、まつ毛がまばたきする直前。初夏の曇った静かな朝、窓辺の柔らかな中立光。85mmの顔寄りで目と小瓶に焦点
3. きっかけ。ネックレスの留め金に苦戦し、片手をうなじに置いたまま助けを求めて見る。秋の夕方、ひとり暮らしの室内と暖かな中立光。背後斜めからの中景で留め金と視線に焦点
4. きっかけ。眼鏡を外して半分畳んだ手と、ピントの合わない裸眼がこちらを探す。冬の曇った朝、窓辺の柔らかな光。85mm上半身寄りで目と眼鏡に焦点
5. 生活の手元。味噌汁を小皿で味見し、自然に目を閉じた横顔と鍋から立つ細い湯気。寒い冬の朝の台所、低い中立な朝日。50mmの横顔中景で顔と湯気に焦点
6. 生活の手元。結露した窓に指で書きかけ、外の景色が線の中にだけ見える。冬の曇った午後、冷たい自然光。窓と上半身が入る50mm横位置で指先と透明な線に焦点
7. 生活の手元。白シャツにアイロンをかけ、短いスチームが窓光を受ける。梅雨の朝の整った室内、曇天の中立光。50mmの中広角ドキュメンタリーで手・アイロン・湯気に焦点
8. 生活の手元。ハンドドリップの蒸らしで、湯をゆっくり円に注ぎ、膨らむ粉を見つめる。初秋の晴れた朝の台所、暖かな中立光。カウンター脇からの50mm中景で手と粉に焦点
9. 生活の手元。観葉植物の葉を一枚ずつ柔らかな布で拭く。穏やかな春の午後、窓越しの清潔な緑がかった光。部屋の向かいからの50mm中景で指先と葉の質感に焦点
10. 気配のツーショット。隣にいる人の視点。溶けかけのアイスをレンズへ差し出し、カメラを見ずに鞄を探す。真夏の明るい正午の木陰、35mmの近いドキュメンタリーで手と顔に焦点
11. 気配のツーショット。セルフタイマーへ数歩手前から走り込み、髪がぶれ始めて自然に笑う。晴れた夏の夕方の公園、腰高に固定した35mm全身環境構図で動きに焦点
12. 気配のツーショット。隣にいる人へイヤホンを片方だけ差し出し、コードの長さが距離を決める。初秋の午後遅い列車内、柔らかな中立の窓光。親しい二人称視点の50mmでイヤホンと顔に焦点
13. 気配のツーショット。カフェのテーブル越しにスプーンを差し出し、「あーん」と言う前に笑って続かない。晴れた春の午後、柔らかな窓光。向かい側からの50mm着席中景でスプーンと自然な笑顔に焦点
14. 気配のツーショット。信号待ちの助手席で眠る横顔。赤信号は車外の小さな局所反射に留め、車内と肌は中立色。夏の夜、85mm横顔寄りで休んだ顔に焦点。画面全体を赤くしない
15. 天気の変わり目。乾いたアスファルトの最初の雨粒から空を見上げ、髪はまだ乾いている。晩夏の夕立直前の曇った午後。通りの向かいからの35mm全身ドキュメンタリーで動きと最初の濃い点に焦点
16. 天気の変わり目。陽炎で線路の先が揺れる無人踏切、下りた遮断機の前で待つ。真夏の快晴の正午、高く白い日光。35mm全身環境構図で人物・線路・熱の揺らぎに焦点
17. 天気の変わり目。濃霧の並木道、淡い球にほどけた街灯の間から数メートル先の姿が現れる。晩秋の明け方。望遠の全身環境構図で、顔寄りではなく人物の輪郭と霧の層に焦点
18. 天気の変わり目。雹を避けて軒下へ入り、驚きが笑いへ変わる途中。早春の荒れた曇り空、地面で跳ねる白い粒。35mmの中広角ドキュメンタリーで反応と雹に焦点
19. マジックリアリズム。普通の朝食卓で、カップの湯気だけが小さな積雲になって浮かぶ。秋の晴れた朝、中立の窓光。向かい側からの50mm食卓中景で顔・カップ・雲に焦点
20. マジックリアリズム。快晴の歩道を手ぶらで歩くが、足元の影だけが傘を差している。春の正午。完全な影まで入る少し高い35mm全身構図で、本人と影の関係に焦点
21. マジックリアリズム。昼の明るい部屋、金魚鉢の水の中にだけ星空が入っている。静かな夏の午後、中立の窓光。人物と鉢全体が入る50mm中景で、反応と水面の両方に焦点
22. マジックリアリズム。古いエレベーターの階数盤に一つだけ知らないボタンがあり、指がその上で止まる。秋の夕方、清潔な中立の室内光。肩越しの50mm寄りで指先・ボタン・横顔の一部に焦点
23. 大人っぽい。白いブラウスとロングプリーツスカートで高いスタジオ窓辺に立ち、逆光が布の縁で光る。春の晴れた朝、清潔な白い影。85mmの膝上構図で顔と服の輪郭に焦点
24. 大人っぽい。マットなシルク混のハイネックドレスでホテルの窓辺の椅子に座り、布が静かに垂れる。秋の穏やかな曇り朝、明るい部屋。85mmの着席膝上構図で顔と服の端正な線に焦点

【共通】服装指定のないscene cardでは、場面・季節・天気に合う無地の普段着にする。実写のRAW写真調、自然なカラー写真、中立で現実的な色バランス、毛穴が見える自然な肌、作り込みすぎないスナップの空気感、清潔な画面端、3:4縦位置。白黒・モノクロ・グレースケール・単色セピアにはしない。赤・橙・マゼンタの光漏れ、画面端の色モヤ、色付きの霞を入れない。アニメ調・イラスト・3DCG・プラスチックのような肌・人形顔・強いフラッシュ・透かし・文字・破綻した手指は避ける。
```

> ⚠️ 冒頭に「成人女性」「全身着衣」「非性化されたシーン」と**肯定文で**書くこと。
> 「未成年を出すな」「裸体を出すな」と書くと逆に弾かれる。詳細は [safe.md](../random/safe.md)。

**連投したいとき**は末尾に `これを4枚。1枚ごとに【顔造作】と【scene card】のshuffle bagを1つずつ消費し、選択済み要素だけで別々に生成。` を足す。

### 注意

LLM系の選択は、実装された乱数器の一様性を保証するものではない。上のshuffle bagは、
会話内で顔造作とscene cardの使用回数を揃え、リスト先頭への収束を減らすための運用。

- `scene cardは7番固定、他はサイレント抽選` のように軸を1つ固定してもよい
- 23・24（大人っぽい）を多く出したい → `scene cardは23・24を2倍の重みでbagへ入れる`
- 特定の顔造作だけで回したい → `【顔造作】は2番固定、他はサイレント抽選`
- 統計的な均等性を測る場合は、生成結果ではなく実際に選ばれた番号を別の検証用チャットで記録する。本番の「画像だけ返す」運用とは分ける

### Geminiで弾かれるときの注意（実測）

Geminiは文脈を見ず、プロンプト内の語彙を合算スコアで判定する。以下の現象を実測:

1. **同じプロンプトでも、チャット（セッション）が違うと結果が変わる** — 累積スコア判定の揺れ。同じ内容でも通ったり弾かれたりする。
2. **長いプロンプトほど弾かれやすい** — 内容語が多いほど合算スコアが上がる。コードブロックだけを貼ること（説明文は貼らない）。
3. **Geminiが検出する語** — `透け` `色気` `薄暗い` `ベッド` `ドキッ` `振り返る` `脱げかけ` 等を、文脈不問で弾く。本ファイルではこれらをすべて除去済み。

**Geminiで弾かれたら:**
1. 新しいチャットで試す（セッションの累積をリセット）
2. それでも弾かれるなら、scene cardを1-22だけに減らす（L2.5の23・24を外す）
3. さらに減らすなら、scene cardを3-4個だけ残す

---

## L2.5（大人っぽい）の使い方

scene cardの23・24が「大人っぽい」のカード。色気は服の仕立てと光だけで出す。

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

| card | 弾かれた語 | 通った言い換え |
|---|---|---|
| 23（白いブラウス） | 透け感のある / 形体をほのかに暗示 / 織りが入射光を散乱 | 白いブラウス / 逆光が布の縁で光る のみ |
| 24（ハイネックドレス） | ラグジュアリーブライダル / シャゼロング / ドレープ | ハイネックドレス / 椅子に座り / 布は静かに垂れ のみ |

### 弾かれたら

1. まず scene card 23・24 を外して残りの22枚で回す
2. ChatGPTなら光学言い回し版（expression/01準拠）に戻せるが、Geminiでは上記の安全語彙版を使う
3. それでも弾かれるなら、そのサービスは人物写真に厳しい。`safe.md` の「それでも弾かれたときの切り分け」参照

---

## どれを使うべきか

- **手元にSD/ComfyUI環境がある** → ①。候補抽選をチャットAIへ任せず、バッチで回したい場合に最も扱いやすい
- **Midjourney** → ②。ただし「抽選」ではなく「全部生成」なのでジョブ数に注意。人物のブレだけなら同じプロンプトを再送するだけでもいい
- **ChatGPT / Gemini しかない** → ③。shuffle bagで会話内の使用回数は揃えられるが、選択や画像の均等分散はサービス側から保証されない
