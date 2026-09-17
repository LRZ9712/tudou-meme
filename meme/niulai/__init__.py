from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL import Image, ImageDraw
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def niulai(images: list[BuildImage], texts, args):
    avatar_states = [[(78, 46, 51, 75, 0, True, False), (76, 31, 57, 88, 0, True, False), (69, 16, 68, 101, 0, True, False), (59, 2, 83, 121, 0, True, False), (55, -11, 90, 133, 0, True, False), (46, -34, 101, 157, 0, True, False), (41, -46, 113, 166, 0, True, False), (38, -49, 119, 174, 0, True, False), (31, -72, 127, 199, 0, True, False)]]
    frames: list[IMG] = []
    for i in range(9):
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
    "niulai",
    niulai,
    min_images=1,
    max_images=1,
    keywords=["牛来"],
    date_created=datetime(2026, 9, 11),
    date_modified=datetime(2026, 9, 11),
)
