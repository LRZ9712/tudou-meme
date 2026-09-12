from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL import Image, ImageDraw
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def nailongpao(images: list[BuildImage], texts, args):
    avatar_states = [[(74, 63, 76, 77, 0, True, False), (56, 42, 76, 77, 0, True, False), (54, 33, 76, 77, 0, True, False), (51, 47, 76, 77, 0, True, False), (41, 62, 76, 77, 0, True, False), (38, 68, 76, 77, 0, True, False), (56, 64, 76, 77, 0, True, False), (71, 81, 76, 77, 0, True, False), (73, 91, 76, 77, 0, True, False), (72, 72, 76, 77, 0, True, False), (69, 60, 76, 77, 0, True, False), (61, 73, 76, 77, 0, True, False)]]
    frames: list[IMG] = []
    for i in range(12):
        frame = BuildImage.open(img_dir / f"{i}.png")
        for n, avatar in enumerate(images):
            x, y, w, h, angle, circle, bottom = avatar_states[n][i]
            head = avatar.convert("RGBA").resize((w, h), keep_ratio=True)
            if circle:
                mask = Image.new("L", (w, h), 0)
                ImageDraw.Draw(mask).ellipse((0, 0, w - 1, h - 1), fill=255)
                head.image.putalpha(mask)
            head = head.rotate(angle, expand=True)
            if bottom:
                frame.paste(head, (x, y), below=True)
        for n, avatar in enumerate(images):
            x, y, w, h, angle, circle, bottom = avatar_states[n][i]
            if not bottom:
                head = avatar.convert("RGBA").resize((w, h), keep_ratio=True)
                if circle:
                    mask = Image.new("L", (w, h), 0)
                    ImageDraw.Draw(mask).ellipse((0, 0, w - 1, h - 1), fill=255)
                    head.image.putalpha(mask)
                head = head.rotate(angle, expand=True)
                frame.paste(head, (x, y), alpha=True)
        frames.append(frame.image)
    return save_gif(frames, 0.067)

add_meme(
    "nailongpao",
    nailongpao,
    min_images=1,
    max_images=1,
    keywords=["奶龙跑"],
    date_created=datetime(2026, 9, 11),
    date_modified=datetime(2026, 9, 11),
)
