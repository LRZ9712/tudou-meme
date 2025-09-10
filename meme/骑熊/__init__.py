from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def qixiong(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((110, 110)).circle()  # 确保生成透明背景的圆形
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height)
    locs = [
        [101, 29, 45, 48],
        [99, 31, 45, 48],
        [98, 41, 45, 48],
        [98, 44, 45, 48],
        [98, 53, 45, 48],
        [102, 46, 45, 48],
        [99, 46, 45, 48],
        [102, 39, 45, 48],
        [102, 31, 45, 48],
        [99, 31, 45, 48],
        [99, 30, 45, 48],
        [98, 34, 45, 48],
        [97, 40, 45, 48],
        [99, 46, 45, 48],
        [99, 51, 45, 48],
        [98, 49, 45, 48],
        [99, 41, 45, 48],
        [103, 34, 45, 48],
        [101, 31, 45, 48],
        [103, 30, 45, 48],
        [97, 33, 45, 48],
        [97, 35, 45, 48],
        [98, 43, 45, 48],
        [100, 46, 45, 48],
        [100, 47, 45, 48],
        [101, 45, 45, 48],
        [99, 38, 45, 48],
        [99, 31, 45, 48],
        [98, 27, 45, 48],
        [99, 31, 45, 48],
        [101, 35, 45, 48],
        [101, 39, 45, 48],
        [101, 46, 45, 48],
        [101, 48, 45, 48],
        [101, 45, 45, 48],
        [102, 41, 45, 48],
        [104, 31, 45, 48],
        [104, 33, 45, 48],
        [104, 33, 45, 48],
        [104, 34, 45, 48],
        [104, 36, 45, 48],
        [104, 46, 45, 48],
        [106, 46, 45, 48]
        [106, 46, 45, 48]
    ]
    
    for i in range(len(locs)):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 如果该帧有位置信息，则贴上圆形头像
        pos = locs[i]
        if pos:  # 跳过为null的帧
            avatar_size = (pos[2], pos[3])
            avatar_pos = (pos[0], pos[1])
            avatar_img = avatar.resize(avatar_size)
            frame.paste(avatar_img, avatar_pos, alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "qixiong",
    qixiong,
    min_images=1,
    max_images=1,
    keywords=["骑熊"],
    date_created=datetime(2025, 9, 8),
    date_modified=datetime(2025, 9, 8),
)