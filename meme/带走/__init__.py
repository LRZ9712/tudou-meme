from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def run_with(images: list[BuildImage], texts, args):
    # 第一个头像的位置信息 (35个位置点，null表示与上一帧相同)
    avatar1_raw_locs = [
        [164, 109, 40, 40], [163, 154, 40, 40], [172, 149, 40, 40], [172, 145, 40, 40],
        [179, 158, 40, 40], [176, 165, 40, 40], [168, 135, 40, 40], [166, 137, 40, 40],
        [174, 137, 40, 40], [176, 143, 40, 40], [174, 140, 40, 40], [171, 140, 40, 40],
        [171, 145, 40, 40], [176, 155, 40, 40], [181, 113, 40, 40], [178, 122, 42, 42],
        [173, 136, 42, 42], [180, 168, 42, 42], [175, 143, 42, 42], [175, 143, 42, 42],
        None, [178, 152, 42, 42], [174, 146, 42, 42], [171, 131, 42, 42], [169, 137, 42, 42],
        [182, 151, 42, 42], [167, 164, 42, 42], [173, 140, 42, 42], [172, 146, 42, 42],
        [179, 159, 42, 42], [174, 154, 42, 42], [172, 134, 42, 42], [173, 141, 42, 42],
        [176, 165, 42, 42], [160, 164, 42, 42]
    ]
    
    # 第二个头像的位置信息 (35个位置点)
    avatar2_locs = [
        [78, 143, 39, 39], [57, 163, 39, 39], [23, 157, 39, 39], [8, 131, 39, 39],
        [27, 162, 39, 39], [40, 127, 39, 39], [88, 152, 39, 39], [96, 163, 39, 39],
        [116, 175, 39, 39], [14, 151, 39, 39], [13, 131, 39, 39], [15, 131, 39, 39],
        [16, 130, 39, 39], [41, 133, 39, 39], [61, 149, 39, 39], [109, 118, 41, 41],
        [97, 125, 41, 41], [32, 181, 41, 41], [8, 127, 41, 41], [7, 127, 41, 41],
        [8, 132, 41, 41], [20, 155, 41, 41], [85, 160, 41, 41], [118, 125, 41, 41],
        [85, 123, 41, 41], [30, 177, 41, 41], [10, 152, 41, 41], [9, 127, 41, 41],
        [12, 127, 41, 41], [21, 152, 41, 41], [107, 144, 41, 41], [102, 145, 41, 41],
        [107, 159, 41, 41], [35, 181, 41, 41], [10, 147, 41, 41]
    ]
    
    # 处理第一个头像的位置信息，将null替换为上一帧的位置
    avatar1_locs = []
    for i, pos in enumerate(avatar1_raw_locs):
        if pos is None:
            # 使用上一帧的位置
            avatar1_locs.append(avatar1_locs[-1])
        else:
            avatar1_locs.append(pos)
    
    # 处理头像
    avatar1 = (
        images[0]
        .convert("RGBA")
        .resize((40, 40), keep_ratio=True)
        .circle()
    )
    avatar2 = (
        images[1]
        .convert("RGBA")
        .resize((39, 39), keep_ratio=True)
        .circle()
    )
    
    frames: list[IMG] = []
    
    for i in range(35):
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 粘贴第二个头像
        x2, y2, w2, h2 = avatar2_locs[i]
        avatar2_resized = avatar2.resize((w2, h2), keep_ratio=True)
        frame.paste(avatar2_resized, (x2, y2), alpha=True)
        
        # 粘贴第一个头像
        x1, y1, w1, h1 = avatar1_locs[i]
        avatar1_resized = avatar1.resize((w1, h1), keep_ratio=True)
        frame.paste(avatar1_resized, (x1, y1), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)


add_meme(
    "run_with",
    run_with,
    min_images=2,
    max_images=2,
    keywords=["拿着跑", "抱着跑", "带走"],
    date_created=datetime(2025, 10, 25),
    date_modified=datetime(2025, 10, 25),
)