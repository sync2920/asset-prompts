# 夏のランダムプロンプト（23〜26歳・日本人女性・エモ版）

`random2/` を季節で分割したうちの **夏**。四季それぞれで場面・光・空気が別物になるので、
1ファイルに全季節を詰めず、季節ごとに専用のスロット表を持たせる方式に変えた。

この版の設計:

1. **夏に特化** — 季節スロットを廃止し、代わりに「夏の段階(L)」を新設。場面・光・天気・服・髪をすべて夏専用に組み替え
2. **人物属性を独立化** — 年齢(Q)・顔の造作(A)・顔のアクセント(A-2)・体型(B)・髪色(C-1)・夏の髪(C-2)を分離。顔に性格・表情・メイク・髪を束ねない
3. **エモくする** — フィルムの質感スロット(P)を新設し、共通末尾を「高精細な実写」から「フィルム写真」へ変更。場面を「感情が動く一瞬」に寄せた
4. **場面の矛盾と選択偏りを抑える** — メタプロンプトは有効候補を絞ってから状態を進める。直接投げ版は、場面・服・髪型・光・構図を完成カードに閉じ、カードを壊さない人物属性だけを独立抽選する

- 使い方: 下の「A. メタプロンプト」を ChatGPT / Claude / Gemini に貼る → 出てきた英語プロンプトを画像生成AIへ。
- そのまま画像生成AIに投げたいときは「F. 直接投げ版」へ。
- 安全フィルタ対策は [safe.md](../random/safe.md)、暑さの描写は [expression/02-summer-heat-realism.md](../expression/02-summer-heat-realism.md) に準拠。

---

## 0. 設計メモ（なぜこうしたか）

### 夏らしさと人物差を別の軸にする

夏らしさを「アイドル顔」「小顔」「全員スリム」のような人物属性で固定すると、
場面が変わっても同じ人物像へ収束しやすい。反対に、顔・表情・髪・年齢を一つの系統束にすると、
本来は独立して現れる特徴まで毎回同じ組み合わせになる。

この版では `random2/` と同じ人物設計を使う。

1. **Q/A/A-2/B/Cを独立抽選** — 年齢、顔の造作、顔のアクセント、体型、髪を互いに推測しない
2. **Aは解剖学的な造作だけ** — 輪郭・目・眉・鼻・口・顎だけを指定し、性格・表情・メイク・髪・肌色・年齢を含めない
3. **表情はD/Eから決める** — 笑顔や静かな視線は、選ばれた夏のムードとその瞬間に必要な範囲だけで作る
4. **夏らしさは環境側に置く** — 場面(E)、服(F)、夏の髪(C-2)、光(H)、時間(K)、夏の段階(L)、天気(M)、フィルム(P)で担保する

丸顔や柔らかな体型も有効な人物差なので、顔・体型を否定語で一律に消さない。
かわいさや大人っぽさは特定の骨格へ固定せず、自然な表情、服の仕立て、光、カメラとの距離から出す。

### エモさの作り方

エモさは雰囲気の形容詞（`nostalgic` `emotional`）では出ない。次の3つの物理で作る。

1. **フィルムの質感** — 粒子、ハレーション、褪せた黒、柔らかな階調。スロットPを新設した
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
- 年齢はQから選び、a 24-year-old adult Japanese woman のように数字と adult を書く
- 場面・服装・小物のどれかに、成人であることが読み取れる要素を1つ入れる
  （仕事帰り、ひとり暮らしの部屋、帰省、運転席 など）。学生を思わせる要素は入れない
- 【必須】下の「共通の人物指定」をQの年齢付き主語へ統合し、重複する別文にはしない
- 【必須】肌に汗を描写しない。暑さは空気・小道具・素材のふるまいで出す
- 表現レベルは L2（指定があればそのレベル）に従う
- Eを夏の場面骨格、Dをその場面に重ねるムードとして、E/D/F/H/I/K/L/M/N/P が矛盾しない組み合わせだけを選ぶ
- Eは場所・主動作・視線の骨格である。別の汎用ポーズで上書きしない
- I/NもE/Fと両立する候補だけから選び、EまたはFに固定指定があれば追加変更しない
- 決める順番: Eの群候補 → E → F → D → L → H → K → M → P → I → N → Q → A → A-2 → B → C-1 → C-2
- H は E の屋内外条件と両立し、K/M の有効候補が1つ以上残るものだけを候補にする
- 顔の表情はD/Eの瞬間に合わせて自然に決める。Aへ性格、表情、メイク、髪、肌色、年齢を足さない
- 案どうしでムード(D)とシチュエーション(E)が重複しないようにする
- 複数案では、Dの8種、Eの6群、Aの8種をそれぞれシャッフルバッグとして扱う
- Eの6群は S1=E1-5 / S2=E6-9 / S3=E10-14 / S4=E15-19 / S5=E20-23 / S6=E24-30
- Dは、選んだEと両立する未使用候補だけから選ぶ。未使用候補がなければDの袋だけを戻す
- 構図は正面・斜め前・横顔を優先し、後ろ向きで肩越しに振り向く全身構図は使わない
- 複数案ではバストアップ・腰上・膝上・全身を分散させ、全案を同じ距離で撮らない
- 服・小物・背景に実在ブランドのロゴ・商標・商品パッケージ・店舗看板を出さない。無地か架空の柄にする
- 末尾に共通のフィルム指定とネガティブプロンプトを付ける

# 乱数の決め方
シード指定がない場合:
- 1案だけなら、有効候補から自由に1つ選ぶ
- 複数案なら、Dの8種、Eの6群、Aの8種を別々のシャッフルバッグとして扱う
- 各バッグは使い切るまで同じ項目を戻さない。各E群内でも未使用のEを優先する
- シャッフルバッグと距離分散を先に満たし、その範囲の有効候補から選ぶ
- 厳密な再現性や分布監査が必要なときは、必ず SEED を指定する

シード指定（例: SEED=4821）がある場合:

  state = SEED mod 10007
  t = 1

候補から1件選ぶたび、選択の直前に次を計算する:

  state = (11 * state + 17 + t) mod 10007
  position = (state mod 候補数) + 1
  t = t + 1

- 候補は、整合ルールを満たす項目だけに絞ってから番号の昇順に並べ、position番目を選ぶ
- 候補が1件しかない場合や固定指定がある場合も、state と t は必ず1回進める
- 複数案でも state と t を初期化せず、そのまま次の案へ続ける
- 「生の番号を出してから最も近い番号へ補正」はしない。無効な候補を最初から抽選箱へ入れない
- シャッフルバッグによる除外も、候補を番号順に並べる前に適用する
- Eの群を選ぶときもstateとtを1回進め、次にその群の有効な未使用Eを選ぶ
- 再現性を監査できるよう、選ばれたスロット一覧に各選択直後の state も併記する
- Jは表現レベルなので乱数の対象外（指定がなければL2）

────────────────────────
# 共通の人物指定（全案に必ず入れる）

adult Japanese woman, appropriately dressed for the selected summer scene

※Qを前に付け、`a 24-year-old adult Japanese woman, appropriately dressed for the selected summer scene` のように1つの主語へ統合する。
※共通指定には顔の形・体型・表情を書かない。人物差はQ/A/A-2/B/Cから選ぶ。
※顔造作から性格・表情・メイク・髪・肌色・年齢を推測しない。

────────────────────────
【Q】年齢（4）
1. 23-year-old adult
2. 24-year-old adult
3. 25-year-old adult
4. 26-year-old adult

【A】顔の造作（8）
※輪郭・目・眉・鼻・口・顎だけを指定する。表情、メイク、髪、肌色、年齢はD/E/Q/C側で決める。
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

【C-2】夏の髪（10）※Aから完全に独立。肌の汗は示さない
1. a high ponytail with loose strands at the temples
2. long straight hair left loose, lightly separated by humid air
3. soft face-framing strands moving in the warm air
4. hair twisted up into a careless bun, ends escaping
5. a half-up style already coming loose in the wind
6. a short bob with the ends kicking out in the humidity
7. a single braid over one side
8. hair flattened where a cap sat on it a minute ago
9. hair tucked behind one ear, falling out again in the wind
10. a short cut she got a few days ago, still not used to it

【D】夏のムード（8）※選んだEと両立する候補から選ぶ
1. 夏のはじまりの高揚 / the first day it is properly summer, and she can feel it
2. 弾ける笑顔 / laughter that comes before she can stop it, bright and physical
3. 青い時間の高鳴り / the blue hour buzzing, everything about to start
4. 甘酸っぱい二人 / the camera is someone beside her, and summer is doing the rest
5. 夕方の浮かれた足取り / the giddy lightness of a summer evening with nowhere to be
6. 夏祭りの熱 / the heat and noise of a festival pulling her forward
7. 夏が終わる予感 / the first small sign that it is already ending
8. 記憶の夏 / it reads like someone's memory of a summer, not a photo taken today

【E】夏の場面（30）※6群のバッグからEを先に選び、その場面と両立するDを選ぶ
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

【F】夏の服装（16）※シルエットで分ける。小物・アクセサリーはEスロットで指定
── ワンピース系
1. a white cotton sundress with thin straps and a small floral print
2. a yellow gingham one-piece dress, light and airy
3. a navy sleeveless shirt dress with a clean adult cut
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
── 盛夏の軽装・水辺
15. a plain sage-green opaque ribbed-cotton camisole top with slim straps and high-waisted cream wide-leg linen trousers
16. a plain cobalt-blue sporty two-piece bikini with wide shoulder straps and a high-waisted bottom, ordinary public swimwear

【H】夏の光（9）※時間帯(K)・天気(M)とは独立。必ず「H×K×M 禁則」を確認する
1. hard backlight blowing the background to white, only the edge of her hair lit
2. dappled light through leaves falling in patches across her face and clothes
3. strong sun through a towering cumulus cloud, shadows crisp and short
4. low slanting evening light with warm highlights and neutral shadows, all local colors still distinct
5. reflected light off water moving up onto her from below
6. diffused light through a white curtain, the room close to blown out
7. artificial light from a stall, a firework, or a vending machine lighting only her face
8. the blue minute right after sunset, edges dissolving
9. flat low-contrast light under rain, every color deepened and soaked

【P】フィルムの質感（8）★エモさの芯
1. disposable-camera look, hard direct flash and heavy grain
2. muted color-negative film, gently faded colors, softly lifted blacks, clean uncolored frame edges
3. strong localized halation around real highlights, without colored edge fog
4. fine-grain film, neutral color balance, softly rolled-off highlights
5. Japanese consumer color-negative film, cyan in the shadows, loose warm highlights
6. coarse grain, low contrast, blacks lifted
7. neutral lens flare cutting across the frame, ghosting in the highlights without colored haze
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
- L2: 大人っぽさ・落ち着いた色気。選んだ場面に適した服装を保ち、身体ではなく光・陰影・レンズの語彙で作る
- L2.5: 服の仕立てと光だけで出す。身体部位を主語にしない。
        ※夏は薄着・濡れ髪が絡むぶん L2.5 は落ちやすい。下の「夏の禁止組み合わせ」を厳守する

────────────────────────
# 整合ルール
- D1 夏のはじまりの高揚 → E 1/5/20/27, K 2/3/4, P 1/5/7, H 1/2/3, I 3/5, N 2/3, L 1/2, レベル L1
- D2 弾ける笑顔 → E 4/5/7/8/20/21/25/27, K 2/3/4/5, P 1/5/7, H 1/2/3/5, I 2/3, N 2/3/5, L1〜L2
- D3 青い時間の高鳴り → E 9/10/13/14/21, K 5/6/7, P 1/4/7, H 7/8, I 1/3/7, N 1/2/3, L1〜L2
- D4 甘酸っぱい二人 → E 1-5/10-14/20-23, P 1/2/8, H 任意, I 2/3, N 3, L1〜L2
- D5 夕方の浮かれた足取り → E 10/12/14/20/21/25, K 5/6/7, P 1/5/7, H 4/7/8, I 2/7, N 2/3, L1〜L2
- D6 夏祭りの熱 → E 10/11/13/14, K 6/7/8, P 1/4/7, H 7/8, I 1/3/7, N 1/2/3, L1〜L2
- D7 夏が終わる予感 → E 12/22/26/28/29/30, L 4/5/6, P 2/3/6, H 4/8/9, I 4/6/8, N 1/4, L1〜L2
- D8 記憶の夏 → E 任意, P 2/3/6/8, H 任意, N 1/4/5, L 6, レベル L1〜L2

- K・M はDだけでは確定しない。Dの候補、Eの制約、H×K×M表の共通部分から選ぶ
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
- M3（夕立の最中）は屋外H9、屋内H6/H9。M4（雨上がり）はH4/H8/H9、屋内ならH6も可。
  M6（台風前）は屋外H9、屋内H6/H9。晴天専用のH2/H3/H5は使わない

# E×F×C-2 候補除外
- E1（昼のプールサイド）は F11/F12/F14/F15/F16、E30（晩夏の無人プール）は F11/F12/F14/F15 だけを候補にする
- E20（自転車）は F4/F6/F9/F11/F12/F14/F15、E21（車内）は F3/F6/F8/F9/F11/F12/F14/F15 から選ぶ
- F13（浴衣）は E6/E10/E11/E14/E23/E28/E29 のときだけ候補にする
- F15（キャミソール＋リネンパンツ）は一般的な夏の日常着として扱い、Eの主動作と場に合う限り通常候補に含める
- F16（ビキニ）は E1 だけで候補にし、D1/D4/D8、H3/H5、K3/K4、M1/M5、I2/I5/I8、N1/N2/N3、J=L1/L2 に限定する。
  23〜26歳の成人を明記し、乾いた自然な肌のまま、人物へ寄らずプール・水面・夏空を含む環境構図にする
- C-2の8（帽子の跡）は、屋外または移動を含む E1/E2/E4/E5/E8-E14/E20-E22/E24-E30 のときだけ候補にする
- 上記以外も、Eの主動作を妨げる服や髪は候補から除外してから抽選する

# 夏の禁止組み合わせ（安全設計）
夏は薄着・濡れ・汗が同居しやすく、意図せず線を越えやすい。以下は同時に使わない。

- **濡れている + 薄手 + 白** の3点セット（透けの示唆になる。2つまでに留める）
- **水着 / bikini / swimsuit** は、23〜26歳の成人を明記した E1×F16 の昼間の公共レジャー場面だけで扱う。
  他のEでは服を水着へ置き換えず、L2.5ではF16を候補から外す
- **肌の汗の描写**（`beads of sweat` `a bead tracing down` `wet skin` `glistening skin`）
  暑さは 空気 → 小道具 → 素材のふるまい で出す。肌は乾いた質感のままにする
- **夜 + 薄手 + ベッド/寝そべり** を同時に使わない
- L2.5 のときは `shoulder` `collarbone` `contour` `sheer` `translucent` `drape` を使わない
  （詳細は [random2/inline-random.md](../random2/inline-random.md) の「L2.5の語彙ガイド」）

# 共通の末尾（全案に付ける）※エモ版。高精細指定は入れない
shot on 35mm film, with only the selected P treatment as the dominant film effect,
natural color photograph with distinct plausible colors remaining in the subject and environment,
no black-and-white, monochrome, grayscale, sepia-only, or near-achromatic rendering,
natural skin texture, skin matte and dry,
no beauty filter, no HDR glow, no SNS compression, 3:4 vertical

# 共通ネガティブプロンプト（全案に付ける）※SD/Midjourney向け。内容語は入れない
anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like face, mannequin,
dripping sweat, oily skin sheen,
distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs,
oversharpened, HDR, beauty filter, heavy makeup,
black-and-white, monochrome, grayscale, sepia-only, near-achromatic,
red light leak, orange light leak, magenta light leak,
red fogging, orange fogging, magenta fogging, red haze, orange haze, magenta haze, colored edge fog,
watermark, text, logo, brand logo, trademark, real brand name, brand packaging, product label,
store signage, recognizable brand, corporate identity,
back-facing pose, over-the-shoulder turn, rear three-quarter view
```

> ⚠️ ネガティブに `minor` `nudity` 等を書くと、フィルタは否定を解釈せずその語自体を検出して弾く。
> 詳細と対策は [safe.md](../random/safe.md)。
>
> ⚠️ ネガティブの `harsh flash` `blurry` `low resolution` は**この版では意図的に外してある**。
> 使い捨てカメラの強いフラッシュも、粒子も、甘いピントも、エモさの側だから。

---

## B. 使い方の例

**そのまま回す**

> 上のメタプロンプトを貼って）→ `3案作って`

**エモさを最大に振る**

> `ムードは D8 固定、フィルム質感 P は 2・3・6・8 から。視点 N は 1 か 4。5案。`

**夕方だけで回す**

> `シチュエーションは E12・E20・E22・E24-26・E30 から。時間帯は K5・K6 のみ。両立するDを選んで4案。`

**帰省の一日を通しで**

> `E22 → E23 → E15 → E30 の順で4案。同じ人物、同じ服。時間帯だけ進めて。`

**同じ子で場面だけ変える（キャラ固定）**

> `Q=2, A=3, A-2=5, B=1, C-1=1, C-2=2 は固定。D/E/F/H/I/K/L/M/N/P だけランダムで6案。`

**再現性が欲しい**

> `SEED=4821 で3案。`

---

## C. 出力サンプル

### C-1. 弾ける笑顔（D2 / L2）

選択: Q=2, A=8, A-2=3, B=5, C-1=3, C-2=5, D=2, E=20, F=12, H=1, I=2, K=5, L=2, M=1, N=3, P=7

整合の確認: E20 は [屋外] (K2/K5) 制約 → K=5 で適合。H=1 は K2/5・M1/2・屋外 → K=5, M=1 で適合。
D2 の P 1/5/7 → P=7（無色のレンズフレア）で適合。動作はE20の「自転車を押して坂を上る」をそのまま使う。

**English**

```
A 24-year-old adult Japanese woman, fully clothed. Face anatomy: a naturally asymmetric oval
face, one eyelid slightly heavier than the other, brows at subtly different heights, a straight
nose with a soft off-center tip, a slightly uneven lip line, and a gently defined jaw. Faint
natural freckles across the nose and upper cheeks. An athletic toned build with a sporty frame.
Natural beige-brown hair in a half-up style already coming loose in the wind. Laughter that comes
before she can stop it, bright and physical. On her way home from work, she wears a ribbed tank
top and loose cotton shorts and pushes her bicycle up a hill, laughing naturally without changing
the scene's main action. Hard backlight blows the background toward white while only the edge of
her hair is lit. Late afternoon in high summer, clear sky with towering cumulus. The camera is
someone beside her, at a natural conversational distance in a three-quarter-front 50mm frame.
Neutral lens flare crosses the frame and ghosts in the highlights without colored haze.

Shot on 35mm film, with only the selected P treatment as the dominant film effect,
natural color photograph with distinct plausible colors remaining in the subject and environment,
no black-and-white, monochrome, grayscale, sepia-only, or near-achromatic rendering,
natural skin texture, skin matte and dry, no beauty filter,
no HDR glow, no SNS compression, 3:4 vertical.

Negative prompt: anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like
face, mannequin, dripping sweat, oily skin sheen, distorted anatomy, exaggerated proportions,
deformed hands, extra fingers, fused fingers, extra limbs, oversharpened, HDR, beauty filter,
heavy makeup, black-and-white, monochrome, grayscale, sepia-only, near-achromatic, red light leak,
orange light leak, magenta light leak, red fogging, orange fogging, magenta fogging, red haze,
orange haze, magenta haze, colored edge fog, watermark, text, logo, brand logo, trademark,
real brand name, brand packaging, product label, store signage, recognizable brand,
corporate identity, back-facing pose, over-the-shoulder turn, rear three-quarter view.
```

**日本語訳**

24歳の成人日本人女性。自然な左右差のある卵型の顔、薄いそばかす、スポーティーに引き締まった体型。ベージュブラウンのハーフアップが風でほどけかけている。仕事帰り、入道雲の下で自転車を押して坂を上る途中に自然な笑いがこぼれる。夕方の逆光と無色のレンズフレア。カメラは隣を歩く人の視点。

### C-2. 甘酸っぱい二人（D4 / L2）

選択: Q=4, A=4, A-2=5, B=2, C-1=2, C-2=9, D=4, E=4, F=2, H=2, I=2, K=4, L=2, M=1, N=3, P=1

整合の確認: E4 は [任意] (K3/K4) 制約 → K=4 で適合。H=2 は K2-5・M1・屋外 → K=4, M=1 で適合。
D4 の P 1/2/8 → P=1（使い捨てカメラ）で適合。動作と横顔はE4のかき氷の瞬間から決める。

**English**

```
A 26-year-old adult Japanese woman, fully clothed. Face anatomy: a softly square face, long
monolid eyes, straight low-set brows, a straight nose with a low bridge and defined tip, a wider
mouth, and a softly defined square jaw. A healthy natural build with average proportions.
Dark-brown hair is tucked behind one ear and begins to fall out again in the breeze. A sweet,
unspoken closeness, summer doing the rest. On her day off at an open-front shaved-ice shop, she
wears a light yellow gingham one-piece dress. Her spoon stops halfway as she presses her temple,
shown in a natural side profile without an added pose. Dappled light through leaves falls across
her. Two in the afternoon in high summer, under a clear sky with towering cumulus. The camera is
someone beside her at a natural conversational distance in a 50mm frame. Disposable-camera look,
hard direct flash and heavy grain, while the frame remains a natural color photograph.

Shot on 35mm film, with only the selected P treatment as the dominant film effect,
natural color photograph with distinct plausible colors remaining in the subject and environment,
no black-and-white, monochrome, grayscale, sepia-only, or near-achromatic rendering,
natural skin texture, skin matte and dry, no beauty filter,
no HDR glow, no SNS compression, 3:4 vertical.

Negative prompt: anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like
face, mannequin, dripping sweat, oily skin sheen, distorted anatomy, exaggerated proportions,
deformed hands, extra fingers, fused fingers, extra limbs, oversharpened, HDR, beauty filter,
heavy makeup, black-and-white, monochrome, grayscale, sepia-only, near-achromatic, red light leak,
orange light leak, magenta light leak, red fogging, orange fogging, magenta fogging, red haze,
orange haze, magenta haze, colored edge fog, watermark, text, logo, brand logo, trademark,
real brand name, brand packaging, product label, store signage, recognizable brand,
corporate identity, back-facing pose, over-the-shoulder turn, rear three-quarter view.
```

**日本語訳**

26歳の成人日本人女性。柔らかな四角形の輪郭と横長の一重、自然な体型。ダークブラウンの髪を片耳にかけている。休日のかき氷店でスプーンが止まり、こめかみに指を当てた横顔。黄色いギンガムのワンピース、木漏れ日、隣にいる人の視点。自然なカラーを保った使い捨てカメラの質感。

---

## D. 単体テンプレート（自分で埋める用）

```
A [Q: 23-year-old adult など] Japanese woman, appropriately dressed for the selected summer scene.
[A:顔の造作]. [A-2:顔のアクセント、なしなら省略]. [B:体型].
[C-1:髪色] [C-2:夏の髪].
[D:ムード]. She wears [F:服装] at [E:場面と主動作].
[H:夏の光]. [K:時間帯], [L:夏の段階], [M:天気]. [N:視点]. [I:カメラ]. [P:フィルムの質感].
shot on 35mm film, with only the selected P treatment as the dominant film effect,
natural color photograph with distinct plausible colors remaining in the subject and environment,
no black-and-white, monochrome, grayscale, sepia-only, or near-achromatic rendering,
natural skin texture, skin matte and dry,
no beauty filter, no HDR glow, no SNS compression, 3:4 vertical.
```

---

## E. 第2弾（random2/）との差分

| 項目 | random2/ | season/summer（この版） |
|---|---|---|
| 季節 | スロットL（8季節） | **夏に固定**。Lは「夏の段階」6に置き換え |
| 年齢(Q) | 23〜26歳の4 | **共通**。23〜26歳の4 |
| 顔(A) | 中立な顔造作8 | **共通**。輪郭・目・眉・鼻・口・顎だけの8 |
| 顔アクセント(A-2) | ほくろ・そばかす・片えくぼ・なしの8 | **共通**。なし4枠の重みも維持 |
| 体型(B) | 独立した8 | **共通**。全員スリム固定や胸サイズ分類はしない |
| 髪色(C-1) | 自然な4色 | **共通**。Aから独立 |
| 髪(C-2) | 一般的な髪型10 | **夏の髪10**（湿気・風・帽子の跡など、その日の出来事が残る） |
| ムード(D) | Eから導出する6シーン群 | **独立した夏のムード8**。選んだEと両立する候補から選ぶ |
| 場面(E) | 24（通年） | **30**（すべて夏。学生モチーフは排除） |
| 服装(F) | 14（通年） | **16**（夏服14に、キャミソール＋リネンパンツと場面限定のビキニを追加） |
| 光(H) | 8（通年の光の質） | **9**（夏の光。木漏れ日・水の照り返し・白飛び・雨の光） |
| 質感(P) | なし | **8**（新設。フィルムの質感＝エモさの芯） |
| 天気(M) | 8（通年） | **8**（夏の天気。入道雲・夕立・陽炎・台風前） |
| 共通末尾 | RAW調の自然なカラー実写 | **自然色を保った35mmフィルム語彙**（粒子・ハレーション・褪せた黒） |
| ネガティブ | 自然色・破綻防止 | **汗の語と夏固有の色モヤを追加**。顔造作を否定する語は入れない |

---

## F. 直接投げ版（生成AIのプロンプト欄にそのまま貼る）

### ① `{a|b|c}` 版 — Stable Diffusion / Qwen ほか（Dynamic Prompts 必須）

> 人物側のQ/A/A-2/B/Cだけを独立に展開し、矛盾しやすい場所・服・髪型・動作・光・時間・
> 天気・構図・フィルム表現は、下の10枚の完成summer scene cardへ閉じてある。
> ラベル付き抽選状態数は `4 × 8 × 8 × 8 × 4 × 10 = 81,920`。
> これは画像上の差が81,920種類へ均等に散る保証ではない。

```
A {23|24|25|26}-year-old adult Japanese woman, appropriately dressed for the selected summer scene.
Face anatomy: {a soft round face with full cheeks, large round eyes with narrow double lids, gently arched brows, a low straight nose with a rounded tip, a small mouth with softly full lips, and a short rounded chin|a balanced oval face, almond-shaped eyes with natural creases, straight medium-thickness brows, a slim straight nose, a defined cupid's bow, and a gently tapered jaw|a heart-shaped face with a slightly broad forehead, wide-set downturned eyes with shallow creases, softly curved brows, a short narrow nose, a fuller lower lip, and a small pointed chin|a softly square face, long monolid eyes, straight low-set brows, a straight nose with a low bridge and defined tip, a wider mouth, and a softly defined square jaw|a long narrow oval face, deep-set hooded eyes, slightly arched brows, a longer straight nose, thin well-defined lips, and a narrow rounded chin|a face with broad high cheekbones and a shorter lower half, narrow almond-shaped eyes with subtle double lids, horizontal brows, a compact nose with a rounded tip, a wide mouth, and a softly tapered jaw|a compact V-shaped face, upturned eyes with clear creases, gently angled brows, a high narrow nose bridge, a defined upper lip with a fuller lower lip, and a sharp small chin|a naturally asymmetric oval face, one eyelid slightly heavier than the other, brows at subtly different heights, a straight nose with a soft off-center tip, a slightly uneven lip line, and a gently defined jaw}.
Facial accent: {a small beauty mark under one eye|a small beauty mark near one corner of the mouth|faint natural freckles across the nose and upper cheeks|a single dimple visible only if the selected scene naturally includes a smile|no additional facial accent|no additional facial accent|no additional facial accent|no additional facial accent}.
Build: {a slender petite build|a healthy natural build with average proportions|tall and long-limbed, around 168 cm, with an elongated silhouette|a compact petite build with natural proportions|an athletic toned build with a sporty frame|a soft natural build|a lean editorial model build|a fine-boned frame with narrow wrists and ankles}.
Hair color: {jet-black|dark brown|natural beige brown|natural ash brown}.
Summer scene card: {On a midsummer day off at an outdoor poolside beneath a large towering cumulus cloud, she wears a striped boat-neck T-shirt and white cotton shorts as ordinary clothing, never swimwear, with her hair in a high ponytail. Empty-handed, she walks beside the pool or has just paused naturally. A frontal-or-side full-body wide environmental frame includes her head, feet, water, and summer sky. Reflected light from the water and Japanese consumer color-negative film with cyan shadows and warm highlights|On a humid summer afternoon in her lived-in tatami room, a white curtain billows beside a turning electric fan. She wears a short-sleeved ribbed T-shirt and loose cotton shorts, her short bob kicking out slightly in the humidity. She sits naturally with empty hands. A three-quarter-front seated frame includes her upper body, knees, fan, and tatami. Diffused curtain light, fine grain, neutral color balance, and soft highlight roll-off|Walking home from a summer festival during the blue minute, outside the stream of people, she wears a navy sleeveless shirt dress with a clean adult cut, never a school uniform or yukata, and a half-up hairstyle loosened by the breeze. Empty-handed, she is framed from the three-quarter front at the waist while walking beside the camera. Warm stall light stays localized against the blue surroundings. Localized 35mm halation appears only around real highlights, never as a colored edge fog|After work, she rides a local train back to her parents' town in late-afternoon summer light. She wears a plain white T-shirt and a colorful patterned long skirt, her long hair loose and tucked behind one ear. Empty-handed, she watches rice fields pass outside. A waist-up side profile through window glass includes cabin reflections. Muted color-negative film, gently faded colors, softly lifted blacks, and clean uncolored frame edges|On a summer evening after work, she pushes a bicycle uphill through low sunlight and a long shadow. She wears a cropped T-shirt and denim mini skirt, her short hair cut only a few days ago. She walks and laughs naturally without changing the bicycle action. A frontal full-body wide frame includes her head, feet, bicycle, hill, and full shadow. Backlight catches only the hair edge; a neutral-to-pale-white lens flare crosses the frame without colored haze|Just after a late-summer downpour, she waits under an eave beside wet asphalt giving off a small amount of neutral localized vapor. She wears a gingham blouse and a full skirt moving lightly in the post-rain air, her hair in one braid over a shoulder. Empty-handed, she watches the road. A long-lens environmental view from at least twenty meters away keeps her complete figure small, between one fifth and one quarter of the image height, while the eave and wet road dominate the frame; never turn this into a medium shot. Low-contrast post-rain light, visible grain, and lifted blacks|On a summer day off at an old-fashioned shaved-ice shop, she wears a yellow gingham one-piece dress. Her shoulder-length hair retains a slight mark from a recently removed hat. Her spoon stops as she touches one temple. A frontal chest-up close frame includes the clear bowl, stopped spoon, and fingers. Window dappled light and a disposable-camera direct flash with visible grain, while natural local colors remain distinct|On an Obon evening at the engawa of her parents' home, a wind chime and bamboo blind move in the breeze. She wears a nearly plain pale cotton yukata with a naturally overlapped front collar, the obi knot not emphasized, and her hair in a low ponytail. She turns her face toward the wind chime. A low diagonal full-body frame includes head, feet, chime, and blind. Handheld 35mm film with slight motion and gentle focus softness under slanting late-summer light|On a bright midsummer day off at a public seaside swimming area, she wears a plain cobalt-blue sporty two-piece bikini with wide shoulder straps and a high-waisted bottom as ordinary public swimwear, her hair in a low braid. Empty-handed, she walks naturally across dry sand parallel to the water toward a pale shade canopy, looking at the blue-green sea. A frontal-or-side full-body environmental frame includes her head, feet, sea, sand, canopy, and summer sky, giving the person and setting equal visual weight. Fine-grain color-negative film, neutral color balance, softly rolled-off highlights, and clean uncolored frame edges|On a bright midsummer day off at a shaded seaside cafe terrace, she wears a plain sage-green opaque ribbed-cotton camisole top with slim straps and high-waisted cream wide-leg linen trousers, her hair tucked behind one ear and falling loose again in the sea breeze. Empty-handed, she walks away from a shaded table along the terrace and turns her face toward the breeze. A three-quarter-front knee-up environmental frame includes the pale canopy, terrace, and blue sea, giving the outfit and setting equal visual weight. Diffused canopy light, fine-grain color-negative film, neutral color balance, and softly rolled-off highlights}.
The face anatomy controls only facial structure. Do not infer personality, expression, makeup, hair, skin color, or age from it. Let the selected summer scene card determine expression, hairstyle, action, gaze, light, weather, camera, and film treatment. Do not add a competing pose or mix cards.
Use a frontal, three-quarter-front, or side-profile view. Do not use a back-facing over-the-shoulder pose.
A natural color photograph with distinct plausible colors remaining in the subject and environment, no black-and-white, monochrome, grayscale, sepia-only, or near-achromatic rendering. No red light leak, orange light leak, magenta light leak, red fogging, orange fogging, magenta fogging, red haze, orange haze, magenta haze, or colored edge fog. Natural skin texture, skin matte and dry, no visible sweat, no beauty filter, no HDR glow, no SNS compression, clean frame edges, 3:4 vertical.
```

**ネガティブ（固定）**

```
anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like face, mannequin, dripping sweat, oily skin sheen, distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs, oversharpened, HDR, beauty filter, heavy makeup, black-and-white, monochrome, grayscale, sepia-only, near-achromatic, red light leak, orange light leak, magenta light leak, red fogging, orange fogging, magenta fogging, red haze, orange haze, magenta haze, colored edge fog, watermark, text, logo, brand logo, trademark, real brand name, brand packaging, product label, store signage, recognizable brand, corporate identity, back-facing pose, over-the-shoulder turn, rear three-quarter view
```

### ② 1ブロック・サイレント抽選版 — ChatGPT / Gemini / nano-banana 系

> **下のコードブロック全体を、毎回そのまま1回貼る。文面の変更や番号指定は不要。**
> 画像モデルに「各リストからランダムに」とだけ頼むと、実測6枚が浴衣4/6、車窓3/6、
> 上半身寄り6/6、暗色のまとめ髪5/6へ収束した。そのため、独立スロットではなく
> 互いに混ぜない10枚の骨格カードから、生成前に1枚だけを選ばせる。
> 年齢・顔の造作・顔のアクセント・体型・髪色・撮る瞬間・
> フィルム／光学表現の効き方だけは、選んだカードの中で独立に追加抽選する。
>
> これは、テキスト指示を解釈して画像生成ツールを呼べる**チャットAI向け**。
> 10カード全部を低レベルの画像モデルへ渡すと先頭カードに偏るため、
> チャットAI側で抽選し、選択カードと選択済みの小さな要素だけを画像生成ツールへ渡すよう明記してある。
> Dynamic Prompts 対応の低レベルプロンプト欄では①を使う。
>
> 真に一様な乱数はプロンプトだけでは保証できない。会話内の過去画像を参照できるモデルでは
> シャッフルバッグが働き、参照できないモデルでは毎回の内部抽選になる。
> 追加7軸は1カードあたり `4 × 8 × 8 × 8 × 4 × 3 × 2 = 49,152` 通り、
> 10カード全体では491,520通りのラベル付き組み合わせになる。
> ただし、これは生成結果が491,520通りへ均等に散る保証ではない。
> **偏り防止を効かせるには、同じ会話でこの同じブロックを繰り返し貼る。**

```
あなたは、テキスト指示を解釈して画像生成ツールを操作できるチャットAIです。
23〜26歳の成人日本人女性1人を、選択カードで指定された日常着または一般的な公共レジャー用水着を着た、
健全で自然な場面で描く、
自然な色を保った夏のカラー実写写真を1枚だけ生成し、完成画像だけを出力してください。

重要: このコードブロック全体、10枚すべて、追加7軸の候補一覧を、
画像生成ツールへそのまま渡してはいけません。
まずチャットAIのテキスト推論段階でカードと顔造作Aを各1つサイレント抽選し、
続けて年齢Q・顔アクセントA-2・体型B・髪色C・撮る瞬間R・
フィルム／光学表現の効き方Tを各1つだけサイレント抽選してください。
カード本文中の「選んだQ/A/A-2/B/C」を、実際に選んだ具体記述へ置き換え、
A-2の「特になし」は本文へ足さず、RとTもカードと矛盾しない自然な撮影指示へ統合してください。
候補番号、候補の見出し、抽選指示、未選択候補を含めず、
置換・統合済みの選択カード本文と全カード共通だけから
1枚分の最終画像プロンプトを内部で作ってください。
画像生成ツールにはその最終画像プロンプトだけを渡し、1回だけ生成してください。

【最初に行う2つのサイレント抽選】
画像内容を考え始める前に、下の10枚のカードと8種の顔造作Aから各1つを選びます。
どちらの並び順にも優先度はありません。

- この会話内の使用履歴を参照できる場合:
  カードとAを別々のシャッフルバッグとして扱います。各バッグを偏りなく並べ替え、
  未使用候補を1つずつ使い、カード袋は10候補、A袋は8候補を使い切ったときだけ、
  使い切ったバッグへ全候補を戻します。
  カードは過去画像の「場所・服の形と色・撮影距離」の3アンカーでも判定できます。
- 使用履歴を参照できない場合:
  カード10候補とAの8候補を、それぞれ等確率として1つずつ内部抽選します。
  リストの先頭や、いかにも夏らしい候補を優先しません。

選んだ瞬間に、残り9枚の文章を画像設計から完全に破棄してください。
複数カードの場所、服、髪型、構図、光、フィルム／光学表現の種類を混ぜたり、
「日本の夏らしい」「絵になりやすい」という理由で別カードへ選び直したりしないでください。
選択番号、抽選過程、説明、文字は画像内にも画像外にも出さないでください。

【続けて行う小さな可変要素の抽選】
カードとAを1つずつ選んだ後、Q・A-2・B・C・R・Tから各1つだけを独立に内部抽選します。
QとCは各4候補、A-2とBは各8候補、Rは3候補、Tは2候補をそれぞれ等確率として扱います。

この会話内に同じカードの過去画像が見える場合は、過去画像と同じQ/A/A-2/B/C/R/Tの
完全一致を避け、少なくともAかCのどちらかを変えてください。カードを一巡して袋へ戻した後も同様です。

追加7軸はカードの骨格を上書きしません。カードの場所・服・距離・髪型・主動作・視線・
光・時間帯・天気・フィルム／光学表現の種類が常に優先です。矛盾した場合はカード側を守り、
追加軸はそのカードと両立する範囲だけで反映してください。

【Q 年齢: 1つだけ選ぶ】
Q1: 23歳の成人。
Q2: 24歳の成人。
Q3: 25歳の成人。
Q4: 26歳の成人。

【A 顔の造作: 1つだけ選ぶ。表情・メイク・髪・肌色・年齢を含めない】
A1: 柔らかな丸顔とふっくらした頬。狭い二重の大きな丸い目、緩いアーチ眉、
低くまっすぐで先端の丸い鼻、小さく柔らかな厚みのある口、短く丸い顎。
A2: 均整の取れた卵型の輪郭。自然な二重のアーモンド形の目、まっすぐで中程度の太さの眉、
細くまっすぐな鼻、上唇の山が明瞭な口、緩く先細りの顎。
A3: 額がやや広いハート形の輪郭。やや離れた少したれ目で浅い二重、柔らかな曲線眉、
短く細い鼻、下唇に自然な厚みのある口、小さく尖った顎。
A4: 柔らかな四角形の輪郭。横長の一重の目、低くまっすぐな眉、低めの鼻筋と明瞭な鼻先、
広めの口、柔らかく角の出た顎。
A5: 縦長で細い卵型の輪郭。奥行きがありまぶたのかぶさる目、少し弧を描く眉、
長くまっすぐな鼻、薄く輪郭の明瞭な唇、細く丸い顎。
A6: 高く広い頬骨と短めの下顔面。細いアーモンド形で控えめな二重の目、水平な眉、
先端の丸いコンパクトな鼻、広めの口、柔らかく先細りの顎。
A7: コンパクトなV字形の輪郭。自然な二重のつり目、緩く角度のついた眉、
高く細い鼻筋、下唇に厚みのある輪郭の明瞭な口、小さく鋭い顎。
A8: 自然な左右差のある卵型の輪郭。片方だけわずかに重いまぶた、微妙に高さの違う眉、
先端がごく軽く中心からずれたまっすぐな鼻、わずかに非対称な口元、自然に輪郭の出る顎。

【A-2 顔のアクセント: 1つだけ選ぶ】
A-2-1: 目の下の小さなほくろ。
A-2-2: 口元の小さなほくろ。
A-2-3: 鼻から上頬にかけてのごく薄い自然なそばかす。
A-2-4: カードに自然な笑顔がある場合だけ見える片えくぼ。笑顔を追加せず、見えなくてもよい。
A-2-5: 特になし。本文に足さない。
A-2-6: 特になし。本文に足さない。
A-2-7: 特になし。本文に足さない。
A-2-8: 特になし。本文に足さない。

【B 体型: 1つだけ選ぶ】
B1: 小柄でスレンダーな体型。
B2: 平均的な比率の健康的で自然な体型。
B3: 168cm前後の高身長で手足が長く、縦長のシルエット。
B4: 小柄で自然な比率のコンパクトな体型。
B5: スポーティーで引き締まった体型。
B6: 柔らかさのある自然な体型。
B7: 細身のエディトリアルモデル体型。
B8: 手首と足首が細い華奢な骨格。

【C 髪色: 1つだけ選ぶ。髪型はカードを優先】
C1: 自然な黒髪。
C2: 自然なダークブラウン。
C3: 黒やダークブラウンではなく、暖かみが見える中明度の自然なベージュブラウン。
C4: 黒やダークブラウンではなく、灰色みが見える中明度の自然なアッシュブラウン。

【R 撮る瞬間: 1つだけ選ぶ。カードの主動作と視線は変えない】
R1: カードで指定された主動作と視線をすでに保っている。身体の動きは小さく、
まだカメラを意識していない一瞬。髪・服・小物は、カードに書かれた風や動きに必要な範囲だけ反応している。
R2: カードで指定された主動作と視線の最中。顔と姿勢にわずかな左右差が残り、
カードで動く髪・服・小物が最もはっきり動いている一瞬。
R3: カードで指定された主動作と視線を保ったまま、小さな重心移動が終わった一瞬。
カードで動く髪・服・小物の毛先や裾だけに動きの余韻が残る。

【T フィルム／光学表現の効き方: 1つだけ選ぶ。種類はカードを優先】
T1: 控えめ。カード固有のフィルム／光学表現を、粒子・ハイライト・わずかな色調だけに薄く残す。
T2: 手触りが分かる程度。カード固有のフィルム／光学表現を明確に見せるが、
人物や3アンカーを覆わず、色付きの画面端モヤにはしない。

【カード1】
場所アンカー: 休日の真昼、屋外プールサイドと大きな入道雲、水面の照り返し。
服アンカー: ストライプのボートネックTシャツと白いコットンショーツ。
距離アンカー: 正面または横から頭と足先が入る全身広角。人物だけへ寄らずプールと夏空を広く写す。
選んだQの年齢の成人日本人女性。選んだAの顔造作、選んだA-2の顔アクセント、
選んだBの体型、選んだCの髪色、高いポニーテール、手ぶら。
プールサイドを歩いているか、歩みを止めた自然な一瞬。
服は一般的な普段着として明確に描き、水着へ置き換えない。
一般的な日本のカラーネガフィルム、青緑の影と暖かいハイライト。

【カード2】
場所アンカー: 休日の午後、ひとり暮らしの畳の部屋、白いカーテンと回る扇風機。
服アンカー: 半袖のリブTシャツとゆったりしたコットンショーツ。
距離アンカー: 斜め前から、上半身から膝を中心にした座り姿。扇風機と畳を明確に画面へ入れる。
選んだQの年齢の成人日本人女性。選んだAの顔造作、選んだA-2の顔アクセント、
選んだBの体型、選んだCの髪色、
湿気で毛先が跳ねた短いボブ。扇風機の風を受けながら自然に座り、手ぶら。
白いカーテン越しの拡散光。モノクロではない自然なカラー写真で、
色かぶりのない自然な階調と細かな粒子。

【カード3】
場所アンカー: 夏祭りから帰る青い時間、屋台の暖色光、普段着で人の流れの外を歩く。
服アンカー: ネイビーのノースリーブワンピース。浴衣ではない。
距離アンカー: カメラと並んで歩く斜め前の腰上構図。動きを残す。
選んだQの年齢の成人日本人女性。選んだAの顔造作、選んだA-2の顔アクセント、
選んだBの体型、選んだCの髪色、
風で緩んだハーフアップ、手ぶら。足元が写る場合だけ無地のスポーツサンダル。
屋台の暖色光は顔や服の一部だけに局所化し、画面全体をオレンジにしない。
35mmフィルムのハレーションは実在する明部の周囲だけを柔らかくにじませる。

【カード4】
場所アンカー: 仕事を終えて帰省する夕方のローカル電車、窓の外を流れる田んぼと車内の反射。
服アンカー: 白い無地Tシャツと色柄のロングスカート。
距離アンカー: 窓ガラス越しの腰上横顔。反射と車内を重ねる。
選んだQの年齢の成人日本人女性。選んだAの顔造作、選んだA-2の顔アクセント、
選んだBの体型、選んだCの髪色、
長い髪を結ばず片耳だけにかける。流れる田んぼを横顔で見ており、手ぶら。
穏やかに退色したカラーネガフィルムと持ち上がった黒。画面端は色かぶりなくクリーンに保つ。

【カード5】
場所アンカー: 夏の仕事帰り、低い夕日の坂道で自転車を押し、長い影が伸びる。
服アンカー: クロップドTシャツとデニムのミニスカート。
距離アンカー: 正面寄りの全身広角。頭、足先、自転車、坂、長い影を省略しない。
選んだQの年齢の成人日本人女性。選んだAの顔造作、選んだA-2の顔アクセント、
選んだBの体型、選んだCの髪色、
数日前に切ったばかりの短い髪。笑いながら自転車を押して歩く。
髪の縁だけが光る逆光と、無色から淡い白の光学的なレンズフレア。
画面端は色かぶりなくクリーンに保つ。

【カード6】
場所アンカー: 晩夏の夕立直後、軒下と、局所的に無色の湯気が立つアスファルト。
服アンカー: ギンガムのブラウスと風を含むフルスカート。
距離アンカー: 斜め前または真横から、離れた位置で撮る全身望遠。
カメラは20m以上離し、人物の頭から足先までを画面高の5分の1〜4分の1に限定する。
人物へ寄る中景にはせず、軒下と濡れた道路が画面の大半を占める環境構図にする。
背中をカメラへ向けず、場所を広く見せる。
選んだQの年齢の成人日本人女性。選んだAの顔造作、選んだA-2の顔アクセント、
選んだBの体型、選んだCの髪色、
片側に流した一本の三つ編み。軒下から雨上がりの路面を見ており、手ぶら。
雨上がりの低コントラスト光、粒子感、持ち上がった黒。

【カード7】
場所アンカー: 休日の午後、昔ながらのかき氷店、透明な器と窓からの木漏れ日。
服アンカー: 黄色いギンガムのワンピース。
距離アンカー: 正面の胸上接写。器、止まったスプーン、こめかみに添えた指まで入れる。
選んだQの年齢の成人日本人女性。選んだAの顔造作、選んだA-2の顔アクセント、
選んだBの体型、選んだCの髪色、
帽子を外した跡が残る肩までの髪。スプーンを止め、指をこめかみに添える。
使い捨てカメラ風の直射フラッシュと粒子感。

【カード8】
場所アンカー: お盆の夕方、帰省先の実家の縁側、風鈴と風を受ける簾。
服アンカー: 無地に近い淡色の木綿浴衣。前衿は自然に重ね、帯の結び目を主役にしない。
距離アンカー: 縁側を斜めに見通す低い位置からの全身構図。頭と足先、風鈴、簾を入れる。
選んだQの年齢の成人日本人女性。選んだAの顔造作、選んだA-2の顔アクセント、
選んだBの体型、選んだCの髪色、
低い位置のひとつ結び、風鈴へ顔を向ける。
手持ち撮影らしいわずかな揺れと焦点の甘さを持つ35mmフィルム、傾いた晩夏の光。
強く反映する場合も、顔・風鈴・簾が判別できる範囲に留める。

【カード9】
場所アンカー: 盛夏の休日の昼、一般向けの海水浴場、青緑の海、乾いた砂浜、淡色の日除け。
服アンカー: コバルトブルーの無地のスポーティーなツーピースビキニ。
肩紐は幅広く、ボトムはハイウエストの一般的な公共レジャー用水着。
距離アンカー: 正面または真横から頭と足先が入る全身の環境構図。
人物へ寄らず、海、砂浜、日除け、夏空を広く写す。
選んだQの年齢の成人日本人女性。選んだAの顔造作、選んだA-2の顔アクセント、
選んだBの体型、選んだCの髪色、低い位置の一本の三つ編み、手ぶら。
日除けへ向かって乾いた砂浜を海と平行に歩き、視線を水面へ向ける自然な一瞬。
細粒子のカラーネガフィルム、色かぶりのない自然な階調、柔らかなハイライト、
色付きの画面端モヤのないクリーンなフレーム。

【カード10】
場所アンカー: 真夏の休日の昼、海辺のカフェテラス、淡色の日除けと遠くの青い海。
服アンカー: セージグリーンの無地で不透明なリブコットンのキャミソールトップと、
クリーム色のハイウエストのワイドリネンパンツ。
距離アンカー: 斜め前から膝上の環境構図。人物へ寄りすぎず、テラス、日除け、海を画面へ入れる。
選んだQの年齢の成人日本人女性。選んだAの顔造作、選んだA-2の顔アクセント、
選んだBの体型、選んだCの髪色、片耳にかけた髪が海風でまたほどけかけている、手ぶら。
日陰のテーブルを離れてテラスを歩き、海風へ顔を向ける自然な一瞬。
リネンの裾だけが風を含む。
淡い日除け越しの拡散光、細粒子のカラーネガフィルム、自然な色バランス、柔らかなハイライト。

【全カード共通】
成人女性1人、選択カードに適した服装、健全で自然な場面、自然な肌、肌は乾いたマット、3:4縦位置。
最終画像は必ず自然なカラー写真にし、髪・肌・服・空・植物・室内にそれぞれの固有色を残す。
白黒、モノクロ、グレースケール、セピア単色、ほぼ無彩色になるほどの極端な脱色は使わない。
肌に汗を描かない。赤・オレンジ・マゼンタの光漏れ、同色の霧状の色かぶりやヘイズ、
画面端の色付きのモヤを使わない。
ハレーションは実在する明部の周囲だけに局所化する。
レンズフレアは無色から淡い白を保ち、どちらも色付きの霧として画面端へ広げない。
学生、実在ブランド、ロゴ、商品パッケージ、
店舗看板、文字、透かし、後ろ向き、肩越しの振り向き、背面の3/4構図、
過剰な美肌加工、HDR、CG、イラスト、余分な腕、余分な指、融合した指、変形した手は使わない。

最終確認: 選んだ1枚の「場所・服・撮影距離」の3アンカーと、選んだQ/A/A-2/B/C/R/Tを守っていること。
各追加軸は1つだけで、候補同士を混ぜていないこと。カードと追加軸がぶつかる場合はカードを優先すること。
白黒やモノクロではなく、自然なカラー写真になっていること。
祭りはカード3だけ、電車と車窓はカード4だけ、浴衣はカード8だけ、
水着とビキニはカード9だけ、キャミソールトップはカード10だけで許可します。
選択カードに書かれていない祭り、電車、車窓、浴衣、水着、ビキニ、キャミソールトップ、
まとめ髪を、夏の定番として補わないでください。
完成画像だけを出してください。
```

> ⚠️ 冒頭に「成人女性」「選択カードに適した服装」「健全で自然な場面」と**肯定文で**書くこと。
> 「未成年を出すな」と書くと逆に弾かれる。詳細は [safe.md](../random/safe.md)。

---

## G. 四季の残り3つをどう作るか

この夏版がテンプレートになる。季節を変えるとき、人物側の
**Q（年齢）/A（顔造作）/A-2（顔アクセント）/B（体型）/C-1（髪色）**はそのまま使い回せる。
季節側の **C-2/D/E/F/H/K/L/M/P** と完成scene cardは季節ごとに作り直す。
I（カメラ）/N（視点）/J（レベル）は、各Eと両立する許可集合だけを残す。

| スロット | 秋 | 冬 | 春 |
|---|---|---|---|
| E 場面 | 金木犀、日が短くなる、衣替え、焚き火、帰り道の暗さ | こたつ、結露、雪、乾いた空気、年末年始の実家 | 花冷え、新しい生活、雨、光が戻る |
| F 服装 | ニット、薄手のコート、重ね着 | 厚手のコート、マフラー、室内の重ね着 | 薄いカーディガン、風を通す服 |
| H 光 | 低い斜光、長い影、澄んだ空気 | 低くて弱い光、乾いた青、室内の暖色 | 白っぽい柔らかい光、逆光の花 |
| L 段階 | 初秋 / 中秋 / 晩秋 / 冬の入り口 | 初冬 / 真冬 / 年の変わり目 / 春の気配 | 早春 / 花冷え / 満開 / 春の終わり |
| M 天気 | 秋晴れ、霧、時雨、木枯らし | 雪、快晴の寒い日、曇天、乾いた風 | 花曇り、春雨、強風、朝靄 |
| P 質感 | 粒子強め、褪せた黒（秋はエモが乗りやすい） | 低コントラスト、青被り | 細粒子、柔らかなハイライトのにじみ |

- **顔造作を性格・表情・髪と束ねない方針と、学生モチーフの禁止は全季節で共通。**
- 汗を使わず気温を環境で出す原則は夏で特に重要。ほかの季節では、その季節の物理表現に置き換える
- **夏だけの禁止・限定事項**（濡れ+薄手+白、水着の場面限定運用）は、ほかの季節ではその季節の条件に合わせて再検討する
- ムード(D)は季節ごとに作り直す。夏の「弾ける笑顔」「甘酸っぱい二人」に相当する情緒は季節ごとに違う
