from PIL import Image, ImageOps

class IOHandler:
    def __init__(self) -> None:
        pass

    def loadImage(self, path):
        return Image.open(path)

    def saveImage(self, img, path, name):
        img.save(path + "\\" + name, "JPEG", quality=95)
        print("Saving: " + name + " -> " + path)

