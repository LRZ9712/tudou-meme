from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL import Image, ImageDraw
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def moni(images: list[BuildImage], texts, args):
    avatar_states = [[(227, 102, 274, 198, 0, True, False), (227, 102, 274, 198, 0, True, False), (227, 102, 274, 198, 0, True, False), (227, 102, 274, 198, 0, True, False), (227, 102, 274, 198, 0, True, False), (227, 102, 274, 198, 0, True, False)], [(49, 414, 145, 102, 0, True, False), (41, 397, 149, 106, 0, True, False), (38, 380, 157, 116, 0, True, False), (34, 362, 152, 120, 0, True, False), (33, 337, 154, 129, 0, True, False), (38, 369, 158, 124, 0, True, False)]]
    frames: list[IMG] = []
    for i in range(6):
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
    "moni",
    moni,
    min_images=2,
    max_images=2,
    keywords=["摸你"],
    date_created=datetime(2026, 9, 11),
    date_modified=datetime(2026, 9, 11),
)
