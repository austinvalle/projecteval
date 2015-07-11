from flask import Blueprint, jsonify, make_response

errorapi = Blueprint('errorapi', __name__)

@errorapi.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Resource not found'}), 404)