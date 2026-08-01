# 22. ソファの上の朝読書、同じ行を二度読む（参照画像ベース）

`ideas/README.md` の人物参照方針に準拠し、人物の顔、髪、肌、体型、身長感、プロポーションなどの身体的特徴は添付画像から忠実に保持する（髪を含む身体特徴は本文にハードコードしない）。朝7時のリビング、予定になかった読書の時間。ソファの上で体育座りになり、膝に乗せた読み古した小説をぼんやり読む寝起きの一瞬を切り取る。顔はすっぴん（メイクなし）、目はまだ焦点の合わない寝ぼけ眼。キャミソールは完全不透明で透けは一切使わない。本は膝の上（鎖骨より下）に固定して胸の前を空け、膝は斜めに倒して胴をカメラ側に開く。一筋の朝日が開いたページに落ち、紙がマットに明るいのが画面のハイライト。ページもスマホ同様「発光体」としては描かせない設計。本の背表紙はカメラ側に向けて「読み古した小説」と読めるが、文字は一切読めない処理とする。

- **アスペクト比:** 4:3 横（生活シーン）
- **見せ場:** 体育座りの丸まった姿勢の幾何学と、キャミソールの細いストラップが框架する肩〜鎖骨のライン。朝日を受けてマットに明るい開いたページが画面のハイライト。
- **構図:** ソファの手前コーナーからクッション高さで斜めに。人物は右三分の二、ソファアームとブランケットの畳みを手前下のぼけた前景に。髪から素足まで入る。
- **服装:** 薄手リブコットンのキャミソール（オフホワイト、完全不透明、細いストラップとスクープネック）＋ヘザーグレーのニットショーツ。寝巻き、素足。寝じわはそのまま。
- **背景:** 朝7時の小さなリビング、静かで物が少ない。カーテンの隙間から一筋の低い朝日がソファに落ちる。コーヒーテーブルの水グラス。
- **照明:** 一筋の朝日が主光（ページ・ソファ・脚）。部屋の残りは青みがかった薄い陰。ページは「紙が光を受ける」表現に留め、発光させない。
- **文脈:** 寝起きのすっぴん × 寝ぼけ眼の読書 × 完全不透明キャミの質感 × プロの一瞬

---

## プロンプト

```text
A highly detailed photorealistic portrait of the person from the reference image. 4:3 horizontal aspect ratio, a small sofa filling most of the frame with the subject to one side. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode features that are not present in the reference image — no invented hair colors, accessories, uniforms, or props. Use this scene only if the reference is unambiguously adult; otherwise switch to a plain crew-neck tee over the same shorts.

Makeup: She has just woken up, so the face is essentially bare — fresh, natural just-out-of-bed skin with its real texture, pillow crease still fading on one cheek, at most the faintest trace of tinted lip balm. No eyeliner, no drawn brows, no mascara, no foundation finish, no polished full makeup. Natural lip and cheek color only, soft and sleepy.

Pose: An unplanned morning reading hour on the sofa. She sits in a loose gym-sit on the cushions: knees drawn up and tilted slightly to one side, bare feet tucked close with the soles just touching the cushion, an open paperback novel resting on top of her knees, both hands holding its edges with the softened, creased spine turned a little toward the camera — a much-reread novel, plain as day from its worn back. Her spine curls into a soft reader's hunch, chin dipped toward the page, and the tilt of her knees keeps her torso open to the camera side — the book stays on her knees, below the collarbone line, with nothing held in front of the chest. Her eyes are still heavy-lidded from sleep, blinking slowly at the page: she has read the same paragraph twice and doesn't mind. The corner of her mouth softens at something the story just did. Inside she is only half in the book; the other half is still asleep. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A thin-strap ribbed cotton camisole in soft off-white, worn as sleepwear — fully opaque, but a soft, fluid knit that follows the body: the fabric curves over the bust and drapes from its outermost point with gentle tension lines, so the silhouette reads exactly as in the reference. The bust sits high and supported on the ribcage, as if wearing a well-fitted bra: its fullest point is level with the mid-upper arm, roughly at armpit height, with only a short distance between the collarbones and the top of the curve — never sagging low toward the waist. The thin straps and the scoop neckline frame the shoulders and the collarbone line, and the reader's hunch draws the fabric smooth across the upper back — the single accent of the outfit. Plain heather-grey knit shorts, bare legs folded up in front of her. Sleep-wrinkled, unstyled, no logos.

Background: A small living room at seven in the morning, quiet and uncluttered. A single bright blade of low sun slips through the gap in the curtains and lies across the sofa, falling on the open pages of her book so the paper holds the light the way paper does — bright but matte, no glow. The paperback's cover is a quiet muted tone with no legible lettering on cover or spine, just the creased, rounded back of a novel that has been read many times. A folded throw blanket pushed to one end of the sofa, a water glass on the coffee table, the morning otherwise holding its breath. One palette of off-white, heather grey and a thin line of sunrise gold.

Camera: 35mm lens at f/2.0 set at cushion height across from the sofa's near corner, angled diagonally so her seated figure reads in three-quarter view from hair to bare feet, with the sofa arm and a fold of the throw blanket running through the lower foreground out of focus. She occupies the right two-thirds, the sunlit open book on her knees reading as the brightest matte surface in the frame — paper in the sun, not a light source. Natural sensor grain, no HDR glow, no beauty filter. Avoid: no extra limbs, extra fingers, or malformed hands.

Format: 4:3 horizontal orientation, intimate domestic composition.
```

---

## 設計メモ

### 既存案との差
- `09`（夜のベッド・シアー背向け）や bedroom アーカイブ（夜）とは時間帯と主題が別。`197` のキッチン朝案（起きて動く朝）に対し、本案は「動かない朝」。体育座りの読書は既存案にない構図。
- ideas/362 として設計した朝10案の一つ（当初タイトル「二度寝の攻防、スヌーズを止める手」）を、生成テストのフィードバックで数回改訂し、最終的に「ソファの上の朝読書」へピボットしたもの。

### スマホ発光の破綻と対策（観察記録）
- 初版（スヌーズを止める構図、ベッド）で画面の見えづらさを `screen washed out / glare` と書いたところ、スマホ自体が強く発光する物体として描かれる破綻が出た。
- 対策はネガの追加ではなく肯定形の書き直し。「光を浴びているだけの普通の黒い板（an ordinary dark slab of glass and plastic）」「画面は直射日光に負けた通常輝度の表示（dull grey panel）」「自身は発光しない（gives off no glow of its own）」を文に織り込むと落ち着く。`washed out` `glare` の語は発光の誘因になるので使わない。
- 本に置き換わった現在も同型の予防線を残す: ページは `bright but matte, no glow`、カメラブロックに `paper in the sun, not a light source`。光る小物全般に使える書き方。

### 胸の前を空ける体育座り
- 体育座りは膝が胸の前を塞ぎやすい。膝を斜めに倒して胴をカメラ側に開き、本は膝の上＝鎖骨より下に固定する（`the book stays on her knees, below the collarbone line, with nothing held in front of the chest`）。3点セット（体に沿う生地・布の挙動の明示・胸の前を空ける）と胸の高い位置指定は維持。

### 本の文字の処理
- 背表紙をカメラ側に少し向け「読み古した小説」と特定するが、表紙・背表紙の文字は読めないものと明記（`no legible lettering on cover or spine`）。AIの造語文字の生成を防ぐ。装丁は mute な一色。

### すっぴんと寝ぼけ眼
- Makeup ブロックは独立欄（`199` の書式）。枕の跡が残る頬・素肌の質感・リップバームまでとし、アイライン・眉描き・マスカラ・ファンデはなし。
- 寝ぼけ眼は「まぶたが重い・焦点が泳ぐ・ゆっくり瞬き」の身体描写に、「同じ段落を二度読んでいる」内心を接続して演技化（形容詞の羅列にしない）。

### 透けを使わない設計
- キャミソールは寝巻きとして完全不透明（fully opaque）。見せ場は透けではなく、ストラップとスクープネックが框架する肩〜鎖骨のライン、読書の前かがみで上背部に張る布、体育座りの幾何学に絞る。

### 手の解剖学ネガ
- 本を持つ両手が画の主役級になる構図のため、`no extra limbs, extra fingers, or malformed hands` を Avoid 行に配置。
