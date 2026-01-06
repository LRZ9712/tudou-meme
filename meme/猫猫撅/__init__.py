from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def cat_jue(images: list[BuildImage], texts, args):
    # 第一个头像位置（上方/左侧头像）
    avatar1_locs = [
        (54, 15), (50, 16), (51, 14), (51, 14), (54, 14), (51, 15),
        (51, 15), (51, 15), (52, 15), (50, 15), (52, 15), (52, 14)
    ]
    avatar1_sizes = [
        (60, 52), (63, 50), (62, 55), (61, 53), (59, 55), (61, 53),
        (61, 53), (66, 50), (63, 53), (65, 53), (61, 53), (61, 53)
    ]
    
    # 第二个头像位置（下方/右侧头像）
    avatar2_locs = [
        (8, 69), (7, 68), (6, 66), (7, 67), (7, 68), (6, 68),
        (6, 67), (6, 67), (8, 68), (7, 68), (8, 67), (8, 67)
    ]
    avatar2_sizes = [
        (57, 46), (59, 48), (61, 47), (59, 48), (59, 48), (60, 46),
        (60, 46), (61, 46), (61, 46), (61, 47), (59, 46), (59, 46)
    ]
    
    # 处理第一个头像
    avatar1_head = images[0].convert("RGBA").circle()
    
    # 处理第二个头像
    avatar2_head = images[1].convert("RGBA").circle()
    
    frames: list[IMG] = []
    total_frames = 12  # 总共有12帧
    
    for i in range(total_frames):
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 粘贴第一个头像
        head1_resized = avatar1_head.resize(avatar1_sizes[i], keep_ratio=True)
        frame.paste(head1_resized, avatar1_locs[i], alpha=True)
        
        # 粘贴第二个头像
        head2_resized = avatar2_head.resize(avatar2_sizes[i], keep_ratio=True)
        frame.paste(head2_resized, avatar2_locs[i], alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.02)


add_meme(
    "cat_jue",
    cat_jue,
    min_images=2,
    max_images=2,
    keywords=["猫猫撅", "猫撅", "猫咪撅"],
    date_created=datetime(2026, 1, 6),
    date_modified=datetime(2026, 1, 6),
)