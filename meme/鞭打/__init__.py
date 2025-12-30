from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def whip(images: list[BuildImage], texts, args):
    # 第一个头像位置（上方头像）
    avatar1_locs = [
        (70, 11),  # 第一帧
        (68, 15)   # 第二帧
    ]
    avatar1_sizes = [
        (90, 83),  # 第一帧尺寸
        (90, 83)   # 第二帧尺寸
    ]
    
    # 第二个头像位置（下方头像）
    avatar2_locs = [
        (14, 123),  # 第一帧
        (10, 124)   # 第二帧
    ]
    avatar2_sizes = [
        (94, 58),  # 第一帧尺寸
        (94, 58)   # 第二帧尺寸
    ]
    
    # 处理第一个头像（上方）
    avatar1_head = images[0].convert("RGBA").circle()
    
    # 处理第二个头像（下方）
    avatar2_head = images[1].convert("RGBA").circle()
    
    frames: list[IMG] = []
    for i in range(2):  # 2帧动画
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 粘贴第一个头像
        head1_resized = avatar1_head.resize(avatar1_sizes[i], keep_ratio=True)
        frame.paste(head1_resized, avatar1_locs[i], alpha=True)
        
        # 粘贴第二个头像
        head2_resized = avatar2_head.resize(avatar2_sizes[i], keep_ratio=True)
        frame.paste(head2_resized, avatar2_locs[i], alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)


add_meme(
    "whip",
    whip,
    min_images=2,
    max_images=2,
    keywords=["鞭打"],
    date_created=datetime(2025, 12, 31),
    date_modified=datetime(2025, 12, 31),
)