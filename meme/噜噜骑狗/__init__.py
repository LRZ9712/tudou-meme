from datetime import datetime
from pathlib import Path
from PIL import Image
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def luluqigou(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((110, 110)).circle()  # 调整基础尺寸
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height) - 共29个位置数据
    locs = [
        (237, 176, 102, 102),
        (236, 177, 102, 102),
        (239, 175, 102, 102),
        (234, 179, 102, 102),
        (220, 175, 102, 102),
        (216, 176, 104, 104),
        (217, 171, 104, 104),
        (231, 177, 104, 104),
        (232, 176, 104, 104),
        (245, 178, 104, 104),
        (259, 172, 104, 104),
        (281, 181, 104, 104),
        (290, 175, 104, 104),
        (298, 181, 104, 104),
        (310, 181, 104, 104),
        (314, 177, 104, 104),
        (309, 177, 104, 104),
        (305, 168, 104, 104),
        (296, 170, 104, 104),
        (286, 162, 104, 104),
        (288, 169, 104, 104),
        (283, 160, 104, 104),
        (257, 169, 104, 104),
        (254, 162, 104, 104),
        (260, 168, 104, 104),
        (270, 158, 104, 104),
        (274, 169, 104, 104),
        (275, 160, 104, 104),
        (274, 158, 104, 104)
    ]
    
    total_frames = len(locs)  # 一共29帧
    
    for i in range(total_frames):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定位置贴上圆形头像
        x, y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        
        # 应用旋转效果（angle: 2 表示顺时针旋转2度）
        # 注意：数据中angle是2度，表示轻微顺时针旋转
        avatar_resized = avatar_resized.rotate(-2, expand=True, resample=Image.BICUBIC)
        
        frame.paste(avatar_resized, (x, y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)  # 快速帧率，模拟快速骑行

add_meme(
    "luluqigou",
    luluqigou,
    min_images=1,
    max_images=1,
    keywords=["噜噜骑狗"],
    date_created=datetime(2026, 1, 23),
    date_modified=datetime(2026, 1, 23),
)