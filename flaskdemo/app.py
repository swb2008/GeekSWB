import flask
from flask import request, render_template, session
from flask import make_response
import random

app = flask.Flask(__name__, static_url_path='')
app.secret_key = "wefwefwef65"
app.debug = True


@app.route('/')
def hello_world():
    # 跳转到登录页
    p = session.get("user_info")
    if not p:
        return render_template("login.html")
    else:
        return render_template("main.html")


@app.route('/user/<int:name>')
def user(name):
    print(type(name))
    return 'Hello,%s!' % name


@app.route('/info', methods=["post"])
def info():
    name = request.form.get("username")
    password = request.form.get("password")
    d = {}
    with open("userinfo", "r") as f:
        d = eval(f.read())
    if d.__contains__(name):
        # session是一个特殊的字典 {"":"","":""}
        session["user_info"] = name
        return render_template("main.html", msg2=name)
    else:
        return render_template("login.html", msg='用户名或密码错误')


@app.route('/logout')
def logout():
    del session["user_info"]
    return render_template("login.html")


#
# @app.route('/rule')
# def rule():
#     return render_template("rule.html")

@app.route("/create")
def creat_room():
    """生成目标数字，创建房间号"""
    room_num = str(random.randint(1, 20))
    target_num = str(random.randint(1, 200))
    r_t_n = room_num + " " + target_num
    with open("room_tag.txt", "a+") as f:
        f.write(r_t_n + "/n")
    return "创建的房间号为：%s,生成目标数字是%s" % (room_num, target_num)


if __name__ == '__main__':
    print(app.url_map)
    app.run()
