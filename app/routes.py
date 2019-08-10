from flask import Flask, render_template
from app import app

@app.route('/')
@app.route('/index')
def home():
    user = { 'username': 'Max' }
    return render_template('index.html', title='Home | Statipy', user=user)
