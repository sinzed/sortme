def saveState(state, videoFileName):
    videoFileParts = videoFileName.split(".jpg")
    txtFileName = videoFileParts[0]+".txt"
    open(txtFileName, "w").write(state)

def getColor(videoFileName):
    try:
        videoFileParts = videoFileName.split(".jpg")
        txtFileName = videoFileParts[0]+".txt"    
        file = open(txtFileName, "r").read()
        return  mapColor(file)
    except:
        return (256,256,256)

def mapColor(colorName):
    if(colorName =="same"):
        return  (0, 255, 0)
    elif(colorName == "dontKnow"):
        return (200, 200, 200)
    elif(colorName == "not"):
        return (0, 0, 200)

