from flask import Flask, render_template
from app import app

@app.route('/')
@app.route('/index')
def home():
    user = { 'username': 'Max' }
    views = [
    {
        'title': {'date': 'Artist'},
        'body': 'Artists in playlist by date'
    },
    {
        'title': {'date': 'Song Rating: PG-13/ALL'},
        'body': 'Song rating of tracks in playlist by date'
    }
    return render_template('index.html', title='Statipy', user=user)
