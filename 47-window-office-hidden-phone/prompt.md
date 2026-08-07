# 47. 窓際オフィス・机の下でこっそりスマホ

人物ID用の参照画像、`reference-outfit-pose.jpeg`、`reference-desk-layout.png` を一緒に使用する。人物の顔・髪・肌・体格・身体寸法は人物ID参照だけから保持する。服装参照からは色・素材感・座り姿勢・手元・照明だけを取り入れ、机と窓の位置関係は配置図だけに従う。

- **人物参照:** 生成時に別途添付する人物ID画像
- **服装・姿勢参照:** `reference-outfit-pose.jpeg`
- **机配置参照:** `reference-desk-layout.png`
- **成人判定:** 服装・姿勢参照は明確に成人として読める。人物IDの見た目年齢は参照画像から推定して保持
- **比率:** 3:4 縦
- **構図:** 窓面に対して机の長辺を垂直に配置した窓際の席。頭から太もも上部、モニターを左前景、人物を右側
- **衣装:** 鎖骨の少し下で止まる浅めの中央Vネック。交差するラップ構造を使わない、淡いパウダーブルーのドレープブラウス＋濃紺またはチャコールのハイウエストパンツ
- **動作:** 顔と視線はモニターへ向けたまま、机の下のスマホを片手で操作
- **表情:** 楽しそうで少しいたずらっぽい、自然な口を閉じた笑顔
- **身体保持:** 胸・腰まわりを参照どおり厳密に保持し、ブラウスの張り・折れ・落ち方へ反映

---

## 完成プロンプト

```text
Use case: reference-guided photorealistic scene creation
Asset type: candid Japanese office lifestyle photograph

Input image roles:
- Image 1 is the sole identity reference. Use it for the subject's identity, apparent age, gender presentation, ancestry, face, skin, hair, body shape, height impression, proportions, overall physique, and all physical characteristics including chest and hip shape and fullness.
- Image 2 is the outfit and pose reference supplied with this prompt. Use it only for the pale-blue blouse color and softness, dark tailored trousers, seated working posture, low smartphone hand, mouse hand, and daylight office atmosphere.
- Explicitly ignore Image 2's desk direction, window-to-desk relationship, wrap-front blouse construction, neckline depth, identity, face, hair, skin tone, body dimensions, and physique.
- Image 3 is a strict top-down desk-layout diagram. It is the sole authority for the spatial relationship between the window wall, desk, monitor, and seated subject. Reproduce its 90-degree geometry even when Image 2 shows a different arrangement.
- Do not transfer Image 2's identity, face, hair, skin tone, body dimensions, or physique to the subject. When the two images differ, Image 1 always controls every identity-derived and anatomical characteristic.

Primary request: Create a highly detailed photorealistic candid portrait of the person from Image 1, seated at a bright window-side workstation in a contemporary Japanese office, secretly checking a smartphone below the desk while pretending to work. 3:4 vertical portrait.

Infer apparent age from Image 1 and preserve it. Match Image 1 exactly for gender presentation, ancestry, body shape and lines, height impression, proportions, overall build, skin tone and texture, facial features, hair, and all physical characteristics including chest and hip shape and fullness. Reproduce the natural volume, dimensions, position, projection, and silhouette of the bust and hips exactly as seen in Image 1, kept accurate through the fit, tension, folds, and drape of the clothing.

Preserve the subject's identity and physique faithfully without age-shifting, beautifying, slimming, exaggerating, or reshaping. Never add or hardcode physical features that are not present in Image 1. Do not copy or blend in any identity traits from Image 2.

Anatomy and physique fidelity: The bust and hips must retain the same natural size, fullness, width, forward projection, side projection, apex spacing, and vertical position shown in Image 1. Match both the front-facing volume and the outer side contours. Do not reduce, flatten, conceal, compress, enlarge, exaggerate, or otherwise reinterpret them. Preserve the exact shoulder width, ribcage depth, torso depth, waist-to-hip relationship, limb proportions, and seated body silhouette from Image 1.

The bust sits high and supported on the ribcage, as if wearing a correctly fitted supportive bra: its fullest point is level with the mid-upper arm, roughly at armpit height, with only a short distance between the collarbones and the beginning of the upper curve—never displaced downward toward the waist. This positioning must remain consistent with Image 1 and must not override its actual natural size or shape.

Scene: A bright, contemporary Japanese open-plan office during an ordinary weekday afternoon. The subject is seated at a workstation beside large floor-to-ceiling windows. A softly blurred Japanese cityscape is visible through the glass. Neutral ceiling lights and additional desks recede into the office behind the subject.

Mandatory top-down geometry: Follow Image 3 exactly. In plan view, the window wall is one straight vertical line and the desk is one straight horizontal rectangle joined to it at a 90-degree angle, visually equivalent to “│────”. The desk's short end meets the window side, and its long axis projects from the window into the office interior. The desk and window must never run alongside each other.

The workstation must read as a peninsula desk projecting inward from the glass wall, not as a long counter running beneath or parallel to the windows. Place the large computer monitor toward the window-side end of the desk. Seat the subject at the free office-side end, facing along the desk toward the monitor and window. The monitor is directly in front of the face. Its screen faces the subject and its back faces toward the window-side end.

The workstation also has a slim keyboard, a mouse, restrained office stationery, and a black mesh office chair. Additional desks and a few coworkers remain deeper inside the office, softly blurred and visually secondary. The environment feels genuinely functional and occupied rather than staged.

Pose: The subject is secretly checking a smartphone while maintaining the appearance of working. The upper body stays upright and naturally oriented toward the computer monitor.

One hand rests on and lightly operates the mouse. The other hand holds the smartphone low beside the thigh, completely below the level of the desktop and close to the lap. Keep the entire phone beneath the desk edge, never resting on or rising above the desktop. Its screen faces slightly upward toward the subject, with the thumb paused in the middle of a small scrolling movement.

Keep both arms away from the front of the chest. Nothing crosses, presses against, compresses, or visually obscures the bust. The mouse arm extends naturally to the side, while the phone hand remains low beside the thigh.

Head and gaze: The subject's face, head, and eyes remain directed toward the computer monitor, closely matching the orientation in Image 2. The gaze is visibly focused on the monitor screen as if reading work displayed there. Do not turn the face or eyes toward the camera, window, smartphone, aisle, or coworkers.

The secretive quality comes from the smartphone being kept below the desk and the restrained working posture, not from looking away from the screen. No sideways glance and no direct eye contact with the camera.

Expression: A clearly visible, warm closed-mouth smile with softly lifted cheeks and playful brightness around the eyes. The subject looks genuinely amused by a private message while trying to maintain a normal working expression. The inner thought is: “Nobody noticed, right?” Keep the smile cheerful, relaxed, and slightly mischievous, not nervous, frightened, guilty, forced, or exaggerated.

Outfit: A pale powder-blue long-sleeved office blouse in a soft, fluid, fully opaque fabric, using Image 2 only for approximate color and material softness. Give it a shallow, centered V-shaped neckline. The point of the V ends only slightly below the collarbones at the upper sternum, noticeably shallower and more closed than Image 2. Use two soft collar folds that descend symmetrically toward the center front.

The blouse has a single centered front seam or concealed placket below the V. It is not a wrap blouse, not a surplice blouse, and has no diagonal crossover panel across the chest or waist. No fabric band pulls from one side of the torso to the opposite hip. Keep the neckline office-appropriate, with no deep plunge. Tuck the blouse into dark navy or charcoal high-waisted tailored trousers.

The blouse must not be boxy, stiff, oversized, tent-like, compressive, or tightly stretched flat. Use a supple fluid weave with discreet shaping darts that naturally follows the body. The fabric must form two clearly readable, reference-accurate three-dimensional bust volumes. It travels outward from the upper chest over each natural bust apex, reaches the Image 1-accurate foremost and outermost points, and then falls separately toward the waist. Preserve a visible change of plane from upper chest to bust apex to under-bust and side torso.

Use gentle curved tension lines radiating from the side seams and shaping darts toward the bust apices, plus soft vertical folds falling from the natural outermost points. Keep a small natural valley between the two fabric-covered volumes without creating a deep neckline. The front panel must not bridge in a single flat plane from shoulder to waist, and it must not collapse inward over the chest.

Preserve the exact chest size and silhouette from Image 1 beneath the blouse. In this seated three-quarter view, the Image 1-accurate forward projection, lower curve, and outer side contour must remain visibly legible through normal fit and drape. Do not minimize the chest through loose fabric, diagonal crossover folds, incorrect dart placement, inward pulling, downward displacement, compression, or an unnaturally flat front. Do not enlarge or exaggerate it beyond Image 1.

The tailored trousers follow the Image 1-accurate waist and hip proportions without slimming or enlarging them. Include natural sitting folds around the waist, lap, elbows, and cuffs. The clothing is professional, realistic, fully opaque, and appropriate for a Japanese office.

Do not add jewelry, glasses, an employee badge, or other accessories unless they are already present in Image 1.

Composition: Use Image 2 only for the approximate seated crop and hand positions; do not copy its desk geometry. Follow Image 3 for layout. Place the monitor along the left foreground and the seated subject on the right. Show the subject from the top of the head through the upper thighs.

The window wall forms a strong line along the left-side background. From that window line, the pale-wood desk visibly projects across the frame into the office at 90 degrees. Show enough of the desk's window-side short end and two long edges that the perpendicular relationship is unmistakable. The monitor stands near the window-side end, directly ahead of the subject and aligned with the desk's long axis. Keep the subject's monitor-focused face, unobstructed torso, mouse hand, desk edge, and phone hand beside the thigh visible.

Position the camera at a slightly elevated front three-quarter angle. From this viewpoint, the viewer can see the smartphone beneath the desk edge, although it remains concealed from coworkers seated farther along the office. The placement must be physically convincing.

Camera: Professional documentary-style office photography, 50mm lens at f/2.8, slightly above seated eye level. Sharp focus on the smiling face and upper body, with enough depth of field to keep both hands and the hidden smartphone recognizable. Let distant coworkers, additional monitors, and the cityscape dissolve into natural background blur.

Lighting: Bright diffused daylight enters through the adjacent windows and creates soft side illumination across the face and blouse. Mix it naturally with restrained neutral-white ceiling lights. Preserve realistic skin texture, individual fabric fibers, subtle blouse folds, desk grain, and controlled reflections on the monitor.

Avoid overexposed facial highlights, artificial blue monitor light, dramatic darkness, glamour retouching, or excessive skin smoothing.

The smartphone screen is dim and contains no readable text, recognizable application interface, personal information, notification details, or logos.

Format: 3:4 vertical composition, realistic window-side Japanese office, candid everyday humor, playful secrecy, natural posture and anatomy. In top-down terms the layout reads “window │──── desk,” with a strict 90-degree junction. Both the face and eyes remain focused on the monitor. Strictly preserve Image 1's chest and hip size, width, forward projection, side projection, position, fullness, and overall body proportions.

Avoid: any change to identity, apparent age, facial structure, hair, skin tone, body shape, chest size, chest position, hip size, height impression, or proportions; any transfer of Image 2's identity traits; copying Image 2's desk arrangement; desk parallel to the windows; workstation counter running along the glass; monitor placed beside rather than directly in front of the subject; phone above the desk; face or eyes turned away from the monitor; direct camera eye contact; deep or plunging V-neckline; wrap blouse; surplice blouse; diagonal crossover panel; fabric pulled diagonally across the bust; exaggerated sneaking gesture; chest compression; flattened torso; merged single chest mound; undersized or oversized bust; low-positioned bust; boxy blouse; extra limbs; extra fingers; malformed hands; duplicated devices; readable text; logo; watermark; or UI icon.
```

## 設計メモ

- スマホは天板より完全に下へ置き、同僚からは隠れるがカメラからは手元が読める角度にした。
- 机配置は服装参照から切り離し、上面図 `│────` を示す専用画像だけに従わせる。
- 机の短辺を窓側へ接続し、長辺は窓から室内方向へ90度で伸ばす。窓沿いのカウンター配置は使わない。
- 顔と視線はモニターへ固定し、こっそりした印象は机の下の手元と抑えた姿勢で表現する。
- 笑顔は「私的なメッセージが面白い」という内心から組み立て、罪悪感や大げさな焦りには寄せない。
- Vネックは鎖骨の少し下、胸骨上部で止め、服装・姿勢参照より浅く端正な開きにする。
- 胸を平坦化した主因だった斜めのラップ前合わせを廃止し、中央V＋左右対称の襟折れ＋縦の前中心線へ変更する。
- 胸の前を両腕、小物、モニターで遮らず、左右それぞれの頂点、前方突出、外側輪郭、下側カーブ、ダーツからの張りで人物ID参照の寸法を保持する。
- 服装・姿勢参照の人物特徴は移さず、人物IDは生成時に添付する別画像だけから取得する。
