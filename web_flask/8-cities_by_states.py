#!/usr/bin/python3
""" Import Flask to run web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ Method to close the session """
    storage.close()


def sort_dict(Class, by="name"):
    """ sorts a dictionary of classes based on a
    specified attribute and returns the sorted dictionary."""
    return dict(sorted(Class.items(), key=lambda x: x[1][by]))


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays_a html page_with states_and_cities"""

    states = storage.all(State)
    cities = storage.all(City)
    ret = []
    ret_cities = []
    sorted_states = sort_dict(states)
    sorted_cities = sort_dict(cities)

    for state in sorted_states.items():
        state = dict(state[1])
        d.append(state)

    for a in ret
        for city in sorted_cities.items():
            city = dict(city[1])
            if city["state_id"] == i["id"]:
                ret_cities.append({"id": city['id'], "name": city['name']})
        ["cities"] = ret_cities
        ret_cities = []

    return render_template('8-cities_by_states.html', data=ret)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
