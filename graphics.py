""" The game's graphics. """
# Terrain Tiles

GRASS_TILE = [['#5cb528', '#569e2c', '#54b048'],
              ['#58b34d', '#40b334', '#54b048'],
              ['#5cb528', '#5cb528', '#569e2c']]

WATER_TILE = [['#0044ff', '#2d79eb', '#0044ff'],
              ['#2d79eb', '#0044ff', '#081cfc'],
              ['#081cfc', '#0044ff', '#2d79eb']]

# main: #0044ff
# darker: #081cfc
# lighter: #2d79eb

# Structure Tiles

ROAD_TILE = [['#000000', '#4a2912', '#000000'],
             ['#4a2912', '#6b3c1c', '#874f29'],
             ['#000000', '#874f29', '#000000']]

CITY_UNIT = [['#000000', '#595858', '#000000'],
             ['#595858', '#595858', '#595858'],
             ['#595858', '#595858', '#595858']]

# main: #6b3c1c
# darker: #4a2912
# lighter: #874f29


# Unit Tiles

SETTLER_UNIT = [['#000000', '#528c35', '#000000'],
                ['#000000', '#dadbd7', '#000000'],
                ['#000000', '#000000', '#000000']]
# USE THIS HEX IF IT BLENDS INTO THE GRASS: e8e117

WARRIOR_UNIT = [['#000000', '#eb441e', '#000000'],
                ['#000000', '#dadbd7', '#000000'],
                ['#000000', '#000000', '#000000']]

WORKER_UNIT = [['#000000', '#eda915', '#000000'],
               ['#000000', '#dadbd7', '#000000'],
               ['#000000', '#000000', '#000000']]


class TileGraphic:
    """ The 3x3 pixel graphic that a tile will render as.

    Instance Attributes
        - vis: the 3x3 colour array. Colours are strings in the form '#FFFFFF' or '' empty string
            for transparent pixels. There are no semi-transparent.

    """
    vis: list[list[str]]

    def __init__(self, vis: list[list[str]]) -> None:
        self.vis = vis
