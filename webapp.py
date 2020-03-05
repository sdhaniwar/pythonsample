
from flask.app import Flask
from flask import render_template

#if entrypoint is not defined, app engine will look for an app
app = Flask(__name__)

Feelings = ["Happiness","Confused","Fear","Anger","Surprise"]

@app.route('/')
def display():
    return render_template("index.html", len = len(Feelings), Feelings = Feelings)

#if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
app.run(use_reloader = True, debug=True)