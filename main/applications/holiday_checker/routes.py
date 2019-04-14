from flask import Blueprint, render_template, request
from main.applications.holiday_checker.utils import is_holiday

holiday_main = Blueprint("holiday_main", __name__)


@holiday_main.route("/may_pasok_ba")
def home():
    return render_template("holiday_checker/home.html", content=is_holiday(), title="May Pasok Ba?")
