import flask
from flask import request
from flask import make_response

app = flask.Flask(__name__,static_url_path='')


@app.route('/')
@app.route('/home')
def hello_world():
    return """<form action="/info" method="post">
        用户名：<input type="text" name="username"></br>
        密 码:<input type="text" name="password"></br>
        <button>登陆</button>
    </form>"""


@app.route('/python')
def py():
    return 'python'


@app.route('/user/<int:name>')
def user(name):
    print(type(name))
    return 'Hello,%s!' % name

@app.route('/error')
def err():
    re = make_response('<h1>系统走丢了</h1>')
    re.status_code = 666
    return re


@app.route('/info',methods=["post"])
def info():
    name = request.form.get("username")
    password = request.form.get("password")
    d = {}
    with open("userinfo","r") as f:
        d = eval(f.read())
    if d.__contains__(name):
        return '登陆成功,%s'%name
    else:
        return '登陆失败'


if __name__ == '__main__':
    print(app.url_map)
    app.run()

