from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL import Image, ImageDraw
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def naiwazhuan(images: list[BuildImage], texts, args):
    avatar_states = [[(147, -8, 37, 41, 0, True, False), (125, -4, 36, 35, 0, True, False), (109, -6, 36, 35, 0, True, False), (110, -5, 36, 35, 0, True, False), (87, -3, 36, 35, 0, True, False), (70, 2, 36, 35, 0, True, False), (58, 2, 38, 39, 0, True, False), (53, 2, 38, 43, 0, True, False), (44, 11, 38, 39, 0, True, False), (36, 17, 38, 39, 0, True, False), (29, 24, 38, 39, 0, True, False), (22, 34, 38, 39, 0, True, False), (19, 45, 38, 39, 0, True, False), (26, 60, 38, 39, 0, True, False)], [(44, 10, 35, 37, 0, True, False), (38, 16, 35, 37, 0, True, False), (30, 24, 35, 37, 0, True, False), (30, 26, 35, 37, 0, True, False), (23, 34, 35, 37, 0, True, False), (21, 45, 35, 37, 0, True, False), (25, 60, 35, 37, 0, True, False), (35, 73, 35, 37, 0, True, False), (46, 78, 35, 37, 0, True, False), (60, 85, 35, 37, 0, True, False), (72, 92, 35, 37, 0, True, False), (97, 96, 35, 37, 0, True, False), (118, 98, 35, 37, 0, True, False), (149, 103, 35, 37, 0, True, False)], [(179, 103, 36, 33, 0, True, False), (196, 101, 36, 33, 0, True, False), (215, 95, 36, 33, 0, True, False), (215, 95, 36, 33, 0, True, False), (229, 89, 43, 41, 0, True, False), (251, 80, 39, 39, 0, True, False), (266, 64, 39, 39, 0, True, False), (268, 52, 39, 39, 0, True, False), (271, 43, 39, 39, 0, True, False), (263, 28, 39, 39, 0, True, False), (253, 21, 39, 39, 0, True, False), (241, 12, 39, 39, 0, True, False), (217, 3, 39, 39, 0, True, False), (186, -4, 39, 39, 0, True, False)], [(43, 80, 41, 40, 0, True, False), (57, 84, 36, 37, 0, True, False), (70, 90, 36, 37, 0, True, False), (70, 91, 36, 37, 0, True, False), (92, 96, 36, 37, 0, True, False), (116, 99, 36, 37, 0, True, False), (148, 102, 36, 39, 0, True, False), (168, 102, 36, 39, 0, True, False), (181, 102, 36, 39, 0, True, False), (196, 101, 36, 39, 0, True, False), (214, 94, 37, 37, 0, True, False), (230, 87, 40, 43, 0, True, False), (249, 79, 39, 40, 0, True, False), (266, 65, 39, 40, 0, True, False)], [(271, 43, 38, 38, 0, True, False), (262, 27, 38, 38, 0, True, False), (254, 22, 34, 37, 0, True, False), (254, 22, 34, 37, 0, True, False), (239, 13, 34, 37, 0, True, False), (222, 3, 34, 36, 0, True, False), (187, -4, 35, 41, 0, True, False), (168, -8, 35, 41, 0, True, False), (150, -7, 35, 41, 0, True, False), (127, -6, 36, 40, 0, True, False), (111, -5, 36, 40, 0, True, False), (88, -5, 36, 40, 0, True, False), (72, -1, 36, 40, 0, True, False), (56, 2, 36, 40, 0, True, False)]]
    frames: list[IMG] = []
    for i in range(14):
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
    "naiwazhuan",
    naiwazhuan,
    min_images=5,
    max_images=5,
    keywords=["奶蛙转"],
    date_created=datetime(2026, 11, 5),
    date_modified=datetime(2026, 11, 5),
)
