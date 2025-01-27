import requests

data = {
    "grant_type": "refresh_token",
    "refresh_token": refresh_token
}

headers = {
    "Authorization": "Bearer ",
    "Content-Type": "application/json"
}

response = requests.post(refresh_url, json=data, headers=headers)

