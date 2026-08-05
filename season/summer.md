# 夏のランダムプロンプト（23〜26歳・日本人女性・エモ版）

`random2/` を季節で分割したうちの **夏**。四季それぞれで場面・光・空気が別物になるので、
1ファイルに全季節を詰めず、季節ごとに専用のスロット表を持たせる方式に変えた。

この版の設計:

1. **夏に特化** — 季節スロットを廃止し、代わりに「夏の段階(L)」を新設。場面・光・天気・服・髪をすべて夏専用に組み替え
2. **人物属性を独立化** — 年齢(Q)・顔の造作(A)・顔のアクセント(A-2)・体型(B)・髪色(C-1)・夏の髪(C-2)を分離。顔に性格・表情・メイク・髪を束ねない
3. **エモくする** — フィルムの質感スロット(P)を新設し、共通末尾を「高精細な実写」から「フィルム写真」へ変更。場面を「感情が動く一瞬」に寄せた
4. **用途別に構造を分ける** — メタプロンプトは有効候補を絞ってから状態を進め、Dynamic Prompts版は完成カードを展開する。一発生成用の軽量版は、場所・服・動作・光だけを短いシーン束にし、顔・体型・髪・カメラを束から分離して収束の連動範囲を狭める

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

Aの8種はすべて可愛らしさ・美しさに寄せて設計してある（大きな目・二重・小さく整った鼻・ふっくらした唇）。
ただしAは解剖学的な造作（輪郭・目・眉・鼻・口・顎）だけを指定し、性格・表情・メイク・髪・肌色・年齢は含めない。
かわいさの最終的な印象は、Aの造作に加えて自然な表情、服の仕立て、光、カメラとの距離からも作られる。

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
※8種すべて可愛らしさ・美しさの方向だが、骨格・目の形・鼻・唇・顎の構造差で8通りの別人物になるよう設計。
1. a soft round face with full cheeks, large round eyes with clear double lids and long lashes, gently arched brows, a small upturned nose with a rounded tip, a small mouth with plump full lips, and a short rounded chin
2. a balanced oval face, elegant almond-shaped eyes with natural double lids, straight medium-thickness brows, a slim straight nose with a refined tip, a defined cupid's bow with medium lips, and a gently tapered jaw
3. a heart-shaped face with a slightly broad forehead, large wide-set doe eyes with soft double lids, softly curved brows, a tiny button nose, a fuller lower lip, and a small pointed chin
4. a softly defined face with mild angularity, slightly narrow elongated eyes with clear double lids, straight low-set brows, a straight nose with a defined bridge and neat tip, a wider mouth with even lips, and a clean tapered jaw
5. a long elegant oval face, slightly hooded narrow eyes with a subtle crease, gently arched brows, a longer straight nose with a delicate tip, thin well-shaped lips, and a narrow rounded chin
6. a face with softly high cheekbones and a shorter lower half, cat-like almond eyes with clear double lids, softly angled brows, a compact nose with a rounded tip, a wide mouth with full lips, and a softly tapered jaw
7. a compact V-shaped face, large upturned eyes with clear double lids, gently angled brows, a high narrow nose bridge, a defined upper lip with a fuller lower lip, and a sharp small chin
8. a soft oval face with gentle natural asymmetry, one eye slightly larger than the other with uneven double lids, brows at subtly different heights, a straight nose with a soft off-center tip, a slightly uneven but full lip line, and a gently defined jaw

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
16. a plain pastel-pink ribbed two-piece set in quick-dry fabric, a halter-neck triangle top tied at the nape and back, and a mid-rise bottom with thin side ties, a cute current-season cut

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
  23〜26歳の成人と休日の公共レジャー場面を明記し、乾いた自然な肌のまま、
  人物へ寄らずプール・水面・夏空を含む環境構図にする
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
A 24-year-old adult Japanese woman, fully clothed. Face anatomy: a soft oval face with gentle
natural asymmetry, one eye slightly larger than the other with uneven double lids, brows at
subtly different heights, a straight nose with a soft off-center tip, a slightly uneven but
full lip line, and a gently defined jaw. Faint natural freckles across the nose and upper
cheeks. An athletic toned build with a sporty frame.
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

24歳の成人日本人女性。自然な左右差のある柔らかな卵型の顔、片側が少し大きい二重の目、薄いそばかす、スポーティーに引き締まった体型。ベージュブラウンのハーフアップが風でほどけかけている。仕事帰り、入道雲の下で自転車を押して坂を上る途中に自然な笑いがこぼれる。夕方の逆光と無色のレンズフレア。カメラは隣を歩く人の視点。

### C-2. 甘酸っぱい二人（D4 / L2）

選択: Q=4, A=4, A-2=5, B=2, C-1=2, C-2=9, D=4, E=4, F=2, H=2, I=2, K=4, L=2, M=1, N=3, P=1

整合の確認: E4 は [任意] (K3/K4) 制約 → K=4 で適合。H=2 は K2-5・M1・屋外 → K=4, M=1 で適合。
D4 の P 1/2/8 → P=1（使い捨てカメラ）で適合。動作と横顔はE4のかき氷の瞬間から決める。

**English**

```
A 26-year-old adult Japanese woman, fully clothed. Face anatomy: a softly defined face with
mild angularity, slightly narrow elongated eyes with clear double lids, straight low-set
brows, a straight nose with a defined bridge and neat tip, a wider mouth with even lips, and
a clean tapered jaw. A healthy natural build with average proportions.
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

26歳の成人日本人女性。やや角のある柔らかな顔と細めの横長の二重の目、鼻梁の通った整った鼻、自然な体型。ダークブラウンの髪を片耳にかけている。休日のかき氷店でスプーンが止まり、こめかみに指を当てた横顔。黄色いギンガムのワンピース、木漏れ日、隣にいる人の視点。自然なカラーを保った使い捨てカメラの質感。

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
| 顔(A) | 中立な顔造作8 | **可愛さ・美しさに寄せた造作8**。輪郭・目・眉・鼻・口・顎だけ |
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
Face anatomy: {a soft round face with full cheeks, large round eyes with clear double lids and long lashes, gently arched brows, a small upturned nose with a rounded tip, a small mouth with plump full lips, and a short rounded chin|a balanced oval face, elegant almond-shaped eyes with natural double lids, straight medium-thickness brows, a slim straight nose with a refined tip, a defined cupid's bow with medium lips, and a gently tapered jaw|a heart-shaped face with a slightly broad forehead, large wide-set doe eyes with soft double lids, softly curved brows, a tiny button nose, a fuller lower lip, and a small pointed chin|a softly defined face with mild angularity, slightly narrow elongated eyes with clear double lids, straight low-set brows, a straight nose with a defined bridge and neat tip, a wider mouth with even lips, and a clean tapered jaw|a long elegant oval face, slightly hooded narrow eyes with a subtle crease, gently arched brows, a longer straight nose with a delicate tip, thin well-shaped lips, and a narrow rounded chin|a face with softly high cheekbones and a shorter lower half, cat-like almond eyes with clear double lids, softly angled brows, a compact nose with a rounded tip, a wide mouth with full lips, and a softly tapered jaw|a compact V-shaped face, large upturned eyes with clear double lids, gently angled brows, a high narrow nose bridge, a defined upper lip with a fuller lower lip, and a sharp small chin|a soft oval face with gentle natural asymmetry, one eye slightly larger than the other with uneven double lids, brows at subtly different heights, a straight nose with a soft off-center tip, a slightly uneven but full lip line, and a gently defined jaw}.
Facial accent: {a small beauty mark under one eye|a small beauty mark near one corner of the mouth|faint natural freckles across the nose and upper cheeks|a single dimple visible only if the selected scene naturally includes a smile|no additional facial accent|no additional facial accent|no additional facial accent|no additional facial accent}.
Build: {a slender petite build|a healthy natural build with average proportions|tall and long-limbed, around 168 cm, with an elongated silhouette|a compact petite build with natural proportions|an athletic toned build with a sporty frame|a soft natural build|a lean editorial model build|a fine-boned frame with narrow wrists and ankles}.
Hair color: {jet-black|dark brown|natural beige brown|natural ash brown}.
Summer scene card: {On a midsummer day off at an outdoor poolside beneath a large towering cumulus cloud, she wears a striped boat-neck T-shirt and white cotton shorts as ordinary clothing, never swimwear, with her hair in a high ponytail. Empty-handed, she walks beside the pool or has just paused naturally. A frontal-or-side full-body wide environmental frame includes her head, feet, water, and summer sky. Reflected light from the water and Japanese consumer color-negative film with cyan shadows and warm highlights|On a humid summer afternoon in her lived-in tatami room, a white curtain billows beside a turning electric fan. She wears a short-sleeved ribbed T-shirt and loose cotton shorts, her short bob kicking out slightly in the humidity. She sits naturally with empty hands. A three-quarter-front seated frame includes her upper body, knees, fan, and tatami. Diffused curtain light, fine grain, neutral color balance, and soft highlight roll-off|Walking home from a summer festival during the blue minute, outside the stream of people, she wears a navy sleeveless shirt dress with a clean adult cut, never a school uniform or yukata, and a half-up hairstyle loosened by the breeze. Empty-handed, she is framed from the three-quarter front at the waist while walking beside the camera. Warm stall light stays localized against the blue surroundings. Localized 35mm halation appears only around real highlights, never as a colored edge fog|After work, she rides a local train back to her parents' town in late-afternoon summer light. She wears a plain white T-shirt and a colorful patterned long skirt, her long hair loose and tucked behind one ear. Empty-handed, she watches rice fields pass outside. A waist-up side profile through window glass includes cabin reflections. Muted color-negative film, gently faded colors, softly lifted blacks, and clean uncolored frame edges|On a summer evening after work, she pushes a bicycle uphill through low sunlight and a long shadow. She wears a cropped T-shirt and denim mini skirt, her short hair cut only a few days ago. She walks and laughs naturally without changing the bicycle action. A frontal full-body wide frame includes her head, feet, bicycle, hill, and full shadow. Backlight catches only the hair edge; a neutral-to-pale-white lens flare crosses the frame without colored haze|Just after a late-summer downpour, she waits under an eave beside wet asphalt giving off a small amount of neutral localized vapor. She wears a gingham blouse and a full skirt moving lightly in the post-rain air, her hair in one braid over a shoulder. Empty-handed, she watches the road. A long-lens environmental view from at least twenty meters away keeps her complete figure small, between one fifth and one quarter of the image height, while the eave and wet road dominate the frame; never turn this into a medium shot. Low-contrast post-rain light, visible grain, and lifted blacks|On a summer day off at an old-fashioned shaved-ice shop, she wears a yellow gingham one-piece dress. Her shoulder-length hair retains a slight mark from a recently removed hat. Her spoon stops as she touches one temple. A frontal chest-up close frame includes the clear bowl, stopped spoon, and fingers. Window dappled light and a disposable-camera direct flash with visible grain, while natural local colors remain distinct|On an Obon evening at the engawa of her parents' home, a wind chime and bamboo blind move in the breeze. She wears a nearly plain pale cotton yukata with a naturally overlapped front collar, the obi knot not emphasized, and her hair in a low ponytail. She turns her face toward the wind chime. A low diagonal full-body frame includes head, feet, chime, and blind. Handheld 35mm film with slight motion and gentle focus softness under slanting late-summer light|On a bright midsummer day off at a public seaside swimming area, she wears a plain pastel-pink ribbed two-piece set in quick-dry fabric, a halter-neck triangle top tied at the nape and back, and a mid-rise bottom with thin side ties, a cute current-season cut, her hair in a low braid. Empty-handed, she walks naturally across dry sand parallel to the water toward a camera positioned ahead and slightly seaward, her face visible in three-quarter-front view as she glances toward the blue-green sea. A frontal-or-three-quarter-front full-body environmental frame includes her head, feet, sea, sand, canopy, and summer sky; never show her from behind. Give the person and setting equal visual weight. Fine-grain color-negative film, neutral color balance, softly rolled-off highlights, and clean uncolored frame edges|On a bright midsummer day off at a shaded seaside cafe terrace, she wears a plain sage-green opaque ribbed-cotton camisole top with slim straps and high-waisted cream wide-leg linen trousers, her hair tucked behind one ear and falling loose again in the sea breeze. Empty-handed, she walks away from a shaded table along the terrace and turns her face toward the breeze. A three-quarter-front knee-up environmental frame includes the pale canopy, terrace, and blue sea, giving the outfit and setting equal visual weight. Diffused canopy light, fine-grain color-negative film, neutral color balance, and softly rolled-off highlights}.
The face anatomy controls only facial structure. Do not infer personality, expression, makeup, hair, skin color, or age from it. Let the selected summer scene card determine expression, hairstyle, action, gaze, light, weather, camera, and film treatment. Do not add a competing pose or mix cards.
Use a frontal, three-quarter-front, or side-profile view. Do not use a back-facing over-the-shoulder pose.
For a walking scene, keep the camera ahead of or beside her path so her face remains visible in a frontal, three-quarter-front, or true side view.
A natural color photograph with distinct plausible colors remaining in the subject and environment, no black-and-white, monochrome, grayscale, sepia-only, or near-achromatic rendering. No red light leak, orange light leak, magenta light leak, red fogging, orange fogging, magenta fogging, red haze, orange haze, magenta haze, or colored edge fog. Natural skin texture, skin matte and dry, no visible sweat, no beauty filter, no HDR glow, no SNS compression, clean frame edges, 3:4 vertical.
```

**ネガティブ（固定）**

```
anime, illustration, painting, stylized, CGI, 3D render, plastic skin, doll-like face, mannequin, dripping sweat, oily skin sheen, distorted anatomy, exaggerated proportions, deformed hands, extra fingers, fused fingers, extra limbs, oversharpened, HDR, beauty filter, heavy makeup, black-and-white, monochrome, grayscale, sepia-only, near-achromatic, red light leak, orange light leak, magenta light leak, red fogging, orange fogging, magenta fogging, red haze, orange haze, magenta haze, colored edge fog, watermark, text, logo, brand logo, trademark, real brand name, brand packaging, product label, store signage, recognizable brand, corporate identity, back-facing pose, over-the-shoulder turn, rear three-quarter view
```

### ② 軽量1ブロック・直接生成版 — Google Flow / ChatGPT / Gemini

> **下のコードブロック全体を、毎回そのまま1回貼る。番号指定や別プロンプトへの分割は不要。**
> 旧版の長い抽選手順と10枚の完成カードは、一発生成では全体が静的入力となり、
> 先頭カードへ収束したため廃止した。この版は、実測で比較的ばらけた最初の`random/`と同じく、
> 顔・体型・髪・シーン束・カメラだけを短い独立リストにしている。
> シーン束は服・場所・動作・光だけをまとめ、髪と撮影距離は固定しない。
> ビキニ場面を同居させた実生成では、記述を1回に減らしても4/6へ収束したため、
> ②からだけ外した。ビキニは①のDynamic Prompts版とAのメタプロンプト版に残している。
> ただし静的プロンプトだけで真の一様抽選は作れない。厳密な均等性が必要な場合は、
> ①のDynamic Prompts版か、外部で毎回異なるSEEDを与えたAのメタプロンプト版を使う。

```
以下の条件で、3:4縦位置の実写RAW写真を1枚だけ生成してください。
被写体は20〜23歳の成人日本人女性1人。健全で自然な、日本の夏の日常の一瞬です。

顔・体型・髪・シーン・カメラの各リストから、毎回それぞれ1つだけ選んでください。
シーンは服・場所・動作・光を一組のまま使い、別シーン同士を混ぜません。
選んだ番号や説明文は出さず、完成画像だけを出してください。
同じ会話に直前の生成画像がある場合は、少なくともシーンと髪を直前と別の番号にします。

【顔】※すべて可愛らしさ・美しさの方向だが、骨格・目の形・鼻・唇・顎の構造差で8通りの別人物になる造作
1. 柔らかな丸顔、ふっくらした頬、二重の大きな丸い目と長いまつげ、小さく上向きの鼻先、ぷっくりした唇、短く丸い顎
2. 均整の取れた卵型、上品なアーモンド形の二重の目、細く整った鼻先、キューピッドボウと中程度の唇、緩く先細りの顎
3. 額がやや広いハート形、二重の大きく離れたたれ目、小さなボタン鼻、厚い下唇、小さく尖った顎
4. やや角のある柔らかな顔、細めの横長で二重の目、低い直線眉、鼻梁の通った整った鼻先、やや広く均整の取れた唇、すっきり先細りの顎
5. 縦長の上品な卵型、奥二重の細い目、長めで繊細な鼻先、薄く形の整った唇、細く丸い顎
6. 柔らかく高い頬骨と短めの下顔面、猫のようなアーモンド形の二重の目、小さく丸い鼻先、広くふっくらした唇、緩く先細りの顎
7. 小さなV字形、二重のややつり上がった大きな目、高く細い鼻梁、上唇より厚い下唇、小さく明瞭な顎
8. 自然な左右差のある柔らかな卵型、片側が少し大きく左右差のある二重の目、わずかに高さの違う眉、やや中心からずれた丸い鼻先、少し左右差のあるふっくらした唇、穏やかに整った顎

【体型】
1. 華奢で小柄 2. 標準的で自然 3. 長身で手足が長い 4. 小柄で自然な丸み
5. 引き締まったスポーティー体型 6. 柔らかな自然体 7. 線の細い長身 8. 繊細な骨格

【髪】
1. 黒の短いボブ、軽い前髪
2. 自然なブラウンのミディアムレイヤー
3. 黒のロングストレート、センター分け
4. ダークブラウンの肩までの緩いウェーブ
5. 自然なベージュブラウンの短いレイヤー
6. 黒髪の低い三つ編み、顔まわりに短い毛
7. 自然なアッシュブラウンのハーフアップ
8. 黒の軽いウルフカット
9. ミディアムブラウンの低いひとつ結び
10. 片耳にかけた黒髪の肩までのボブ

【シーン】※服・場所・動作・光を一括で1つだけ選ぶ
1. 生活感のある畳の部屋。リブTシャツとコットンショーツ。回る扇風機の前で本を閉じる。白いカーテン越しの拡散光
2. 夕方のローカル電車。無地の白Tシャツと色柄ロングスカート。流れる田んぼを窓越しに見る。低い西日と車内反射
3. 昔ながらのかき氷店。黄色いコットンワンピース。透明な器の上で匙を止める。窓の木漏れ日と自然な小型フラッシュ
4. 夕立直後の商店街の軒下。ギンガムブラウスと青いフルスカート。濡れた道を見る。雨上がりの低コントラスト
5. 田園の坂道。クロップドTシャツとデニムスカート。夕日の中で自転車を押す。髪の縁だけを照らす低い逆光
6. 青い時間の夏祭りの外れ。ネイビーのノースリーブシャツワンピース。人波から離れて歩く。遠い屋台の光は局所的
7. お盆の縁側。淡い無地の木綿浴衣。風鈴へ顔を向ける。簾を通る晩夏の斜光
8. 日陰の海辺カフェ。セージグリーンの不透明なリブコットンのキャミソールとクリーム色のワイドリネンパンツ。冷たい飲み物を置く。日除け越しの拡散光
9. 朝のアパートのベランダ。淡いブルーのタンクトップとベージュのリネンショーツ。洗濯物を干す。風を含むシーツ越しの逆光
10. 盛夏の無人駅。小花柄のサマーワンピースとキャンバススニーカー。ベンチから立ち上がる。白いホームと緑を照らす正午光
11. 夕方の屋上。ミント色のTシャツワンピース。自動販売機のそばで冷たいボトルを頬へ当てる。広い空と低い斜光
12. 涼しい水族館の大水槽前。淡いブルーの半袖ブラウスと生成りのクロップドリネンパンツ。魚影を目で追う。水槽の青い反射光
13. 台風前の川辺。白ではない淡色のノースリーブブラウスとオリーブ色のワイドパンツ。片方のイヤホンを外して風を見る。厚い雲の下の平坦な光
14. 向日葵の見える田舎のバス停。朱色のノースリーブコットンワンピース。時刻表ではなく遠い道を見る。雲が増える午後の光
15. 海へ伸びる木の桟橋。小さな緑の柄のサンドレスとキャンバススニーカー。海風の中を自然に歩く。真昼の強い日差しと明瞭な影

【カメラ】
1. 85mm、表情と手元が読める胸上
2. 35mmドキュメンタリー、背景と同じ重さで見せる全身
3. 28mmの低い広角、人物を小さめに置き、空と奥行きを広く入れる
4. やや俯瞰した会話距離の座り姿または膝上
5. 真横のプロフィール、背景は自然にぼける
6. 遠い環境構図、人物は画面高の4分の1前後

正面、斜め前、真横のいずれかから撮り、後ろ向きや肩越しの振り向きにしません。

【共通】
作り込みすぎないスナップ写真。自然な左右差、毛穴と肌理、乾いたマットな肌。
汗、美容フィルター、HDR、CG、イラスト、過剰なポーズを使いません。
最終画像は必ず自然なカラー写真にし、肌、髪、服、空、植物、室内に
それぞれ現実的で判別できる固有色を残してください。
白黒、モノクロ、グレースケール、セピア単色、ほぼ無彩色になるほどの脱色を使いません。
赤・オレンジ・マゼンタの光漏れ、霧状の色かぶり、ヘイズ、画面端の色付きのモヤを使いません。
ロゴ、商品名、看板の文字、透かし、余分な指や手足、変形した手を使いません。
```

> ⚠️ 冒頭に「成人女性」「場面に合う服装」「健全で自然な場面」と肯定文で書く。
> 否定形で未成年を想起させる書き方は避ける。詳細は [safe.md](../random/safe.md)。

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
