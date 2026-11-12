from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL import Image, ImageDraw
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def koukou(images: list[BuildImage], texts, args):
    avatar_states = [[(-27, 29, 276, 287, 0, True, False), (-27, 29, 284, 266, 0, True, False), (-10, 0, 292, 248, 0, True, False), (-10, 0, 298, 278, 0, True, False), (-10, 0, 325, 286, 0, True, False), (-10, 0, 319, 311, 0, True, False), (-10, 0, 327, 297, 0, True, False), (-10, 0, 322, 268, 0, True, False), (-10, 0, 339, 237, 0, True, False), (-10, 0, 357, 315, 0, True, False), (-10, 0, 349, 331, 0, True, False), (-10, 0, 349, 351, 0, True, False)]]
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
    "koukou",
    koukou,
    min_images=1,
    max_images=1,
    keywords=["抠"],
    date_created=datetime(2026, 9, 11),
    date_modified=datetime(2026, 9, 11),
)
