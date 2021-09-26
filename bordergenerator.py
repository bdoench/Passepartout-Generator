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

    parser.add_argument("-p", "--path", type = str, default = params.getPath(), help = "Root location containing image files for processing. Default: Working Directory")
    parser.add_argument("-o", "--out", type = str, default = os.getcwd() + "\\converted" , help = "Directory, where processed images are being saved to.")
    parser.add_argument("-r", "--rec", type = bool, default = True , help = "Enable recursive scanning of subfolders.") 
    parser.add_argument("-d", "--depth", type = int, default = 3 , help = "Specifies the max. depth for recursive scanning.") 
    parser.add_argument("-m", "--mode", type = int, default = 1, help = "Switches the mode of operation for image placement inside the frame. [0 : CENTER; 1 : GOLDEN_RATIO; 2 : OPTICAL_CENTER]")
    parser.add_argument("-c", "--color", type = str, default = "white", help = "Specifies the color to be used as the image border.") 
    parser.add_argument("-b", "--border", type = float, default = 0.15, help = "Sets the border width as a fraction of the source dimensions. (values betweeen 0 and 1)")
    parser.add_argument("-f", "--filetypes", type = tuple, default = (".png", ".jpg", ".jpeg", ".tif", ".tiff"), help = "Filetypes listed here will be considered as valid and selected for processing.")
    args = parser.parse_args()
    
    params.setPath(args.path)
    params.setOut(args.out)
    params.setRec(args.rec)
    params.setDepth(args.depth)
    params.setMode(args.mode)
    params.setColor(args.color)
    params.setBorder(args.border)
    params.setFiletypes(args.filetypes)
    
    img_paths = findImages(params.getPath(), params.recursion())

    generator = Generator(params.getOut(), params.getMode(), params.getColorRGB(), params.getBorder(), img_paths)
    generator.start()
   
def findImages(dir, recursive):
    paths = []
    depth = 0
    for path, folders, files in os.walk(dir):

        for file in files:
            if str(file).endswith(params.filetypes):
                paths.append(os.path.join(path, file))

        if params.getDepth() <= depth or not recursive:
            break

        depth = depth + 1
    
    print("Found " + str(len(paths)) + " valid image files!")
    
    return paths

if __name__ == "__main__":
    main()

