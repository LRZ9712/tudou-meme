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
        (112, 111, 133, 81), (127, 129, 129, 71), (127, 129, 129, 71), 
        (127, 129, 129, 71), (127, 129, 149, 81), (127, 129, 152, 81), 
        (127, 129, 154, 81), (127, 129, 164, 81), (127, 129, 164, 121), 
        (127, 129, 154, 121), (127, 129, 104, 66), (127, 129, 60, 36), 
        (127, 129, 60, 36), (127, 129, 60, 36), (92, 92, 61, 45), 
        (92, 92, 66, 50), (92, 92, 69, 90), (92, 92, 66, 120), 
        (92, 92, 60, 130), (92, 92, 60, 140), (98, 104, 52, 144), 
        (103, 100, 31, 128), (103, 100, 41, 128), (103, 100, 51, 122), 
        (103, 100, 61, 112), (108, 104, 74, 100), (116, 110, 73, 102), 
        (123, 116, 66, 95), (137, 129, 58, 88), (146, 135, 50, 82), 
        (158, 142, 38, 82), (166, 152, 30, 76), (181, 168, 4, 66), 
        (173, 168, 0, 70), (182, 177, -50, 80), (182, 177, -50, 80), 
        (167, 178, -18, 98), (192, 177, 0, 91), (192, 177, 19, 75), 
        (192, 177, 27, 62), (192, 177, 27, 62), (192, 177, 27, 62), 
        (192, 177, 27, 62), (192, 177, 27, 62), (192, 177, 27, 62), 
        (192, 177, 27, 62), (192, 177, 35, 45), (192, 177, 27, 53), 
        (192, 177, 27, 53)
    ]
    
    for i in range(49):
        frame = BuildImage.open(img_dir / f"zaoleipi ({i+1}).png")
        
        # 检查是否需要透明化 (第12-16帧和40-49帧)
        if 11 <= i <= 15 or 39 <= i <= 48:
            # 创建完全透明的图像
            wheel_img = BuildImage.new("RGBA", locs[i][:2], (0, 0, 0, 0))
        else:
            # 正常使用头像
            wheel_img = avatar.resize(locs[i][:2])
        
        # 将图像贴到模板上
        frame.paste(wheel_img, locs[i][2:], alpha=True)
        frames.append(frame.image)
    
    return save_gif(frames, 0.02)

add_meme(
    "zaoleipi",
    zaoleipi,
    min_images=1,
    max_images=1,
    keywords=["遭雷劈","电"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)
