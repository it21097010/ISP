import requests


def prediction(val):

    url = f'http://127.0.0.1:8000/pred/?input={val}' # Replace with actual base URL
    
    headers = {
        'accept': 'application/json'
    }
    # Send POST request to the /predict/{input}
    res = requests.post(url, headers=headers)

    if res.status_code == 200:
        # Process JSON response
        return res.json()
    else:
        return f'Request failed! {res.status_code}'