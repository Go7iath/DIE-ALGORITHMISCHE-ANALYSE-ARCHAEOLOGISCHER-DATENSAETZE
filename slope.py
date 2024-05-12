import math
from math import tan, atan



#berechnet einfache steigung
def calcSlope(line):
    pointA, pointB = line[0], line[1]
    if pointB[1] == pointA[1]:
        slope = 0
    elif pointB[0] == pointA[0]:
        slope = math.inf
    else:
        slope = (pointB[1] - pointA[1]) / (pointB[0] - pointA[0])

    return slope


