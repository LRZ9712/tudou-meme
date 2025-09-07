from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def wanhuo(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((110, 110)).circle()  # 确保生成透明背景的圆形
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height)
    locs = [
        (54, 3, 26, 26),
        (56, -2, 30, 30),
        (58, 0, 28, 28),
        (61, 7, 28, 28),
        (59, 4, 31, 31),
        (58, -1, 29, 29),
        (55, 1, 29, 29),
        (50, 3, 29, 29),
        (53, 5, 29, 29),
        (53, 3, 29, 29),
        (56, -2, 29, 29),
        (58, 1, 29, 29),
        (61, 5, 29, 29),
        (61, 4, 28, 28),
        (57, 0, 29, 29),
        (54, 1, 29, 29),
        (50, 1, 31, 31),
        (51, 3, 31, 31),
        (0, 0, 0, 0),  # 这些位置为(0,0,0,0)的帧不添加头像
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0)
    ]
    
    for i in range(40):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 只有在位置参数不为(0,0,0,0)时才添加头像
        pos = locs[i]
        if pos[2] > 0 and pos[3] > 0:  # 宽度和高度都大于0
            avatar_size = (pos[2], pos[3])
            avatar_pos = (pos[0], pos[1])
            avatar_img = avatar.resize(avatar_size)
            
            # 应用凸起滤镜效果
            # 注意：这里需要根据您的库支持情况实现BULGE滤镜
            # 如果库不支持，可以省略此步骤
            frame.paste(avatar_img, avatar_pos, alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "wanhuo",
    wanhuo,
    min_images=1,
    max_images=1,
    keywords=["玩火"],
    date_created=datetime(2025, 9, 6),
    date_modified=datetime(2025, 9, 6),
)