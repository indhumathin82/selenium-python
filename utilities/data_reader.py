import csv
def readCSV(filename):
    allrows = []
    datafile = open(filename, 'r')
    myreader = csv.reader(datafile)
    # next(myreader)
    for row in myreader:
        allrows.append(row)
    return allrows