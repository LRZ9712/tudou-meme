from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif
from meme_generator.exception import TextOverLength

img_dir = Path(__file__).parent / "images"

def chishi(images, texts: list[str], args):
    text = texts[0]
    frames: list[IMG] = []
    
    # 一共有4帧
    total_frames = 4
    
    # 文本绘制区域（根据您的需要调整这些参数）
    text_area = (216, 75, 717, 281)  # (x1, y1, x2, y2) - 从(369,162)到(569,262)的200x100区域
    
    for i in range(total_frames):
        # 1. 加载每一帧的模板图片
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 2. 在指定区域添加文字
        try:
            frame.draw_text(
                text_area,
                text,
                fill=(255, 255, 255),  # 黑色文字
                # fill=(255, 255, 255),  # 白色文字
                allow_wrap=True,
                max_fontsize=200,
                min_fontsize=50,
                lines_align="center",
                stroke_ratio=0.08,  # 添加文字描边（可选）
                stroke_fill=(0, 0, 0),  # 白色描边（可选）
                font_families=["FZSJ-QINGCRJ"],
            )
        except ValueError:
            raise TextOverLength(text)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.04)

add_meme(
    "chishi",  # 请修改为您想要的名称
    chishi,
    min_texts=1,
    max_texts=1,
    default_texts=["输入文字"],
    keywords=["吃屎"],
    date_created=datetime(2026, 1, 7),
    date_modified=datetime(2026, 1, 7),
)