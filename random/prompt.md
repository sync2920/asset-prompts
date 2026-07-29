# ランダム生成メタプロンプト（20代前半・日本人女性）

顔・体型・髪・服装・シチュエーション・トーンをスロット（変数）化し、
1回の指示で毎回ちがう組み合わせの画像プロンプトを吐かせるための元プロンプト。

- 使い方: 下の「A. メタプロンプト」を ChatGPT / Claude / Gemini にそのまま貼る → 出てきた英語プロンプトを画像生成AIへ。
- 直接ガチャを回したいだけなら「D. 単体テンプレート」に自分で値を埋めてもいい。
- 表現レベルは L1〜L3（後述）で管理。上限は「示唆的な色っぽさ」まで。露骨な描写は出さない設計。

---

## A. メタプロンプト（これをコピーして貼る）

```
あなたは画像生成AI用のプロンプト作成アシスタントです。
以下のスロット表からランダムに1つずつ選び、組み合わせて英語の画像生成プロンプトを作ってください。

# 出力ルール
- 出力数: 3案（指定があればその数）
- 各案について「選ばれたスロット一覧」→「英語プロンプト」→「日本語訳（要約でよい）」の順で出す
- 被写体は必ず a Japanese woman in her early 20s（成人）と明記する
- 表現レベルは L2（指定があればそのレベル）に従う
- スロットDのトーンを軸にして、E/F/G/H が矛盾しない組み合わせだけを選ぶ（整合ルール参照）
- 案どうしでトーン(D)とシチュエーション(E)が重複しないようにする
- 末尾に共通の画質指定とネガティブプロンプトを付ける

# 乱数の決め方
シード指定がない場合は毎回ちがう組み合わせを自由に選ぶ。
シード指定（例: SEED=4821）がある場合は、スロット番号 n（A=1, B=2, C=3 …）に対して
  index = (SEED + n * 7) mod （そのスロットの項目数）
で決定し、同じシードなら同じ結果になるようにする。

────────────────────────
【A】顔の系統（10）
1. clean symmetrical idol-like features, large almond dark-brown eyes, small straight nose
2. cool mature features, sharp defined double eyelids, high nose bridge, calm gaze
3. round youthful baby face, soft downturned (tareme) eyes, gentle mouth
4. feline upturned eyes, small sharp chin, slightly mischievous look
5. understated quiet features, single-eyelid (hitoe) eyes, minimal makeup, refined stillness
6. polished K-beauty styling, glass skin, straight brows, gradient lips
7. light freckles across the nose, bare-faced natural look, honest expression
8. high cheekbones, wide-set eyes, long editorial face, strong bone structure
9. deep-set eyes and defined brow line, dark hair, mixed-looking but Japanese features
10. friendly open face with a small snaggletooth showing when she smiles

【B】体型（8）
1. slender petite build, narrow shoulders, delicate frame
2. healthy natural build, average proportions, relaxed posture
3. tall and long-limbed, around 168cm, elongated silhouette
4. petite with a softly curved figure, gentle hourglass line
5. athletic toned build, defined shoulders and calves, sporty frame
6. soft, gently rounded figure, natural body line, unstyled
7. lean editorial model build, flat lines, sharp collarbones
8. sloping shoulders, fine wrists and ankles, fragile-looking frame

【C】髪（10）
1. jet-black short bob with blunt bangs
2. medium layered brown hair, airy movement
3. long straight black hair, glossy, center-parted
4. loose wavy perm, soft volume around the cheeks
5. high ponytail with loose strands at the temples
6. messy top bun with stray hairs at the nape
7. dark hair with a hidden inner color peeking through
8. wet-look wolf cut, damp strands framing the face
9. high-tone beige hair, slightly grown-out roots
10. shoulder-length hair pulled behind one ear, no bangs

【D】トーン（7）★軸になるスロット
1. 上品・清楚 / elegant and composed, quiet refinement, understated
2. スタイリッシュ・モード / editorial and graphic, confident stylish attitude
3. 大人っぽい・落ち着いた色気 / calm and self-possessed, fully clothed, warm low-key lighting
4. だらしない・オフ / off-duty and unkempt in a charming way, unposed candid
5. 元気・カジュアル / bright energetic casual, natural laughter, movement
6. 気だるげ・アンニュイ / languid and detached, sleepy morning mood
7. レトロ・フィルム / nostalgic film-photo mood, 90s Japanese snapshot feel

【E】シチュエーション（14）
1. 早朝の自室、ベッドサイドで差し込む光の中
2. 夏の海辺、木製の桟橋の先
3. 都会のビル街、ガラス張りのエントランス前
4. 昭和レトロな喫茶店のボックス席
5. 雨上がりの路地、濡れたアスファルトの反射
6. 深夜のコンビニの明かりの外側
7. 冬の温泉旅館、外気浴の縁側
8. 春の河川敷、土手の斜面
9. 洗濯物を干すベランダ、午後の逆光
10. ホテルの窓辺、レースカーテン越しの光
11. 夜のバーカウンター、間接照明
12. 電車の窓際、夕方の車内
13. 古いアパートのキッチン、換気扇の下
14. 屋上、フェンス越しの街並みと夕焼け

【F】服装（14）※Dのトーンに合うものを選ぶ
1. crisp white linen shirt tucked into wide beige trousers
2. simple black knit dress with a thin gold necklace
3. oversized gray sweatshirt with relaxed track pants, thick socks slipping down
4. sheer-layered blouse over a camisole, long pleated skirt
5. faded blue denim overalls over a striped tee
6. oversized white dress shirt with sleeves rolled past the elbow
7. ribbed tank top and loose sweatpants, hair tie on the wrist
8. summer sundress with a delicate small pattern, thin straps
9. tailored black blazer over a plain white tee, structured
10. loose cotton yukata worn casually, sash slightly relaxed
11. cropped cardigan and high-waisted vintage denim
12. soft jersey loungewear set, slightly oversized
13. muted midi dress with a knit cardigan on top
14. long wool coat over a fine-gauge turtleneck and trousers

【G】ポーズ・仕草（10）
1. leaning against a wall, one knee bent, looking off-frame
2. mid-stride walking toward the camera, hair caught in motion
3. sitting on the floor hugging her knees, chin resting on them
4. stretching her arms overhead, torso lengthening, eyes closed
5. taking a quiet mirror selfie with a smartphone
6. glancing back over her shoulder at the camera
7. holding a mug with both hands close to her face
8. lying on her stomach on a bed, feet crossed in the air
9. tying her hair up, arms raised, looking down
10. crouching low, elbows on knees, relaxed and unposed

【H】光・時間帯（8）
1. soft golden-hour backlight with warm rim light on the hair
2. cool blue overcast daylight, flat and even
3. hard midday sun with crisp shadows
4. window light filtered through lace curtains, gentle falloff
5. warm tungsten interior light, deep shadows
6. neon signage reflecting on wet surfaces at night
7. cold fluorescent light with a slight green cast
8. dim candle-like low light, high contrast, mostly shadow

【I】カメラ・構図（8）
1. 85mm portrait lens, shallow depth of field, tight upper-body framing
2. 35mm documentary framing, full body with environment
3. low-angle wide shot emphasizing sky and perspective
4. slightly high angle looking down, intimate distance
5. side profile in sharp focus, background heavily blurred
6. full-length mirror reflection composition
7. 3:4 vertical portrait, subject off-center on the rule of thirds
8. film-grain snapshot look, slightly off-kilter framing

【J】表現レベル（指定がなければ L2）
- L1: 完全に健全。雰囲気は表情と光のみで表現
- L2: 大人っぽさ・落ち着いた色気。全身着衣のまま、
      身体ではなく「照明・陰影・レンズ」の語彙でムードを作る（逆光、低いタングステン光、深い影など）
※ 旧 L3 は削除。安全フィルタが弾く領域なので、言い換えでくぐらせず狙いを L2 に下げる。

────────────────────────
# 整合ルール（ランダムでも破綻させないため）
- D1 上品 → F 1/2/4/8/13、E 4/7/10/12、H 1/4、L1〜L2
- D2 スタイリッシュ → F 2/9/11/13、E 3/5/11/14、H 2/6、L1〜L2
- D3 大人っぽい → F 6/8/10/13、E 1/7/10/11、H 1/4/5/8、L2
- D4 だらしない → F 3/7/12、E 1/6/9/13、H 4/5/7、L1〜L2
- D5 元気 → F 5/6/11、E 2/8/14、H 1/3、L1
- D6 気だるげ → F 3/12/13、E 1/6/12/13、H 4/7/8、L2
- D7 レトロ → F 5/10/11/14、E 4/8/12/13、H 3/5、L1〜L2
- 上のリストに無い組み合わせでも、明らかに矛盾しなければ可（例: 温泉旅館にブレザーは不可）

# 共通の末尾（全案に付ける）
photorealistic raw photo, natural skin texture with visible pores, authentic candid feel,
cinematic color grading, sharp focus on the eyes, 8k resolution, highly detailed, 3:4 vertical

# 共通ネガティブプロンプト（全案に付ける）※内容語は入れない。安全側はポジティブ文で担保する
anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like face, mannequin,
distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs,
harsh flash, blown highlights, heavy makeup, watermark, text, logo, low resolution, blurry
```

> ⚠️ ネガティブに `minor` `nudity` 等を書くと、フィルタは否定を解釈せずその語自体を検出して弾く。
> 詳細と対策は [safe.md](safe.md)。

---

## B. 使い方の例

**そのまま回す**

> 上のメタプロンプトを貼って）→ `3案作って`

**軸を固定してガチャ**

> `トーンは D3 固定、シチュエーションだけランダムで5案。レベルは L2。`

**同じ子で服とシーンだけ変える（キャラ固定）**

> `A=2, B=3, C=4 は固定。E/F/G/H だけランダムで6案。`

**再現性が欲しい**

> `SEED=4821 で3案。` → 同じシードを渡せば同じ組み合わせが戻る

---

## C. 出力サンプル（D3 / L2 で1案回した例）

選択: A=5, B=4, C=8, D=3, E=10, F=6, G=6, H=4, I=1

**English**

```
Professional fashion editorial photograph. A 23-year-old adult Japanese woman, fully clothed in
modest everyday clothing, with understated quiet features, single-eyelid eyes and minimal makeup,
a petite frame with soft natural proportions, and a freshly washed wolf cut framing her face.
Calm and self-possessed. She wears an oversized white shirt with the sleeves rolled past the elbow
and tailored trousers, standing by a hotel window and glancing back over her shoulder at the camera.
Morning light filtered through lace curtains rakes across her jawline with a gentle falloff, the rest
of the room sinking into soft shadow. 85mm portrait lens, shallow depth of field, tight upper-body
framing. Photorealistic raw photo, natural skin texture with visible pores, candid documentary feel,
cinematic color grading, sharp focus on the eyes, 8k resolution, highly detailed, 3:4 vertical.

Negative prompt: anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like
face, mannequin, distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused
fingers, extra limbs, harsh flash, blown highlights, heavy makeup, watermark, text, logo, blurry.
```

**日本語訳**

プロのファッションエディトリアル写真。23歳の成人日本人女性、きちんと着衣。薄めの顔立ちに一重の目、メイクは最小限。小柄で自然なプロポーション、洗いたてのウルフカットが顔まわりに落ちている。落ち着いた佇まい。袖を肘までまくったオーバーサイズの白シャツにテーラードパンツ姿で、ホテルの窓辺に立ち、肩越しにカメラを振り返る。レースカーテン越しの朝の光が顎のラインを撫でるように差し、部屋の残りは柔らかい影に沈む。85mmポートレート、浅い被写界深度、上半身寄りの構図。

---

## D. 単体テンプレート（自分で埋める用）

```
Photorealistic raw photo of a Japanese woman in her early 20s, with [A:顔], [B:体型], and [C:髪].
[D:トーン]. She wears [F:服装], [G:ポーズ] at [E:シチュエーション].
[H:光]. [I:カメラ].
photorealistic raw photo, natural skin texture with visible pores, authentic candid feel,
cinematic color grading, sharp focus on the eyes, 8k resolution, highly detailed, 3:4 vertical.
```

---

## E. 各モデルでの注意

| モデル | 補足 |
|---|---|
| Midjourney | ネガティブは `--no` に分解。末尾に `--ar 3:4 --style raw`。`--seed` で固定できる |
| Stable Diffusion / Qwen | Negative prompt 欄にそのまま貼る。実写系チェックポイント推奨 |
| ChatGPT / Gemini | 長文をそのまま通せる。L3 は弾かれることがあるので L2 中心が安定 |
| nano-banana 系 | 「顔だけ固定」の指示は参照画像を併用したほうが安定する |

- 同じ顔を維持したいときは、A/B/C を固定 + 参照画像 + `same person, consistent face` を追加。
- 20代前半＝成人であることは毎回明記する（省略すると年齢が下振れしやすい）。
