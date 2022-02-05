from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello There"

@app.route("/index")
def index():
    return "<h1>Hello there</h1>"

@app.route("/title")
def title():
    return "<h1>Hello there</h1>"

@app.route("/title1")
def title1():
    return "<h1>Hello there</h1>"

if __name__ == '__main__':
    app.run()
else:
    app.run()