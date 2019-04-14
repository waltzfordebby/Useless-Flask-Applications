from main import ma


class PictureSchema(ma.Schema):
    class Meta:
        fields = ("id", "filename", "height", "width")


picture_schema = PictureSchema(strict=True)
pictures_schema = PictureSchema(many=True, strict=True)
