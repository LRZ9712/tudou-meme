from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def yaozi(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((120, 120)).circle()  # 调整基础尺寸
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height) - 共15个位置数据
    locs = [
        (182, 42, 111, 98),
        (182, 34, 108, 111),
        (167, 53, 108, 112),
        (159, 59, 108, 99),
        (170, 65, 108, 99),
        (176, 53, 108, 113),
        (193, 61, 107, 107),
        (213, 53, 107, 104),
        (241, 54, 107, 107),
        (261, 68, 107, 106),
        (221, 69, 102, 111),
        (199, 62, 107, 104),
        (207, 66, 107, 110),
        (243, 72, 107, 107),
        (174, 75, 109, 117)
    ]
    
    total_frames = len(locs)  # 一共15帧
    
    for i in range(total_frames):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        x, y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        
        # 注意：位置信息中有 angle: 347，但标准方法没有旋转参数
        # 如果需要旋转，可以使用以下代码（取消注释）：
        # avatar_resized = avatar_resized.rotate(347, expand=True)
        
        frame.paste(avatar_resized, (x, y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.08)

add_meme(
    "yaozi",
    yaozi,
    min_images=1,
    max_images=1,
    keywords=["摇子", "大清摇"],
    date_created=datetime(2026, 1, 14),
    date_modified=datetime(2026, 1, 14),
)