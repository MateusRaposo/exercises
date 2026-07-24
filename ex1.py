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