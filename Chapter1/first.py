import survey

'''
Think Stats

Chapter 1

http://greenteapress.com/thinkstats/html/thinkstats002.html

Refactored as knowledge of Python/data sets gets better
'''

class Pregnancies(object):

    # Create lists to store the various pregnancy lists 
    allLiveBirths = []
    allFirstBirths = []
    allSubsequentBirths = []

    def __init__ (self):
	    # initialise the table, and all the lists to contain what they need 
		self.table = survey.Pregnancies()
		self.table.ReadRecords()
		for pregnancy in self.table.records:
		    if pregnancy.outcome == 1:
				self.allLiveBirths.append(pregnancy.prglength)
				if pregnancy.birthord == 1:
					self.allFirstBirths.append(pregnancy.prglength)
				else:
					self.allSubsequentBirths.append(pregnancy.prglength)

    def getNumberOfPregnancies(self):
        '''get the total records in the dataset'''
        return len(self.table.records)

    def getNumberOfLiveBirths(self):
        '''get the live births'''
        return len(self.allLiveBirths)

    def getNumberOfFirstBabies(self):
        '''get the first baby count'''
        return len(self.allFirstBirths)		

    def getTotalLengthofPregnancies(self, listToWorkFrom):
        '''based on a passed in list (listToWorkFrom) calculate the total length of all of the pregnancies'''
        total = 0.0
        for value in listToWorkFrom:
            total += value
        return total
		
    def getAverageLengthOfFirstBirths(self):
        '''get the average length of First Births'''
        totalFirstBirthsInWeeks = self.getTotalLengthofPregnancies(self.allFirstBirths)
        totalNumberOfFirstBirths = self.getNumberOfFirstBabies()
        return totalFirstBirthsInWeeks/totalNumberOfFirstBirths

    def getAverageLengthOfSubsequentBirths(self):
        '''get the average length of subsequent Births'''
        totalSubsequentBirthsInWeeks = self.getTotalLengthofPregnancies(self.allSubsequentBirths)
        totalNumberOfSubsequentBirths = self.getNumberOfLiveBirths() - self.getNumberOfFirstBabies()
        return totalSubsequentBirthsInWeeks/totalNumberOfSubsequentBirths


pregnancies = Pregnancies()
print 'Number of pregnancies', pregnancies.getNumberOfPregnancies()
print 'Number of Live births', pregnancies.getNumberOfLiveBirths()
print 'Number of 1st babies', pregnancies.getNumberOfFirstBabies()
print 'Average first baby pregnancy length', pregnancies.getAverageLengthOfFirstBirths()
print 'Average subsequent baby pregnancy length', pregnancies.getAverageLengthOfSubsequentBirths()
print 'Difference between first baby pregnancy length and subsequent pregnancy length (hours)', (pregnancies.getAverageLengthOfFirstBirths() - pregnancies.getAverageLengthOfSubsequentBirths()) * 7 * 24
