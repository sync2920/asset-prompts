# ランダム生成メタプロンプト第2弾（23〜26歳・日本人女性・シーン束版）

`random/prompt.md` の派生版。人物参照を使わず、次の4点を広げる:

1. **シーン** — 第二弾固有の24場面を、動作・場所・視線を含む骨格として収録
2. **人物** — 年齢、顔の造作、顔のアクセント、体型、髪色、髪型を独立化
3. **環境** — 時間帯・季節・天気・光・カメラを、シーンと両立する候補から選択
4. **再現性** — 無効値を後補正せず、有効候補を絞ってから状態付き乱数で選択

- 使い方: 下の「A. メタプロンプト」を ChatGPT / Claude / Gemini にそのまま貼り、出てきた英語プロンプトを画像生成AIへ渡す。
- シーン番号は [inline-random.md](inline-random.md) の直接投げ版と共通。
- L2.5の運用メモとモデル差は `inline-random.md` を参照。貼り付け本文には、生成に不要な注意語の一覧を含めない。
- 出力は自然なカラー写真に固定し、白黒化と色付きの画面端モヤを使わない。

---

## A. メタプロンプト（これをコピーして貼る）

```
あなたは画像生成AI用のプロンプト作成アシスタントです。
以下から整合する値を選び、英語の画像生成プロンプトを作ってください。

# 出力ルール
- 出力数: 3案（指定があればその数）
- 各案を「選択一覧」→「英語プロンプト」→「日本語訳（要約）」の順で出す
- 年齢はQから選び、a 24-year-old adult Japanese woman のように数字と adult を書く
- 場面・服装・小物のいずれかに、仕事、ひとり暮らし、運転、休日の自宅など成人の生活文脈を1つ入れる
- 最初にEを1つ選ぶ。DはEの番号から導出し、独立抽選しない
- Eは場所・主動作・視線・視点の骨格である。Eに書かれた動作を別のポーズで上書きしない
- Gの独立スロットは使わない。I/NもEの許可集合から選び、Eに固定指定があれば追加変更しない
- 選択順は Eの群候補 → E → Q → A → A-2 → B → C-1 → C-2 → F → L → H → K → M → I → N
- F/L/H/K/M/I/Nは「E別の有効候補表」と「H×K×M整合表」の両方を満たす候補だけに絞る
- Hを選ぶ前に、そのHで有効なKとMが1件以上残ることを確認する
- 顔の表情はEの瞬間に合わせて自然に決める。Aへ性格、表情、メイク、髪、肌色、年齢を足さない
- 複数案では同じEを繰り返さず、Dの6群とAの8種をシャッフルバッグとして扱う
- 服・小物・背景は無地または架空の意匠とし、実在ブランドのロゴ、商品名、看板を入れない
- Jは指定がなければL2。E23・E24はL2.5固定
- 共通末尾と共通ネガティブプロンプトを全案に付ける

# 乱数の決め方
シード指定がない場合:
- 1案なら、有効候補から自由に1つ選ぶ
- 複数案なら、Dの6群とAの8種を別々のシャッフルバッグとして扱う
- Dの全群を使うまで同じ群を再利用せず、Aも8種を使うまで再利用しない
- 各群内でも未使用のEを優先する。袋を使い切ったときだけ全候補を戻す
- 厳密な再現性や分布監査が必要ならSEEDを指定する

シード指定（例: SEED=4821）がある場合:

  state = SEED mod 10007
  t = 1

候補から1件選ぶ直前に毎回:

  state = (11 * state + 17 + t) mod 10007
  position = (state mod 候補数) + 1
  t = t + 1

- 整合する候補だけを番号順に並べてからposition番目を選ぶ
- 固定指定や候補1件の場合もstateとtを1回進める
- 複数案でもstateとtを初期化せず、次案へ継続する
- 無効な生番号を出して後から別番号へ補正しない
- シャッフルバッグによる除外も、候補を並べる前に適用する
- 複数案では、Eを選ぶ前に未使用の6群を候補として同じ式で1群を選び、次にその群の未使用Eを選ぶ。
  群の選択でもstateとtを1回進める。Dは選ばれたEの群名であり、人物・場面とは別の内容スロットではない
- 選択一覧に、各選択直後のstateを併記する
- Jは指定値なのでstateを進めない

────────────────────────
【D】シーン群（Eから導出）
D1 きっかけ: E1-4
D2 生活の手元: E5-9
D3 気配のツーショット: E10-14
D4 天気の変わり目: E15-18
D5 静かなマジックリアリズム: E19-22
D6 大人っぽいエディトリアル: E23-24

【Q】年齢（4）
1. 23-year-old adult
2. 24-year-old adult
3. 25-year-old adult
4. 26-year-old adult

【A】顔の造作（8）
※輪郭・目・眉・鼻・口・顎だけを指定する。表情、メイク、髪、肌色、年齢はE/Q/C側で決める。
1. a soft round face with full cheeks, large round eyes with narrow double lids, gently arched brows, a low straight nose with a rounded tip, a small mouth with softly full lips, and a short rounded chin
2. a balanced oval face, almond-shaped eyes with natural creases, straight medium-thickness brows, a slim straight nose, a defined cupid's bow, and a gently tapered jaw
3. a heart-shaped face with a slightly broad forehead, wide-set downturned eyes with shallow creases, softly curved brows, a short narrow nose, a fuller lower lip, and a small pointed chin
4. a softly square face, long monolid eyes, straight low-set brows, a straight nose with a low bridge and defined tip, a wider mouth, and a softly defined square jaw
5. a long narrow oval face, deep-set hooded eyes, slightly arched brows, a longer straight nose, thin well-defined lips, and a narrow rounded chin
6. a face with broad high cheekbones and a shorter lower half, narrow almond-shaped eyes with subtle double lids, horizontal brows, a compact nose with a rounded tip, a wide mouth, and a softly tapered jaw
7. a compact V-shaped face, upturned eyes with clear creases, gently angled brows, a high narrow nose bridge, a defined upper lip with a fuller lower lip, and a sharp small chin
8. a naturally asymmetric oval face, one eyelid slightly heavier than the other, brows at subtly different heights, a straight nose with a soft off-center tip, a slightly uneven lip line, and a gently defined jaw

【A-2】顔のアクセント（8）
1. a small beauty mark under one eye
2. a small beauty mark near her mouth
3. faint natural freckles across the nose and upper cheeks
4. a single dimple visible only if E naturally includes a smile; do not add a smile only to show it
5. 特になし（本文に足さない）
6. 特になし（本文に足さない）
7. 特になし（本文に足さない）
8. 特になし（本文に足さない）

【B】体型（8）
1. slender petite build
2. healthy natural build with average proportions
3. tall and long-limbed, around 168 cm, with an elongated silhouette
4. compact petite build with natural proportions
5. athletic toned build with a sporty frame
6. soft natural build
7. lean editorial model build
8. fine-boned frame with narrow wrists and ankles

【C-1】髪色（4）※Aから完全に独立
1. jet-black
2. dark brown
3. natural beige brown
4. natural ash brown

【C-2】髪型（10）※Aから完全に独立
1. short bob with blunt bangs
2. medium layered hair with airy movement
3. long straight hair, glossy and center-parted
4. loose wavy hair with soft volume
5. high ponytail with loose strands at the temples
6. messy top bun with loose ends
7. wolf cut with choppy face-framing layers
8. long blunt one-length cut
9. half-up style
10. medium-length hair pulled behind one ear, with no bangs

【E】シーン骨格（24）
※主動作・視線・場所を一括で使う。別の汎用ポーズを追加しない。

── D1 きっかけ
1. 仕事の休憩中、髪を耳にかける指が途中で止まり、こちらの視線に気づく。午後の光が入る扉口
2. 休日の自宅の窓辺で目薬をさすため上を向き、まばたきする直前
3. 外出前の自室でネックレスの留め金に苦戦し、髪を持ち上げたまま助けを求める
4. 休日の部屋で眼鏡を外した直後、半分たたんだ眼鏡を持ち、裸眼でこちらを探す

── D2 生活の手元
5. ひとり暮らしの朝の台所で味噌汁を味見し、目を閉じて味を確かめる
6. 冬の自室で結露した窓に指で何かを書き、線の中にだけ外が見える
7. 休日の部屋で白いシャツにアイロンをかけ、スチームが窓の光に浮かぶ
8. 朝の台所でハンドドリップの蒸らしを見つめ、湯を小さな円に注ぐ
9. 自宅で観葉植物の葉を一枚ずつ布で拭き、指先と葉に集中する

── D3 気配のツーショット
10. 夏の木陰で溶けかけのアイスを「持っていて」とレンズへ差し出す。カメラは受け取る側
11. 夕方の公園でセルフタイマーへ走り込む数歩手前。固定カメラへ近づく
12. 隣り合って座り、イヤホンを片方だけレンズへ差し出す。カメラは隣の人
13. カフェで「あーん」とスプーンをレンズへ差し出す一歩手前に笑い、動きが止まる。カメラは向かいの人
14. 夜の信号待ちの助手席で眠る横顔。カメラは運転席側

── D4 天気の変わり目
15. 夏の仕事帰り、乾いたアスファルトへ落ちた夕立の一粒目を見てから空を見上げる
16. 真夏の無人踏切で、陽炎に溶ける線路の先を見ながら遮断機の前で待つ
17. 濃霧の並木道で、街灯が光の球に見える数メートル先から歩いて現れる
18. 雹を避けて軒下へ入り、地面で跳ねる白い粒への驚きが笑いに変わる途中

── D5 静かなマジックリアリズム
19. 休日の朝食卓で、紅茶の湯気だけが小さな積雲の形になって浮かぶ
20. 晴れた歩道を手ぶらで歩くが、足元の影だけが傘を差している
21. 昼の自室の窓辺で、金魚鉢の水の中だけに星空が見える
22. 仕事先の古いエレベーターで、階数盤に一つだけ知らないボタンを見つけ、指を直前で止める

── D6 大人っぽいエディトリアル（J=L2.5）
23. 白いブラウスとロングプリーツスカートで高いスタジオ窓辺に立つ。布の縁に逆光が入り、室内は明るい白い影
24. マットなシルク混のハイネックドレスでホテルの窓辺の椅子に座る。朝の光と静かな布の落ち方

【F】服装（15）
1. a crisp white linen shirt tucked into wide beige trousers
2. a simple black knit dress with a thin gold necklace
3. an oversized gray sweatshirt with relaxed track pants
4. a white blouse with a long pleated skirt
5. faded blue denim overalls over a striped tee
6. an oversized white dress shirt with straight-leg trousers
7. a ribbed sleeveless top with loose full-length trousers
8. a summer sundress with a delicate small pattern
9. a tailored black blazer over a plain white tee and trousers
10. a loose cotton yukata worn casually with a neatly secured sash
11. a cropped cardigan with high-waisted vintage denim
12. a soft jersey loungewear set
13. a muted midi dress with a knit cardigan
14. a long wool coat over a fine-gauge turtleneck and trousers
15. a matte silk-blend dress with a high neckline

【H】光の質（8）
1. warm low-angle backlight with a natural rim along the hair
2. flat even diffused daylight, cool and nearly shadowless
3. hard direct sunlight with crisp high-contrast shadows
4. daylight filtered through a white curtain with gentle falloff
5. warm tungsten interior light with deep natural shadows
6. restrained neutral artificial light diffused by fog or reflected on wet surfaces
7. cold fluorescent interior light with a slight green cast
8. a single dim warm interior source with most detail held in shadow

【I】カメラ・構図（8）
1. 85mm portrait lens, shallow depth of field, tight upper-body framing
2. 35mm documentary framing, full body with environment
3. low-angle wide shot emphasizing sky and perspective
4. slightly high angle at a natural conversational distance
5. side profile in sharp focus with a softly blurred background
6. full-length mirror reflection composition
7. 3:4 vertical portrait, subject off-center on the rule of thirds
8. film-grain snapshot framing, slightly off-kilter

【K】時間帯（8）
1. early dawn
2. morning
3. midday
4. early afternoon
5. late afternoon
6. evening blue hour
7. night
8. deep night

【L】季節（8）
1. early spring
2. spring
3. rainy season
4. summer
5. late summer
6. autumn
7. late autumn
8. winter

【M】天気（8）
1. clear sky
2. overcast
3. rain
4. just after rain with wet surfaces
5. snow
6. fog
7. strong wind
8. heat shimmer

【N】視点（6）
1. a third-person documentary observer
2. a passerby's fleeting glance
3. the camera is someone beside or opposite her
4. a high static observational camera
5. her own gaze in a mirror or held-at-arm's-length shot
6. a static self-timer camera waiting for her

【J】表現レベル
- L1: 清潔な日常写真。雰囲気は場面、表情、自然光で作る
- L2: 成人の落ち着いた映画的写真。全身着衣のまま照明、陰影、レンズで作る
- L2.5: 成人の上品なファッション写真。全身着衣のまま仕立て、布、明るい窓光で作る

────────────────────────
# E別の有効候補表
※「任意」はその列の全候補。固定値も1件の候補としてstateを進める。
※Eの文章に視点や構図が明記されている場合、その意味を変えない候補だけを使う。

| E | F | L | H | K | M | I | N |
|---|---|---|---|---|---|---|---|
| 1 | 1/2/4/8/9/11/13 | 2/4/5/6 | 1/4 | 4/5 | 1/2/4 | 1/4/5/7 | 3 |
| 2 | 1/3/4/6/12/13 | 任意 | 4 | 2/4 | 任意 | 1/4/5 | 3 |
| 3 | 2/4/8/13/15 | 任意 | 4/5 | 2/4/5/6 | 任意 | 1/4/5 | 3 |
| 4 | 1/3/4/6/9/12/13 | 任意 | 2/4/7 | 2-6 | 任意 | 1/4/5 | 3 |
| 5 | 1/3/6/7/12 | 任意 | 4/5/7 | 2 | 任意 | 1/4/5/7 | 1/3 |
| 6 | 3/6/12/13/14 | 1/7/8 | 2/4 | 2-5 | 2/3/5/6 | 1/4/5/7 | 1/3 |
| 7 | 3/7/12/13 | 任意 | 4/7 | 2-5 | 任意 | 1/4/7 | 1/3 |
| 8 | 1/3/6/7/12/13 | 任意 | 4/5 | 2 | 任意 | 1/4/5/7 | 1/3 |
| 9 | 1/3/6/7/12/13 | 1-6 | 2/4 | 2-5 | 任意 | 1/4/5/7 | 1/3 |
| 10 | 5/8/11 | 4/5 | 1/2/3 | 3-5 | 1/2 | 2/4/7 | 3 |
| 11 | 2/5/8/11/13 | 2/4/5/6 | 1/2 | 5/6 | 1/2/4 | 2/7/8 | 6 |
| 12 | 1/2/5/8/9/11/13 | 任意 | 1/2/4/5 | 2-7 | 1/2/4 | 1/4/7 | 3 |
| 13 | 1/2/4/8/11/13 | 任意 | 2/4/5/7 | 2-7 | 任意 | 1/4/7 | 3 |
| 14 | 1/2/9/11/13/14 | 任意 | 5/7/8 | 7 | 1-6 | 5 | 3 |
| 15 | 2/9/14 | 4/5 | 2 | 4/5 | 2 | 2/3/8 | 1/2 |
| 16 | 1/5/8/9/11 | 4/5 | 3 | 3/4 | 8 | 2/3/8 | 1/2 |
| 17 | 2/9/14 | 1/6/7/8 | 2/6 | 1/6/7 | 6 | 2/5/8 | 1/2 |
| 18 | 9/13/14 | 1/3/6 | 2/6 | 4/5/6 | E固定の雹 | 2/3/8 | 1/2 |
| 19 | 1/3/6/12/13 | 任意 | 4 | 2 | 任意 | 1/4/7 | 1/3 |
| 20 | 1/2/5/8/9/11/13 | 2/4/5/6 | 3 | 3/4 | 1 | 2/3/7 | 1/2 |
| 21 | 1/2/4/6/13/15 | 任意 | 4 | 3/4 | 任意 | 1/4/7 | 1/3 |
| 22 | 1/2/9/13/14/15 | 任意 | 7/8 | 6-8 | 任意 | 1/4/7 | 1/3 |
| 23 | 4固定 | 2/4/5/6 | 4 | 2-5 | 1/2/4 | 1/5/7 | 1/3 |
| 24 | 15固定 | 1/6/7/8 | 4 | 2 | 1/2/4 | 1/5/7 | 3 |

# H×K×M整合表
| H | K | M | 場所 |
|---|---|---|---|
| 1 | 2/5 | 1/4/8 | 屋外または窓際 |
| 2 | 2-6 | 2/3/6 | 屋内外 |
| 3 | 3/4 | 1/8 | 屋外 |
| 4 | 2-6 | 任意 | 屋内 |
| 5 | 5-8 | 任意 | 屋内 |
| 6 | 6-8 | 3/4/5/6 | 屋外または窓越し |
| 7 | 任意 | 任意 | 屋内 |
| 8 | 6-8 | 任意 | 屋内 |

- E18のMは場面固定の雹として扱い、H2またはH6のK条件だけを確認する
- Eの固定内容が最優先。表に共通部分がないH/K/Mは候補へ入れない

# 共通末尾
photorealistic raw photo, a natural color photograph with distinct plausible colors in the subject
and environment, natural skin texture with visible pores, authentic candid feel, restrained
cinematic color grading, sharp focus on the intended subject, highly detailed, 3:4 vertical,
clean uncolored frame edges

# 共通ネガティブプロンプト
anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like face, mannequin,
distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs,
harsh flash, blown highlights, heavy makeup, black-and-white, monochrome, grayscale, sepia-only,
near-achromatic rendering, red light leak, orange light leak, magenta light leak, red haze,
orange haze, magenta haze, red fogging, orange fogging, magenta fogging, colored edge fog,
watermark, text, logo, brand logo, product label, store signage, low resolution, blurry
```

> モデル別のL2.5運用上の注意は [inline-random.md](inline-random.md) を参照。生成用コードブロックには、注意対象となる語彙の一覧を持ち込まない。

---

## B. 使い方の例

**そのまま回す**

> `上のメタプロンプトを貼って、3案作って`

**同じ人物でシーンだけ変える**

> `Q=2, A=5, A-2=7, B=2, C-1=1, C-2=3 は固定。Eは未使用群を優先して6案。`

**天気の変わり目**

> `E15-18を1つずつで4案。Eの天気指定を優先。`

**再現性を持たせる**

> `SEED=4821で3案。各選択後のstateも表示。`

---

## C. 出力サンプル

### C-1. 天気の変わり目（D4 / E15 / L2）

選択: E=15 → D=4, Q=1, A=4, A-2=7, B=2, C-1=2, C-2=5, F=9, L=4, H=2, K=4, M=2, I=2, N=1

整合: E15の候補内で、H2 × K4 × M2が整合。Eの「一粒目を見る」動作を使い、別のGは追加しない。

**English**

```
Photorealistic raw photo of a 23-year-old adult Japanese woman on her way home from work.
She has a softly square face, long monolid eyes, straight low-set brows, a straight nose with a low
bridge and defined tip, a wider mouth, and a softly defined square jaw. She has a healthy natural
build with average proportions and dark brown hair in a high ponytail with loose strands at the
temples. She wears a tailored black blazer over a plain white tee and trousers.

On a summer street in early afternoon, she notices the first raindrop darkening the dry asphalt,
then looks up at the overcast sky. Her movement pauses naturally in that exact moment. Flat even
diffused daylight is cool and nearly shadowless. A third-person documentary observer photographs
her with 35mm full-body framing that includes the street and changing sky.

Photorealistic raw photo, a natural color photograph with distinct plausible colors in the subject
and environment, natural skin texture with visible pores, authentic candid feel, restrained
cinematic color grading, sharp focus on the intended subject, highly detailed, 3:4 vertical,
clean uncolored frame edges.

Negative prompt: anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like
face, mannequin, distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused
fingers, extra limbs, harsh flash, blown highlights, heavy makeup, black-and-white, monochrome,
grayscale, sepia-only, near-achromatic rendering, red light leak, orange light leak, magenta light
leak, red haze, orange haze, magenta haze, red fogging, orange fogging, magenta fogging, colored
edge fog, watermark, text, logo, brand logo, product label, store signage, low resolution, blurry.
```

**日本語訳**

23歳の成人日本人女性が仕事帰りの夏道で、乾いたアスファルトに落ちた夕立の一粒目を見てから空を見上げる。柔らかい四角形の輪郭、一重の切れ長の目、ダークブラウンの高いポニーテール。黒いブレザーと白T、パンツ姿。曇天の拡散光で、通りの向かいから35mmの全身ドキュメンタリーとして撮る。自然なカラーで画面端に色かぶりを付けない。

### C-2. L2.5（D6 / E24）

選択: E=24 → D=6, Q=3, A=2, A-2=1, B=8, C-1=1, C-2=3, F=15固定, L=6, H=4, K=2, M=4, I=1, N=3

整合: E24の固定服と動作を保持。H4 × K2 × M4が整合し、E24の許可集合内だけで選択。

**English**

```
Professional fashion editorial photograph of a 25-year-old adult Japanese woman in a bright hotel
room after rain. She has a balanced oval face, almond-shaped eyes with natural creases, straight
medium-thickness brows, a slim straight nose, a defined cupid's bow, and a gently tapered jaw, with
a small beauty mark under one eye. She has a fine-boned frame and jet-black long straight hair,
glossy and center-parted.

Fully clothed in a matte silk-blend dress with a high neckline, she sits naturally on a chair by a
tall window. Morning daylight filtered through a white curtain falls gently across the quiet folds
of the fabric. The camera is someone nearby, using an 85mm portrait lens with shallow depth of field
and tight upper-body framing.

Photorealistic raw photo, a natural color photograph with distinct plausible colors in the subject
and environment, natural skin texture with visible pores, authentic candid feel, restrained
cinematic color grading, sharp focus on the intended subject, highly detailed, 3:4 vertical,
clean uncolored frame edges.

Negative prompt: anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like
face, mannequin, distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused
fingers, extra limbs, harsh flash, blown highlights, heavy makeup, black-and-white, monochrome,
grayscale, sepia-only, near-achromatic rendering, red light leak, orange light leak, magenta light
leak, red haze, orange haze, magenta haze, red fogging, orange fogging, magenta fogging, colored
edge fog, watermark, text, logo, brand logo, product label, store signage, low resolution, blurry.
```

**日本語訳**

25歳の成人日本人女性が雨上がりの明るいホテル客室にいる。卵型の輪郭、自然な二重のアーモンド形の目、目の下の小さなほくろ、黒いロングストレート。マットなシルク混のハイネックドレスで窓辺の椅子に座り、白いカーテン越しの朝の光が布へ柔らかく落ちる。隣にいる人の視点から85mmで上半身を撮る自然なカラー写真。

---

## D. 単体テンプレート

```
Photorealistic raw photo of a [Q: 23-year-old adult など] Japanese woman with [A: 顔の造作],
[A-2: 顔のアクセントまたは省略], [B: 体型], and [C-1: 髪色] [C-2: 髪型].
[E: シーン骨格を、場所・主動作・視線ごと一文に統合].
She wears [F]. [H]. [K], [L], [M]. [N]. [I].
Use E's action and viewpoint without adding a separate generic pose.
Natural color photograph, clean uncolored frame edges, 3:4 vertical.
```

---

## E. 第1弾（random/）との差分

| 項目 | 第1弾 | 第2弾 |
|---|---|---|
| 年齢(Q) | 20代前半の固定文 | **23〜26歳の独立4択** |
| 顔(A) | 顔・印象が混在した10種 | **輪郭・目・眉・鼻・口・顎だけの中立8種** |
| 顔アクセント(A-2) | なし | **8枠。4種＋なし4** |
| 髪(C-1/C-2) | 色と型が一体 | **色4 × 型10。Aから独立** |
| シーン | 場所中心の14場面 | **動作・視線・場所を束ねた24場面** |
| ムード(D) | 7種を独立抽選 | **Eから6群を導出** |
| ポーズ(G) | 独立10種 | **廃止。Eの主動作を使用** |
| 光・時間・天気 | 光へ混在 | **H/K/L/Mを分離し、有効候補から抽選** |
| 視点(N) | なし | **6種。ただしEの意味を変えない候補のみ** |
| シード | 生番号を後補正 | **状態更新式で有効候補から直接選択** |
| 表現レベル(J) | L1〜L2 | **L1〜L2.5。E23・24がL2.5** |

第二弾は、きっかけ、生活の手元、気配のツーショット、天気の変わり目、静かなマジックリアリズム、大人っぽいエディトリアルに特化する。

---

## F. 各モデルでの注意

| モデル | 補足 |
|---|---|
| Midjourney | ネガティブは `--no` に分け、末尾に `--ar 3:4 --style raw` |
| Stable Diffusion / Qwen | Negative prompt欄を分け、実写系モデルを使う |
| ChatGPT / Claude | コード実行が使える場合はstate計算を実行し、選択stateを表示する |
| Gemini | 生成用コードブロックだけを貼り、L2.5はE23・24の肯定的な場面文を保つ |
| nano-banana系 | 同じ人物を維持するときは、最初の生成画像を参照画像として併用する |

- 同一人物を続ける場合はQ/A/A-2/B/C-1/C-2を固定し、最初の生成画像を参照する。
- Eが指定した主動作・視線・視点を、追加の汎用ポーズで上書きしない。
- 出力は自然なカラー写真に固定し、白黒、単色化、赤・橙・マゼンタの光漏れ、色付きの画面端モヤを使わない。
