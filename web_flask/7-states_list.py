#!/usr/bin/python3
"""A script that starts a flask web application"""


from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """remove the current sqlalchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_route():
    """displays HTML page"""
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
