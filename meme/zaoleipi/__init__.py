from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def zaoleipi(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((110, 110)).circle()  # 确保生成透明背景的圆形
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (width, height, x, y)
    locs = [
        (112, 111, 133, 81),  # 车轮位置1
        (127, 129, 129, 71),  # 车轮位置1
        (127, 129, 129, 71),  # 车轮位置1
        (127, 129, 129, 71),  # 车轮位置1
        (127, 129, 149, 81),  # 车轮位置1
        (127, 129, 152, 81),  # 车轮位置1
        (127, 129, 154, 81),  # 车轮位置1
        (127, 129, 164, 81),  # 车轮位置1
        (127, 129, 164, 121),  # 车轮位置1
        (127, 129, 154, 121),  # 车轮位置1
        (127, 129, 104, 66),  # 车轮位置1
        (127, 129, 60, 36),  # 车轮位置1
        (127, 129, 60, 36),  # 车轮位置1
        (127, 129, 60, 36),  # 车轮位置1
        (92, 92, 61, 45),  # 车轮位置1
        (92, 92, 66, 50),  # 车轮位置1
        (92, 92, 69, 90),  # 车轮位置1
        (92, 92, 66, 120),  # 车轮位置1
        (92, 92, 60, 130),  # 车轮位置1
        (92, 92, 60, 140),  # 车轮位置1
       (98, 104, 52, 144),  # 车轮位置1
       (103, 100, 31, 128),  # 车轮位置1
       (103, 100, 41, 128),  # 车轮位置1
       (103, 100, 51, 122),  # 车轮位置1
       (103, 100, 61, 112),  # 车轮位置1
       (108, 104, 74, 100),  # 车轮位置1
       (116, 110, 73, 102),  # 车轮位置1
       (123, 116, 66, 95),  # 车轮位置1
       (137, 129, 58, 88),  # 车轮位置1
       (146, 135, 50, 82),  # 车轮位置1
       (158, 142, 38, 82),  # 车轮位置1
       (166, 152, 30, 76),  # 车轮位置1
       (181, 168, 4, 66),  # 车轮位置1
       (173, 168, 0, 70),  # 车轮位置1
       (182, 177, -50, 80),  # 车轮位置1
       (182, 177, -50, 80),  # 车轮位置1
       (167, 178, -18, 98),  # 车轮位置1
       (192, 177, 0, 91),  # 车轮位置1
       (192, 177, 19, 75),  # 车轮位置1
       (192, 177, 27, 62),  # 车轮位置1
       (192, 177, 27, 62),  # 车轮位置1
       (192, 177, 27, 62),  # 车轮位置1
       (192, 177, 27, 62),  # 车轮位置1
       (192, 177, 27, 62),  # 车轮位置1
       (192, 177, 27, 62),  # 车轮位置1
       (192, 177, 27, 62),  # 车轮位置1
       (192, 177, 35, 45),  # 车轮位置1
       (192, 177, 27, 53),  # 车轮位置1
       (192, 177, 27, 53),  # 车轮位置1





        
    ]
    
    for i in range(49):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"zaoleipi ({i+1}).png")
        
        # 2. 在模板的透明车轮区域贴上圆形头像
        wheel_size = (locs[i][0], locs[i][1])
        wheel_pos = (locs[i][2], locs[i][3])
        wheel_img = avatar.resize(wheel_size)
        frame.paste(wheel_img, wheel_pos, alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "zaoleipi",
    zaoleipi,
    min_images=1,
    max_images=1,
    keywords=["遭雷劈","电"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)
