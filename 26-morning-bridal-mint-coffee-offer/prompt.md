# 26. 朝の差し出すコーヒー、ミントのシアーブライダルガウン（参照画像ベース）

`ideas/README.md` の人物参照方針と `expression/01-sheer-skin-intimacy.md` の間接表現手法に準拠。人物の顔・髪・肌・体型・身長感・プロポーションなどの身体的特徴は添付画像から忠実に保持し（髪を含む身体特徴は本文にハードコードしない）、ラグジュアリーブライダルエディトリアル×朝の文脈で健全に収める。参照画像のベビードールと同じ光学（薄い布を朝光が通って体の輪郭が布の中に影絵として浮かぶ）を、ミディ丈のシアーガウンに転用した「差し出すコーヒー」の朝。色は白禁止の依頼に対し「若くて爽やか」へ最も振れる**ソフトミント**を採用。背景は無地の淡い壁＋シアーの白カーテンだけにミニマル化。透過は expression/01 の「透け感には必ず構造」を守り、肌色・下着は透かさず光が通る部分だけシルエットを浮かべる設計。ネガティブ欄は作らず、除外要素は肯定文中に織り込む（ChatGPT画像で除外欄が逆に不安定化することを観察済み）。

- **アスペクト比:** 4:5 縦（上半身主体。差し出す腕とカップに前景の余白）
- **見せ場:** ①カメラへ差し出されたコーヒーと湯気（媒質=湯気）②逆光でガウン全体にうっすら浮かぶボディーラインの影絵。同じ朝の逆光が「裸の肩は直接リム／布は透過して輪郭を描く」の2態様を1主題に統一（356 の二光源デバイスの転用）
- **構図:** ソフトな三分の二スタンス。差し出す腕は胸の前を横切らず体の斜め横へ、もう片手はうなじの髪。4:5 で腿半ばから上、顔は上三分の一。差し出す手は前景に入りつつ自然な遠近に収める
- **服装:** ソフトミントのシアーブライダルモーニングガウン（白禁止の代替色）。極薄サテン1枚＋シアーチュール1層で、バスト・ウエスト・ヒップ・太もものラインが逆光でうっすら影絵として浮かぶ。影側のひだは不透明のまま（構造ガード）。肌色・下着は透かさずシルエットのみ
- **背景:** 無地の淡い壁＋シアーの白カーテンだけ。家具・鏡・花・小物は一切なし（肯定文＋明示的除外でガード）。湯気は暗い壁側へ配置して可読性を確保
- **照明:** 低い朝日がカーテン越しに側面〜背面から。裸の肩・腕・髪を暖色リム、布を透過して輪郭を描く。湯気は窓光に照らされるだけで発光体にしない（22/25 の教訓）
- **文脈:** ラグジュアリーブライダルエディトリアル × 朝 × 友人カメラマンへの差し出し。若く爽やかなトーン
- **差し替え変数:** 色（アイスブルー、ペールレモン、ライラック）、壁色（オフホワイト↔淡グレージュ）、透け強度（1語で調整）

---

## プロンプト

```text
A highly detailed photorealistic portrait of the person from the reference image. 4:5 vertical aspect ratio, an ultra-realistic editorial fashion photo shoot in the style of a luxury bridal editorial. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate through the fit and drape of the clothing. Preserve the subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never add or hardcode features that are not present in the reference image — no invented hair colors, accessories, uniforms, or props. Use this outfit and its translucent effect only if the reference is unambiguously adult; otherwise switch to a fully opaque matte soft-mint chiffon gown with no translucency in the same scene. Avoid: no extra limbs, extra fingers, or malformed hands.

Pose: Morning in a bright, bare room, caught in the middle of offering a cup of coffee to the friend behind the camera. She stands in a soft three-quarter stance, torso angled a quarter-turn away from the reaching arm, and extends one arm forward and slightly out to her side, presenting a small clear double-walled glass mug of black coffee toward the viewer at chest height. The offered mug stays beside the line of her torso, never crossing in front of her chest, and nothing else is held in front of the body. The reach is gentle — elbow soft, wrist level, the coffee surface calm and flat — a quiet "would you like some?" gesture, not a thrust. Her other hand is tucked into the loose hair at her nape, lifting it lightly off her neck. Her chin tips toward the coffee, then back up to the viewer, a small knowing smile — half hosting, half showing off the morning she has made. Inner-thought acting, not a posed advertisement grin. The offering hand is simple and natural, fingers relaxed around the mug, five fingers exactly. The three-quarter stance lets the line of the bust, the cinched waist and the curve of the hip read in profile through the gown. Candid, mid-gesture, a real moment with the person behind the camera.

Outfit (visual elements / optical material design): An haute-couture bridal morning gown in soft mint — a pale, sun-washed mint tone, fresh and youthful, clearly not white — built from a single fine layer of sheer tulle over a whisper-thin silk-satin slip in the same soft mint, the slip itself so thin that the body reads faintly through the whole gown, not only at the sleeves. Where the morning light passes through the layered fabric, the micro-fibre structure of the tulle and the thin slip scatter and partially transmit it, and the light physically suggests the tone and contour of the body beneath: the line of the bust, the cinch of the waist at the sash, the curve of the hip and the shape of the thigh read as soft dark silhouettes within the glowing cloth — the body's outline as shadow-form in the fabric, the way thin material against bright light really behaves, a contour implied by light rather than shown. The translucency is silhouette only — no skin tone showing through, no underwear detail, no see-through; in the shadowed folds the soft mint stays fully its own colour and opaque, so the body-line appears only where the light passes through and fades to nothing in shadow. Thin delicate straps frame the collarbones as fine lines; a deep open-back cut lets the arch of the back read along the morning light; long sheer bishop sleeves gather into lace-trimmed cuffs at the wrists, the arm within them a soft luminous shape; the skirt falls full and soft to mid-calf, the legs beneath it a gentle hazy silhouette where backlit and simply the drape's own colour in shadow; a slim satin sash in a slightly deeper mint ties at the natural waist in a small bow, marking the waistline where the silhouette cinches. The bodice fabric follows the body — it curves over the bust and drapes from its outermost point with gentle tension lines, so the silhouette reads exactly as in the reference. The bust sits high and supported on the ribcage, as if wearing a well-fitted bra: its fullest point level with the mid-upper arm, roughly at armpit height, with only a short distance between the collarbones and the top of the curve — never sagging low toward the waist. A contemporary fine-art study of material, light and the human form — light, airy and young, a fresh editorial bridal-morning look. No close-up of body parts, no voyeuristic gaze.

Background: A simple bright room in the morning — nothing but a plain pale wall and a tall window hung with a sheer white curtain that glows as a soft, almost blown-out field of morning light. No furniture, no mirror, no flowers, no props of any kind in the room; the wall and the curtain are the entire backdrop. The low morning sun comes through the curtain from her side and slightly behind. She stands so the glowing curtain fills one side of the frame while the plain wall, in gentle warm shadow, fills the other — and the offered mug with its steam sits against that wall so the pale ribbon of steam reads clearly against it, lit by the window light, not a light source itself. The same sun rims her bare shoulder, the reaching arm and the hair in a thin warm edge, and, passing through the sheer gown, makes the cloth glow so the body's silhouette reads softly within it — a warm rim on the bare skin and a transmitted glow through the fabric that draws the body-line, the body read by light rather than exposure. One palette of soft mint, white and morning gold, the dark coffee in the glass mug as the single deep accent.

Camera: 50mm lens at f/2.8, set just below chest height and close enough that the offered mug enters the near foreground — mug and steam sharp and clearly readable, her face and the gown's drape tack-sharp behind it in the middle ground. The perspective of the reaching arm stays natural — a believable hand size, no exaggerated foreshortening, no oversized fingers. Framed from mid-thigh up, her face on the upper third, the reaching forearm drawing a soft depth line from her shoulder to the mug; the faint body-line through the backlit skirt and bodice stays crisp where the light passes. The bright curtain is kept off her face — her features are modeled by soft bounced morning light, with a gentle warm rim along the reaching arm, the hair and the open back; no bright band across the cheek or forehead. Natural sensor grain, no HDR glow, no beauty filter; real skin texture — pores and fine peach-fuzz, small highlights at the nose bridge, cheek, lip crest and the bare shoulder.

Format: 4:5 vertical orientation, intimate editorial composition, the offered coffee as the near subject.
```

---

## 設計メモ

### 既存案との差
- **10（朝バスルーム・ブライダルシアー）**: 窓辺に立つ単一像・白・上半身強シアー＋下半身は裏地で潰す。本案は「差し出す」動作・ミント・ガウン全体にうっすらボディーライン・背景ミニマル。
- **199（ホテルのカーテン開け・ローブ逆光影絵）**: 布1枚の逆光影絵＋開ける動作。本案は差し出す＋二重の光（裸の肌の直接リム＋布の透過輪郭）。
- **197（家庭キッチンのトースト湯気）**: 静の画・家庭。本案はブライダル／ミニマルルームの差し出す動の画。

### 透け設計（expression/01 準拠）
- 初期版（胴〜脚をサテン裏地で完全に潰す）から、極薄サテン1枚にしてガウン全体でうっすらボディーラインが読める仕様へ引き上げ。参照画像のベビードールと同じ光学をミディ丈ガウンに転用。
- 「透け感には必ず構造」: 肌色・下着ディテールは透かさず、光が通る部分だけシルエットが浮かび、影のひだは不透明のまま。覗き見的クローズなし。
- 透け強度は1語で段階調整: `reads faintly`（標準）↔ `reads only at the faintest threshold`（弱）/ `reads clearly as a soft silhouette`（強）。

### 差し出すポーズの破綻対策
- 前腕の強制パースで手が巨大化しやすい → `a believable hand size, no exaggerated foreshortening, no oversized fingers` をカメラブロックに明記。
- 手が主役級 → `Avoid: no extra limbs, extra fingers, or malformed hands` を冒頭に配置。
- 胸潰れ対策: カップは体の斜め横へ差し出し、胸の前を横切らない／何も持たない、を Pose に明記。

### 湯気の発光対策
- 22/25 の教訓を継承: `a pale ribbon lit by the window — lit by the light, not a light source itself`。

### 背景ミニマル化のガード
- モデルが勝手に小物（鏡・花瓶・家具）を足すのを防ぐため、肯定文で「壁とカーテンだけ」を宣言し、`No furniture, no mirror, no flowers, no props of any kind in the room` で明示的に除外。湯気は暗い壁側へ配置して可読性を確保。

### 色の選定
- 白禁止の依頼に対し「若くて爽やか」へ最も振れるソフトミントを採用。白カーテン＋朝光に透けて清涼感が出る。サッシュは一段濃いミントでウエストラインをマーク。差し替え変数に他色（アイスブルー、ペールレモン、ライラック）を用意。色の差し替えは `soft mint`（と `slightly deeper mint` / `soft-mint chiffon`）を置換するだけで回る。
