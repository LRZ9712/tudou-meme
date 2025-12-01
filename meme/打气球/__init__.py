from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def daqiqiu(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((100, 100)).circle()  # 调整基础尺寸
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height)
    locs = [
        (91, 165, 12, 12),
        (91, 162, 12, 12),
        (91, 164, 12, 12),
        (93, 158, 15, 15),
        (93, 158, 14, 14),
        (97, 154, 14, 14),
        (96, 154, 14, 14),
        (97, 146, 19, 15),
        (97, 149, 16, 12),
        (96, 140, 27, 21),
        (98, 143, 24, 18),
        (98, 128, 33, 25),
        (100, 131, 30, 23),
        (107, 118, 36, 28),
        (106, 119, 36, 28),
        (108, 108, 40, 30),
        (107, 109, 40, 30),
        (108, 101, 45, 34),
        (108, 102, 45, 34),
        (111, 91, 54, 41),
        (115, 89, 60, 40),
        (115, 88, 72, 38),
        (115, 88, 81, 41),
        (104, 82, 90, 60),
        (107, 82, 90, 60),
        (106, 71, 90, 60),
        (107, 67, 90, 60),
        (107, 65, 90, 60),
        (107, 60, 90, 60),
        (107, 54, 90, 60),
        (106, 49, 90, 60),
        (104, 31, 90, 60),
        (103, 15, 90, 60),
        (105, 11, 96, 55),
        (0, 0, 0, 0),  # 不显示头像的帧
        (0, 0, 0, 0),  # 不显示头像的帧
        (0, 0, 0, 0),  # 不显示头像的帧
        (0, 0, 0, 0)   # 不显示头像的帧
    ]
    
    for i in range(len(locs)):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 检查位置数据是否有效（width和height不为0）
        x, y, width, height = locs[i]
        if width > 0 and height > 0:
            # 在指定位置贴上圆形头像
            avatar_resized = avatar.resize((width, height))
            frame.paste(avatar_resized, (x, y), alpha=True)
        # 如果width和height为0，则不贴头像，直接使用模板
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "daqiqiu",
    daqiqiu,
    min_images=1,
    max_images=1,
    keywords=["打气球"],
    date_created=datetime(2025, 11, 26),
    date_modified=datetime(2025, 11, 26),
)