""" The game module will contain the game and all its high-level classes. """
from __future__ import annotations
from typing import Optional

from config import *


# GAME


class Game:
    """ The game.

    Instance Attributes:
        - players: A list of players of the game. Player 0 will be the user.
        - current_turn: The index of 'players' who's turn it currently is.
        - game_map:  A tile matrix that represents a map of the game.
        - structures:  A tile matrix that represents a map of all the structures.
        - discovered_tiles: A tile matrix of whether or not a tile is covered by a cloud.
    """
    players: list[Player]
    current_turn: int
    game_map: list[list[Tile]]
    structures: list[list[Optional[Tile]]]
    discovered_tiles: list[list[Optional[Tile]]]

    def __init__(self, players: list[Player], game_map: list[list[Tile]],
                 enable_discovery_tiles: bool = True) -> None:
        self.players = players
        self.game_map = game_map
        self.current_turn = 0
        self.structures = [[None for i in range(BOARD_WIDTH)]
                           for j in range(BOARD_HEIGHT)]

        # Discovery tiles
        self.discovered_tiles = [[CloudTile() for i in range(BOARD_WIDTH)]
                                 for j in range(BOARD_HEIGHT)] if enable_discovery_tiles \
            else [[None for i in range(BOARD_WIDTH)]
                  for j in range(BOARD_HEIGHT)]

        for player in players:
            for unit in player.units:
                self.discover_tiles(unit.position)  # Initially discovered tiles

    def is_user_turn(self) -> bool:
        """ Return whether or not the current turn is the user's turn. """
        return self.current_turn == 0

    def next_turn(self) -> None:
        """ Update the current turn to be the turn of the next player. """
        self.current_turn = (self.current_turn + 1) % len(self.players)

        # Resets all the moves for all the units of the new current player.
        new_current_player = self.players[self.current_turn]
        for unit in new_current_player.units:
            unit.reset_moves()

        # Update the production for all the cities of the new current player.
        for city in new_current_player.cities:
            city.update_production()

        print(f"It is now {self.players[self.current_turn].name}'s turn.")

    def create_city(self, player: Player, position: list[int]) -> None:
        """ Create a new city in the game. """
        new_city = City('Madrid', player, position)
        player.cities.append(new_city)
        self.structures[position[1]][position[0]] = new_city

    def discover_tiles(self, position: list[int]) -> None:
        """ Discover new tiles on the map given a position. """
        for y in range(position[1] - 1, position[1] + 2):
            for x in range(position[0] - 1, position[0] + 2):
                if self.within_map_border([x, y]):
                    self.discovered_tiles[y][x] = None

    @staticmethod
    def within_map_border(position: list[int]) -> bool:
        """ Return whether an [x, y] position is within the map border. """
        return 0 <= position[0] < BOARD_WIDTH and 0 <= position[1] < BOARD_HEIGHT

    def render_game(self) -> list[list[str]]:
        """ Renders the game in a (3*BOARD_WIDTH)x(3*BOARD_HEIGHT) pixel matrix of colours in
            the form '#FFFFFF'.
        """
        output = [['#000000' for i in range(BOARD_WIDTH * 3)]
                  for j in range(BOARD_HEIGHT * 3)]

        # Render map & structures
        Game._render_tilemap(self.game_map, output)
        Game._render_tilemap(self.structures, output)

        # Render units
        for player in self.players:
            for unit in player.units:
                # Rip this nested ternary operator 😔
                unit_vis = SETTLER_UNIT if isinstance(unit, Settler) else \
                    (WARRIOR_UNIT if isinstance(unit, Warrior) else WORKER_UNIT)

                Game._render_vis(unit_vis, [unit.position[0], unit.position[1]], output)

        # Find which item is currently selected and render the selection outline around it
        current_player = self.players[self.current_turn]
        focused_view = current_player.current_view
        focused_item = current_player.units[current_player.selected_unit] \
            if focused_view == 'unit' else current_player.cities[current_player.selected_city]

        Game._render_selection_outline(focused_item.position, output, current_player)

        # Cover the map with undiscovered tile clouds
        Game._render_tilemap(self.discovered_tiles, output)

        return output

    @staticmethod
    def _render_tilemap(tilemap: list[list[Tile]], output: list[list[str]]) -> None:
        """ Helper function for render_game() that renders tilemaps to the output matrix. """
        for tile_y in range(BOARD_HEIGHT):
            for tile_x in range(BOARD_WIDTH):
                current_tile = tilemap[tile_y][tile_x]

                if current_tile:
                    Game._render_vis(current_tile.vis, [tile_x, tile_y], output)

    @staticmethod
    def _render_vis(vis: list[list[str]], pos: list[int], output: list[list[str]]) -> None:
        """ Helper function which will update the output matrix with a visualization."""
        for y in range(3):
            for x in range(3):
                colour = vis[y][x]

                if colour:
                    output[pos[1] * 3 + y][pos[0] * 3 + x] = colour

    @staticmethod
    def _render_selection_outline(pos: list[int], output: list[list[str]], player: Player) -> None:
        """ Render the selection outline to the output matrix. """
        selection_outline = [[OUTLINE_COLOURS[player.name] if max(i, j) == 6 or min(i, j) == 0
                              else None for i in range(7)] for j in range(7)]
        for y in range(7):
            for x in range(7):
                colour = selection_outline[y][x]

                vis_pos = [pos[0] * 3 - 2 + x, pos[1] * 3 - 2 + y]
                if colour and Game._vis_within_map_border(vis_pos):
                    output[vis_pos[1]][vis_pos[0]] = colour

    @staticmethod
    def _vis_within_map_border(vis_pos: list[int]) -> bool:
        """ Return whether an [x, y] vis position is within the map render border. """
        return 0 <= vis_pos[0] < BOARD_WIDTH * 3 and 0 <= vis_pos[1] < BOARD_HEIGHT * 3

    def handle_user_input(self, keycode: str) -> None:
        """ Handle user input for a player."""
        self.players[self.current_turn].handle_user_input(keycode, self)

    def generate_info(self) -> dict[str, str]:
        """ Generate the info box of the game depending on the current game state."""
        current_player = self.players[self.current_turn]

        current_view_text = VIEW_TEXTS[current_player.current_view]
        if current_player.current_view == 'unit':
            current_unit = current_player.units[current_player.selected_unit]

            name = current_unit.name
            message = f"Position: {current_unit.position} ⠀⠀ Moves Left: {current_unit.moves_left}"
            lst = [unit.name for unit in current_player.units]
            controls = f"SPACE - {current_unit.action_name} ⠀⠀ " + \
                       "Enter - Switch Unit ⠀⠀ Arrow Keys - Move Unit ⠀⠀ TAB - Switch View ⠀⠀ " + \
                       "ESC - End Turn"
        else:
            current_city = current_player.cities[current_player.selected_city]

            name = current_city.name
            lst = [city.name for city in current_player.cities]

            if current_player.current_view == 'city':
                message = f"Position: {current_city.position} ⠀⠀ " + \
                          f"Production: {current_city.current_production}" + \
                          f"({current_city.production_turns_left} Turns left.)"

                controls = "SPACE - Choose Production ⠀⠀ Enter - Switch City ⠀⠀ " + \
                           "TAB - Switch View ⠀⠀ ESC - End Turn"
            else:  # production view
                message = f"Choose your Production for {current_city.name} (4 turns per unit)"

                controls = "ArrowUp - Settler ⠀⠀ ArrowLeft - Warrior ⠀⠀ ArrowRight - Worker ⠀⠀ " + \
                           "TAB - Switch View ⠀⠀ ESC - End Turn"

        return {'title': f"{current_player.name}'s Turn - {current_view_text} - {name}",
                'message': message,
                'list': ', '.join(lst),
                'controls': controls}

        # TODO: Fix the thing where when you have no units, you can't be in unit view.


class Player:
    """ A player of the game.

    Instance Attributes:
        - name: The name of the player/civilization.
        - units: A list of all the player's units
        - cities: A list of all the player's cities
        - selected_unit: The index of 'units' that the player currently has selected.
        - selected_city: The index of 'cities' that the player currently has selected.
        - current_view: The current view of the player (of 'city', 'unit' and 'production')
        - eliminated: Whether or not the player is eliminated.
            (Players are eliminated when all their units and cities are destroyed)
    """
    name: str
    units: list[Unit]
    cities: list[City]

    selected_unit: int
    selected_city: int

    current_view: str

    eliminated: bool

    def __init__(self, name, settler_spawn_location: list[int]) -> None:
        self.name = name
        self.units = [Settler(self, settler_spawn_location)]  # This spawns the players first unit
        self.cities = []

        self.selected_unit = 0
        self.selected_city = 0

        self.current_view = 'unit'

    def remove_unit(self, unit: Unit) -> None:
        """ Delete this unit. """
        self.units.remove(unit)

    def handle_user_input(self, keycode: str, game: Game) -> None:
        """ Handle user input for the current player."""

        if keycode == 'Escape':  # The universal
            game.next_turn()

        # UNIT VIEW
        if self.current_view == 'unit' and len(self.units) > 0:
            if keycode == 'Tab':
                self.current_view = 'city'
            elif keycode == 'Space':
                self.units[self.selected_unit].action(game)
            elif keycode == 'Enter':
                self.selected_unit = (self.selected_unit + 1) % len(self.units)
            else:  # Movement
                self.units[self.selected_unit].move_unit(keycode, game)

        # CITY VIEW
        elif self.current_view == 'city':
            if keycode == 'Tab':
                self.current_view = 'unit'
            elif keycode == 'Space':
                self.current_view = 'production'
            elif keycode == 'Enter':
                self.selected_city = (self.selected_city + 1) % len(self.cities)
            else:  # Movement
                self.units[self.selected_unit].move_unit(keycode, game)

        # Lastly, update the player state
        self.update_player_state(game)

    def update_player_state(self, game: Game) -> None:
        """ Switches the view or detects if eliminated. """
        if not self.units:
            self.current_view = 'city'

        if not self.cities:
            self.current_view = 'unit'

        if not self.cities and not self.units:
            self.eliminated = True

            # This isn't very elegant, but I'm running low on hackathon time
            game.players.remove(self)


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
        self.vis = GRASS_TILE


class WaterTile(Tile):
    """ A water tile. """

    def __init__(self) -> None:
        self.vis = WATER_TILE


class City(Tile):
    """ A city tile.

    Instance Attributes:
        - name: The name of the city.
        - owner: The owner of the city.
        - current_production: The unit that this city is currently producing.
        - production_turns_left: The number of turns left until the unit is finished.
        - position: the position of the city on the board.
    """
    name: str
    owner: Player
    current_production: str
    production_turns_left: int
    position: list[int]

    def __init__(self, name: str, owner: Player, position: list[int]) -> None:
        self.vis = CITY_TILE
        self.name = name
        self.owner = owner
        self.current_production = ''
        self.production_turns_left = 0
        self.position = position

    def set_production(self, unit: str) -> None:
        """ Sets the production of the current city. """

    def update_production(self):
        """ Updates the status of the production. """


class Road(Tile):
    """ A road tile.

    Instance Attributes:
        - road_connections: A tuple of 4 bools representing which of the 4 directions
            (up, down, left, right) that this road is connected to.
    """
    road_connections: tuple[bool, bool, bool, bool]

    def __init__(self) -> None:
        self.vis = ROAD_TILE


class CloudTile(Tile):
    """ A cloud tile. """

    def __init__(self):
        self.vis = CLOUD_TILE


# UNITS


class Unit:
    """ A Miniciv unit abstract class.

    Instance Attributes
        - name: The unit name (the same as unit type)
        - owner: The player who owns this unit.
        - moves_left: the moves this unit has left for the current turn.
        - position: the (x, y) position of the unit on the game board.
        - action_name: the action display text of the unit's special action.
    """
    name: str
    owner: Player
    moves_left: int
    position: list[int]
    action_name: str

    def __init__(self, owner: Player, position: list[int]) -> None:
        self.owner = owner
        self.position = position

    def reset_moves(self) -> None:
        """ Reset the current unit's moves. """
        raise NotImplementedError

    def move_unit(self, direction: str, game: Game) -> bool:
        """ Move the unit one tile in a direction. Return false if illegal move.
            The unit will not use up a move if the unit is standing on a road tile. """

        current_structure = game.structures[self.position[1]][self.position[0]]

        # Not able to move if no moves left
        if self.moves_left <= 0:
            return False

        new_position = self.position.copy()
        # Movement code
        if direction == 'ArrowDown':
            new_position[1] += 1
        elif direction == 'ArrowUp':
            new_position[1] -= 1
        elif direction == 'ArrowLeft':
            new_position[0] -= 1
        elif direction == 'ArrowRight':
            new_position[0] += 1

        # Make sure you didn't go on water or outside of the map
        if not game.within_map_border(new_position) or \
                isinstance(game.game_map[new_position[1]][new_position[0]], WaterTile):
            return False

        self.position = new_position
        print(f"Moved {self.owner.name}'s {self.name} to {new_position}.")

        # Take away a move
        if not isinstance(current_structure, Road):
            self.moves_left -= 1

        # Discover new tiles
        game.discover_tiles(self.position)
        return True

    def action(self, game: Game):
        """ The special action of this unit."""
        raise NotImplementedError


class Settler(Unit):
    """ A Miniciv settler unit. """

    def __init__(self, owner: Player, position: list[int]) -> None:
        super().__init__(owner, position)
        self.moves_left = 4
        self.name = 'Settler'
        self.action_name = 'Found City'

    def reset_moves(self) -> None:
        self.moves_left = 4

    def action(self, game: Game) -> bool:
        """ Found a city on the game board. Return false if illegal move."""
        if not game.structures[self.position[1]][self.position[0]] \
                and not isinstance(game.game_map[self.position[1]][self.position[0]], WaterTile):
            # Creates the city, then removes itself from the game.
            game.create_city(self.owner, self.position)
            self.owner.remove_unit(self)

            print(f'{self.owner.name} founded the city {self.owner.cities[-1].name}.')
            return True
        return False


class Warrior(Unit):
    """ A Miniciv warrior unit. """

    def __init__(self, owner: Player, position: list[int]) -> None:
        super().__init__(owner, position)
        self.moves_left = 3
        self.name = 'Warrior'
        self.action_name = 'Guard Tile'

    def reset_moves(self) -> None:
        self.moves_left = 3

    def action(self, game: Game):
        """ Sadly, the warrior has no special action in Miniciv because of hackathon time
         restrictions. :'( """


class Worker(Unit):
    """ A Miniciv worker unit. """

    def __init__(self, owner: Player, position: list[int]) -> None:
        super().__init__(owner, position)
        self.moves_left = 8
        self.name = 'Worker'
        self.action_name = 'Build Road'

    def reset_moves(self) -> None:
        self.moves_left = 8

    def action(self, game: Game):
        """ Build a road on the game board. Return false if illegal move."""


# Top-level Functions

def to_tilemap(string_map: list[list[str]]) -> list[list[Tile]]:
    """ Convert a matrix of strings to a matrix of grass and water tiles.
        The strings in the input matrix must be either 'grass' or 'water'.
    """
    # TODO: Implement this function.


# Debug
if __name__ == '__main__':
    p = [Player('Spain', [0, 0]), Player('Zulu', [10, 4]), Player('Russia', [4, 4])]
    m = [[GrassTile() for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
    g = Game(p, m)
