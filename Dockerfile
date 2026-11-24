FROM python:3.12-alpine
WORKDIR /app
COPY scoreboard ./scoreboard
CMD ["python", "-c", "from scoreboard import leaderboard; print(leaderboard({'Orbit': 5, 'Pulse': 3}))"]
