# 15. 植物園の野草クラスタにしゃがみ込む（参照画像ベース）

`ideas/README.md` の人物参照方針に準拠し、人物の顔、髪、肌、体型、身長感、プロポーションなどの身体的特徴は添付画像から忠実に保持する。`expression/01-sheer-skin-intimacy.md` の「素材のふるまいで出す」手法をスカートの際どさに適用する。露出語彙に頼らず、布の物理的な挙動（ヘムの持ち上がり、左右非対称、影と見分けがつかない安全ショーツの帯）で際どさを出す。

- **アスペクト比:** 4:5 縦長
- **見せ場:** 夏の有名花6種が混生するクラスタと、しゃがみで持ち上がるスカートのヘムライン、Vネックの開き
- **花の種類:** hydrangea / salvia / garden roses / lavender / marigolds / daisies の6種、高低差つき
- **スカート:** warm off-white ivory のmid-thigh丈A-lineミニ。しゃがみで前面ヘムが数cm持ち上がり、ヘムと膝の間に細い肌の帯。背面ヘムは低く残り左右非対称。下には何も着用しない
- **文脈:** 植物園の午前 × 野草を見つけた一瞬 × 布の物理挙動と光の素材研究

---

## プロンプト

```text
A highly detailed photorealistic portrait of the person from the reference image. 4:5 vertical aspect ratio,
a full-body botanical-garden portrait including the subject, the hand gesture, and the small flowers near the
feet. Infer apparent age from the reference image and preserve it. Match the reference image exactly for gender
presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and
texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness.
Reproduce the natural volume and silhouette of the bust and hips as seen in the reference, kept accurate
through the fit and drape of the clothing. The bust sits high and supported on the ribcage, as if wearing a
well-fitted bra: its fullest point is level with the mid-upper arm, roughly at armpit height, with only a short
distance between the collarbones and the top of the curve — never sagging low toward the waist. Preserve the
subject's identity and physique faithfully without age-shifting, beautifying, exaggerating, or reshaping. Never
add or hardcode physical features that are not present in the reference image.

  Use the mini-skirt styling only if the person in the reference image is unambiguously an adult. If the
apparent age is uncertain or the person appears underage, replace it with a fully opaque knee-length A-line
skirt while preserving the same colors, pose, botanical setting, and cheerful tone.

  Pose: The subject crouches low at the edge of the stone path, right beside the flower bed, her body turned
about forty-five to sixty degrees to the side of the camera so she reads in three-quarter view. She settles
into a deep, asymmetric squat: the nearer leg is drawn forward with the knee bent high toward the chest and
the foot flat on the ground, while the farther leg folds back beneath her, balanced on the ball of the foot.
The upper body stays fairly upright rather than hunched forward; only the head tilts down.

  The far-side hand rests flat and relaxed on top of the raised near knee, the fingers draping gently over the
kneecap. The near-side arm reaches down toward the flowers, the hand cupped softly upward to cradle a single
open blossom from beneath, supporting it with palm and fingertips without plucking it, bending the stem, or
closing the fingers around the petals. The cradled flower, the supporting hand, and the down-turned face must
all remain clearly visible.

  The subject does not look toward the camera. Her chin is lowered and her head tilts down toward the blossom
she is cradling, the lids softly dropped so the gaze falls entirely on the flower, absorbed as though she has
forgotten anyone else is there. A small, private smile rests on her lips, the kind that appears when something
small and beautiful holds your attention completely. The down-turned three-quarter profile reads clearly: the
slope of the forehead, the line of the nose, the lowered lashes, and the corner of the smiling mouth. Candid,
unposed, caught mid-moment.

  Outfit: A fully opaque, soft fine-knit V-neck top in a pale mint green with short sleeves, fitted naturally
without compression. The V opens to the mid-sternum, the fabric following the natural curve of the bust
and framing the décolletage with a clean, unadorned line. Pair it with a high-waisted A-line mini skirt in a warm off-white ivory opaque woven fabric (a soft cream-tinged white, clearly distinct from the pure white of the daisies),
structured enough to hold its shape yet short enough that the hem sits at mid-thigh when standing. In the
crouch, the skirt's front hem rides up a few centimeters along the thigh, the fabric drawing taut across the
upper leg and revealing a narrow band of skin between the hemline and the knee. The back hem stays slightly
lower, held by the seated posture, creating an asymmetric hemline that catches light differently on each side.
Nothing is worn beneath the skirt. Simple low-profile walking shoes
suitable for a botanical garden. Keep the palette restrained and daytime-appropriate.

  The clothing must follow the reference physique faithfully. Nothing is carried or crossed in front of the
chest. The knit fabric curves naturally over the bust and falls from its outermost point with gentle,
physically plausible tension lines, preserving the reference silhouette without exaggeration.

  Background: A botanical garden at approximately 10 a.m. The subject is beside a curved stone path where a
small wildflower cluster grows close to the ground: a low rounded mound of blue-violet hydrangea blossoms
at the back, several upright spikes of deep purple salvia rising beside them, a few stems of soft pink garden
roses at mid-height, a generous spread of lavender with its slender purple flower spikes leaning gently over
the path edge, clusters of bright orange-yellow marigolds catching the light at ground level, and a scatter
of white daisies with open faces threading through the gaps. The varieties intermingle at different heights,
from ankle-level marigolds and daisies to knee-height hydrangea mounds and salvia spikes, giving the cluster
natural depth and a lush midsummer abundance.
Taller foliage forms a soft green backdrop, while sunlight filtered through overhead leaves creates irregular
patches of light across the path, skirt, hands, and flowers. One clear patch of light falls across the mixed
cluster, making the white petals and blue forget-me-nots stand out without artificial glow. The garden feels
fresh, quiet, and already fully awake rather than misty or dawn-like.

  Camera: 50mm lens at f/2.8, positioned in front of the subject and approximately 30 to 45 degrees to one
side. Keep the camera around the subject's seated chest height, clearly above the flowers and knees, never at
ground level and never looking upward beneath the skirt. Frame the face in the upper third and the flowers with
the supporting hand in the lower opposite third, creating a clean diagonal connection between gaze, fingertips,
and blossom. Full figure remains visible from hair to shoes. The face, eyes, hand, and selected flower share
sufficient focus; surrounding foliage falls into a soft natural blur. Realistic daylight, natural skin texture,
restrained highlights, and fine sensor grain.

  Avoid: low-angle or upward-looking framing, under-skirt visibility, exposed underwear, distorted crouching
anatomy, hidden face, blocked flowers, picking or crushing the flower, extra limbs, extra fingers, or malformed
hands.

  Format: 4:5 portrait orientation, full-body vertical composition.
```

---

## 設計メモ

### 花の多様性

- 1種だけだった花を4種（oxeye daisies / forget-me-nots / wild roses / buttercups）に拡張。
- 高低差（ankle-level buttercups → knee-height rose stems）でクラスタに奥行きを出す。
- 光のパッチが複数種に当たる描写で、白と淡青の花弁が自然に際立つ。

### スカートの際どさ（`expression/01` の素材ふるまい手法）

- 丈を mid-thigh に短縮。しゃがみで前面ヘムが数cm持ち上がり、ヘムと膝の間に細い肌の帯が出る物理挙動を記述。
- 背面ヘムは座位で低く残り、左右非対称。光の当たり方が両側で異なる。
- 安全ショーツは「ヘムの縁に影と見分けがつかない細い帯」として気配だけ残す。露出語彙（sexy, daring, revealing）は使わず、布のテンションと光の境界で際どさを出す。

### 既存案との差

- `14` はベランダの朝顔、指先と横顔を同一水平線に置く近距離構図。
- `200` は庭のホース霧と全身、低い朝日が主役。
- `15` は植物園の4種野草クラスタ、しゃがみ姿勢、スカートの物理挙動が主役。霧、風鈴、布の透過は使用しない。
