from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def maomaochong(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA").square().resize((110, 110)).circle()
    frames: list[IMG] = []
    locs = [
        (94, 94, 146, 140),
        (94, 94, 142, 138),
        (94, 94, 148, 142),
        (94, 94, 141, 137),
        (94, 94, 147, 143),
        (94, 94, 141, 137),
        (94, 94, 147, 142),
        (94, 94, 141, 139),
        (94, 94, 147, 139),
        (94, 94, 145, 138),      
        (94, 94, 147, 141),    
        (94, 94, 141, 139),

        
        
    ]
    for i in range(12):
        frame = BuildImage.open(img_dir / f"{i}.png")
        w, h, x, y = locs[i]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.05)


add_meme(
    "maomaochong",
    maomaochong,
    min_images=1,
    max_images=1,
    keywords=["毛毛虫"],
    date_created=datetime(2023, 1, 8),
    date_modified=datetime(2023, 2, 14),
)
