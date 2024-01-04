#!/usr/bin/python3
"""A script that starts a flask web application"""


from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """remove the current sqlalchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_route():
    """displays HTML page"""
    states = storage.all('State').values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id_route(id):
    """displays HTML page"""
    states = storage.all('State').values()
    state = states[id]
    if state:
        return render_template('9-states.html',
                               state=state)
    else:
        return render_template('9-states.html',
                               state=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
