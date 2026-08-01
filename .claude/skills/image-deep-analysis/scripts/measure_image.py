#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pillow"]
# ///
"""画像の客観計測レイヤー（image-deep-analysis スキル用）。

出力はすべて実測値で、推定を含まない。JSON を stdout に書く。
edge_intensity と symmetry は「このスクリプトの固定処理内でのみ比較可能」な相対指標。
"""

import json
import os
import sys

STANDARD_RATIOS = [
    (1, 1), (4, 3), (3, 4), (3, 2), (2, 3), (16, 9), (9, 16),
    (4, 5), (5, 4), (21, 9), (2, 1), (1, 2), (5, 7), (7, 5),
]

EXIF_KEEP = {
    "Make", "Model", "LensModel", "Software", "DateTimeOriginal", "Orientation",
    "FocalLength", "FocalLengthIn35mmFilm", "FNumber", "ExposureTime",
    "ISOSpeedRatings", "PhotographicSensitivity", "ExposureBiasValue",
    "WhiteBalance", "Flash", "MeteringMode", "ExposureProgram",
}


def jsonable(v):
    """EXIF 等の値を JSON 化できる形に丸める。"""
    if isinstance(v, bytes):
        try:
            return v.decode("utf-8", "replace").strip("\x00 ")
        except Exception:
            return None
    if isinstance(v, (tuple, list)):
        return [jsonable(x) for x in v]
    try:
        if hasattr(v, "numerator") and hasattr(v, "denominator"):  # IFDRational
            return float(v)
    except Exception:
        return None
    if isinstance(v, (int, float, str, bool)) or v is None:
        return v
    return str(v)


def nearest_standard_ratio(w, h):
    r = w / h
    best = min(STANDARD_RATIOS, key=lambda t: abs(t[0] / t[1] - r))
    deviation = abs(best[0] / best[1] - r) / r
    return "%d:%d" % best, round(deviation, 4)


def percentile_from_hist(hist, q):
    total = sum(hist)
    if total == 0:
        return None
    target = total * q
    acc = 0
    for i, n in enumerate(hist):
        acc += n
        if acc >= target:
            return i
    return 255


def extract_exif(im, ExifTags):
    exif = im.getexif()
    if not exif:
        return None, False
    merged = {}
    for tag_id, val in exif.items():
        merged[ExifTags.TAGS.get(tag_id, str(tag_id))] = val
    try:
        for tag_id, val in exif.get_ifd(ExifTags.IFD.Exif).items():
            merged[ExifTags.TAGS.get(tag_id, str(tag_id))] = val
    except Exception:
        pass
    gps_present = False
    try:
        gps_present = bool(exif.get_ifd(ExifTags.IFD.GPSInfo))
    except Exception:
        pass
    out = {}
    for name in EXIF_KEEP:
        if name in merged:
            v = jsonable(merged[name])
            if name == "ExposureTime" and isinstance(v, float) and 0 < v < 1:
                v = "1/%d" % round(1 / v)
            out[name] = v
    return (out or None), gps_present


def icc_description(im, io, ImageCms):
    raw = im.info.get("icc_profile")
    if not raw:
        return None
    try:
        prof = ImageCms.ImageCmsProfile(io.BytesIO(raw))
        return (prof.profile.profile_description or "").strip() or "present"
    except Exception:
        return "present"


def main(path):
    try:
        import io
        from PIL import (Image, ImageChops, ImageCms, ImageFilter, ImageOps,
                         ImageStat)
        from PIL import ExifTags
    except ImportError:
        print(json.dumps({"error": "Pillow がありません。`uv run` でこのスクリプトを実行してください。"},
                         ensure_ascii=False))
        return 1
    if not os.path.isfile(path):
        print(json.dumps({"error": "ファイルが見つかりません: %s" % path}, ensure_ascii=False))
        return 1

    out = {
        "tool": "measure_image.py",
        "note": "全て実測値。edge_intensity / symmetry は本スクリプト内でのみ比較可能な相対指標。",
    }
    im = Image.open(path)
    exif_data, gps_present = extract_exif(im, ExifTags)

    out["file"] = {
        "source_file": path,
        "format": im.format,
        "file_size_bytes": os.path.getsize(path),
        "color_mode": im.mode,
        "animated": getattr(im, "n_frames", 1) > 1,
        "dpi": jsonable(im.info.get("dpi")),
    }
    out["icc_profile"] = icc_description(im, io, ImageCms)
    out["exif"] = exif_data
    out["gps_present"] = gps_present

    im = ImageOps.exif_transpose(im)
    w, h = im.size
    ratio_label, ratio_dev = nearest_standard_ratio(w, h)
    out["dimensions"] = {
        "width_px": w,
        "height_px": h,
        "megapixels": round(w * h / 1e6, 2),
        "aspect_ratio_decimal": round(w / h, 4),
        "nearest_standard_ratio": ratio_label,
        "ratio_deviation": ratio_dev,
        "orientation": "square" if w == h else ("landscape" if w > h else "portrait"),
    }

    try:
        rgb = im.convert("RGB")
        out["file"]["has_alpha"] = "A" in im.getbands() or "transparency" in im.info

        big = rgb.copy()
        big.thumbnail((1024, 1024))
        small = rgb.resize((100, 100))
        L = big.convert("L")

        # 輝度
        st = ImageStat.Stat(L)
        hist = L.histogram()
        total = sum(hist)
        out["luminance"] = {
            "mean": round(st.mean[0], 1),
            "median": round(st.median[0], 1),
            "std": round(st.stddev[0], 1),
            "p5": percentile_from_hist(hist, 0.05),
            "p95": percentile_from_hist(hist, 0.95),
            "clipped_shadows_ratio": round(sum(hist[:8]) / total, 4),
            "clipped_highlights_ratio": round(sum(hist[248:]) / total, 4),
        }
        # 3x3 輝度グリッド（行=上→下、値は 0〜1）
        bw, bh = L.size
        grid = []
        for j in range(3):
            row = []
            for i in range(3):
                cell = L.crop((bw * i // 3, bh * j // 3, bw * (i + 1) // 3, bh * (j + 1) // 3))
                row.append(round(ImageStat.Stat(cell).mean[0] / 255, 3))
            grid.append(row)
        out["luminance"]["grid_3x3"] = grid

        # 彩度・色温度傾向
        s_band = big.convert("HSV").split()[1]
        s_stat = ImageStat.Stat(s_band)
        r_mean, g_mean, b_mean = ImageStat.Stat(big).mean[:3]
        colors_info = {
            "saturation": {"mean": round(s_stat.mean[0], 1), "std": round(s_stat.stddev[0], 1)},
            "channel_means_rgb": [round(r_mean, 1), round(g_mean, 1), round(b_mean, 1)],
            "warm_cool_ratio": round(r_mean / b_mean, 3) if b_mean > 0 else None,
        }
        uc = small.getcolors(10000)
        colors_info["unique_colors_approx_100px"] = len(uc) if uc else "10000+"

        # 主要色（メディアンカット 6 色）
        q = small.quantize(colors=6, method=Image.Quantize.MEDIANCUT)
        pal = q.getpalette()
        counts = sorted(q.getcolors(w * h) or [], reverse=True)
        n_px = sum(c for c, _ in counts) or 1
        colors_info["dominant_colors"] = [
            {
                "hex": "#%02x%02x%02x" % tuple(pal[idx * 3: idx * 3 + 3]),
                "rgb": pal[idx * 3: idx * 3 + 3],
                "ratio": round(c / n_px, 3),
            }
            for c, idx in counts[:6]
        ]
        out["colors"] = colors_info

        # エッジ強度（先鋭度の相対指標）
        edges = ImageStat.Stat(L.filter(ImageFilter.FIND_EDGES))
        out["edges"] = {"intensity_mean": round(edges.mean[0], 2),
                        "intensity_std": round(edges.stddev[0], 2)}

        # 対称度（1 に近いほど対称）
        g64 = L.resize((64, 64))
        lr = ImageStat.Stat(ImageChops.difference(g64, g64.transpose(Image.Transpose.FLIP_LEFT_RIGHT)))
        tb = ImageStat.Stat(ImageChops.difference(g64, g64.transpose(Image.Transpose.FLIP_TOP_BOTTOM)))
        out["symmetry"] = {
            "left_right": round(1 - lr.mean[0] / 255, 3),
            "top_bottom": round(1 - tb.mean[0] / 255, 3),
        }
    except Exception as e:
        out["stats_error"] = "%s: %s" % (type(e).__name__, e)

    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "usage: measure_image.py <image_path>"}, ensure_ascii=False))
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
