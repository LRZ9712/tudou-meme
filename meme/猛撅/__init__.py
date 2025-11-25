from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def mengjue(images: list[BuildImage], texts, args):
    # 根据提供的位置信息设置坐标
    # 第一个头像位置 (TO类型)
    user1_locs = [(10, 23), (10, 31)]
    # 第二个头像位置 (TO类型)  
    user2_locs = [(226, 170), (223, 170)]
    
    # 头像尺寸
    user1_size = (118, 118)
    user2_size = (104, 104)
    
    # 处理头像
    user1_head = (
        images[0]
        .convert("RGBA")
        .resize(user1_size, keep_ratio=True)
        .circle()  # 圆形头像
    )
    user2_head = (
        images[1]
        .convert("RGBA")
        .resize(user2_size, keep_ratio=True)
        .circle()  # 圆形头像
    )
    
    frames: list[IMG] = []
    for i in range(2):  # 2帧动画
        frame = BuildImage.open(img_dir / f"{i}.png")
        frame.paste(user1_head, user1_locs[i], alpha=True)
        frame.paste(user2_head, user2_locs[i], alpha=True)
        frames.append(frame.image)
    
    return save_gif(frames, 0.04)


add_meme(
    "mengjue",
    mengjue,
    min_images=2,
    max_images=2,
    keywords=["猛撅", "速撅", "狗狗撅"],
    date_created=datetime(2025, 11, 23),  # 可以更新为当前日期
    date_modified=datetime(2025, 11, 23),  # 可以更新为当前日期
)