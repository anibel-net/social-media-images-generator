import re
from os import path
from sys import argv

from PIL import Image, ImageDraw, ImageFont


def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


if __name__ == '__main__':
    # Args
    PROGRAM_FILES_PATH = argv[1]
    TITLE = argv[2]
    FORMAT = argv[3].upper()
    CATEGORY = argv[4].upper()
    SUBCATEGORY = argv[5].upper()
    COLOR = '#282C34' if CATEGORY == 'CINEMA' else '#7E60B6'
    for filepath in argv[6:]:
        # Init
        image = Image.new('RGBA', (5464, 3072))
        background = Image.open(filepath).convert('RGBA')
        if background.size[0] / background.size[1] == 16 / 9:   # 16:9
            background = background.resize((5464, 3072))
        elif background.size[0] / background.size[1] > 16 / 9:  # Wider
            background = background.resize((int(3072 / background.size[1] * background.size[0]), 3072))
        elif background.size[0] / background.size[1] < 16 / 9:  # Higher
            background = background.resize((5464, int(5464 / background.size[0] * background.size[1])))
        background = crop_center(background, *image.size)
        image.paste(background)
        draw = ImageDraw.Draw(image, 'RGBA')
        # Episode Title
        if SUBCATEGORY == 'SERIAL':
            EPISODE_NUMBER = str(int(re.findall(r'\d+', filepath.split('/')[-1].split('\\')[-1])[-1]))
            draw.rectangle((0, 0, 640, 640), COLOR)
            font_288 = ImageFont.truetype(path.join(PROGRAM_FILES_PATH, 'Montserrat-Regular.ttf'), 288)
            w = draw.textsize(EPISODE_NUMBER, font_288)[0]
            draw.text(((640 - w) / 2, 143), EPISODE_NUMBER, 'white', font_288)
        # Sub/Dub
        font_192 = ImageFont.truetype(path.join(PROGRAM_FILES_PATH, 'Montserrat-Regular.ttf'), 192)
        if FORMAT == 'DUB':
            draw.rectangle((0, 2271, 1344, 2671), COLOR)
            mic = Image.open(path.join(PROGRAM_FILES_PATH, 'DUB.png'))
            mic = mic.resize((172, 264))
            image.paste(mic, (128, 2344), mic)
            draw.text((420, 2353), 'АГУЧКА', '#FFFFFF', font_192)
        if FORMAT == 'SUB':
            draw.rectangle((0, 2271, 1696, 2671), COLOR)
            sub = Image.open(path.join(PROGRAM_FILES_PATH, 'SUB.png'))
            sub = sub.resize((256, 184))
            image.paste(sub, (128, 2380), sub)
            draw.text((512, 2353), 'СУБЦІТРЫ', '#FFFFFF', font_192)
        # Title
        current_font_size = 220
        title_font = ImageFont.truetype(path.join(PROGRAM_FILES_PATH, 'Montserrat-Regular.ttf'), current_font_size)
        w, h = draw.textsize(TITLE, title_font)
        while w > 5400:
            current_font_size -= 1
            title_font = ImageFont.truetype(path.join(PROGRAM_FILES_PATH, 'Montserrat-Regular.ttf'), current_font_size)
            w, h = draw.textsize(TITLE, title_font)
        # Export
        if w <= 3232:
            draw.rectangle((0, 2672, 3360, 3072), (255, 255, 255, 242))
            draw.text(((3360 - w) / 2, 2736), TITLE, '#000000', title_font)
        elif current_font_size == 220:
            draw.rectangle((0, 2672, w + 128, 3072), (255, 255, 255, 242))
            draw.text((64, 2736), TITLE, '#000000', title_font)
        else:
            draw.rectangle((0, 2672, 5464, 3072 + current_font_size / 10), (255, 255, 255, 242))
            draw.text(((5464 - w) / 2, 2672 + (400 - h) / 2), TITLE, '#000000', title_font)
        file_name, file_ext = path.splitext(path.basename(filepath))
        image.save(file_name + '.png')
