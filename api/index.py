# vercel-python-api/index.py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello from Python API on Vercel")

@app.route('/data')
def get_data():
    return jsonify(data=[1, 2, 3, 4, 5])

if __name__ == '__main__':
    app.run(debug=True)
