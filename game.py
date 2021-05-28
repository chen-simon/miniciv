""" The game module will contain the game. """
from __future__ import annotations


class Game:
    """ The game. """
    players: list[Player]  # A list of players of the game
    current_turn: int  # The index of 'players' who's turn it currently is
    game_map: Map  # The map of the game

    def __init__(self, players: list[Player], game_map: Map = Map()) -> None:
        self.players = players
        self.game_map = game_map
        self.current_turn = 0


class Map:
    """ The map. """

class Player:
    """ A player of the game. """

    def move_unit(self) -> None:
        """ Move the current unit in a direction"""
        # TODO: implement this function

    def end_turn(self) -> None:
        """ ends the player's turn """
        # TODO: implement this function
