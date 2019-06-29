import cv2
import numpy
import os
import time
import pyautogui
from matplotlib import pyplot
import multiprocessing as mp
import StockImage


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

stockImages = []
imgDirPath = os.getcwd() + "\\StockImages\\"
imgExpPath = os.getcwd() + "\\PostImages\\"

for name in stockImageNames:
    stockImages.append(StockImage(name, 0.80))

print("Number of processors: ", mp.cpu_count())

startTime = int(time.time())
x = 1

while int(time.time()) < startTime + 5:
    screenshotColor = get_color_screenshot()

    for stockImage in stockImages:
        patch = cv2.imread(stockImage.imagePath)
        mask = cv2.imread(stockImage.imageMaskPath)
        c, w, h = patch.shape[::-1]

        res = cv2.matchTemplate(screenshotColor, patch, cv2.TM_CCORR_NORMED, None, stockImage.imageMaskName)
        threshold = 0.9
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screenshotColor, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            print("location identified -> (" + str(pt[0]) + "," + str(pt[1]) + ")")
            r = 3

        cv2.imwrite(imgExpPath + "screenshot_" + str(x) + ".png", screenshotColor)
        print("screenshot captured " + str(x))
        x += 1

print("\n\nProgram terminated")

