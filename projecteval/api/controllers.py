from flask import Blueprint, session, request, jsonify, make_response, abort

from projecteval import db

from werkzeug import check_password_hash, generate_password_hash

from projecteval.api.models import User, Game, Platform, ESRB, Gameplatform

from projecteval.api.forms import RegisterForm, LoginForm, EditGameForm

api = Blueprint('api', __name__)


# Game API
def build_game(game):
	platforms = []
	for gameplatform in game.platforms:
		platform = {
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

@api.route('/api/games/', methods=['GET'])
def all_games():
	games = Game.query.all()

	json_result = []

	for game in games:
		g = build_game(game)
		json_result.append(g)

	return jsonify(games=json_result)

@api.route('/api/games/<int:id>', methods=['GET'])
def game_info(id):
	game = Game.query.filter_by(id=id).first()

	if(game == None):
		abort(404)

	json_result = build_game(game)
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

	if(platform == None):
		abort(404)

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

# ESRB API
@api.route('/api/esrb/', methods=['GET'])
def all_esrbs():
	esrbs = ESRB.query.all()

	json_result = []

	for esrb in esrbs:
		e = {
			'id':esrb.id,
			'short_desc':esrb.short_desc,
			'full_desc':esrb.full_desc,
			'image_url':esrb.image_url
		}
		json_result.append(e)
		
	return jsonify(esrbs=json_result)

@api.route('/api/esrb/<int:id>', methods=['GET'])
def esrb_info(id):
	esrb = ESRB.query.filter_by(id=id).first()

	if(esrb == None):
		abort(404)

	json_result = {
		'id':esrb.id,
		'short_desc':esrb.short_desc,
		'full_desc':esrb.full_desc,
		'image_url':esrb.image_url
	}

	return jsonify(esrb=json_result)

@api.route('/api/edit/game/', methods=['POST'])
def edit_game():
	errors = [];
	id = request.form.get('id')
	releaseDate = request.form.get('release_date')
	developer = request.form.get('developer')
	publisher = request.form.get('publisher')
	description = request.form.get('desc')
	trailerUrl = request.form.get('trailer')
	title = request.form.get('title')
	form = EditGameForm(id=id, description=description, releaseDate=releaseDate, developer=developer, publisher=publisher, trailerUrl=trailerUrl, title=title)
	# EditGameForm doesn't take trailerUrl and description values initially, use below as a workaround	
	form.description.data = description
	form.trailerUrl.data = trailerUrl

	if form.validate():
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

			# To Do: add functionality for ESRB and platforms
			dbsession.commit()
			return jsonify({"success":"true"})
		else:
			errors.append("No such game exists!")		
	else:
		errors_to_json(form, errors)

	return jsonify({"success":"false", "errors":errors})

@api.route('/api/user/', methods=['POST'])
def register_user():
	errors = [];
	email = request.form.get('email')
	username = request.form.get('username')
	password = request.form.get('password')
	form = RegisterForm(email=email, username=username, password=password)

	if form.validate():
		user_email = User.query.filter_by(email=email).first()
		user_username = User.query.filter_by(username=username).first()

		if user_email:
			errors.append("Email already taken")
		if user_username:
			errors.append("Username already taken")

		if not user_email and not user_username:
			dbsession = db.session()
			user = User(username, email, generate_password_hash(password))
			dbsession.add(user)
			dbsession.commit()

			session['user_id'] = user.id
			session['user_name'] = user.username
			return jsonify({"success": "true", "username": user.username})
	else:
		errors_to_json(form, errors)

	return jsonify({"success": "false", "errors": errors})

@api.route('/api/login/', methods=['POST'])
def login_user():
	errors = []
	email = request.form.get('email')
	password = request.form.get('password')
	form = LoginForm(email=email,password=password)
	if form.validate():
		user = User.query.filter_by(email=email).first()

		if not user:
			errors.append("No user with that email address")
		elif check_password_hash(user.password, password):
			session['user_id'] = user.id
			session['user_name'] = user.username
			return jsonify({"success":"true", "username":user.username})
		else:
			errors.append("Wrong password")
	else:
		errors_to_json(form, errors)
	return jsonify({"success":"false","errors":errors}) 

@api.route('/api/logout/', methods=['POST'])
def logout_user():
	session['user_id'] = None
	session['user_name'] = None
	return ""   

# Error Handling
@api.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Resource not found'}), 404)

def errors_to_json(form, errors_arr):
	for field, errors in form.errors.items():
		for error in errors:
			errors_arr.append(error)
