from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL import Image, ImageDraw
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def kanzhutou(images: list[BuildImage], texts, args):
    avatar_states = [[(172, 55, 41, 43, 0, True, False), (170, 60, 40, 41, 0, True, False), (168, 66, 40, 41, 0, True, False), (168, 70, 40, 41, 0, True, False), (168, 73, 40, 41, 0, True, False), (165, 69, 40, 41, 0, True, False), (165, 69, 40, 41, 0, True, False), (162, 70, 40, 41, 0, True, False), (160, 73, 40, 41, 0, True, False), (161, 75, 40, 41, 0, True, False), (156, 81, 40, 41, 0, True, False), (155, 82, 40, 41, 0, True, False), (152, 87, 40, 41, 0, True, False), (150, 91, 40, 41, 0, True, False), (146, 95, 40, 41, 0, True, False), (143, 96, 40, 41, 0, True, False), (139, 105, 40, 41, 0, True, False), (136, 110, 40, 41, 0, True, False), (132, 109, 40, 41, 0, True, False), (121, 97, 45, 48, 0, True, False), (111, 98, 45, 48, 0, True, False), (104, 106, 45, 48, 0, True, False), (100, 115, 45, 48, 0, True, False), (96, 121, 45, 48, 0, True, False), (89, 138, 45, 48, 0, True, False), (86, 154, 45, 48, 0, True, False), (81, 168, 48, 49, 0, True, False), (72, 184, 48, 49, 0, True, False), (67, 186, 48, 49, 0, True, False), (63, 193, 48, 49, 0, True, False), (54, 200, 48, 49, 0, True, False), (53, 208, 48, 49, 0, True, False), (50, 216, 48, 49, 0, True, False), (45, 225, 48, 49, 0, True, False), (40, 226, 48, 49, 0, True, False), (30, 229, 48, 49, 0, True, False), (30, 231, 48, 49, 0, True, False), (10, 239, 48, 49, 0, True, False), (2, 246, 48, 49, 0, True, False), (26, 238, 48, 49, 0, True, False), (19, 257, 48, 49, 0, True, False), (16, 249, 48, 49, 0, True, False), (23, 246, 48, 49, 0, True, False), (20, 249, 48, 49, 0, True, False), (24, 248, 48, 49, 0, True, False), (24, 253, 48, 49, 0, True, False), (3, 248, 48, 49, 0, True, False), (23, 252, 48, 49, 0, True, False), (18, 246, 48, 49, 0, True, False), (23, 263, 48, 49, 0, True, False), (21, 246, 48, 49, 0, True, False), (8, 251, 48, 49, 0, True, False), (9, 262, 48, 49, 0, True, False), (23, 264, 48, 49, 0, True, False), (6, 256, 48, 49, 0, True, False), (36, 281, 48, 49, 0, True, False)]]
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
    return save_gif(frames, 0.020)

add_meme(
    "kanzhutou",
    kanzhutou,
    min_images=1,
    max_images=1,
    keywords=["砍猪头"],
    date_created=datetime(2026, 11, 5),
    date_modified=datetime(2026, 11, 5),
)
