from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL import Image, ImageDraw
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def naiwading(images: list[BuildImage], texts, args):
    avatar_states = [[(14, 158, 76, 75, 0, True, False), (21, 156, 76, 75, 0, True, False), (23, 158, 76, 75, 0, True, False), (11, 162, 76, 75, 0, True, False), (22, 155, 76, 75, 0, True, False), (8, 163, 76, 75, 0, True, False), (7, 163, 76, 75, 0, True, False), (22, 161, 76, 75, 0, True, False), (19, 161, 76, 75, 0, True, False), (9, 164, 76, 75, 0, True, False), (7, 168, 76, 75, 0, True, False), (21, 162, 76, 75, 0, True, False), (21, 159, 76, 75, 0, True, False)]]
    frames: list[IMG] = []
    for i in range(13):
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
    return save_gif(frames, 0.020)

add_meme(
    "naiwading",
    naiwading,
    min_images=1,
    max_images=1,
    keywords=["奶蛙顶"],
    date_created=datetime(2026, 9, 11),
    date_modified=datetime(2026, 9, 11),
)
