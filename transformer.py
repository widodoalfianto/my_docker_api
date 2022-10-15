from pickler import MODEL_FILE_NAME
import pickle
import regex as re

MAX_LENGTH = 1000

def generate_prompt(input_text, model, tokenizer):
    input_text = input_text.strip()
    input_text += '[endprompt]'
    input_ids = tokenizer.encode(input_text, 
                                return_tensors='pt')

    output = model.generate(input_ids,
                        max_length=MAX_LENGTH,
                        num_beams=5,
                        no_repeat_ngram_size= 2,
                        early_stopping= True)

    return clean_text(tokenizer.decode(output[0], skip_special_tokens=True))


def clean_text(text):
    newline_pattern = r'\s*\[newline\]\s*'
    endprompt_pattern = r'.*\[endprompt\]\s*'

    text = re.sub(endprompt_pattern, '', text)
    text = re.sub(newline_pattern, '\n', text)
    
    return text.strip()

if __name__ == '__main__':
    # For local testing
    with open(MODEL_FILE_NAME, 'rb') as model_file:
        model, tokenizer = pickle.load(model_file)

    sentence = 'Who is Donald Trump?'
    prompt = generate_prompt(sentence, model, tokenizer)

    print(prompt)