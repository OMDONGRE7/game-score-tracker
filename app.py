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
    <!DOCTYPE html>
    <html>
    <head>
        <title>Game Score Tracker</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
            }

            body {
                min-height: 100vh;
                background:
                    radial-gradient(circle at top left, #263b73, transparent 35%),
                    radial-gradient(circle at bottom right, #512a68, transparent 35%),
                    #0b1020;
                color: white;
            }

            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 22px 8%;
                border-bottom: 1px solid rgba(255,255,255,0.1);
                background: rgba(10,15,30,0.65);
            }

            .logo {
                font-size: 22px;
                font-weight: bold;
            }

            nav a {
                color: #d7dcff;
                text-decoration: none;
                margin-left: 25px;
                font-size: 14px;
            }

            nav a:hover {
                color: white;
            }

            .hero {
                max-width: 1000px;
                margin: auto;
                padding: 100px 25px 60px;
                text-align: center;
            }

            .badge {
                display: inline-block;
                padding: 8px 15px;
                border-radius: 30px;
                background: rgba(255,255,255,0.1);
                border: 1px solid rgba(255,255,255,0.15);
                color: #bfc8ff;
                font-size: 13px;
                margin-bottom: 25px;
            }

            h1 {
                font-size: clamp(42px, 7vw, 72px);
                line-height: 1.05;
                margin-bottom: 20px;
            }

            .highlight {
                background: linear-gradient(90deg, #7c9cff, #c084fc);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            .subtitle {
                max-width: 600px;
                margin: auto;
                color: #aeb6cf;
                font-size: 18px;
                line-height: 1.7;
            }

            .buttons {
                margin-top: 35px;
            }

            .btn {
                display: inline-block;
                padding: 14px 24px;
                margin: 8px;
                border-radius: 12px;
                text-decoration: none;
                font-weight: bold;
                transition: 0.25s;
            }

            .primary {
                background: #ffffff;
                color: #101528;
            }

            .secondary {
                background: rgba(255,255,255,0.08);
                color: white;
                border: 1px solid rgba(255,255,255,0.15);
            }

            .btn:hover {
                transform: translateY(-3px);
            }

            .stats {
                max-width: 900px;
                margin: 30px auto 0;
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 18px;
                padding: 20px;
            }

            .stat {
                padding: 25px;
                border-radius: 18px;
                background: rgba(255,255,255,0.07);
                border: 1px solid rgba(255,255,255,0.1);
                backdrop-filter: blur(10px);
            }

            .stat h2 {
                font-size: 30px;
                margin-bottom: 6px;
            }

            .stat p {
                color: #9fa8c2;
                font-size: 14px;
            }

            footer {
                text-align: center;
                padding: 35px;
                color: #727b98;
                font-size: 13px;
            }

            @media (max-width: 650px) {
                nav {
                    padding: 18px 5%;
                }

                nav div:last-child {
                    display: none;
                }

                .stats {
                    grid-template-columns: 1fr;
                }

                .hero {
                    padding-top: 70px;
                }
            }
        </style>
    </head>

    <body>

        <nav>
            <div class="logo">🎮 GameTrack</div>

            <div>
                <a href="/">Home</a>
                <a href="/scores">Scores</a>
                <a href="/leaderboard">Leaderboard</a>
            </div>
        </nav>

        <section class="hero">

            <div class="badge">⚡ SIMPLE • FAST • TRACK YOUR GAME</div>

            <h1>
                Track Your <span class="highlight">Game.</span><br>
                Chase Your Score.
            </h1>

            <p class="subtitle">
                Keep your game scores organized, check player performance,
                and see who's leading the leaderboard.
            </p>

            <div class="buttons">
                <a class="btn primary" href="/scores">
                    View Scores →
                </a>

                <a class="btn secondary" href="/leaderboard">
                    🏆 Leaderboard
                </a>
            </div>

            <div class="stats">

                <div class="stat">
                    <h2>3</h2>
                    <p>Players Tracked</p>
                </div>

                <div class="stat">
                    <h2>2</h2>
                    <p>Games Recorded</p>
                </div>

                <div class="stat">
                    <h2>85</h2>
                    <p>Highest Score</p>
                </div>

            </div>

        </section>

        <footer>
            GameTrack • DevOps Lab Mini Project
        </footer>

    </body>
    </html>
    """


@app.route("/scores")
def view_scores():
    result = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Game Scores</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            * {
                box-sizing: border-box;
                font-family: Arial, sans-serif;
            }

            body {
                margin: 0;
                min-height: 100vh;
                background: #0b1020;
                color: white;
                padding: 50px 20px;
            }

            .container {
                max-width: 900px;
                margin: auto;
            }

            a {
                color: #aebaff;
                text-decoration: none;
            }

            h1 {
                font-size: 42px;
                margin-bottom: 10px;
            }

            .subtitle {
                color: #8992ad;
                margin-bottom: 30px;
            }

            .card {
                background: rgba(255,255,255,0.07);
                border: 1px solid rgba(255,255,255,0.1);
                border-radius: 18px;
                padding: 22px;
                margin: 15px 0;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .player {
                font-size: 20px;
                font-weight: bold;
            }

            .game {
                color: #929bb5;
                margin-top: 6px;
            }

            .score {
                font-size: 30px;
                font-weight: bold;
                color: #aab8ff;
            }

            .back {
                display: inline-block;
                margin-bottom: 35px;
            }
        </style>
    </head>

    <body>
        <div class="container">

            <a class="back" href="/">← Back to Home</a>

            <h1>🎯 Game Scores</h1>
            <p class="subtitle">Latest recorded player scores</p>
    """

    for score in scores:
        result += f"""
            <div class="card">
                <div>
                    <div class="player">{score['player']}</div>
                    <div class="game">🎮 {score['game']}</div>
                </div>

                <div class="score">{score['score']}</div>
            </div>
        """

    result += """
        </div>
    </body>
    </html>
    """

    return result


@app.route("/leaderboard")
def leaderboard():
    sorted_scores = sorted(scores, key=lambda x: x["score"], reverse=True)

    result = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Leaderboard</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            * {
                box-sizing: border-box;
                font-family: Arial, sans-serif;
            }

            body {
                margin: 0;
                min-height: 100vh;
                background: #0b1020;
                color: white;
                padding: 50px 20px;
            }

            .container {
                max-width: 800px;
                margin: auto;
            }

            a {
                color: #aebaff;
                text-decoration: none;
            }

            h1 {
                font-size: 42px;
                margin-bottom: 10px;
            }

            .subtitle {
                color: #8992ad;
                margin-bottom: 35px;
            }

            .rank {
                display: flex;
                align-items: center;
                gap: 20px;
                padding: 22px;
                margin: 14px 0;
                border-radius: 18px;
                background: rgba(255,255,255,0.07);
                border: 1px solid rgba(255,255,255,0.1);
            }

            .number {
                width: 48px;
                height: 48px;
                display: flex;
                align-items: center;
                justify-content: center;
                border-radius: 50%;
                background: rgba(255,255,255,0.1);
                font-weight: bold;
                font-size: 18px;
            }

            .player {
                flex: 1;
                font-size: 19px;
                font-weight: bold;
            }

            .game {
                color: #858ea9;
                font-size: 13px;
                margin-top: 5px;
            }

            .points {
                font-size: 25px;
                font-weight: bold;
                color: #aab8ff;
            }

            .back {
                display: inline-block;
                margin-bottom: 35px;
            }
        </style>
    </head>

    <body>
        <div class="container">

            <a class="back" href="/">← Back to Home</a>

            <h1>🏆 Leaderboard</h1>
            <p class="subtitle">Top players ranked by score</p>
    """

    for position, score in enumerate(sorted_scores, start=1):
        result += f"""
            <div class="rank">
                <div class="number">{position}</div>

                <div class="player">
                    {score['player']}
                    <div class="game">{score['game']}</div>
                </div>

                <div class="points">
                    {score['score']}
                </div>
            </div>
        """

    result += """
        </div>
    </body>
    </html>
    """

    return result


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)