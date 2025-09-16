from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import add_meme

img_dir = Path(__file__).parent / "images"

def huanying(images: list[BuildImage], texts, args):
    # 加载模板图片（带透明通道）
    template = BuildImage.open(img_dir / "0.gif")
    
    # 创建与模板同尺寸的底图
    final_img = BuildImage.new("RGBA", template.size)
    
    # 调整用户图片到模板透明区域的显示尺寸（159x124）
    user_img = (
        images[0]
        .convert("RGBA")
        .resize(
            (150, 122),
            keep_ratio=True,
            inside=False,  # 覆盖模式填充
            direction="center"
        )
    )
    
    # 将用户图片放置在模板下方（位置34,23）
    final_img.paste(user_img, (77, 164))
    
    # 覆盖模板图片（显示模板不透明部分，透出用户图片的透明区域）
    final_img.paste(template, alpha=True)
    
    return final_img.save_jpg()

add_meme(
    "huanying",
    huanying,
    min_images=1,
    max_images=1,
    keywords=["欢迎"],
    date_created=datetime(2022, 3, 10),
    date_modified=datetime(2023, 2, 14),
)
