# 182〜196 — オフィスカジュアル / かっこいい系 15案

端正な仕事着を「働いている場面」ではなく、**移動・待機・退勤・切り替えの瞬間**に置いて、シルエットと光でかっこよさを立てる設計。露出ではなく、仕立て・素材・姿勢・視線・間の取り方で強さを作る。

## 共通方針

- 人物の見かけの年齢、性別表現、民族的特徴、顔、髪、肌、体型、身体のライン、身長感、比率は**参照画像だけ**から推定して保持する。参照にない髪色・身体特徴・キャラ設定をハードコードしない。
- 胸・腰まわりの形とボリュームも参照画像どおりに再現し、服のフィット感とドレープを通してシルエットが正確に伝わるように指定する（`including chest and hip shape and fullness` を全案の英文に含める）。誇張はしない。
- **胸が小さく出るときの原因は大抵ポーズと生地。** 腕・鞄・フォルダ・組んだ手が胸の前を横切ると潰れて見え、箱型で張りのある生地（crisp / boxy / oversized）は布が体から浮いてボリュームを消す。胸のシルエットを見せたい案では、①胸の前を空ける（nothing held in front of the chest）、②体に沿う生地（soft, fluid weave that follows the body）、③布の挙動を明示（curves over the bust, drapes from its outermost point, gentle tension lines）の3点を指定する。
- **胸の位置は高く指定する。** 生成では実際より下に描かれやすいため、`the bust sits high and supported on the ribcage, as if wearing a well-fitted bra: its fullest point is level with the mid-upper arm, roughly at armpit height — never sagging low toward the waist` のように、脇の高さ・二の腕の中ほどといった体の相対位置を基準に入れる。
- 若返り、加齢、美化、体型変更、比率誇張、別人化を行わない。
- 一着につき見せ場は一箇所（肩線、袖、ウエスト、脚の縦線、襟元のいずれか）。残りは長い丈と端正な仕立てで引き算する。
- かっこよさは「重心」で作る。片足荷重、下がった肩、力の抜けた手元。媚びない表情を基本にするが、無表情の彫像にはしない。
- **ポーズは常に「動作の途中」を切り取る。** 完了した静止ポーズ（直立、正対、カメラ目線、左右対称）を書かない。歩きかけ、振り向きかけ、髪が風で動く、笑いかけの口元、ずれた荷物を直す途中など、次の瞬間には消える状態を指定し、`candid, unposed, caught mid-moment, unaware of the camera` を英文に含める。
- 色は各案で一系統に絞る（チャコール、グレージュ、ネイビー、オフホワイト、ブラウン、ブラック）。差し色は一点まで。
- 文字、ロゴ、ウォーターマーク、余分な指や手足、不自然な関節、重複人物、参照外のアクセサリーを避ける。
- **画角はプロの撮影を思わせる作り込みを必ず入れる。** 各案に `Camera:` ブロックを置き、焦点距離、カメラ高さ（目線 / 腰 / 膝下 / 頭上）、水平からの振り、被写体の置き位置（三分割・片寄せ・余白の方向）、前景に噛ませる要素、被写界深度を明示する。真正面・目線高さ・中央配置の「証明写真的な既定値」は使わない。

## 各案の読み方

- **比率 / 見せ場 / 差し替え変数** を先に読み、英語プロンプトはそれ単体でコピーして使える。
- 骨格は `README.md` の共通テンプレート（Pose / Outfit / Background / Format）に準拠。

---

## A. 移動と通過（182〜186）

### 182. 朝の並木道
- **比率:** 3:4
- **見せ場:** 日差しを片手で遮る仕草と、腕が顔にかける影の境界。
- **差し替え変数:** 街路樹の種類、時間帯、手荷物、トップスの色。

```text
A highly detailed photorealistic portrait of the person from the reference image. 3:4 vertical aspect ratio, waist-up framing — do not show the full body. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Caught mid-step on a tree-lined pavement, just raising one hand to shade her eyes from the sudden glare — the hand not yet settled above the brow, hair lifting slightly with the movement and the breeze. The other hand loosely holds a slim document folder swinging at her side. She squints toward the light with the faint beginning of a smile at the surprise of the brightness. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: No jacket — it is too hot for one. A plain off-white short-sleeve crew-neck knit, lightly tucked at the front into high-waisted charcoal wide-leg trousers with a sharp center crease. No visible logos, minimal jewellery only if present in the reference.

Background: A wide open avenue lined with street trees on a clear summer morning. Hard direct sunlight comes from ahead and slightly to one side, rimming the shoulder line and casting a crisp shadow of her raised hand and forearm across her face and neck; dappled leaf shadow scatters over the pavement and the wall behind. Bright, high-key daylight with real contrast, no lens flare gimmicks.

Camera: 85mm lens at f/2.0, waist-up. Camera set slightly below her eye line and offset about 30 degrees to her right, so the raised arm cuts diagonally across the top third of the frame. She sits on the left third with the sunlit avenue opening into the empty right side. An out-of-focus tree trunk grazes the near edge of the frame as a soft foreground mask. Background compressed and softly out of focus.

Format: 3:4 portrait orientation, vertical composition.
```

### 183. エレベーターホールの待ち
- **比率:** 4:5
- **見せ場:** 金属面に映る静かな反射と、袖をまくった前腕。
- **差し替え変数:** 扉の材質、手に持つもの、シャツの色。

```text
A highly detailed photorealistic portrait of the person from the reference image. 4:5 vertical aspect ratio. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Waiting for the elevator, one shoulder slouched against the wall, torso open to the camera with nothing held in front of the chest, in the middle of glancing up at the floor indicator — head just turning, a strand of hair swinging across the cheek. One arm hangs at her side with a soft taupe jacket hooked from that hand, low against the thigh; the other hand absent-mindedly tucks hair behind an ear. Mouth soft, mind elsewhere. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A pale grey cotton shirt in a smooth weave slightly too fitted through the chest, only the top button left undone so the collar opens in a small, shallow notch at the base of the throat — the opening ends just below the collarbones, where only the very beginning of the cleavage line is faintly suggested, barely visible, nothing more. The second button and everything below it stay fastened. Cuffs rolled twice to just below the elbow, tucked into straight-cut black tailored trousers with a thin leather belt. The top curve of the bust begins immediately below that small opening, so the volume clearly starts high on the chest: the bust sits high and supported, as if in a well-fitted push-up bra, its fullest point level with the armpit line, round and lifted, never sagging or sitting low toward the waist. Below the notch the closed shirt strains gently across the chest with tension pulls at the buttons, matching the reference volume exactly, not minimized and not exaggerated. Elegant, office-appropriate, no exposure beyond the small opening at the throat.

Background: A quiet corporate elevator hall in polished stainless steel and warm grey stone. She stands directly beside the closed elevator doors, angled so the large polished-steel door panel fills the left half of the frame — and that panel carries her reflection the way real brushed elevator steel does: recognizably her — the profile, the grey shirt, the fall of her hair — but softly blurred and diffused, edges bleeding into the metal, details lost, colours slightly desaturated and darkened, with the faint vertical streaking of the brushed grain smearing the image. Not a sharp mirror image; a hazy, dreamlike echo of her in the metal. Overhead lighting is diffused and slightly warm.

Camera: 50mm lens at f/2.8, chest height, positioned so both appear together: the real woman on the right third of the frame, her mirrored reflection in the steel door panel on the left third, the two silhouettes facing each other across the door seam. The reflection is prominent in size — roughly the same scale as the real figure — but soft in rendering: blurred, low-contrast, absorbed into the steel, clearly a reflection and never mistakable for a second person or a true mirror.

Format: 4:5 portrait orientation, vertical composition.
```

### 184. 地下駐車場の出口
- **比率:** 16:9
- **見せ場:** コンクリートの暗さの中で、コートの縦一本が抜ける対比。
- **差し替え変数:** 車、コートの丈、時間帯。

```text
A highly detailed photorealistic portrait of the person from the reference image. 16:9 cinematic horizontal aspect ratio, wide framing with the subject small in the frame. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Mid-stride toward the ramp exit of an underground car park, coat hem caught swinging open around the legs, one heel just lifting off the ground. One hand in a coat pocket, the other coming up to push hair back from her face as the daylight hits. Head tilted a touch, eyes forward on the bright exit, mouth relaxed. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: An ankle-length stone-beige trench coat left unbelted and open, over a black fine-gauge turtleneck and straight black trousers. Flat black ankle boots. The coat's vertical line is the only strong shape in the frame.

Background: A raw concrete car park with low ceilings and cool strip lighting, opening onto a bright daylight ramp ahead. The ambient interior is dim and desaturated while the exit blows out to soft white, so the figure reads as a dark vertical against light.

Camera: 35mm lens at f/4, placed low — roughly knee height — and pushed to one side of the ramp, so the concrete ceiling presses down across the top of the frame and the floor runs out toward the viewer. She is deliberately small and set off-centre on the left third, walking into the open right two-thirds. A structural pillar sits half in frame at the near edge. Wide, largely deep focus with only the far ramp blowing out.

Format: 16:9 landscape orientation, cinematic horizontal composition.
```

### 185. 雨のオフィス入口
- **比率:** 3:4
- **見せ場:** 濡れた石畳の反射と、傘を畳む一連の手つき。
- **差し替え変数:** 傘の色、雨足、玄関の様式。

```text
A highly detailed photorealistic portrait of the person from the reference image. 3:4 vertical aspect ratio. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Just ducked under the entrance canopy, caught in the middle of shaking rain off a half-folded umbrella — droplets still flying off it, blurred with motion. Shoulders hunched a little from the cold, hair damp at the edges and falling forward past the jaw, a small exhaled laugh at how hard it's raining. Weight dropping onto one hip as she settles out of the hurry. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A navy double-breasted wool coat worn buttoned, collar turned up at the back of the neck, over a white shirt with the collar sitting outside the coat. Dark slim trousers cropped at the ankle, polished black derby shoes with rain speckle.

Background: The stone entrance of an office building on a heavy rain evening. Wet paving returns broken reflections of warm lobby light; the street behind is a dark blur of headlights. Cool blue exterior against warm interior spill.

Camera: 35mm lens at f/1.8, held low and close, tilted slightly up so the canopy edge and falling rain cross the top of the frame. Shot from outside in the rain looking back toward the entrance, with out-of-focus raindrops and a smear of umbrella fabric breaking the near edge. She sits low and to the right; the wet paving and its reflected light fill the lower left. Very shallow focus held on the face and the folding hands.

Format: 3:4 portrait orientation, vertical composition.
```

### 186. 出張前のプラットフォーム
- **比率:** 9:16
- **見せ場:** 電車を待つ何気ない立ち姿と、あくび混じりの気の緩み。
- **差し替え変数:** 駅、荷物、ニットの色。

```text
A highly detailed photorealistic portrait of the person from the reference image. 9:16 vertical aspect ratio, full-length vertical framing. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Waiting on the platform with her weight sunk onto one leg, leaning lightly on the raised handle of a small cabin suitcase, mid-glance down the track to see if the train is coming. The other hand covers a small early-morning yawn, eyes half-closing with it. Hair moves faintly in the platform draught. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A boxy grey-brown wool blazer over a ribbed dark brown knit top tucked into wide dark brown trousers, one tonal family head to toe. A slim leather tote hangs from the shoulder. Flat black loafers.

Background: An early-morning intercity platform, long and empty, with a train stationary behind her slightly out of focus. Overhead lights and pale dawn light mix into an even, cool illumination; strong horizontal lines of the platform edge run behind her.

Camera: 135mm telephoto at f/2.5 from far down the platform, heavily compressing the depth so the train, the pillars and the far end stack flat behind her. Camera at hip height, dead level with no tilt, subject placed centrally but pushed low in the tall frame so the station roof carries the upper half as negative space. The nearest pillar clips the frame edge. Focus tight on her, everything past two metres soft.

Format: 9:16 portrait orientation, vertical composition.
```

---

## B. 執務空間の余白（187〜191）

### 187. 会議室、全員が出た後
- **比率:** 4:3
- **見せ場:** 長机の直線と、腰掛けた片脚の角度。
- **差し替え変数:** 部屋の広さ、机上の残り物、上着の色。

```text
A highly detailed photorealistic portrait of the person from the reference image. 4:3 horizontal aspect ratio. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Perched loosely on the edge of the emptied meeting table, one foot swinging free of the floor, caught mid-stretch — arms reaching up and back, spine arching, face tipped toward the ceiling with eyes shut and the unguarded grimace-smile of a long meeting finally over. Papers still under one palm on the table. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A stone-grey wool waistcoat worn over a white shirt with the sleeves pushed up, tucked into pleated grey trousers. No jacket. A thin dark leather belt marks the waist; the waistcoat is the only structured layer.

Background: A long meeting room after the meeting: empty chairs pushed out of line, a few paper cups and a closed laptop left on the table. Late afternoon sun cuts through half-open blinds in broad stripes across the table and the far wall. Warm dust in the light, quiet and still.

Camera: 40mm lens at f/2.8, camera at seated eye level and set at the far corner of the table so the tabletop leads diagonally through the frame toward her. She sits on the right third; empty pushed-out chairs blur through the left foreground. The stripes of blind-light rake across the table surface toward the lens. Focus on her, the table edge softening as it nears the camera.

Format: 4:3 landscape orientation, horizontal composition.
```

### 188. 給湯室の一分
- **比率:** 4:5
- **見せ場:** カップを持つ手元と、ゆるめたシャツの襟。
- **差し替え変数:** カップ、時刻、シャツの生地。

```text
A highly detailed photorealistic portrait of the person from the reference image. 4:5 vertical aspect ratio. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Slouched back against the kitchenette counter mid-sip, mug just leaving her lips, steam drifting across her face. Ankles loosely crossed, one shoulder higher than the other, gaze drifting out of focus toward the window — somewhere else entirely. A little slack in the whole body, the first true pause of the day. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A pale sand oversized shirt with the top two buttons open and the collar slightly askew, half-tucked into dark olive straight trousers. Sleeves rolled unevenly. The looseness is the point: everything is well cut but worn in.

Background: A small office kitchenette in the mid-morning, pale tiles, a kettle steaming, cupboard doors closed. One window on the left throws soft directional daylight across the counter, leaving the right side of the room in gentle shadow.

Camera: 56mm lens at f/2.0, shot through the kitchenette doorway so the door frame edges both sides of the image and darkens the borders — a frame within the frame. Camera at chest height, square to her, she leans just left of centre with the steaming kettle blurred on the counter behind. Shallow focus on the mug and collar.

Format: 4:5 portrait orientation, vertical composition.
```

### 189. 窓際のスタンディングデスク
- **比率:** 3:4
- **見せ場:** 窓光に対する背筋と、開いた袖口。
- **差し替え変数:** 街の景色、天候、トップスの色。

```text
A highly detailed photorealistic portrait of the person from the reference image. 3:4 vertical aspect ratio. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: At a raised desk by the window, caught the second her attention slips from the screen to the city — head just turning toward the glass, pen still hovering over a notepad mid-word. One hip leans into the desk edge, the other foot has come up onto its toe. The distracted stillness of a thought arriving. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A fine black merino long-sleeve top with the cuffs pushed back over the wrists, tucked into high-waisted grey pinstripe trousers with a clean drape. A slim silver watch if the reference already shows a wrist accessory; otherwise nothing.

Background: A quiet corner of an open-plan office at midday, one wall entirely glass, city towers softly out of focus beyond. Flat, generous daylight from the side; the interior behind her falls a stop darker so her silhouette separates cleanly.

Camera: 75mm lens at f/2.8 in strict profile, camera at her shoulder height and far enough back that she occupies the left half while the window and city fill the right — a clean two-part composition split by the window mullion. A blurred monitor edge crosses the near lower-left corner. Slight negative space above the head; horizon of the city kept level.

Format: 3:4 portrait orientation, vertical composition.
```

### 190. 資料棚の前
- **比率:** 4:5
- **見せ場:** 伸ばした腕がつくる長い斜線。
- **差し替え変数:** 棚の内容、ジャケットの丈、照明の色温度。

```text
A highly detailed photorealistic portrait of the person from the reference image. 4:5 vertical aspect ratio. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Up on tiptoe reaching for a high shelf, fingertips just short of the box she wants, jacket hem swinging with the stretch and a folder clamped awkwardly under the other arm. Face lifted, lips slightly parted with the effort, a wisp of hair fallen loose across the forehead. The honest imbalance of almost-reaching. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A long unstructured black linen-blend jacket that falls to mid-thigh, worn open over a plain white tee and straight ecru trousers. The jacket's hem swings with the reach, exaggerating the diagonal. Flat black shoes.

Background: A wall of archive shelving in a well-kept office library, boxes and binders in muted neutral colours. Cool overhead lighting with one warmer lamp further along the aisle, giving depth down the corridor of shelves.

Camera: 35mm lens at f/2.8, shot from low — waist height, tilted up along the reach — so the extended arm and the shelving verticals converge toward the top of the frame. Camera positioned inside the aisle at an angle, with the near shelf running out of focus down the right edge as a leading line. She stands on the left third; the aisle recedes behind her. Focus on the face and reaching hand.

Format: 4:5 portrait orientation, vertical composition.
```

### 191. 打ち合わせ前のロビーソファ
- **比率:** 4:3
- **見せ場:** 深く沈んだ座り姿勢と、組んだ脚の直線。
- **差し替え変数:** ロビーの様式、鞄、スーツの色。

```text
A highly detailed photorealistic portrait of the person from the reference image. 4:3 horizontal aspect ratio. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Sunk deep into the lobby sofa, one leg crossed, caught in the middle of checking the time — wrist just turning, sleeve pulled back with the other hand, eyes down on the watch. A phone balances on the sofa arm. The crossed foot bounces faintly with waiting. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A relaxed navy two-piece: a soft-shouldered jacket left open and matching wide trousers, worn over a plain white ribbed tank. Dark leather loafers, no socks visible. A structured leather bag sits on the floor beside her feet.

Background: A hotel-like corporate lobby in warm stone and dark wood, a reception desk far behind and out of focus. Large windows to one side give soft daylight; a low lamp adds a warm accent near the sofa.

Camera: 50mm lens at f/2.0, camera dropped to her seated eye level — low, almost coffee-table height — so the sofa reads monumental and the crossed leg's line runs toward the lens. Shot from about 20 degrees off her front, she sits on the right third with the lobby depth opening left. The blurred corner of a marble coffee table cuts the near lower edge. Focus on her face, lobby melting into soft warm bokeh.

Format: 4:3 landscape orientation, horizontal composition.
```

---

## C. 退勤と切り替え（192〜196）

### 192. 退勤、消灯直前のフロア
- **比率:** 16:9
- **見せ場:** 消えかけた蛍光灯の下、一人だけ立つ縦の存在。
- **差し替え変数:** フロアの規模、明かりの残り方、コートの色。

```text
A highly detailed photorealistic portrait of the person from the reference image. 16:9 cinematic horizontal aspect ratio, wide framing. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Alone on the emptied floor, caught mid-shrug into her coat — one arm in, the other sleeve swinging loose behind her, scarf half-slipping off one shoulder. Head turned back over the shoulder toward the last lit desk as if remembering something, then deciding it can wait. Body still in the twist of the movement. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A long charcoal wool coat being put on over a slate grey knit and dark tailored trousers. A soft scarf hangs unlooped around the neck. Everything is in one cool tonal family so the shape reads as a single vertical.

Background: An open-plan office at night with most lights already off, only one bank of ceiling panels and a single desk lamp still burning. Deep shadow in the foreground, cool overhead pools of light behind. City windows dark blue beyond.

Camera: 35mm lens at f/2.8, shot over the tops of the darkened desks from the unlit side of the floor, camera at desk height so out-of-focus monitors and partitions layer the whole foreground in silhouette. She stands small, on the right third, inside the one remaining pool of light. Ceiling lights recede in perspective toward her. Focus on her through the gap between two dark desks.

Format: 16:9 landscape orientation, cinematic horizontal composition.
```

### 193. 非常階段の踊り場
- **比率:** 9:16
- **見せ場:** 階段の斜線と、手すりに掛けた手。
- **差し替え変数:** 階段の材質、光源の位置、ニットの色。

```text
A highly detailed photorealistic portrait of the person from the reference image. 9:16 vertical aspect ratio, full-length vertical framing. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Caught mid-climb between landing and stairs, one foot already on the next tread, hand sliding along the rail. She's glancing down at the phone in her other hand — mid-scroll, thumb moving — a small involuntary smile at whatever just arrived on the screen. Hair swings forward with the downward glance. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A dark green fine-knit polo tucked into black straight trousers with a sharp crease, a thin black belt. A grey jacket hooked over the handrail beside her rather than worn. Simple black leather shoes.

Background: A bare concrete fire stairwell, painted steel rail, one caged wall light on the landing. The light falls hard from above, cutting the steps into strong diagonals and leaving the lower flight in shadow.

Camera: 28mm lens at f/2.8, shot from half a flight below looking up through the stair rail, so out-of-focus rail bars cross the lower foreground and the ceiling light burns at the top of the frame. Strong upward perspective; the staircase diagonal runs corner to corner. She stands in the upper right third, lit from above, the shadowed lower steps filling the bottom of the tall frame.

Format: 9:16 portrait orientation, vertical composition.
```

### 194. 帰り道の立ち食いそば前
- **比率:** 3:4
- **見せ場:** きちんとした服装と、雑然とした夜の街の対比。
- **差し替え変数:** 店、看板の色、上着。

```text
A highly detailed photorealistic portrait of the person from the reference image. 3:4 vertical aspect ratio. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Slowing to a stop outside a small late-night noodle counter, mid-turn toward the doorway, drawn by the smell — body still angled down the street, head already inside. One hand hitches the slipping strap of a shoulder bag back up without looking. A tired, tempted half-smile. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A camel-brown single-breasted coat worn open over a black shirt buttoned to the collar and dark straight trousers. Sleeves fall to the wrist bone. The tailoring stays sharp against the casual surroundings.

Background: A narrow city side street at night, the noodle shop's warm yellow interior spilling onto wet asphalt, signage out of focus behind her. Mixed colour temperature — warm shop light against cold street light — with natural bokeh and no readable text.

Camera: 50mm lens at f/1.8, shot from across the narrow street at a candid angle, camera at chest height and tilted a few degrees off level for a documentary feel. A passer-by's out-of-focus shoulder clips the near left edge, half-veiling the frame. She stands on the right third against the warm shop glow; cold street light fills the left. Focus locked on her, foreground and signage dissolved into bokeh.

Format: 3:4 portrait orientation, vertical composition.
```

### 195. タクシー後部座席
- **比率:** 4:5
- **見せ場:** 窓を流れる光が顔と肩に落ちる速度。
- **差し替え変数:** 街の色、時刻、上着の素材。

```text
A highly detailed photorealistic portrait of the person from the reference image. 4:5 vertical aspect ratio. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Sagged into the back seat of a moving taxi, head lolling toward the window, temple resting on the glass, eyes heavy-lidded and about to close. One hand lies open in her lap, the phone in it long forgotten. Coat collar pushed up crooked by the seat; her body sways slightly with a turn the car is taking. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A black wool coat worn over a pale grey shirt, the coat's collar standing at the neck. Dark trousers. A thin chain or watch only if already visible in the reference image.

Background: Night city passing outside the taxi window, streetlights and signage smeared into soft streaks by the car's motion. Interior almost dark; her face and shoulder are lit only by the moving exterior light, so the illumination shifts across the frame.

Camera: 35mm lens at f/1.4 from the front passenger seat, shooting back between the headrests so a dark out-of-focus headrest edge frames the left side. Camera slightly below her eye level; she sits on the right third against the streaked window, which fills the rest of the frame with moving light. Razor-thin focus on the eye nearest the glass; interior falls to near-black.

Format: 4:5 portrait orientation, vertical composition.
```

### 196. 帰宅直後の玄関
- **比率:** 4:5
- **見せ場:** 崩れ始めた仕事着（外れたボタン、脱いだ片方の靴）。
- **差し替え変数:** 玄関の様式、荷物、シャツの色。

```text
A highly detailed photorealistic portrait of the person from the reference image. 4:5 vertical aspect ratio. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping.

Pose: Just through the front door, caught wobbling slightly on one leg as she pries a heel off with the toe of the other foot, one hand slapped against the wall for balance. Bag sliding off her shoulder toward the floor, hair coming loose. Head dropping back against the wall mid-exhale, eyes closing, the day finally ending in her face. Candid, unposed, caught mid-moment, unaware of the camera.

Outfit: A white shirt worn all day: collar open two buttons, hem pulled loose on one side, sleeves shoved to the elbows. Charcoal trousers still creased and correct. The blazer is over her forearm, not on. Nothing removed beyond shoes and jacket.

Background: A small entrance hall lit only by one lamp further inside the apartment, so most of the frame is soft shadow with a warm pool of light at her back. Keys and bag on the floor, coat hooks on the wall. Quiet, domestic, end of day.

Camera: 40mm lens at f/1.8, shot from inside the apartment looking back toward the door, from slightly below standing height, so she is backlit by the entrance and the warm lamp pool catches her from the side. The dropped bag and keys sit large and out of focus in the near foreground at the bottom edge. She leans on the left third; the dark doorway fills the right. Shallow focus on the tipped-back face.

Format: 4:5 portrait orientation, vertical composition.
```
