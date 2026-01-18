from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def quanzidong(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((40, 40)).circle()  # 调整基础尺寸以适应小的头像
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height) - 共8个位置数据
    locs = [
        (71, 5, 31, 31),
        (68, 4, 31, 31),
        (72, 5, 31, 31),
        (69, 4, 31, 31),
        (72, 4, 31, 31),
        (68, 4, 31, 31),
        (72, 4, 31, 31),
        (68, 3, 31, 31)
    ]
    
    total_frames = len(locs)  # 一共8帧
    
    for i in range(total_frames):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        x, y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (x, y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)  # 快速帧率，模拟机械振动

add_meme(
    "quanzidong",
    quanzidong,
    min_images=1,
    max_images=1,
    keywords=["全自动", "自动杯子"],
    date_created=datetime(2026, 1, 18),
    date_modified=datetime(2026, 1, 18),
)