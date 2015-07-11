from flask import Blueprint, jsonify, abort

from projecteval.api.models.db import Platform

platformapi = Blueprint('platformapi', __name__)

@platformapi.route('/api/platforms/', methods=['GET'])
def all_platforms():
	platforms = Platform.query.all()

	json_result = []

	for platform in platforms:
		p = {
			'id':platform.id,
			'name':platform.name,
			'release_date':platform.release_date,
			'desc':platform.desc,
			'developer':platform.developer,
			'manufacturer':platform.manufacturer,
			'cpu':platform.cpu,
			'memory':platform.memory,
			'graphics':platform.graphics,
			'storage':platform.storage,
			'added_by':platform.added_by,
			'date_added':platform.date_added,
			'last_modified_by':platform.last_modified_by,
			'last_modified':platform.last_modified
		}
		json_result.append(p)
	return jsonify(platforms=json_result)

@platformapi.route('/api/platforms/<int:id>', methods=['GET'])
def platform_info(id):
	platform = Platform.query.filter_by(id=id).first()

	if(platform == None):
		abort(404)

	json_result = {
		'id':platform.id,
		'name':platform.name,
		'release_date':platform.release_date,
		'desc':platform.desc,
		'developer':platform.developer,
		'manufacturer':platform.manufacturer,
		'cpu':platform.cpu,
		'memory':platform.memory,
		'graphics':platform.graphics,
		'storage':platform.storage,
		'added_by':platform.added_by,
		'date_added':platform.date_added,
		'last_modified_by':platform.last_modified_by,
		'last_modified':platform.last_modified
	}

	return jsonify(platform=json_result)