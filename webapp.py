
from flask.app import Flask
from flask import render_template, url_for, redirect
import re

#if entrypoint is not defined, app engine will look for an app
app = Flask(__name__)

Sentiments = ["Happiness","Confused","Fear","Anger","Surprise"]

Captions = ["The only joy in the world is to begin.",
            "Happiness depends upon ourselves.",
            "Happy people plan actions, they don’t plan results.",
            "Courage is knowing what not to fear.",
            "Find out what you’re afraid of and go live there."]

@app.route('/')
def display():
    return render_template("index.html", len = len(Sentiments), Sentiments = Sentiments)

@app.route('/execute')
def execute():
    return "executed successfully"
#if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
app.run(use_reloader = True, debug=True)


@app.route('/checkF')
def checkF(feel):
    SortedCap = []
    if(feel=="Happiness"):
        for i in range(0, len(Captions)):
            hap = re.search("Happ|joy", Captions[i])
            if(hap):
                SortedCap.append(Captions[i])
        print(SortedCap[i])
    elif(feel=="Fear"):
        for j in range(0,len(SortedCap)):
            fear = re.search("fear",Captions[j])
            if(fear):
                if(SortedCap):
                    SortedCap = []
                    SortedCap.append(Captions[i])
        print(SortedCap[i])
    return render_template("result.html", SortedCap = SortedCap)