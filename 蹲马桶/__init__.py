from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def dunmatong(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((300, 300)).circle()  # 调整基础尺寸
    
    frames: list[IMG] = []
    
    # 位置参数 (x, y, width, height)
    locs = [
        (465, 23, 269, 269)  # 只有一个位置
    ]
    
    # 加载模板图片
    frame = BuildImage.open(img_dir / "0.png")
    
    # 在指定位置贴上圆形头像
    x, y, width, height = locs[0]
    avatar_resized = avatar.resize((width, height))
    frame.paste(avatar_resized, (x, y), alpha=True)
    
    # 添加到帧列表
    frames.append(frame.image)
    
    # 保存为单帧GIF格式
    return save_gif(frames, 3.0)  # 3秒的持续时间

add_meme(
    "dunmatong",
    dunmatong,
    min_images=1,
    max_images=1,
    keywords=["蹲马桶"],
    date_created=datetime(2026, 1, 21),
    date_modified=datetime(2026, 1, 21),
)