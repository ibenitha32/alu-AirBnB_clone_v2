#!/usr/bin/python3
"""Flask Application for Displaying a List of States

This Python script runs a Flask application that listens on 0.0.0.0:5000. It displays a web page with a list of all State objects stored in the DBStorage.

The `/states_list` route is used to display the list, and the states are sorted by name. A teardown function is provided to close the SQLAlchemy session when the application context is torn down.

To run the application, execute this script.

"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a List of States

    This function retrieves all State objects from the database and displays them on an HTML page. The states are sorted by name.

    Returns:
        str: The rendered HTML page with the list of states.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session when the app context is torn down."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
