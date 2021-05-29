""" A module to convert a given image to a miniciv gameboard map"""
from typing import Any
from PIL import Image

import config
from game import Tile, GrassTile, WaterTile


def generate_gameboard(image: Image) -> list[list[Tile]]:
    """Create the gameboard given an image"""
    resized_image = image.resize((config.BOARD_WIDTH, config.BOARD_HEIGHT), Image.ANTIALIAS)
    return boardify(resized_image)


def boardify(image: Image) -> list[list[Tile]]:
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
    """ Return the example map"""
    image = Image.open('images/test_map.png')
    return generate_gameboard(image)


def google_maps_url_to_image(url: str) -> Image:
    """ Call the google maps static api, given a url, and return a Pillow image."""
    # TODO: Implement this function, Zhenia.


# Debug
if __name__ == '__main__':
    img = google_maps_url_to_image('https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=12&size=640x256&maptype=roadmap&style=feature:all%7Cvisibility:off&style=feature:landscape%7Cvisibility:on&style=feature:landscape%7Celement:geometry.fill%7Ccolor:0x000000&style=feature:water%7Cvisibility:on&style=feature:water%7Celement:geometry.fill%7Ccolor:0x0000FF&key=AIzaSyB_NnU8wRTS5S0dFjS_5kUhtuetWqY0xWI')
    img.show()
