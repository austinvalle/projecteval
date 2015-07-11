from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.route('/errors/', methods=['GET'])
def error_default():
    return render_template("default_error.html")


@errors.route('/errors/404/', methods=['GET'])
def error_404():
    return render_template("404.html")
