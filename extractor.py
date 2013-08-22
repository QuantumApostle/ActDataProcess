import json
import os

def extractData(fileName):
	
	print "Data Extraction Starts"

	dataFile = open(fileName, "r")
	extractData = []
	lines = dataFile.readlines()
	for line in lines:
		dataLine = line.split() 
		acc = []
		accX = float(dataLine[1])
		accY = float(dataLine[2])
		accZ = float(dataLine[3])
		acc = [accX, accY, accZ]
	
		timeStamp = [float(dataLine[0]) / 40.0]
		
		dataPoint = acc + timeStamp
		extractData.append(dataPoint)
	print "Data Extraction Finishes"
	return extractData

def writeFile(newData, extractedFileName):
	print "Data Export Starts"
	newDataFile = open(extractedFileName, 'w')
	
	for data in newData:
		for value in data:
			newDataFile.write(str(value) + ' ')
		newDataFile.write('\n')
	print "Data Export Finishes"

def writeJsonFile(newData, extractedFileName):
	newJsonDataFile = open(extractedFileName, 'w')
	json.dump(newData, newJsonDataFile)

if __name__ == "__main__":
	dataFileName = ""
	for file in os.listdir('.'):
		if "txt" in str(file):
			dataFileName = str(file)
	extractedFileName = dataFileName[:-4] + "_extracted.dat"
	newData = extractData(dataFileName)
	writeFile(newData, extractedFileName)
#	writeJsonFile(newData, extractedFileName)
