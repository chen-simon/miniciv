""" The game server. """
from flask import Flask, render_template, url_for, request
import json

from game import *

app = Flask(__name__)
current_game = None  # Game([], Map())


# #### TILE DEBUGGING #### #
@app.route('/debug/')
def debug_tile():
    return render_template('debug.html')


@app.route('/debug/tile/')
def send_tile():
    import graphics  # CHANGE THIS CODE TO SEE WHAT TILE YOU ARE LOOKING AT
    return {'screen': graphics.ROAD_TILE}


# Game
@app.route('/game/generate/', methods=['POST'])
def generate():
    request.get_data()


@app.route('/game/')
def game():
    return render_template('game.html')


if __name__ == '__main__':
    app.run(debug=True)
