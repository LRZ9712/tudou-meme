from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def chiwoyichui(images: list[BuildImage], texts, args):
    # 处理头像：转换为圆形透明 PNG
    avatar = images[0].convert("RGBA").resize((100, 100)).circle()

    frames: list[IMG] = []

    # 各帧头像位置信息 (x, y, w, h)
    locs = [
        (252, 171, 102, 102),
        (258, 187, 102, 102),
        (257, 180, 102, 102),
        (259, 170, 102, 102),
        (258, 186, 102, 102),
        (256, 176, 102, 102),
        (255, 171, 102, 102),
        None,  # 这里用上一帧的
        (254, 175, 102, 102),
        (254, 167, 102, 102),
        (257, 183, 102, 102),
        (257, 173, 102, 102),
    ]

    last_loc = None  # 用于记录上一帧位置

    for i, loc in enumerate(locs):
        frame = BuildImage.open(img_dir / f"{i}.png")

        # 若当前帧为 None，沿用上一帧的位置
        if loc is None:
            loc = last_loc
        else:
            last_loc = loc  # 更新上一帧记录

        # 解包坐标并粘贴头像
        if loc is not None:
            x, y, w, h = loc
            face = avatar.resize((w, h))
            frame.paste(face, (x, y), alpha=True)

        frames.append(frame.image)

    # 生成 GIF 动画
    return save_gif(frames, 0.07)


# 注册表情包
add_meme(
    "chiwoyichui",
    chiwoyichui,
    min_images=1,
    max_images=1,
    keywords=["吃我一锤"],
    date_created=datetime(2025, 11, 7),
    date_modified=datetime(2025, 11, 7),
)
