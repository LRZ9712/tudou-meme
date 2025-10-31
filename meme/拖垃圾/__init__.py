from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def tuo_laji(images: list[BuildImage], texts, args):
    # 处理用户头像
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((136, 128)).circle()  # 基础尺寸，部分帧会调整
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height)
    locs = [
        (288, 180, 136, 128),
        (284, 186, 136, 128),
        (280, 195, 136, 128),
        (273, 195, 136, 128),
        (280, 195, 136, 128),
        (287, 195, 136, 128),
        (291, 192, 136, 128),
        (285, 198, 136, 128),
        (264, 214, 136, 128),
        (245, 202, 136, 128),
        (227, 205, 136, 128),
        (238, 202, 136, 128),
        (242, 205, 136, 128),
        (236, 212, 122, 128),  # 特殊尺寸
        (238, 214, 130, 128),  # 特殊尺寸
        (253, 217, 150, 128),  # 特殊尺寸
        (279, 220, 136, 128),
        (284, 221, 136, 128),
        (276, 223, 136, 128),
        (270, 218, 136, 128),
        (274, 220, 136, 128),
        (274, 232, 136, 128),
        (276, 227, 136, 128),
        (259, 246, 148, 128),  # 特殊尺寸
        (241, 246, 148, 128),  # 特殊尺寸
        (239, 243, 133, 128)   # 特殊尺寸
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
    "tuo_laji",
    tuo_laji,
    min_images=1,
    max_images=1,
    keywords=["拖垃圾", "拖垃圾车", "垃圾车"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)