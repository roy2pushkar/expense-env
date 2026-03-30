def easy_task(state):
    score = state["savings"] / 300
    return min(max(score, 0.0), 1.0)


def medium_task(state):
    score = state["savings"] / 700
    return min(max(score, 0.0), 1.0)


def hard_task(state):
    score = state["savings"] / 1200
    return min(max(score, 0.0), 1.0)