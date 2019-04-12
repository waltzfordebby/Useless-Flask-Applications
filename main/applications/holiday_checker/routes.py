from flask import render_template, request, Blueprint, jsonify
from main.models.holiday import Holiday, HolidayType
from main.schemas.holiday import holiday_schema, holidays_schema, holiday_types_schema
from main.applications.holiday_checker.utils import today
from main.applications.holiday_checker.database_seeder.holidays import run

holiday = Blueprint("holiday", __name__)


@holiday.route("/api/holidays", methods=["GET"])
def holidays():
    all_holidays = Holiday.query.all()
    return holidays_schema.jsonify(all_holidays)


@holiday.route("/api/holiday/type", methods=["GET"])
def holiday_types():
    all_holiday_types = HolidayType.query.all()
    return holiday_types_schema.jsonify(all_holiday_types)


@holiday.route("/holiday/seed")
def seed():
    seeding = run()
    return seeding
