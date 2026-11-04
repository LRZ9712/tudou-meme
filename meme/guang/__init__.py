from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL import Image, ImageDraw
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def guang(images: list[BuildImage], texts, args):
    avatar_states = [[(190, 162, 110, 156, 0, True, False), (176, 188, 137, 131, 0, True, False), (164, 195, 155, 120, 0, True, False), (439, 170, 137, 131, 0, True, False), (403, 178, 137, 131, 0, True, False), (189, 162, 112, 154, 0, True, False), (176, 188, 137, 131, 0, True, False), (164, 193, 156, 126, 0, True, False), (438, 279, 137, 131, 0, True, False), (422, 190, 137, 131, 0, True, False), (189, 164, 113, 150, 0, True, False), (177, 189, 137, 131, 0, True, False), (163, 194, 160, 124, 0, True, False), (416, 222, 137, 131, 0, True, False), (413, 185, 137, 131, 0, True, False), (187, 161, 113, 151, 0, True, False), (176, 188, 137, 131, 0, True, False), (165, 193, 152, 124, 0, True, False), (416, 186, 137, 131, 0, True, False), (432, 189, 137, 131, 0, True, False)]]
    frames: list[IMG] = []
    for i in range(20):
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
    "guang",
    guang,
    min_images=1,
    max_images=1,
    keywords=["咣"],
    date_created=datetime(2026, 9, 11),
    date_modified=datetime(2026, 9, 11),
)
