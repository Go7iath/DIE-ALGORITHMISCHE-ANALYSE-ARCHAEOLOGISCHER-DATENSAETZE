import math
from math import tan, atan
import itertools
from itertools import combinations
import shapely
from shapely.geometry import Point, Polygon
from PIL import Image, ImageDraw, ImageColor
import time
import pandas as pd
import xlsxwriter
from functools import reduce
import operator
from alive_progress import alive_bar
from time import sleep
import multiprocessing
from tqdm import tqdm
import json
import os

from colors import *
from convert import *



my_path = os.path.dirname(__file__)





def draw_triangles(Triangles, beginningRes, outputRes, minLength, maxLength, maxDegreeVar, line_width, outputPath, border):
    ConvertedShape = []
    for tri in Triangles:
        ConvertedShape.append(convertShapes(tri,beginningRes, outputRes, border))

    #draw images
    counter = 0
    im = Image.new('RGBA', (outputRes, outputRes), (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)
    current_color = "red"

    #in segmente unterteileb    
    for tri in ConvertedShape:
        if counter >= len(hex_colors):
            counter = 0
        #farbe wählen
        current_color = hex_colors[counter]
        line1 = tri[0]
        line2 = tri[1]
        line3 = tri[2]
        #linien zeichnen
        for line in tri:
            x1 = line[0][0]
            y1 = line[0][1]
            x2 = line[1][0]
            y2 = line[1][1]

            draw.line((x1, y1, x2, y2), width=line_width, fill= current_color)
        counter += 1
    #sichern des Bildes
    status = 'AllTriangles'
    current_time = time.strftime('%Y%m%d-%H%MS')
    filename = f'{outputPath}\\{status}_{minLength}-{maxLength}_{maxDegreeVar}°{current_time}.png'
    im.save(filename)




def draw_rectangles(Rectangles, beginningRes, outputRes, minLength, maxLength, maxDegreeVar, line_width, outputPath, border):
    Converted_rect = []
    for rect in Rectangles:
        Converted_rect.append(convertRects(rect, beginningRes, outputRes, border))

    #Rechtecke zeichnen
    counter = 0
    im = Image.new('RGBA', (outputRes, outputRes), (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)
    current_color = "red"
        
    #print(Rectangles)
    for rect in Converted_rect:
        if counter >= len(hex_colors):
            counter = 0
        current_color = hex_colors[counter]

        line1 = rect[0]
        line2 = rect[1]
        line3 = rect[2]
        line4 = rect[3]


            

        for line in rect:
            x1 = line[0][0]
            y1 = line[0][1]
            x2 = line[1][0]
            y2 = line[1][1]
             
            draw.line((x1, y1, x2, y2), width = line_width, fill = current_color)
        counter += 1
    #sichern des Bildes
    status = 'AllRectangles'
    current_time = time.strftime('%Y%m%d-%H%MS')
    filename = f'{outputPath}\\{status}_{minLength}-{maxLength}_{maxDegreeVar}°{current_time}.png'
    im.save(filename)

