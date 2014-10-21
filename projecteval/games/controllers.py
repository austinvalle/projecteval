from flask import Blueprint, request, jsonify

from projecteval import db

from projecteval.games.models import Game

games = Blueprint('games', __name__)

@games.route('/games/', methods=['GET'])
def all_games():
	games = Game.query.limit(10).offset(0).all()

	json_results = []

	for game in games:
		g = {
			'title':game.title,
			'release_date':game.release_date,
			'desc':game.desc,
			'developer':game.developer,
			'publisher':game.publisher,
			'trailer_url':game.trailer_url,
			'esrb_id':game.esrb_id,
			'genre_id':game.genre_id,
			'added_by':game.added_by,
			'date_added':game.date_added,
			'last_modified_by':game.last_modified_by,
			'last_modified':game.last_modified
		}
		json_results.append(g)

	return jsonify(games=json_results)