import cv2
import numpy
import os
import time
import pyautogui
import multiprocessing as mp
from StockImage import GameObject


def get_greyscale_screenshot():
    image = pyautogui.screenshot(region=(10, 60, 765, 430))
    return cv2.cvtColor(numpy.array(image), cv2.COLOR_BGR2GRAY)


def get_color_screenshot():
    image = pyautogui.screenshot(region=(10, 60, 765, 430))
    return cv2.cvtColor(numpy.array(image), cv2.COLOR_BGR2RGB)


stockImageNames = ["fire_shot",
               "ship_1",
               "striker_1",
               "striker_2",
               "sun_1", "tank_1",
               "tank_2",
               "powerup_1",
               "powerup_2",
               "powerup_3"]

stockImageNames = ["striker_1",
               "striker_2"]

gameObjects = []
projPath = os.getcwd()
imgDirPath = projPath + "\\StockImages\\"
imgExpPath = projPath + "\\PostImages\\"
log = open(projPath + "\\log.txt")

for name in stockImageNames:
    threshold = 0.90

    if name == "ship_1":
        threshold = .95
    elif name == "fire_shot":
        threshold = .91
    elif name == "striker_1" or "striker_2":
        threshold = .97

    gameObjects.append(GameObject(name, threshold, imgDirPath))


print("Number of processors: ", mp.cpu_count())

startTime = int(time.time())
x = 1

while int(time.time()) < startTime + 5:
    screenshotColor = get_color_screenshot()

    for object in gameObjects:
        patch = cv2.imread(object.imagePath)
        mask = cv2.imread(object.imageMaskPath)
        c, w, h = patch.shape[::-1]

        res = cv2.matchTemplate(screenshotColor, patch, cv2.TM_CCORR_NORMED, None, mask)
        loc = numpy.where(res >= object.threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screenshotColor, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            print(object.objName + " identified")
            log.write(object.objName + " identified\n")
            r = 3

        cv2.imwrite(imgExpPath + "screenshot_" + str(x) + ".png", screenshotColor)

    print("screenshot captured " + str(x))
    log.write("screenshot captured " + str(x) + "\n\n")
    x += 1

print("\n\nProgram terminated")

