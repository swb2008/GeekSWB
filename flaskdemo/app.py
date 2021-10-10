import flask

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/python')
def py():
    return 'python'


@app.route('/user/<name>')
def user(name):
    return 'Hello,%s!' % name


if __name__ == '__main__':
    app.run()
