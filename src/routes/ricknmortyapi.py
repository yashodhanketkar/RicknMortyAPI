import json
import urllib.request

from flask import Blueprint
from flask_cors import cross_origin

from ..instance.config import BASE_URI

_api = Blueprint("api", __name__)


@_api.route("/api/characters/", methods=["GET"])
@cross_origin()
def get_all_characters():
    url = BASE_URI + "character"

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    return data


@_api.route("/api/characters/<string:id>/", methods=["GET"])
@cross_origin()
def get_character_via_id(id: str):
    url = f"{BASE_URI}character/{id}"

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    return data


@_api.route("/api/episodes/", methods=["GET"])
@cross_origin()
def get_all_episodes():
    url = BASE_URI + "episode"

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    return data


@_api.route("/api/episodes/<string:id>/", methods=["GET"])
@cross_origin()
def get_episode_via_id(id: str):
    url = f"{BASE_URI}episode/{id}"

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    return data


@_api.route("/api/locations/", methods=["GET"])
@cross_origin()
def get_all_locations():
    url = BASE_URI + "location"

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    return data


@_api.route("/api/locations/<string:id>/", methods=["GET"])
@cross_origin()
def get_location_via_id(id: str):
    url = f"{BASE_URI}location/{id}"

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    return data
