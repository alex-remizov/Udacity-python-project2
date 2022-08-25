"""Generate mems."""

from PIL import Image, ImageDraw, ImageFont
from random import randint


class MemeGenerator:
    """Class that generates meme."""

    def __init__(self, output_dir):
        """Initialize a mem with output_dir."""
        self.output_dir = output_dir

    def make_mem(self, img_path, text, author, width=500) -> str:
        """Make and save the mem. retun the path of a mem."""
        img = Image.open(img_path)

        if width > 0:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)
        else:
            raise Exception('width should be > 0')

        if text is not None and author is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("arial.ttf", 20)
            message = f'{text} - {author}'
            draw.text(
                (randint(0, width*0.66), randint(0, width*0.66)),
                message, font=font, fill='black')

        img.save(self.output_dir)
        return self.output_dir
