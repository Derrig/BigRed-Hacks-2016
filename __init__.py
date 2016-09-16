from flask import Flask, render_template
from random import randint
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ohGod")
def tester():
    return "what are we doing"

if __name__ == "__main__":
    app.run()
