import flask
from flask import request
from flask import make_response

app = flask.Flask(__name__,static_url_path='')


@app.route('/')
@app.route('/home')
def hello_world():
    # user_agent = request.headers.get("User-Agent")
    # return 'Hello World!%s' % user_agent
    return "index.html"


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
    dict = {}
    with open("userinfo","r") as f:
        dict = eval(f.read())
    print(dict)
    return '登陆成功,%s'%name


if __name__ == '__main__':
    print(app.url_map)
    app.run()

