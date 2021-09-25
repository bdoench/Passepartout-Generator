import math

from PIL import Image

from IOHandler import IOHandler
from mode import Mode

io = IOHandler()

class Generator:
    def __init__(self, out, mode, color, border, img_paths = []):
        self.out = out
        self.mode = mode
        self.color = color
        self.border = border
        self.img_paths = img_paths

    def calculateMargins(self, border, width, height, mode):
        left = right = border * width
        top = bottom = border * height

        if mode == Mode.OPTICAL_CENTER:
            offset = (border * border * height * width) / (2 * border * width + width)
            top = border * height - offset
            bottom = border * height + offset
        elif mode == Mode.GOLDEN_RATIO:
            x = (math.sqrt((width+height)*(width+height)+((4*width*height)/1.618))-width-height)/2
            top = bottom = left = right = x/2

        return top, bottom, left, right
   
    def start(self):
        for i in range(len(self.img_paths)):
            image = io.loadImage(self.img_paths[i])

            top, bottom, left, right = self.calculateMargins(self.border, image.size[0], image.size[1], self.mode)

            width = round(left + image.size[0] + right)
            height = round(top + image.size[1] + bottom)
            
            img = Image.new(image.mode, (width, height), self.color)
            img.paste(image, (round(left), round(top)))
            io.saveImage(img, self.out, "image_" + str(i+1) + ".jpg")          

