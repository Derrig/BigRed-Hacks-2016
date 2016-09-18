from flask import Flask, render_template
import data_fetcher
from werkzeug.contrib.cache import SimpleCache
import json

cache = SimpleCache()
app = Flask(__name__)

@app.route("/")
def index():
    # return ''.join('{}{}'.format(key, val) for key, val in sorted(data_fetcher.main().items()))
    id = 'homepage'
    value = cache.get(id)
    electricity=json.dumps(data_fetcher.main(), sort_keys=True)
    if value is not None:
        print "used cache -----------------------------"
        return value
    print 'no cache ------------------------'
    value = json.dumps(render_template('index.html', electricity=electricity))
    cache.set(id, value, timeout=60 * 5)
    return value

if __name__ == "__main__":
    app.run()
