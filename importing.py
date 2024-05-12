import pandas


#file_location = "excel\koordinaten.xlsx"
#aus excel importieren
def import_excel(file_location):
    df = pandas.read_excel(file_location)

    Mean_X = list(df.MEAN_X)
    Mean_Y = list(df.MEAN_Y)
    Names = list(df.EntityHand)

    Points = [[a, b] for a, b in zip(Mean_X, Mean_Y)]
    Points0 = Points

    highests = []

    for point in Points:
        highests.append(max(point))
        beginningRes = max(highests)


    return Points,Names, beginningRes

#für entity hand umwanlung zusätzlich importieren   
def import_excel_end(file_location):
    df = pandas.read_excel(file_location)

    Mean_X = list(df.MEAN_X)
    Mean_Y = list(df.MEAN_Y)
    Names = list(df.EntityHand)

    Points = [[a, b] for a, b in zip(Mean_X, Mean_Y)]


    return Points, Names

    