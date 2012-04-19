import Pmf

'''
Think Stats

Chapter 2 - Exercise 4

http://greenteapress.com/thinkstats/html/thinkstats003.html'''

def RemainingLifetime (pmfOfLifeTimes, age):
    '''Write a function called RemainingLifetime that takes a Pmf of lifetimes and an age, and returns a new Pmf that represents the distribution of remaining lifetimes.'''
    #Not clear what the code should be for end of data values - i.e. age > oldest item in current Pmf - so returning None and a "No data available" message

    newPmf = pmfOfLifeTimes
    for item in pmfOfLifeTimes.Items():
        if item[0] <= age:
            newPmf.Incr(item[0], -item[1]) # negate those which are already older/same age as the current thing, so zero them out           
    
    if newPmf.Total() == 0:
        return None
    else:
        # renormalise remaining items
        newPmf.Normalize()
        return newPmf

pmfForFailureTime = Pmf.MakePmfFromList([1, 1, 1, 2, 2, 2, 2, 3, 4, 5, 5])
currentAge = 3
updatedPmfBasedOnCurrentAge = RemainingLifetime (pmfForFailureTime, currentAge)
if updatedPmfBasedOnCurrentAge == None:
    print "No data available beyond age", currentAge
else:   
    print "Given that your item is already aged",currentAge, "the chances of it getting to"
    for item in updatedPmfBasedOnCurrentAge.Items():
        if updatedPmfBasedOnCurrentAge.Prob(item[0]) > 0:
            print "age",item[0], "are", item[1]

