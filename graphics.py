""" The game's graphics. """

GRASS_TILE = [['#5cb528', '#569e2c', '#54b048'],
              ['#58b34d', '#40b334', '#54b048'],
              ['#5cb528', '#5cb528', '#569e2c']]

WATER_TILE = [['#5cb528', '#569e2c', '#54b048'],
              ['#58b34d', '#40b334', '#54b048'],
              ['#5cb528', '#569e2c', '#40b334']]


class TileGraphic:
    """ The 3x3 pixel graphic that a tile will render as.

    Instance Attributes
        - vis: the 3x3 colour array. Colours are strings in the form '#FFFFFF' or '' empty string
            for transparent pixels. There are no semi-transparent.

    """
    vis: list[list[str]]

    def __init__(self, vis: list[list[str]]) -> None:
        self.vis = vis
