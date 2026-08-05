# 33. 水滑り台×水飛沫×15時の太陽、フローラル紐トップ×白ボトム（参照画像ベース）

`ideas/README.md` の人物参照方針に準拠し、人物の顔・髪・肌・体型・胸と腰まわりの形と自然なボリューム・身長感・プロポーションなどの身体的特徴を参照画像から精緻に保持する。胸・腰のボリュームはユーザー指示により保持ブロックで参照どおり保持（圧縮版: サイズ保持2文＋布の挙動文のみ、高位文はトリガー表面積削減のため本文から外す。`ideas/391-393-waterslide-spray-light.md` の設計の柱4参照）。`ideas/391-393` の392案を採用した実生成用フォルダ。15時ごろの屋外ウォータープールでストレートの水滑り台を滑る一瞬を、ド派手な水飛沫と飛沫に反射する西日を主役に切り取る。

- **アスペクト比:** 3:4 縦
- **見せ場:** ストレート滑降の正面からの迫力と、水シートの放射状の線。結び目の房が疾走の風になびいて躍動感を足す
- **衣装:** トップ＝ヴィンテージフローラル柄（クリーム地にバターイエローの花×ダークオリーブの芯・ブラッシュピンク・深緑の小葉）、肩で結ぶ細いコード紐。下＝無地の白、腰で結ぶ白い細紐＋房（ユーザー指定）
- **光:** 15時の西斜光が横から水面を走り、飛沫の粒子一つ一つを小さなハイライトの星に変える
- **遮蔽:** 水飛沫のヴェールを構図的遮蔽（布で見せないの水版）の主役に。白ボトムは飛沫と同色融合して下半身を飛沫へ溶かす
- **既存案との差:** 365/28（渓流足浸し）は静止して水に浸かる涼、本案は滑走の躍動と飛沫の光が主題。391（カーブ・9:16）/393（着水の光の壁・16:9）とはトップのシルエットと構図で差別化

---

## プロンプト

```text
A photorealistic editorial action photograph for a summer sportswear catalog feature — a clean, wholesome, energetic outdoor scene — of the person from the reference image, shot on a full-frame camera with a fast shutter. 3:4 vertical aspect ratio, full body in frame. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing, the fabric curving smoothly over the bust and draping from its outermost point with gentle tension lines. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode features that are not present in the reference image — no invented hair colors, accessories, uniforms, or props. Use this scene only if the reference is unambiguously adult; otherwise switch to a long-sleeve rash guard and knee-length board shorts in the same cream floral palette.

Scene: On a midsummer day off at an outdoor water park, around three in the afternoon, she is caught mid-descent on a wide open straight water slide, coming almost directly toward the camera. She wears a current-season quick-dry sport set — the top in a vintage floral print on a cream ground, butter-yellow flower motifs with dark olive centers, blush-pink accents, and small deep-green leaves scattered across the fabric, a clean cut held by thin cords, a single string rising over each shoulder and knotted in a small bow, the cords tracing fine lines that follow the contour of the collarbone, a soft matte quick-dry fabric that follows the body — paired with plain white simple bottoms tied at the sides of the hips with thin white strings knotted in small bows, the loose ends fluttering in the rush of air. A cute current-season athletic cut, the whole set reading as one clean cream contour with butter-yellow and pink points and thin cord lines against skin. Her hair, in the same style as the reference, streams back in the rush of air. Empty-handed, her body is in the natural sliding posture of the straight drop, shoulders slightly back, arms trailing in the flowing water, face lit with the bright physical thrill of speed, mid-laugh.

The slide flume is a wide open straight trough of pale fiberglass, water sheeting fast down its surface in radiating lines toward the camera, the laminar sheet breaking into spray at her passage. The mid-afternoon sun is past its peak and coming in at a low western angle from the side, raking across the flowing water. Water sheets up from the flume and bursts into spray around her as she descends, a bright frothy wake trailing behind, and the low sun lights every airborne droplet into small crisp points of light, so the air around her shimmers with scattered sparkles refracting the afternoon light. The cream contour of the top and its thin cord lines and the white spray share the same highlights and merge at the edges, the loose bow ends streaming in the air and the butter-yellow flower motifs flickering as small points of color within the white, while the plain white bottoms dissolve into the spray entirely, so the set reads as part of the water rather than a separate surface, and the water and light are the main surfaces the eye reads.

A frontal-or-three-quarter-front view as she comes down the straight flume toward a camera positioned at the lower end of the slide; never show her from behind. Give the spray, the light, and the figure equal visual weight. Fast shutter freezing every droplet crisp, shallow depth of field on her with the spray and slide edges falling to soft bokeh, backlight handled to let the droplet highlights sparkle without washing the frame to white. Accurate hands, no extra limbs, no distorted fingers. Fine-grain color-negative film, neutral color balance, softly rolled-off highlights, clean uncolored frame edges, natural skin texture, no beauty filter, no HDR glow.

Keep the spray and scattered sparkles present — do not flatten the scene to a dry slide. Do not let the cream contour or its thin cord ties vanish entirely into the white spray. Keep the light as a side raking angle — do not turn it into flat front light. Keep her in the sliding posture of the straight drop — do not straighten her into a standing or posed pose.

Format: 3:4 portrait orientation, vertical composition.
```

---

## 設計メモ

### 幾何学・光学言い回しと水飛沫遮蔽
- 水着の直接語（`bikini` / `swimwear`）は不使用。衣装は `quick-dry sport set` とし、身体との境界を線と輪郭で描く（`the cords tracing fine lines that follow the contour of the collarbone`）。
- 水飛沫のヴェールを構図的遮蔽（expression/01 の「布で見せない」の水版）の主役にし、衣装を「飛沫の中にちらつく色と線」へ抽象化。白ボトムは飛沫と同色融合して下半身を飛沫へ溶かす。
- 文脈枠は `summer sportswear catalog feature — a clean, wholesome, energetic outdoor scene`。catalog 枠と肯定アンカー（`clean / wholesome`）で安定させる。

### 胸・腰のボリューム保持（圧縮版）
- 保持ブロックはサイズ保持に必須の2文（`including chest and hip shape and fullness` / `Reproduce the natural volume and silhouette of the bust and hips…`）と布の挙動文（`the fabric curving smoothly over the bust and draping from its outermost point with gentle tension lines`）のみ。
- 高位文（`as if wearing a well-fitted bra` / `armpit height` / `never sagging`）は下着語彙＋胸部解剖の反復で水着文脈のトリガーになりやすいため本文から外す。生成結果で位置が低いと判断した場合のみ `ideas/391-393` 設計メモの任意付加オプションを付加する。

### 運用
- 参照画像（`main/_profile/Woman's_portrait_on_beach_4K_202608030518.jpeg` など既定の参照）と一緒に貼り付けて単体で使う。
- ChatGPT画像で弾かれた場合は1〜2回再試行（判定にランダム性あり）。最終フォールバックはプロンプトに埋め込んだラッシュガード＋ボードショーツ（同クリームフローラルパレット）。
- 派生元と検証履歴は `ideas/391-393-waterslide-spray-light.md` に記録。
