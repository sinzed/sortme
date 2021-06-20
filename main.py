import cv2
import state
import time
import numpy as np

def main():
    allEntities = state.getAllEntites() 
  
    img = cv2.imread(allEntities[0]["image"])
    img = state.loadCircle(img, allEntities[0])
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
        elif key == 49:
            index = enterPressed(allEntities, index, 1)      
        elif key == 50:
            index = enterPressed(allEntities, index, 2)      
        elif key == 51:
            index = enterPressed(allEntities, index, 3)      
        elif key == 111:
            index = dontKnowPressed(allEntities, index)
        elif key == 225 or key == 32 or key == 48:
            index = notSamePressed(allEntities, index)
        elif key == 110:
            index = showNextNotSeen(allEntities, index)
        elif key == 109:
            img = showNextDontKnow(allEntities)
        elif key == 101:
            exportResult(img)
        # 255 is what the console returns when there is no key press...
        elif key != 255:
            print(int(key))

def exportResult(img):
    img = np.zeros((1200,1200,3), np.uint8)
    img[:,0:1200//2] = (230,200,0)      # (B, G, R)
    img[:,1200//2:1200] = (0,230,200)

    img = state.writeTextToImage(img, "exporting", (200,200))
    cv2.imshow ('screen', img)
    state.exportToCsv()
    img = state.writeTextToImage(img, "finished result.csv", (200,400))
    cv2.imshow ('screen', img)
    cv2.waitKey(2000)
    # exit()

def showNextDontKnow(allEntities):
    index = getNextDontKnowIndex(allEntities)
    img = cv2.imread(allEntities[index]["image"])
    img = showFileAdress(img, allEntities[index]["image"])
    img = state.loadCircle(img, allEntities[index])
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
    img = state.drawCircle(img, color, 0)
    img = showFileAdress(img, allEntities[index]["image"])
    cv2.imshow ('screen', img)
    state.saveState("n",allEntities[index], eqNumber=0)
    cv2.waitKey(300)
    index = showNextNotSeen(allEntities, index)
    return index

def dontKnowPressed(allEntities, index):
    img = cv2.imread(allEntities[index]["image"])
    color = state.mapColor("dontKnow")
    img = state.drawCircle(img, color)
    img = showFileAdress(img, allEntities[index]["image"])
    cv2.imshow ('screen', img)
    state.saveState("dontKnow",allEntities[index])
    cv2.waitKey(300)
    index = showNextNotSeen(allEntities, index)
    return index

def enterPressed(allEntities, index, equalityNumber):
    img = cv2.imread(allEntities[index]["image"])
    color = state.mapColor("y")
    img = state.drawCircle(img, color, str(equalityNumber))
    img = showFileAdress(img, allEntities[index]["image"])
    cv2.imshow ('screen', img)
    state.saveState("y",allEntities[index],equalityNumber)
    cv2.waitKey(300)
    index = showNextNotSeen(allEntities, index)
    return index

def leftPressed(allEntities, index):
    if(index>0):
        index = index-1
    img = cv2.imread(allEntities[index]["image"])
    img = state.loadCircle(img, allEntities[index])
    img = showFileAdress(img, allEntities[index]["image"])
    cv2.imshow ('screen', img)
    return index

def rightPressed(allEntities, index):
    if(index<len(allEntities)-1):
        index = index+1
    img = cv2.imread(allEntities[index]["image"])
    img = showFileAdress(img, allEntities[index]["image"])
    img = state.loadCircle(img, allEntities[index])
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







def showFileAdress(image, text):
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (400,30)
    fontScale              = 1
    fontColor              = (0,0,0)
    lineType               = 2
    image = cv2.putText(image, str(text), 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)
    return image



main()