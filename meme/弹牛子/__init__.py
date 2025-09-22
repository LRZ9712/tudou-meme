from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def mo_niuzi(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((115, 115)).circle()  # 根据位置信息调整基础大小
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height)
    locs = [
        (88, 81, 113, 113),  # 第1帧
        (88, 82, 115, 115),  # 第2帧
        (86, 83, 113, 113),  # 第3帧
        (86, 82, 115, 115),  # 第4帧
        (85, 82, 115, 115),  # 第5帧
        (86, 82, 113, 113),  # 第6帧
        (86, 84, 113, 113),  # 第7帧
        (87, 84, 113, 113),  # 第8帧
        (87, 82, 115, 115),  # 第9帧
        (90, 86, 115, 115),  # 第10帧
        (94, 86, 115, 115),  # 第11帧
        (92, 85, 115, 115),  # 第12帧
        (86, 82, 115, 115),  # 第13帧
    ]
    
    for i in range(13):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        x, y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (x, y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "mo_niuzi",
    mo_niuzi,
    min_images=1,
    max_images=1,
    keywords=["摸牛子","弹牛子"],
    date_created=datetime(2025, 9, 22),
    date_modified=datetime(2025, 9, 22),
)