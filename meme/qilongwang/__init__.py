from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def qilongwang(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA").square().resize((110, 110)).circle()
    frames: list[IMG] = []
    locs = [
        (33, 33, 64, 3),
        (33, 33, 62, 3),
        (33, 33, 58, 2),       
    ]
    for i in range(3):
        frame = BuildImage.open(img_dir / f"{i}.png")
        w, h, x, y = locs[i]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.05)


add_meme(
    "qilongwang",
    qilongwang,
    min_images=1,
    max_images=1,
    keywords=["骑龙王"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)
