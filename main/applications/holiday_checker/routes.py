from flask import render_template, request, Blueprint
from main.models.holiday import Holiday
from main.applications.holiday_checker.utils import today
from main.applications.holiday_checker.database_seeder.holidays import run

holiday = Blueprint("holiday", __name__)


@holiday.route("/holiday", methods=['GET'])
def home():
    return today


@holiday.route("/holiday/seed")
def seed():
    seeding = run()
    return seeding
