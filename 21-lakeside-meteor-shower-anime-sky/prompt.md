# 21. 流星群の湖・実写の彼女とアニメの夜空（参照画像ベース）

`ideas/README.md` の人物参照方針に準拠し、人物の顔、髪、肌、体型、身長感、プロポーションなどの身体的特徴は添付画像から忠実に保持する（髪を含む身体特徴は本文にハードコードしない）。`13` の媒質混交方式（実写の彼女とアニメの世界を一枚に同居させる）を転用し、倒影ではなく**空そのものがアニメ**の世界に実写の人物を置く。水平線を一本のシャープな境界として、上＝劇場アニメ背景、下＝完全な実写写真。人物は巨大な空の下に小さく佇み、環境が主役のシネマ構図。

- **アスペクト比:** 16:9 横（シネマ。環境が主役、人物は風景に溶け込む）
- **見せ場:** 細いストラップが框架する肩とデコルテのライン（引きの全身なので強度は抑えめ、世界観が主役）
- **服装:** 白い綿のマキシサンドレス（細いストラップ、完全不透明ボディス、層の長いスカート）、素足
- **背景:** 流星群の夜の山湖。水平線を境界に上＝アニメ・下＝実写。アニメの空にはクレーターまで描き込まれた銀白色の大きな月（満月から一二日過ぎ、片縁に薄影）と、水面へ細く揺れる銀の光柱。桟橋の手前に小さな暖色ランタン
- **文脈:** 静かなマジックリアリズム × 13 の媒質混交方式の転用 × 非日常の中に佇む人物

---

## プロンプト

```text
A highly detailed photorealistic environmental portrait of the person from the reference image, small within a vast mixed-media night landscape where only the sky is hand-drawn anime. 16:9 horizontal aspect ratio, her full figure on the end of a wooden pier beneath an immense sky. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode features that are not present in the reference image — no invented hair colors, accessories, uniforms, or props. Use this scene only if the reference is unambiguously adult; otherwise switch to the same dress with a higher opaque neckline.

Pose: Standing barefoot at the far end of a small weathered wooden pier on a still mountain lake at night, seen from behind at a three-quarter angle, a few steps into the walk toward the pier's end. Her head is tipped back to watch the sky, arms relaxed at her sides, one hand loosely gathering a fistful of skirt that the lakeside breeze presses against her legs. Her hair lifts softly off her shoulders in the same breeze. She is a small, quiet figure beneath the enormous sky — a person pausing inside a miracle. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A white cotton maxi sundress with thin straps and a fitted, fully opaque bodice that follows the body's line, opening from the waist into a long layered skirt that the wind draws against her legs and streams sideways. The thin straps frame the shoulders and décolleté line — the single accent of the outfit; everything else is long, white and simple. Barefoot on the old boards. No accessories beyond what appears in the reference, no logos.

Background: A mirror-calm mountain lake at the peak of a summer meteor shower. The dark horizon line where the far shore meets the sky runs low across the frame as one sharp, clean boundary. EVERYTHING AT AND BELOW the horizon — the woman, the pier's weathered planks, the black glass water, faint shoreline reeds, the dark conifer ridge — is a completely photorealistic photograph. EVERYTHING ABOVE the horizon — the whole sky filling the upper two-thirds of the frame — is a lavish theatrical anime-film background, modern anime key-visual quality painted art: a dramatic gradient of deep cobalt, vivid cyan, turquoise, lavender and pale rose; a brilliant Milky Way band of stardust; dozens of shooting stars streaking from a single radiant point, each meteor a white-gold core with a long cyan-violet glowing trail shedding tiny sparkle particles; immense soft-brushwork clouds with silver-lit edges; fine bokeh-like light particles drifting low over the horizon. A large, luminous moon a day or two past full — one edge just touched by shadow, its craters rendered in crisp, loving detail — hangs near one edge of the sky away from the meteor radiant, glowing cool silver-white rather than golden, wrapped in a soft halo that silver-lines the nearby clouds. Luminous, translucent, richly coloured — never a dark monochrome night. The two styles never blend: the photographic woman stays fully photographic under the anime sky, her silhouette cut clean against it. The anime sky touches the photorealistic world only as light and colour: a cool silver-white moonlight and starlight rim along her hair, arms and the white dress, the meteor glow shimmering faintly on the wet planks and on the dark water, which catches the sky's colours as soft natural reflections without becoming a painted surface itself, the moon laying one narrow, trembling column of silver light across the water toward the pier. A single small warm lantern sits at the pier's near end, barely enough to read her figure by. Natural sensor grain, no HDR glow, no beauty filter.

Camera: 28mm wide lens at f/4, positioned on the shore behind and beside the pier at water level, so the pier runs diagonally into the frame and leads to her small figure on the right third, with the vast anime sky dominating the composition. Deep focus from the planks to the horizon; her figure stays sharp despite her small size. Deliberate, controlled composition as by a professional photographer. No text, no logo, no watermark.

Format: 16:9 horizontal cinematic orientation, environment as the main subject.
```

---

## 日本語訳

参照画像の人物の高精細なフォトリアリスティックな環境ポートレート。空だけが手描きアニメの、広大な混合メディアの夜景の中に小さく佇む姿。アスペクト比16:9横、巨大な空の下、木の桟橋の端に立つ全身像。見た目の年齢は参照画像から推定して保持。性別表現、民族的特徴、体型とライン、身長感、比率、全体的な体つき、肌の色と質感、顔立ち、髪、胸とお尻の形とボリュームを含むすべての身体的特徴を参照画像に忠実に一致させ、服のフィットとドレープを通してバストとヒップの自然なボリュームとシルエットを正確に再現し、若返り・美化・誇張・体型改変は一切行わない。参照にない特徴（髪色・アクセサリー・制服・小物）は勝手に足さない。参照人物が明確に成人と判断できる場合のみこのシーンを使用し、判断できない場合は同じドレスをより高い不透明なネックラインに切り替える。

**ポーズ:** 夜の静かな山湖の、小さな風化した木の桟橋の先端に素足で立つ。後ろ斜め四分の三のアングルから、桟橋の端へ向かう歩行の数歩目の途中。頭を後ろに倒して空を見上げ、腕は体の横に自然に下ろし、片方の手は湖畔の風で脚に押し付けられるスカートの布を軽く掴んでいる。髪は同じ風に肩から柔らかく浮く。巨大な空の下の小さく静かな人影 — 奇跡の中で足を止めた人。作られていない、偶然捉えられた瞬間、カメラを知らない。

**服装:** 白い綿のマキシサンドレス。細いストラップと、体のラインに沿うフィットした完全不透明のボディス。ウエストから長い層のスカートが開き、風が脚に布を引き寄せ横へ流す。細いストラップが肩とデコルテのラインを框架する — 衣装の唯一のアクセントで、他はすべて長く白くシンプル。古い板の上に素足。参照に現れるもの以外のアクセサリーなし、ロゴなし。

**背景:** 夏の流星群のピークの、鏡のように穏やかな山湖。対岸と空が接する暗い水平線がフレームの低い位置を、一本のシャープでクリーンな境界として横切る。水平線以下のすべて — 女性、桟橋の風化した板、黒いガラスの水、岸のかすかな葦、暗い針葉樹の稜線 — は完全にフォトリアリスティックな写真。水平線より上のすべて — フレームの上三分の二を埋める空全体 — は華麗な劇場アニメ映画の背景、モダンアニメのキービジュアル品質の描画: 深いコバルト、鮮やかなシアン、ターコイズ、ラベンダー、淡いローズの劇的なグラデーション、星屑の輝く天の川の帯、単一の放射点から走る数十の流星（各流星は白金色の核にシアン〜紫の長い発光する尾を引き、小さな光の粒子を散らす）、銀色に縁取られた巨大な柔らかな筆致の雲、水平線の低く漂う細かな玉ボケ状の光粒子。流星の放射点から離れた空の片縁には、満月から一二日過ぎの大きく輝く月がかかる — 片側の縁だけかすかに影を帯び、クレーターまで精緻に描き込まれ、金色ではなく冷たい銀白色に発光し、柔らかなハローが周りの雲を銀色に縁取る。発光するようで透明感があり、豊かな発色 — 暗い単色の夜にしない。二つのスタイルは決して混ざらない: 写真の女性はアニメの空の下でも完全に写真のまま、シルエットは空に対してクリーンに切り抜かれる。アニメの空は光と色としてだけ実写の世界に触れる: 髪・腕・白いドレスに沿った冷たい銀白の月光と星のリムライト、濡れた板と暗い水の上でかすかに揺れる流星の輝き。水面は空の色を柔らかな自然な反射として受け止めるが、水面そのものが描かれた絵にはならず、月は桟橋へ向かう細く揺れる銀の光の柱を一本、水の上に横たえる。桟橋の手前の端に小さな暖色のランタンが一つ、彼女の姿を読める程度のわずかな灯り。自然なセンサーノイズ、HDRグローなし、美肌フィルターなし。

**カメラ:** 28mm広角レンズ f/4、岸の水面の高さから桟橋の後ろ斜めに位置し、桟橋がフレームへ斜めに走って右3分の1の小さな人影へ視線を導き、広大なアニメの空が構図を支配する。板から水平線まで深いフォーカス、人影は小さくてもシャープに。プロのカメラマンによる意図的で制御された構図。テキスト・ロゴ・透かしなし。

**フォーマット:** 16:9横向きシネマ構図、環境が主役。

---

## 設計メモ

### 既存案との差

- `13`（満月の湖・倒影だけがアニメ・ボールガウン・9:16）に対し、本案は**空そのものがアニメ**。衣装はカジュアルな白ワンピ、16:9横で環境主役。
- `ideas` 105（流星群を待つ毛布・浜辺・完全実写・4:3）とは媒質とトーンで差別化。

### 採用経緯（改訂の末、初稿 v1 を採用）

- チャットで9回の改訂を重ねた（天文精度の反映 → 人物の接地 → 視線を放射点へ → 流星の運動方向 → 月の色と大きさ → 引き具合 → ポーズ → 比率）。
- 最終的に**初稿を採用**。決め手は湖面の反射表現（「空の色を柔らかな自然な反射として受け止めるが、水面そのものは絵にならない」）が最も綺麗に出たこと、人物は小さいがシルエットが読める距離感であること。
- 改訂で得た知見（月は金色を避け銀白に／流星は中心へ収束させず外へ爆ぜる／ワープ感の否定／映り込みはアニメ調も許容／体は斜めこちら向きで顔は星へ）は、将来の派生用に `ideas/359-361-meteor-shower-anime-sky.md` へ記録してある。
- 初稿の `her silhouette cut clean against it` は引きの距離では貼り付き感が出にくいため、そのまま維持。

### 月の追加（添付画像の反映）

- 採用後の依頼で、アニメの空に添付画像の月（大きくクレーターまで描き込まれた銀白色の月、片縁に薄影）を追加。
- 配置は流星の放射点と離れた空の片縁。色は金色ではなく銀白（以前の生成で満月の金色が強すぎた反省）。
- 月光は人物の銀白リムライトと、水面へ細く揺れる銀の光柱として実写側に届く（「光としてだけ境界を越える」ルールに準拠）。

### 媒質混交ルール

- 水平線がシャープな一本の境界。上＝100%アニメ背景、下＝100%実写写真。混交ゼロ。
- アニメの空は**光と色としてだけ**実写側に触れる（銀白のリムライト、濡れた板と水への揺らぎ、月の光柱）。

### 参照

- `ideas/359-361-meteor-shower-anime-sky.md` — 本案を含む3案のアイデアストック（改訂履歴と知見）
- `ideas/README.md` — 共通テンプレート・身体特徴保持・ハードコード禁止規約
- `13-fullmoon-lake-anime-reflection/prompt.md` — 媒質混交方式の原案
