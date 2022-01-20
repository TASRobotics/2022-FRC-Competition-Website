from flask import Flask, render_template, url_for
from website import create_app

app = create_app()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/scout')
def scout():
    return render_template('scout.html')

@app.route('/data')
def data():
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)