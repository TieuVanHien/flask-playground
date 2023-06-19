from flask import Flask, render_template
app = Flask(__name__)

@app.route('/score/<int:score>')
def index(score):
   return render_template('hello.html', marks = score)

@app.route('/result')
def result():
    list = { 'math': 50, 'phy': 50, 'che': 60}
    return render_template('hello.html', result = list)

if __name__ == '__main__':
   app.run(debug = True)