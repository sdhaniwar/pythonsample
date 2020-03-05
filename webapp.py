from flask import Flask;

#if entrypoint is not defined, app engine will look for an app
app = Flask(__name__)

def display():
    print("Digital1")
    print("Mainframe")
    print("Healthcare")
    print("Java")

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)