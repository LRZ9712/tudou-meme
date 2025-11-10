from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def tangyuanqizhu(images: list[BuildImage], texts, args):
    # 处理头像：转换为圆形透明 PNG
    avatar = images[0].convert("RGBA").resize((80, 80)).circle()

    frames: list[IMG] = []

    # 各帧头像位置信息 (x, y, w, h)
    locs = [
        (31, 154, 74, 74),
        (31, 157, 74, 74),
        (31, 159, 74, 74),
        (37, 164, 76, 76),
        (33, 154, 76, 76),
    ]

    for i, (x, y, w, h) in enumerate(locs):
        # 加载模板帧
        frame = BuildImage.open(img_dir / f"{i}.png")

        # 调整头像大小并粘贴
        face = avatar.resize((w, h))
        frame.paste(face, (x, y), alpha=True)

        frames.append(frame.image)

    # 输出 GIF 动画（0.07 秒一帧，可调节节奏）
    return save_gif(frames, 0.07)


# 注册表情包
add_meme(
    "tangyuanqizhu",
    tangyuanqizhu,
    min_images=1,
    max_images=1,
    keywords=["汤圆骑猪"],
    date_created=datetime(2025, 11, 7),
    date_modified=datetime(2025, 11, 7),
)
