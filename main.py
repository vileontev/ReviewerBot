import requests

url = "https://seller.ozon.ru/api/v3/review/list"
refresh_url = "https://api.ozon.ru/auth/token"

refresh_token = "7.69242093.ofjNYAePR4aq1KI76zLG6g.89.Af1Q5C7RnT8X4C5L8Y-x369acSRK56_bhrnOYFEA47aGVEJ0coj_CZUmlrW2151Qf7nx611BkobHII2gVpceoefZOhe47r0uAtv81D78xHf1.20210612201846.20250127110835.UIRPfdg800MxJlFVb0y3php-P4mTKXZXiSBoPjg_39k.11343d96646204858"

data = {
    "grant_type": "refresh_token",
    "refresh_token": refresh_token
}

headers = {
    "Authorization": "Bearer ",
    "Content-Type": "application/json"
}

response = requests.post(refresh_url, json=data, headers=headers)

