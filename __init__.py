from flask import Flask, render_template
import data_fetcher
from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()
app = Flask(__name__)

@app.route("/")
def index():
    # return ''.join('{}{}'.format(key, val) for key, val in sorted(data_fetcher.main().items()))
    id = 'homepage'
    value = cache.get(id)
    if value is not None:
        print "used cache -----------------------------"
        return value
    print 'no cache ------------------------'
    value = render_template('index.html')
    cache.set(id, value, timeout=60 * 5)
    return value

@app.route("/ohGod")
def tester():
    return "what are we doing"

@app.route("/secret")
def secret():
    """TODO: Docstring for secret.
    :returns: TODO
    """
    return 'This is a secret page. Congratulations for finding this page! Please contact Byungchan Lim at bl458@cornell.edu, and (408)-203-0543 for your prize!'

if __name__ == "__main__":
    app.run()
