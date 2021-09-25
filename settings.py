import os
from colour import Color

from mode import Mode

class Settings:
    def __init__(self):
        self.path = os.getcwd() + "\\testimages"
        self.out = os.getcwd() + "\\converted"
        self.rec = False
        self.depth = 3
        self.mode = Mode.CENTER
        self.color = Color("white")
        self.border = 0.309
        self.filetypes = (".png", ".jpg", ".jpeg", ".tif", ".tiff")

    def getPath(self):
        return self.path

    def setPath(self, path):
        self.path = path

    def getOut(self):
        return self.out

    def setOut(self, out):
        self.out = out

    def recursion(self):
        return self.rec

    def setRec(self, rec):
        self.rec = rec

    def getDepth(self):
        return self.depth
    
    def setDepth(self, depth):
        self.depth = depth

    def getMode(self):
        return self.mode
    
    def setMode(self, mode):
        if mode == 0:
            self.mode = Mode.CENTER
        elif mode == 1:
            self.mode = Mode.GOLDEN_RATIO
        elif mode == 2:
            self.mode = Mode.OPTICAL_CENTER
        else:
            raise Exception("Unknown value selected: " + str(mode))

    def getColorRGB(self):
        rgb = self.color.rgb
        return (round(rgb[0]*255), round(rgb[1]*255), round(rgb[2]*255))

    def setColor(self, color):
        self.color = Color(color)

    def getBorder(self):
        return self.border

    def setBorder(self, border):
        if 0 <= border <= 1:
            self.border = border
        else:
            raise Exception("Invalid border value: " + str(border))

    def getMode(self):
        return self.mode

    def setMode(self, mode):
        self.mode = mode

    def getFiletypes(self):
        return self.filetypes

    def setFiletypes(self, filetypes):
        self.filetypes = filetypes

    def addFiletype(self, ext):
        self.filetypes + ext

