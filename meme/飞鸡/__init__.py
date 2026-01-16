from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme

img_dir = Path(__file__).parent / "images"

def feiji(images: list[BuildImage], texts, args):
    # 检查图片数量
    if len(images) < 2:
        raise ValueError("飞鸡模板需要至少2张图片")
    
    # 加载模板图片
    frame = BuildImage.open(img_dir / "0.png")
    
    # 处理第一个头像：转换为圆形透明PNG
    avatar1 = images[0].convert("RGBA")
    avatar1 = avatar1.resize((160, 160)).circle()  # 先调整基础尺寸
    
    # 处理第二个头像：可能是方形或圆形（根据数据没有指定round:true）
    avatar2 = images[1].convert("RGBA")
    avatar2 = avatar2.resize((160, 160))  # 先调整基础尺寸
    
    # 第一个头像位置：圆形头像
    x1, y1, width1, height1 = 259, 266, 149, 149
    avatar1_resized = avatar1.resize((width1, height1))
    frame.paste(avatar1_resized, (x1, y1), alpha=True)
    
    # 第二个头像位置：没有指定圆形，可能是方形
    x2, y2, width2, height2 = 1058, 124, 154, 154
    avatar2_resized = avatar2.resize((width2, height2))
    frame.paste(avatar2_resized, (x2, y2), alpha=True)
    
    return frame.save_jpg()

add_meme(
    "feiji",
    feiji,
    min_images=2,
    max_images=2,
    keywords=["飞鸡"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)