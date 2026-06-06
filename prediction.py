def strength(stats):
    goals = stats.get("goalsScored", 0)
    conceded = stats.get("goalsConceded", 1)
    matches = stats.get("matches", 1)

    attack = goals / matches
    defense = conceded / matches

    return (attack * 2) - defense


def predict_match(stats1, stats2):

    s1 = strength(stats1)
    s2 = strength(stats2)

    diff = s1 - s2

    if diff > 1:
        return {
            "winner": "team1",
            "prob_team1": 65,
            "prob_draw": 20,
            "prob_team2": 15
        }

    elif diff < -1:
        return {
            "winner": "team2",
            "prob_team1": 15,
            "prob_draw": 20,
            "prob_team2": 65
        }

    else:
        return {
            "winner": "draw",
            "prob_team1": 35,
            "prob_draw": 30,
            "prob_team2": 35
        }