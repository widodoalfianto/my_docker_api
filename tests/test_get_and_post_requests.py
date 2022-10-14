import requests

SAMPLE_QUERY = '?q=To be or not to be'
SAMPLE_PAYLOAD = { 'q' : 'To be or not to be'}

api_url = 'http://127.0.0.1:8000/api'

'''
    Testing our api by sending it a GET request
    The api should return status code 405 since it does not accept GET requests
'''
def test_get_request():
    response = requests.get(api_url + SAMPLE_QUERY)
    
    assert response.status_code == 405

'''
    Testing our API by sending a sample POST request
    The api should return status code 200
'''
def test_post_request():
    payload = SAMPLE_PAYLOAD
    response = requests.post(url=api_url, json=payload)
    
    assert response.status_code == 200

if __name__ == '__main__':
    print('This is a test module to be run with pytest.')