from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def nizhejiah(images: list[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((240, 220), keep_ratio=True)
        return frame.copy().paste(img, (245, 45), alpha=True) 

    return make_jpg_or_gif(images, make)


add_meme(
    "nizhejiah",
    nizhejiah,
    min_images=1,
    max_images=1,
    keywords=["你这家伙","军训"],
    date_created=datetime(2025, 7, 27),
    date_modified=datetime(2025, 7, 27),
)
