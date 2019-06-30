class GameObject:

    def __init__(self, objName, threshold, imgDirPath):
        self.objName = objName + ".png"
        self.threshold = threshold
        self.imagePath = imgDirPath + self.objName
        self.imageMaskPath = imgDirPath + objName + "_mask.png"

