from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def tianpiggu(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((200, 200)).circle()  # 调整基础尺寸以适应大的头像
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height) - 共10个位置数据
    locs = [
        (191, -52, 189, 189),
        (208, -46, 189, 189),
        (183, -68, 189, 189),
        (186, -61, 189, 189),
        (192, -54, 189, 189),
        (178, -65, 189, 189),
        (189, -68, 189, 189),
        (184, -63, 189, 189),
        (184, -61, 189, 189),
        (183, -46, 189, 189)
    ]
    
    total_frames = len(locs)  # 一共10帧
    
    for i in range(total_frames):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        # 注意：y坐标是负数，说明头像在画面顶部之外
        x, y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (x, y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "tianpiggu",
    tianpiggu,
    min_images=1,
    max_images=1,
    keywords=["舔屁股"],
    date_created=datetime(2026, 1, 16),
    date_modified=datetime(2026, 1, 16),
)