class StockImage():

    def __init__(self, imageName, threshold, imgDirPath):
        self.imageName = imageName + ".png"
        self.threshold = threshold
        self.imageMaskName = imageName + "_mask.png"
        self.imagePath = imgDirPath + self.imageName
        self.imageMaskPath = imgDirPath + self.imageMaskName

    def setThreshold(self, threshold):
        self.threshold = threshold