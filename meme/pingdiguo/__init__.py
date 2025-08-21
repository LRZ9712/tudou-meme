from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def pingdiguo(images: list[BuildImage], texts, args):
    # 坐标参数保持不变
    self_locs = [(41, 14), (40, 13)]  # 己方头像位置 (x,y)
    user_locs = [(21, 96), (17, 95)]  # 对方头像位置 (x,y)
    
    # 处理己方头像（添加旋转）
    self_head = (
        images[0]
        .convert("RGBA")
        .resize((99, 90), keep_ratio=True)
        .circle()
        .rotate(15)  # 保持15度旋转
    )
    
    # 处理对方头像（移除旋转）
    user_head = (
        images[1]
        .convert("RGBA")
        .resize((91, 79), keep_ratio=True)
        .circle()  # 移除rotate(90)
    )
    
    frames: list[IMG] = []
    for i in range(2):
        # 获取模板尺寸
        template = BuildImage.open(img_dir / f"{i}.png")
        
        # 创建透明画布（与模板同尺寸）
        frame = BuildImage.new("RGBA", template.size)
        
        # 先贴两个头像（底层）
        frame.paste(user_head, user_locs[i], alpha=True)  # 对方头像
        frame.paste(self_head, self_locs[i], alpha=True)  # 己方头像
        
        # 最后覆盖模板图（上层）
        frame.paste(template, (0, 0), alpha=True)  # 关键修改点
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)  # 保持原帧率

add_meme(
    "pingdiguo",
    pingdiguo,
    min_images=2,
    max_images=2,
    keywords=["平底锅", "拍死你"],
    date_created=datetime(2023, 3, 7),
    date_modified=datetime(2023, 3, 7),
)