from flask import request
import os
import json
import time
from projecteval.api.models.forms import LoginForm
import projecteval.controllers.errors as error_controller

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

def parse_fields(fields):
        field = ''
        subfields= ''

        level = 0
        results= {}
        fields = fields.lower()

        for c in fields:
            if c == '(':
                level += 1
                if level == 1:
                    subfields = ''
                    continue
            elif c == ')':
                level -= 1

            if level == 0:
                if c in 'abcdefghijklmnopqrstuvwxyz0123456789_-':
                    field += c
                else:
                    if field != '':
                        results[field] = subfields
                    field = ''
                    subfields = ''
            else:
                subfields += c
        if level == 0 and field != '':
            results[field] = subfields

        return results