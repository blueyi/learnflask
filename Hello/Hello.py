from flask import Flask, request, make_response
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello %s!</h1>' % name

@app.route('/cookie')
def re_cookie():
    response = make_response('<h1>This document carries a cookie</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your broswer is %s</p>' % user_agent

if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0')
    manager.run()
