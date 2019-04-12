from main import db
from main.models.holiday import Holiday
from main.models.holiday import HolidayType

holidays = [
    {"date": "January 1", "name": "New Year's Day",
     "type": "Regular Holiday"},
    {"date": "February 5", "name": "Chinese Lunar New Year's Day",
     "type": "Special Non-working Holiday"},
    {"date": "February 25", "name": "People Power Anniversary",
     "type": "Special Non-working Holiday"},
    {"date": "April 9", "name": "The Day of Valor",
     "type": "Regular Holiday"},
    {"date": "April 18", "name": "Maundy Thursday",
     "type": "Regular Holiday"},
    {"date": "April 19", "name": "Good Friday",
     "type": "Regular Holiday"},
    {"date": "May 1", "name": "Labor Day",
     "type": "Regular Holiday"},
    {"date": "June 6", "name": "Eidul-Fitar",
     "type": "Regular Holiday"},
    {"date": "June 12", "name": "Independence Day",
     "type": "Regular Holiday"},
    {"date": "August 12",
     "name": "Eid al-Adha (Feast of the Sacrifice)", "type": "Regular Holiday"},
    {"date": "August 21", "name": "Ninoy Aquino Day",
     "type": "Special Non-working Holiday"},
    {"date": "August 26", "name": "National Heroes Day",
        "type": "Regular Holiday"},
    {"date": "September 3", "name": "Yamashita Surrender Day",
     "type": "Regular Holiday"},
    {"date": "November 1", "name": "All Saints' Day",
     "type": "Special Non-working Holiday"},
    {"date": "November 2", "name": "All Souls' Day",
     "type": "Special Non-working Holiday"},
    {"date": "November 30", "name": "Bonifacio Day",
     "type": "Regular Holiday"},
    {"date": "December 8", "name": "Feast of the Immaculate Conception",
     "type": "Special Non-working Holiday"},
    {"date": "December 24", "name": "Additional Special Non-Working Day",
     "type": "Special Non-working Holiday"},
    {"date": "December 25", "name": "Christmas Day",
     "type": "Regular Holiday"},
    {"date": "December 30", "name": "Rizal Day",
     "type": "Regular Holiday"},
    {"date": "December 31", "name": "New Year's Eve",
     "type": "Special Non-working Holiday"}
]


def add_holiday_type(name):
    holiday_type = HolidayType.query.filter_by(name=name).first()

    if holiday_type is None:
        holiday_type = HolidayType(name=name)
        db.session.add(holiday_type)
        db.session.commit()

        return holiday_type

    return holiday_type


def add_holiday(date, name, type):
    holiday = Holiday.query.filter_by(name=name).first()

    if holiday is None:
        holiday = Holiday(date=date, name=name, type_id=type.id)
        db.session.add(holiday)
        db.session.commit()


def run():
    for holiday in holidays:
        add_holiday(holiday["date"], holiday["name"],
                    add_holiday_type(holiday["type"]))

    return "Seeding is finished!"
