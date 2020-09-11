from flask import Flask
from flask_restful import Api
from flask import request
from utils import *
from data_process import *
from  flask import jsonify

app = Flask(__name__)
api = Api(app)


def hello_world():
    return 'Hello World!'
@app.route('/', methods=['GET', 'POST'])
def parse_aspect_distances():
    sent = request.args.get('sentence')
    aspect = request.args.get('aspect')
    start = request.args.get('start')
    end = request.args.get('end')
    sentences = []
    sentences.append({'sentence': sent, 'aspect': aspect, 'start': start, 'end': end})
    result = get_sentence_vector(sentences)
    print(result[0])
    return jsonify(result[0])



if __name__ == '__main__':
    app.run(debug=True)