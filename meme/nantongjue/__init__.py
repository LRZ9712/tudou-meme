from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def nantongjue(images: list[BuildImage], texts, args):
    self_locs = [  (168, 66), (175, 66), (176, 67), (176, 67), (176, 67), (175, 65),
        (176, 68), (176, 68), (175, 66), (175, 66), (175, 67), (175, 68),
        (175, 68), (175, 69), (175, 69), (175, 67)]
    user_locs = [  (42, 237), (44, 234), (44, 234), (43, 231), (43, 229), (46, 228),
        (46, 228), (43, 227), (43, 227), (43, 227), (46, 227), (46, 229),
        (46, 229), (46, 229), (46, 229), (46, 229)]
    self_head = (
        images[0]
        .convert("RGBA")
        .resize((137, 151), keep_ratio=True)
        .circle()
        .rotate(1)
    )
    user_head = (
        images[1]
        .convert("RGBA")
        .resize((133, 143), keep_ratio=True)
        .circle()
        .rotate(30)
    )
    frames: list[IMG] = []
    for i in range(16):
        frame = BuildImage.open(img_dir / f"{i}.png")
        frame.paste(user_head, user_locs[i], alpha=True)
        frame.paste(self_head, self_locs[i], alpha=True)
        frames.append(frame.image)
    return save_gif(frames, 0.02)


add_meme(
    "nantongjue",
    nantongjue,
    min_images=2,
    max_images=2,
    keywords=["男同撅","猥琐撅"],
    date_created=datetime(2023, 3, 7),
    date_modified=datetime(2023, 3, 7),
)
