import flask
from flask import request, render_template, session

app = flask.Flask(__name__, static_url_path='')
app.debug = True


@app.route('/')
def hello_world():
    return render_template("main.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
