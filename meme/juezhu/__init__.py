from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL import Image, ImageDraw
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def juezhu(images: list[BuildImage], texts, args):
    avatar_states = [[(196, 113, 75, 75, 0, True, False), (192, 119, 63, 61, 0, True, False), (204, 117, 70, 71, 0, True, False), (197, 123, 70, 62, 0, True, False), (191, 123, 70, 61, 0, True, False), (220, 128, 63, 59, 0, True, False), (235, 108, 64, 49, 0, True, False), (231, 106, 67, 62, 0, True, False), (224, 140, 69, 51, 0, True, False), (210, 178, 76, 53, 0, True, False), (212, 164, 79, 59, 0, True, False), (216, 182, 67, 48, 0, True, False), (218, 188, 62, 48, 0, True, False), (215, 186, 65, 61, 0, True, False), (216, 183, 64, 59, 0, True, False), (212, 185, 64, 61, 0, True, False), (213, 184, 70, 57, 0, True, False), (215, 189, 62, 48, 0, True, False), (209, 186, 62, 52, 0, True, False), (211, 188, 71, 58, 0, True, False), (209, 187, 68, 53, 0, True, False), (214, 183, 60, 55, 0, True, False), (204, 185, 68, 60, 0, True, False), (209, 186, 57, 48, 0, True, False), (207, 185, 65, 57, 0, True, False)]]
    frames: list[IMG] = []
    for i in range(25):
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
    "juezhu",
    juezhu,
    min_images=1,
    max_images=1,
    keywords=["撅猪"],
    date_created=datetime(2026, 11, 5),
    date_modified=datetime(2026, 11, 5),
)
