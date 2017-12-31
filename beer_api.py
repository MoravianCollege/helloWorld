
import requests
import flask

app = flask.Flask(__name__)


@app.route('/')
def inventory():
    return '{}'


if __name__ == '__main__':
    app.run(port=3000, debug=False)
