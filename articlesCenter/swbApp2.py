import flask
from flask import request, render_template, session
import sqlite3

app = flask.Flask(__name__, static_url_path='')
app.debug = True

cu = None


@app.before_first_request
def con():
    global cu
    # 连接数据库,创建连接对象
    cx = sqlite3.connect("test.db")
    # 创建游标
    cu = cx.cursor()


@app.route('/')
def hello_world():
    return render_template("main.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
