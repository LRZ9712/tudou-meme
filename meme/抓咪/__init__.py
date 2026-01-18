from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def grab_cat(images: list[BuildImage], texts, args):
    # 头像位置信息
    avatar_locs = [
        (27, -5), (25, -8), (29, -2), (37, 8), (32, 2),
        (29, -6), (30, 0), (35, 3), (25, -3), (25, 0),
        (24, -5), (35, 2)
    ]
    
    # 头像尺寸
    avatar_size = (121, 121)
    
    # 处理头像
    avatar_head = (
        images[0]
        .convert("RGBA")
        .resize(avatar_size, keep_ratio=True)
        .circle()
    )
    
    frames: list[IMG] = []
    for i in range(12):  # 12帧动画
        frame = BuildImage.open(img_dir / f"{i}.png")
        frame.paste(avatar_head, avatar_locs[i], alpha=True)
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)


add_meme(
    "grab_cat",
    grab_cat,
    min_images=1,
    max_images=1,
    keywords=["抓咪咪", "抓奶", "抓奶子", "抓咪"],
    date_created=datetime(2026, 1, 18),
    date_modified=datetime(2026, 1, 18),
)