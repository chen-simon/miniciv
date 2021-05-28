""" The module containing all Miniciv's units. """
import board
from tiles import *


class Unit:
    """ A Miniciv unit abstract class.

    Instance Attributes
        - moves_left: the moves this unit has left for the current turn.
        - position: the (x, y) position of the unit on the game board.
    """
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
