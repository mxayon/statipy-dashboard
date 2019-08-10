from flask import Flask
from app import app

@app.route('/')
@app.route('/index')
def home():
    user = { 'username': 'Max' }
    return '''
    <html>
    <head>
        <title>Statipy Dashboard</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
    </html>
    '''
