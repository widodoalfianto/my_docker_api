# my_docker_api
Take home project for an internship
<br><br>
This is a Flask API that runs on a Docker container, generating a prompt conditioned on an input text it is given.
<br><br>

```
# Example of an API call
response = requests.post(url='hostname/api', { 'q' : 'To be or not to be'})
```
```
curl -d '{"q": "some text"}' -H 'Content-Type: application/json' hostname/api
```

<br>
Before building and deploying, run the following command:<br>

```
python pickler.py
```

The model is loaded onto the app from a pickle file.<br>
The pickler module downloads the model and saves the model for it to be loaded onto the app.<br>
<br>
Model source from Hugging Face Hub:hugs::<br>
[https://huggingface.co/Meli/GPT2-Prompt](https://huggingface.co/Meli/GPT2-Prompt)
<br>
Docker commands:
```
docker build --tag app:latest .
docker run --publish 8000:5000 app
```
