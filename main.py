import cv2
import numpy as np
from PIL import Image
import os
import state

def main():
    allEntities = getAllEntites() 
  
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
        elif key == 81:
            if(index<len(allEntities)-1):
                index = index+1
            img = cv2.imread(allEntities[index]["image"])
            img = showFileAdress(img, allEntities[index]["image"])
            img = loadCircle(img, allEntities[index])
            cv2.imshow ('screen', img)
            print ("left")
        elif key == 83:
            if(index>0):
                index = index-1
            img = cv2.imread(allEntities[index]["image"])
            img = loadCircle(img, allEntities[index])
            img = showFileAdress(img, allEntities[index]["image"])
            cv2.imshow ('screen', img)
            print ("right")

        elif key == 13:
            img = cv2.imread(allEntities[index]["image"])
            color = state.mapColor("same")
            img = showCircle(img, color)
            img = showFileAdress(img, allEntities[index]["image"])
            cv2.imshow ('screen', img)
            state.saveState("same",allEntities[index])
        elif key == 32:
            img = cv2.imread(allEntities[index]["image"])
            color = state.mapColor("dontKnow")
            img = showCircle(img, color)
            img = showFileAdress(img, allEntities[index]["image"])
            cv2.imshow ('screen', img)
            state.saveState("dontKnow",allEntities[index])

        elif key == 225:
            img = cv2.imread(allEntities[index]["image"])
            color = state.mapColor("not")
            img = showCircle(img, color)
            img = showFileAdress(img, allEntities[index]["image"])
            cv2.imshow ('screen', img)
            state.saveState("not",allEntities[index])

        elif key == 110:
            index = getNextNotSeenIndex(allEntities)
            img = cv2.imread(allEntities[index]["image"])
            img = showFileAdress(img, allEntities[index]["image"])
            cv2.imshow ('screen', img)

        # 255 is what the console returns when there is no key press...
        elif key != 255:
            print(key)
    # print(f'You entered {value}')
    # cv2.waitKey (0)
    # cv2.destroyAllWindows ()
def getNextNotSeenIndex(allEntities):
    # print(allEntities)
    for idx, entity in enumerate(allEntities):
        print(len(entity['text']))
        print(entity['text'], len(entity['text']))
        if len(entity['text']) < 1:
            return idx

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