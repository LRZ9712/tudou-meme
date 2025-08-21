from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def wudizhen(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA").square().resize((110, 110)).circle()
    frames: list[IMG] = []
    locs = [
        (28, 28, 46, 8),
        (28, 28, 56, 0),
        (28, 28, 63, 6),
        (28, 28, 54, 12),

        
    ]
    for i in range(4):
        frame = BuildImage.open(img_dir / f"{i}.png")
        w, h, x, y = locs[i]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.05)


add_meme(
    "wudizhen",
    wudizhen,
    min_images=1,
    max_images=1,
    keywords=["无敌帧"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)
