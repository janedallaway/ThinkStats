import survey

class Pregnancies(object):

	def __init__ (self):
		self.table = survey.Pregnancies()
		self.table.ReadRecords()
	
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
				else: 
					if pregnancy.birthord > 1:
						total += pregnancy.prglength
		return total
		
	def getAverageLengthOfFirstBirths(self):
		totalFirstBirthsInWeeks = self.getTotalLengthofPregnancies(True)
		totalNumberOfFirstBirths = self.getNumberOfFirstBabies()
		return totalFirstBirthsInWeeks/totalNumberOfFirstBirths

	def getAverageLengthOfSubsequentBirths(self):
		totalSubsequentBirthsInWeeks = self.getTotalLengthofPregnancies(False)
		totalNumberOfSubsequentBirths = self.getNumberOfLiveBirths() - self.getNumberOfFirstBabies()
		return totalSubsequentBirthsInWeeks/totalNumberOfSubsequentBirths

pregnancies = Pregnancies()
print 'Number of pregnancies', pregnancies.getNumberOfPregnancies()
print 'Number of Live births', pregnancies.getNumberOfLiveBirths()
print 'Number of 1st babies', pregnancies.getNumberOfFirstBabies()
print 'Average first baby pregnancy length', pregnancies.getAverageLengthOfFirstBirths()
print 'Average subsequent baby pregnancy length', pregnancies.getAverageLengthOfSubsequentBirths()
print 'Difference between first baby pregnancy length and subsequent pregnancy length (hours)', (pregnancies.getAverageLengthOfFirstBirths() - pregnancies.getAverageLengthOfSubsequentBirths()) * 7 * 24