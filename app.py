from flask import Flask, request, render_template
from pickler import MODEL_FILE_NAME
from transformer import generate_prompt

import pickle
import json


app = Flask('app',
            static_folder='static',
            template_folder='static/templates')


# Pre-loading model for quicker prompt generation
with open(MODEL_FILE_NAME, 'rb') as model_file:
    model, tokenizer = pickle.load(model_file)


# Prompt generator API at /api
# Expects a json with a single element 'q' to be the input text to generate the prompt from
@app.route('/api', methods=['POST'])
def api():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = json.loads(request.data)
        return generate_prompt(data['q'], model, tokenizer)
    else:
        return 'Content-Type not supported!'

# Homepage for GUI entry
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)