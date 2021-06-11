import cv2
import numpy as np
from PIL import Image
import os


allFiles = [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk('./')] for val in sublist]
allFiles = [f for f in allFiles if ".jpg" in f]
print(allFiles)

img = cv2.imread(allFiles[0])

cv2.namedWindow ('screen', cv2.WINDOW_NORMAL)
cv2.setWindowProperty ('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow ('screen', img)
index=0
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
        index = index+1
        img = cv2.imread(allFiles[index])
        cv2.imshow ('screen', img)
        print ("left")
    elif key == 83:
        index=index-1
        img = cv2.imread(allFiles[index])
        cv2.imshow ('screen', img)
        print ("right")
    elif key == 13:
        img = cv2.imread(allFiles[index])
        center_coordinates = (220, 150)
        radius = 100
        color = (0, 255, 0)
        thickness = 2
        image = cv2.circle(img, center_coordinates, radius, color, thickness)
        cv2.imshow ('screen', image)

    # 255 is what the console returns when there is no key press...
    elif key != 255:
        print(key)
# print(f'You entered {value}')
# cv2.waitKey (0)
# cv2.destroyAllWindows ()
