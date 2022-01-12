


#Gir alle linjuene i en textfil som en liste med elementer
def readFromFile(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    return lines

def makeNewConfig(newFilename,configuredData):
    with open(newFilename,'w') as f:
        for i in range(len(configuredData)):
            f.write(configuredData[i])

#Må lokalisere relevant data


def stringToIntList(string):
    aList = string.split()
    mapObject = map(float, aList)

    return list(mapObject)


#print(int_list)

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

"""
s = "cx=951.469"
print(s[3:])

a = s[3:]
print(s.replace(s[3:],"1"))

"""


"""
def inputUpdatedDataLeftCamera(newData, oldData):
    fx,fy,cx,cy,k1,k2,k3,p1,p2 = findUpdatedDataLeftCamera(newData)
     #Checkinng if VGA
    if (int(newData[20])==672):
      cxLine = oldData[35]
      oldData[35] = cxLine.replace(cxLine[3:],str(cx))

      cyLine = oldData[36]
      oldData[36] = cyLine.replace(cyLine[3:],str(cy))

      fxLine = oldData[37]
      oldData[37] = fxLine.replace(fxLine[3:],str(fx))

      fyLine = oldData[38]
      oldData[38] = fyLine.replace(fyLine[3:],str(fy))

      k1Line = oldData[39]
      oldData[39] = k1Line.replace(k1Line[3:],str(k1))

      k2Line = oldData[40]
      oldData[40] = k2Line.replace(k2Line[3:],str(k2))

      k3Line = oldData[41]
      oldData[41] = k3Line.replace(k3Line[3:],str(k3))

      p1Line = oldData[42]
      oldData[42] = p1Line.replace(p1Line[3:],str(p1))

      p2Line = oldData[43]
      oldData[43] = p2Line.replace(p2Line[3:],str(p2))
"""


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


    newData = readFromFile("NewData.txt")
    oldData = readFromFile("OldData.txt")

    print(oldData)
   
    inputUpdatedDataLeftCamera(newData, oldData)
    inputUpdatedDataRightCamera(newData, oldData)
    print(" ")
    print(oldData)

 

    makeNewConfig("newConfig.txt",oldData)


main()




