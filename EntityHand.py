import json
import pandas as pd
import os
from tkinter import messagebox


my_path = os.path.dirname(__file__)

#excel importierne

def import_excel_end(file_location):
    df = pd.read_excel(file_location)

    Mean_X = list(df.MEAN_X)
    Mean_Y = list(df.MEAN_Y)
    Names = list(df.EntityHand)

    Points = [[a, b] for a, b in zip(Mean_X, Mean_Y)]


    return Points, Names

#zu entity hand umwandeln
def convert_tri_entity(Triangles, list_name, file_location, saver, outputPath, current_time):
    Points, Names = import_excel_end(file_location)
    #print("Len is:", len(Points))

    tempconverted_triangles = []
    #vernestete Struktur der Rechtecke aufdröseln
    for nest0 in Triangles:
        converted_nest0 = []

        for i, nest1 in enumerate(nest0):
            converted_nest1 = []

            for j, item in enumerate(nest1):
                if item in Points:
                    index_names = Points.index(item)
                    converted_nest1.append(Names[index_names])
                else:
                    print("TRI ERROR, ", item, " not found in Points!!!")

            converted_nest0.append(converted_nest1)

        tempconverted_triangles.append(converted_nest0)
    #Speiecherorte und ordnere erstellen
    new_Entity_tri = readable(tempconverted_triangles)
    if not os.path.exists(os.path.join(outputPath, "Triangle_lists")):
        os.makedirs(os.path.join(outputPath, "Triangle_lists"))
    list_name_call = os.path.join(outputPath, "Triangle_lists",f"{list_name}_EntityHand_"f"{current_time}_.json")

    list_to_excel(new_Entity_tri, list_name_call)
    if saver:
        #zusätzlich als Json sichern
        with open(list_name_call, 'w') as MyFile:
            json.dump(new_Entity_tri, MyFile)

    print("File saved!")

#selbiges für Rechtecke
def convert_rects_entity(Rectangles, list_name, file_location, saver, outputPath, current_time):
    Points, Names = import_excel_end(file_location)
    #print("Len is:", len(Points))

    tempconverted_rectangles = []

    for nest0 in Rectangles:
        converted_nest0 = []

        for i, nest1 in enumerate(nest0):
            converted_nest1 = []

            for j, item in enumerate(nest1):
                if list(item) in Points:
                    index_names = Points.index(list(item))
                    converted_nest1.append(Names[index_names])
                else:
                    print("RECT ERROR, ", item, " not found in Points!!!")

            converted_nest0.append(converted_nest1)

        tempconverted_rectangles.append(converted_nest0)
    new_Entity_rect = readable(tempconverted_rectangles)
    if not os.path.exists(os.path.join(outputPath, "Rectangles_lists")):
        os.makedirs(os.path.join(outputPath, "Rectangles_lists"))
    list_name_call = os.path.join(outputPath, "Rectangles_lists",f"{list_name}_EntityHand_"f"{current_time}_.json")
    list_to_excel(new_Entity_rect, list_name_call)
    if saver:
        with open(list_name_call, 'w') as MyFile:
            json.dump(new_Entity_rect, MyFile)

    print("File saved!")


#Punkte aus Segmenten filtern
def readable(Rectangles):
    returner= []
    temp_returner = []
    for rect in Rectangles:
        for segment in rect:
            for name in segment:
                if name not in temp_returner:
                    temp_returner.append(name)
        if temp_returner not in returner:
            returner.append(temp_returner)
        temp_returner = []
    return returner

#liste zu excel wandeln
def list_to_excel(my_list, output_name):
    if len(my_list) == 0:
        return

    output_file = output_name + ".xlsx"
    df = pd.DataFrame(my_list, columns=['Point'] + [f'Point{i+2}' for i in range(len(my_list[0])-1)])

    df.insert(0, 'Index', range(1, len(df) + 1))

    df.to_excel(output_file, index=False)
