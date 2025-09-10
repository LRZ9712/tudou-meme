from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def wanshi(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((110, 110)).circle()  # 确保生成透明背景的圆形
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height)
    locs = [
        [98, 84, 101, 74],
        [97, 84, 101, 77],
        [99, 86, 102, 73],
        [96, 87, 103, 74]
    ]
    
    for i in range(4):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在模板的指定位置贴上圆形头像
        pos = locs[i]
        avatar_size = (pos[2], pos[3])
        avatar_pos = (pos[0], pos[1])
        avatar_img = avatar.resize(avatar_size)
        frame.paste(avatar_img, avatar_pos, alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "wanshi",
    wanshi,
    min_images=1,
    max_images=1,
    keywords=["玩屎"],
    date_created=datetime(2025, 9, 8),
    date_modified=datetime(2025, 9, 8),
)