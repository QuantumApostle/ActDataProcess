import os
import sys
import time

#print local time
def printLocalTime():
	localTime = time.asctime(time.localtime(time.time()))
	print "\t\t\t\t", localTime


#read dynamic acceleration data from file
def readData(fileName):
	print "Data reading begins."
	printLocalTime()
	dataFile = open(fileName, "r")
	rawData = []
	lines = dataFile.readlines()

	for line in lines:
		dataLine = line.split()
		dataSet = []
		for value in dataLine:
			dataSet.append(float(value))
		rawData.append(dataSet)
	print "Data reading finishes."
	printLocalTime()
	return rawData

def averageODBA(ODBA, fileName):
	dataType = "avgODBA"
	newODBA = []
	avgRange = 10.0
	avgValue = 0
	sumValue = 0
	count = 0
	for dataset in ODBA:
		count += 1
#		print "count = ", count
#		print dataset
		sumValue += dataset[0]
		if count == (avgRange / 2):
			timeStamp = dataset[1]
#			print "timeStamp = ", timeStamp
#		print "sumValue", sumValue
		if count == avgRange:
			avgValue = sumValue / avgRange
			count = 0
			sumValue = 0
			newODBA.append([avgValue, timeStamp])
			timeStamp = 0
	
#	for dataset in newODBA:
#		print "newODBA", dataset
	exportToFile(fileName, dataType, newODBA) 
	return newODBA

#export to file
def exportToFile(fileName, dataType, data):
	print dataType + " exported starts."
	printLocalTime()

	newFileName = fileName[:-9] + "_" + dataType + ".dat"
	newFile = open(newFileName, "w")
	for dataSet in data:
		for value in dataSet:
			newFile.write(str(value) + " ")
		newFile.write('\n')
	print dataType + " exported finishes."
	printLocalTime()

if __name__ == "__main__":
	startTime = time.time()
	fileName = ""
	for file in os.listdir("."):
		if "_ODBA.dat" in str(file):
			fileName = str(file)
	ODBA = readData(fileName)
	newODBA = averageODBA(ODBA, fileName)
	finishTime = time.time()
	print "total time duration:\t", finishTime - startTime, "seconds"
	sys.exit(0)

