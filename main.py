from flask import Flask, jsonify, render_template, redirect
import requests
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from prometheus_flask_exporter import PrometheusMetrics

def get_random_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.request("GET", url)
    data = response.json()
    quote = data[0]['h']
    return quote


app = Flask(__name__)
metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')



limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="memory://",
)
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/hello', methods=['GET'])
@limiter.limit("10 per minute")
def hello():
    return jsonify({"greeting": "Hello world!"})


@app.route('/quote', methods=['GET'])
@limiter.limit("5 per minute")
def quote():
    quote = get_random_quote()
    return jsonify({"quote": quote})


# Catch-all route for non-existing routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
