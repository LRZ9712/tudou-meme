from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def pao(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((110, 110)).circle()  # 确保生成透明背景的圆形
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (width, height, x, y)
    locs = [
        (24, 24, 12, 7),  # 车轮位置1
        (24, 24, 12, 8),  # 车轮位置1
        (24, 24, 12, 7),  # 车轮位置1
        (24, 24, 12, 8),  # 车轮位置1
        (24, 24, 12, 7),  # 车轮位置1
        (24, 24, 12, 8),  # 车轮位置1
        (24, 24, 12, 7),  # 车轮位置1
        (24, 24, 12, 8),  # 车轮位置1


    ]
    
    for i in range(8):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在模板的透明车轮区域贴上圆形头像
        wheel_size = (locs[i][0], locs[i][1])
        wheel_pos = (locs[i][2], locs[i][3])
        wheel_img = avatar.resize(wheel_size)
        frame.paste(wheel_img, wheel_pos, alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "pao",
    pao,
    min_images=1,
    max_images=1,
    keywords=["跑"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)
