from flask import Flask, redirect


app_flask = Flask(__name__)

@app_flask.route('/')
@app_flask.route('/index')
@app_flask.route('/home')
def render_dashboard():
    return redirect('/dash')
