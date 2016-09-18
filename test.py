from flask import Flask, render_template
import data_fetcher
from werkzeug.contrib.cache import SimpleCache
import json

electricity=json.dumps(data_fetcher.main(), sort_keys=True)
print electricity
