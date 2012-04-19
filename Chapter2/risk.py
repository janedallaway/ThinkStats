import Pmf
import survey

'''
Think Stats

Chapter 2 - Exercise 6

http://greenteapress.com/thinkstats/html/thinkstats003.html'''

def ProbEarly (pmf):
    '''defined as Week 37 and earlier'''
    return ProbRange(pmf, 0, 37)

def ProbOnTime (pmf):    
    '''defined as Weeks 38, 39 or 40'''
    return ProbRange(pmf, 38, 40)

def ProbLate (pmf):
    '''defined as Weeks 41 and beyond'''
    return ProbRange(pmf, 41, 100)

def ProbRange (pmf, lower, upper):
    prob=0.0;
    for x in range(lower, upper+1):
        prob += pmf.Prob(x)
        
    return prob

def RelativeRisk(probThing1,probThing2):
    '''
    Probability of thing 1 / probability of thing 2
    '''
    return probThing1/probThing2

# need to get a pmf for first babies
# need to get a pmf for subsequent babies
# need to get a pmf for all live births

# get the data
table = survey.Pregnancies()
table.ReadRecords()

# prepare empty lists
allLive = [] 
allFirst = []
allSubsequent = []
# get pregancies
for pregnancy in table.records:
    if pregnancy.outcome == 1:
        allLive.append(pregnancy.prglength)
        if pregnancy.birthord == 1:
            allFirst.append(pregnancy.prglength)
        else:
            allSubsequent.append(pregnancy.prglength)

# output counts so we know our lists are right (compare with data in first.py)
print "Total live",len(allLive)
print "Total first",len(allFirst)
print "Total subsequent",len(allSubsequent)

# make the PMFs for the three lists
pmfLive = Pmf.MakePmfFromList(allLive)
pmfFirst = Pmf.MakePmfFromList(allFirst)
pmfSubsequent = Pmf.MakePmfFromList(allSubsequent)

# compute the results
print "Probability first baby born early",ProbEarly(pmfFirst)
print "Probability subsequent baby born early",ProbEarly(pmfSubsequent)
print "Relative Risk",RelativeRisk(ProbEarly(pmfFirst),ProbEarly(pmfSubsequent))
