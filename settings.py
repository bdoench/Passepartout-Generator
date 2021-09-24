from colour import Color
from enum import Enum

class Mode(Enum):
    CENTER = 0
    GOLDEN_RATIO = 1 

class Settings:
    def __init__(self, amount = 0, color = Color("white"), margin = (0,0,0,0), mode=Mode.CENTER):
        self.amount = amount
        self.color = color
        self.margin = margin
        self.mode = mode