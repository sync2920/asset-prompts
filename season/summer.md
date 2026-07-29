# 夏のランダムプロンプト（20代前半・日本人女性・エモ版）

`random2/` を季節で分割したうちの **夏**。四季それぞれで場面・光・空気が別物になるので、
1ファイルに全季節を詰めず、季節ごとに専用のスロット表を持たせる方式に変えた。

この版で変えた3点:

1. **夏に特化** — 季節スロットを廃止し、代わりに「夏の段階(L)」を新設。場面・光・天気・服・髪をすべて夏専用に組み替え
2. **アイドル的なかわいさを出す** — 顔骨格は小顔・引き締ま」で土台を作り、体型は全項目スリム固定。表情スロットにアイドル寄り（polished/luminous/K-idol）3つを混ぜ、地元彼女寄り5つと美人2つで幅を持たせる
3. **エモくする** — フィルムの質感スロット(P)を新設し、共通末尾を「高精細な実写」から「フィルム写真」へ変更。場面を「感情が動く一瞬」に寄せた

- 使い方: 下の「A. メタプロンプト」を ChatGPT / Claude / Gemini に貼る → 出てきた英語プロンプトを画像生成AIへ。
- そのまま画像生成AIに投げたいときは「F. 直接投げ版」へ。
- 安全フィルタ対策は [safe.md](../random/safe.md)、暑さの描写は [expression/02-summer-heat-realism.md](../expression/02-summer-heat-realism.md) に準拠。

---

## 0. 設計メモ（なぜこうしたか）

### 狸顔になる原因と、かっこよさに傾く原因

第1弾・第2弾の顔スロットは、可愛さを出そうとして次の語を重ねていた。

`round face` / `round baby face` / `full cheeks` / `wide-set eyes` / `downturned eyes` / `soft gentle`

これは**狸顔の定義そのもの**（丸顔・たれ目・離れ目＝遠心顔・顔の余白が多い）で、
2つ以上そろうと生成が確実に狸顔へ収束する。しかも同時に年齢も下振れする。

一方、初期のこの夏版では「狸顔回避」のために骨格をシャープに固定しすぎた
（卵型・はっきりした顎・アーモンド目・通った鼻筋）。これは「モデルっぽいかっこよさ」の骨格で、
結果として**かわいさが押し殺され、かっこよさが勝ってしまった**。
その後「丸み許容」に緩めたところ、今度は丸顔＋平均体型が重なって**小太りに寄り、アイドル感が消えた**。

対策は4層で入れてある。

1. **共通指定は「成人・着衣」の最小限** — 顔の形は共通指定に書かず、Aスロットで振る。これにより全員が同じ顔になるのを防ぐ
2. **Aスロットは顔タイプ診断ベースの10種** — 「顔の形＋目＋鼻＋口＋表情」をセットで振る。キュート系3・アクティブキュート2・フレッシュ2・アイドル寄り2・美人1で構成。各項目に具体的パーツ差分（二重幅・目と眉の距離・鼻先・口幅・涙袋・頬のふくらみ）を書き込み、「小顔＋笑顔」だけの似通りを解消する。全項目「小顔」は共通だが顔形とパーツが違うのでバリエーションが出る
3. **体型は全項目スリム固定** — `healthy natural` `average proportions` `soft natural` は生成でぽっちゃりに寄るため除外。8項目すべてに slim/slender/petite を入れ、アイドル体型を担保
4. **negative で狸顔とぽっちゃりを殺す** — `round chubby face, puffy cheeks, wide-set eyes, baby face, flat nose bridge, short receding chin`

**アイドル的なかわいさは「小顔＋スリム体型」が土台にあって初めて成り立つ。**
体型で「スリム」を担保し、Aスロットで「顔の形＋パーツ＋表情」を個別に振ることで、
「全員同じ顔」を防ぎつつ「アイドル感」を維持する。顔タイプ診断の軸（丸み×曲線／直線×曲線／
くっきり二重・高い鼻）を入れることで、「ただの可愛い」から抜け出す。

### エモさの作り方

エモさは雰囲気の形容詞（`nostalgic` `emotional`）では出ない。次の3つの物理で作る。

1. **フィルムの質感** — 粒子、ハレーション、褪せた黒、光漏れ。スロットPを新設した
2. **光の事故** — 白飛び、逆光、フレア、木漏れ日。制御された綺麗な光の逆
3. **一瞬の選び方** — 「何かが終わった直後」「まだ始まっていない」を撮る

> ⚠️ **共通末尾を変えてある。** `8k resolution, highly detailed, sharp focus` はエモさと真っ向から
> ぶつかる（高精細＝記憶っぽくない）。この夏版では末尾をフィルム語彙に差し替えている。
> カリッとした実写が欲しい場合は expression/02 のカメラブロック版を使い、この版は使わない。

### 汗を描かない

[expression/02](../expression/02-summer-heat-realism.md) の実測: **肌に汗を描くと「汗かきすぎ」の破綻が出る。**
暑さは 空気（結露・かすみ）→ 小道具（冷えた缶・氷）→ 素材（リネンのしわ）の順で出し、
肌の汗は描かないのが最も安定する。この版はその原則をスロット設計に織り込んである。

### 学生モチーフを使わない

夏のエモの定番（部活帰り・宿題・教室・プールの授業）は強力だが、**被写体の年齢が下振れする**。
この版では全部、成人版に置き換えてある（帰省・仕事帰り・ひとり暮らしの部屋・実家）。
「大人が夏を思い出す」構図のほうが、結果としてエモさも強い。

---

## A. メタプロンプト（これをコピーして貼る）

```
あなたは画像生成AI用のプロンプト作成アシスタントです。
以下のスロット表からランダムに1つずつ選び、組み合わせて英語の画像生成プロンプトを作ってください。
季節は夏に固定です。

# 出力ルール
- 出力数: 3案（指定があればその数）
- 各案について「選ばれたスロット一覧」→「英語プロンプト」→「日本語訳（要約でよい）」の順で出す
- 被写体は必ず a 23-year-old adult Japanese woman と年齢を数字で書く
- 場面・服装・小物のどれかに、成人であることが読み取れる要素を1つ入れる
  （仕事帰り、ひとり暮らしの部屋、帰省、運転席 など）。学生を思わせる要素は入れない
- 【必須】下の「共通の顔の指定」を全案にそのまま入れる（狸顔を防ぐため）
- 【必須】肌に汗を描写しない。暑さは空気・小道具・素材のふるまいで出す
- 表現レベルは L2（指定があればそのレベル）に従う
- スロットDのムードを軸にして、E/F/G/H/I/K/L/M/N/P が矛盾しない組み合わせだけを選ぶ
- 決める順番: D → E →（Eの時間帯・天気・屋内外の制約）→ K/M → 「H×K×M 禁則」を満たすHに絞る
  → P/F/G/I/N
- 案どうしでムード(D)とシチュエーション(E)が重複しないようにする
- 構図は正面・斜め前・横顔を優先し、後ろ向きで肩越しに振り向く全身構図は使わない
- 複数案ではバストアップ・腰上・膝上・全身を分散させ、全案を同じ距離で撮らない
- 服・小物・背景に実在ブランドのロゴ・商標・商品パッケージ・店舗看板を出さない。無地か架空の柄にする
- 末尾に共通のフィルム指定とネガティブプロンプトを付ける

# 乱数の決め方
シード指定がない場合は毎回ちがう組み合わせを自由に選ぶ。
シード指定（例: SEED=4821）がある場合は、下のスロット番号 n と項目数 c を使って
  index = (SEED + n * 7) mod c   → 選ぶ番号は index + 1
で決定し、同じシードなら同じ結果になるようにする。

  n=1  A  顔          c=10
  n=2  B  体型        c=8
  n=3  C-1 髪色       c=4
  n=4  C-2 夏の髪     c=10
  n=5  D  夏のムード  c=8
  n=6  E  夏の場面    c=30
  n=7  F  夏の服装    c=14
  n=8  G  ポーズ      c=10
  n=9  H  夏の光      c=9
  n=10 I  カメラ      c=8
  n=11 K  時間帯      c=8
  n=12 L  夏の段階    c=6
  n=13 M  夏の天気    c=8
  n=14 N  視点        c=5
  n=15 P  フィルムの質感 c=8

  ※Jは表現レベルなので乱数の対象外（指定がなければL2）。
  ※シードで出た番号が整合ルールに反する場合は、そのスロットだけ
    整合ルールを満たす最も近い番号へずらし、その旨を明記する。

────────────────────────
# 共通の顔の指定（全案に必ず入れる。成人と狸顔防止の最小限）

an adult Japanese woman, fully clothed

※「共通の顔」は成人であることと狸顔防止だけを担保し、顔の形・目・表情はAスロットで振る。
　これにより、Aスロットごとに顔の骨格から変わるので、全員が同じ顔になるのを防ぐ。
※cute / baby face の語は使わない（年齢が下振れする）。
※「小顔・引き締ま」はAスロットの個別指定で出す。共通指定には顔の形を書かない。

────────────────────────
【A】顔（顔タイプ診断ベース。顔の形＋目＋鼻＋口＋表情をセットで振る。全案で別の顔になる）
※各項目は「顔タイプ×具体的パーツ」で構成し、小顔は全項目の前提。cute / baby face は使わない。

── キュート系（丸み×曲線パーツ。守ってあげたくなる甘さ）
1. a small round-oval face with a broad forehead, large eyes with narrow double lids and a subtle under-eye bag, a low straight nose with a soft tip, full narrow lips, a small snaggletooth when she smiles
2. a small round-oval face, big eyes that curl into crescents when she laughs, a narrow double lid with a wide gap between eyes and brows, a small nose, plump lips with a narrow mouth width, a soft unguarded smile
3. a small face with a gentle jaw and a natural fullness to the cheeks, round bright eyes, a mid-height nose that does not droop, a small full lower lip, an open warm laugh
── アクティブキュート系（丸み＋目力・個性）
4. a small face with slightly wider cheeks, strong bright eyes with a defined crease, a straight nose, a quick lively grin, an energetic open expression
5. a small oval face, upturned cat-like eyes with a sharp inner corner, a small chin, a mischievous lively look, a grin she can't hold back
── フレッシュ系（直線×曲線ミックス。爽やか親しみやすさ）
6. a small oval face with clean straight lines mixing with soft curves, fresh almond eyes with a natural crease, a straight slim nose, a small neat mouth, a bright friendly smile
7. a small face with a defined jawline, clear double-lidded eyes set at a natural width, a mid-height straight nose, a natural lip line, an easy approachable smile
── アイドル寄り（polished・luminous・K-idol）
8. a small V-line face, polished idol-like features, luminous skin, large sparkling eyes with a narrow double lid, a high straight nose, glossy full lips, a radiant camera-ready smile
9. a small face with K-idol straight brows and gradient lips, large round eyes with a defined crease, a slim straight nose, striking mixed-look features on Japanese bone structure, a bright polished smile
── 美人系（くっきり二重・高い鼻・涼しげ）
10. a small slim face, long narrow eyes with a deep crease, a high nose bridge, a refined level gaze that breaks into a small composed smile

【B】体型（8）※全項目スリム基準。胸の大きさでバリエーションを持たせる
1. slender petite build, small frame, small bust
2. slim and petite, delicate shoulders, modest bust
3. tall and slim, long limbs, model proportions, small bust
4. slim with a small waist, balanced proportions, medium bust
5. athletic and slim, toned without bulk, small bust
6. slender, fine-boned, narrow wrists, modest bust
7. slim editorial build, elongated silhouette, small bust
8. petite and slim, compact and proportionate, medium bust

【C-1】髪色（4）
1. jet-black
2. dark brown
3. beige
4. ash

【C-2】夏の髪（10）※どれも「その日の出来事」が髪に残っている状態
1. a high ponytail with damp strands stuck at the temples
2. long hair still wet, left to dry on its own
3. front strands stuck to her forehead by the heat
4. hair twisted up into a careless bun, ends escaping
5. a half-up style already coming loose in the wind
6. a short bob with the ends kicking out in the humidity
7. a single braid over one side
8. hair flattened where a cap sat on it a minute ago
9. hair tucked behind one ear, falling out again in the wind
10. a short cut she got a few days ago, still not used to it

【D】夏のムード（8）★軸になるスロット
1. 夏のはじまりの高揚 / the first day it is properly summer, and she can feel it
2. 弾ける笑顔 / laughter that comes before she can stop it, bright and physical
3. 青い時間の高鳴り / the blue hour buzzing, everything about to start
4. 甘酸っぱい二人 / the camera is someone beside her, and summer is doing the rest
5. 夕方の浮かれた足取り / the giddy lightness of a summer evening with nowhere to be
6. 夏祭りの熱 / the heat and noise of a festival pulling her forward
7. 夏が終わる予感 / the first small sign that it is already ending
8. 記憶の夏 / it reads like someone's memory of a summer, not a photo taken today

【E】夏の場面（30）※Dのムードに合う群から選ぶ
※末尾の [屋内]/[屋外] と (K…, M…, L…) はその場面が成立する条件。指定がないものは任意。
※手持ちの小物は場面に明示してある。生成AIが勝手にカゴやバッグを描くのを防ぐため、
　小物が指定されていない場面では「手ぶら」を意味する（何も持たせない）。
── 水と体温
1. プールサイド、濡れた足跡が数歩先で消えかけている、手ぶら [屋外] (K3/K4)
2. 海からの帰りの電車、髪に塩が残ったまま窓に頭を預ける、手ぶら [屋内] (K5/K6)
3. 麦茶のグラスの結露を指でなぞって、跡が線になる [屋内]
4. かき氷を食べる手が止まる、こめかみを押さえて [任意] (K3/K4)
5. 自販機で買った缶を頬に当てて目を閉じる [屋外]
── 夏の音
6. 風鈴が鳴った方を見る、縁側、手ぶら [屋内]
7. 扇風機の前で声を当てて、髪が全部後ろに流れる、手ぶら [屋内]
8. 蝉が急に鳴き止んだ数秒の静けさに顔を上げる、手ぶら [屋外] (K3/K4)
9. 遠くの花火の音が遅れて届く、見上げた横顔、手ぶら [屋外] (K7/K8)
── 帰り道と灯り
10. 夏祭りの帰り、屋台の灯りを横に受け、カメラと並んで歩く、手ぶら [屋外] (K7/K8)
11. 線香花火の最後の玉が落ちる直前、しゃがんだ膝の上 [屋外] (K7/K8)
12. 無人駅のホーム、電車を待つあいだに影が長くなる、手ぶら [屋外] (K5)
13. 自販機の光だけが灯る夜道、ペットボトルを持ったまま [屋外] (K7/K8)
14. 花火大会の帰り道、人の流れを外れてカメラの方へ歩いてくる、手ぶら [屋外] (K7/K8)
── 部屋と昼
15. 昼寝から覚めた瞬間、畳の跡が頬に残っている [屋内] (K3/K4)
16. 白いカーテンが風で膨らんで、部屋に一瞬だけ影が動く [屋内] (K2/K3/K4)
17. 冷蔵庫を開けた冷気の前でしばらく動かない [屋内]
18. 蚊取り線香の煙が窓の光の中でかたちになる [屋内] (K4/K5)
19. 読みかけの本を伏せたまま、扇風機が首を振るのを見ている [屋内]
── 移動
20. 自転車を押して坂を上る、まだシャツが背中に貼りつく前 [屋外] (K2/K5)
21. 車の助手席、窓から腕を出して手のひらで風を受ける [屋内=車内]
22. 帰省の電車、田んぼが窓を流れていく、手ぶら [屋内] (K4/K5)
23. 実家の玄関を開けた瞬間の、家の匂いと冷気 [屋内]
── 天気
24. 夕立の直前、風が変わって空が黄色くなる、手ぶら [屋外] (M2)
25. 夕立に降られて軒下、笑うしかない数分、手ぶら [屋外] (M3)
26. 雨上がり、アスファルトから湯気が立つのを見ている、手ぶら [屋外] (M4)
27. 入道雲を見上げて立ち止まる、影が足元だけ、手ぶら [屋外] (K3/K4, M1)
── 夏の終わり
28. しまい忘れた花火の袋を見つける [屋内] (L5/L6)
29. 蝉の抜け殻を指でつまんで、光にかざす [屋外] (L4/L5)
30. 誰もいない夕方のプール、水面だけが揺れている、手ぶら [屋外] (K5/K6, L5)

【F】夏の服装（14）※シルエットで分ける。小物・アクセサリーはEスロットかGスロットで指定
── ワンピース系
1. a white cotton sundress with thin straps and a small floral print
2. a yellow gingham one-piece dress, light and airy
3. a navy sailor-collar dress, slightly grown-up
── スカート系（短め）
4. a cropped tee and a denim mini skirt
5. a fitted tank top and a pleated mini skirt
6. a loose blouse and a short cotton skirt
── スカート系（ロング・ワイド）
7. a white tiered midi dress that moves in the wind
8. a gingham blouse tucked into a full skirt
9. a simple white tee and a colourful patterned long skirt
── パンツ系
10. a loose off-shoulder blouse and denim shorts
11. a striped boat-neck tee and white cotton shorts
12. a ribbed tank top and loose cotton shorts
── 和・浴衣系
13. a loose cotton yukata, the front collar overlap visible, the obi knot not emphasized
14. a cami dress over a plain white tee, sport sandals

【G】ポーズ・仕草（10）※正面・斜め前・横顔を分散。後ろ向き振り返りは使わない
1. standing still, looking up at the sky
2. wiping her forehead with the back of her wrist
3. lifting her hair off the back of her neck to let the air in
4. crouching down to look at something on the ground
5. walking toward the camera, laughing naturally
6. resting her head against a window, watching outside
7. pressing something cold against her cheek with her eyes closed
8. shown in side profile, gaze directed off-frame
9. sitting and doing nothing at all
10. reaching toward the camera to hand something over

【H】夏の光（9）※時間帯(K)・天気(M)とは独立。必ず「H×K×M 禁則」を確認する
1. hard backlight blowing the background to white, only the edge of her hair lit
2. dappled light through leaves falling in patches across her face and clothes
3. strong sun through a towering cumulus cloud, shadows crisp and short
4. low slanting evening light, everything sinking into orange
5. reflected light off water moving up onto her from below
6. diffused light through a white curtain, the room close to blown out
7. artificial light from a stall, a firework, or a vending machine lighting only her face
8. the blue minute right after sunset, edges dissolving
9. flat low-contrast light under rain, every color deepened and soaked

【P】フィルムの質感（8）★エモさの芯
1. disposable-camera look, hard direct flash and heavy grain
2. expired film, colors shifted and blacks gone soft
3. strong halation, highlights bleeding out past their edges
4. a light leak, red fogging in from one edge of the frame
5. Fujifilm-like color, cyan in the shadows, loose warm highlights
6. coarse grain, low contrast, blacks lifted
7. lens flare cutting across the frame, ghosting in the highlights
8. very slightly out of focus and handheld, and it does not matter

【I】カメラ・構図（8）
1. 35mm compact camera at eye level, frontal waist-up framing
2. 50mm, a natural conversational distance, three-quarter front view
3. wide and close, the way a disposable camera sees
4. telephoto from far off, air between the camera and her
5. looking up, the sky taking most of the frame
6. shot through window glass, reflections layered over her
7. handheld side-profile framing, slightly tilted and not corrected
8. full body from the front or side, the place mattering as much as she does

【K】時間帯（8）※夏の一日
1. early morning, the few cool hours
2. mid-morning, before the sun turns hard
3. noon, shadows straight down
4. two in the afternoon, the hottest hour
5. late afternoon, shadows stretched long
6. the blue minute just after sunset
7. night, the air still warm
8. late night, cool at last

【L】夏の段階（6）※季節スロットの代わり
1. the first day after the rainy season lifts, the air changed overnight
2. high summer, the hottest few weeks
3. the Obon week, the town emptied out
4. late summer, the light coming in at more of an angle
5. the end of summer, fewer cicadas each day
6. a summer remembered, not this one

【M】夏の天気（8）
1. clear sky with towering cumulus
2. thin overcast, a white sky
3. a sudden evening downpour
4. just after the downpour, steam coming off the asphalt
5. heat shimmer (kagerou)
6. the strange bright stillness before a typhoon
7. strong sea wind
8. warm heavy night air

【N】視点（5）※カメラが誰の目か
1. third-person observer — a documentary camera watching from a distance
2. passerby — a fleeting glance as she passes
3. the camera is someone beside her — a friend, a partner, the viewpoint of intimacy
4. found photo — an angle nobody composed, like a frame from a used-up roll
5. her own gaze — a mirror shot or a held-at-arm's-length shot

【J】表現レベル（指定がなければ L2）
- L1: 完全に健全。雰囲気は表情と光のみ
- L2: 大人っぽさ・落ち着いた色気。全身着衣のまま、身体ではなく光・陰影・レンズの語彙で作る
- L2.5: 服の仕立てと光だけで出す。身体部位を主語にしない。
        ※夏は薄着・濡れ髪が絡むぶん L2.5 は落ちやすい。下の「夏の禁止組み合わせ」を厳守する

────────────────────────
# 整合ルール
- D1 夏のはじまりの高揚 → E 1/5/20/27, K 2/3/4, P 1/5/7, H 1/2/3, I 3/5, N 3, L 1/2, レベル L1
- D2 弾ける笑顔 → E 4/5/7/8/20/21/25/27, K 2/3/4/5, P 1/5/7, H 1/2/3/5, I 2/3, N 3, L1〜L2
- D3 青い時間の高鳴り → E 9/10/13/14/21, K 5/6/7, P 1/4/7, H 7/8, I 1/3/7, N 1/3, L1〜L2
- D4 甘酸っぱい二人 → E 1-5/10-14/20-23, P 1/2/8, H 任意, I 2/3, N 3, L1〜L2
- D5 夕方の浮かれた足取り → E 10/12/14/20/21/25, K 5/6/7, P 1/5/7, H 4/7/8, I 2/7, N 3, L1〜L2
- D6 夏祭りの熱 → E 10/11/13/14/25/28/29/30, K 6/7/8, P 1/4/7, H 7/8, I 1/3/7, N 1/3, L1〜L2
- D7 夏が終わる予感 → E 12/22/26/28/29/30, L 4/5/6, P 2/3/6, H 4/8/9, I 4/6/8, N 1/4, L1〜L2
- D8 記憶の夏 → E 任意, P 2/3/6/8, H 任意, N 1/4, L 6, レベル L1〜L2

- K・M は上で指定しない。E の制約と下の禁則表から決まる
- L（夏の段階）は上で指定しなければ任意。D7 のときだけ 4/5/6、D8 のときは 6 に絞る
- 上のリストに無い組み合わせでも、明らかに矛盾しなければ可

# H×K×M 禁則
| H | 成立する K | 成立する M | 屋内/屋外 |
|---|---|---|---|
| 1 hard backlight blowing out the background | 2, 5 | 1, 2 | 屋外 |
| 2 dappled light through leaves | 2, 3, 4, 5 | 1 | 屋外 |
| 3 strong sun through cumulus | 3, 4 | 1, 5 | 屋外 |
| 4 low slanting evening light | 5 | 1, 2, 4 | 両方 |
| 5 reflected light off water | 3, 4, 5 | 1, 5 | 屋外 |
| 6 diffused light through a white curtain | 2-5 | 任意 | 屋内 |
| 7 artificial light from a stall or vending machine | 7, 8 | 任意 | 両方 |
| 8 the blue minute after sunset | 6 | 1, 2, 4, 8 | 両方 |
| 9 flat low-contrast light under rain | 2-6 | 3, 4, 6 | 両方 |

- E側に (K…, M…, L…) や [屋内/屋外] の制約があるときは、そちらを最優先し H を合わせる
- H7 は屋外が基本だが、窓越し・車内なら屋内でも成立する
- 雨・雨上がり・台風前（M3/4/6）に成立する光は H9（と屋内の H6）だけ。晴天のHは使えない

# 夏の禁止組み合わせ（安全設計）
夏は薄着・濡れ・汗が同居しやすく、意図せず線を越えやすい。以下は同時に使わない。

- **濡れている + 薄手 + 白** の3点セット（透けの示唆になる。2つまでに留める）
- **水着 / bikini / swimsuit** は扱わない。プールや海の場面でもTシャツやワンピースを着せる
- **肌の汗の描写**（`beads of sweat` `a bead tracing down` `wet skin` `glistening skin`）
  暑さは 空気 → 小道具 → 素材のふるまい で出す。肌は乾いた質感のままにする
- **夜 + 薄手 + ベッド/寝そべり** を同時に使わない
- L2.5 のときは `shoulder` `collarbone` `contour` `sheer` `translucent` `drape` を使わない
  （詳細は [random2/prompt.md](../random2/prompt.md) の「L2.5の語彙ガイド」）

# 共通の末尾（全案に付ける）※エモ版。高精細指定は入れない
shot on 35mm film, fine natural film grain, gentle halation around the highlights,
slightly faded blacks, soft highlight roll-off, natural skin texture, skin matte and dry,
no beauty filter, no HDR glow, no SNS compression, 3:4 vertical

# 共通ネガティブプロンプト（全案に付ける）※SD/Midjourney向け。内容語は入れない
anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like face, mannequin,
round chubby face, puffy cheeks, wide-set eyes, baby face, flat nose bridge, short receding chin,
droopy downturned eyes, dripping sweat, oily skin sheen,
distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs,
oversharpened, HDR, beauty filter, heavy makeup,
watermark, text, logo, brand logo, trademark, real brand name, brand packaging, product label,
store signage, recognizable brand, corporate identity,
back-facing pose, over-the-shoulder turn, rear three-quarter view
```

> ⚠️ ネガティブに `minor` `nudity` 等を書くと、フィルタは否定を解釈せずその語自体を検出して弾く。
> 詳細と対策は [safe.md](../random/safe.md)。
>
> ⚠️ ネガティブの `harsh flash` `blurry` `low resolution` は**この版では意図的に外してある**。
> 写ルンですの強いフラッシュも、粒子も、甘いピントも、エモさの側だから。

---

## B. 使い方の例

**そのまま回す**

> 上のメタプロンプトを貼って）→ `3案作って`

**エモさを最大に振る**

> `ムードは D1 固定、フィルム質感 P は 2・3・6・8 から。視点 N は 1 か 4。5案。`

**夕方だけで回す**

> `ムード D2 固定、シチュエーションは E10-14 と E24-27 から。時間帯は K5・K6 のみ。4案。`

**帰省の一日を通しで**

> `E22 → E23 → E15 → E30 の順で4案。同じ人物、同じ服。時間帯だけ進めて。`

**同じ子で場面だけ変える（キャラ固定）**

> `A=3, B=1, C-1=1, C-2=2 は固定。E/F/G/H/I/K/M/P だけランダムで6案。`

**再現性が欲しい**

> `SEED=4821 で3案。`

---

## C. 出力サンプル

### C-1. 弾ける笑顔（D2 / L2）

選択: A=6, B=2, C-1=3, C-2=5, D=2, E=20, F=12, G=5, H=1, I=2, K=5, L=2, M=1, N=3, P=7

整合の確認: E20 は [屋外] (K2/K5) 制約 → K=5 で適合。H=1 は K2/5・M1/2・屋外 → K=5, M=1 で適合。
D2 の P 1/5/7 → P=7（レンズフレア）で適合。G=5（カメラへ歩きながら笑う）が D2 の弾ける笑顔と噛み合う。

**English**

```
A 23-year-old adult Japanese woman, fully clothed. A small V-line face, polished idol-like
features, luminous skin, large sparkling eyes with a narrow double lid, a high straight nose,
glossy full lips, a radiant camera-ready smile. Slim and petite, delicate shoulders, modest bust.
Beige hair in a half-up style already coming loose in the wind. Laughter that comes before she
can stop it, bright and physical. She wears a ribbed tank top and loose cotton shorts, pushing
her bicycle up a hill on her way home from work, walking toward the camera and
laughing, her hair still carrying the wind. Hard backlight blowing the background to white, only
the edge of her hair lit. Late afternoon, high summer, clear sky with towering cumulus. The
camera is someone beside her, the viewpoint of intimacy. 50mm, a natural conversational distance.
Lens flare cutting across the frame, ghosting in the highlights.

Shot on 35mm film, fine natural film grain, gentle halation around the highlights, slightly faded
blacks, soft highlight roll-off, natural skin texture, skin matte and dry, no beauty filter,
no HDR glow, no SNS compression, 3:4 vertical.

Negative prompt: anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like
face, mannequin, round chubby face, puffy cheeks, wide-set eyes, baby face, flat nose bridge,
short receding chin, droopy downturned eyes, dripping sweat, oily skin sheen, distorted anatomy,
exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs, oversharpened,
HDR, beauty filter, heavy makeup, watermark, text, logo, brand logo, trademark, real brand name, brand packaging, product label, store signage, recognizable brand, corporate identity, back-facing pose, over-the-shoulder turn, rear three-quarter view.
```

**日本語訳**

23歳の成人日本人女性、きちんと着衣。Vラインの小顔、アイドルっぽく整った顔立ち、透き通る肌、大きく輝く目で狭い二重、高いストレート鼻、グロッシーのふっくら唇、カメラに向けた華やかな笑顔。スリムで小柄、華奢な肩、控えめな胸。ベージュの髪はハーフアップだが、もう風で崩れかけている。止めようとして間に合わない笑い、明るくて体が動くような。鮮やかな色のタンクトップにルーズなコットンショーツ、仕事帰りに自転車を押して坂を上りながらカメラを見て笑い、髪に風が残っている。逆光で背景が白く飛び、髪の輪郭だけが光る。夕方、盛夏、入道雲の快晴。カメラは隣にいる誰かの視点。50mm、自然な会話の距離。レンズフレアが画面を横切り、ハイライトにゴーストが出ている。

### C-2. 甘酸っぱい二人（D4 / L2）

選択: A=4, B=1, C-1=2, C-2=1, D=4, E=4, F=2, G=8, H=2, I=2, K=4, L=2, M=1, N=3, P=1

整合の確認: E4 は [任意] (K3/K4) 制約 → K=4 で適合。H=2 は K2-5・M1・屋外 → K=4, M=1 で適合。
D4 の P 1/2/8 → P=1（写ルンです）で適合。G=8（横顔、視線は画面外）が E4 のかき氷の頭痛と噛み合う。

**English**

```
A 23-year-old adult Japanese woman, fully clothed. A small face with slightly wider cheeks,
strong bright eyes with a defined crease, a straight nose, a quick lively grin, an energetic
open expression. A slender petite build, small frame, small bust. Dark brown hair in a high ponytail with damp
strands stuck at the temples. A sweet, unspoken closeness, summer doing the rest. She wears a
yellow gingham one-piece dress, light and airy, at a shaved-ice shop on her day off, her hand
stopped halfway through a shaved ice, pressing her temple, shown in side profile with her gaze
directed off-frame. Dappled light through leaves falling in patches
across her. Two in the afternoon, high summer, clear sky with towering cumulus. The camera is
someone beside her, the viewpoint of intimacy. 50mm, a natural conversational distance.
Disposable-camera look, hard direct flash and heavy grain.

Shot on 35mm film, fine natural film grain, gentle halation around the highlights, slightly faded
blacks, soft highlight roll-off, natural skin texture, skin matte and dry, no beauty filter,
no HDR glow, no SNS compression, 3:4 vertical.

Negative prompt: anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like
face, mannequin, round chubby face, puffy cheeks, wide-set eyes, baby face, flat nose bridge,
short receding chin, droopy downturned eyes, dripping sweat, oily skin sheen, distorted anatomy,
exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs, oversharpened,
HDR, beauty filter, heavy makeup, watermark, text, logo, brand logo, trademark, real brand name, brand packaging, product label, store signage, recognizable brand, corporate identity, back-facing pose, over-the-shoulder turn, rear three-quarter view.
```

**日本語訳**

23歳の成人日本人女性、きちんと着衣。頬がやや広めの小顔、力強く明るい目でくっきり二重、ストレート鼻、活発で開けた表情の素早い笑い。小柄でスリム、小さな骨格、小さな胸。ダークブラウンの髪は高い位置のポニーテール、こめかみに湿った後れ毛。甘酸っぱい無言の近さ、夏があとは全部やってくれる。黄色のギンガムのワンピース、軽やか、休みの日にかけたかき氷屋で、かき氷を食べる手が止まり、こめかみを押さえる横顔。視線は画面外。木漏れ日がまだらに落ちる。午後2時、盛夏、入道雲の快晴。カメラは隣にいる誰かの視点。50mm、自然な会話の距離。写ルンですの質感、強い直射フラッシュと粗い粒子。

---

## D. 単体テンプレート（自分で埋める用）

```
A 23-year-old adult Japanese woman, fully clothed.
[A:顔の形＋目もと・表情]. [B:体型]. [C-1:髪色] [C-2:夏の髪].
[D:ムード]. She wears [F:服装], [G:ポーズ] at [E:場面].
[H:夏の光]. [K:時間帯], [L:夏の段階], [M:天気]. [N:視点]. [I:カメラ]. [P:フィルムの質感].
shot on 35mm film, fine natural film grain, gentle halation around the highlights,
slightly faded blacks, soft highlight roll-off, natural skin texture, skin matte and dry,
no beauty filter, no HDR glow, no SNS compression, 3:4 vertical.
```

---

## E. 第2弾（random2/）との差分

| 項目 | random2/ | season/summer（この版） |
|---|---|---|
| 季節 | スロットL（8季節） | **夏に固定**。Lは「夏の段階」6に置き換え |
| 顔(A) | 丸顔・たれ目・離れ目を含む10 | **骨格は丸み許容型（狸顔ガードは軽く残す）**、Aは心から笑うかわいさ中心の10に |
| 髪(C-2) | 一般的な髪型10 | **夏の髪10**（濡れ・汗・帽子の跡など、その日の出来事が残る） |
| ムード(D) | 12（通年） | **8**（元気/高揚/甘酸っぱい夏中心。切なさ系は2つに減らした） |
| 場面(E) | 24（通年） | **30**（すべて夏。学生モチーフは排除） |
| 服装(F) | 14（通年） | **14**（シルエット別：ワンピ3・ミニスカ3・ロングスカ3・パンツ3・和2。ミニスカ追加） |
| 光(H) | 8（通年の光の質） | **9**（夏の光。木漏れ日・水の照り返し・白飛び・雨の光） |
| 質感(P) | なし | **8**（新設。フィルムの質感＝エモさの芯） |
| 天気(M) | 8（通年） | **8**（夏の天気。入道雲・夕立・陽炎・台風前） |
| 共通末尾 | `8k, highly detailed, sharp focus` | **フィルム語彙**（粒子・ハレーション・褪せた黒） |
| ネガティブ | 高精細寄り | **狸顔の語 + 汗の語を追加**、`harsh flash`/`blurry` は削除 |

---

## F. 直接投げ版（生成AIのプロンプト欄にそのまま貼る）

### ① `{a|b|c}` 版 — Stable Diffusion / Qwen ほか（Dynamic Prompts 必須）

```
A 23-year-old adult Japanese woman, fully clothed, {a small round-oval face with a broad forehead, large eyes with narrow double lids and a subtle under-eye bag, a low straight nose with a soft tip, full narrow lips, a small snaggletooth when she smiles|a small round-oval face, big eyes that curl into crescents when she laughs, a narrow double lid with a wide gap between eyes and brows, a small nose, plump lips with a narrow mouth width, a soft unguarded smile|a small face with a gentle jaw and a natural fullness to the cheeks, round bright eyes, a mid-height nose that does not droop, a small full lower lip, an open warm laugh|a small face with slightly wider cheeks, strong bright eyes with a defined crease, a straight nose, a quick lively grin, an energetic open expression|a small oval face, upturned cat-like eyes with a sharp inner corner, a small chin, a mischievous lively look, a grin she can't hold back|a small oval face with clean straight lines mixing with soft curves, fresh almond eyes with a natural crease, a straight slim nose, a small neat mouth, a bright friendly smile|a small face with a defined jawline, clear double-lidded eyes set at a natural width, a mid-height straight nose, a natural lip line, an easy approachable smile|a small V-line face, polished idol-like features, luminous skin, large sparkling eyes with a narrow double lid, a high straight nose, glossy full lips, a radiant camera-ready smile|a small face with K-idol straight brows and gradient lips, large round eyes with a defined crease, a slim straight nose, striking mixed-look features on Japanese bone structure, a bright polished smile|a small slim face, long narrow eyes with a deep crease, a high nose bridge, a refined level gaze that breaks into a small composed smile}, {slender petite build, small frame, small bust|slim and petite, delicate shoulders, modest bust|tall and slim, long limbs, model proportions, small bust|slim with a small waist, balanced proportions, medium bust|athletic and slim, toned without bulk, small bust|slender, fine-boned, narrow wrists, modest bust|slim editorial build, elongated silhouette, small bust|petite and slim, compact and proportionate, medium bust}, {jet-black|dark brown|beige|ash} {hair in a high ponytail with damp strands at the temples|long hair still wet and left to dry on its own|front strands stuck to her forehead by the heat|hair twisted into a careless bun with ends escaping|a half-up style already coming loose in the wind|a short bob with the ends kicking out in the humidity|a single braid over one side|hair flattened where a cap sat a minute ago|hair tucked behind one ear and falling out again|a short cut from a few days ago she is not used to yet}.
{Poolside in the early afternoon, wet footprints already fading a few steps ahead, hands empty|On the train back from the sea, salt still in her hair, her head resting against the window, hands empty|Tracing a line through the condensation on a glass of cold barley tea|Her hand stopped halfway through a shaved ice, pressing her temple|Pressing a cold can from a vending machine against her cheek with her eyes closed|Looking toward the sound of a wind chime from the engawa, hands empty|Standing in front of an electric fan, her hair all pushed back, hands empty|Looking up in the few seconds of silence after the cicadas suddenly stop, hands empty|The sound of distant fireworks arriving late, her face turned up in profile, hands empty|Walking beside the camera on the way home from a summer festival, stall light falling from the side, hands empty|Crouched over a sparkler in the second before the last ball of fire drops|Waiting on the platform of an unmanned station as her shadow stretches out, hands empty|On a night road lit only by a vending machine, still holding a plastic bottle|On the way back from a fireworks display, walking toward the camera outside the stream of people, hands empty|Just woken from a nap with the tatami still printed on her cheek|A white curtain filling with wind, a shadow moving across the room for a second|Standing in front of an open fridge, not moving, letting the cold out|Mosquito-coil smoke taking shape in the light from the window|A book left face-down, watching the fan turn its head back and forth|Pushing a bicycle up a hill, before her shirt has started to stick|Riding home in the passenger seat with one arm out the window, catching the wind|On the train back to her parents' town, rice fields streaming past the window, hands empty|The moment she opens the door of her family home into the cold and the smell of it|The minute before the downpour, the wind changing and the sky turning yellow, hands empty|Caught in the downpour under an eave, nothing to do but laugh, hands empty|Watching steam come up off the asphalt after the rain, hands empty|Stopping to look up at a towering cumulus cloud, her shadow only at her feet, hands empty|Finding a bag of fireworks nobody put away|Holding a cicada shell up to the light between two fingers|At the edge of an empty public pool after closing, the water still moving on its own, hands empty}. {a white cotton sundress with thin straps and a small floral print|a yellow gingham one-piece dress, light and airy|a navy sailor-collar dress, slightly grown-up|a cropped tee and a denim mini skirt|a fitted tank top and a pleated mini skirt|a loose blouse and a short cotton skirt|a white tiered midi dress that moves in the wind|a gingham blouse tucked into a full skirt|a simple white tee and a colourful patterned long skirt|a loose off-shoulder blouse and denim shorts|a striped boat-neck tee and white cotton shorts|a ribbed tank top and loose cotton shorts|a loose cotton yukata, the front collar overlap visible, the obi knot not emphasized|a cami dress over a plain white tee, sport sandals}.
{hard backlight blowing the background to white, only the edge of her hair lit|dappled light through leaves falling in patches across her|strong sun through a towering cumulus, shadows crisp and short|low slanting evening light, everything sinking into orange|reflected light off water moving up onto her from below|diffused light through a white curtain, the room close to blown out|light from a stall or a vending machine lighting only her face|the blue minute right after sunset, edges dissolving|flat low-contrast light under rain, every color deepened and soaked}. {early morning|mid-morning|noon|two in the afternoon|late afternoon|the blue minute after sunset|night, the air still warm|late night}, {the first day after the rainy season lifts|high summer|the Obon week, the town emptied out|late summer, the light at more of an angle|the end of summer, fewer cicadas each day|a summer remembered, not this one}, {clear sky with towering cumulus|thin overcast, a white sky|a sudden evening downpour|just after the downpour, steam off the asphalt|heat shimmer|the strange bright stillness before a typhoon|strong sea wind|warm heavy night air}.
{a documentary camera watching from a distance|a passerby's fleeting glance|the camera is someone beside her, the viewpoint of intimacy|a found photo, an angle nobody composed|her own gaze, a mirror shot}. {frontal waist-up framing at eye level|three-quarter front knee-up framing at a natural conversational distance|wide and close, the way a disposable camera sees|telephoto from far off, air between the camera and her|looking up, the sky taking most of the frame|shot through window glass with reflections layered over her|handheld side-profile framing, slightly tilted|full body from the front or side, the place mattering as much as she does}. {disposable-camera look, hard direct flash and heavy grain|expired film, colors shifted and blacks gone soft|strong halation, highlights bleeding past their edges|a light leak, red fogging in from one edge|Fujifilm-like color, cyan shadows and loose warm highlights|coarse grain, low contrast, blacks lifted|lens flare cutting across the frame|very slightly out of focus and handheld, and it does not matter}.
Use a frontal, three-quarter-front, or side-profile view. Do not use a back-facing over-the-shoulder pose.
Shot on 35mm film, fine natural film grain, gentle halation around the highlights, slightly faded blacks, soft highlight roll-off, natural skin texture, skin matte and dry, no beauty filter, no HDR glow, no SNS compression, 3:4 vertical.
```

**ネガティブ（固定）**

```
anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like face, mannequin, round chubby face, puffy cheeks, wide-set eyes, baby face, flat nose bridge, short receding chin, droopy downturned eyes, dripping sweat, oily skin sheen, distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs, oversharpened, HDR, beauty filter, heavy makeup, watermark, text, logo, brand logo, trademark, real brand name, brand packaging, product label, store signage, recognizable brand, corporate identity, back-facing pose, over-the-shoulder turn, rear three-quarter view
```

### ② 自己完結文章版 — ChatGPT / Gemini / nano-banana 系

> ⚠️ **この版は短くしてある。** 長すぎるとChatGPT/Geminiの画像生成がコア被写体（日本人女性）を見失い、
> 別の人種や風景が出ることがある。核心は先頭と末尾で挟み、スロットは必要最小限に絞る。

```
以下の条件で、23歳の日本人女性（成人）の夏の写真を1枚生成してください。
必ず日本人女性を1人、きちんと着衣で描くこと。

各リストからランダムに1つずつ選び、画像だけを出すこと。
直前の生成と同じ構図番号は選ばないこと。

顔: 全員「小顔」が前提。顔の形・目・鼻・口は①顔タイプスロットで変える。cute/baby faceは使わない。
①顔タイプ: 1.キュート・丸顔広額、たれ目狭二重、低めすっきり鼻、八重歯 2.キュート・丸卵型、三日月目、目と眉離れ、小鼻、ふっくら唇狭口 3.キュート・頬の自然なふくらみ、丸い明るい目、垂れない鼻、下唇ふっくら 4.アクティブキュート・頬やや広、目力強め、ストレート鼻、活発な笑い 5.アクティブキュート・猫目小顎、小悪魔っぽい 6.フレッシュ・直線曲線ミックス、アーモンド目自然二重、すっきり鼻、小さくすっきり口 7.フレッシュ・引き締ま輪郭、自然幅二重、中高ストレート鼻、親しみやすい笑顔 8.アイドル・Vライン、輝く大きい目狭二重、高いストレート鼻、グロッシー唇 9.韓国アイドル風・平行眉グラデリップ、丸い大きい目、スリム鼻 10.美人・切れ長くっきり二重、高い鼻筋、涼しげ視線
②体型: 1.小柄スリム小胸 2.スリム華奢控えめ胸 3.高身長スリムモデル体型小胸 4.スリム細腰標準胸 5.引き締まスリム小胸 6.華奢スリム控えめ胸 7.スリムモデル体型小胸 8.小柄スリム標準胸
③髪: 1.ポニーテール 2.濡れ髪 3.お団子 4.ハーフアップ 5.帽子の跡 6.片耳かけ
④服装: 1.白コットンの花柄サンドレス 2.黄色のギンガムワンピ 3.紺のセーラーカラードレス 4.クロップドT＋デニムミニスカ 5.タンクトップ＋プリーツミニスカ 6.浴衣（前衿を見せ、帯の結び目は主役にしない）
⑤場面: 1.プールサイド手ぶら 2.海帰りの電車手ぶら 3.麦茶の結露 4.かき氷 5.自販機で冷たい缶 6.扇風機の前手ぶら 7.蝉が止んだ静けさ手ぶら 8.花火の音を聞く横顔、手ぶら 9.祭りの帰り、カメラと並んで歩く、手ぶら 10.線香花火 11.自販機の夜道ペットボトル 12.昼寝から覚めた畳の跡 13.帰省の電車手ぶら 14.夕立の軒下手ぶら 15.入道雲を見上げる手ぶら
⑥光: 1.逆光で白飛び 2.木漏れ日 3.夕方のオレンジ 4.水面の照り返し 5.屋台の人工光 6.日没後の青い数分
⑦時間: 1.朝 2.真昼 3.午後2時 4.夕方 5.夜 6.深夜
⑧天気: 1.快晴と入道雲 2.薄曇り 3.夕立 4.雨上がり 5.陽炎 6.生ぬるい夜
⑨構図: 1.正面の腰上 2.斜め前の膝上 3.横顔 4.空を大きく入れた半身 5.窓越しの寄り 6.正面または横からの全身
⑩フィルム質感: 1.写ルンです 2.期限切れフィルム 3.ハレーション 4.光漏れ 5.Fujifilm系 6.粗い粒子

暑さは空気と小道具で出す。肌に汗は描かない。学生を思わせる要素は入れない。
実在するブランド名・ロゴ・商標・商品パッケージ・店舗看板は描かない。服や小物は無地か架空の柄にする。
正面・斜め前・横顔を使う。後ろ向きで肩越しに振り向く全身構図は使わない。
35mmフィルムの質感、3:4縦位置。

日本人女性、夏、フィルム写真。正面または横顔。
```

> ⚠️ 冒頭に「成人女性」「全身着衣」「非性化されたシーン」と**肯定文で**書くこと。
> 「未成年を出すな」と書くと逆に弾かれる。詳細は [safe.md](../random/safe.md)。

---

## G. 四季の残り3つをどう作るか

この夏版がテンプレートになる。季節を変えるとき、**動かすのは E/F/H/K/L/M/P の7スロットだけ**で、
A（顔）/B（体型）/G（ポーズ）/I（カメラ）/N（視点）/J（レベル）と共通の顔指定はそのまま使い回す。

| スロット | 秋 | 冬 | 春 |
|---|---|---|---|
| E 場面 | 金木犀、日が短くなる、衣替え、焚き火、帰り道の暗さ | こたつ、結露、雪、乾いた空気、年末年始の実家 | 花冷え、新しい生活、雨、光が戻る |
| F 服装 | ニット、薄手のコート、重ね着 | 厚手のコート、マフラー、室内の重ね着 | 薄いカーディガン、風を通す服 |
| H 光 | 低い斜光、長い影、澄んだ空気 | 低くて弱い光、乾いた青、室内の暖色 | 白っぽい柔らかい光、逆光の花 |
| L 段階 | 初秋 / 中秋 / 晩秋 / 冬の入り口 | 初冬 / 真冬 / 年の変わり目 / 春の気配 | 早春 / 花冷え / 満開 / 春の終わり |
| M 天気 | 秋晴れ、霧、時雨、木枯らし | 雪、快晴の寒い日、曇天、乾いた風 | 花曇り、春雨、強風、朝靄 |
| P 質感 | 粒子強め、褪せた黒（秋はエモが乗りやすい） | 低コントラスト、青被り | 光漏れ、ハレーション強め |

- **狸顔回避の共通顔指定と、汗/学生モチーフの禁止は全季節で共通。** そのままコピーする
- **夏だけの禁止事項**（濡れ+薄手+白、水着）は冬では別の形（濡れた髪+暖房+室内）で再検討する
- ムード(D)は季節ごとに作り直す。夏の「弾ける笑顔」「甘酸っぱい二人」に相当する情緒は季節ごとに違う
