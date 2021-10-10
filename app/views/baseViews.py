"""Create a simple route """
from app import app


# create basic route
@app.route("/")
def index():
    return "<h1 style=color:red>Welcome to Python Flask Dockerfile Demo </h1>"
