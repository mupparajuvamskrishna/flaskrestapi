#!flask/bin/python
from flask import Flask
from flask import abort, Flask, jsonify, request
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app = Flask(__name__)
analyser = SentimentIntensityAnalyzer()

@app.route('/api/v1/analyzeSentiment', methods = ['POST'])
def analyzeSentiment():
    if not request.json or not 'message' in request.json:
        abort(400)
    
    if 'message' in request.json:
        return jsonify(analyser.polarity_scores(request.json['message']))
    else:
        return not_found()
		


@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
