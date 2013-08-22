import os
import math

def readData(fileName):
	print "Data reading begins"
	dataFile = open(fileName, "r")
	rawData = []
	lines = dataFile.readlines()
	
	for line in lines:
		dataLine = line.split()
		dataSet = []
		for value in dataLine:
			dataSet.append(float(value))
		rawData.append(dataSet)
	
	print "Data reading finishes"

	return rawData

#calculate static acceleration
#by averaging data in 2 seconds
def staticAcc(rawData, fileName):
	print "Static acceleration calculation starts"
	
	dataType = "sAcc"
	meanRange = 80
	sAcc = []
	sAccX = []
	sAccY = []
	sAccZ = []
	
	for dataSet in rawData:
		sAccX.append(dataSet[0])
		sAccY.append(dataSet[1])
		sAccZ.append(dataSet[2])
	
	for i in range(len(rawData) - meanRange):
		meanX = sum(sAccX[i: i + meanRange]) / meanRange
		meanY = sum(sAccY[i: i + meanRange]) / meanRange
		meanZ = sum(sAccZ[i: i + meanRange]) / meanRange
		timeStamp = rawData[i][3]
		sAcc.append([meanX, meanY, meanZ, timeStamp])
	
	print "Static acceleration calculation finishes"
	exportToFile(fileName, dataType, sAcc)
	
	return sAcc
	
#calculate dynamic acceleration
#by calculate the absolute value
#of difference between rawData and static Acc
def dynamicAcc(rawData, staticAcc, fileName):
	print "Dynamic acceleration calculation starts"
	dAcc = []
	dataType = "dAcc"
	for i in range(len(staticAcc)):
		dAccX = rawData[i][0] - staticAcc[i][0]
		dAccY = rawData[i][1] - staticAcc[i][1]
		dAccZ = rawData[i][2] - staticAcc[i][2]
		dAcc.append([dAccX, dAccY, dAccZ, staticAcc[i][3]])
	
	print "Dynamic acceleration calculation finishes"
	exportToFile(fileName, dataType, dAcc)

	return dAcc	

#export data to file
def exportToFile(fileName, dataType, data):
	print dataType + " exported starts."
	
	newFileName = fileName[:-4] + "_" + dataType + ".dat"
	newFile = open(newFileName, "w")

	for dataSet in data:
		for value in dataSet:
			newFile.write(str(value) + " ")
		newFile.write('\n')
	print dataType + " exported finishes."
	 
if __name__ == "__main__":
	fileName = ""
	for file in os.listdir("."):
		if "_extracted.dat" in str(file):
			fileName = str(file)
	rawData = readData(fileName)
	sAcc = staticAcc(rawData, fileName)
	dAcc = dynamicAcc(rawData, sAcc, fileName)
