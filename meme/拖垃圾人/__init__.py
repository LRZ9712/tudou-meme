from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def drag_trash(images: list[BuildImage], texts, args):
    # 第一个头像的位置信息 (302, 188, 126, 120) 等
    user1_locs = [
        (302, 188), (302, 195), (301, 208), (296, 206), (296, 202),
        (308, 208), (310, 211), (307, 209), (258, 221), (241, 208),
        (235, 212), (241, 211), (238, 211), (239, 221), (235, 220),
        (265, 224), (287, 229), (291, 226), (285, 227), (277, 224),
        (279, 226), (290, 235), (280, 230), (265, 250), (251, 253), (245, 249)
    ]
    user1_sizes = [
        (126, 120), (126, 120), (117, 112), (117, 112), (117, 112),
        (117, 112), (117, 112), (117, 112), (117, 112), (115, 114),
        (115, 114), (115, 114), (105, 114), (105, 114), (124, 114),
        (136, 124), (133, 124), (133, 124), (133, 124), (133, 124),
        (133, 124), (133, 124), (133, 124), (133, 124), (125, 110), (122, 110)
    ]
    
    # 第二个头像的位置信息 (111, 233, 104, 131) 等
    user2_locs = [
        (111, 233), (103, 243), (112, 228), (98, 240), (108, 233),
        (116, 236), (105, 254), (108, 234), (112, 234), (110, 248),
        (105, 240), (105, 236), (105, 242), (105, 239), (105, 240),
        (99, 262), (118, 240), (101, 254), (121, 236), (108, 240),
        (108, 239), (112, 243), (116, 240), (119, 246), (119, 246), (112, 245)
    ]
    user2_sizes = [
        (104, 131), (119, 104), (104, 122), (120, 99), (120, 116),
        (120, 116), (120, 92), (109, 131), (109, 107), (109, 107),
        (109, 107), (109, 107), (109, 107), (109, 107), (109, 107),
        (123, 79), (88, 122), (120, 85), (88, 116), (114, 116),
        (114, 116), (114, 116), (114, 116), (114, 116), (114, 116), (114, 116)
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
    for i in range(26):  # 有26帧
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
    "drag_trash",
    drag_trash,
    min_images=2,
    max_images=2,
    keywords=["拖垃圾人"],
    date_created=datetime(2025, 1, 1),
    date_modified=datetime(2025, 1, 1),
)