from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def mengqin(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((66, 66)).circle()
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height)
    locs = [
        (37, 121, 66, 66),
        None,
        None,
        (34, 124, 66, 66)
    ]
    
    # 记录上一帧的有效位置信息
    last_valid_loc = locs[0]  # 第一帧肯定有有效位置
    
    for i in range(len(locs)):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 获取当前帧的位置信息，如果是null则使用上一帧的位置
        current_loc = locs[i]
        if current_loc is None:
            current_loc = last_valid_loc
        else:
            last_valid_loc = current_loc
        
        # 3. 贴上圆形头像
        pos_x, pos_y, width, height = current_loc
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (pos_x, pos_y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "mengqin",
    mengqin,
    min_images=1,
    max_images=1,
    keywords=["猛亲", "仓鼠亲", "一顿亲"],
    date_created=datetime(2025, 10, 26),
    date_modified=datetime(2025, 10, 26),
)