from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_jpg_or_gif

# 图片目录
img_dir = Path(__file__).parent / "images"


def mengbimao(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    """懵逼猫表情模版"""

    # 载入底图
    frame = BuildImage.open(img_dir / "mengbimao.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        # 复制底图
        base = frame.copy()

        # 第一个头像（左边）
        img1 = imgs[0].convert("RGBA").resize((109, 109))
        base.paste(img1, (87, 173), alpha=True, below=True)

        # 如果提供第二张头像
        if len(imgs) > 1:
            img2 = imgs[1].convert("RGBA").resize((105, 104))
            base.paste(img2, (253, 212), alpha=True, below=True)

        return base

    # 支持 jpg/gif 输出
    return make_jpg_or_gif(images, make)


# 注册表情包
add_meme(
    "mengbimao",
    mengbimao,
    min_images=2,
    max_images=2,
    min_texts=0,
    max_texts=0,
    keywords=["懵逼猫", "猫懵了", "猫傻了"],
    date_created=datetime(2025, 11, 11),
    date_modified=datetime(2025, 11, 11),
)
