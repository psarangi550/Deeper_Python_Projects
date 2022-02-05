import importlib

flask=importlib.import_module("flask")#here loading up the flask module using the importlib module

app=flask.Flask(__name__)

@app.route('/')
def index():
    return "<h1> Hello There </h1>"


if __name__=="__main__":
    app.run()