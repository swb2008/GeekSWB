import flask
from flask import request, render_template, session
import sqlite3

app = flask.Flask(__name__, static_url_path='')
app.debug = True

cu = None
cx = None


@app.before_first_request
def con():
    global cu
    global cx
    # 连接数据库,创建连接对象
    cx = sqlite3.connect("test.db")
    # 创建游标
    cu = cx.cursor()


@app.route('/')
def hello_world():
    return render_template("main.html")


@app.route('/create', methods=["post"])
def create():
    t = request.form.get('title')
    c = request.form.get('content')
    cu.execute("insert into articles ( title, content, author) VALUES ('%s','%s','%s')" % (t, c, 'swb'))
    cx.commit()

    return render_template("main.html", msg='发布成功')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
