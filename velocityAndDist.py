import os
import sys
g = 9.8

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

def velocityCalculation(dAcc, fileName):
	dataType = "Velocity"
	print "Velocity calculation starts"
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
	
	exportToFile(fileName, dataType, velocity)
	return velocity

def distCalculation(velocity, fileName):
	dataType = "Dist"
	print "Distance calculation starts"
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
	
	exportToFile(fileName, dataType, dist)
	return velocity

def exportToFile(fileName, dataType, data):
	print dataType + " exported starts."

	newFileName = fileName[:-9] + "_" + dataType + ".dat"
	newFile = open(newFileName, "w")
	for dataSet in data:
		for value in dataSet:
			newFile.write(str(value) + " ")
		newFile.write('\n')
	print dataType + "exported finishes."

if __name__ == "__main__":
	fileName = ""
	for file in os.listdir("."):
		if "_dAcc.dat" in str(file):
			fileName = str(file)
	dAcc = readData(fileName)
	#print dAcc
	velocity = velocityCalculation(dAcc, fileName)
	dist = distCalculation(velocity, fileName)

	sys.exit(0)
	
