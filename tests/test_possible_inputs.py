import pytest
import requests
import random

import string

EMPTY_RESPONSE = 'Empty request'
OVER_MAX_LENGTH = 'Input over length limit: 200'
SEQUENCE_LENGTH = 10
MAX_LENGTH = 200

api_url = 'http://127.0.0.1:8000/api'

'''
    Sequence of numbers are generated from generating random integers between 0 and 100
    This sequence is then turned into a string, each number separated by a whitespace

    The api should return status code 200
'''
def test_sequence_of_numbers_as_str():
    
    sequence_of_numbers = []
    for i in range(0,SEQUENCE_LENGTH):
        sequence_of_numbers.append(random.randint(0,100))

    q_string = ''
    for num in sequence_of_numbers:
        q_string += str(num)
        q_string += (' ')

    payload = { 'q' : q_string[:-1]} 
    response = requests.post(url=api_url, json=payload)

    assert response.status_code == 200


'''
    Testing api with a JSON sequence of numbers as an input
    The api should return status code 400 for malformed input
'''
def test_sequence_of_numbers():
    
    sequence_of_numbers = []
    for i in range(0,SEQUENCE_LENGTH):
        sequence_of_numbers.append(random.randint(0,100))

    payload = { 'q' : sequence_of_numbers } 
    response = requests.post(url=api_url, json=payload)

    assert response.status_code == 400


'''
    Testing api with a single random number as input
    Random number is a random integer between 0 and 100

    The api should return status code 400 for malformed input
'''
def test_single_number():
    
    payload = { 'q' : random.randint(0,100)} 
    response = requests.post(url=api_url, json=payload)

    assert response.status_code == 400

'''
    Testing api with a single random number converted to string as input
    Random number is a random integer between 0 and 100

    The api should return status code 200
'''
def test_single_number_as_str():
    
    payload = { 'q' : str(random.randint(0,100))} 
    response = requests.post(url=api_url, json=payload)

    assert response.status_code == 200


'''
    Testing api with a single random alphabet character as input text
    The api should return status code 200
'''
def test_single_alphabet():
    
    random_alphabet = random.choice(string.ascii_letters)
    payload = { 'q' : random_alphabet} 
    response = requests.post(url=api_url, json=payload)

    assert response.status_code == 200


'''
    Testing api with a sequence of random words converted to string
    Words are randomly generated and concatenated together with a whitespace in between
    This should be the most typical/expected entry for our api
    
    The api should return status code 200
'''
def test_sequence_of_random_words_as_str():
    
    sequence_of_random_words = []
    curr_word = ''
    for i in range(0,SEQUENCE_LENGTH):
        
        # Generating randomized word each of a random length between 1-10
        for j in range(0, random.randint(1,SEQUENCE_LENGTH)):
            curr_word += random.choice(string.ascii_letters)
        sequence_of_random_words.append(curr_word)
        curr_word = ''

    q_string = ''
    for word in sequence_of_random_words:
        q_string += word
        q_string += ' '

    payload = { 'q' : q_string[:-1]} 
    response = requests.post(url=api_url, json=payload)

    assert response.status_code == 200


'''
    Testing api with a JSON sequence of random words as an input
    The api should return status code 400 for malformed input
'''
def test_sequence_of_random_words_as_str():
    sequence_of_random_words = []
    curr_word = ''
    for i in range(0,SEQUENCE_LENGTH):
        
        # Generating randomized word each of a random length between 1-10
        for j in range(0, random.randint(1,SEQUENCE_LENGTH)):
            curr_word += random.choice(string.ascii_letters)
        sequence_of_random_words.append(curr_word)
        curr_word = ''


    payload = { 'q' : sequence_of_random_words} 
    response = requests.post(url=api_url, json=payload)

    assert response.status_code == 400


'''
    Testing api with an input of length over the set maximum length allowed
    The api should return status code 400 for malformed input
'''
def test_over_max_length_input():
    
    over_max_length =  ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=MAX_LENGTH+1))
    payload = { 'q' : over_max_length} 
    response = requests.post(url=api_url, json=payload)
    
    assert response.status_code == 400
    assert response.text == OVER_MAX_LENGTH


'''
    Testing api with an input of length of exactly the set maximum length allowed
    The api should return status code 200
'''
def test_max_length_input():
    over_max_length =  ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=MAX_LENGTH))
    payload = { 'q' : over_max_length} 
    response = requests.post(url=api_url, json=payload)
    
    assert response.status_code == 200

if __name__ == '__main__':
    print('This is a test module to be run with pytest.')