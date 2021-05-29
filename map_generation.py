""" A moduole to convert a given image to a miniciv gameboard map"""
from typing import Any
from PIL import Image, ImageEnhance


def generate_gameboard() -> list[list[str]]:
    """Create the gameboard given an image"""
    img1 = image_resize('testermap.png')
    img2 = pixelate(img1, 4)


def image_resize(path: str) -> Any:
    """Generate a gameboard given an image
    Credit: https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio"""
    base_width = 40
    img = Image.open(path)
    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((base_width, hsize), Image.ANTIALIAS)
    return img


# def color_correction():
#     img = Image.open('testermap.png')
#     corrected = ImageEnhance.Color(img)
#     corrected.enhance(300).show()

def pixelate(image: str, pixel_size: int) -> list:
    """Pixelates a given image into individual 16x16 pixels
    Credit: https://dev.to/natamacm/turn-photos-into-pixel-art-with-python-32pc"""
    rgb_list = []
    image = Image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)
    image = Image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)
    """Credit: https://www.kite.com/python/answers/how-to-list-pixel-values-from-a-pil-image-in-python"""
    sequence_of_pixels = image.getdata()
    for i in range(len(sequence_of_pixels)):
        temp = (list(sequence_of_pixels[i]))
        del temp[-1]
        rgb_list.append(temp)
    print(rgb_list)


def tile_picker(rgb_list):
    """Decides what pixel will become a water tile based off blue RBG value """
    for i in rgb_list:
        print(i)









# def threshhold(image, value):
#     an_image = Image.open("testermap.png")
#     sequence_of_pixels = an_image.getdata()
#     list_of_pixels = list(sequence_of_pixels)
#
#     print(list_of_pixels)

    # -> list[list[Tile]]
    # identify the tyo
    # choose all blue tiles into
