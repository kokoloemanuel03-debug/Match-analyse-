from flask import Flask, render_template, request

from services.teams import search_team
from services.matches import check_match
from services.stats import get_team_stats
from services.prediction import predict_match

app = Flask(__name__)


# 🟢 PAGE ACCUEIL
@app.route("/")
def index():
    return render_template("index.html")


# 🟡 PAGE INPUT (ANALYSE)
@app.route("/analyse")
def analyse():
    return render_template("analyse.html")


# ⚙️ TRAITEMENT FORMULAIRE
@app.route("/process", methods=["POST"])
def process():

    # 🔥 INPUTS viennent de analyse.html
    team1 = request.form["team1"]
    team2 = request.form["team2"]

    # 🔎 équipes
    id1 = search_team(team1)
    id2 = search_team(team2)

    if not id1 or not id2:
        return "❌ Équipe introuvable"

    # ⚽ match
    match = check_match(id1, id2)

    if not match:
        return "❌ Match introuvable"

    # 📊 stats
    stats1 = get_team_stats(id1)
    stats2 = get_team_stats(id2)

    # 🔮 prédiction
    prediction = predict_match(stats1, stats2)

    # 🟢 RESULTAT
    return render_template(
        "result.html",
        team1=team1,
        team2=team2,
        match=match,
        stats1=stats1,
        stats2=stats2,
        prediction=prediction
    )

@app.route("/contact")
def contact():
    render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)