from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def zizuozuo(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((300, 300)).circle()  # 调整基础尺寸以适应大的缩放
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height)
    locs = [
        (162, 93, 74, 74),
        (163, 92, 74, 74),
        (163, 88, 86, 86),
        (163, 90, 86, 86),
        (157, 83, 89, 89),
        (150, 78, 100, 100),
        (145, 91, 100, 100),
        (143, 87, 108, 108),
        (146, 82, 112, 112),
        (147, 82, 117, 117),
        (143, 79, 127, 127),
        (135, 69, 137, 137),
        (130, 69, 143, 143),
        (123, 73, 151, 151),
        (121, 65, 163, 163),
        (122, 59, 168, 168),
        (120, 71, 185, 185),
        (113, 58, 198, 198),
        (101, 45, 215, 215),
        (86, 46, 228, 228),
        (66, 46, 261, 261),
        (67, 33, 271, 271),
        (61, 33, 302, 302),
        (40, 19, 357, 357),
        (0, -78, 413, 388)
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
    "zizuozuo",
    zizuozuo,
    min_images=1,
    max_images=1,
    keywords=["嘬嘬嘬", "嘬"],
    date_created=datetime(2025, 12, 1),
    date_modified=datetime(2025, 12, 1),
)