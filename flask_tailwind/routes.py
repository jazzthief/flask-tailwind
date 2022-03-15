import os, sys
import datetime as dt
from flask import (
    render_template
)
from flask_tailwind import app
""" from app.helpers import *
from app.forms import *
from app.models import * """


# Home route
@app.route('/')
def index():
    return render_template('index.html')
