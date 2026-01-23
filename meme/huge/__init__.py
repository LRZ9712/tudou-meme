from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import make_jpg_or_gif

# 背景图目录
img_dir = Path(__file__).parent / "images"

def youmei(images: list[BuildImage], texts, args):
    bg_path = img_dir / "0.png"
    if not bg_path.exists():
        raise FileNotFoundError(f"背景图不存在: {bg_path}")
    frame = BuildImage.open(bg_path)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = (
            imgs[0]
            .convert("RGBA")
            .rotate(8, expand=True)  # 逆时针旋转 8 度
            .resize((350, 350), keep_ratio=True)
        )
        return frame.copy().paste(img, (520, 0), alpha=True)

    return make_jpg_or_gif(images, make)

# 注册 meme
add_meme(
    "youmei",
    youmei,
    min_images=1,
    max_images=1,
    keywords=["撅未花", "未花"],
    date_created=datetime(2025, 8, 12),
    date_modified=datetime(2025, 8, 12),
)
