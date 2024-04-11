#!/usr/bin/python3
""" starts a web flask app """
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ display html page with all states """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ html with state id """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """ remove the SQLA session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
