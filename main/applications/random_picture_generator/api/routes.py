from flask import Blueprint, jsonify
from main.models.pictures import Picture
from main.schemas.pictures import pictures_schema

picture_api = Blueprint("picture_api", __name__)


@picture_api.route("/api/pictures", methods=["GET"])
def pictures():
    all_pictures = Picture.query.all()
    return pictures_schema.jsonify(all_pictures)
