from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def gejiji(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((47, 47)).circle()  # 根据位置信息调整大小
    
    frames: list[IMG] = []
    
    # 位置信息：每个元组包含 (x, y, width, height)
    # 从您提供的JSON中提取的位置数据
    locs = [
        (104, 20, 44, 44), (101, 18, 42, 42), (98, 14, 46, 46), (97, 12, 47, 47),
        (95, 8, 47, 47), (92, 4, 47, 47), (90, 1, 47, 47), (90, 1, 47, 47),
        (90, 1, 47, 47), (89, 0, 47, 47), (89, -1, 47, 47), (88, 0, 47, 47),
        (89, 0, 47, 47), (90, 0, 47, 47), (91, 1, 47, 47), (91, 1, 47, 47),
        (92, 5, 47, 47), (95, 6, 47, 47), (95, 8, 47, 47), (96, 10, 47, 47),
        (96, 15, 47, 47), (96, 20, 47, 47), (96, 20, 47, 47), (96, 20, 47, 47),
        (96, 19, 47, 47), (98, 20, 47, 47), (97, 21, 47, 47), (96, 20, 47, 47),
        (95, 20, 47, 47), (97, 20, 47, 47), (95, 21, 47, 47), (95, 21, 47, 47),
        (94, 21, 47, 47), (98, 23, 47, 47), (100, 23, 47, 47), (102, 22, 47, 47),
        (103, 22, 47, 47), (104, 20, 47, 47), (104, 20, 47, 47), (104, 20, 47, 47),
        (102, 20, 47, 47)
    ]
    
    # 检查是否有对应数量的帧图片
    for i in range(len(locs)):
        try:
            # 1. 加载模板作为底层
            frame = BuildImage.open(img_dir / f"{i}.png")
        except FileNotFoundError:
            # 如果图片文件不存在，创建一个空白帧（用于测试）
            frame = BuildImage.new("RGBA", (200, 200), (255, 255, 255, 0))
        
        # 2. 在指定位置贴上圆形头像
        pos = locs[i]
        # 使用位置信息中的宽高调整头像大小
        avatar_resized = avatar.resize((pos[2], pos[3]))
        frame.paste(avatar_resized, (pos[0], pos[1]), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "gejiji",
    gejiji,
    min_images=1,
    max_images=1,
    keywords=["割鸡鸡", "割jj"],
    date_created=datetime(2025, 9, 26),
    date_modified=datetime(2025, 9, 26),
)