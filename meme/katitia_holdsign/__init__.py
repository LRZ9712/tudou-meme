from datetime import datetime
from pathlib import Path
import random

from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"

def katitia_holdsign(images, texts: list[str], args):
    text = texts[0]
    bg_filename = random.choice(["0.jpg", "1.jpg"])
    image_path = img_dir / bg_filename
    frame = BuildImage.open(image_path)
    try:
        frame.draw_text(
            (230, 680, 660, 970),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=300,
            min_fontsize=30,
            lines_align="left",
            font_families=["FZKT.TTF"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()

add_meme(
    "katitia_holdsign",
    katitia_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["不要再涩涩了"],
    keywords=["色色卡提举牌", "瑟瑟卡提举牌"],
    date_created=datetime(2025, 7, 7),
    date_modified=datetime(2025, 7, 7),
)
