from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def lick_cat(images: list[BuildImage], texts, args):
    # 头像位置信息
    avatar_locs = [
        (-8, 72), (-10, 75), (-13, 68), (-6, 83), (-10, 72),
        (-8, 81), (-17, 75), (-19, 80), (-8, 78), (-8, 78)
    ]
    
    # 头像尺寸
    avatar_size = (143, 143)
    
    # 处理头像
    avatar_head = (
        images[0]
        .convert("RGBA")
        .resize(avatar_size, keep_ratio=True)
        .circle()
    )
    
    frames: list[IMG] = []
    for i in range(10):  # 10帧动画
        frame = BuildImage.open(img_dir / f"{i}.png")
        frame.paste(avatar_head, avatar_locs[i], alpha=True)
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)


add_meme(
    "lick_cat",
    lick_cat,
    min_images=1,
    max_images=1,
    keywords=["舔咪", "舔奶子", "舔咪咪"],
    date_created=datetime(2026, 1, 18),
    date_modified=datetime(2026, 1, 18),
)