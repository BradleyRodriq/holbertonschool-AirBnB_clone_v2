from flask import Flask
""" starts the flask app """

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ returns hello HBNB """
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def funC(text):
    """ returns C """
    return 'C ' + text.replace('_', ' ')

@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyfun(text):
    """ returns python """
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<n>', strict_slashes=False)
def its_a_num(n):
    """ returns the number """
    return str(n) + " is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)