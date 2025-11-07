from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def tiaopi(images: list[BuildImage], texts, args):
    # 第一位头像（攻击者）
    avatar1_pos = [
        (129, 78, 78, 54),
        (127, 78, 80, 56),
        (127, 78, 80, 56),
        (128, 78, 80, 56),
        (128, 77, 80, 56),
        (128, 77, 80, 56),
        (127, 78, 80, 56),
        (138, 92, 80, 38),
        (130, 59, 69, 57),
        (110, 42, 76, 66),
        (100, 49, 81, 62),
        (97, 48, 81, 62),
        (99, 47, 81, 62),
        (98, 48, 81, 62),
        (99, 47, 81, 62),
        (99, 48, 81, 62),
        (99, 48, 81, 62),
        (104, 42, 79, 61),
        (114, 36, 87, 68),
        (130, 58, 70, 59),
    ]

    # 第二位头像（被劈者）
    avatar2_pos = [
        (60, 97, 83, 60),
        (61, 98, 85, 62),
        (61, 98, 85, 63),
        (61, 98, 85, 63),
        (61, 98, 85, 63),
        (61, 97, 85, 63),
        (59, 97, 85, 63),
        (62, 98, 81, 53),
        (60, 98, 83, 54),
        (58, 98, 81, 54),
        (47, 105, 123, 58),
        (47, 105, 123, 58),
        (48, 106, 123, 58),
        (50, 106, 123, 58),
        (48, 106, 123, 58),
        (50, 107, 123, 58),
        (46, 106, 123, 58),
        (52, 92, 129, 67),
        (59, 97, 84, 59),
        (58, 98, 84, 59),
    ]

    # 头像处理为 BuildImage
    attacker = (
        images[0]
        .convert("RGBA")
        .resize((100, 100), keep_ratio=True)
        .circle()
    )
    target = (
        images[1]
        .convert("RGBA")
        .resize((100, 100), keep_ratio=True)
        .circle()
    )

    frames = []
    for i in range(len(avatar1_pos)):
        # 模板帧
        top_frame = BuildImage.open(img_dir / f"{i}.png").convert("RGBA")

        # 创建底层透明画布
        base = BuildImage.new("RGBA", top_frame.size, (0, 0, 0, 0))

        # 放头像（底层）
        x1, y1, w1, h1 = avatar1_pos[i]
        x2, y2, w2, h2 = avatar2_pos[i]

        base.paste(attacker.resize((w1, h1), keep_ratio=False), (x1, y1), alpha=True)
        base.paste(target.resize((w2, h2), keep_ratio=False), (x2, y2), alpha=True)

        # 模板覆盖在上层
        base.paste(top_frame, (0, 0), alpha=True)

        frames.append(base.image)

    return save_gif(frames, 0.05)


add_meme(
    "tiaopi",
    tiaopi,
    min_images=2,
    max_images=2,
    keywords=["跳劈", "敲死你"],
    date_created=datetime(2025, 11, 7),
    date_modified=datetime(2025, 11, 7),
)
