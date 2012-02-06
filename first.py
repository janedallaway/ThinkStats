import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

count = 0
firstBabyCount = 0
firstBabyWeeks = 0
otherCount = 0
otherWeeks = 0
for row in table.records:
	if row.outcome == 1:
		count = count + 1
		if row.birthord == 1:
			firstBabyCount = firstBabyCount + 1
			firstBabyWeeks = firstBabyWeeks + row.prglength
		else:
			otherCount = otherCount + 1
			otherWeeks = otherWeeks + row.prglength

print 'Number of live births',count
print 'Number of 1st babies',firstBabyCount
avgFirst = float(float(firstBabyWeeks)/float(firstBabyCount))
print 'Average number of weeks for 1st baby',avgFirst
print 'Number of other babies',otherCount
avgOther = float(float(otherWeeks)/otherCount)
print 'Average number of weeks for other baby',avgOther
print 'Difference in hours',(avgFirst - avgOther)*7.0*24
