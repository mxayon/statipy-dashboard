from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'Max' }
    views = [
        {
            'head': 'Artist',
            'body': 'Artists in playlist by date'
        },
        {
            'head': 'Song Rating: PG-13/ALL',
            'body': 'Song rating of tracks in playlist by date'
        }
    ]
    return render_template('index.html', title='Statipy', user=user, views=views)
