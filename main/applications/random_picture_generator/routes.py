from flask import Blueprint, render_template, request
from main.applications.random_picture_generator.utils import run

random_picture = Blueprint("random_picture", __name__)


@random_picture.route("/picture/random")
def home():
    return render_template("random_picture_generator/home.html", filename=run(), title="Random Picture Generator")
