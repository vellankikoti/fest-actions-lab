import pytest

from scoreboard import add_vote, leaderboard


def test_first_vote_counts():
    assert add_vote({}, "Orbit") == {"Orbit": 1}


def test_votes_add_up():
    tally = add_vote(add_vote({}, "Orbit"), "Orbit")
    assert tally["Orbit"] == 2


def test_empty_team_rejected():
    with pytest.raises(ValueError):
        add_vote({}, "  ")


def test_leaderboard_order():
    assert leaderboard({"Pulse": 3, "Orbit": 5, "Echo": 3}) == [
        ("Orbit", 5),
        ("Echo", 3),
        ("Pulse", 3),
    ]
