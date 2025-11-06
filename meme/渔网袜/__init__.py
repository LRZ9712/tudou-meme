from datetime import datetime
from pathlib import Path

from PIL import ImageDraw
from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def yuwangwa(images: list[BuildImage], texts, args):
    # 基础头像圆形化
    base_img = images[0].convert("RGBA").square().resize((83, 83)).circle()

    # 新建带描边头像
    border_size = 5
    bordered_size = base_img.width + border_size * 2
    bordered_img = BuildImage.new("RGBA", (bordered_size, bordered_size), (0, 0, 0, 0))

    # 绘制黑色圆环作为描边
    draw = ImageDraw.Draw(bordered_img.image)
    draw.ellipse(
        (0, 0, bordered_size - 1, bordered_size - 1),
        fill=(0, 0, 0, 255)
    )
    # 在中间贴上头像（实现“内描边”效果）
    bordered_img.paste(base_img, (border_size, border_size), alpha=True)

    frames: list[IMG] = []

    # (x, y, w, h) 每帧位置
    locs = [
        (102, 40, 77, 77),
        (100, 41, 79, 79),
        (101, 41, 79, 79),
        (107, 35, 81, 81),
        (102, 25, 81, 81),
        (93, 22, 81, 81),
        (83, 34, 81, 81),
        (91, 35, 81, 81),
        (91, 33, 81, 81),
        (92, 31, 81, 81),
        (102, 36, 83, 83),
        (103, 36, 83, 83),
        (103, 39, 83, 83),
        (103, 36, 83, 83),
        (103, 35, 83, 83),
        (98, 37, 83, 83),
        (97, 36, 83, 83),
        (98, 38, 83, 83),
        (100, 36, 83, 83),
        (100, 36, 83, 83),
        (100, 38, 83, 83),
    ]

    # 生成 GIF 帧
    for i in range(len(locs)):
        frame = BuildImage.open(img_dir / f"{i}.png")
        x, y, w, h = locs[i]
        avatar = bordered_img.resize((w + border_size * 2, h + border_size * 2))
        frame.paste(avatar, (x - border_size, y - border_size), below=True)
        frames.append(frame.image)

    # 导出 GIF
    return save_gif(frames, 0.05)


# 注册表情包模板
add_meme(
    "yuwangwa",
    yuwangwa,
    min_images=1,
    max_images=1,
    keywords=["渔网袜", "黑丝"],
    date_created=datetime(2025, 11, 6),
    date_modified=datetime(2025, 11, 6),
)
