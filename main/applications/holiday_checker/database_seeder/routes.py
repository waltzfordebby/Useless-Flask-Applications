from flask import render_template, request, Blueprint
from main.applications.holiday_checker.database_seeder.holidays import run

holiday_seeder = Blueprint("holiday_seeder", __name__)


@holiday_seeder.route("/holiday/seed")
def seed():
    seeding = run()
    return seeding
