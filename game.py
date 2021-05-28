""" The game module will contain the game and all its high-level classes. """
from __future__ import annotations
import config


class Game:
    """ The game.

    Instance Attributes:
        - players: A list of players of the game. Player 0 will be the user.
        - current_turn: The index of 'players' who's turn it currently is.
        - game_map: The map of the game.
    """
    players: list[Player]
    current_turn: int
    game_map: Map

    def __init__(self, players: list[Player], game_map: Map) -> None:
        self.players = players
        self.game_map = game_map
        self.current_turn = 0

    def is_user_turn(self) -> bool:
        """ Return whether or not the current turn is the user's turn. """
        return self.current_turn == 0

    def next_turn(self) -> None:
        """ Update the current turn to be the turn of the next player. """
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def render_game(self) -> list[list[str]]:
        """ Renders the game in a 120x48 pixel matrix of colours in the form '#FFFFFF'. """
        # TODO: Implement this method.


class Map:
    """ The map.

    Instance Attributes:
        - structure: A tile matrix containing all the structural tiles (City, road).
        - natural: A tile matrix containing all the natural tiles.
    """
    structure: list[list[Tile]]
    natural: list[list[Tile]]

    def __init__(self) -> None:
        pass


class Player:
    """ A player of the game.

    Instance Attributes:
        - name: The name of the player/civilization.
    """
    name: str
    units: list[Unit]
    cities: list[City]

    def __init__(self, name, settler_spawn_location: list[int, int]) -> None:
        self.name = name
        units = [Settler(settler_spawn_location)]  # This spawns the players first unit
        cities = []

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
        vis = config.GRASS_TILE


class WaterTile(Tile):
    """ A water tile. """
    def __init__(self) -> None:
        vis = config.WATER_TILE


class City(Tile):
    """ A city tile.

    Instance Attributes:
        - name: The name of the city.
    """
    name: str
    owner: Player

    def __init__(self) -> None:
        vis = config.CITY_TILE


class Road(Tile):
    """ A road tile.

    Instance Attributes:
        - road_connections: A tuple of 4 bools representing which of the 4 directions
            (up, down, left, right) that this road is connected to.
    """
    road_connections: tuple[bool, bool, bool, bool]

    def __init__(self) -> None:
        vis = config.ROAD_TILE


# UNITS


class Unit:
    """ A Miniciv unit abstract class.

    Instance Attributes
        - moves_left: the moves this unit has left for the current turn.
        - position: the (x, y) position of the unit on the game board.
    """
    owner: Player
    moves_left: int
    position: list[int, int]

    # def __init__(self, unit_type: str, position: tuple[int, int]) -> None:
    #     raise NotImplementedError

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
        if direction == 'up' and self.position[1] < board.HEIGHT - 1:
            self.position[1] += 1
        elif direction == 'down' and self.position[1] > 0:
            self.position[1] -= 1
        elif direction == 'left' and self.position[0] > 0:
            self.position[0] -= 1
        elif direction == 'right' and self.position[0] < board.WIDTH - 1:
            self.position[0] += 1
        else:
            return False

        # Take away a move
        if not isinstance(current_tile, Road):
            self.moves_left -= 1
        return True


class Settler(Unit):
    """ A Miniciv settler unit. """

    def __init__(self, position: list[int, int]) -> None:
        self.position = position
        self.moves_left = 4

    def reset_moves(self) -> None:
        self.moves_left = 4

    def found_city(self, game_board) -> None:
        """ Found a city on the game board. """


class Warrior(Unit):
    """ A Miniciv warrior unit. """

    def __init__(self, position: list[int, int]) -> None:
        self.position = position
        self.moves_left = 3

    def reset_moves(self) -> None:
        self.moves_left = 3


class Worker(Unit):
    """ A Miniciv worker unit. """

    def __init__(self, position: list[int, int]) -> None:
        self.position = position
        self.moves_left = 8

    def reset_moves(self) -> None:
        self.moves_left = 8


# Debug
if __name__ == '__main__':
    p = [Player('Spain', [0, 0]), Player('Zulu', [0, 4]), Player('Russia', [4, 4])]
    m = Map()
    g = Game(p, m)
