from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def nvtongjue(images: list[BuildImage], texts, args):
    self_locs = [  (207, 41), (207, 41), (209, 41), (216, 41), (223, 47), (223, 52),
        (218, 52), (223, 54), (226, 48), (216, 47), (208, 44), (204, 41),
        (205, 42), (204, 40)]
    user_locs = [  (103, 109), (105, 109), (105, 109), (106, 109), (105, 109), (108, 114),
        (104, 117), (106, 118), (104, 118), (106, 119), (106, 119), (106, 119),
        (106, 119), (106, 119)]
    self_head = (
        images[0]
        .convert("RGBA")
        .resize((106, 119), keep_ratio=True)
        .circle()
        .rotate(1)
    )
    user_head = (
        images[1]
        .convert("RGBA")
        .resize((99, 99), keep_ratio=True)
        .circle()
        .rotate(30)
    )
    frames: list[IMG] = []
    for i in range(14):
        frame = BuildImage.open(img_dir / f"{i}.png")
        frame.paste(user_head, user_locs[i], alpha=True)
        frame.paste(self_head, self_locs[i], alpha=True)
        frames.append(frame.image)
    return save_gif(frames, 0.05)


add_meme(
    "nvtongjue",
    nvtongjue,
    min_images=2,
    max_images=2,
    keywords=["女同撅","姐妹撅"],
    date_created=datetime(2023, 3, 7),
    date_modified=datetime(2023, 3, 7),
)
