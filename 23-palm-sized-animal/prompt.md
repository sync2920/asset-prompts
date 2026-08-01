# 23. 手のひらサイズの小さな客、一緒にカメラ目線（参照画像ベース）

`ideas/README.md` の人物参照方針に準拠し、人物の顔、髪、肌、体型、身長感、プロポーションなどの身体的特徴は添付画像から忠実に保持する（髪を含む身体特徴は本文にハードコードしない）。掌に収まるサイズの小さな動物を掲げ、人物と動物がそろってカメラ目線で柔らかく微笑む「紹介ショット」。動物の種・動物のポーズ・人物の掲げ方・背景は生成のたびにプロンプト内でランダム抽選される（`181` のモデル発明方式の転用）。動物はぬいぐるみ化を排した実写の生き物として描きつつ、穏和な種の選定・幼体比率・落ち着いた態度で怖さのない可愛さを担保する。服装は参照画像から再現（テキストで固定しない）。掲げ方がランダムでも「掌で掲げる・両者カメラ目線・微笑み・胸の前を空ける」は不変条件として明文化してある。

- **アスペクト比:** 4:5 縦（Instagram フィード向き）
- **見せ場:** 掌の上の小さな動物と人物の顔のツーショット。フォーカスは動物と掌のラインにロックし、顔はすぐ後ろで読める程度に。
- **構図:** 掌と動物をフレームの前景半分、顔をすぐ後ろに。掲げ方（カメラへ差し出す／顎の横／鎖骨の高さで手首を添える等）は毎回ランダム。
- **服装:** 参照画像から再現（テキストで固定しない）。布の挙動（バストを越えてカーブし最も張り出した点からドレープ）とバスト位置の基準点指定は服装に依存しない再現指示として残す。
- **動物:** 生成ごとにランダム抽選（子猫・トイプードル/ポメラニアンの子犬・うさぎ・ハムスター等、例示はゆるいインスピレーション宣言付き）。大粒のイチゴ程度のサイズで掌に完全に収まる。種に正しい解剖学・一本一本の毛並み・濡れた鼻・掌に乗る重みを肯定形で指定。ポーズも毎回ランダム（おねだり・片手あげ・隠れんぼ・プレイバウ等）。
- **背景:** 生成ごとに異なる整った実世界背景を、柔らかい夏の昼光で大きくぼかす。
- **文脈:** いちばん小さな友だちの紹介 × 顔とのサイズ対比 × 実写の毛並み × プロの一瞬

---

## プロンプト

```text
A highly detailed photorealistic portrait of the person from the reference image. Carefully study the reference image and reproduce the subject's appearance with strict fidelity to every visible detail. 4:5 aspect ratio. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode features that are not present in the reference image — no invented hair colors, accessories, uniforms, or props.

Pose: She presents the tiny animal on her open palm to the camera — and the two of them face the camera together, like friends posing for one photo. Her exact way of holding and posing is her own invention, different every generation — one palm extended toward the lens at chest height, the palm raised beside her chin with her head tilted toward it, the palm held at her collarbone with her free hand cradling that wrist, the palm lifted near her shoulder as she leans in toward it, or equally lighthearted variations; loose inspiration only, not a fixed menu — invent freely beyond these, never a pointing or finger-gun pose. In every variation her arms stay clear of her chest — nothing crosses or covers her chest. She looks straight into the lens with a soft, happy smile that rises naturally to her eyes: the smile of someone introducing a dear little friend. Her feeling comes from the inside: half proud to show off the tiny guest, half simply happy it chose her hand.

Animal — chosen at random on every generation: Pick one small, naturally gentle real animal to sit on her palm — for example a tiny kitten, a toy-poodle or Pomeranian puppy, a baby rabbit, a hamster, a chinchilla, a duckling, a baby hedgehog, a red squirrel, a sugar glider, a baby owl, or a fennec fox kit. Loose inspiration only, not a fixed menu — invent freely beyond these, but always choose a species whose real appearance is soft and harmless; never one that bares its teeth, raises its hackles, or threatens. The animal is small enough to rest entirely within her open palm — roughly the size of a large strawberry — and it is a real living creature, never a plush toy, figurine, or cartoon: correct anatomy for its species with the right number of limbs and proper paws, real fur or feathers with individual strands catching the light, a moist nose, whiskers, and believable weight settling into her skin. Favor the young of the species, whose naturally larger head and eyes keep it endearing without any cartoon exaggeration.

Animal pose — its own invention, different every generation: The animal strikes a small charming pose that is natural to its species and turned toward the camera with her. Loose inspiration only, not a fixed menu — invent freely beyond these: standing tall on its hind legs with front paws tucked in a begging pose, one front paw raised toward the lens as if reaching out, rolled onto its back with all four paws curled in the air and its face tipped toward the camera, or mid-yawn showing its tiny tongue. Always a distinct, readable little gesture — never a plain neutral sit. Its mood is calm, trusting, and mildly curious about the lens, leaning into the warmth of her hand.

Outfit: Reproduce the outfit from the reference image exactly — same garment, color, neckline, fit, and styling, without substitution or embellishment. Whatever the garment, the fabric follows the body's line: it curves over the bust and drapes from its outermost point, with gentle tension lines — never a stiff, boxy cut that floats away from the body. The bust sits high and supported on the ribcage, as if wearing a well-fitted bra: its fullest point level with the mid-upper arm, roughly at armpit height, never sagging low toward the waist. Nothing competes with the tiny animal — no added logos, jewelry, or loud patterns beyond what is in the reference.

Background: A different coherent, uncluttered real-world background every generation, rendered as a soft wash of blur in gentle summer daylight; nothing in it pulls the eye from her palm and her face.

Camera: 50mm lens at f/2.8, focus locked on the animal and the lines of her palm, her face just behind falling only slightly soft while staying fully readable. The animal rests fully supported on her palm — never floating, never sinking through the skin. Both hands and the animal are anatomically correct: no extra limbs, extra fingers, or malformed hands. Natural skin texture, natural sensor grain, no beauty filter.

Format: 4:5, vertical composition, the palm and its tiny guest in the foreground half of the frame, her face close behind.
```

---

## 設計メモ

### 既存案との差

- 動物が第二の主役として「ちゃんと見える」案は本リポジトリで初。`151-180` の「見えない生き物を抱く」案や `206-355` の気配のツーショット群は、生き物の存在を物理的な証拠（重み・へこみ・結露）だけで描く設計だったのに対し、本案は実写の小動物を正面から見せる。
- ランダム抽選は `random/` のスロット表方式ではなく、`181`（チビドゥードルズ）の「プロンプト内でモデルに毎回選ばせる」方式を動物に転用。貼り付け1回で完結し、生成のたびに種・ポーズ・掲げ方・背景が変わる。
- 採用経緯: チャットで 362〜364 として設計した3姉妹案（4:5 差し出し / 1:1 両手包み / 3:4 頬の高さ）のうち、362 を本案として採用。363・364 は未保存。

### ランダム化の設計

- 可変要素は4つ: 動物の種 / 動物のポーズ / 人物の掲げ方 / 背景。すべての例示リストに `loose inspiration only, not a fixed menu — invent freely beyond these` を付記（`ideas/README.md` の収束対策規約）。
- **動物ポーズは独立セクション**（`Animal pose — its own invention, different every generation:`）として、人物ポーズ（`Pose:`）と対等の構造・文言で記述。種の選定・サイズ・リアリティの制約と混在させるとポーズ指示が「ついで」扱いになり収束するため、分離した。例示は4つに削減（README「例を並べると先頭に収束しがち」対策）。
- 人物ポーズの収束ガード: `never a pointing or finger-gun pose`。動物ポーズの収束ガード: `Always a distinct, readable little gesture — never a plain neutral sit`（ただ座って無表情、がデフォルト収束先のため）。
- 不変条件は Pose ブロック内で `In every variation ...` として明文化: 掌で掲げる・両者カメラ目線・柔らかい微笑み・胸の前を空ける。ガチャが回ってもこの4点は毎回成立する。

### 可愛さと実写の両立

- 可愛さは3段構え: ①種の選定制約（外見が柔らかく無害なものだけ。牙を剥く・逆立つ・威嚇するものは選ばせない）②その種の幼体比率（実際の幼獣が持つ大きめの頭と目。カートゥーン的誇張ではない）③穏和で信頼した態度（手の温もりに寄り添う）。
- 実写性は肯定形で担保: 種に正しい解剖学と四肢・肉球、一本一本の毛並み、濡れた鼻、掌に沈む重み。ぬいぐるみ・フィギュア・カートゥーン化は観測済みの代表的失敗として具体的な語でネガに置く（`never a plush toy, figurine, or cartoon`）。
- サイズのアンカーは「大粒のイチゴ程度」＋「掌の中に完全に収まる」の2点で固定。

### 体型保持（胸の前を空ける設計）

- 掲げ方がランダムでも胸の前を空けることを不変条件に格上げ（`In every variation her arms stay clear of her chest — nothing crosses or covers her chest`）。
- 服装は参照画像から再現（`Reproduce the outfit from the reference image exactly`）。テキストで特定の服を固定しない。布の挙動の明示（`curves over the bust and drapes from its outermost point, with gentle tension lines`）＋バスト位置の基準点指定（脇の高さ、二の腕の中ほど）は服装に依存しない再現指示として残す。`ideas/README.md` の「胸が小さく出る主因はポーズと生地」対策に準拠。

### 手と動物の解剖学ネガ

- 掌が画の主役級の構図のため `no extra limbs, extra fingers, or malformed hands` をカメラブロックに配置。
- 動物側は肯定形で「種に正しい数の四肢と肉球」「掌に完全に支持されている — 浮遊も皮膚へのめり込みもなし」を指定。小さい生き物は四肢欠損・融合が出やすいため。
