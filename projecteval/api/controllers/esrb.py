from flask import Blueprint, jsonify, abort

from projecteval.api.models.db import ESRB

esrbapi = Blueprint('esrbapi', __name__)

@esrbapi.route('/api/esrb/', methods=['GET'])
def all_esrbs():
	esrbs = ESRB.query.all()

	json_result = []

	for esrb in esrbs:
		e = {
			'id':esrb.id,
			'short_desc':esrb.short_desc,
			'full_desc':esrb.full_desc,
			'image_url':esrb.image_url
		}
		json_result.append(e)
		
	return jsonify(esrbs=json_result)

@esrbapi.route('/api/esrb/<int:id>', methods=['GET'])
def esrb_info(id):
	esrb = ESRB.query.filter_by(id=id).first()

	if(esrb == None):
		abort(404)

	json_result = {
		'id':esrb.id,
		'short_desc':esrb.short_desc,
		'full_desc':esrb.full_desc,
		'image_url':esrb.image_url
	}

	return jsonify(esrb=json_result)