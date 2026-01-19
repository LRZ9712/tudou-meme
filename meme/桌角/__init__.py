from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def zhuojiao(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((110, 110)).circle()  # 调整基础尺寸
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height) - 共17个位置数据
    locs = [
        (37, 47, 102, 102),
        (29, 61, 102, 102),
        (37, 40, 102, 102),
        (38, 46, 92, 92),
        (37, 54, 92, 92),
        (31, 46, 92, 92),
        (30, 54, 92, 92),
        (26, 44, 92, 92),
        (43, 44, 92, 92),
        (40, 37, 92, 92),
        (35, 43, 92, 92),
        (32, 48, 92, 92),
        (35, 38, 92, 92),
        (40, 36, 92, 92),
        (41, 32, 92, 92),
        (36, 43, 92, 92),
        (31, 42, 92, 92)
    ]
    
    total_frames = len(locs)  # 一共17帧
    
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
    "zhuojiao",
    zhuojiao,
    min_images=1,
    max_images=1,
    keywords=["桌角"],
    date_created=datetime(2026, 1, 19),
    date_modified=datetime(2026, 1, 19),
)