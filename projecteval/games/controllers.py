from flask import Blueprint, request, jsonify, render_template, flash

import json

from projecteval import db

from projecteval.api.models import Game, Platform

import projecteval.api.controllers as api

import projecteval.helper.controllers as helper

games = Blueprint('games', __name__)


# Game
@games.route('/games/', methods=['GET'])
def all_games():
    response = api.all_games()
    helper.check_response(response)
    games = json.loads(response.data)
    games = games["games"]
    return render_template("games/games.html", games=games)

@games.route('/games/<int:id>', methods=['GET'])
def game_info(id=None):
    if (id is None):
        return self.all_games()
    response = api.game_info(id)
    helper.check_response(response)
    game = json.loads(response.data)
    game = game["game"]
    return render_template("games/game.html", game=game)


