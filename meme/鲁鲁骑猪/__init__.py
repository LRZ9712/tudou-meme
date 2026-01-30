from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def lulu_qizhu(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((137, 128)).circle()  # 根据位置信息中的尺寸调整
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height)
    locs = [
        (141, 36, 137, 128),
        (124, 33, 137, 128),
        (118, 31, 137, 128),
        (108, 30, 137, 128),
        (110, 31, 137, 128),
        (100, 33, 137, 128),
        (94, 31, 137, 128),
        (85, 34, 137, 128),
        (65, 38, 137, 128),
        (61, 38, 137, 128),
        (70, 41, 137, 128),
        (68, 36, 137, 128),
        (75, 37, 137, 128),
        (83, 36, 137, 128),
        (88, 36, 137, 128),
        (81, 34, 137, 128),
        (88, 28, 137, 128),
        (87, 31, 137, 128),
        (74, 24, 137, 128),
        (88, 27, 137, 128),
        (88, 37, 137, 128),
        (97, 40, 137, 128),
        (95, 41, 137, 128),
        (97, 40, 137, 128),
        (97, 40, 137, 128),
        (111, 44, 137, 128),
        (110, 41, 137, 128)
    ]
    
    for i in range(len(locs)):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        pos_x, pos_y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (pos_x, pos_y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "lulu_qizhu",
    lulu_qizhu,
    min_images=1,
    max_images=1,
    keywords=["鲁鲁骑猪"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)
