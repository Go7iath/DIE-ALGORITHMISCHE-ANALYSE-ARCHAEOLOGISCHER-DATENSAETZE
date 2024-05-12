import math
import itertools
from itertools import combinations
import os

from slope import *
from convert import *
from construct import *
from properties import *
from angle import *
from importing import *




my_path = os.path.dirname(__file__)


Rectangles = []
Converted_rect = []

#initializes functions below


#koordiniert make rectangles, matcht kominationen (alt, unbenutzt)
def search_rects(comb):
        solution = make_rectangles(comb[0], comb[1])
        if solution != "ERROR":
            Rectangles.append(solution)

            #progress_bar.update(1)
#koordiniert make rectangles, matcht kominationen
def calc_rects(Triangles, beginningRes, minLength, maxLength, maxDegreeVar):

    n = len(Triangles)
    r = 2
    fact = math.factorial
    all_combs = int(fact(n)/(fact(r)*fact(n-r)))    #calculate all permutations


    combinations = itertools.combinations(Triangles, 2) #create list




    for comb in combinations:
        solution = make_rectangles(comb[0], comb[1], maxDegreeVar)
        counterx = 0

        if solution != "ERROR":
            Rectangles.append(solution)

    return Rectangles
    
    
