import random
from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def llq(images: list[BuildImage], texts, args):
    print("[llq] 模板函数被调用")
    user_head = images[0].resize((110, 110)).circle()
    frames: list[IMG] = []

    for i in range(5):
        frame_path = img_dir / f"{i}.png"
        print(f"[llq] 加载帧图片: {frame_path}")
        frame = BuildImage.open(frame_path).convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)

        new_frame.paste(frame, (0, 0), alpha=True)

        if i == 4:
            print("[llq] 贴圆形头像")
            new_frame.paste(user_head, (180, 90), alpha=True)

        frames.append(new_frame.image)

    gif_bytes = save_gif(frames, 0.8)
    print("[llq] GIF生成完毕")
    return gif_bytes

add_meme(
    "llq",
    llq,
    min_images=1,
    max_images=1,
    keywords=["群p", "群p我"],
    date_created=datetime(2025, 7, 26),
    date_modified=datetime(2025, 7, 26),
)
