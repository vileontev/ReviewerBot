import requests
import time
from auth import get_access_token

def get_reviews(star_filter=None):
    url = "https://api-seller.ozon.ru/v1/review/list"
    access_token = get_access_token()

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

# Фильтр отзывов по звездам
    body = {"filter": {"status": "unanswered"}}
    if star_filter:
        body["filter"]["stars"] = {star_filter}

    response = requests.post(url, json=body, headers=headers)

    if response.status_code == 200:
        return response.json().get("reviews", [])
    else:
        raise Exception("Ошибка при запросе отзывов:", response.text)
    
def parse_reviews():
    reviews = get_reviews()
    for review in reviews:
        print("Обработка отзыва:", review["text"])
        time.sleep(5)
        yield review