from flask import Flask, jsonify

app = Flask(__name__)

scores = [
    {"player": "Om", "game": "Chess", "score": 85},
    {"player": "Rahul", "game": "Carrom", "score": 72},
    {"player": "Aryan", "game": "Chess", "score": 68}
]


@app.route("/")
def home():
    return """
    <h1>🎮 Game Score Tracker</h1>
    <p>Welcome to the Game Score Tracker!</p>
    <p>Track and view game scores easily.</p>
    <a href="/scores">View Scores</a><br>
    <a href="/leaderboard">View Leaderboard</a>
    """


@app.route("/scores")
def view_scores():
    result = "<h1>Game Scores</h1>"

    for score in scores:
        result += f"""
        <p>
        Player: {score['player']} |
        Game: {score['game']} |
        Score: {score['score']}
        </p>
        """

    return result


@app.route("/leaderboard")
def leaderboard():
    sorted_scores = sorted(scores, key=lambda x: x["score"], reverse=True)

    result = "<h1>🏆 Leaderboard</h1>"

    for position, score in enumerate(sorted_scores, start=1):
        result += f"""
        <p>
        {position}. {score['player']} -
        {score['game']} -
        {score['score']} points
        </p>
        """

    return result


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)