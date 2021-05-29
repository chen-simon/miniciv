""" The game server. """
from flask import Flask, render_template, url_for, request, redirect
import json
from random import choice

from api_key import API_KEY
from config import *
import map_generation
from game import *

app = Flask(__name__)

current_game = [Game([], [])]


# Start
@app.route('/')
def start():
    return render_template('start.html', api_key=API_KEY)


@app.route('/start/', methods=['POST'])
def start_game():
    data = json.loads(request.get_data())

    # THIS INITIALIZES THE GAME
    data = json.loads(request.get_data())
    game_map = map_generation.generate(data['lat'], data['lng'], data['zoom'])
    valid_positions = Game.get_valid_positions(game_map)
    players = [Player(data['playername'], choice(valid_positions)),
               Player('Spain', choice(valid_positions)), Player('Russia',
                                                                choice(valid_positions))]

    new_game = Game(players, game_map, enable_discovery_tiles=False)

    current_game[0] = new_game  # Python-scoping jankiness for persistent server session

    return {}


# Game
@app.route('/game/generate/', methods=['POST'])
def generate():
    request.get_data()
    return {}


@app.route('/game/')
def game():
    print(current_game[0])
    print('^^ for the /game/ reuqest')
    return render_template('game.html')


@app.route('/game/io/', methods=['POST'])
def game_io():
    data = json.loads(request.get_data())

    # Handle user input to update game state
    if 'key' in data:
        current_game[0].handle_user_input(data['key'])

    info = current_game[0].generate_info()
    return {'screen': current_game[0].render_game(), **info}


if __name__ == '__main__':
    # p = [Player('America', [2, 2]), Player('Spain', [4, 4])]
    # p[0].units.append(Worker(p[0], [30, 5]))
    # m = map_generation.example_map()
    # current_game = Game(p, m, enable_discovery_tiles=False)

    app.run(debug=True)
