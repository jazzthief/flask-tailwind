from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle


__version__ = '0.1.0'
app = Flask(__name__)

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
# assets = Environment()

""" if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object('config.DevelopmentConfig')
elif os.environ.get('FLASK_ENV') == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.ProductionConfig') """

import flask_tailwind.routes
