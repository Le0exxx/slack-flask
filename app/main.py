from flask import Flask, jsonify, request
from matchdc import match, dcmap
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dcmap', methods=['POST'])
def slash():
    if request.form['token'] == 'XVUMLgbFulZj6jF16Qk8J3cg':
        if request.form['text']:
            if match(request.form['text']):
                payload = {'text': match(request.form['text'])}
            else:
                payload = {'text': 'DC Not Found'}
        else:
            payload = {'text': json.dumps(dcmap)}
        return jsonify(payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)