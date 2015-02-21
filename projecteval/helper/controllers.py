# This controller will provide a host of helper functions that can be used throughout the website...useful for error handling and other functions

from flask import Blueprint, request, jsonify, render_template, flash

import os
import json
import time

from projecteval import db

from projecteval.api.models import Game, Platform
from projecteval.api.forms import LoginForm
from projecteval.api.models import User

import projecteval.errors.controllers as error_controller

# Eventually configure error handling here...leave like this for now
def check_response(response):
    if response is not None and response.status_code == 200:
        ""
    else:
        redirect(url_for('error_controller.error_404'))

def convert_date_string(datestring):
    readTime = time.strptime(datestring, "%a, %d %b %Y %H:%M:%S GMT")
    return time.strftime("%m/%d/%Y", readTime)

def get_login_form():
    return LoginForm(request.login_form)

def extractPlatformIds(requestForm):
    platformIds = []
    i = 0

    while requestForm.get('platforms['+ str(i) + '][id]'):
        platformIds.append(requestForm.get('platforms['+ str(i) + '][id]'))
        i += 1

    return platformIds
