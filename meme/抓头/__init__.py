from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def zhuatou(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((100, 100)).circle()  # 调整基础尺寸
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height) - 共22个位置数据
    locs = [
        (27, 160, 73, 58),
        (26, 159, 75, 60),
        (26, 157, 75, 60),
        (26, 146, 75, 72),
        (27, 116, 77, 83),
        (28, 88, 75, 101),
        (28, 91, 75, 100),
        (28, 96, 75, 98),
        (26, 94, 77, 101),
        (28, 97, 75, 98),
        (27, 99, 75, 96),
        (26, 101, 75, 96),
        (28, 98, 75, 96),
        (28, 99, 75, 96),
        (28, 106, 75, 89),
        (31, 106, 75, 89),
        (27, 106, 75, 89),
        (27, 106, 75, 89),
        (27, 103, 75, 89),
        (26, 102, 75, 89),
        (27, 95, 75, 101),
        (27, 99, 75, 97)
    ]
    
    total_frames = len(locs)  # 一共22帧
    
    # 首先需要知道模板图片的尺寸
    # 先加载第一张模板图片来获取尺寸
    first_template = BuildImage.open(img_dir / "0.png")
    template_width, template_height = first_template.size
    
    for i in range(total_frames):
        # 1. 创建一个与模板相同大小的透明背景
        frame = BuildImage.new("RGBA", (template_width, template_height))
        
        # 2. 在底层贴上调整后的头像
        x, y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (x, y), alpha=True)
        
        # 3. 在上层叠加模板图片（模板应该是半透明的）
        template = BuildImage.open(img_dir / f"{i}.png").convert("RGBA")
        frame.paste(template, (0, 0), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "zhuatou",
    zhuatou,
    min_images=1,
    max_images=1,
    keywords=["抓头"],
    date_created=datetime(2026, 1, 6),
    date_modified=datetime(2026, 1, 6),
)