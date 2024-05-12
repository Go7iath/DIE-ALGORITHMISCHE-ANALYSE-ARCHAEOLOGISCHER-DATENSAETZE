
from math import tan, atan
import itertools
from itertools import combinations
from angle import *
from shapely import *

#bereich um punkt deklarieren, UMkreis  Minus Minimale distanz 
def getArea(center,minLength, maxLength):
    center = Point(center[0], center[1])
    outerCircle = center.buffer(maxLength)
    innerCircle = center.buffer(minLength)

    area = outerCircle.difference(innerCircle)

    return area

#diesen Bereich durchsuchen
def searchArea(center, list, minLength, maxLength):
    area = getArea(center, minLength, maxLength)
    result = []
    for point in list: 
        pointObj = Point(point[0], point[1])
        if area.contains(pointObj):
            result.append([center, point])

    return result

#Unwichtiger Sortieralgorithmus
'''def findNext(center, points):
    angles = [calcAngle_Points(center, point) for point in points]
    sorted_indices = sorted(range(len(angles)), key=lambda i: angles[i])
    center_index = sorted_indices.index(0)
    next_index = (center_index + 1) % len(points)
    return points[sorted_indices[next_index]]
'''
#prüft Rechtwinkligkeit
def is_perpendicular(line1, line2, maxDegreeVar):
    angle = calcAngle(line1, line2, maxDegreeVar)

    if abs(angle - 90) <= maxDegreeVar:
        
        return True
    
    else:
        return False
    

#wenn beide Segmente senkrecht sind, wird das dritte aus den Beiden anderen gebildet
def findPerpendicular(Segments, maxDegreeVar):
    result = []
    for comb in itertools.combinations(Segments, 2):
        if is_perpendicular(comb[0], comb[1], maxDegreeVar):
            result.append([comb[0], comb[1],[comb[0][1], comb[1][1]]])
    
    return result

'''def findPerpendicular_edge(Segments, maxDegreeVar):
    edges = []
    for comb in itertools.combinations(Segments, 2):
        if is_perpendicular(comb[0], comb[1], maxDegreeVar):
                for i in comb:
                    for e in i:
                        edges.append(e)
                        if edges.count(e) == 2:
                            return e
                
'''
#findet den Punkt mit rechtem Winkel
def findPerpendicular_edge(Segments, maxDegreeVar):
    edges = []
    for comb in itertools.combinations(Segments, 2):
        if is_perpendicular(comb[0], comb[1], maxDegreeVar):
            for segment in comb:
                for point in segment:
                    if point in edges:
                        return point
                    else:
                        edges.append(point)
                
  
    
