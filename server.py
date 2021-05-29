""" The game server. """
from flask import Flask, render_template, url_for, request
import json

from config import *
from map_generation import example_map
from game import *

app = Flask(__name__)

p = [Player('Spain', [0, 0]), Player('Zulu', [0, 4]), Player('Russia', [4, 4])]
m = [[GrassTile() for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
current_game = Game(p, m)


# #### TILE DEBUGGING #### #
@app.route('/debug/')
def debug_tile():
    return render_template('debug.html')


@app.route('/debug/tile/')
def send_tile():
    import config  # CHANGE THIS CODE TO SEE WHAT TILE YOU ARE LOOKING AT
    return {'screen': ROAD_TILE}


# Game
@app.route('/game/generate/', methods=['POST'])
def generate():
    request.get_data()
    return {}


@app.route('/game/')
def game():
    return render_template('game.html')


@app.route('/game/io/', methods=['POST'])
def game_io():
    data = json.loads(request.get_data())

    # Handle user input to update game state
    if 'key' in data:
        current_game.handle_user_input(data['key'])

    info = current_game.generate_info()
    return {'screen': current_game.render_game(), **info}


if __name__ == '__main__':
    p = [Player('America', [2, 2]), Player('Spain', [4, 4])]
    p[0].units.append(Worker(p[0], [30, 5]))
    m = example_map()
    current_game = Game(p, m, enable_discovery_tiles=False)

    app.run(debug=True)
