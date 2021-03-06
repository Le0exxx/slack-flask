from flask import Flask, jsonify, request
from matchdc import match, dcmap

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dcmap', methods=['POST'])
def slash():
    if request.form['token'] == 'A1KQ1quNPDZxyUy25NxCyZld':
        if request.form['text']:
                payload = {'text': match(request.form['text'])}
        else:
            payload = {'text': dcmap}
        return jsonify(payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)