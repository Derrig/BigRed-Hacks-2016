from flask import Flask, render_template
from random import randint
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test")
def tester():
    return "this is a test"

if __name__ == "__main__":
    app.run()
