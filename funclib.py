import math


# returns distance between 2 points


def dist(x1y1, x2y2):
    return math.sqrt((x2y2[0] - x1y1[0]) ** 2 + (x2y2[1] - x1y1[1]) ** 2)


