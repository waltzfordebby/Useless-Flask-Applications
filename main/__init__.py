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
    from main.models.holiday import Holiday
    from main.models.holiday import HolidayType

    # Blueprint imports
    from main.applications.holiday_checker.routes import holiday

    # Register Blueprint
    app.register_blueprint(holiday)

    return app
