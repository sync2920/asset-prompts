# 181. 肌でいたずらするチビドゥードルズ

顔から胸元までの実写人物の上——肌を主舞台に、服・髪にも——黒線のチビドゥードルが現れる。数体は2.5Dに飛び出し、本人似のミニ分身も交えて小さないたずらをする。主役は本人と同じポーズを取り、感情だけをアニメ的に爆発させる分身1体。

- **比率:** 4:5
- **固定:** 総数7体（黒マーカー落書きタッチのチビ）。出現は人物の上のみ（肌が主体、服・髪にも1〜2体）で、背景には一切出ない。主役1体は本人似の分身で他の倍サイズ、本人のポーズのアイデアを共有する。飛び出しは2体以上。色は黒一色＋主役横の赤ハート1個のみ。
- **可変:** 背景、種類、いたずらとアンサンブル芸、出現面の配分、本人のポーズとリアクション、獣耳モチーフ、コミック記号の種類と配置。
- **見せ場:** 本人が毎回違う遊びポーズ→鎖骨に立つ分身が同じポーズのアイデアを「><」目・牙付き大笑いの誇張カオス版で再現するミニツーショット。本人は半分渋々、分身は大はしゃぎの温度差がコメディの核。黒一色の画面で主役の横の赤ハート1個だけが色を持つ。

## 設計メモ

- **計数の破綻対策:** 厳密な数値は総数7のみに絞る。旧版は「7体＋内訳3/2/2＋4種類以上＋分身2体以上＋いたずら4つ以上」と数値制約が5重で、合体・欠損・重複が起きやすかった。内訳は "roughly half / a couple / at least two" の緩い表現にし、種類数の下限指定は「全員違う見た目」と実質重複なので削除。
- **出現面の拡張、ただし肌主体:** 当初は肌限定（服・髪は禁止）だったが、人物全体（肌・服・髪）に拡張。ただしデフォルトは「肌が主体、服・髪に1〜2体」とし、タイトル「肌でいたずらする」との整合と、肌から飛び出す署名的瞬間の主役感を保つ。背景だけは禁止を維持し「本人に住み着いている」コンセプトを守る。面ごとの物理を分けるのが肝: 平面段階の線画は「描ける面」（肌・布）に置き、髪は平面線画が不自然なので飛び出した個体の遊び場（登る・ぶら下がる・巣にする）とする。旧版にあった「髪から出現しない vs 毛束ブランコ」の矛盾はこの拡張で自然解消。
- **ポーズは毎回モデルに発明させる:** 固定デフォルト（猫の手）は置かず、例示（猫の手・指ハート・頬つぶし・力こぶ・ピース）だけ渡して毎回変えさせる。主役のポーズミラーはポーズ非依存なのでどのポーズでも成立する。ただし遊びポーズは手が頬の横に来がちで、「顔ゾーン最大2体」の領域と手（＝肌なので発生面）が重なり顔まわりが渋滞しやすいため、"hands stay at cheek level or below, leaving the face itself clear" のガードは維持。
- **服のいたずらの安全設計:** 布への効果は「袖口を引く」「襟の皺から覗く」「小さな布のつまみ」まで。服の露出・フィット・形状の変更は明示的に禁止し、178派生と同方針で参照以上の露出を絶対に増やさない。
- **ヒーロー構造:** 7体が等価に振る舞う指示だと画面がノイズ化する。参考画像（実写の本人＋等身大アニメ分身が同じ猫の手ポーズ）のテイストを取り込み、「本人のポーズを分身がミラーリングして感情最大化」を主役に据えた。旧主役（首筋滑り台）は差し替え段落として下に保持。あわせて「顔ゾーンは最大2体」で顔の埋没を防ぐ。
- **分身のアニメ感情顔:** 参考画像から「><」目・開口の牙笑い・頬の照れ線・猫耳と尻尾を分身の標準装備に採用。照れ線は "in the same black ink" と明記（無指定だとピンクの照れが出て "no fill colors" と矛盾する）。スタイルアンカー（imperfect black ink lines のチビ）は維持し、似せ要素は「髪シルエット＋アクセサリーモチーフ1点」限定のまま。要素をANDで増やすと Avoid の "realistic tiny humans" と衝突して写実ミニ人間が出る。
- **壁の落書き絵感（線質の指定）:** 参考画像の壁ドゥードルが持つ「マーカーで描いた落書き」の線質を全ドゥードル・記号に適用: 揺れた線、不均一な線幅、二度描きの重なり、交差のはみ出し、面はベタ塗りせずガリガリしたハッチング。"crisp line art" 系の表現はクリーンなベクター線に寄って落書き感が消えるので、シャープなのはフォーカス（macro detail）だけに限定し、線そのものはラフを維持。肌の上では「表面に乗った描きたてのペンインク」と読ませ、皮下インクのタトゥー解釈も同時に防ぐ。
- **賑やかさの足し方（キャラ数は増やさない）:** 画面のエネルギーはコミック記号（ハート・星・キラキラ・汗・渦・効果線）の散布と、アンサンブル芸（毛束の綱引き、鎖骨間ジャンプ、主役への応援団）で足す。キャラ総数を増やすと計数破綻が戻るため7のまま。記号は "hovering just off the surface" の浮遊を維持してタトゥー化（Avoid の "no tattoos" との競合）を防ぎ、顔だけは無記号を厳守して face scribbling 化を止める。
- **赤ハート1個だけの色:** 黒一色の規律を全体で守りつつ、主役の横に唯一の色として小さな赤ハートを置く。黒だけの画面に一点だけ色が入ると視線がそこに集まる（目立つ要素）。スタイルアンカーの例外は "exactly one" と数を固定して色の拡散を防ぐ。
- **主役の倍サイズをデフォルト化:** 調整ノブだった "twice the size" を本文へ昇格。記号で画面が賑やかになった分、主役の格を上げないと埋没する。
- **元ネタ（壁ドゥードル・シャドウ版プロンプト）から移植した要素:** ①感情の温度差——本人は「なぜ付き合ってるんだろう」と半分渋々、分身は大はしゃぎ。この対比がコメディの核。②ポーズミラーの緩和——「完全一致」から「同じポーズのアイデアを誇張カオス版で」へ。厳密ミラーは絵が固くなり生成も失敗しやすい。③指差し・フィンガーガンの禁止——放置するとモデルがこの2つに収束する既知の癖。④ハードコード禁止ガード——参照にない特徴（髪色・アクセ等）を勝手に足さない明文化。⑤cute-never-creepy——黒線の小人は不気味側に倒れうるので明示。⑥手の解剖学ネガ——手が主役級に写るポーズ構図なので extra fingers / malformed hands を追加。壁構図・等身大・全身フレーミングは取り込まない（このファイルの核は「肌の上のチビ」）。
- **サイズは相対指定:** "1–3 cm" はモデルに測れない。「本人の目の幅以下」と身体部位基準に変更。
- **否定形は無視されやすい**（178派生の知見）: 線のスタイルは冒頭で肯定形（black outlines, white or transparent interiors）として宣言し、Avoid 行は末尾に圧縮。
- **文字数:** 4,859字（実測）。5,000字以内。賑やか化と落書き線質の追加で一度5,838字まで膨れたため、機能要素は全部残して冗長表現だけ圧縮した。追記するときは必ず実測で確認する。

## 完成プロンプト

```text
Create a photorealistic 4:5 portrait from the uploaded reference, framed head to upper chest, 85mm portrait lens, moderate depth of field. Preserve the subject's apparent age, exact face, skin, hair, body proportions, accessories, and visible outfit without beautification or reshaping; infer every such detail solely from the reference and never add features that are not in it. Use a different coherent real-world background each generation, uncluttered and softly blurred. The subject strikes a small playful pose of their own invention, different each generation — cat paws, finger hearts, a cheek squish, a ta-da flourish, or anything equally lighthearted, never a pointing or finger-gun pose — hands staying at cheek level or below so the face stays clear. Their reaction also changes each time, always half playing along and half wondering why: a ticklish giggle, mock surprise, a sweetly reluctant smile.

THE DOODLE CAST:
Exactly seven tiny chibi characters scribbled in rough black felt-tip lines, like graffiti doodled on a wall: wobbly strokes of uneven weight, double-stroked corrections, small overshoots, and loose scratchy hatching for tone — black outlines only, white or transparent interiors, no fills or colors. Each stands no taller than the width of the subject's eye. All seven look different — animals, blobs, fantasy beings, personified objects — and stay cute and cheeky, never creepy. At least two are mischievous mini alter egos of the subject in the same rough chibi style; their likeness comes only from the hair silhouette and one accessory motif from the reference, never from realistic facial features. The alter egos run at maximum cartoon emotion: eyes squeezed into a "><" arc, a wide laughing fanged smile, short parallel blush strokes in the same black ink.

ON-BODY ORIGIN AND 2.5D TRANSITION:
Every doodle lives on the subject — uncovered skin (forehead edge, cheek, jaw, neck, collarbone, upper chest), clothing, or hair — never in the background. Keep most on skin, one or two on clothing or hair, never clustered in one spot. Each obeys its surface: skin drawings bend with the skin's curvature, fabric drawings ride the folds of the cloth, and the hair is the playground of popped-out figures that climb and hang among the strands. Roughly half are still flat drawings, a couple are halfway lifting out, and at least two stand fully popped out as paper-thin 2.5D scribble figures, each still connected to its surface by a foot, a tail, or a thin ink trail, with correct occlusion and tiny contact shadows, lifting cleanly away and leaving skin, cloth, and hair perfectly intact.

HERO INTERACTION:
One popped-out alter ego is the star: standing on the collarbone with tiny cat ears and a curling cat tail, about twice the size of every other doodle, it performs the subject's pose idea at the same moment — a miniature two-shot — as a wildly exaggerated, chaotic cartoon version rather than an exact copy. The subject plays the cute, mildly reluctant real version; the hero is having far more fun. Draw it in the sharpest detail and let the subject's expression clearly react to it. Every other doodle is supporting cast.

COMIC MARKS AND ONE SPOT OF COLOR:
Scatter small hand-drawn emotion marks around the cast — hearts, stars, sparkles, sweat drops, spirals, short motion lines — hovering just off the skin, clothing, or hair in the same rough scribble, enough to feel noisy and celebratory while leaving the face completely free of marks. Exactly one mark breaks the rule: a single small bright-red heart beside the hero — the only touch of color in all the doodle work.

SUPPORTING PRANKS:
The supporting doodles perform varied harmless antics, invented fresh each generation: pressing a tiny cheek dimple, tickling the jaw, tug-of-war with a hair strand, leaping from one collarbone toward the other, a tiny cheering squad for the hero, tugging a sleeve hem — loose inspiration only, not a fixed menu; invent freely beyond these. Show only subtle believable effects — a small dimple, one displaced strand of hair, a gently tented fold of fabric, soft contact shadows — and never change the outfit's coverage, fit, or shape, or the subject's anatomy. Keep at most two doodles inside the face area; eyes, eyebrows, nose, lips, and teeth stay fully unobstructed.

QUALITY:
Soft natural light, realistic skin and fabric texture, sharp focus on the face. The scribbles stay sharply in focus like macro detail while keeping their rough graffiti character — fresh felt-tip ink sitting on top of the surface, never a tattoo beneath the skin — against gentle background bokeh. No realistic tiny humans, no tattoos or stickers, no anime conversion of the real subject, no identity or outfit changes, no wounds or body horror, no nudity, no extra limbs, extra fingers, or malformed hands, no text, logos, or watermarks.
```

## 代替主役（首筋滑り台版・HERO INTERACTION 差し替え段落）

ポーズミラーではなく動きで見せたいときは、HERO INTERACTION をこれに差し替える。

```text
HERO INTERACTION:
One fully popped-out doodle is the star of the image: it slides down the side of the neck toward the collarbone as if on a slide, arms thrown up mid-whee, leaving a faint ink trail behind it. Render this one largest and in the sharpest detail, and let the subject's expression clearly react to it. Every other doodle is supporting cast performing smaller pranks around it.
```

## 調整ノブ

- **計数が崩れる（合体・欠損）:** "Exactly seven" → "Exactly five"。内訳の下限も "at least two stand fully popped out" → "at least one" に合わせて下げる。
- **配分を変えたい:** デフォルトは肌主体（"Keep most of the cast on skin, with one or two settling on the clothing or in the hair"）。服メインなら "let the clothing carry most of the cast"、全面に均等なら "spread the cast evenly across skin, clothing, and hair" に差し替え。
- **手にドゥードルが乗って顔まわりが渋滞する:** 発生ゾーンの列挙に "never on the hands" を追加（手は頬の横に来るため、乗ると顔ゾーン上限をすり抜けて混雑する）。
- **背景に漏れる:** ORIGIN の "never in the background" を段落の先頭に移し、QUALITY に "the background contains zero drawings of any kind" を追加（圧縮時に QUALITY 側の背景文は削ってあるので、漏れが出たときだけ戻す）。
- **主役が大きすぎる/小さすぎる:** "about twice the size of every other doodle" を "noticeably larger"（控えめ）↔ "three times the size"（強調）で振る。
- **本人までアニメ化する / 画面がイラスト寄りに倒れる:** 冒頭に "shot on a full-frame camera, a candid photograph, not an illustration" を追加。Avoid の "no anime conversion of the real subject" は維持。
- **うるさすぎる:** コミック記号を "around the popped-out doodles only" に絞る、さらに静かにするなら「主役の周りに2〜3個」まで戻す。赤ハートを黒に戻せば完全黒一色。
- **もっと賑やかに:** 記号の種類に爆発マーク・音符形の飾りを足す（文字・数字は不可）。総数7→9も可能だが計数破綻リスクが上がるので、まず記号とアンサンブル芸で足すのが先。
- **獣耳の差し替え:** cat ears → devil horns / angel wings / bear ears / bunny ears。尻尾も対応させる。
- **分身が似ない ↔ 写実化する:** 似せ要素を "hair silhouette only" に減らす（写実化する時）↔ "and the outfit's neckline shape" を足す（似なさすぎる時）。
- **顔まわりがうるさい:** 顔ゾーン上限を 2→1 に、または発生ゾーンから cheek を外す。
