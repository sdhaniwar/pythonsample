
from flask.app import Flask
from flask import render_template
import re

#if entrypoint is not defined, app engine will look for an app
app = Flask(__name__)

Feelings = ["Happiness","Confused","Fear","Anger","Surprise"]

Captions = ["The only joy in the world is to begin.",
            "Happiness depends upon ourselves.",
            "Happy people plan actions, they don’t plan results.",
            "Courage is knowing what not to fear.",
            "Find out what you’re afraid of and go live there."]


for i in range(0, len(Captions)):
    hap = re.search(".Happ.",Captions[i])

@app.route('/')
def display():
    return render_template("index.html", len1 = len(Feelings), Feelings = Feelings, len2 = len(hap) , hap = hap)

#if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
app.run(use_reloader = True, debug=True)