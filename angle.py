import math
from math import tan, atan
from slope import *

#maxDegreeVar = 10 #intervall arround 90° 
#maxSlopeVariation = tan(maxDegreeVar)


#einfache Winkelberechnung (für Punktesuche)
def calcAngle_Points(PointA, PointB):

    dx = PointB[0] - PointA[0]
    dy = PointB[1] - PointA[1]
    return math.atan2(dy, dx)


#skalarprodukt berechnen
def skalar(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vektoren müssen gleichlang sein...")
    
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    
    return result

#vektorlänge berechnen
def sumofVector(vector):
    sum = 0
    for i in vector:
        sum += i * i

    return sum ** 0.5

def calcAngle(line1, line2, maxDegreeVar):
    #line1 und line2 sind tupel zweier punkte
    #gemeinsamen Punkt bestimmen
    for point in line1:
        if point in line2:
            common_point = point
            break
    
    #die anderen zwei äußeren Punkte bestimmen
    other_point_line1 = [point for point in line1 if point != common_point][0]
    other_point_line2 = [point for point in line2 if point != common_point][0]
    
    #vektoren berechnen    
    vector_AB = [other_point_line1[0] - common_point[0], other_point_line1[1] - common_point[1]]
    vector_AC = [other_point_line2[0] - common_point[0], other_point_line2[1] - common_point[1]]

    #skalarprodukt
    skalarprod_upper = skalar(vector_AB, vector_AC)

    #länge der vektoren berechnen
    length_AB = sumofVector(vector_AB)
    length_AC = sumofVector(vector_AC)

    #winkel berechnen und in grad umwandeln
    quotient = skalarprod_upper / (length_AB * length_AC)
    angle_radians = math.acos(quotient)
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees
