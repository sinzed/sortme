import os
import cv2

def saveState(state, entity, eqNumber=""):
    videoFileParts = entity["image"].split(".jpg")
    txtFileName = videoFileParts[0]+".txt"
    open(txtFileName, "w").write(state+","+str(eqNumber))
    entity["text"]=txtFileName
    entity["state"]=state
    entity["eqNumber"]=eqNumber

def getColor(txtFileName):
    dataText = open(txtFileName, "r").read()
    dataSplited = dataText.split(",")
    colorText = dataSplited[0]
    if(len(dataSplited)>1):
        eqNumber = dataSplited[1]
    return  mapColor(colorText)

def loadCircle(img, entity):
    if len(entity['text']) > 2:
        color = getColor(entity["text"])
        # img = cv2.circle(img, color, )
        img = drawCircle(img, color, entity['eqNumber'])
    return img

def mapColor(colorName):
    if(colorName =="y"):
        return  (0, 255, 0)
    elif(colorName == "dontKnow"):
        return (200, 200, 200)
    elif(colorName == "n"):
        return (0, 0, 200)

def getAllEntites():
    allFiles = [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk('./')] for val in sublist]
    allImages = [f for f in allFiles if ".jpg" in f]
    AllEntities = []
    for image in allImages:
        textFileName = getFileTextName(image)
        if(textFileName in allFiles):
            dataText = open(textFileName, "r").read()
            data = dataText.split(",")
            state = data[0]
            eqNumber = ""
            if(len(data)>1):
                eqNumber = data[1]
            else:
                eqNumber = ""


            entity = {
                'image':image,
                'text': textFileName,
                'state': state,
                'eqNumber': eqNumber
                }
            AllEntities.append(entity)
        else:
            entity = {
            'image':image,
            'text': "",
            'state': ""
            }
            AllEntities.append(entity)

    return AllEntities

def exportToCsv():
    csvFile = open("result.csv","w")
    textToWrite = ""
    allEntities = getAllEntites()
    for entity in allEntities:
        txt = open(entity['text'], "r").read()
        textToWrite =textToWrite + entity['image']+","+txt+"\n"
    
    csvFile.write(textToWrite)


def getFileTextName(imageFileName):
    splitedImageFileName = imageFileName.split(".jpg")
    return splitedImageFileName[0]+".txt"

def writeTextToImage(image, text, position):
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = position
    fontScale              = 1
    fontColor              = (0,0,0)
    lineType               = 2
    image = cv2.putText(image, text, 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)
    return image

def drawCircle(img, color, numberOnCircle=""):
    center_coordinates = (220, 150)
    bottomLeftCornerOfText = (190, 170)
    radius = 30
    thickness = 200
    circle = cv2.circle(img, center_coordinates, radius, color, thickness)
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    fontScale              = 3
    fontColor              = (0,0,0)
    lineType               = 2
    image = cv2.putText(circle, numberOnCircle, bottomLeftCornerOfText,
    font, 
    fontScale,
    fontColor,
    lineType)
    return image