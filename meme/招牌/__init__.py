from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def zhaopai(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((500, 500)).circle()
    
    frames: list[IMG] = []
    
    # 位置参数 (x, y, width, height)
    locs = [
        (-41, 165, 438, 458)
    ]
    
    # 先加载模板图片获取尺寸
    template = BuildImage.open(img_dir / "0.png").convert("RGBA")
    template_width, template_height = template.size
    
    # 1. 创建一个与模板相同大小的透明背景
    frame = BuildImage.new("RGBA", (template_width, template_height))
    
    # 2. 在底层贴上调整后的头像
    x, y, width, height = locs[0]
    avatar_resized = avatar.resize((width, height))
    frame.paste(avatar_resized, (x, y), alpha=True)
    
    # 3. 在上层叠加模板图片（模板应该是半透明的）
    frame.paste(template, (0, 0), alpha=True)
    
    # 添加到帧列表
    frames.append(frame.image)
    
    return save_gif(frames, 5.0)

add_meme(
    "zhaopai",
    zhaopai,
    min_images=1,
    max_images=1,
    keywords=["招牌"],
    date_created=datetime(2026, 1, 19),
    date_modified=datetime(2026, 1, 19),
)