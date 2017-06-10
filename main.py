from datetime import datetime
import csv as util
import itertools
# from Tkinter import *

#TODO: case for month changing
#TODO: case for having program run every night
#TODO: case for

#updateValues lambda function

# make into lambda function
def addValue(dictionary):
    key = "key"; value = "value"
    dictionary.update({key: value})

def writeToPortfolio(newdict):
    newlist = [(k,v) for k,v in newdict.iteritems()]
    print newlist
    with open('example.csv', 'wb') as out:
        portfolio = util.writer(out)
        portfolio.writerow(['month',datetime.now().strftime("%B")])
        for row in newlist:
            portfolio.writerow(row)

def get_range(dictionary, begin, end):
    return dict(itertools.islice(dictionary.iteritems(), begin, end + 1))

with open('example.csv', mode='r') as infile:
    reader = util.reader(infile)
    with open('test.csv', mode='w') as outfile:
        mainwriter = util.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}
    print(mydict)

    # here append the updated values

    # calculate sum of all values as monthly total

    newdict = get_range(mydict, 0, len(mydict)-2)
    print(newdict)
    sample = [int(x) for x in newdict.values()]
    print(sample)
    print(sum(sample))

    # write to File
    writeToPortfolio(newdict)