from flask import Blueprint, request, jsonify, render_template, flash

import json

from projecteval import db

from projecteval.api.models import Game, Platform

import projecteval.api.controllers as api

import projecteval.helper.controllers as helper

home = Blueprint('home', __name__)


# Home page
@home.route('/', methods=['GET'])
def default_home():
    return render_template("home/index.html")
