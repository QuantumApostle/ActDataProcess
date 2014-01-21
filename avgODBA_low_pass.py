import os
import sys
import time

DAY_LENGTH = 86400
HOUR_LENGTH = 3600
MIN_LENGTH = 60
DATA_POINT_INTERVAL = 0.025
THRESHOLD = 5.0

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

#averaging the ODBA
def averageODBA(ODBA, fileName):
    dataType = "lowPassODBA"
    newODBA = []
    dayODBA = []
    avgRange = 1.0
    avgValue = 0
    sumValue = 0
    avgCount = 0
    totalCount = 0
    timeStamp = 0.0
    day = 1
    for dataset in ODBA:
        avgCount += 1
        totalCount += 1
        sumValue += dataset[0]
        if avgCount == round(avgRange / 2):
            timeStamp = dataset[1]
        if avgCount == avgRange:
            avgValue = sumValue / avgRange
            avgCount = 0
            sumValue = 0
            if avgValue <= THRESHOLD:
                dayODBA.append([avgValue, timeStamp])
                timeStamp = 0
        if totalCount == (DAY_LENGTH / DATA_POINT_INTERVAL):
            totalCount = 0
            newODBA.append(dayODBA)
            dayODBA = []
    
    newODBA.append(dayODBA)

    for singleODBA in newODBA:
        exportToFile(fileName, dataType + "_day" + str(day), singleODBA)
        day += 1

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

