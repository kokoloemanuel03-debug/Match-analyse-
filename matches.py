import requests
from services.api import HEADERS

def check_match(team1_id, team2_id):
    url = f"https://www.sofascore.com/api/v1/team/{team1_id}/events/next/50"

    res = requests.get(url, headers=HEADERS)

    if res.status_code != 200:
        return None

    data = res.json()

    for event in data.get("events", []):
        home = event["homeTeam"]["id"]
        away = event["awayTeam"]["id"]

        if (home == team1_id and away == team2_id) or (home == team2_id and away == team1_id):
            return event

    return None