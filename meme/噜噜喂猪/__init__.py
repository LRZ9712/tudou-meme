from datetime import datetime
from pathlib import Path
from PIL import Image
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def luluweizhu(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((110, 110)).circle()
    
    frames: list[IMG] = []
    
    # 位置参数列表 (x, y, width, height)
    locs = [
        (208, 224, 100, 100),
        (204, 226, 100, 100),
        (201, 228, 100, 100),
        (204, 231, 100, 100),
        (204, 234, 100, 100),
        (198, 232, 100, 100),
        (196, 236, 100, 100),
        (191, 232, 100, 100),
        (187, 239, 100, 100),
        (177, 243, 100, 100),
        (178, 243, 100, 100),
        (178, 244, 100, 100),
        (176, 240, 100, 100),
        (173, 238, 100, 100),
        (171, 236, 100, 100),
        (162, 246, 100, 100),
        (165, 249, 98, 98),
        (160, 244, 98, 98),
        (161, 244, 98, 98),
        (160, 245, 98, 98),
        (160, 238, 100, 100),
        (162, 239, 98, 98),
        (171, 231, 98, 98),
        (165, 230, 98, 98),
        (162, 234, 98, 98),
        (167, 263, 85, 85),
        (164, 267, 87, 87),
        (154, 256, 87, 87)
    ]
    
    for i in range(28):
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        x, y, width, height = locs[i]
        avatar_resized = avatar.resize((width, height))
        
        # 旋转5度（355度 = 逆时针5度）
        # PIL中正角度表示逆时针旋转
        avatar_resized = avatar_resized.rotate(5, expand=True, resample=Image.BICUBIC)
        
        frame.paste(avatar_resized, (x, y), alpha=True)
        frames.append(frame.image)
    
    return save_gif(frames, 0.07)

add_meme(
    "luluweizhu",
    luluweizhu,
    min_images=1,
    max_images=1,
    keywords=["噜噜喂猪"],
    date_created=datetime(2026, 1, 15),
    date_modified=datetime(2026, 1, 15),
)