import cv2
import state
import time

def main():
    allEntities = state.getAllEntites() 
  
    img = cv2.imread(allEntities[0]["image"])
    img = loadCircle(img, allEntities[0])
    index = 0
    cv2.namedWindow ('screen', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty ('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    img = showFileAdress(img, allEntities[0]["image"])
    cv2.imshow ('screen', img)
   


    while True:
        key = cv2.waitKey(1) & 0xFF

        # if the 'ESC' key is pressed, Quit
        if key == 27:
            quit()
        if key == 82:
            print ("up")
        elif key == 84:
            print ("down")
        elif key == 83  or key == 100:
            index = rightPressed(allEntities, index)
        elif key == 81 or key == 97:
            index = leftPressed(allEntities, index)
        elif key == 13:
            index = enterPressed(allEntities, index)      
        elif key == 111:
            index = dontKnowPressed(allEntities, index)
        elif key == 225 or key == 32:
            index = notSamePressed(allEntities, index)
        elif key == 110:
            index = showNextNotSeen(allEntities)
        elif key == 109:
            img = showNextDontKnow(allEntities)
        elif key == 101:
            exportResult(img)
        # 255 is what the console returns when there is no key press...
        elif key != 255:
            print(int(key))

def exportResult(img):
    img = state.writeTextToImage(img, "exporting", (400,200))
    cv2.imshow ('screen', img)
    state.exportToCsv()
    img = state.writeTextToImage(img, "finished result.csv", (400,400))
    cv2.imshow ('screen', img)

def showNextDontKnow(allEntities):
    index = getNextDontKnowIndex(allEntities)
    img = cv2.imread(allEntities[index]["image"])
    img = showFileAdress(img, allEntities[index]["image"])
    img = loadCircle(img, allEntities[index])
    cv2.imshow ('screen', img)
    return img

def showNextNotSeen(allEntities, index):
    nextNotSeenIndex = getNextNotSeenIndex(allEntities)
    if nextNotSeenIndex is not None:
        index = nextNotSeenIndex
        img = cv2.imread(allEntities[index]["image"])
        img = showFileAdress(img, allEntities[index]["image"])
        cv2.imshow ('screen', img)
        index = nextNotSeenIndex
    return index

def notSamePressed(allEntities, index):
    img = cv2.imread(allEntities[index]["image"])
    color = state.mapColor("n")
    img = showCircle(img, color)
    img = showFileAdress(img, allEntities[index]["image"])
    cv2.imshow ('screen', img)
    state.saveState("n",allEntities[index])
    cv2.waitKey(300)
    index = showNextNotSeen(allEntities, index)
    return index

def dontKnowPressed(allEntities, index):
    img = cv2.imread(allEntities[index]["image"])
    color = state.mapColor("dontKnow")
    img = showCircle(img, color)
    img = showFileAdress(img, allEntities[index]["image"])
    cv2.imshow ('screen', img)
    state.saveState("dontKnow",allEntities[index])
    cv2.waitKey(300)
    index = showNextNotSeen(allEntities, index)
    return index

def enterPressed(allEntities, index):
    img = cv2.imread(allEntities[index]["image"])
    color = state.mapColor("y")
    img = showCircle(img, color)
    img = showFileAdress(img, allEntities[index]["image"])
    cv2.imshow ('screen', img)
    state.saveState("y",allEntities[index])
    cv2.waitKey(300)
    index = showNextNotSeen(allEntities, index)
    return index

def leftPressed(allEntities, index):
    if(index>0):
        index = index-1
    img = cv2.imread(allEntities[index]["image"])
    img = loadCircle(img, allEntities[index])
    img = showFileAdress(img, allEntities[index]["image"])
    cv2.imshow ('screen', img)
    return index

def rightPressed(allEntities, index):
    if(index<len(allEntities)-1):
        index = index+1
    img = cv2.imread(allEntities[index]["image"])
    img = showFileAdress(img, allEntities[index]["image"])
    img = loadCircle(img, allEntities[index])
    cv2.imshow ('screen', img)
    return index

def getNextNotSeenIndex(allEntities):
    for idx, entity in enumerate(allEntities):
        if len(entity['text']) < 1:
            return idx

def getNextDontKnowIndex(allEntities):
    for idx, entity in enumerate(allEntities):
        if len(entity['text']) > 1 and entity['state']=="dontKnow":
            return idx
    # return getNextNotSeenIndex(allEntities)

def getFileTextName(imageFileName):
    splitedImageFileName = imageFileName.split(".jpg")
    return splitedImageFileName[0]+".txt"

def loadCircle(img, entity):
    center_coordinates = (220, 150)
    radius = 30
    thickness = 200
    if len(entity['text']) > 2:
        color = state.getColor(entity["text"])
        img = cv2.circle(img, center_coordinates, radius, color, thickness)
    return img


def showCircle(img, color):
    center_coordinates = (220, 150)
    radius = 30
    thickness = 200
    return cv2.circle(img, center_coordinates, radius, color, thickness)

def showFileAdress(image, text):
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (400,30)
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



main()