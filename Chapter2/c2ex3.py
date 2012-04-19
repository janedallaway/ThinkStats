import Pmf
from operator import itemgetter

'''ThinkStats chapter 2 exercise 3
http://greenteapress.com/thinkstats/html/thinkstats003.html 

Built to consume pmf.py'''

def ModeV1(theHistogram):
    ''' This was my v1. Having learnt about the sortedlist and itemgetter, I'm going to use my AllModes and take the top item instead'''

    currentHighestCount = 0
    currentMode = 0
    
    for val in theHistogram.Values(): 
        if (hist.Freq(val) > currentHighestCount):
            currentHighestCount = theHistogram.Freq(val)
            currentMode = val

    return currentMode

def AllModesOrdered(histItems, isReversed):
    # sorting information gleaned from http://wiki.python.org/moin/HowTo/Sorting
    # should be called with hist.Items() and a True/False value for ordering of the list
    orderedList = sorted(histItems, key=itemgetter(1),reverse=isReversed) # sorted works on any iterable. itemgetter allows us to target the item of the tuple to sort on, reverse = True basically means in reverse order, default is false
    return orderedList

def ModeV2(theHistogram):
    ''' Updated following learning about stuff for AllModes '''
    allItems =  AllModesOrdered(theHistogram.Items(), True)
    # return the top element as this will be the most frequently used item
    return allItems[0][0] 

hist = Pmf.MakeHistFromList([1, 2, 2, 3, 5, 6, 7, 7, 8, 7, 89, 3, 23, 7, 1, 1, 2, 34])
print "List is", hist.Items()
print "Mode is",ModeV1(hist)    
print "Mode is",ModeV2(hist)    

