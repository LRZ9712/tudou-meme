from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def tuoni(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((80, 80)).circle()  # 调整基础尺寸
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height) - 共14个位置数据
    locs = [
        (25, 10, 70, 70),
        (27, 10, 70, 70),
        (28, 8, 70, 70),
        (28, 8, 70, 70),
        (27, 8, 70, 70),
        (25, 8, 70, 70),
        (28, 8, 70, 70),
        (27, 8, 70, 70),
        (25, 11, 70, 70),
        (25, 10, 70, 70),
        (28, 10, 70, 70),
        (29, 10, 70, 70),
        (28, 10, 70, 70),
        (25, 10, 70, 70)
    ]
    
    total_frames = len(locs)  # 一共14帧
    
    for i in range(total_frames):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        x, y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (x, y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "tuoni",
    tuoni,
    min_images=1,
    max_images=1,
    keywords=["托尼", "tony", "洗头"],
    date_created=datetime(2026, 2, 2),
    date_modified=datetime(2026, 2, 2),
)