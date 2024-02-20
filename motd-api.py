from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_PORT = os.getenv('APP_PORT')
MESSAGE = os.getenv('MESSAGE')

@app.route('/', methods=['GET'])
def hello():
    data={
        "message":MESSAGE
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=APP_PORT)