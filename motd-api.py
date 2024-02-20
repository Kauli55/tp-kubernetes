from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_PORT = os.getenv('APP_PORT')
MESSAGE = os.environ.get('MESSAGE')

@app.route('/', methods=['GET'])
def hello():
    return jsonify(message=MESSAGE)

if __name__ == '__main__':
    app.run(debug=True, port=APP_PORT)