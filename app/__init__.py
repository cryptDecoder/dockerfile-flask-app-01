""" 
initialize the flask app and views
"""

from flask import Flask

app = Flask(__name__)
from app.views import baseViews
