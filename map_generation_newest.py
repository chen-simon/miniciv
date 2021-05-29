""" A moduole to convert a given image to a miniciv gameboard map"""
from typing import Any
from PIL import Image, ImageEnhance


def generate_gameboard() -> Any:
    """Create the gameboard given an image"""
    img = Image.open('testermap.png')

    resized_image = image_resize('testermap.png')
    pixelated_image = pixelate(resized_image, 16)


def image_resize(path: str) -> Any:
    """Generate a gameboard given an image
    Credit: https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio"""
    base_width = 40
    img = Image.open(path)
    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((base_width, hsize), Image.ANTIALIAS)
    return img


def pixelate(path, pixel_size):
    """Pixelates a given image into individual 16x16 pixels
        Credit: https://dev.to/natamacm/turn-photos-into-pixel-art-with-python-32pc"""
    tile_list = []
    rgb_list = []
    path = path.convert("RGB")
    #image = path.resize((path.size[0] // pixel_size, path.size[1] // pixel_size), Image.NEAREST)
    #image = path.resize((path.size[0] * pixel_size, path.size[1] * pixel_size), Image.NEAREST)
    list_of_pixels = list(path.getdata())
    #path.show()
    #path.save('sss.png')
    #print(list_of_pixels)
    for i in range(len(list_of_pixels)):
        temp = list_of_pixels[i]
        rgb_list.append(list(temp))
    #print(rgb_list)

    for i in range(len(rgb_list)):
        if rgb_list[i][-1] > 250:
            tile_list.append('WATER_TILE')
        else:
            tile_list.append('GRASS_TILE')
    print(tile_list)

    # for i in range(len(list_of_pixels)):
    #     print('11111')
    #     temp = list(list_of_pixels)
    #     rgb_list.append(temp)
    # print(rgb_list)


def tile_picker(rgb_list):
    """Decides what pixel will become a water tile based off blue RBG value """
    for i in rgb_list:
        print(i)


# def threshhold(image, value):
#     an_image = Image.open("testermap.png")
#     sequence_of_pixels = an_imagege.getdata()
#     list_of_pixels = list(sequence_of_pixels)
#
#     print(list_of_pixels)

    # -> list[list[Tile]]
    # identify the tyo
    # choose all blue tiles into
