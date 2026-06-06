import requests
from services.api import HEADERS

def search_team(name):
    url = f"https://www.sofascore.com/api/v1/search/all?q={name}"

    res = requests.get(url, headers=HEADERS)

    if res.status_code != 200:
        return None

    data = res.json()

    for item in data.get("results", []):
        if item["type"] == "team":
            return item["entity"]["id"]

    return None