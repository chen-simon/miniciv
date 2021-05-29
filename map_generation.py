""" A module to convert a given image to a miniciv gameboard map"""
from typing import Any
from PIL import Image, ImageEnhance

import config
from game import Tile, GrassTile, WaterTile


def generate_gameboard(image) -> list[list[Tile]]:
    """Create the gameboard given an image"""
    resized_image = image.resize((config.BOARD_WIDTH, config.BOARD_HEIGHT), Image.ANTIALIAS)
    return boardify(resized_image, 16)


def boardify(image, pixel_size) -> list[list[Tile]]:
    """Return a matrix of game tiles given an image."""
    tile_matrix = [[Tile() for _ in range(config.BOARD_WIDTH)]
                   for _ in range(config.BOARD_HEIGHT)]
    rgb_list = list(image.convert("RGB").getdata())

    for i in range(len(rgb_list)):
        tile = GrassTile() if colour_diff(config.WATER_COLOUR, rgb_list[i]) \
                              > config.DIFF_THRESHOLD else WaterTile()
        tile_matrix[i // config.BOARD_WIDTH][i % config.BOARD_WIDTH] = tile
    return tile_matrix


def colour_diff(colour1: tuple[int, int, int], colour2: tuple[int, int, int]) -> int:
    """ Return a numeric difference in colour from 2 colours in RGB format."""
    return sum(abs(colour1[i] - colour2[i]) for i in range(3))


# Example
def example_map() -> list[list[Tile]]:
    image = Image.open('images/test_map.png')
    return generate_gameboard(image)


# Debug
if __name__ == '__main__':
    example_map()
