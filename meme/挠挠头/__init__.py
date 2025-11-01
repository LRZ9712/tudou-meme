from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def naonao_tou(images: list[BuildImage], texts, args):
    # 处理用户头像
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((92, 92)).circle()  # 使用最大尺寸作为基础
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height)
    locs = [
        (75, 72, 90, 90),
        (74, 72, 90, 90),
        (75, 71, 90, 90),
        (75, 71, 90, 90),
        (74, 72, 90, 90),
        (75, 73, 90, 90),
        (73, 72, 90, 90),
        (76, 71, 90, 90),
        (70, 72, 92, 92),
        (70, 72, 92, 92),
        (72, 71, 90, 90),
        (74, 71, 90, 90),
        (72, 72, 90, 90),
        (73, 74, 90, 90),
        (72, 74, 90, 90)
    ]
    
    for i in range(len(locs)):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        pos_x, pos_y, width, height = locs[i]
        # 根据每帧的尺寸调整头像
        avatar_frame = avatar.resize((width, height))
        frame.paste(avatar_frame, (pos_x, pos_y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "naonao_tou",
    naonao_tou,
    min_images=1,
    max_images=1,
    keywords=["挠挠头"],
    date_created=datetime(2025, 1, 1),
    date_modified=datetime(2025, 1, 1),
)