from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def xiaoxiongmaozi(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((130, 130)).circle()
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height) - 共7个位置数据
    locs = [
        (58, 67, 117, 101),
        (56, 68, 117, 101),
        (54, 67, 117, 101),
        (54, 67, 117, 101),
        (58, 70, 107, 92),
        (58, 70, 112, 92),
        (222, -98, 114, 94)
    ]
    
    total_frames = 10  # 总共有10帧
    
    for i in range(total_frames):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 前7帧（0-6）显示头像，第7帧（索引6）之后不显示
        if i < 7:  # 0,1,2,3,4,5,6 显示头像
            x, y, width, height = locs[i]
            avatar_resized = avatar.resize((width, height))
            frame.paste(avatar_resized, (x, y), alpha=True)
        # 第7,8,9帧（索引7,8,9）不显示头像
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.08)

add_meme(
    "xiaoxiongmaozi",
    xiaoxiongmaozi,
    min_images=1,
    max_images=1,
    keywords=["小熊帽子"],
    date_created=datetime(2025, 12, 31),
    date_modified=datetime(2025, 12, 31),
)