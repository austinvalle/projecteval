from flask import Blueprint, request, jsonify

from projecteval import db

from projecteval.api.models import Game, Platform

api = Blueprint('api', __name__)


# Game API
@api.route('/api/games/', methods=['GET'])
def all_games():
	games = Game.query.all()

	json_result = []

	for game in games:
		g = {
			'id': game.id,
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
		json_result.append(g)

	return jsonify(games=json_result)

@api.route('/api/games/<int:id>', methods=['GET'])
def game_info(id):
	game = Game.query.filter_by(id=id).first()

	json_result = {
		'id': game.id,
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

	return jsonify(game=json_result)

# Platform API
@api.route('/api/platforms/', methods=['GET'])
def all_platforms():
	platforms = Platform.query.all()

	json_result = []

	for platform in platforms:
		p = {
			'id':platform.id,
			'name':platform.name,
			'release_date':platform.release_date,
			'desc':platform.desc,
			'developer':platform.developer,
			'manufacturer':platform.manufacturer,
			'cpu':platform.cpu,
			'memory':platform.memory,
			'graphics':platform.graphics,
			'storage':platform.storage,
			'added_by':platform.added_by,
			'date_added':platform.date_added,
			'last_modified_by':platform.last_modified_by,
			'last_modified':platform.last_modified
		}
		json_result.append(p)
	return jsonify(platforms=json_result)

@api.route('/api/platforms/<int:id>', methods=['GET'])
def platform_info(id):
	platform = Platform.query.filter_by(id=id).first()

	json_result = {
		'id':platform.id,
		'name':platform.name,
		'release_date':platform.release_date,
		'desc':platform.desc,
		'developer':platform.developer,
		'manufacturer':platform.manufacturer,
		'cpu':platform.cpu,
		'memory':platform.memory,
		'graphics':platform.graphics,
		'storage':platform.storage,
		'added_by':platform.added_by,
		'date_added':platform.date_added,
		'last_modified_by':platform.last_modified_by,
		'last_modified':platform.last_modified
	}

	return jsonify(platform=json_result)