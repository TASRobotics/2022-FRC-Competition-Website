from flask import Flask, render_template, url_for
from website import create_app

app = create_app()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/scout', methods=['GET', 'POST'])
def scout():
    return render_template('scout.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/auton')
def auton():
    return render_template('auton.html')

@app.route('/teleop')
def teleop():
    return render_template('teleop.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/auton1')
def test():
    return render_template('auton1.html')

if __name__ == '__main__':
    app.run(debug=True)