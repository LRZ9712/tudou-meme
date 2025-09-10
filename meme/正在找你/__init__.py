from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG

from pil_utils import BuildImage, Text2Image
from pydantic import Field

from meme_generator import (
    MemeArgsModel,
    MemeArgsType,
    add_meme,
)
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

class ZhengZaiZhaoNiArgs(MemeArgsModel):
    pass

args_type = MemeArgsType(args_model=ZhengZaiZhaoNiArgs)

def zheng_zai_zhao_ni(images: list[BuildImage], texts: list[str], args: ZhengZaiZhaoNiArgs):
    """
    生成"正在找你"GIF表情包。
    """
    try:
        bg = BuildImage.open(img_dir / "0.png")
    except FileNotFoundError:
        raise FileNotFoundError("错误：模板图片 '0.png' 未找到。")

    # 确定显示的文本
    if texts:
        name = texts[0]
    elif args.user_infos:
        name = args.user_infos[0].name
    else:
        name = args.sender_info.name
    
    # 修正：移除 fontsize= 关键字参数，改为位置参数
    text_img = Text2Image.from_text(name, 28, fill="black").to_image()
    text_w, text_h = text_img.size
    
    # 计算文本粘贴位置
    box_x, box_y, box_w, box_h = 155, 230, 176, 33
    text_x = box_x + (box_w - text_w) // 2
    text_y = box_y + (box_h - text_h) // 2
    text_pos = (text_x, text_y)

    # 处理用户头像
    avatar = images[0].convert("RGBA").circle()
    
    # 定义头像的位置和大小
    x, y, w, h = 158, 39, 165, 165
    avatar_pos = (x, y)
    avatar_size = (w, h)

    resized_avatar = avatar.resize(avatar_size)

    frames: list[IMG] = []
    num_frames = 36
    angle_step = 10
    
    for i in range(num_frames):
        frame = bg.copy()
        current_angle = -(i * angle_step)
        rotated_avatar = resized_avatar.rotate(current_angle)
        frame.paste(rotated_avatar, avatar_pos, alpha=True)
        frame.paste(text_img, text_pos, alpha=True)
        frames.append(frame.image)

    return save_gif(frames, 0.05)

# 注册表情包
add_meme(
    "zheng_zai_zhao_ni",
    zheng_zai_zhao_ni,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    args_type=args_type,
    keywords=["正在找你"],
    date_created=datetime(2025, 9, 10),
    date_modified=datetime(2025, 9, 10)
)