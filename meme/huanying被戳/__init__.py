from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def huanyingchuo(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA").square().resize((110, 110)).circle()
    frames: list[IMG] = []
    locs = [
        (42, 42, 92, 106),
        (42, 42, 117, 91),
        (42, 42, 129, 105),
        (42, 42, 125, 105),


    ]
    for i in range(4):
        frame = BuildImage.open(img_dir / f"{i}.png")
        w, h, x, y = locs[i]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.02)


add_meme(
    "huanyingchuo",
    huanyingchuo,
    min_images=1,
    max_images=1,
    keywords=["欢迎新人"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)