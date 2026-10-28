#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
GAMELIST_WALL = ROOT / "assets" / "gamelist_wall"
FALLBACK_WALL = ROOT / "assets" / "wall"
OUT = ROOT / "assets" / "video_gamelist_gradient"

# Video mode gamelist: x=.015, width=.305 -> right edge=.320.
# Fade the final 5% of screen width into the exact underlying backdrop.
X0 = 0.270
X1 = 0.320
Y0 = 0.160
Y1_NORMAL = 0.960
Y1_HELP = 0.880

SUPPORTED = {".png", ".jpg", ".jpeg"}
PRIORITY = {".png": 0, ".jpg": 1, ".jpeg": 2}


def collect_sources():
    # Prefer the actual Details/Video gamelist_wall. If a system has no
    # gamelist_wall image, fall back to its normal wall image.
    sources = {}
    for folder_rank, folder in enumerate((GAMELIST_WALL, FALLBACK_WALL)):
        if not folder.exists():
            continue
        for path in folder.iterdir():
            if not path.is_file() or path.suffix.lower() not in SUPPORTED:
                continue
            stem = path.stem
            rank = (folder_rank, PRIORITY[path.suffix.lower()])
            existing = sources.get(stem)
            if existing is None or rank < existing[0]:
                sources[stem] = (rank, path)
    return {stem: value[1] for stem, value in sources.items()}


def alpha_mask(width, height):
    # Smoothstep alpha ramp: transparent at the left, fully opaque at right.
    vals = []
    for x in range(width):
        t = x / (width - 1) if width > 1 else 1.0
        t = t * t * (3.0 - 2.0 * t)
        vals.append(round(255 * t))
    row = bytes(vals)
    mask = Image.frombytes("L", (width, 1), row)
    return mask.resize((width, height))


def make_strip(source, y1, dest):
    with Image.open(source) as img:
        img = img.convert("RGB")
        w, h = img.size
        left = max(0, min(w - 1, round(w * X0)))
        right = max(left + 1, min(w, round(w * X1)))
        top = max(0, min(h - 1, round(h * Y0)))
        bottom = max(top + 1, min(h, round(h * y1)))
        crop = img.crop((left, top, right, bottom)).convert("RGBA")
        crop.putalpha(alpha_mask(crop.width, crop.height))
        crop.save(dest, "PNG", optimize=True)


def write_theme_xml():
    globals_xml = '''<?xml version="1.0"?>
<theme>
  <formatVersion>7</formatVersion>
  <include>./globals_video_base.xml</include>

  <!-- Backdrop-matched right-edge fade for the narrower Video gamelist. -->
  <view name="video" extra="true">
    <image name="video_gamelist_fade" extra="true" ifHelpPrompts="false">
      <pos>0.27 0.16</pos>
      <size>0.05 0.80</size>
      <origin>0 0</origin>
      <zIndex>7.5</zIndex>
      <path>./assets/video_gamelist_gradient/${system.theme}.png</path>
    </image>
    <image name="video_gamelist_fade" extra="true" ifHelpPrompts="true">
      <pos>0.27 0.16</pos>
      <size>0.05 0.72</size>
      <origin>0 0</origin>
      <zIndex>7.5</zIndex>
      <path>./assets/video_gamelist_gradient/${system.theme}_help.png</path>
    </image>
  </view>
</theme>
'''
    globals_gl_xml = globals_xml.replace(
        "./globals_video_base.xml", "./globalsGL_video_base.xml"
    ).replace(
        "./assets/video_gamelist_gradient/", "./../assets/video_gamelist_gradient/"
    )
    (ROOT / "inc" / "globals.xml").write_text(globals_xml, encoding="utf-8")
    (ROOT / "inc" / "globalsGL.xml").write_text(globals_gl_xml, encoding="utf-8")

    tools = ROOT / "tools" / "theme.xml"
    text = tools.read_text(encoding="utf-8")
    text = text.replace(
        '<image name="video_media_border">\n      <visible>false</visible>\n    </image>',
        '<image name="video_gamelist_fade">\n      <visible>false</visible>\n    </image>'
    )
    tools.write_text(text, encoding="utf-8")


def main():
    sources = collect_sources()
    if not sources:
        raise SystemExit("No backdrop images found")

    OUT.mkdir(parents=True, exist_ok=True)
    # Ensure reruns cannot leave obsolete generated strips behind.
    for old in OUT.glob("*.png"):
        old.unlink()

    for stem, source in sorted(sources.items()):
        make_strip(source, Y1_NORMAL, OUT / f"{stem}.png")
        make_strip(source, Y1_HELP, OUT / f"{stem}_help.png")

    write_theme_xml()
    print(f"Generated {len(sources)} system fades ({len(sources) * 2} PNG files)")
    print(f"Fade geometry: x={X0:.3f}-{X1:.3f}, normal y={Y0:.3f}-{Y1_NORMAL:.3f}, help y={Y0:.3f}-{Y1_HELP:.3f}")


if __name__ == "__main__":
    main()
