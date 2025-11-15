from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def pinch_egg(images: list[BuildImage], texts, args):
    # 定义两个头像的位置信息 (x, y, w, h)
    avatar1_positions = [
        [90, 171, 26, 31],
        [90, 171, 26, 31],
        [90, 170, 26, 31],
        [91, 169, 26, 31],
        [91, 170, 26, 31],
        [90, 171, 26, 31],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    
    avatar2_positions = [
        [181, 169, 24, 31],
        [182, 170, 24, 29],
        [182, 170, 26, 31],
        [183, 169, 26, 31],
        [182, 170, 26, 31],
        [183, 169, 26, 31],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    
    # 处理第一个头像（圆形，角度358度）
    avatar1 = (
        images[0]
        .convert("RGBA")
        .resize((avatar1_positions[0][2], avatar1_positions[0][3]), keep_ratio=True)
        .circle()
        .rotate(358)
    )
    
    # 处理第二个头像（圆形，角度3度）
    avatar2 = (
        images[1]
        .convert("RGBA")
        .resize((avatar2_positions[0][2], avatar2_positions[0][3]), keep_ratio=True)
        .circle()
        .rotate(3)
    )
    
    frames: list[IMG] = []
    
    for i in range(13):  # 总共13帧
        # 加载背景帧
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 处理第一个头像位置
        pos1 = avatar1_positions[i]
        # 处理第二个头像位置
        pos2 = avatar2_positions[i]
        
        # 粘贴第二个头像（位置2）- 如果不是[0,0,0,0]就粘贴
        if pos2 != [0, 0, 0, 0]:
            frame.paste(avatar2, (pos2[0], pos2[1]), alpha=True)
        
        # 粘贴第一个头像（位置1）- 如果不是[0,0,0,0]就粘贴
        if pos1 != [0, 0, 0, 0]:
            frame.paste(avatar1, (pos1[0], pos1[1]), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)


add_meme(
    "pinch_egg",
    pinch_egg,
    min_images=2,
    max_images=2,
    keywords=["捏鸡蛋"],
    date_created=datetime(2025, 11, 16),
    date_modified=datetime(2025, 11, 16),
)