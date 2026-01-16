from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def feiji(images: list[BuildImage], texts, args):
    # 检查图片数量
    if len(images) < 2:
        raise ValueError("飞鸡模板需要至少2张图片")
    
    # 由于是单帧图片，但需要保存为GIF格式
    # 创建单帧列表
    frames: list[IMG] = []
    
    # 加载模板图片（确保模板本身是透明背景的）
    frame = BuildImage.open(img_dir / "0.png").convert("RGBA")
    
    # 处理第一个头像：转换为圆形透明PNG
    avatar1 = images[0].convert("RGBA")
    avatar1 = avatar1.resize((160, 160)).circle()
    
    # 处理第二个头像：根据数据没有指定round:true，可能是方形
    avatar2 = images[1].convert("RGBA")
    avatar2 = avatar2.resize((160, 160))
    
    # 第一个头像位置：圆形头像 (259, 266, 149, 149)
    x1, y1, width1, height1 = 259, 266, 149, 149
    avatar1_resized = avatar1.resize((width1, height1))
    frame.paste(avatar1_resized, (x1, y1), alpha=True)
    
    # 第二个头像位置：没有指定圆形，可能是方形 (1058, 124, 154, 154)
    x2, y2, width2, height2 = 1058, 124, 154, 154
    avatar2_resized = avatar2.resize((width2, height2))
    frame.paste(avatar2_resized, (x2, y2), alpha=True)
    
    # 添加到帧列表
    frames.append(frame.image)
    
    # 保存为单帧GIF（GIF支持透明背景）
    return save_gif(frames, 1.0)  # 1秒的持续时间

add_meme(
    "feiji",
    feiji,
    min_images=2,
    max_images=2,
    keywords=["飞鸡"],
    date_created=datetime(2026, 1, 16),
    date_modified=datetime(2026, 1, 16),
)