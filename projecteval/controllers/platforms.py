from flask import Blueprint, render_template
import json
import projecteval.api.controllers.platform as platformapi
import projecteval.controllers.helpers as helper

platforms = Blueprint('platforms', __name__)


@platforms.route('/platforms/', methods=['GET'])
def all_platforms():
    response = platformapi.all_platforms()
    helper.check_response(response)
    platforms = json.loads(response.data)
    platforms = platforms["platforms"]
    return render_template("platforms/platforms.html", platforms=platforms)

@platforms.route('/platforms/<int:id>', methods=['GET'])
def platform_info(id=None):
    if (id is None):
        return self.all_games()
    response = platformapi.platform_info(id)
    helper.check_response(response)
    platform = json.loads(response.data)
    platform = platform["platform"]
    platform["release_date"] = helper.convert_date_string(platform["release_date"])
    return render_template("platforms/platform.html", platform=platform)
