from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def guan_bingxiang(images: list[BuildImage], texts, args):
    # 处理用户头像
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((235, 227)).circle()  # 使用最大尺寸作为基础
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height)
    locs = [
        (124, 140, 196, 196),
        (124, 145, 196, 196),
        (122, 142, 196, 196),
        (128, 140, 196, 196),
        (130, 139, 196, 196),
        (136, 140, 196, 196),
        (128, 145, 186, 186),
        (133, 139, 186, 186),
        (137, 139, 186, 186),
        (137, 144, 186, 186),
        (144, 142, 174, 188),
        (140, 145, 174, 188),
        (139, 145, 174, 188),
        (145, 159, 174, 188),
        (147, 179, 190, 201),
        (150, 199, 219, 201),
        (166, 206, 235, 216),
        (179, 200, 235, 216),
        (195, 186, 235, 227),
        (195, 188, 235, 227),
        (202, 183, 232, 224),
        (193, 186, 232, 224),
        (200, 189, 232, 224),
        (205, 182, 232, 224),
        (205, 188, 232, 224),
        (194, 188, 232, 224),
        (199, 188, 232, 224),
        (196, 185, 232, 224),
        (207, 182, 232, 224),
        (197, 192, 232, 224),
        (199, 185, 232, 224),
        (200, 185, 232, 224),
        (188, 186, 232, 224),
        (191, 188, 232, 224),
        (184, 191, 232, 224),
        (188, 197, 220, 207),
        (177, 195, 220, 207),
        (188, 188, 203, 191),
        (161, 154, 191, 180),
        (159, 154, 179, 168),
        (150, 145, 179, 168),
        (145, 145, 179, 168),
        (150, 142, 179, 168),
        (153, 145, 179, 168),
        (156, 147, 179, 168),
        (154, 142, 179, 168),
        (144, 147, 179, 168),
        (147, 142, 179, 168),
        (150, 145, 179, 168),
        (147, 147, 179, 168),
        (154, 148, 187, 174),
        (150, 144, 187, 174),
        (156, 140, 189, 176),
        (172, 145, 173, 176),
        (184, 145, 159, 176),
        (204, 140, 159, 176),
        (0, 0, 0, 0)
    ]
    
    total_frames = 72
    
    for i in range(total_frames):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 只在56帧之前显示头像（第0-55帧）
        if i < 56 and i < len(locs):
            pos_x, pos_y, width, height = locs[i]
            # 检查是否为有效位置（width和height不为0）
            if width > 0 and height > 0:
                # 根据每帧的尺寸调整头像
                avatar_frame = avatar.resize((width, height))
                frame.paste(avatar_frame, (pos_x, pos_y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "guan_bingxiang",
    guan_bingxiang,
    min_images=1,
    max_images=1,
    keywords=["关冰箱"],
    date_created=datetime(2025, 1, 1),
    date_modified=datetime(2025, 1, 1),
)