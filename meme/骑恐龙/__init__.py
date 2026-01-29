from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def qikonglong(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((45, 45)).circle()  # 调整基础尺寸
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height) - 共10个位置数据
    locs = [
        (36, 13, 37, 32),
        (36, 14, 36, 31),
        (39, 14, 36, 31),
        (39, 18, 36, 31),
        (37, 19, 36, 31),
        (37, 20, 36, 31),
        (35, 16, 36, 31),
        (34, 17, 36, 31),
        (32, 14, 36, 31),
        (31, 16, 36, 31)
    ]
    
    total_frames = len(locs)  # 一共10帧
    
    for i in range(total_frames):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        x, y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (x, y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "qikonglong",
    qikonglong,
    min_images=1,
    max_images=1,
    keywords=["骑恐龙", "恐龙"],
    date_created=datetime(2026, 1, 22),
    date_modified=datetime(2026, 1, 22),
)