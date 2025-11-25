from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def nietumao(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((150, 150)).circle()  # 调整基础尺寸
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height)
    locs = [
        (49, 104, 146, 106),
        (48, 105, 146, 106),
        (47, 102, 148, 108),
        (48, 103, 148, 108),
        (48, 102, 148, 108),
        (47, 103, 148, 108),
        (47, 102, 148, 108),
        (49, 99, 148, 108),
        (51, 97, 148, 108),
        (47, 99, 150, 110),
        (46, 99, 150, 110),
        (48, 101, 148, 108),
        (47, 100, 150, 110),
        (49, 100, 146, 107),
        (48, 100, 148, 108),
        (51, 99, 141, 110),
        (52, 100, 145, 112),
        (53, 99, 143, 108),
        (53, 100, 145, 110),
        (53, 99, 145, 110),
        (54, 98, 145, 110),
        (53, 99, 145, 110),
        (53, 99, 147, 112),
        (53, 99, 147, 112),
        (51, 97, 147, 112),
        (52, 97, 141, 112),
        (52, 96, 139, 110),
        (52, 97, 141, 112),
        (54, 96, 141, 112),
        (54, 98, 141, 112),
        (55, 97, 139, 110),
        (56, 95, 141, 112),
        (57, 93, 141, 112),
        (55, 94, 139, 110),
        (52, 98, 141, 112),
        (53, 98, 140, 111),
        (52, 99, 140, 111),
        (52, 100, 140, 111),
        (53, 97, 140, 111),
        (51, 103, 140, 111),
        (51, 104, 140, 111)
    ]
    
    for i in range(len(locs)):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        x, y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (x, y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "nietumao",
    nietumao,
    min_images=1,
    max_images=1,
    keywords=["捏兔帽","捏粉帽"],
    date_created=datetime(2025, 11, 26),
    date_modified=datetime(2025, 11, 26),
)