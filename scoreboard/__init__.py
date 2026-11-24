"""The fest scoreboard: count votes and rank teams."""


def add_vote(votes: dict, team: str) -> dict:
    """Return a new tally with one more vote for team."""
    if not team or not team.strip():
        raise ValueError("team name is empty")
    tally = dict(votes)
    tally[team] = tally.get(team, 0) + 1
    return tally


def leaderboard(votes: dict) -> list:
    """Teams ordered by votes, most first; ties by name."""
    return sorted(votes.items(), key=lambda item: (-item[1], item[0]))
