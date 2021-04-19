#Project 3 - CS210
#Author: CJ Busca
#Date: 21103
# Instructor: Gregori

import re
import string

from collections import Counter

#This block opens the file and sorts the items in the list by highest value
def ItemList():
    

    file = open("C:/Users/Ceej/source/repos/Python-CPP/Release/frequency.dat", "r")
    filedata = file.read()
    words=str.split(filedata)
    histogram = {}
    for word in words:
            histogram[word] = histogram.get(word, 0) + 1
            #for word in histogram.keys():
            #print 'Word: %s - count %s' % (word, str(histogram[word]))
    flist = []
    for word, count in histogram.items():
        flist.append([count, word])
    flist.sort()
    flist.reverse()
    for pair in flist:
        print ("%30s: %4d" % (pair[1], pair[0]))

    #This block searches for the typed word in the list
def OccurByWord():
    
    file = open("C:/Users/Ceej/source/repos/Python-CPP/Release/frequency.dat", "r").read()
    item = input("Enter item name: ")
    count = file.count(item)

    print(count)

    #Function for a text-based histogram by percentage of produce purchased out of 104 items, soley based on the item list function above
def HistogramPercentage():
    
    data = open("C:/Users/Ceej/source/repos/Python-CPP/Release/frequency.dat", "r")
    data = data.read()
    c = Counter( data.split() )   # count the words total is 104

    values_list = c.values()
    word_sum = 0

    for v in values_list:
        word_sum += v # get the number of words in the file


    words=str.split(data) #splits strings into an ordered list of substrings and put into an array
    
    histogram = {}
    for word in words:
            
            histogram[word] = histogram.get(word, 0) + 1
    flist = []
    for word, count in histogram.items():
        flist.append([count, word])
    flist.sort()
    flist.reverse()

    percent_dict = {}

    #this code block sorts the key value pairs of the item and percentage and formats it into both tally marks and a percentage to simulate a horizontal bargraph
    for k, v in flist:
        percentage = (100*k)/word_sum
        percent_dict[k] = percentage

        number = int(k)
        quotient = number // 5
        remainder = number % 5
        tallymarks = "||||/   " * quotient + "|" * remainder
            
        print ("{}: {} -- {:.3}%".format (v, tallymarks, percent_dict[k]))
        


#Error and exiting functions

def Error():
    print("\nError! Use numbers 1 through 4!")

def ExitApp():
    print("\nGoodbye.\n")