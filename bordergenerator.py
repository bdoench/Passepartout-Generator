### This script adds a white border to all image files inside the specified folder.

import os
from settings import Settings

class Generator:
    def __init__(self, settings=Settings(), filepath = ""):
        self.setting = settings
        self.filepath
