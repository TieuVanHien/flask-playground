from flask import Flask, redirect, url_for, request, render_template, make_response
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        sub = request.form['sub']
        age = request.form['age']
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie("userID", user)
    resp.set_cookie("subject", sub)
    resp.set_cookie("age", age)
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    sub = request.cookies.get('subject')
    age = request.cookies.get('age')
    return '<1h> You are ' + name + ' and you are ' + age + ' and your favorite subject is ' + sub + '</h1>'   
     
if __name__ == "__main__":
    app.run(debug=True)
