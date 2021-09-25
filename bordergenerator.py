### This script adds a white border to all image files inside the specified folder.

import argparse
import os

from PIL import ImageOps

from generator import Generator
from IOHandler import IOHandler
from settings import Settings

params = Settings()

def main():
   
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--path", type = str, default = os.getcwd(), help = "Directory containing the image files to be processed")
    parser.add_argument("-m", "--mode", type = int, default = 0, help = "Controls Image placement within border [0 : CENTER; 1 : GOLDEN_RATIO; 2 : OPTICAL_CENTER]")
    args = parser.parse_args()

    img_paths = findImages(args.path)

    print(img_paths)
   
    generator = Generator(params, img_paths)

    generator.start()
   
def findImages(dir):
    paths = []
    for path, folders, files in os.walk(dir):
        for file in files:
            if str(file).endswith(params.filetypes):
                paths.append(os.path.join(path, file))

    return paths

if __name__ == "__main__":
    main()
