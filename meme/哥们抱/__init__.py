from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def gemen_hug(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    # 载入底图
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        # 头像尺寸 (w=78, h=71)
        img = imgs[0].convert("RGBA").resize((78, 71))
        # 头像粘贴坐标 (x=87, y=25)
        return frame.copy().paste(img, (87, 25), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


# 注册表情包
add_meme(
    "gemen_hug",
    gemen_hug,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["哥们抱","兄弟抱"],
    date_created=datetime(2025, 11, 6),
    date_modified=datetime(2025, 11, 6),
)
