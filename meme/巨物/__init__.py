from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"


def juwu(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    # 固定尺寸 640x640
    img_w = 640
    img_h = 640

    # 叠加图
    mask = BuildImage.open(img_dir / "0.png").resize((img_w, img_h), keep_ratio=False)

    def make(imgs: list[BuildImage]) -> BuildImage:
        # 头像同样缩放到 640x640
        img = imgs[0].convert("RGBA").resize((img_w, img_h), keep_ratio=False)
        # 叠加图覆盖上去
        img.paste(mask, alpha=True)
        return img

    return make_png_or_gif(images, make)


add_meme(
    "juwu",
    juwu,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["巨物"],
    date_created=datetime(2025, 3, 16),
    date_modified=datetime(2025, 3, 16),
)
