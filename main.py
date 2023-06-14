from flask import Flask, jsonify
import requests
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def get_random_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.request("GET", url)
    data = response.json()
    quote = data[0]['h']
    return quote


app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="memory://",
)

@app.route('/hello', methods=['GET'])
@limiter.limit("5 per minute")
def hello():
    return jsonify({"greeting": "hello world!"})


@app.route('/quote', methods=['GET'])
@limiter.limit("4 per minute")
def quote():
    quote = get_random_quote()
    return jsonify({"quote": quote})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
