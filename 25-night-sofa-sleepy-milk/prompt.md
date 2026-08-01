# 25. 夜のソファ、大きなシャツ1枚で眠いミルク（参照画像ベース・部屋参照併用）

`ideas/README.md` の人物参照方針に準拠し、人物の顔、髪、肌、体型、身長感、プロポーションなどの身体的特徴は**1枚目の添付画像**から忠実に保持する（髪を含む身体特徴は本文にハードコードしない）。部屋は**2枚目の添付画像**（`22-morning-sofa-reading` の生成画像）から取得し、夜へ転換する2画像運用。22 の朝版と対になる夜版: 同じソファの同じコーナーで、大きなシャツ1枚のままホットミルクを持ち、眠気に負けかける一瞬。シャツは完全不透明で透けは一切使わない。ポーズは22の体育座りと重ならない「開放もたれ」（背もたれに深くもたれ、片膝をゆるく立て、片足は床）に固定し、2枚目の人物のポーズはコピーしないことを明文化してある。

- **アスペクト比:** 4:3 横（22と同じ生活シーン向き）
- **見せ場:** シャツ裾から下の脚だけ。開放もたれのシルエットと半開きのまぶた。シャツは緩い服で意図的に覆う例外案（バストは布の落ち方でのみ暗示）。
- **構図:** 22同型。ソファ手前コーナーからクッション高さで斜めに、人物は右三分の二、ソファアームとブランケットの畳みを手前下のぼけた前景に。髪から素足まで入る。
- **服装:** 大きなメンズ風コットンボタンアップシャツ1枚（洗いざらし白、完全不透明）。立ち膝でも裾が腿を覆うカバー指定入り。
- **背景:** 2枚目画像の部屋をそのまま取得（グレージュの織り生地ソファ、無地の壁と額縁、右側面の窓、端のブランケット、右端の本棚、コーヒーテーブルの水グラス）。夜転換はテキストで指示（カーテン閉、ランプ1灯、奥は深い影）。
- **照明:** 左後ろのサイドテーブルの琥珀ランプが唯一の主光。湯気は照らされて見えるだけで発光体にしない（22のページ発光対策と同型）。
- **文脈:** すっぴん × 半開きのまぶた × 大きなシャツ1枚の安心感 × プロの一瞬

---

## プロンプト

```text
A highly detailed photorealistic portrait of the person from the first reference image, set in the room from the second reference image. 4:3 horizontal aspect ratio, the sofa filling most of the frame with the subject to one side. Infer apparent age from the first reference image and preserve it. Match the first reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the first reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode features that are not present in the first reference image — no invented hair colors, accessories, uniforms, or props. Use this scene only if the reference is unambiguously adult; otherwise switch to the same oversized shirt worn over fully opaque lounge shorts. Avoid: no extra limbs, extra fingers, or malformed hands.

Room: Take the room entirely from the second reference image — the same low, deep, soft woven-fabric sofa in warm greige with its plump rounded cushions and rolled arm, the same plain bare wall behind the sofa with its single framed picture, the same window with curtains off to the right side of the room and never behind the sofa, the folded throw blanket pushed to one end of the sofa, the dark bookshelf at the right edge, the coffee table with the water glass. Keep the furniture layout, the camera-facing angle of the sofa and the room's uncluttered feeling exactly as they appear there. Take only the room and its objects from the second image — ignore the person in it completely: do not copy her pose, her seated position, or the way her body is arranged; the person comes only from the first reference image and is posed exactly as written below. Then re-light this room for late at night: the curtains drawn, the daylight gone, a single warm amber table lamp now glowing on a wooden side table behind her to the left, its light lying across one end of the sofa, the far side of the room falling into deep, true shadow. One palette of greige, washed white and a single pool of lamplight amber.

Makeup: She is one step from bed, so the face is essentially bare — fresh, natural end-of-day skin with its real texture, at most the faintest trace of lip balm. No eyeliner, no drawn brows, no mascara, no foundation finish, no polished full makeup. Natural lip and cheek color only, soft and sleepy.

Pose: Late at night on the sofa, in the middle of losing a fight with sleep — an open, reclined sprawl, not a compact huddle. She sits deep in the sofa's corner with her back leaned into the cushions and her head tipped back against the backrest, face tilted a little toward the camera, throat relaxed. One leg is folded up loosely on the cushion, knee bent outward, her arm draped over that knee with the hand hanging slack; the other leg stretches down, bare foot resting on the floor. In her other hand a warm ceramic mug of hot milk sits lowered and forgotten against her lap, the sip she meant to take never happening — steam still curling up from it, a pale ribbon lit by the lamp, not a light source itself. Her eyelids sit at half-mast, lashes nearly touching, gaze gone soft and unfocused on the ceiling — the exact moment of losing the fight, not asleep yet. She meant to finish the cup and then get up for bed; the sofa has already half claimed her. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A single oversized men's-style cotton button-up shirt in soft washed white, worn as sleepwear — nothing but the one shirt. It is genuinely big on her: the shoulder seams drop well past her own shoulders, the long sleeves are pushed up in loose folds to her forearms, and the shirttail hem reaches mid-thigh when standing. Even with one knee folded up, the hem falls over her lap and thigh and keeps her fully covered — nothing rides up, nothing underneath is visible. The cotton is soft from many washes but fully opaque: nothing reads through the cloth anywhere — no skin tone, no line of the body beneath — only its sleep-rumpled wrinkles and the play of warm lamplight on the weave, the volume beneath suggested solely by the natural fall and drape of the fabric. Buttons done up to a modest point at the collarbone, the collar relaxed and a little rumpled. Bare legs, one bare foot on the floor. Sleep-rumpled, unstyled, no logos.

Camera: 35mm lens at f/2.0 set at cushion height across from the sofa's near corner, angled diagonally so her reclined figure reads in three-quarter view from hair to bare feet, with the sofa arm and a fold of the throw blanket running through the lower foreground out of focus — matching the viewpoint of the room in the second image. She occupies the right two-thirds, her body leaning back along the sofa's corner in a long open line, the lowered mug and its lamplight steam near the centre reading as the brightest element in the frame — steam in the lamp light, not a light source. Her face is modeled gently by the lamplight — no harsh hotspot, no bright band on the cheek or forehead. Real skin — pores and fine peach-fuzz, the natural heaviness and slight asymmetry of half-fallen lids, a faint warmth-flush on the cheekbone. Natural sensor grain, no HDR glow, no beauty filter, no smoothing, no elongated body.

Format: 4:3 horizontal orientation, intimate domestic composition.
```

---

## 設計メモ

### 既存案との差
- `22`（朝・キャミソール+ニットショーツ・読書・体育座り・朝日）の対になる夜版。同じ部屋・同じカメラで、夜・シャツ1枚・ホットミルク・開放もたれへ転換。
- もとは夜の眠気案 `382`（ローテーブルで頬杖）だったが、部屋参照の運用決定を受けてソファへ移動し、ポーズも22と重ならない開いたシルエットへ組み替えた派生版。

### 2画像運用の設計
- 添付順は **1枚目=人物、2枚目=部屋**。プロンプト冒頭の `first` / `second` はこの順序に依存する。ツール側で並びが変わる場合は入れ替える。
- 2枚目は部屋の取得専用。「2枚目の人物は無視、ポーズ・座り位置・体の配置はコピーしない」を Room ブロックに明文化（下記の観察記録参照）。
- 部屋の静的なレイアウトは画像に委ね、夜への転換（カーテン閉・ランプ点灯・深い影）だけをテキストで指示する分担。

### 観察記録（生成テストの失敗と対策）
- **カーテンがソファ背後に出る失敗:** 初版は部屋の位置指定がなく、生成側が定型レイアウトでカーテンをソファ背後に配置した。対策は壁を肯定形で固定（`a plain, bare wall ... its only decoration a single framed picture`）し、観測された失敗として `no window and no curtains on the wall behind the sofa` / `never behind the sofa` を具体的に残す。窓は部屋の右側面へ明示移動。
- **2枚目の人物ポーズへの引きずられ:** 部屋参照として22の画像を添付すると、体育座りのポーズまでコピーされた。対策は2点: ①Room ブロックに `do not copy her pose, her seated position, or the way her body is arranged` を明記 ②ポーズ自体を正反対のシルエット（丸まった前かがみ → 背もたれにもたれる開いた長い線）に組み替え、参照しても重ならない構造にする。
- **フレーミングが寄り気味になる傾向:** 初回生成はバストアップ寄りにクロップされた。`from hair to bare feet` をカメラブロックに保持しつつ、冒頭の Format 指定（`the sofa filling most of the frame with the subject to one side`）でも全体感を先に宣言する二重指定で対処。

### シャツ1枚のカバー設計
- 大きなシャツ1枚は「緩い服で意図的に覆う案」（`ideas/README.md` の例外条項）。完全不透明＋裾のカバー範囲（立位で腿半ば、立ち膝でも腿を覆う・まくれ上がらない・下に何も見えない）を明文化し、見せ場は裾から下の脚だけに絞る。
- バストのボリュームは布の落ち方（`the natural fall and drape of the fabric`）でのみ暗示し、強調しない。

### 眠さの演技指定
- 目は閉じきらない「半開きの敗北寸前」で固定（`eyelids at half-mast, the exact moment of losing the fight`）。全閉じだとただの寝顔になる。
- 「飲むつもりだった一口が来ない」内心ベースの指定で、マグを持ち下げたまま忘れる動作に接続（形容詞の羅列にしない）。

### 湯気とランプの発光対策
- 22のページ発光の知見を転用: 湯気は `a pale ribbon lit by the lamp, not a light source itself`、カメラブロックにも `steam in the lamp light, not a light source` と二重に明記。ランプは「光を浴びた湯気」の光源としてだけ機能させる。

### 手の解剖学ネガ
- 膝に掛けた手とマグを持つ手が主役級のため、`no extra limbs, extra fingers, or malformed hands` を Avoid 行に配置。
