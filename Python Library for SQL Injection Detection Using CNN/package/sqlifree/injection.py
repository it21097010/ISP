import requests


def prediction(val):
    # Set the base URL of your FastAPI application
    url = f'http://127.0.0.1:8000/pred/?input={val}'
    
    headers = {
        'accept': 'application/json'
    }
    # Send POST request to the /predict/{input}
    res = requests.post(url, headers=headers)

    if res.status_code == 200:
        return res.json()
    else:
        return f'Request failed! {res.status_code}'