from flask import render_template, request, Blueprint
from main.applications.random_picture_generator.database_seeder.utils import run

picture_seeder = Blueprint("picture_seeder", __name__)


@picture_seeder.route("/picture/seed")
def seed():
    seeding = run()
    return seeding
