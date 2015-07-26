from flask import Blueprint, jsonify, abort, request

from projecteval.api.models.db import Platform

platformapi = Blueprint('platformapi', __name__)

@platformapi.route('/api/platforms/', methods=['GET'], strict_slashes = False)
def all_platforms():
	fields = request.args.get('fields')
	platforms = Platform.query.all()

	json_result = []

	for platform in platforms:
		json_result.append(platform.toJSON(fields))

	return jsonify(platforms=json_result)

@platformapi.route('/api/platforms/<int:id>/', methods=['GET'], strict_slashes = False)
def platform_info(id):
	platform = Platform.query.filter_by(id=id).first()

	if(platform == None):
		abort(404)

	return jsonify(platform=platform.toJSON())