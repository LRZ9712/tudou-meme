from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL import Image, ImageDraw
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def naiqiang(images: list[BuildImage], texts, args):
    avatar_states = [[(133, -9, 49, 50, 0, True, False), (133, -15, 49, 50, 0, True, False), (138, -16, 52, 53, 0, True, False), (138, -29, 51, 59, 0, True, False), (137, -24, 49, 56, 0, True, False), (129, -17, 50, 53, 0, True, False), (133, -21, 49, 57, 0, True, False), (136, -10, 53, 51, 0, True, False), (144, 0, 49, 46, 0, True, False), (138, -4, 45, 47, 0, True, False), (117, -2, 55, 57, 0, True, False), (93, 48, 46, 57, 0, True, False), (76, 104, 45, 68, 0, True, False), (74, 103, 43, 66, 0, True, False), (63, 127, 57, 67, 0, True, False), (73, 137, 50, 65, 0, True, False), (135, 8, 46, 84, 20, True, False), (118, -39, 46, 64, 0, True, False), (126, -40, 43, 70, 0, True, False), (143, -36, 46, 72, 0, True, False), (100, -53, 59, 81, 0, True, False), (123, -11, 59, 22, 0, True, False), (122, -11, 55, 20, 0, True, False), (115, -38, 57, 53, 0, True, False), (118, -11, 38, 48, 30, True, False), (105, -9, 40, 45, -13, True, False), (113, -9, 45, 43, 0, True, False), (106, -23, 47, 45, 0, True, False), (119, -16, 43, 40, 0, True, False), (118, -26, 49, 41, 0, True, False), (132, -21, 50, 58, 0, True, False), (84, 64, 54, 59, 0, True, False), (92, 59, 54, 60, 0, True, False), (76, 29, 100, 100, 0, True, False), (75, 22, 107, 103, 0, True, False), (70, 14, 117, 112, 0, True, False), (66, 13, 127, 121, 0, True, False), (62, 0, 131, 129, 0, True, False), (45, -2, 165, 150, 0, True, False), (51, 5, 157, 148, 0, True, False), (47, 3, 162, 147, 0, True, False), (42, -2, 162, 146, 0, True, False), (39, -14, 150, 156, 0, True, False), (43, -5, 155, 140, 0, True, False), (43, -5, 155, 140, 0, True, False), (43, -5, 155, 140, 0, True, False), (43, -5, 155, 140, 0, True, False), (43, -5, 155, 140, 0, True, False), (43, -5, 155, 140, 0, True, False), (43, -5, 155, 140, 0, True, False), (43, -5, 155, 140, 0, True, False), (43, -5, 155, 140, 0, True, False), (43, -5, 155, 140, 0, True, False), (43, -5, 155, 140, 0, True, False), (43, -5, 155, 140, 0, True, False), (43, -5, 155, 140, 0, True, False)]]
    frames: list[IMG] = []
    for i in range(56):
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
    "naiqiang",
    naiqiang,
    min_images=1,
    max_images=1,
    keywords=["奶枪"],
    date_created=datetime(2026, 11, 5),
    date_modified=datetime(2026, 11, 5),
)
