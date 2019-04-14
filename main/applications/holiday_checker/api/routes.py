from flask import Blueprint, jsonify
from main.models.holiday import Holiday, HolidayType
from main.schemas.holiday import holiday_schema, holidays_schema, holiday_types_schema

holiday_api = Blueprint("holiday_api", __name__)


@holiday_api.route("/api/holidays", methods=["GET"])
def holidays():
    all_holidays = Holiday.query.all()
    return holidays_schema.jsonify(all_holidays)


@holiday_api.route("/api/holiday/types", methods=["GET"])
def holiday_types():
    all_holiday_types = HolidayType.query.all()
    return holiday_types_schema.jsonify(all_holiday_types)
