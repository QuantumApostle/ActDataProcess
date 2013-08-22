import os

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

#calculate ODBA
#by sum up the dynamic acceleration
def oDBA(dAcc, fileName):
        dataType = "ODBA"
        print "ODBA calculation starts"
        ODBA = []
        for dataSet in dAcc:
                ODBA.append([abs(dataSet[0]) + abs(dataSet[1]) + abs(dataSet[2]), dataSet[3]])

        print "ODBA calculation finishes"
        exportToFile(fileName, dataType, ODBA)
        return ODBA

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
                if "_dAcc.dat" in str(file):
                        fileName = str(file)
        dAcc = readData(fileName)
        ODBA = oDBA(dAcc, fileName)

