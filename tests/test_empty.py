import pytest
import requests
import json

EMPTY_RESPONSE = 'Empty request'

api_url = 'http://127.0.0.1:8000/api'

'''
    Testing the api with an empty input text
    The api should return a status 400 for malformed input
'''
def test_empty():
    payload = { 'q' : ''} 
    response = requests.post(url=api_url, json=payload)

    assert response.headers['Content-Type'] == 'text/html; charset=utf-8'
    assert response.status_code == 400
    assert response.text == EMPTY_RESPONSE

if __name__ == '__main__':
    print('This is a test module to be run with pytest.')