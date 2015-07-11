from flask import Blueprint, session, request, jsonify, abort

from projecteval import db

from projecteval.api.models.db import Game, Gameplatform

from projecteval.api.models.forms import EditGameForm

gameapi = Blueprint('gameapi', __name__)

def build_game(game):
	platforms = []
	for gameplatform in game.platforms:
		platform = {
			'id':gameplatform.platform.id,
			'name':gameplatform.platform.name
		}
		platforms.append(platform)

	result = {
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
		'last_modified':game.last_modified,
		'platforms': platforms,
		'esrb_url': game.esrb.image_url
	}

	return result

@gameapi.route('/api/games/', methods=['GET'])
def all_games():
	games = Game.query.all()

	json_result = []

	for game in games:
		g = build_game(game)
		json_result.append(g)

	return jsonify(games=json_result)

@gameapi.route('/api/games/<int:id>', methods=['GET'])
def game_info(id):
	game = Game.query.filter_by(id=id).first()

	if(game == None):
		abort(404)

	json_result = build_game(game)
	return jsonify(game=json_result)

@gameapi.route('/api/edit/game/', methods=['POST'])
def edit_game(platformIds):
	errors = [];
	id = request.form.get('id')
	releaseDate = request.form.get('release_date')
	developer = request.form.get('developer')
	publisher = request.form.get('publisher')
	description = request.form.get('desc')
	trailerUrl = request.form.get('trailer')
	title = request.form.get('title')
	platforms = set([int(x) for x in platformIds])

	form = EditGameForm(id=id, description=description, releaseDate=releaseDate, developer=developer, publisher=publisher, trailerUrl=trailerUrl, title=title)
	# EditGameForm doesn't take trailerUrl and description values initially, use below as a workaround	
	form.description.data = description
	form.trailerUrl.data = trailerUrl

	# Validate platforms outside of Form as workaround for now
	if not validatePlatformIds(platforms):
		errors.append('Game requires at least one platform')

	if form.validate() and not errors:
		dbsession = db.session()
		game = Game.query.filter_by(id=id).first()
		if (game != None):
			# Update game here
			game.title = title
			game.release_date = releaseDate
			game.desc = description
			game.developer = developer
			game.publisher = publisher
			game.trailer_url = trailerUrl

			gameplatforms = Gameplatform.query.filter_by(game_id=game.id).all()
			currentIds = set()

			for g in gameplatforms:
				currentIds.add(g.platform_id)

			if not currentIds.issubset(platforms):
				for cId in currentIds:
					if not cId in platforms:
						deleteThis = Gameplatform.query.filter_by(game_id=game.id, platform_id=cId).first()
						dbsession.delete(deleteThis)
					else:
						platforms.remove(cId)

			if len(platforms) > 0:
				for addId in platforms:
					exists = Gameplatform.query.filter_by(game_id=game.id, platform_id=addId).first()

					if not exists:
						addThis = Gameplatform(game.id, addId)
						dbsession.add(addThis)

			# To Do: add functionality for ESRB and platforms
			dbsession.commit()
			return jsonify({"success":"true"})
		else:
			errors.append("No such game exists!")		
	else:
		errors_to_json(form, errors)

	return jsonify({"success":"false", "errors":errors})

def validatePlatformIds(platforms):
	if len(platforms) <= 0:
		return False

	return True
	
def errors_to_json(form, errors_arr):
	for field, errors in form.errors.items():
		for error in errors:
			errors_arr.append(error)