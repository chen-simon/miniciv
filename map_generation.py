""" A module to convert a given image to a miniciv gameboard map"""
from typing import Any
from PIL import Image, ImageEnhance

import config
from game import Tile, GrassTile, WaterTile


def generate_gameboard(image) -> list[list[Tile]]:
    """Create the gameboard given an image"""
    resized_image = image.resize((config.BOARD_WIDTH, config.BOARD_HEIGHT), Image.ANTIALIAS)
    return pixelate(resized_image, 16)


def pixelate(image, pixel_size) -> list[list]:
    """Pixelates a given image into individual 16x16 pixels"""
    tile_matrix, rgb_list = [[Tile() for _ in range(config.BOARD_WIDTH)]
                             for _ in range(config.BOARD_HEIGHT)], []
    list_of_pixels = list(image.convert("RGB").getdata())

    for i in range(len(list_of_pixels)):
        temp = list_of_pixels[i]
        rgb_list.append(list(temp))

    for i in range(len(rgb_list)):
        new_tile = GrassTile() if rgb_list[i][2] <= config.WATER_THRESHOLD else WaterTile()
        tile_matrix[i // config.BOARD_WIDTH][i % config.BOARD_WIDTH] = new_tile
    return tile_matrix


# Example
def example_map() -> list[list[Tile]]:
    image = Image.open('testermap.png')
    return generate_gameboard(image)


# Debug
if __name__ == '__main__':
    example_map()
