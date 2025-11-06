from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

# 图片模板所在目录（确保该目录下有 0.png ~ 11.png）
img_dir = Path(__file__).resolve().parent / "images"

def rengshi(images: list[BuildImage], texts, args):
    # 处理头像：转换为圆形透明 PNG
    avatar = images[0].convert("RGBA").circle()

    frames: list[IMG] = []

    # 各帧头像位置 (x, y, w, h)
    locs = [
        (100, 233, 86, 86),
        (92, 235, 86, 86),
        (98, 237, 88, 88),
        (95, 235, 88, 88),
        (76, 166, 86, 86),
        (249, 236, 268, 268),
        (254, 228, 268, 268),
        (250, 233, 268, 268),
        (254, 240, 268, 268),
        (264, 244, 268, 268),
        (267, 244, 268, 268),
        (267, 223, 270, 270),
    ]

    # 生成每一帧
    for i, loc in enumerate(locs):
        frame_path = img_dir / f"{i}.png"
        frame = BuildImage.open(frame_path)

        # 头像大小与位置
        x, y, w, h = loc
        avatar_resized = avatar.resize((w, h))

        # 粘贴头像
        frame.paste(avatar_resized, (x, y), alpha=True)

        # 加入帧列表
        frames.append(frame.image)

    # 导出 GIF（0.08 秒一帧）
    return save_gif(frames, 0.08)

# 注册表情包
add_meme(
    "rengshi",
    rengshi,
    min_images=1,
    max_images=1,
    keywords=["扔屎"],
    date_created=datetime(2025, 11, 6),
    date_modified=datetime(2025, 11, 6),
)
