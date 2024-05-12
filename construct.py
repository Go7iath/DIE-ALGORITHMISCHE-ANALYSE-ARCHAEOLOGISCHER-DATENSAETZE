from shapely.geometry import LineString
import numpy as np
import tqdm

from slope import * 
from angle import * 
from properties import * 

#Dreiecksfunktion (zusammengefasstes Funktionsbündel)
def makeTriangles(list, minLength, maxLength, maxDegreeVar):
    Triangles = []

    for point in list:
        possibleSegments = searchArea(point, list, minLength, maxLength)
        all_reactangulares = findPerpendicular(possibleSegments, maxDegreeVar)
        list.remove(point)
        Triangles.extend(all_reactangulares)

    return Triangles

#Duplizierte Segmente entfernen (wird zurzeit nicht genutzt)
def removeDupes(segments): #code snippet
    unique_segments = set()
    for segment in segments:
        # Convert the segment to a tuple so it can be hashed
        segment_tuple = tuple(map(tuple, segment))
        unique_segments.add(segment_tuple)
    # Convert the set back to a list
    unique_list = [list(segment) for segment in unique_segments]
    return unique_list




#Einzigartige Punkte in Rechteck filtern, für EntityHand Umwandlung (wird nicht genutzt)
def getPoints(rect):
    unique = []
    for line in rect:
        if line[0] not in unique:
            unique.append(line[0])
        if line[1] not in unique:
            unique.append(line[1])

    return unique


#shapely bound function, testet ob Überschneidung
def intersection(line1, line2):
    line1_n = [(x, y) for x, y in line1]
    line2_n = [(x, y) for x, y in line2]
    #print(line1, line2)
    line1 = LineString(line1)
    line2 = LineString(line2)
    return line1.intersects(line2)




def make_rectangles(triangle1, triangle2, maxDegreeVar):
    #sets erstellen  --> listen mit einzigartigen items
    points1 = set()
    segments1 = set()

    #first failsafe to avoid concave rectangles
    edge1 = findPerpendicular_edge(triangle1, maxDegreeVar)
    edge2 = findPerpendicular_edge(triangle2, maxDegreeVar)
    if edge1 == edge2 :
        return "ERROR"
    #extract Points
    for side in triangle1:
        points1.update(map(tuple, side))
        segments1.add(tuple(map(tuple, side)))

    points2 = set()
    segments2 = set()

    for side in triangle2:
        points2.update(map(tuple, side))
        segments2.add(tuple(map(tuple, side)))

    matching_points = points1.intersection(points2)
    matching_segments = segments1.intersection(segments2)


    #check if not overlapping, exactly one matching segment(hypothenuse) and 2 matching points
    if len(matching_points) == 2 and len(matching_segments) == 1:
        '''print("num match. points: ", len(matching_points), "\nnum match.seg.: ", len(matching_segments))
        print("points: ", matching_points, "segs: ", list(matching_segments))'''
        
        #sorts all the rectangle segments, first for the #1 triangle then for #2
        rectangle_segments = []
        for segment in segments1:
            if segment not in matching_segments:
                rectangle_segments.append(list(segment))

        for segment in segments2:
            if segment not in matching_segments:
                rectangle_segments.append(list(segment))
    
    else:
        return "ERROR"

    


    #second failsafe for concave rectangles
    match_seg_list =  np.array(list(matching_segments)).tolist()
    match_seg = match_seg_list[0]

    if len(match_seg) != 2:
        print("noooo", match_seg)
        return "ERROR"

    

    diagonale = [edge1, edge2]
    #diagonalen Intersektions testen
    if intersection(match_seg, diagonale) == False:
        return "ERROR"



    


        
            





        
    return [list(map(list, sublist)) for sublist in rectangle_segments] 


    




