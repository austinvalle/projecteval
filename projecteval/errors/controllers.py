from flask import Blueprint, request, jsonify, render_template, flash

import json

from projecteval import db

from projecteval.api.models import Game, Platform

errors = Blueprint('errors', __name__)


# Error
@errors.route('/errors/', methods=['GET'])
def error_default():
    return render_template("default_error.html")


@errors.route('/errors/404/', methods=['GET'])
def error_404():
    return render_template("404.html")
