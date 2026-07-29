# 画像生成アイデア集

`04/prompt.md` の運用（人物の年齢、性別表現、顔、髪、肌、体型、身体のライン、身長感、プロポーションなどは参照画像だけから推定・保持し、ポーズ・服・背景・アスペクト比をテキストで指定する方式）を前提としたバリエーション案。

## 収録ファイル

- [50-variations.md](50-variations.md) — 初期50案の原案アーカイブ。現在の生成には、衣装と場面を再設計した次の完成版を推奨。
- [001-050-full-prompts.md](001-050-full-prompts.md) — 日常、夜の街、小さな特別な日を中心に、上品な色気・生活の余韻・クールさ・幻想を織り交ぜた完成英語プロンプト50案。
- [181-engawa-watermelon.md](181-engawa-watermelon.md) — 単発1案（181）。夏の縁側でスイカ、着古したキャミソールの緩みを軸にしたドキュメンタリー調。設計メモ付き。
- [182-196-office-casual-cool.md](182-196-office-casual-cool.md) — オフィスカジュアル／かっこいい系15案（182〜196）。移動と通過、執務空間の余白、退勤と切り替えの3群。露出ではなく仕立て・光・重心で強さを出す設計。
- [100-viral-prompts.md](100-viral-prompts.md) — 新規100案（051〜150）。上品な色気25案、だらしない色気20案、四季と小さな特別な日20案、非日常・幻想20案、かっこいい堅実服15案。
- [197-199-morning-post.md](197-199-morning-post.md) — 朝投稿用3案（197〜199）。朝の斜光を主役に、キッチンの湯気／朝ラン後の自販機／旅先ホテルのカーテン開けの3場面。
- [200-morning-garden-mist.md](200-morning-garden-mist.md) — 朝投稿用1案（200）。裏庭で植物に水、ホースの霧が低い朝日を浴びて光の粒子の柱になる一瞬。霧（空気）と薄い布の二重の透過で輪郭を描く設計。
- [206-355-daily-thrill-fusion.md](206-355-daily-thrill-fusion.md) — 新規150案（206〜355）。不意のドキッ20案、生活の手元20案、気配のツーショット15案、天気の変わり目15案、一点だけの異変（静かなマジックリアリズム）20案、現実半分・空想半分15案、街の時間外20案、音・温度・匂いの可視化10案、手仕事と趣味15案。
- [205-rooftop-juice-short-shadow.md](205-rooftop-juice-short-shadow.md) — お昼過ぎ投稿用1案（205）。真夏の屋上で缶ジュース、頂光に近い午後一の太陽が足元に短い影を落とす構図。風でオーバーシャツが膨らみ布が体から離れる一瞬を、媒質変奏シリーズの「風による離反」として設計。
- [../expression/01-sheer-skin-intimacy.md](../expression/01-sheer-skin-intimacy.md) — 透け感や露出を素材・光・輪郭で間接的に描写する書き方。薄手の衣装や親密な場面の案を組むときの表現手法として参照。
- [../expression/02-summer-heat-realism.md](../expression/02-summer-heat-realism.md) — 夏の暑さと実写感（プロカメラマン撮影）を間接的に描写する書き方。暑さは空気・小道具・素材で出し肌の汗は控えめに、実写感はカメラブロックとディテール要求で出す手法。夏の案や実写感を強めたいときの表現手法として参照。

## 身体特徴の保持（全プロンプト共通の必須方針）

- **顔・胸・お尻を含む体型は、参照画像から必ず忠実に保持する。** 顔立ちはもちろん、胸と腰まわりの形とボリューム、身体のライン、身長感、プロポーションを参照どおりに再現することを全プロンプトの前提にする。
- 英文には `all physical characteristics including chest and hip shape and fullness` と、バスト・ヒップの自然なボリュームが服のフィットとドレープを通して正確に伝わる旨（`reproduce the natural volume and silhouette of the bust and hips as seen in the reference`）を含める。
- 若返り・加齢・美化・痩身化・誇張など、参照からの体型改変は一切行わない（`without age-shifting, beautifying, exaggerating, or reshaping`）。
- **胸が実際より小さく出るときの主因はポーズと生地。** 腕・鞄・フォルダが胸の前を横切ると潰れ、箱型で張りのある生地（crisp / boxy / oversized）は布が浮いてボリュームを消す。シルエットを見せる案では ①胸の前を空ける（nothing held in front of the chest）②体に沿う生地（soft, fluid weave that follows the body）③布の挙動の明示（curves over the bust, drapes from its outermost point, gentle tension lines）の3点を指定する。意図的に緩い服で隠す案は例外として明記する。
- **胸の位置は高く指定する。** 生成では胸が実際より下（ウエスト寄り）に描かれやすい。「支えられて高い位置にある」ことを基準点つきで英文に入れる: `the bust sits high and supported on the ribcage, as if wearing a well-fitted bra: its fullest point is level with the mid-upper arm, roughly at armpit height, with only a short distance between the collarbones and the top of the curve — never sagging low toward the waist`。脇の高さ・二の腕の中ほどなど、体の相対位置を基準にすると効きやすい。

## 衣装とシチュエーションの基準

- **一着につき見せ場は一箇所:** 背中、片肩、ウエスト、脚などの焦点を一つに絞り、残りは長い丈や端正な仕立てで引き算する。
- **透け感には必ず構造をつくる:** レース、シフォン、オーガンジーなどには不透明な裏地、ボディスーツ、インナーショーツなどを明記し、直接的な透け方にしない。
- **服の特徴を仕草へ接続する:** 背中開きなら振り返り、長い裾なら階段や風、緩んだカーディガンなら帰宅後のソファなど、衣装がその場面にある理由をつくる。
- **上品な色気:** 艶のある素材、精密なカッティング、光の境界、視線、距離感で表現し、露出箇所を増やすだけの設計にしない。
- **だらしない色気:** しわ、半端なタックイン、ずれた上着、ほどけかけの髪など「出来事のあと」の生活感で表現し、脱衣や露骨な描写にはしない。
- **堅実服は映画的な場面へ:** 端正なスーツ、トレンチ、ロングコートなどは、旅の途中、閉館後、式典帰り、雨のホテル玄関など、シルエットが意味を持つ状況で使う。
- **成人条件:** 色気を含む衣装・演出は、参照人物が明確に成人と判断できる場合だけ使用する。年齢が不明、または未成年に見える場合は、同じ配色と雰囲気を保った健全な代替衣装・ポーズへ切り替える。

## プロンプト記述の共通規約

181（チビドゥードルズ）の元ネタ検証と178派生の知見から一般化した、全プロンプト共通の書き方ルール。

- **参照にないものを足さない（ハードコード禁止）:** 「参照から推測して保持」だけでは、モデルが別キャラクターの特徴（髪色、アクセサリー、制服、小物）を勝手に持ち込むのを防げない。逆方向のガードとして `never add or hardcode features that are not present in the reference` を入れる。共通テンプレートに反映済み。
- **モデル任せの可変要素には収束癖ガード:** ポーズや仕草をモデルに発明させる場合、放置すると指差し・フィンガーガン・棒立ちに収束する。可変にした要素には `never a pointing or finger-gun pose` のように、収束しがちな定番を明示的に外す1句を添える。ポーズを固定指定する案には不要。
- **例示は「ゆるいインスピレーション」と宣言する:** 可変要素に例を並べると毎回先頭の例に収束しがち。例示リストには `loose inspiration only, not a fixed menu — invent freely beyond these` の但し書きを付ける。背景・小物・いたずら・ポーズなど、すべての可変リストに適用できる。
- **表情は形容詞でなく内心で書く:** `cute, shy` のような形容詞の羅列より、`half playing along and half wondering why` のような内心の一文の方が演技が具体化する。表情・リアクションの指定は内心ベースを基本にする。
- **手が目立つ構図には解剖学ネガ:** 手・指がフレーム内で主役級に写る構図（顔の横に手が来るポーズ、差し出す手、小道具を持つ手）では `no extra limbs, extra fingers, or malformed hands` を Avoid 行に入れる。
- **ネガは「観測した失敗」だけを具体で書く:** 否定形はモデルに無視されやすい（178派生の知見）。破綻対策はまず肯定形の描写で行い、それでも出る既知の失敗だけを具体的な語でネガに残す。「明らかなAIアーティファクトなし」のような抽象ネガは効かないので書かない。

## 共通テンプレート

各案は、以下の骨格の「ポーズ / 服装 / 背景 / フォーマット」ブロックを差し替えて使う。

```
A highly detailed photorealistic portrait of the person from the reference image.
[ASPECT] aspect ratio. Infer apparent age from the reference image and preserve it.
Match the reference image exactly for gender presentation, ancestry, body shape and
lines, height impression, proportions, overall build, skin tone and texture, facial
features, hair, and all physical characteristics including chest and hip shape and
fullness. Reproduce the natural volume and silhouette of the bust and hips as seen
in the reference, kept accurate through the fit and drape of the clothing. Preserve
the subject's identity and physique faithfully without age-shifting, beautifying,
exaggerating, or reshaping. Never add or hardcode features that are not present in
the reference image — no invented hair colors, accessories, uniforms, or props.

Pose: [ポーズ]
Outfit: [服装]
Background: [背景と光]
Format: [ASPECT], [縦/横] composition.
```

## アスペクト比の使い分け指針

| 比率 | 向き | 主な用途 |
|---|---|---|
| 9:16 | 縦（超縦長） | 全身と衣装の縦線を見せる、Reels / TikTok / Stories |
| 3:4 | 縦 | バストアップ〜膝上。人物と背景のバランスが最も取りやすい標準 |
| 4:5 | 縦 | Instagram フィードの最大表示。上半身主体 |
| 1:1 | 正方形 | 顔・上半身のクローズ。シンメトリな構図 |
| 4:3 | 横 | 人物＋周囲の状況を見せる。室内・生活シーン向き |
| 16:9 | 横（シネマ） | 風景に人物を溶かす。引きの画、映画的な余白 |

**判断の基準**：被写体を主役にするなら縦、環境を主役にするなら横。全身と長い衣装の流れを見せたいときは 9:16、それ以外の縦は 3:4 か 4:5 のほうが破綻が少ない。どの比率でも、参照由来の身長感や身体比率を変えない。
