
from flask import Flask
from flask import request
import databasef

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p>username: <input name="username"></p>
              <p>password: <input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    #databasef.database_init()
    #databasef.set_useraccount(1, request.form['username'], request.form['password'])
    x = databasef.get_useraccountByid()
    num = len(x)
    for i in range(0, num):
        if request.form['username'] == x[i][1] and request.form['password']== x[i][2]:
            return '<h3>Hello, admin!</h3>'
    # if request.form['username']== x[0][1] and request.form['password']== x[0][2]:
    return '<h3>Bad username or password.</h3>'


@app.route('/enroll', methods=['GET'])
def enroll_form():
    return '''<form action="/enroll" method="post">
              <p>username: <input name="username"></p>
              <p>password: <input name="password" type="password"></p>
              <p>password cofirm:<input name="password cofirm" type="password"></p>
              <p><button type="submit">Enroll In</button></p>
              </form>'''

@app.route('/enroll', methods=['POST'])
def enroll():
    # 需要从request对象读取表单内容：
    #databasef.database_init()
    x = databasef.get_useraccountByid()
    num = len(x)
    userid = num + 1
    databasef.set_useraccount(userid, request.form['username'], request.form['password'])
    return '<h3>Enroll Success!</h3>'


if __name__ == '__main__':
    app.run()