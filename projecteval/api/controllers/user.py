from flask import Blueprint, session, request, jsonify

from projecteval import db

from werkzeug import check_password_hash, generate_password_hash

from projecteval.api.models.db import User

from projecteval.api.models.forms import RegisterForm, LoginForm

userapi = Blueprint('userapi', __name__)

@userapi.route('/api/user/', methods=['POST'])
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

@userapi.route('/api/login/', methods=['POST'])
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

@userapi.route('/api/logout/', methods=['POST'])
def logout_user():
	session['user_id'] = None
	session['user_name'] = None
	return ""   

def errors_to_json(form, errors_arr):
	for field, errors in form.errors.items():
		for error in errors:
			errors_arr.append(error)