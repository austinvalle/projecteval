from flask import Flask, render_template
from flask_wtf.csrf import CsrfProtect

from flask.ext.sqlalchemy import SQLAlchemy

projecteval = Flask(__name__)

projecteval.config.from_object('config')

db = SQLAlchemy(projecteval)

from projecteval.api.controllers.game import gameapi as api_game
from projecteval.api.controllers.platform import platformapi as api_platform
from projecteval.api.controllers.esrb import esrbapi as api_esrb
from projecteval.api.controllers.user import userapi as api_user
from projecteval.api.controllers.error import errorapi as api_error

from projecteval.controllers.games import games as games_module
from projecteval.controllers.platforms import platforms as platform_module
from projecteval.controllers.errors import errors as error_module
from projecteval.controllers.home import home as home_module

projecteval.register_blueprint(api_game)
projecteval.register_blueprint(api_platform)
projecteval.register_blueprint(api_esrb)
projecteval.register_blueprint(api_user)
projecteval.register_blueprint(api_error)

projecteval.register_blueprint(games_module)
projecteval.register_blueprint(platform_module)
projecteval.register_blueprint(error_module)
projecteval.register_blueprint(home_module)

CsrfProtect(projecteval)
db.create_all()

@projecteval.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404
