from flask import Blueprint, request, jsonify, render_template, flash, session, url_for, redirect

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
    game["release_date"] = helper.convert_date_string(game["release_date"])
    return render_template("games/game.html", game=game)

@games.route('/edit/games/<int:id>', methods=['GET'])
def edit_game(id=None):
    if (id is None):
        return redirect(url_for('games.all_games'), 302)
    if (not session["user_id"]):
        return redirect(url_for('games.game_info', id=id), 302)
    response = api.game_info(id)
    platform_response = api.all_platforms()

    helper.check_response(response)
    helper.check_response(platform_response)

    platform_list = json.loads(platform_response.data)
    platform_list = platform_list["platforms"]

    game = json.loads(response.data)
    game = game["game"]   
    game["release_date"] = helper.convert_date_string(game["release_date"])
    
    return render_template("edit/edit_game.html", game=game, platform_list=platform_list)

@games.route('/edit/games/', methods=['POST'])
def save_game():
    if (not session["user_id"]):
        return redirect(url_for('games.all_games'), 302)

    platformIds = helper.extractPlatformIds(request.form)

    return api.edit_game(platformIds)

