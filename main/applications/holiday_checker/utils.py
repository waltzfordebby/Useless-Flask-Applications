import datetime
from main.models.holiday import Holiday


def is_holiday():
    current_date = datetime.date.today()
    current_month_date_str = current_date.strftime("%B %d")
    current_day = current_date.isoweekday()

    holiday = Holiday.query.filter_by(date=current_month_date_str).first()
    weekdays = {1: "Lunes",
                2: "Martes",
                3: "Miyerkules",
                4: "Huwebes",
                5: "Biyernes"}
    weekends = {6: "Sabado",
                7: "Linggo"}

    if holiday is None:
        if current_day in weekends:
            return f"Walang Pasok, {weekends[current_day]} ngayun!"
        return f"May Pasok {weekdays[current_day]} ngayon!"

    return f"Walang pasok, {holiday.name} ngayun!"
