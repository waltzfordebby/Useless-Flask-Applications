from main.models.pictures import Picture
from random import choice


def get_filenames():

    all_pictures = Picture.query.all()

    pictures_filename = []
    for picture in all_pictures:
        pictures_filename.append(picture.filename)

    return pictures_filename


def get_random_filename(filenames):
    return choice(filenames)


def run():
    return get_random_filename(get_filenames())
