"""Make the published version of a meetup photo: one treatment for the whole image, so nobody is recognisable at a glance.

The steps, the same for every pixel (nothing is treated apart: not the faces, not the background):
1. Scale the photo to 1600 px wide (16 px per block for 100 columns).
2. Blur it with a Gaussian blur (6 px by default).
3. Cut the height to whole blocks and average each 16 x 16 block into one colour (a grid of 100 columns).
4. Scale each block to 12 x 12 px, so the file can be shared as it is (1200 px wide for 100 columns).

The original photo must stay outside the repository: the script refuses an input path inside it. Pillow writes no
metadata to the output (no EXIF, no GPS, no camera data).

Usage (make photo does the same):
    uv run --group photo python tools/pixelate_photo.py ORIGINAL content/images/eventos/NN-slug.png

The defaults are the settings of Aporia #01 (README, "Publish a meetup photo"). Another value is fine for a later photo,
with --blur and --cols; say which in the commit message.
"""
import argparse
import os
import sys

from PIL import Image, ImageFilter, ImageOps

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# The defaults: the settings chosen for Aporia #01 (2026-11-20). Change a photo's settings with --blur and --cols.
DEFAULT_BLUR = 6    # Gaussian blur in px, measured on the photo scaled to WORK_WIDTH
DEFAULT_COLS = 100  # blocks across: 16 px blocks at WORK_WIDTH, 100 x 56 for a 16:9 photo
WORK_WIDTH = 1600   # the width the blur and the blocks are measured at
SHARE_BLOCK = 12    # px per block in the output file: 1200 px wide for 100 columns


def pixelate(src, blur, cols):
    block = WORK_WIDTH // cols
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")   # a phone photo stores its rotation in EXIF; apply it, or the output lies on its side
        height = round(WORK_WIDTH * im.height / im.width)
        im = im.resize((WORK_WIDTH, height), Image.LANCZOS)
    if blur:
        im = im.filter(ImageFilter.GaussianBlur(blur))
    rows = height // block
    small = im.crop((0, 0, cols * block, rows * block)).resize((cols, rows), Image.BOX)
    return small.resize((cols * SHARE_BLOCK, rows * SHARE_BLOCK), Image.NEAREST)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("original", help="the original photo, outside the repository")
    parser.add_argument("output", help="the published file, for example content/images/eventos/02-slug.png (PNG, so link previews can read it)")
    parser.add_argument("--blur", type=float, default=DEFAULT_BLUR, help=f"Gaussian blur in px at {WORK_WIDTH} px wide (default {DEFAULT_BLUR})")
    parser.add_argument("--cols", type=int, default=DEFAULT_COLS, help=f"blocks across (default {DEFAULT_COLS})")
    args = parser.parse_args()

    if os.path.realpath(args.original).startswith(REPO + os.sep):
        sys.exit("The original photo is inside the repository. Move it out first: the repository is public.")
    out = pixelate(args.original, args.blur, args.cols)
    if args.output.lower().endswith(".webp"):
        out.save(args.output, "WEBP", lossless=True, method=6)
    else:
        out.save(args.output, optimize=True)   # PNG: what every link preview reads (WhatsApp does not read WebP)
    print(f"{args.output}: {out.width} x {out.height}, {os.path.getsize(args.output)} bytes, blur {args.blur}, {args.cols} columns. "
          f'In the Markdown: {{: .pixelada width="{out.width}" height="{out.height}" }}')


if __name__ == "__main__":
    main()
