#!/usr/bin/python3
""" Import Flask to run web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ Function to close the session """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def cities_by_states(id):
    """Display a HTML page with a list of all State & city objects"""
    states = storage.all(State)
    cities = storage.all(City)
    ret_cities = []
    sorted_cities = sort_dict(cities)

    if f"State.{id}" in states:
        states = states[f"State.{id}"]
    else:
        states = None

    if states:
        for city in sorted_cities.items():
            city = dict(city[1])
            if city["state_id"] == states["id"]:
                ret_cities.append({"id": city['id'], "name": city['name']})
        states["cities"] = ret_cities

    return render_template('9-states.html', state_city=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
