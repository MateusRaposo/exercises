# Given two equal length strings representing two players' strategies for a game, return the scores as an array [player1, player2].

# The given strings will only contain one of two letters: "C" (cooperate) or "D" (defect).
# Each character represents one round, scored as follows:
# If both players cooperate, each scores 3.
# If both players defect, each scores 1.
# If one player defects and the other cooperates, the defector scores 5 and the cooperator scores 0.
# Tests:
# Waiting:1. play_game("CCCC", "CCCC") should return [12, 12].
# Waiting:2. play_game("DDDD", "DDDD") should return [4, 4].
# Waiting:3. play_game("CCDD", "CDDD") should return [5, 10].
# Waiting:4. play_game("CCCDCDCCCDDC", "CCDDCDCDDCCD") should return [24, 34].
# Waiting:5. play_game("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC") should return [66, 21].


def play(p1, p2):
    score_p1 = 0
    score_p2 = 0
    for letra in p1, p2:
        if p1 == "c" and p2 == "c":
            score_p1 + 3
            score_p2 + 3
        if p1 == "d" and p2 == "d":
            score_p1 + 1
            score_p2 + 1
        if p1 == "c" and p2 == "d":
            score_p2 + 5
        if p1 == "d" and p2 == "c":
            score_p1 + 5
