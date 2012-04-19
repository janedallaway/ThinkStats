import Pmf
import math

'''
Think Stats

Chapter 2 - Exercise 5

http://greenteapress.com/thinkstats/html/thinkstats003.html'''

def PmfMean(pmf):

    '''
    mu is equal to the sum of all the P(i)X(i) values
    '''

    mu = 0.0
    for item in pmf.Items():
        mu += item[0] * item[1]

    return mu

def PmfVariance(pmf):
    '''
    variance is equal to the sum of all the P(i) * (X(i) - mu) squared
    '''
    
    mu = PmfMean(pmf)

    var = 0.0
    for item in pmf.Items():

        var += item[1] * math.pow((item[0] - mu),2)

    return var


#make a list
pmf = Pmf.MakePmfFromList([1, 1, 1, 2, 2, 2, 2, 3, 4, 5, 5])        
#call the pre-created functions
meanviafn = pmf.Mean()
varianceviafn = pmf.Var()
#call my new functions
meanviathisfn = PmfMean(pmf)
varianceviathisfn = PmfVariance(pmf)

#Print out the answers
print "The PMF class says the mean is",meanviafn,"whereas my fn says",meanviathisfn
print "The PMF class says the variance is",varianceviafn,"whereas my fn says",varianceviathisfn

#Do they match?
if meanviafn == meanviathisfn and varianceviafn == varianceviathisfn:
    print "Yay! They match!"
