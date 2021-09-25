from mode import Mode

class Settings:
    def __init__(self, border = 0.1, color = 255, mode = Mode.CENTER, filetypes = (".png", ".jpg", ".jpeg", ".jp2", ".tif", ".tiff")):
        self.border = border
        self.color = color
        self.mode = mode
        self.filetypes = filetypes

    def setBorder(self, border):
        self.border = border

    def getBorder(self):
        return self.border

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setMode(self, mode):
        self.mode = mode

    def getMode(self):
        return self.mode
