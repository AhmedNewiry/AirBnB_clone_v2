#!/usr/bin/python3
"""A script that starts a flask web application"""


from flask import Flask, render_template
from models import storage
import os
app = Flask(__name__)


@app.teardown_appcontext
def teardown_app():
    """remove the current sqlalchemy session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cit_by_stat_route():
    """displays HTML page"""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
