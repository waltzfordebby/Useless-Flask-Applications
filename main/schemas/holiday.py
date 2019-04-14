from main import ma


class HolidayTypeSchema(ma.Schema):
    holidays = ma.Nested("HolidaySchema", many=True, exclude=("type", ))

    class Meta:
        fields = ("id", "name", "holidays")


class HolidaySchema(ma.Schema):
    class Meta:
        fields = ("id", "date", "name", "type")

    type = ma.Nested(HolidayTypeSchema, exclude=("holidays",))


holiday_schema = HolidaySchema(strict=True)
holidays_schema = HolidaySchema(many=True, strict=True)

holiday_type_schema = HolidayTypeSchema(strict=True)
holiday_types_schema = HolidayTypeSchema(many=True, strict=True)
