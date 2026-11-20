"""Draw the image that the home page shows for an event with no Foto: a question mark in pixel blocks, on the same grid as a
published meetup photo (100 x 56 blocks, 12 px each, 1200 x 672), in the colours of the dark theme.

Usage:
    uv run --group photo python tools/make_tbc_image.py content/images/eventos/tbc.png
"""
import sys

from PIL import Image, ImageDraw, ImageFont

COLS, ROWS, BLOCK = 100, 56, 12
BG, INK = (22, 21, 20), (240, 160, 112)   # --bg and --link of the dark theme
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

small = Image.new("RGB", (COLS, ROWS), BG)
d = ImageDraw.Draw(small)
d.text((COLS / 2, ROWS / 2), "?", font=ImageFont.truetype(FONT, 46), fill=INK, anchor="mm")
out = small.resize((COLS * BLOCK, ROWS * BLOCK), Image.NEAREST)
if sys.argv[1].lower().endswith(".webp"):
    out.save(sys.argv[1], "WEBP", lossless=True, method=6)
else:
    out.save(sys.argv[1], optimize=True)
print(sys.argv[1])
