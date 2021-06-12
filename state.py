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

