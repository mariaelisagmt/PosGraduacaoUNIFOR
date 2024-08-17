from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/people/', methods=['GET'])
def get_people():
    response = requests.get('https://swapi.dev/api/people')
    return jsonify(response.json())

@app.route('/api/planets', methods=['GET'])
def get_planets():
    response = requests.get('https://swapi.dev/api/planets')
    return jsonify(response.json())

@app.route('/', methods=['GET'])
def index():
    return "<p> Hello, Word!</p>"
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)