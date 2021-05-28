""" The game module will contain the game and all its high-level classes. """
from __future__ import annotations
from tiles import *
from player import Player


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
    structure = list[list[Tile]]
    natural = list[list[Tile]]

    def __init__(self) -> None:
        pass


# Debug
if __name__ == '__main__':
    p = [Player(), Player(), Player()]
    m = Map()
    g = Game(p, m)
