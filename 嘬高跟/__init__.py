from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def tianxie(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((70, 70)).circle()  # 调整基础尺寸
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height) - 共2个位置数据
    locs = [
        (102, 117, 61, 61),
        (102, 116, 61, 61)
    ]
    
    total_frames = len(locs)  # 一共2帧
    
    for i in range(total_frames):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        x, y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (x, y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)  # 较慢的帧率，适合舔的动作

add_meme(
    "tianxie",
    tianxie,
    min_images=1,
    max_images=1,
    keywords=["舔鞋","红高跟","嘬高跟","嘬鞋"],
    date_created=datetime(2026, 1, 21),
    date_modified=datetime(2026, 2, 21),
)