""" A module containing all the game tiles. """
from __future__ import annotations
from player import Player
import graphics


class Tile:
    """ An abstract class of a tile of the map.

    Instance Attributes:
        - vis: the 3x3 colour array. Colours are strings in the form '#FFFFFF' or '' empty string
            for transparent pixels. There are no semi-transparent.
    """
    vis: list[list[str]]


class GrassTile(Tile):
    """ A grass tile """

    def __init__(self) -> None:
        vis = graphics.GRASS_TILE


class WaterTile(Tile):
    """ A water tile. """
    def __init__(self) -> None:
        vis = graphics.WATER_TILE


class City(Tile):
    """ A city tile.

    Instance Attributes:
        - name: The name of the city.
    """
    name: str
    owner: Player

    def __init__(self) -> None:
        vis = graphics.CITY_TILE


class Road(Tile):
    """ A road tile.

    Instance Attributes:
        - road_connections: A tuple of 4 bools representing which of the 4 directions
            (up, down, left, right) that this road is connected to.
    """
    road_connections: tuple[bool, bool, bool, bool]

    def __init__(self) -> None:
        vis = graphics.ROAD_TILE


