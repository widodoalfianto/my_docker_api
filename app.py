from flask import Flask, request, render_template, make_response
from pickler import MODEL_FILE_NAME
from transformer import generate_prompt

import pickle
import json


MAX_INPUT_LENGTH = 200


app = Flask('app',
            static_folder='static',
            template_folder='static/templates')


# Pre-loading model for quicker prompt generation
with open(MODEL_FILE_NAME, 'rb') as model_file:
    model, tokenizer = pickle.load(model_file)

def response_400(result):
    response = make_response(result)
    response.status_code = 400
    return response

# Prompt generator API at /api
# Expects a json with a single element 'q' to be the input text to generate the prompt from
@app.route('/api', methods=['POST'])
def api():

    # Validate headers
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = json.loads(request.data)

        # Validate data entry
        if data['q']:

            q = data['q']
            # Make sure data is a string
            if type(q) == str:

                # Input over max length
                if len(q) > MAX_INPUT_LENGTH:
                    result = 'Input over length limit: 200'
                    return response_400(result)
                
                # Valid input
                else:
                    result = generate_prompt(q, model, tokenizer)

                    response = make_response(result)
                    response.status_code = 200

                    return response
            
            else:
                result = f'Object of type {type(q)} is not a valid input. Please enter a string.'
                return response_400(result)

        # Empty request
        else:
            result = 'Empty request'
            return response_400(result)

    # No JSON body
    else:
        result = 'Unsupported content type'
        return response_400(result)


# Homepage for GUI entry
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)