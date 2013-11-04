import os
import sys
import time
g = 9.8
dt = 0.025

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

#calculate the velocity
def vDCalculation(dAcc, fileName):
	
	print "vd calculation starts."
	printLocalTime()

	velocity = []
	vX = 0
	vY = 0
	vZ = 0
	t = 0

	dist = []
	dX = 0
	dY = 0
	dZ = 0

	for acc in dAcc:
		vX += acc[0] * g * dt
		vY += acc[1] * g * dt
		vZ += acc[2] * g * dt
		dX += vX * dt + 0.5 * acc[0] * dt * dt
		dY += vY * dt + 0.5 * acc[1] * dt * dt
		dZ += vZ * dt + 0.5 * acc[2] * dt * dt
		t = acc[3]
		
		velocity.append([vX, vY, vZ, t])
		dist.append([dX, dY, dZ, t])
	#print velocity[1:100]
	print "vd calculation finishes."
	printLocalTime()
	exportToFile(fileName, "Velocity", velocity)
	exportToFile(fileName, "Dist", dist)

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
                if "_dAcc.dat" in str(file):
                        fileName = str(file)
        dAcc = readData(fileName)
        vDCalculation(dAcc, fileName)
        finishTime = time.time()
        print "total time duration:\t", finishTime - startTime, "seconds"
        sys.exit(0)
	
