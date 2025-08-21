from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.tags import MemeTags
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"

def qi(images: list[BuildImage], texts, args):
    jerry = BuildImage.open(img_dir / "0.png").convert("RGBA")
    
    def make(imgs: list[BuildImage]) -> BuildImage:
        # 处理第一个头像（原逻辑）
        img1 = imgs[0].convert("RGBA").circle().resize((94, 93), keep_ratio=True)
        
        # 新增第二个头像处理（调整尺寸和位置）
        img2 = imgs[1].convert("RGBA").circle().resize((113, 99), keep_ratio=True)  # 尺寸略小
        
        # 创建基础画布
        base = jerry.copy()
        
        # 先贴第二个头像（底层）
        base.paste(img2, (16, 115), below=True)  # 新坐标(80,180)
        
        # 再贴第一个头像（保持原位置）
        base.paste(img1, (138, 6), below=True)
        
        return base

    return make_png_or_gif(images, make)  # 自动支持动/静态图

add_meme(
    "qi",
    qi,
    min_images=2,  # 修改为需要2张图片
    max_images=2,
    keywords=["骑"],
    tags=MemeTags.jerry,
    date_created=datetime(2024, 8, 9),
    date_modified=datetime(2024, 8, 9),
)