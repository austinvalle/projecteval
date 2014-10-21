from flask import Flask, render_template

from flask.ext.sqlalchemy import SQLAlchemy

projecteval = Flask(__name__)

projecteval.config.from_object('config')

db = SQLAlchemy(projecteval)

@projecteval.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

from projecteval.auth.controllers import auth as auth_module

from projecteval.games.controllers import games as games_module

projecteval.register_blueprint(auth_module)
projecteval.register_blueprint(games_module)

db.create_all()