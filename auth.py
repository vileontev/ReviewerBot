import requests
import json

def refresh_access_token():
    with open("config.json", "r") as file:
        config = json.load(file)

    refresh_url = config["api_url_token_refresh"]
    refresh_token = config["refresh_token"]

    response = requests.post(
        refresh_url,
        json={"grant_type": "refresh_token", "refresh_token": refresh_token},
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        tokens = response.json()
        config["access_token"] = tokens["access_token"]
        with open("config.json", "w") as file:
            json.dump(config, file)
        return tokens["access_token"]
    else:
        raise Exception("Ошибка обновления токена:", response.text)

def get_access_token():
    with open("config.json", "r") as file:
        config = json.load(file)

    return config["access_token"]