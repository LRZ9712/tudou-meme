from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def hanbaomaodie(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((120, 120)).circle()  # 调整基础尺寸
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height) - 共6个位置数据
    locs = [
        (49, 49, 102, 73),
        (41, 47, 102, 73),
        (44, 52, 102, 73),
        (39, 49, 102, 73),
        (44, 46, 102, 73),
        (42, 49, 102, 73)
    ]
    
    total_frames = len(locs)  # 一共6帧
    
    for i in range(total_frames):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        x, y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (x, y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.1)  # 稍微调慢一点帧率

add_meme(
    "hanbaomaodie",
    hanbaomaodie,
    min_images=1,
    max_images=1,
    keywords=["汉堡耄耋"],
    date_created=datetime(2025, 12, 25),
    date_modified=datetime(2025, 12, 25),
)