from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def maodielanqiu(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA").square().circle()
    frames: list[IMG] = []
    locs = [
        (1, 27, 14, 14),  # 车轮位置1
        (1, 27, 14, 14),  # 车轮位置2
        (2, 26, 14, 14),  # 车轮位置3
        (2, 30, 14, 14),  # 车轮位置4
        (2, 34, 14, 14),  # 车轮位置5
        (2, 33, 14, 14),  # 车轮位置6
        (2, 29, 14, 14),  # 车轮位置7
        (2, 28, 14, 14),  # 车轮位置8
        (2, 27, 14, 14),  # 车轮位置9
        (2, 33, 14, 14),  # 车轮位置10
        (2, 34, 14, 14),  # 车轮位置11
        (2, 31, 14, 14),  # 车轮位置12
        (2, 28, 14, 14),  # 车轮位置13
        (6, 30, 12, 12),  # 车轮位置14
        (16, 37, 10, 10),  # 车轮位置15
        (25, 36, 10, 10),  # 车轮位置16
        (33, 29, 10, 10),  # 车轮位置17
        (37, 24, 10, 10),  # 车轮位置18
        (32, 29, 10, 10),  # 车轮位置19
        (24, 37, 10, 10),  # 车轮位置20
        (16, 37, 10, 10),  # 车轮位置21
        (5, 29, 13, 13),  # 车轮位置22
    ]

    for i in range(22):
        frame = BuildImage.open(img_dir / f"maodie ({i+1}).png")
        x, y, w, h = locs[i]
        # 动态调整头像大小以匹配当前帧的显示区域
        current_img = img.resize((w, h))
        frame.paste(current_img, (x, y), below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.05)


add_meme(
    "maodielanqiu",
    maodielanqiu,
    min_images=1,
    max_images=1,
    keywords=["耄耋篮球"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)