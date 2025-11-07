from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def cairen(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明 PNG
    avatar = images[0].convert("RGBA").resize((90, 90)).circle()
    
    frames: list[IMG] = []
    
    # 各帧头像位置参数 (x, y, w, h)
    locs = [
        (85, 532, 83, 83),
        (83, 532, 87, 87),
        (84, 532, 87, 87),
        (82, 532, 85, 85),
        (84, 532, 87, 87),
        (83, 533, 87, 87),
        (84, 530, 87, 87),
        (84, 531, 87, 87),
        (82, 534, 87, 87),
        (86, 532, 81, 81),
        (84, 531, 83, 83),
        (83, 532, 85, 85),
        (81, 533, 88, 88),
        (84, 531, 88, 88),
    ]

    for i, (x, y, w, h) in enumerate(locs):
        # 加载模板帧
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 调整头像大小并粘贴
        face = avatar.resize((w, h))
        frame.paste(face, (x, y), alpha=True)
        
        frames.append(frame.image)

    # 生成 GIF 动画，帧间隔可根据节奏调整
    return save_gif(frames, 0.05)

# 注册表情包
add_meme(
    "cairen",
    cairen,
    min_images=1,
    max_images=1,
    keywords=["踩人","被踩"],
    date_created=datetime(2025, 11, 7),
    date_modified=datetime(2025, 11, 7),
)
