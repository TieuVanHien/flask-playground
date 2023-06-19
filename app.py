from flask import Flask, redirect, url_for, request, render_template, make_response
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie("userID", user)
    return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+ name +'</h1>'

    
if __name__ == "__main__":
    app.run(debug=True)
