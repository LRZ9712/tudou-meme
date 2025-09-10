from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def xiongqi(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((110, 110)).circle()  # 确保生成透明背景的圆形
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height)
    locs = [
        [74, 114, 60, 60],
        [74, 111, 60, 60],
        [78, 103, 60, 60],
        [78, 103, 60, 60],
        [76, 101, 60, 60],
        [78, 108, 60, 60],
        [78, 111, 60, 60],
        [78, 113, 60, 60],
        [76, 104, 60, 60],
        [74, 102, 60, 60],
        [74, 104, 60, 60],
        [76, 107, 60, 60],
        [76, 112, 60, 60],
        [79, 114, 60, 60],
        [78, 118, 60, 60],
        [78, 113, 60, 60],
        [78, 109, 60, 60],
        [78, 104, 60, 60],
        [76, 108, 60, 60],
        [74, 110, 60, 60],
        [74, 113, 60, 60],
        [74, 113, 60, 62],
        [74, 113, 60, 62],
        [74, 99, 60, 62],
        [75, 99, 60, 62],
        [75, 103, 60, 62],
        [75, 106, 60, 62],
        [73, 105, 60, 62],
        [73, 104, 60, 62],
        [74, 106, 60, 62],
        [75, 102, 60, 62],
        [75, 108, 60, 62],
        [74, 111, 60, 62],
        [74, 114, 60, 62],
        [75, 109, 60, 62],
        [75, 109, 60, 62],
        [74, 105, 60, 62],
        [72, 103, 60, 62],
        [73, 101, 60, 62],
        [73, 101, 60, 62],
        [74, 102, 60, 62],
        [73, 105, 60, 62]
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
    "xiongqi",
    xiongqi,
    min_images=1,
    max_images=1,
    keywords=["熊骑"],
    date_created=datetime(2025, 9, 8),
    date_modified=datetime(2025, 9, 8),
)