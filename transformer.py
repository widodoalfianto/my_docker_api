from pickler import MODEL_FILE_NAME
import pickle

def generate_prompt(input_text, model, tokenizer):
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    output = model.generate(input_ids,
                        max_length=25,
                        num_beams=5,
                        no_repeat_ngram_size= 2,
                        early_stopping= True)

    return(tokenizer.decode(output[0], skip_special_tokens=True))


if __name__ == '__main__':
    # For local testing
    with open(MODEL_FILE_NAME, 'rb') as model_file:
        model, tokenizer = pickle.load(model_file)

    sentence = 'To be or not to be'
    prompt = generate_prompt(sentence, model, tokenizer)

    print(prompt)