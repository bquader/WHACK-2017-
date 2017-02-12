from flask import Flask
from flask import request

import interface
import json

app = Flask(__name__)

@app.route("/quote")
def hello():
    if 'word' in request.args:
        w = request.args['word'].upper()
        return interface.getQuotes(w)
    else:
        return 'Don\'t make your own API calls'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
