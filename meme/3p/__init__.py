from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def meme_3p(images: list[BuildImage], texts, args):
    avatar_states = [[(187, -1, 123, 126, 0, True, False), (172, 8, 123, 126, 0, True, False), (200, -7, 123, 126, 0, True, False)], [(6, 143, 93, 100, 0, True, False), (7, 146, 93, 100, 0, True, False), (6, 140, 93, 100, 0, True, False)], [(74, 186, 114, 115, 0, True, True), (73, 180, 119, 113, 0, True, True), (81, 166, 108, 112, 0, True, True)]]
    frames: list[IMG] = []
    for i in range(3):
        frame = BuildImage.open(img_dir / f"{i}.png")
        for n, avatar in enumerate(images):
            x, y, w, h, angle, circle, bottom = avatar_states[n][i]
            head = avatar.convert("RGBA").resize((w, h), keep_ratio=True)
            if circle:
                head = head.circle()
            head = head.rotate(angle, expand=True)
            if bottom:
                frame.paste(head, (x, y), below=True)
        for n, avatar in enumerate(images):
            x, y, w, h, angle, circle, bottom = avatar_states[n][i]
            if not bottom:
                head = avatar.convert("RGBA").resize((w, h), keep_ratio=True)
                if circle:
                    head = head.circle()
                head = head.rotate(angle, expand=True)
                frame.paste(head, (x, y), alpha=True)
        frames.append(frame.image)
    return save_gif(frames, 0.067)

add_meme(
    "3p",
    meme_3p,
    min_images=3,
    max_images=3,
    keywords=["3p"],
    date_created=datetime(2026, 9, 11),
    date_modified=datetime(2026, 9, 11),
)
