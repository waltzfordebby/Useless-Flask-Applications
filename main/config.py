import os
from dotenv import load_dotenv


class Config(object):

    # Load dotenv in the base root
    app_root = os.path.join(os.path.dirname(__file__), "..")
    dotenv_path = os.path.join(app_root, ".env")
    load_dotenv(dotenv_path)

    # Get ENV Variables
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        "SQLALCHEMY_TRACK_MODIFICATIONS")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://waltzfordebby:password@localhost/personal_web_app"
