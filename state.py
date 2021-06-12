import os
def saveState(state, entity):
    videoFileParts = entity["image"].split(".jpg")
    txtFileName = videoFileParts[0]+".txt"
    open(txtFileName, "w").write(state)
    entity["text"]=txtFileName

def getColor(txtFileName):
    colorText = open(txtFileName, "r").read()
    print(colorText)
    return  mapColor(colorText)

def mapColor(colorName):
    if(colorName =="same"):
        return  (0, 255, 0)
    elif(colorName == "dontKnow"):
        return (200, 200, 200)
    elif(colorName == "not"):
        return (0, 0, 200)

def getAllEntites():
    allFiles = [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk('./')] for val in sublist]
    allImages = [f for f in allFiles if ".jpg" in f]
    AllEntities = []
    for image in allImages:
        textFileName = getFileTextName(image)
        if(textFileName in allFiles):
            entity = {
                'image':image,
                'text': textFileName
                }
            AllEntities.append(entity)
        else:
            entity = {
            'image':image,
            'text': ""
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
