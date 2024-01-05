#!/usr/bin/python3

"""
Starts a Flask web application
"""


from flask import Flask, render_template, url_for
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


def sort_dict(Class, by="name"):
    """ Function thatsort dictionary """
    return dict(sorted(Class.items(), key=lambda x: x[1][by]))


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of all State & city objects"""
    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)
    ret = []
    ret_cities = []
    ret_amen = []
    sorted_states = sort_dict(states)
    sorted_cities = sort_dict(cities)
    sorted_amen = sort_dict(amenities)

    for state in sorted_states.items():
        state = dict(state[1])
        ret.append(state)

    for amenity in sorted_amen.items():
        amenity = dict(amenity[1])
        ret_amen.append(amenity)

    for i in ret:
        for city in sorted_cities.items():
            city = dict(city[1])
            if city["state_id"] == i["id"]:
                ret_cities.append({"id": city['id'], "name": city['name']})
        i["cities"] = ret_cities
        ret_cities = []

    return render_template('10-hbnb_filters.html', data=ret, amen=ret_amen)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
