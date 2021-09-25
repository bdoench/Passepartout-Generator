import os
from PIL import Image, ImageOps

class IOHandler:
    def __init__(self, path, filelist = []):
        self.path = path
        self.filelist = filelist

    def readfiles(self):
        self.filelist = os.listdir(self.path)

    def saveImage(self, img, path):
        pass