import os
import sys
import time
g = 9.8

def printLocalTime():
        localTime = time.asctime(time.localtime(time.time()))
        print "\t\t\t\t", localTime

#read dynamic acceleration data from file
def readData(fileName):
	print "Data reading begins"
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
	print "Data reading finishes"
	printLocalTime()
	return rawData

#calculate the velocity
def velocityCalculation(dAcc, fileName):
	dataType = "Velocity"
	print "Velocity calculation starts"
	printLocalTime()
	velocity = []
	vX = 0
	vY = 0
	vZ = 0
	t = 0
	for dataSet in dAcc:
		vX += dataSet[0] * g * 0.025
		vY += dataSet[1] * g * 0.025
		vZ += dataSet[2] * g * 0.025
		t = dataSet[3]
		
		velocity.append([vX, vY, vZ, t])
	
	#print velocity[1:100]
	print "Velocity calculation finishes"
	printLocalTime()
	exportToFile(fileName, dataType, velocity)
	return velocity

#calculate the distance
def distCalculation(velocity, fileName):
	dataType = "Dist"
	print "Distance calculation starts"
	printLocalTime()
	dist = []
	dX = 0
	dY = 0
	dZ = 0
	t = 0
	for dataSet in velocity:
		dX += dataSet[0] * 0.025
		dY += dataSet[1] * 0.025
		dZ += dataSet[2] * 0.025
		t = dataSet[3]
		
		dist.append([dX, dY, dZ, t])
	
	#print dist[1:100]
	print "Distance calculation finishes"
	printLocalTime()
	exportToFile(fileName, dataType, dist)
	return velocity

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
	print dataType + "exported finishes."
	printLocalTime()

if __name__ == "__main__":
        startTime = time.time()
	fileName = ""
	for file in os.listdir("."):
		if "_dAcc.dat" in str(file):
			fileName = str(file)
	dAcc = readData(fileName)
	velocity = velocityCalculation(dAcc, fileName)
	dist = distCalculation(velocity, fileName)
	finishTime = time.time()
        print "total time duration:\t", finishTime - startTime

	sys.exit(0)
	
