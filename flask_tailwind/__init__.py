import os

from flask import Flask
from flask import render_template
from flask_tailwind.models import db
from flask_migrate import Migrate
# from flask_assets import Environment, Bundle

__version__ = '0.1.0'


def create_app(test_config=None):
    """Create and configure flask app"""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_object(os.environ['APP_SETTINGS'])
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # assets = Environment()

    db.init_app(app)
    migrate = Migrate(app, db)

    register_blueprints(app)
    register_error_handlers(app)

    return app


# Helper functions
def register_blueprints(app):
    """Register flask app blueprints"""

    from flask_tailwind.main import main_blueprint

    app.register_blueprint(main_blueprint)


def register_error_handlers(app):
    """Register error handlers"""

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
