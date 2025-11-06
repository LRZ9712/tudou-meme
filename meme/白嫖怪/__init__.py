from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme

img_dir = Path(__file__).parent / "images"

def baipiaoguai(images: list[BuildImage], texts, args):
    # 处理头像：转换为圆形透明 PNG
    avatar = images[0].convert("RGBA").resize((94, 94)).circle()

    # 加载模板背景
    frame = BuildImage.open(img_dir / "0.png")  # 模板文件为 0.png

    # 头像位置参数 (x, y, w, h)
    x, y, w, h = 67, 17, 94, 94

    # 调整头像大小并粘贴到背景上
    avatar_resized = avatar.resize((w, h))
    frame.paste(avatar_resized, (x, y), alpha=True)

    # 返回生成的图片
    return frame.save_jpg()

# 注册表情包
add_meme(
    "baipiaoguai",
    baipiaoguai,
    min_images=1,
    max_images=1,
    keywords=["白嫖怪"],
    date_created=datetime(2025, 11, 6),
    date_modified=datetime(2025, 11, 6),
)
