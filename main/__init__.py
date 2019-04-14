from flask import Flask
from main.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialization
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Models
    # Holiday Checker
    from main.models.holiday import Holiday
    from main.models.holiday import HolidayType

    # Random Picture Generator
    from main.models.pictures import Picture

    # Blueprint imports

    # Holiday Checker
    from main.applications.holiday_checker.routes import holiday_main
    from main.applications.holiday_checker.database_seeder.routes import holiday_seeder
    from main.applications.holiday_checker.api.routes import holiday_api

    # Picture Seeder
    from main.applications.random_picture_generator.database_seeder.routes import picture_seeder
    from main.applications.random_picture_generator.api.routes import picture_api
    from main.applications.random_picture_generator.routes import random_picture
    # Register Blueprint
    # Holiday Checker
    app.register_blueprint(holiday_main)
    app.register_blueprint(holiday_seeder)
    app.register_blueprint(holiday_api)

    # Picture Seeder
    app.register_blueprint(picture_seeder)
    app.register_blueprint(picture_api)
    app.register_blueprint(random_picture)

    return app
