from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def motivate(images: list[BuildImage], texts, args):
    # 第一个头像的位置信息 (108, 176, 72, 72) 等
    user1_locs = [
        (108, 176), (107, 176), (111, 176), (120, 178), (100, 172),
        (98, 168), (100, 168), (107, 167), (112, 171), (119, 172),
        (131, 182), (131, 184), (113, 184), (106, 184), (100, 179),
        (98, 179), (93, 179), (90, 175), (95, 177), (100, 177), (106, 177)
    ]
    user1_sizes = [
        (72, 72), (72, 72), (72, 72), (72, 72), (74, 74),
        (74, 74), (74, 74), (74, 74), (74, 74), (74, 74),
        (74, 74), (74, 74), (74, 74), (74, 74), (74, 74),
        (74, 74), (74, 74), (74, 74), (74, 74), (74, 74), (74, 74)
    ]
    
    # 第二个头像的位置信息 (423, 244, 81, 81) 等
    user2_locs = [
        (423, 244), (423, 243), (426, 242), (426, 260), (423, 273),
        (420, 283), (419, 287), (413, 291), (415, 292), (411, 292),
        (416, 291), (415, 299), (412, 301), (408, 302), (420, 297),
        (429, 292), (439, 277), (415, 242), (413, 236), (415, 245), (419, 245)
    ]
    user2_sizes = [
        (81, 81), (81, 81), (81, 81), (81, 81), (83, 83),
        (83, 83), (83, 83), (83, 83), (83, 83), (83, 83),
        (83, 83), (83, 83), (83, 83), (83, 83), (83, 83),
        (83, 83), (83, 83), (83, 83), (83, 83), (83, 83), (83, 83)
    ]
    
    # 处理两个头像
    user1_head = (
        images[0]
        .convert("RGBA")
        .resize(user1_sizes[0], keep_ratio=True)
        .circle()
    )
    user2_head = (
        images[1]
        .convert("RGBA")
        .resize(user2_sizes[0], keep_ratio=True)
        .circle()
    )
    
    frames: list[IMG] = []
    for i in range(21):  # 有21帧
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 粘贴第一个头像
        user1_resized = user1_head.resize(user1_sizes[i], keep_ratio=True)
        frame.paste(user1_resized, user1_locs[i], alpha=True)
        
        # 粘贴第二个头像
        user2_resized = user2_head.resize(user2_sizes[i], keep_ratio=True)
        frame.paste(user2_resized, user2_locs[i], alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)


add_meme(
    "motivate",
    motivate,
    min_images=2,
    max_images=2,
    keywords=["鞭策"],
    date_created=datetime(2025, 10, 30),
    date_modified=datetime(2025, 10, 30),
)