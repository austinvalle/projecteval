from flask import Blueprint, request, jsonify

from projecteval.api.models.db import Game

searchapi = Blueprint('searchapi', __name__)


@searchapi.route('/api/search/', methods=['GET'], strict_slashes = False)
def search_games():
	fields = request.args.get('fields')
	title = str(request.args.get('title')).replace("+", " ")

	games = Game.query.filter(Game.title.ilike("%" + title + "%"))

	json_result = []

	for game in games:
		json_result.append(game.toJSON(fields))

	return jsonify(games=json_result)