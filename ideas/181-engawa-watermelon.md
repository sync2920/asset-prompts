# 181. スイカと風鈴の縁側

夏の縁側で、着古したキャミソールとくたびれた短パンのまま、スイカを口へ運ぶ。だらしなさと上品さを同居させた、アンニュイなドキュメンタリー調の一枚。

- **比率:** 3:4
- **固定ルール:** 参照画像を人物のすべての根拠にし、レタッチ的な美化を一切かけない。緩みは着古しの結果としてのみ表現する。
- **差し替え変数:** 季節の小道具（スイカ、蚊取り線香、麦茶、団扇）、縁側の建材と庭の植生、キャミソールと短パンの色。
- **見せ場:** 軒の風鈴の短冊だけが振れ、画面の他の垂直線はすべて静止している。

## 設計メモ

- **緩みの根拠:** カットによる開きではなく、洗いを重ねて生地がへたり、襟ぐりの張りと肩紐が伸びた結果として書く。デザインで開けると狙いが変わる。
- **胸の保持:** 参照から外れやすい部位なので、拡大・縮小・持ち上げの禁止を明示し、衣装側も `unstructured and unpadded` にして補整が入らないようにする。
- **髪:** プロンプト側で髪型・長さ・色に一切触れない。「保持せよ」と書いた直後に状態（下ろす、後れ毛など）を指定すると、そちらが上書きとして効く。
- **構図:** 真横の全身から寄せて、顔から腿までのミディアムショットにしている。引きにすると胸と胴体の面積が小さくなり、参照との一致が落ちる。
- **背面化の防止:** ヒップラインを強調しようとカメラを肩より後ろへ回すと背中向きになる。この構図では取り下げ、`Never shoot from behind the subject` で固定する。
- **文字数:** 約4,000字。5,000字以内に収めている。

```text
An unretouched documentary-style photograph of the person from the reference image, shot on a full-frame camera with an 85mm prime.

Reference lock: infer and preserve apparent age, gender presentation, ancestry, face, hair, skin tone and texture, body shape and lines, height, and proportions exclusively from the reference. This includes the whole torso: chest and bust size, shape and position, shoulder width, waist, hips, limb thickness. Never beautify, age-shift, slim, idealize, or alter the chest in any way. Use the softened neckline and fitted shorts only if the reference is unambiguously adult; otherwise keep the neckline at the collarbone and use a straight-cut mid-thigh short. The shorts stay fully opaque with no underwear visible.

Scene: the engawa veranda of an old Japanese house in late July, seen from the garden. Weathered timber posts and paper shoji screens fill the background, an open doorway showing a dim room beyond. A glass wind chime with a paper strip hangs from the eaves into the upper-left corner at about head height. The rim of a white enamel tray of cut watermelon enters the lower-right corner. Summer greenery presses in at the left edge. The boards are unevenly worn, with real grain and scuffs.

Pose: the subject sits on the veranda edge in clean side profile, the front of the body facing out across the garden. One knee is drawn up with that bare foot on the boards; the other leg hangs down off the veranda. One hand brings a wedge of watermelon to the mouth from the side of the face, that elbow near the raised knee; the other arm reaches back with the palm flat on the boards behind the hip, so the torso stays upright and open and nothing crosses in front of the chest. The gaze goes out across the garden, away from the camera; the expression is languid and unposed, caught mid-bite.

Outfit: a much-loved everyday camisole in sand-ivory cotton jersey, clearly old and washed many times. The knit has gone soft and limp, the bound neckline has lost its tension and now sits lower and looser than it was made to, and the thin straps have stretched slack with wear, though both stay properly on the shoulders. The color is unevenly faded, the hem curls, and the creases are settled in. Fully opaque, unstructured and unpadded, with no shaping or support, so it simply follows the reference body. Slate-gray cotton-linen shorts, equally well-worn and soft, close-cut with the hem high on the thigh, drawstring untied, creased from sitting.

Hero visual: every vertical holds perfectly still, the timber posts, the shoji rails, the chime's cord, and the paper strip beneath the chime is the only thing in the photograph caught mid-swing, hanging just off plumb.

Camera and framing: a medium shot from the garden at seated shoulder height, level, square to the subject's profile. The frame runs from just above the head to mid-thigh, so the face, both shoulders, the full torso, the waist, the seated hip and the upper thighs fill it. Crop below the knee. Never shoot from behind the subject; the front of the torso and the profile of the face must both read. Never frame between the legs.

Lighting: available light only, overcast-bright midday summer. Soft daylight off the open garden, the veranda interior in deep natural shade behind the subject, cool green fill from the grass, a warm return off the timber. No studio light, no rim light, no artificial fill.

Realism: real optical behavior throughout. Moderate depth of field near f/2.8 with the shoji and greenery gently soft, focus on the face, mild vignetting, faint chromatic fringing, natural sensor grain in the shadows, slightly clipped speculars on the glass chime and enamel tray. No skin smoothing, no airbrushing, no retouching. Fabric drapes under real gravity; the worn jersey folds softly with no crispness or stiffness.

Format: 3:4 vertical. A candid photograph, not a render or illustration. No CGI look, no plastic skin, no HDR glow, no sharpening halos, no beauty filter.
```
