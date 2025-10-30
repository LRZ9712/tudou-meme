from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def wang(images: list[BuildImage], texts, args):
    # 处理用户头像：转换为圆形透明PNG
    avatar = images[0].convert("RGBA")
    avatar = avatar.resize((118, 118)).circle()  # 使用最大宽度作为基础尺寸
    
    frames: list[IMG] = []
    # 各帧中头像的位置参数 (x, y, width, height) - 共8帧，没有null值
    locs = [
        [49, 60, 118, 71],   # 第0帧
        [51, 62, 118, 71],   # 第1帧
        [52, 61, 117, 71],   # 第2帧
        [55, 60, 112, 71],   # 第3帧
        [58, 60, 107, 71],   # 第4帧
        [52, 66, 115, 71],   # 第5帧
        [52, 62, 112, 71],   # 第6帧
        [54, 60, 113, 71]    # 第7帧
    ]
    
    for i in range(8):  # 总共8帧
        # 1. 加载模板作为底层
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 获取当前帧的位置信息
        pos_x, pos_y, width, height = locs[i]
        
        # 3. 贴上圆形头像（注意这里高度被压缩，会形成椭圆效果）
        avatar_resized = avatar.resize((width, height))
        frame.paste(avatar_resized, (pos_x, pos_y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)

add_meme(
    "wang",
    wang,
    min_images=1,
    max_images=1,
    keywords=["王"],
    date_created=datetime(2025, 10, 30),
    date_modified=datetime(2025, 10, 30),
)