#!/usr/bin/python3
""" starts a web flask app """
from models import storage
from flask import Flask
from flask import render_template
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ displays the main filters HTML page """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


app.teardown_appcontext
def teardown(exc):
    """ removes current SQLA session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
