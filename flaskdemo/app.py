import flask
from flask import request

app = flask.Flask(__name__,static_url_path='')


@app.route('/')
@app.route('/home')
def hello_world():
    user_agent = request.headers.get("User-Agent")
    return 'Hello World!%s' % user_agent


@app.route('/python')
def py():
    return 'python'


@app.route('/user/<int:name>')
def user(name):
    print(type(name))
    return 'Hello,%s!' % name


if __name__ == '__main__':
    print(app.url_map)
    app.run()

