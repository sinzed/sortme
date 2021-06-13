import os
import cv2

def saveState(state, entity):
    videoFileParts = entity["image"].split(".jpg")
    txtFileName = videoFileParts[0]+".txt"
    open(txtFileName, "w").write(state)
    entity["text"]=txtFileName
    entity["state"]=state

def getColor(txtFileName):
    colorText = open(txtFileName, "r").read()
    return  mapColor(colorText)

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
            state = open(textFileName, "r").read()
            entity = {
                'image':image,
                'text': textFileName,
                'state': state
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