from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL import Image, ImageDraw
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def caoni(images: list[BuildImage], texts, args):
    avatar_states = [[(65, 76, 134, 139, 0, True, False), (72, 73, 134, 139, 0, True, False), (81, 69, 134, 139, 0, True, False), (78, 66, 134, 139, 0, True, False), (68, 63, 134, 139, 0, True, False), (59, 66, 134, 139, 0, True, False), (61, 62, 134, 139, 0, True, False), (63, 69, 134, 139, 0, True, False)]]
    frames: list[IMG] = []
    for i in range(8):
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
    return save_gif(frames, 0.040)

add_meme(
    "caoni",
    caoni,
    min_images=1,
    max_images=1,
    keywords=["草你"],
    date_created=datetime(2026, 11, 5),
    date_modified=datetime(2026, 11, 5),
)
