from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def paobujis(images: list[BuildImage], texts, args):
    # 处理头像：转为圆形透明 PNG
    avatar = images[0].convert("RGBA").resize((200, 200)).circle()

    frames: list[IMG] = []

    # 各帧头像位置参数 (x, y, w, h)
    locs = [
        (214, 72, 198, 198),
        (215, 81, 198, 198),
        (214, 85, 198, 198),
        (217, 103, 198, 198),
        (227, 92, 198, 198),
        (228, 73, 187, 187),
        (227, 83, 187, 187),
        (228, 100, 187, 187),
        (229, 106, 187, 187),
        (217, 91, 187, 187),
    ]

    for i, (x, y, w, h) in enumerate(locs):
        # 加载模板帧
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 调整头像尺寸并粘贴
        face = avatar.resize((w, h))
        frame.paste(face, (x, y), alpha=True)

        frames.append(frame.image)

    # 保存为 GIF，帧间隔控制节奏
    return save_gif(frames, 0.02)


# 注册表情包
add_meme(
    "paobujis",
    paobujis,
    min_images=1,
    max_images=1,
    keywords=["跑步机"],
    date_created=datetime(2025, 11, 7),
    date_modified=datetime(2025, 11, 7),
)
