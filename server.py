""" The game server. """
from flask import Flask, render_template, url_for, request
import game
import json

from game import *

app = Flask(__name__)

p = [Player('Spain', [0, 0]), Player('Zulu', [0, 4]), Player('Russia', [4, 4])]
m = [[GrassTile() for i in range(config.BOARD_WIDTH)] for j in range(config.BOARD_HEIGHT)]
current_game = Game(p, m)


# #### TILE DEBUGGING #### #
@app.route('/debug/')
def debug_tile():
    return render_template('debug.html')


@app.route('/debug/tile/')
def send_tile():
    import config  # CHANGE THIS CODE TO SEE WHAT TILE YOU ARE LOOKING AT
    return {'screen': config.ROAD_TILE}


# Game
@app.route('/game/generate/', methods=['POST'])
def generate():
    request.get_data()
    return {}


@app.route('/game/')
def game():
    return render_template('game.html')


@app.route('/game/io/', methods=['GET', 'POST'])
def game_io():
    return {'screen': current_game.render_game()}


if __name__ == '__main__':
    p = [Player('Spain', [2, 2]), Player('Russia', [4, 4])]
    m = [[GrassTile() for i in range(config.BOARD_WIDTH)] for j in range(config.BOARD_HEIGHT)]
    current_game = Game(p, m)

    app.run(debug=True)
