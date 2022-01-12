
import argparse

parser = argparse.ArgumentParser(description = "Making a new config file based on an old zed calib file and a new ros calib file.\nThe result will be a new config file in the correct format.")
parser.add_argument("old", type=str, help="Old zed calib file")
parser.add_argument("new", type=str, help="New ros calib file")
parser.add_argument("updated", type=str, help="New updated filename")
args = parser.parse_args()

def readFromFile(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    return lines

def makeNewConfig(newFilename,configuredData):
    with open(newFilename,'w') as f:
        for i in range(len(configuredData)):
            f.write(configuredData[i])

def stringToIntList(string):
    aList = string.split()
    mapObject = map(float, aList)

    return list(mapObject)



def findUpdatedDataLeftCamera(newData):

 cameraMatrixRow1 =  stringToIntList(newData[28])
 cameraMatrixRow2 =  stringToIntList(newData[29])
 fx = cameraMatrixRow1[0]
 cx = cameraMatrixRow1[2]
 fy = cameraMatrixRow2[1]
 cy = cameraMatrixRow2[2]

 distortion = stringToIntList(newData[33])
 k1 = distortion[0]
 k2 = distortion[1]
 p1 = distortion[2]
 p2 = distortion[3]
 k3 = distortion[4]

 return cx,cy,fx,fy,k1,k2,k3,p1,p2




def findUpdatedDataRightCamera(newData):

 cameraMatrixRow1 =  stringToIntList(newData[58])
 cameraMatrixRow2 =  stringToIntList(newData[59])
 fx = cameraMatrixRow1[0]
 cx = cameraMatrixRow1[2]
 fy = cameraMatrixRow2[1]
 cy = cameraMatrixRow2[2]

 distortion = stringToIntList(newData[63])
 k1 = distortion[0]
 k2 = distortion[1]
 p1 = distortion[2]
 p2 = distortion[3]
 k3 = distortion[4]

 return cx,cy,fx,fy,k1,k2,k3,p1,p2



def inputUpdatedDataLeftCamera(newData, oldData):
    paramList = list(findUpdatedDataLeftCamera(newData))
        #Checkinng if VGA
    if (int(newData[20])==672):
        startLine = 35 #Starting element in converted file
        for i in range(len(paramList)):
            dataLine = oldData[startLine+i]
            oldData[startLine+i] = dataLine.replace(dataLine[3:],str(paramList[i])+"\n")
        #Checkinng if HD

    elif (int(newData[20])==1280):
        startLine = 24
        for i in range(len(paramList)):
            dataLine = oldData[startLine+i]
            oldData[startLine+i] = dataLine.replace(dataLine[3:],str(paramList[i])+"\n")

        #Checking if FHD

    elif (int(newData[20])==1920):
        startLine = 13
        for i in range(len(paramList)):
            dataLine = oldData[startLine+i]
            oldData[startLine+i] = dataLine.replace(dataLine[3:],str(paramList[i])+"\n")
        #Checking if 2K

    elif (int(newData[20])==2208):
        startLine = 2
        for i in range(len(paramList)):
            dataLine = oldData[startLine+i]
            oldData[startLine+i] = dataLine.replace(dataLine[3:],str(paramList[i])+"\n")



def inputUpdatedDataRightCamera(newData, oldData):
    paramList = list(findUpdatedDataRightCamera(newData))
        #Checkinng if VGA
    if (int(newData[20])==672):
        startLine = 79 #Starting element in converted file
        for i in range(len(paramList)):
            dataLine = oldData[startLine+i]
            oldData[startLine+i] = dataLine.replace(dataLine[3:],str(paramList[i])+"\n")
        #Checkinng if HD

    elif (int(newData[20])==1280):
        startLine = 68
        for i in range(len(paramList)):
            dataLine = oldData[startLine+i]
            oldData[startLine+i] = dataLine.replace(dataLine[3:],str(paramList[i])+"\n")

        #Checking if FHD

    elif (int(newData[20])==1920):
        startLine = 57
        for i in range(len(paramList)):
            dataLine = oldData[startLine+i]
            oldData[startLine+i] = dataLine.replace(dataLine[3:],str(paramList[i])+"\n")
        #Checking if 2K

    elif (int(newData[20])==2208):
        startLine = 46
        for i in range(len(paramList)):
            dataLine = oldData[startLine+i]
            oldData[startLine+i] = dataLine.replace(dataLine[3:],str(paramList[i])+"\n")

    

def main():

    newData = readFromFile(args.new)
    oldData = readFromFile(args.old)
   
    inputUpdatedDataLeftCamera(newData, oldData)
    inputUpdatedDataRightCamera(newData, oldData)

    makeNewConfig(args.updated,oldData)
    


main()




