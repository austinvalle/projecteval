# This controller will provide a host of helper functions that can be used throughout the website...useful for error handling and other functions

from flask import Blueprint, request, jsonify, render_template, flash

import json

from projecteval import db

from projecteval.api.models import Game, Platform

import projecteval.errors.controllers as error_controller

# Eventually configure error handling here...leave like this for now
def check_response(response):
    if response is not None and response.status_code == 200:
        ""
    else:
        redirect(url_for('error_controller.error_404'))
        
