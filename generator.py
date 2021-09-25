import math

from PIL import Image

from mode import Mode
from settings import Settings


class Generator:
    def __init__(self, settings=Settings(), img_paths = []):
        self.settings = settings
        self.img_paths = img_paths

    def calculateMargins(self, border, width, height, mode):
        left = right = border * width
        
        if mode == Mode.CENTER:
            top = bottom = border * height
        elif mode == Mode.OPTICAL_CENTER:
            offset = (border * border * height * width) / (2 * border * width + width)
            top = border * height - offset
            bottom = border * height + offset
        elif mode == Mode.GOLDEN_RATIO:
            x = (math.sqrt((width+height)*(width+height)+((4*width*height)/1.618))-width-height)/2
            top = bottom = left = right = x/2

        return top, bottom, left, right
   

    def start(self):
        for path in self.img_paths:
            image = Image.open(path)
            mode = self.settings.getMode()

            top, bottom, left, right = self.calculateMargins(self.settings.getBorder(), image.size[0], image.size[1], mode)

            
            width = round(left + image.size[0] + right)
            height = round(top + image.size[1] + bottom)
            print(width, height)
            out = Image.new(image.mode,(width, height),self.settings.getColor())
            out.paste(image, (round(left), round(top)))
            out.save("E:\\Programming\\Python\\Passepartout-Generator\\testimages\\converted\\"+str(image.size)+".jpg", "JPEG")
            print("Saving image: " + str(image.size))

