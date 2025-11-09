from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def painitou(images: list[BuildImage], texts, args):
    # 处理头像：转换为圆形透明 PNG
    avatar = images[0].convert("RGBA").resize((130, 110)).circle()

    frames: list[IMG] = []

    # 各帧头像位置信息 (x, y, w, h)
    locs = [
        (98, 296, 125, 102),
        (97, 295, 125, 102),
        (96, 297, 125, 102),
        (98, 297, 125, 102),
        (95, 297, 125, 102),
    ]

    for i, (x, y, w, h) in enumerate(locs):
        # 加载模板帧
        frame = BuildImage.open(img_dir / f"{i}.png")

        # 调整头像大小
        face = avatar.resize((w, h))

        # 直接贴上（不透明）
        frame.paste(face, (x, y), alpha=True)

        frames.append(frame.image)

    # 生成 GIF 动画
    return save_gif(frames, 0.08)


# 注册表情包
add_meme(
    "painitou",
    painitou,
    min_images=1,
    max_images=1,
    keywords=["拍你头"],
    date_created=datetime(2025, 11, 7),
    date_modified=datetime(2025, 11, 7),
)
