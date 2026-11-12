from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL import Image, ImageDraw
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def mjmj(images: list[BuildImage], texts, args):
    avatar_states = [[(39, 23, 74, 74, 0, True, False), (39, 22, 74, 74, 0, True, False), (40, 21, 74, 74, 0, True, False), (39, 20, 74, 74, 0, True, False), (39, 18, 74, 74, 0, True, False), (37, 15, 74, 74, 0, True, False), (34, 16, 74, 74, 0, True, False), (33, 17, 74, 74, 0, True, False), (32, 18, 74, 74, 0, True, False), (31, 18, 74, 74, 0, True, False), (30, 18, 75, 74, 0, True, False), (30, 19, 74, 74, 0, True, False), (28, 20, 74, 74, 0, True, False), (29, 20, 74, 74, 0, True, False), (28, 23, 74, 74, 0, True, False), (27, 24, 74, 74, 0, True, False), (27, 25, 74, 74, 0, True, False), (27, 25, 74, 74, 0, True, False), (28, 26, 74, 74, 0, True, False), (29, 26, 74, 74, 0, True, False), (28, 28, 74, 74, 0, True, False), (29, 28, 74, 74, 0, True, False), (28, 27, 74, 74, 0, True, False), (30, 29, 74, 74, 0, True, False), (32, 29, 74, 74, 0, True, False), (31, 28, 74, 74, 0, True, False), (34, 28, 74, 74, 0, True, False), (35, 28, 74, 74, 0, True, False), (37, 27, 74, 74, 0, True, False), (37, 28, 74, 74, 0, True, False), (38, 29, 74, 74, 0, True, False), (41, 28, 74, 74, 0, True, False), (40, 27, 74, 74, 0, True, False), (41, 26, 74, 74, 0, True, False), (41, 27, 74, 74, 0, True, False), (45, 27, 74, 74, 0, True, False), (41, 25, 74, 74, 0, True, False), (41, 23, 74, 74, 0, True, False), (39, 23, 74, 74, 0, True, False), (39, 23, 74, 74, 0, True, False), (39, 23, 74, 74, 0, True, False), (39, 23, 74, 74, 0, True, False), (35, 21, 74, 74, 0, True, False), (33, 21, 74, 74, 0, True, False), (32, 21, 74, 74, 0, True, False), (32, 22, 74, 74, 0, True, False), (31, 23, 74, 74, 0, True, False), (32, 24, 74, 74, 0, True, False), (32, 24, 74, 74, 0, True, False), (31, 24, 74, 74, 0, True, False), (30, 26, 74, 74, 0, True, False), (33, 27, 74, 74, 0, True, False), (33, 26, 74, 74, 0, True, False), (36, 28, 74, 74, 0, True, False), (35, 27, 74, 74, 0, True, False), (36, 27, 74, 74, 0, True, False), (36, 26, 74, 74, 0, True, False), (36, 26, 74, 74, 0, True, False), (37, 26, 74, 74, 0, True, False), (39, 23, 74, 74, 0, True, False), (39, 23, 74, 74, 0, True, False)]]
    frames: list[IMG] = []
    for i in range(61):
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
    "mjmj",
    mjmj,
    min_images=1,
    max_images=1,
    keywords=["mj"],
    date_created=datetime(2026, 11, 5),
    date_modified=datetime(2026, 11, 5),
)
