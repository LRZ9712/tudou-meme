from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def jiumi(images: list[BuildImage], texts, args):
    # 处理用户头像：圆形头像
    avatar = images[0].convert("RGBA").resize((90, 90)).circle()

    frames: list[IMG] = []

    # 各帧头像位置信息 (x, y, w, h)
    locs = [
        (46, 50, 86, 75),
        (46, 52, 86, 75),
        (46, 51, 86, 75),
        (46, 50, 86, 75),
        (44, 50, 88, 77),
        (48, 54, 85, 75),
        (48, 52, 84, 74),
    ]

    for i, (x, y, w, h) in enumerate(locs):
        # 加载对应帧模板图
        frame = BuildImage.open(img_dir / f"{i}.png")

        # 调整头像大小并粘贴上去
        face = avatar.resize((w, h))
        frame.paste(face, (x, y), alpha=True)

        frames.append(frame.image)

    # 保存为 GIF 动图（帧间隔 0.08 秒）
    return save_gif(frames, 0.08)


# 注册到 meme_generator
add_meme(
    "jiumi",
    jiumi,
    min_images=1,
    max_images=1,
    keywords=["揪咪","掐咪咪""揪咪咪"],
    date_created=datetime(2025, 11, 7),
    date_modified=datetime(2025, 11, 7),
)
