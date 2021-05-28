""" The player module class thing. """
# from units import Unit
from tiles import City


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

