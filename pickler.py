from lib2to3.pgen2 import token
from transformers import AutoTokenizer, AutoModelForCausalLM

import pickle

MODEL_FILE_NAME = 'model_file'

def save_model():
    tokenizer = AutoTokenizer.from_pretrained("Meli/GPT2-Prompt")
    model = AutoModelForCausalLM.from_pretrained("Meli/GPT2-Prompt", pad_token_id =tokenizer.eos_token_id)

    print('Saving model into a pickle file..')
    with open(MODEL_FILE_NAME, 'wb') as model_file:
        pickle.dump((model,tokenizer), model_file, protocol=pickle.HIGHEST_PROTOCOL)
    print('Model saved')

if __name__ == '__main__':
    save_model()