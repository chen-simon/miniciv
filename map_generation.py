""" A module to convert a given image to a miniciv gameboard map"""
from typing import Any
from PIL import Image, ImageEnhance


def generate_gameboard() -> Any:
    """Create the gameboard given an image"""
    img = Image.open('testermap.png')

    resized_image = image_resize('testermap.png')
    pixelated_image = pixelate(resized_image, 16)


def image_resize(path: str) -> Any:
    """Generate a gameboard given an image"""
    base_width = 40
    img = Image.open(path)
    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((base_width, hsize), Image.ANTIALIAS)
    return img


def pixelate(path, pixel_size):
    """Pixelates a given image into individual 16x16 pixels"""
    tile_list = []
    rgb_list = []
    path = path.convert("RGB")
    list_of_pixels = list(path.getdata())

    for i in range(len(list_of_pixels)):
        temp = list_of_pixels[i]
        rgb_list.append(list(temp))

    for i in range(len(rgb_list)):
        if rgb_list[i][-1] > 250:
            tile_list.append('WATER_TILE')
        else:
            tile_list.append('GRASS_TILE')
    return tile_list


