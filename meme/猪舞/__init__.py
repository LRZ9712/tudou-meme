from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def zhuwu(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((108, 108)).circle()  # 使用最大尺寸作为基础尺寸
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height)
    locs = [
        (72, 99, 102, 102),
        None,
        None,
        (69, 90, 102, 102),
        (53, 77, 102, 102),
        (48, 70, 102, 102),
        None,
        (37, 61, 102, 102),
        None,
        None,
        (44, 51, 104, 104),
        None,
        (59, 48, 104, 104),
        None,
        (138, 24, 104, 104),
        None,
        None,
        None,
        (80, 48, 106, 106),
        (50, 42, 106, 106),
        (26, 42, 106, 106),
        None,
        (46, 37, 106, 106),
        None,
        (75, 29, 108, 108),
        (122, 28, 108, 108),
        None,
        None,
        (63, 28, 108, 108),
        None,
        (22, 31, 108, 108),
        None,
        (48, 23, 108, 108),
        None,
        (71, 31, 108, 108),
        (131, 10, 108, 108),
        None,
        None,
        (130, 16, 93, 93),
        None,
        (81, 18, 95, 95),
        None,
        None,
        (57, 24, 97, 97)
    ]
    
    # 记录上一帧的有效位置信息
    last_valid_loc = None
    
    for i in range(len(locs)):
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 获取当前帧的位置信息，如果是null则使用上一帧的位置
        current_loc = locs[i]
        if current_loc is None and last_valid_loc is not None:
            current_loc = last_valid_loc
        elif current_loc is not None:
            last_valid_loc = current_loc
        
        # 3. 如果当前帧有位置信息，则贴上圆形头像
        if current_loc is not None:
            pos_x, pos_y, width, height = current_loc
            avatar_resized = avatar.resize((width, height))
            frame.paste(avatar_resized, (pos_x, pos_y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "zhuwu",
    zhuwu,
    min_images=1,
    max_images=1,
    keywords=["猪舞"],
    date_created=datetime(2025, 10, 25),
    date_modified=datetime(2025, 10, 25),
)