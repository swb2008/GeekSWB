import flask
from flask import request, render_template, session
from flask import make_response

app = flask.Flask(__name__,static_url_path='')
app.secret_key = "wefwefwef65"


@app.route('/')
def hello_world():
    #跳转到登录页
    p = session.get("user_info")
    if not p:
        return render_template("login.html")
    else:
        return "登陆成功"




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
        # session是一个特殊的字典 {"":"","":""}
        session["user_info"] = name
        return '登陆成功,%s'%name
    else:
        return render_template("login.html",msg='用户名或密码错误')


if __name__ == '__main__':
    print(app.url_map)
    app.run()

