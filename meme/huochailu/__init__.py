from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def huochailu(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA").square().resize((110, 110)).circle()
    frames: list[IMG] = []
    locs = [
        (155, 155, 63, 28),
        (155, 155, 63, 28),
        (155, 155, 83, 38),
        (155, 155, 94, 40),
        (155, 155, 97, 45),
        (155, 155, 97, 45),
    ]
    for i in range(6):
        frame = BuildImage.open(img_dir / f"{i}.png")
        w, h, x, y = locs[i]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.05)


add_meme(
    "huochailu",
    huochailu,
    min_images=1,
    max_images=1,
    keywords=["火柴撸"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)