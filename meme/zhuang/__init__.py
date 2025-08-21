from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def zhuang(images: list[BuildImage], texts, args):
    avatar = images[0].convert("RGBA").resize((110, 110)).circle()
    
    # 需要透明的帧索引（Python从0开始计数）
    transparent_frames = list(range(26, 35) # 对应坐标
    
    frames: list[IMG] = []
    # 完整的位置参数（49组）
    locs = [
        (104, 104, 73, 52),  # 车轮位置1
        (104, 104, 73, 52),  # 车轮位置2
        (104, 104, 73, 52),  # 车轮位置3
        (104, 104, 73, 52),  # 车轮位置4
        (104, 104, 73, 52),  # 车轮位置5
        (104, 104, 73, 52),  # 车轮位置6
        (104, 104, 69, 47),  # 车轮位置7
        (104, 104, 65, 40),  # 车轮位置8
        (104, 104, 58, 36),  # 车轮位置9
        (104, 104, 55, 30),  # 车轮位置10
        (104, 104, 50, 25),  # 车轮位置11
        (104, 104, 43, 22),  # 车轮位置12
        (104, 104, 40, 15),  # 车轮位置13
        (104, 104, 33, 12),  # 车轮位置14
        (104, 104, 30, 5),  # 车轮位置15
        (104, 104, 23, 2),  # 车轮位置16
        (104, 104, 19, -3),  # 车轮位置17
        (104, 104, 14, -8),  # 车轮位置18
        (104, 104, 9, -12),  # 车轮位置19
        (104, 104, 2, -17),  # 车轮位置20
        (104, 104, -1, -25),  # 车轮位置21
        (104, 104, -11, -36),  # 车轮位置22
        (104, 104, -11, -36),  # 车轮位置23
        (104, 104, -20, -52),  # 车轮位置24
        (104, 104, -30, -63),  # 车轮位置25
        (104, 104, -42, -70),  # 车轮位置26 没了
        (104, 104, -42, -70),  # 车轮位置27 没了
        (104, 104, -42, -70),  # 车轮位置28 没了
        (104, 104, -42, -70),  # 车轮位置29 没了
        (104, 104, -42, -70),  # 车轮位置30 没了
        (104, 104, -42, -70),  # 车轮位置31 没了
        (104, 104, -42, -70),  # 车轮位置32 没了
        (104, 104, -42, -70),  # 车轮位置33 没了
        (104, 104, -42, -70),  # 车轮位置34 没了
        (104, 104, -42, -70),  # 车轮位置35 没了


    ]
    
    for i in range(35):
        frame = BuildImage.open(img_dir / f"zhuang ({i+1}).png")
        width, height, x, y = locs[i]
        
        if i in transparent_frames:
            # 创建全透明层
            wheel_img = BuildImage.new("RGBA", (width, height), (0, 0, 0, 0))
        else:
            # 正常显示头像
            wheel_img = avatar.resize((width, height))
        
        frame.paste(wheel_img, (x, y), alpha=True)
        frames.append(frame.image)
    
    return save_gif(frames, 0.02)

add_meme(
    "zhuang",
    zhuang,
    min_images=1,
    max_images=1,
    keywords=["撞飞","创飞","创","撞"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)