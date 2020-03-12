import math


def score(x, y):
    z = (math.sqrt(((x - 0) ** 2) + (y - 0) ** 2))
    if z <= 1:
        return 10
    if z <= 5:
        return 5
    if z <= 10:
        return 1
    else:
        return 0
