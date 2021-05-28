""" A module containing all the game tiles. """
from __future__ import annotations
import graphics


class Tile:
    """ A tile of the map. """
    name: str
    vis: graphics.TileGraphic

    def __init__(self, vis: graphics.TileGraphic) -> None:
        self.vis = vis


TILES = {'grass': Tile(graphics.GRASS_TILE),
         'water': Tile()}
