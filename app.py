from flask import Flask, request
from pickler import MODEL_FILE_NAME
from transformer import generate_prompt

import pickle

app = Flask('app')
with open(MODEL_FILE_NAME, 'rb') as model_file:
    model, tokenizer = pickle.load(model_file)

@app.route('/api', methods=['GET'])
def api():
    q = request.args.get('q')
    return generate_prompt(q, model, tokenizer)

@app.route('/', methods=['GET'])
def home():
    return "/api?q=some_query"

if __name__ == '__main__':
    app.run(debug=True)