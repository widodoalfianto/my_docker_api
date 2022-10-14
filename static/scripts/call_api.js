// Calls our prompt generator API at /api with some text input
// Alerts user in case of an empty entry
async function call_api() {
    q = document.getElementById('q').value

    if (q == null || q == "") {
        alert('Cannot generate prompt from an empty entry. Please enter some text.')
    }
    else {
        document.getElementById('q').disabled = true;
        document.getElementById('generate_button').disabled = true;
        document.getElementById('generate_button').innerHTML = 'Generating..'

        data = { q:q }
        headers = { 'Content-Type': 'application/json' }

        axios.post('/api', data, {
            headers: headers
        })
        .then(function (response) {
            document.getElementById('res').innerHTML = '<textarea rows="20" cols="100">' + response.data + '</textarea>'
            document.getElementById('generate_button').disabled = false;
            document.getElementById('q').disabled = false;
            document.getElementById('generate_button').innerHTML = 'Generate'
        })
    }      
}