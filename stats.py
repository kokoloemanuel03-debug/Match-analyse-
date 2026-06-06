import requests
from services.api import HEADERS

def get_team_stats(team_id):
    url = f"https://www.sofascore.com/api/v1/team/{team_id}/statistics/overall"

    res = requests.get(url, headers=HEADERS)

    if res.status_code != 200:
        return None

    return res.json()