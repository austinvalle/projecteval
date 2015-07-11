from flask import Blueprint, render_template

home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def default_home():
    return render_template("home/index.html")
