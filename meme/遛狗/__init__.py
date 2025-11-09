from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def liugou(images: list[BuildImage], texts, args):
    # 处理头像：圆形透明 PNG
    avatar = images[0].convert("RGBA").resize((70, 70)).circle()

    frames: list[IMG] = []

    # 各帧头像位置参数 (x, y, w, h)
    locs = [
        (9, 169, 64, 64),
        (8, 171, 64, 64),
        (13, 166, 64, 64),
        (8, 171, 64, 64),
        (10, 172, 64, 64),
        (11, 169, 64, 64),
        (12, 169, 64, 64),
        (8, 173, 64, 64),
        (8, 173, 64, 64),
        (10, 171, 64, 64),
        (10, 168, 64, 64),
        (6, 172, 66, 66),
        (8, 174, 63, 63),
        (8, 171, 63, 63),
        (13, 167, 63, 63),
        (8, 171, 63, 63),
    ]

    # 每帧角度（所有为 358°，可以后期个别帧改）
    angle = 358

    for i, (x, y, w, h) in enumerate(locs):
        # 加载模板帧
        frame = BuildImage.open(img_dir / f"{i}.png")

        # 调整头像尺寸和角度
        face = avatar.resize((w, h)).rotate(angle, expand=True)

        # 粘贴到模板上
        frame.paste(face, (x, y), alpha=True)

        frames.append(frame.image)

    # 输出 GIF 动图
    return save_gif(frames, 0.07)


# 注册表情包
add_meme(
    "liugou",
    liugou,
    min_images=1,
    max_images=1,
    keywords=["遛狗"],
    date_created=datetime(2025, 11, 7),
    date_modified=datetime(2025, 11, 7),
)
