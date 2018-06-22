from flask import Flask, jsonify, request
from matchdc import match,dcmap

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
            Payload = {'text': 'please input DC you want to query with format: /dcmap DC10'}
        #payload = {'text': 'DC15 Shanghai'}
        return jsonify(payload)


if __name__ == '__main__':
    app.run()
