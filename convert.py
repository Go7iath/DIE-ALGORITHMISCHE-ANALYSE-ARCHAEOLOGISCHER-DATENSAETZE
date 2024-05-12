
from math import tan, atan
from itertools import combinations
import time
import os
from importing import *
#Output Properties

#Methoden zum konvertieren der Segmente und Punkte zu PIL freundlichen Angaben und skalieren der Größe auf ein Ausgabefeld

def convertLines(List, beginningRes, outputRes, border):
    pointA, pointB = List
    pointA = [(pointA[0]/beginningRes) * outputRes * border, (pointA[1]/beginningRes) * outputRes * border]
    pointB = [(pointB[0] / beginningRes) * outputRes * border, (pointB[1] / beginningRes) * outputRes * border]

    return [pointA, pointB]

def convertShapes(tri, beginningRes, outputRes, border):

    line1 = tri[0]
    line2 = tri[1]
    line3 = tri[2]

    converted = [convertLines(line1, beginningRes, outputRes, border), convertLines(line2, beginningRes, outputRes, border), convertLines(line3, beginningRes, outputRes, border)]

    return converted

def convertRects(rect, beginningRes, outputRes, border):

    line1 = rect[0]
    line2 = rect[1]
    line3 = rect[2]
    line4 = rect[3]

    converted = [convertLines(line1, beginningRes, outputRes, border), convertLines(line2, beginningRes, outputRes, border), convertLines(line3, beginningRes, outputRes, border), convertLines(line4, beginningRes, outputRes, border)]

    return converted

def convertPoint(point, beginningRes, outputRes, border):
    point = [(point[0]/beginningRes) * outputRes * border, (point[1]/beginningRes) * outputRes * border]

    return point