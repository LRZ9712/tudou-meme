from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def maomimobai(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((50, 50)).circle()  # 调整基础尺寸
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height)
    locs = [
        (19, 134, 39, 39),
        (24, 136, 39, 39),
        (32, 144, 35, 32)
    ]
    
    for i in range(len(locs)):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        x, y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (x, y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)  # 稍微调慢一点帧率，让膜拜动作更明显

add_meme(
    "maomimobai",
    maomimobai,
    min_images=1,
    max_images=1,
    keywords=["猫咪膜拜", "膜拜猫咪"],
    date_created=datetime(2025, 12, 1),
    date_modified=datetime(2025, 12, 1),
)