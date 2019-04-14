import secrets
from PIL import Image
from os import listdir, remove
from os.path import join, isfile, realpath, splitext
from main import db
from main.models.pictures import Picture


def save_to_database(filename, height, width):
    picture = Picture(filename=filename, height=height, width=width)

    db.session.add(picture)
    db.session.commit()


def get_unrecorded_pictures():

    unrecorded_pictures_path = join(realpath(
        __file__ + "/../../../.."), "static/images/unrecorded_pictures")

    pictures = [p for p in listdir(unrecorded_pictures_path) if isfile(
        join(unrecorded_pictures_path, p))]

    return unrecorded_pictures_path, pictures


def record_pictures(path_and_pictures):
    recorded_pictures_path = join(realpath(
        __file__ + "/../../../.."), "static/images/recorded_pictures")

    path, pictures = path_and_pictures

    if pictures == []:
        return "There is no unrecorded pictures!"

    for picture in pictures:
        random_hex = secrets.token_hex(8)
        _, ext = splitext(picture)
        filename = random_hex + ext
        unrecorded_picture_path = join(path, picture)
        recorded_picture_path = join(recorded_pictures_path, filename)

        pillow_picture = Image.open(unrecorded_picture_path)
        width, height = pillow_picture.size
        picture.save(recorded_picture_path)
        save_to_database(filename, height, width)
        remove(unrecorded_picture_path)

    return "Picture seeding is finished!"


def run():

    return record_pictures(get_unrecorded_pictures())
