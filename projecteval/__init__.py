from flask import Flask, render_template

from flask.ext.sqlalchemy import SQLAlchemy

projecteval = Flask(__name__)

projecteval.config.from_object('config')

db = SQLAlchemy(projecteval)

@projecteval.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

from projecteval.auth.controllers import auth as auth_module

from projecteval.api.controllers import api as api_module

from projecteval.games.controllers import games as games_module

from projecteval.platforms.controllers import platforms as platform_module

from projecteval.errors.controllers import errors as error_module

from projecteval.home.controllers import home as home_module

projecteval.register_blueprint(auth_module)
projecteval.register_blueprint(api_module)
projecteval.register_blueprint(games_module)
projecteval.register_blueprint(platform_module)
projecteval.register_blueprint(error_module)
projecteval.register_blueprint(home_module)

db.create_all()
