#Einen Koordinatenausschnitt betrachten

#checkt ob in der Toleranz
def validation(min_x, min_y, max_x, max_y, x, y):
    if x < min_x or x > max_x:
        return False
    
    if y < min_y or y > max_y:
        return False
    
    return True

#koordiniert das überprüfen
def crop_coordinates(min_x, min_y, max_x, max_y, Points):
    result = []
    for point in Points:
        x = point[0]
        y = point[1]
        if validation(min_x, min_y, max_x, max_y, x, y):
            result.append(point)
    return result

'''
Test_List = [[2, 3], [1, 1], [4, 8], [9, 1], [2, 5]]

print(crop_coordinates(2, 2,5, 9, Test_List))'''