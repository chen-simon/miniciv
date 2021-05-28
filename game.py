""" The game module will contain the game and all its high-level classes. """
from __future__ import annotations
from typing import Optional

import config


# GAME


class Game:
    """ The game.

    Instance Attributes:
        - players: A list of players of the game. Player 0 will be the user.
        - current_turn: The index of 'players' who's turn it currently is.
        - game_map:  A tile matrix that represents a map of the game.
        - structures:  A tile matrix that represents a map of all the structures.

    """
    players: list[Player]
    current_turn: int
    game_map: list[list[Tile]]
    structures: list[list[Optional[Tile]]]

    def __init__(self, players: list[Player], game_map: list[list[Tile]]) -> None:
        self.players = players
        self.game_map = game_map
        self.current_turn = 0
        self.structures = [[None for i in range(config.BOARD_WIDTH)]
                           for j in range(config.BOARD_HEIGHT)]

    def is_user_turn(self) -> bool:
        """ Return whether or not the current turn is the user's turn. """
        return self.current_turn == 0

    def next_turn(self) -> None:
        """ Update the current turn to be the turn of the next player. """
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def render_game(self) -> list[list[str]]:
        """ Renders the game in a (3*BOARD_WIDTH)x(3*BOARD_HEIGHT) pixel matrix of colours in
            the form '#FFFFFF'.
        """
        output = [['#000000' for i in range(config.BOARD_WIDTH * 3)]
                  for j in range(config.BOARD_HEIGHT * 3)]

        # Render map & structures
        Game._render_tilemap(self.game_map, output)
        Game._render_tilemap(self.structures, output)

        # Render units
        for player in self.players:
            for unit in player.units:
                # Rip this nested ternary operator 😔
                unit_vis = config.SETTLER_UNIT if isinstance(unit, Settler) else \
                    (config.WARRIOR_UNIT if isinstance(unit, Warrior) else config.WORKER_UNIT)

                Game._render_vis(unit_vis, [unit.position[1], unit.position[0]], output)

        return output

    @staticmethod
    def _render_tilemap(tilemap: list[list[Tile]], output: list[list[str]]) -> None:
        """ Helper function for render_game() that renders tilemaps to the output matrix. """
        for tile_y in range(config.BOARD_HEIGHT):
            for tile_x in range(config.BOARD_WIDTH):
                current_tile = tilemap[tile_y][tile_x]

                if current_tile:
                    Game._render_vis(current_tile.vis, [tile_x, tile_y], output)

    @staticmethod
    def _render_vis(vis: list[list[str]], pos: list[int], output: list[list[str]]) -> None:
        """ Helper function which will update the output matrix with a visualization."""
        for y in range(3):
            for x in range(3):
                colour = vis[y][x]

                if colour != '':
                    output[pos[1] * 3 + y][pos[0] * 3 + x] = colour


class Player:
    """ A player of the game.

    Instance Attributes:
        - name: The name of the player/civilization.
        - units: A list of all the player's units
        - cities: A list of all the player's cities
        - selected_unit: The index of 'units' that the player currently has selected.
        - selected_city: The index of 'cities' that the player currently has selected.
    """
    name: str
    units: list[Unit]
    cities: list[City]

    selected_unit: int
    selected_city: int

    def __init__(self, name, settler_spawn_location: list[int]) -> None:
        self.name = name
        self.units = [Settler(self, settler_spawn_location)]  # This spawns the players first unit
        self.cities = []

    def move_unit(self) -> None:
        """ Move the current unit in a direction"""
        # TODO: implement this function

    def end_turn(self) -> None:
        """ ends the player's turn """
        # TODO: implement this function

    def destroy_city(self):
        pass


# TILES


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
        self.vis = config.GRASS_TILE


class WaterTile(Tile):
    """ A water tile. """
    def __init__(self) -> None:
        self.vis = config.WATER_TILE


class City(Tile):
    """ A city tile.

    Instance Attributes:
        - name: The name of the city.
    """
    name: str
    owner: Player

    def __init__(self) -> None:
        self.vis = config.CITY_TILE


class Road(Tile):
    """ A road tile.

    Instance Attributes:
        - road_connections: A tuple of 4 bools representing which of the 4 directions
            (up, down, left, right) that this road is connected to.
    """
    road_connections: tuple[bool, bool, bool, bool]

    def __init__(self) -> None:
        self.vis = config.ROAD_TILE


# UNITS


class Unit:
    """ A Miniciv unit abstract class.

    Instance Attributes
        - owner: The player who owns this unit.
        - moves_left: the moves this unit has left for the current turn.
        - position: the (x, y) position of the unit on the game board.
    """
    owner: Player
    moves_left: int
    position: list[int]

    def __init__(self, owner: Player, position: list[int]) -> None:
        self.owner = owner
        self.position = position

    def reset_moves(self) -> None:
        """ Reset the current unit's moves. """
        raise NotImplementedError

    def move_unit(self, direction: str, current_tile: Tile) -> bool:
        """ Move the unit one tile in a direction. Return false if illegal move.
            The unit will not use up a move if the unit is standing on a road tile. """

        # Not able to move if no moves left
        if self.moves_left <= 0:
            return False

        # Movement code
        if direction == 'up' and self.position[1] < config.BOARD_HEIGHT - 1:
            self.position[1] += 1
        elif direction == 'down' and self.position[1] > 0:
            self.position[1] -= 1
        elif direction == 'left' and self.position[0] > 0:
            self.position[0] -= 1
        elif direction == 'right' and self.position[0] < config.BOARD_WIDTH - 1:
            self.position[0] += 1
        else:
            return False

        # Take away a move
        if not isinstance(current_tile, Road):
            self.moves_left -= 1
        return True


class Settler(Unit):
    """ A Miniciv settler unit. """

    def __init__(self, owner: Player, position: list[int]) -> None:
        super().__init__(owner, position)
        self.moves_left = 4

    def reset_moves(self) -> None:
        self.moves_left = 4

    def found_city(self, game_board) -> None:
        """ Found a city on the game board. """


class Warrior(Unit):
    """ A Miniciv warrior unit. """

    def __init__(self, owner: Player, position: list[int]) -> None:
        super().__init__(owner, position)
        self.moves_left = 3

    def reset_moves(self) -> None:
        self.moves_left = 3


class Worker(Unit):
    """ A Miniciv worker unit. """

    def __init__(self, owner: Player, position: list[int]) -> None:
        super().__init__(owner, position)
        self.moves_left = 8

    def reset_moves(self) -> None:
        self.moves_left = 8


# Top-level Functions

def to_tilemap(string_map: list[list[str]]) -> list[list[Tile]]:
    """ Convert a matrix of strings to a matrix of grass and water tiles.
        The strings in the input matrix must be either 'grass' or 'water'.
    """
    # TODO: Implement this function.


# Debug
if __name__ == '__main__':
    p = [Player('Spain', [0, 0]), Player('Zulu', [10, 4]), Player('Russia', [4, 4])]
    m = [[GrassTile() for i in range(config.BOARD_WIDTH)] for j in range(config.BOARD_HEIGHT)]
    g = Game(p, m)
