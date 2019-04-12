from main import ma
from main.models.holiday import Holiday, HolidayType


class HolidayTypeSchema(ma.Schema):
    class Meta:
        model = HolidayType
        fields = ("id", "name", "holidays")

    holidays = ma.List(ma.HyperlinkRelated("name"))


class HolidaySchema(ma.Schema):
    class Meta:
        model = Holiday
        fields = ("id", "date", "name", "type")

    type = ma.Nested(HolidayTypeSchema)


holiday_schema = HolidaySchema(strict=True)
holidays_schema = HolidaySchema(many=True, strict=True)

holiday_type_schema = HolidayTypeSchema(strict=True)
holiday_types_schema = HolidayTypeSchema(many=True, strict=True)
