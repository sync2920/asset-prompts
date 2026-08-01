# 解析 JSON スキーマ

出力はこの構造の単一オブジェクト。キーの並びもこの順を保つ。

## 共通規約

- **measured**: スクリプト / EXIF 由来の実測値。そのまま転記し、推定で上書きしない。
- それ以外の値はすべて推定。各セクション末尾の `confidence`（0〜1）に、
  そのセクション全体の確度を書く。個別の値が特に不確かなときは値を
  `{"value": ..., "confidence": 0.4}` の形にしてよい。
- 分からない・画面に手がかりがない → **null**（配列なら `[]`）。埋めるための創作をしない。
- 座標は左上原点・正規化（0〜1）。`bbox` は `[x, y, w, h]`。角度は度、色温度は K、距離は m。
- enum として例示した語彙は代表値。ぴったり合う語が無ければ自由記述でよい
  （機械可読性より正確さを優先する）。

## スキーマ本体

```jsonc
{
  "meta": {                            // ── 画像そのものの素性
    "source_file": "パス",             // measured
    "format": "PNG",                   // measured
    "file_size_bytes": 0,              // measured
    "width_px": 0, "height_px": 0,     // measured
    "megapixels": 0.0,                 // measured
    "aspect_ratio": "3:4",             // measured（最近傍の標準比と偏差はスクリプト出力を使う）
    "orientation": "portrait|landscape|square",
    "medium": "photo|illustration|anime|3dcg|painting|composite|screenshot|document|other",
    "ai_generated_likelihood": 0.0,    // 0〜1。根拠は quality.ai_artifacts に書く
    "color_mode": "RGB",               // measured
    "has_alpha": false,                // measured
    "icc_profile": "sRGB など or null", // measured
    "exif_present": false,             // measured
    "gps_present": false,              // measured（座標は出さない）
    "confidence": 0.0
  },

  "geometry": {                        // ── 幾何学: 構図・遠近法・カメラ
    "composition": {
      "layout_scheme": "rule_of_thirds|golden_ratio|center|symmetric|diagonal|frame_in_frame|triangle|none|…",
      "main_subject_position": [0.0, 0.0],   // 主被写体の重心
      "main_subject_screen_coverage": 0.0,   // 画面占有率 0〜1
      "symmetry": {
        "left_right_measured": 0.0,    // measured（0〜1、スクリプトの相対指標）
        "top_bottom_measured": 0.0,    // measured
        "perceived": "対称性の目視所見"
      },
      "balance": "視覚的重心がどこにあり、何と釣り合っているか",
      "leading_lines": [ {"type": "手すり/視線/影 など", "from": [0,0], "to": [1,1]} ],
      "negative_space": "余白の位置と役割",
      "framing": "何がどう画面端で切れているか（意図的なクロップ判断を含む）",
      "luminance_grid_3x3": [[0,0,0],[0,0,0],[0,0,0]]  // measured。明るさの空間配分
    },
    "perspective": {
      "type": "one_point|two_point|three_point|isometric|atmospheric_only|flat|none",
      "horizon_y": 0.0,                // 地平線/水平線の縦位置（画面外なら推定値+その旨、不明なら null）
      "vanishing_points": [ [0.0, 0.0] ],  // 画面外は 0〜1 の範囲外の値で表現してよい
      "depth_cues": ["overlap", "relative_size", "atmospheric", "texture_gradient", "dof"]
    },
    "camera_geometry": {
      "camera_height": "ground|low|waist|eye|high|elevated|aerial",
      "pitch_deg": 0.0,                // 上向き +
      "roll_deg": 0.0,                 // 水平からの傾き
      "subject_distance_m": 0.0,
      "estimated_focal_length_mm_35mm_equiv": 0.0  // EXIF があればそれが正（photography 側に記載）
    },
    "notable_relationships": ["黄金比・正三角形など、見つかった幾何的一致"],
    "confidence": 0.0
  },

  "physics": {                         // ── 物理: 光・光学・材質
    "light": {
      "sources": [ {
        "type": "sun|sky|window|overcast|lamp|flash|screen|fire|mixed|…",
        "direction": "画面に対する方位（例: 右上・逆光・7時方向）＋可能なら仰角",
        "elevation_deg": 0.0,          // 光源の高度角（影の長さから逆算）
        "quality": "hard|soft|mixed",
        "color_temp_k": 0,
        "relative_intensity": "key に対する比の所見",
        "role": "key|fill|rim|ambient|practical"
      } ],
      "shadows": {
        "present": true,
        "direction": "落ちる向き",
        "length_relative": "被写体高に対する長さ感（→光源高度の根拠）",
        "softness": "hard|soft と半影の幅",
        "density": "濃度と、遮蔽陰影(AO)の見え方",
        "consistency": "全影が同一光源系で説明できるか。矛盾があれば具体的に"
      },
      "highlights_reflections": {
        "speculars": ["鏡面ハイライトの位置と、それが示す光源情報"],
        "reflective_surfaces": [ {"surface": "水面など", "reflects": "何が映っているか", "fidelity": "鏡面〜拡散"} ],
        "fresnel_effects": "視射角で反射が強まる面の観察（水面・ガラス・肌の縁 等）"
      },
      "atmosphere": {
        "haze": "有無と距離による濃度変化",
        "volumetric_light": "光条・ゴッドレイの有無",
        "scattering": "空の色や遠景の青さ等、散乱の見え（レイリー/ミー的所見）",
        "time_signature": "この光が示す時刻の物理的根拠（色温度・影の長さ・高度角）"
      },
      "confidence": 0.0
    },
    "optics": {
      "depth_of_field": {
        "extent": "shallow|moderate|deep|pan_focus",
        "focus_plane": "何にピントが合っているか",
        "falloff": "前ボケ/後ボケの立ち上がり方",
        "estimated_aperture_f": 0.0
      },
      "bokeh": { "shape": "円形/多角形/口径食(cat-eye)", "character": "なめらか/騒がしい/渦巻き 等" },
      "motion_blur": { "present": false, "of": "subject|camera", "direction": null },
      "aberrations": {
        "chromatic": "色収差の有無と場所",
        "vignetting": "周辺減光",
        "distortion": "barrel|pincushion|none",
        "flare_ghost": "フレア・ゴーストの有無"
      },
      "rendering_naturalness": "光学系として自然か。生成/合成を疑う光学的違和感があれば具体的に",
      "confidence": 0.0
    },
    "materials": [                     // 主要な面ごとに 1 エントリ（3〜8 個目安）
      {
        "surface": "どの面・物体か",
        "material_guess": "木/金属/綿/水/肌 など",
        "roughness": 0.0,              // 0=鏡面 〜 1=完全拡散 の感覚値
        "metallic": false,
        "translucency": "透過・透け感の有無と質",
        "subsurface_scattering": "肌・葉・布などの内部散乱の見え",
        "wetness": "濡れ・艶の有無",
        "texture": "表面の質感の記述"
      }
    ],
    "materials_confidence": 0.0
  },

  "color": {                           // ── 色彩
    "dominant_colors": [ {"hex": "#000000", "ratio": 0.0, "name_ja": "呼び名"} ],  // hex/ratio は measured
    "palette_scheme": "monochromatic|analogous|complementary|split_complementary|triadic|neutral_plus_accent|none",
    "temperature": { "overall": "warm|cool|mixed|neutral", "warm_cool_ratio_measured": 0.0 },
    "white_balance_impression": "正確/意図的に転がしている 等",
    "brightness": {                    // measured を転記
      "mean": 0, "p5": 0, "p95": 0,
      "clipped_shadows_ratio": 0.0, "clipped_highlights_ratio": 0.0,
      "key": "high_key|mid|low_key"
    },
    "saturation": { "mean_measured": 0, "character": "全体の彩度設計の所見" },
    "contrast": { "global_std_measured": 0, "local": "マイクロコントラスト・質感強調の所見" },
    "grading": "カラーグレーディングの傾向（teal&orange / faded film / クリーン無加工 等）",
    "confidence": 0.0
  },

  "subjects": {                        // ── 被写体
    "inventory": [                     // 目立つ順。人物もここに 1 行入れる
      { "label": "何か", "category": "person|animal|plant|object|structure|text|…",
        "bbox": [0,0,0,0], "screen_coverage": 0.0, "state": "状態・動作" }
    ],
    "people": [                        // 人物 1 人につき 1 エントリ。実在人物の特定はしない
      {
        "apparent_age_range": "見た目の印象としての年齢帯（例: 20代前半）",
        "apparent_gender_expression": "見た目の性別表現",
        "pose": { "overall": "全身の姿勢", "head": "頭部の向き", "gaze": "視線の先", "hands": "手の位置と仕草" },
        "expression": "表情",
        "hair": { "length": null, "style": null, "color": null, "motion": "風・重力との関係" },
        "clothing": [ {"item": "服", "color": null, "material_guess": null, "fit": "シルエット・着こなし"} ],
        "accessories": []
      }
    ],
    "text_in_image": [ {"content": "写り込んだ文字", "language": null, "role": "看板/字幕/透かし"} ],
    "focal_hierarchy": ["視線が向かう順に要素を列挙"],
    "confidence": 0.0
  },

  "environment": {                     // ── 環境・舞台
    "setting": "indoor|outdoor|mixed",
    "location_type": "場所の種別（駅ホーム・浴室・桟橋 等）",
    "region_culture_cues": ["地域・文化圏を示す手がかり（日本語の看板、車両の型 等）"],
    "time_of_day": "早朝|午前|正午|午後|golden_hour|薄明|夜|不明",
    "season": null,
    "weather": null,
    "temperature_impression": "暑さ寒さが画面のどこに表れているか",
    "confidence": 0.0
  },

  "photography": {                     // ── 撮影技法（EXIF があれば source: "exif"）
    "shot_type": "extreme_closeup|closeup|bust|waist|knee|full|wide|extreme_wide",
    "angle": "eye_level|low|high|dutch|overhead|…",
    "settings": {
      "source": "exif|estimated",
      "focal_length_mm": null, "aperture_f": null, "shutter_s": null, "iso": null
    },
    "lighting_technique": "自然光/窓光/ストロボ/ミックス などの手法所見",
    "style_lineage": "ポートレート/ストリート/風景/商業/シネマティック 等の系譜",
    "confidence": 0.0
  },

  "style_aesthetics": {                // ── 様式・美学
    "genre": "作品ジャンルの位置づけ",
    "mood_keywords": ["雰囲気を表す語を 3〜6 個"],
    "stylistic_references": ["〜風という傾向の指摘（実在作家の断定はしない）"],
    "post_processing": ["レタッチ・加工の痕跡"],
    "era_or_trend": "時代感・流行との対応",
    "confidence": 0.0
  },

  "quality": {                         // ── 技術品質
    "sharpness": { "edge_intensity_measured": 0.0, "perceived": "解像感の所見（どこが甘い/立っている）" },
    "noise": "輝度/色ノイズ・粒状感の所見",
    "compression_artifacts": "ブロックノイズ・バンディング等",
    "ai_artifacts": ["生成画像特有の破綻（指・文字・パターン反復・物理矛盾）を具体的に。無ければ []"],
    "overall_technical_grade": "S|A|B|C|D",
    "grade_rationale": "その等級の理由",
    "confidence": 0.0
  },

  "semantics": {                       // ── 意味論
    "one_line_summary": "一文要約",
    "narrative": "何が起きているか。直前・直後に何がありそうか",
    "intended_use_impression": "SNS投稿/広告/記録/アート など、作られた目的の推定",
    "emotional_read": "見る者に生じる感情の読み",
    "confidence": 0.0
  },

  "confidence_notes": {                // ── 解析全体のメタ情報
    "overall_confidence": 0.0,
    "measured_layer_available": true,  // スクリプトが実行できたか
    "major_uncertainties": ["特に自信のない判断とその理由"],
    "out_of_scope": ["この画像からは原理的に判断できないこと"]
  }
}
```

## セクション別の記入基準

- **geometry.perspective**: 消失点は画面内の平行線群（床板・手すり・線路など）を 2 本以上
  延長して求める。1 本しか根拠がなければ null にして depth_cues 側に書く。
- **physics.light**: 影の方向と長さ → 光源の方位と高度角、ハイライトの締まり → 硬さ、
  白い面の色かぶり → 色温度、の順で逆算する。「昼っぽい」ではなく根拠を書く。
- **physics.materials**: 迷ったら「ハイライトの形（鏡面性）」「色の均一さ（粗さ）」
  「縁の透け（透過・SSS）」の 3 点で判断する。
- **color**: hex と比率はスクリプトの実測を使い、name_ja と設計意図の解釈だけを目視で足す。
- **quality.ai_artifacts**: meta.ai_generated_likelihood の根拠はすべてここに置く。
  「AIっぽい」ではなく、画面内の座標・部位を指して書く。
- **semantics**: ここだけは解釈の分野。ただし narrative は画面内の証拠
  （濡れた髪、鞄の持ち方、時計の針）から立てた仮説として書く。
