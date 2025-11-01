from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def tiaowu_mao(images: list[BuildImage], texts, args):
    # 处理用户头像
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((169, 138)).circle()  # 使用最大尺寸作为基础
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height)
    locs = [
        (162, 109, 169, 126),
        (167, 109, 169, 126),
        (181, 110, 169, 126),
        (188, 118, 154, 126),
        (183, 114, 154, 126),
        (175, 115, 154, 126),
        (156, 112, 168, 138),
        (144, 104, 168, 138),
        (132, 109, 168, 138),
        (146, 109, 168, 138),
        (65, 80, 168, 138),
        (65, 81, 168, 138),
        (60, 85, 168, 138),
        (68, 88, 168, 138),
        (69, 81, 168, 138),
        (64, 81, 168, 138),
        (67, 79, 168, 138),
        (65, 86, 168, 138),
        (62, 86, 168, 138),
        (67, 80, 168, 138),
        (65, 86, 168, 138),
        (69, 81, 168, 138),
        (70, 81, 168, 138),
        (141, 79, 168, 138),
        (148, 86, 168, 138),
        (146, 88, 168, 138),
        (139, 86, 168, 138),
        (134, 88, 168, 138),
        (141, 88, 168, 138),
        (142, 83, 168, 138)
    ]
    
    for i in range(len(locs)):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        pos_x, pos_y, width, height = locs[i]
        # 根据每帧的尺寸调整头像
        avatar_frame = avatar.resize((width, height))
        frame.paste(avatar_frame, (pos_x, pos_y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "tiaowu_mao",
    tiaowu_mao,
    min_images=1,
    max_images=1,
    keywords=["跳舞猫", "跳舞", "猫猫舞", "舞蹈猫"],
    date_created=datetime(2025, 11, 1),
    date_modified=datetime(2023, 11, 1),
)