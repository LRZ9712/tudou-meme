from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def huanying(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA").square().resize((110, 110)).circle()
    frames: list[IMG] = []
    locs = [
        (98, 98, 112, 108),  # 车轮位置1
        (98, 98, 122, 117),  # 车轮位置1
        (98, 98, 126, 109),  # 车轮位置1
        (98, 98, 112, 110),  # 车轮位置1
        (98, 98, 110, 118),  # 车轮位置1
        (98, 98, 109, 108),  # 车轮位置1

    ]
    for i in range(6):
        frame = BuildImage.open(img_dir / f"{i}.png")
        w, h, x, y = locs[i]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.05)


add_meme(
    "huanying",
    huanying,
    min_images=1,
    max_images=1,
    keywords=["欢迎新人"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)
