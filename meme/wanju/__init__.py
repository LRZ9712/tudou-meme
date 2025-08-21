from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def anmo(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((110, 110)).circle()  # 确保生成透明背景的圆形
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (width, height, x, y)
    locs = [
        (78, 78, 21, 70),  
        (78, 78, 21, 70), 
        (78, 78, 21, 62), 
        (78, 78, 21, 42), 
        (78, 78, 25, 36), 
        (78, 78, 37, 23), 
        (78, 78, 43, 11), 
        (78, 78, 48, 5), 
        (78, 78, 41, 9), 
        (78, 78, 35, 25), 
        (78, 78, 25, 40), 
        (78, 78, 23, 47), 
        (78, 78, 23, 62), 
        (78, 78, 23, 66), 
        (78, 78, 23, 85), 
        (78, 78, 21, 87), 
        (78, 78, 21, 91), 
        (78, 78, 21, 97), 
        (74, 74, 23, 106), 
        (74, 74, 23, 96), 
        (74, 74, 25, 90), 

    ]
    
    for i in range(21):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"按摩 ({i+1}).png")
        
        # 2. 在模板的透明车轮区域贴上圆形头像
        wheel_size = (locs[i][0], locs[i][1])
        wheel_pos = (locs[i][2], locs[i][3])
        wheel_img = avatar.resize(wheel_size)
        frame.paste(wheel_img, wheel_pos, alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "anmo",
    anmo,
    min_images=1,
    max_images=1,
    keywords=["玩具"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)
