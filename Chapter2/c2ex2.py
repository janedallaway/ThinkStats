import survey
import thinkstats
import math

'''ThinkStats chapter 2 exercise 2
http://greenteapress.com/thinkstats/html/thinkstats003.html 

Built on top of first.py/survey.py'''

class Pregnancies(object):

	def __init__ (self):
		self.table = survey.Pregnancies()
		self.table.ReadRecords()
		self.firstBabyGestation = [] # store the individual lengths
		self.subsequentBabyGestation = [] # store the individual lengths
	
	def getPregnancies(self):
		return self.table.records
		
	def getNumberOfPregnancies(self):
		return len(self.getPregnancies())

	def getNumberOfLiveBirths(self):
		count = 0
		for pregnancy in self.getPregnancies():
			if pregnancy.outcome == 1:
				count += 1
		return count

	def getNumberOfFirstBabies(self):
		count = 0
		for pregnancy in self.getPregnancies():
			if pregnancy.outcome == 1:
				if pregnancy.birthord == 1:
					count += 1
		return count					

	def getTotalLengthofPregnancies(self, firstBabies):
		total = 0.0
		for pregnancy in self.getPregnancies():
			if pregnancy.outcome == 1:
				if firstBabies:
					if pregnancy.birthord == 1:
						total += pregnancy.prglength
						self.firstBabyGestation.append (pregnancy.prglength)
				else: 
					if pregnancy.birthord > 1:
						total += pregnancy.prglength
						self.subsequentBabyGestation.append (pregnancy.prglength)
						
		return total
		
	def getMeanLengthOfFirstBirths(self):
		totalFirstBirthsInWeeks = self.getTotalLengthofPregnancies(True)
		totalNumberOfFirstBirths = self.getNumberOfFirstBabies()
		return totalFirstBirthsInWeeks/totalNumberOfFirstBirths

	def getMeanLengthOfSubsequentBirths(self):
		totalSubsequentBirthsInWeeks = self.getTotalLengthofPregnancies(False)
		totalNumberOfSubsequentBirths = self.getNumberOfLiveBirths() - self.getNumberOfFirstBabies()
		return totalSubsequentBirthsInWeeks/totalNumberOfSubsequentBirths

	def getStandardDeviationOfFirstBirths(self):
	    return math.sqrt(thinkstats.Var(self.firstBabyGestation))

	def getStandardDeviationOfSubsequentBirths(self):
	    return math.sqrt(thinkstats.Var(self.subsequentBabyGestation))

	def getDifferenceMeanLengthsFirstvsSubsequent(self):
	    return (pregnancies.getMeanLengthOfFirstBirths() - pregnancies.getMeanLengthOfSubsequentBirths()) * 7 * 24

	def getDifferenceStdDevFirstvsSubsequent(self):
	    return (pregnancies.getStandardDeviationOfFirstBirths() - pregnancies.getStandardDeviationOfSubsequentBirths()) * 7 * 24
                
pregnancies = Pregnancies()
print 'Number of pregnancies', pregnancies.getNumberOfPregnancies()
print 'Number of Live births', pregnancies.getNumberOfLiveBirths()
print 'Number of 1st babies', pregnancies.getNumberOfFirstBabies()
print 'Total length (based on first method)', pregnancies.getTotalLengthofPregnancies(True) + pregnancies.getTotalLengthofPregnancies(False)
print 'Total length (based on new method)', sum(pregnancies.firstBabyGestation) + sum(pregnancies.subsequentBabyGestation)
print 'Mean first baby pregnancy length', pregnancies.getMeanLengthOfFirstBirths()
print 'Mean subsequent baby pregnancy length', pregnancies.getMeanLengthOfSubsequentBirths()
print 'Difference between first baby pregnancy length mean and subsequent pregnancy length mean (in hours)', pregnancies.getDifferenceMeanLengthsFirstvsSubsequent()
print 'Standard deviation for first babies', pregnancies.getStandardDeviationOfFirstBirths()
print 'Standard deviation for subsequent babies', pregnancies.getStandardDeviationOfSubsequentBirths()
print 'Difference between first baby pregnancy length std dev and subsequent pregnancy length std dev (in hours)', pregnancies.getDifferenceStdDevFirstvsSubsequent()
