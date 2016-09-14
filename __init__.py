from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "We're alive! Schuyler for life!"
if __name__ == "__main__":
    app.run()
