from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def tiaosheng(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((76, 53)).circle()  # 根据位置信息中的尺寸调整
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height)
    locs = [
        (267, 160, 76, 53),
        (268, 163, 76, 53),
        (268, 159, 76, 53),
        (268, 160, 76, 53),
        (268, 160, 73, 53),
        (268, 160, 74, 53),
        (270, 163, 74, 53),
        (268, 168, 74, 53),
        (268, 167, 74, 55),
        (268, 159, 74, 55),
        (268, 160, 74, 55),
        (268, 163, 74, 55),
        (267, 153, 74, 55),
        (268, 107, 74, 55),
        (270, 95, 74, 55),
        (270, 86, 74, 55),
        (267, 76, 74, 55),
        (267, 78, 74, 55),
        (267, 80, 74, 55),
        (270, 90, 74, 59),
        (270, 102, 74, 59),
        (270, 139, 74, 59),
        (271, 167, 74, 59)
    ]
    
    for i in range(23):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在模板的指定位置贴上圆形头像
        pos_x, pos_y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (pos_x, pos_y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "tiaosheng",
    tiaosheng,
    min_images=1,
    max_images=1,
    keywords=["跳绳"],
    date_created=datetime(2025, 10, 20),
    date_modified=datetime(2025, 10, 20),
)