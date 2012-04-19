import thinkstats
import math

'''ThinkStats chapter 2 exercise 1
http://greenteapress.com/thinkstats/html/thinkstats003.html 

This is a bit of an overkill solution for the exercise, but as I'm using it as an opportunity to learn python it seemed to make sense'''

class Pumpkin():

    def __init__ (self, type, size, number):
        self.type = type
        self.size = size
        self.number = number       

    def getType(self):
        return self.type

    def getSize(self):
        return self.size

    def getNumber(self):
        return self.number                

class Pumpkins():

    def __init__ (self):
        self.pumpkins = [] # store complete pumpkin objects
        self.weightsOnly = [] # store the weights only, one entry per pumpkin
        pass

    def addPumpkin (self, myPumpkin):       
        self.pumpkins.append (myPumpkin)
        for i in range (myPumpkin.getNumber()):
            self.weightsOnly.append (myPumpkin.getSize())
        
    def writePumpkins(self):
        for pumpkin in self.pumpkins:
            print "There are",pumpkin.getNumber()," ",pumpkin.getType()," pumpkins which weigh",pumpkin.getSize(),"pound each"

    def writeWeights(self):
        for weight in self.weightsOnly:
            print weight

    def meanPumpkin(self):
        return thinkstats.Mean(self.weightsOnly)

    def variancePumpkin(self):
        return thinkstats.Var(self.weightsOnly)

    def stdDeviationPumpkin(self):
        return math.sqrt(self.variancePumpkin())                  
            
myPumpkins = Pumpkins()
myPumpkins.addPumpkin(Pumpkin("Decorative",1,3))
myPumpkins.addPumpkin(Pumpkin("Pie",3,2))     
myPumpkins.addPumpkin(Pumpkin("Atlantic Giant",591,1))
print "The mean weight is", myPumpkins.meanPumpkin() # should be 100
print "The variance weight is", myPumpkins.variancePumpkin() 
print "The standard deviation is", myPumpkins.stdDeviationPumpkin()
