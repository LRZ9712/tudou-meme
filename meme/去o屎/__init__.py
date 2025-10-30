from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def qushi(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((103, 103)).circle()  # 使用最大尺寸作为基础尺寸
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height) - 共6帧，没有null值
    locs = [
        [69, 80, 98, 98],    # 第0帧
        [66, 69, 103, 103],  # 第1帧
        [70, 61, 101, 101],  # 第2帧
        [71, 80, 96, 96],    # 第3帧
        [71, 76, 97, 97],    # 第4帧
        [70, 64, 103, 103]   # 第5帧
    ]
    
    for i in range(6):  # 总共6帧
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 获取当前帧的位置信息
        pos_x, pos_y, width, height = locs[i]
        
        # 3. 贴上圆形头像
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (pos_x, pos_y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "qushi",
    qushi,
    min_images=1,
    max_images=1,
    keywords=["去o屎"],
    date_created=datetime(2025, 10, 30),
    date_modified=datetime(2025, 10, 30),
)