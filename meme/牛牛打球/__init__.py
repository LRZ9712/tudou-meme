from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def niuniu_play_ball(images: list[BuildImage], texts, args):
    # 第一个头像的位置信息（左侧头像）
    avatar1_pos_raw = [
        [3, 115, 75, 86],
        [1, 115, 75, 86],
        [-1, 131, 77, 88],
        [-1, 143, 77, 88],
        [-4, 134, 77, 88],
        [-1, 121, 77, 88],
        [-1, 115, 77, 88],
        [0, 118, 77, 88],
        [1, 134, 77, 88],
        [2, 146, 77, 88],
        [1, 133, 77, 88],
        [0, 118, 77, 88],
        [20, 126, 77, 88],
        [69, 165, 47, 54],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    # 第二个头像的位置信息（右侧头像）
    avatar2_pos_raw = [
        [137, 115, 80, 87],
        [143, 116, 78, 89],
        [145, 130, 79, 89],
        [140, 141, 79, 89],
        [143, 137, 79, 89],
        [143, 121, 79, 89],
        [140, 116, 79, 89],
        [145, 116, 79, 89],
        [142, 137, 79, 89],
        [138, 141, 79, 89],
        [140, 132, 79, 89],
        [144, 118, 79, 89],
        [123, 128, 79, 89],
        [107, 159, 55, 61],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    # 处理头像
    avatar1_head = (
        images[0]
        .convert("RGBA")
        .circle()
    )
    avatar2_head = (
        images[1]
        .convert("RGBA")
        .circle()
    )

    frames: list[IMG] = []
    total_frames = max(len(avatar1_pos_raw), len(avatar2_pos_raw))
    
    for i in range(total_frames):
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 粘贴第一个头像（如果该帧有有效位置）
        if i < len(avatar1_pos_raw):
            pos = avatar1_pos_raw[i]
            if pos[2] > 0 and pos[3] > 0:  # 检查尺寸是否有效
                head_resized = avatar1_head.resize((pos[2], pos[3]), keep_ratio=True).rotate(359)
                frame.paste(head_resized, (pos[0], pos[1]), alpha=True)
        
        # 粘贴第二个头像（如果该帧有有效位置）
        if i < len(avatar2_pos_raw):
            pos = avatar2_pos_raw[i]
            if pos[2] > 0 and pos[3] > 0:  # 检查尺寸是否有效
                head_resized = avatar2_head.resize((pos[2], pos[3]), keep_ratio=True).rotate(359)
                frame.paste(head_resized, (pos[0], pos[1]), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)


add_meme(
    "niuniu_play_ball",
    niuniu_play_ball,
    min_images=2,
    max_images=2,
    keywords=["牛牛打球", "打球", "牛牛"],
    date_created=datetime(2023, 3, 7),
    date_modified=datetime(2023, 3, 7),
)