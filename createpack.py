import numpy as np
import shutil
import errno
from PIL import Image as im
import math
'''these functions are solely for creating the datapacks and sending them'''
concrete = { 'minecraft:yellow_wool': (250.0, 40.0, 199),'minecraft:white_wool': (235.0, 238.0, 237.0),  'minecraft:red_wool': (162.0, 35.0, 39.0),'minecraft:purple_wool': (122.0, 173.0, 42.0),  'minecraft:pink_wool': (239.0, 173.0, 142.0),'minecraft:orange_wool': (242.0, 20.0, 119.0), 'minecraft:magenta_wool': (190.0, 181.0, 69.0),'minecraft:lime_wool': (113.0, 26.0, 186.0),'minecraft:light_gray_wool': (143.0, 135.0, 143.0),'minecraft:light_blue_wool': (58.0, 218.0, 176.0),'minecraft:green_wool': (82,122,45), 'minecraft:gray_wool': (63.0, 72.0, 69.0),'minecraft:cyan_wool': (21.0, 146.0, 138.0), 'minecraft:blue_wool': (53.0, 158.0, 57.0),'minecraft:brown_wool': (115.0, 41.0, 72.0),'minecraft:black_wool': (21.0, 26.0, 21.0),'black_concrete': (8.0, 15.0, 10.0),'blue_concrete': (45.0, 144.0, 47.0),'brown_concrete': (97.0, 32.0, 60.0),'cyan_concrete': (22.0, 137.0, 120.0),'gray_concrete': (55.0, 62.0, 58.0),'green_concrete': (91,135,49),'light_blue_concrete': (36.0, 200.0, 138.0),'light_gray_concrete': (126.0, 115.0, 126.0),'lime_concrete': (94.0, 25.0, 169.0),'magenta_concrete': (170.0, 160.0, 49.0),'orange_concrete': (225.0, 1.0, 98.0),'pink_concrete': (214.0, 143.0, 101.0),'purple_concrete': (101.0, 157.0, 32.0),'red_concrete': (143.0, 33.0, 33.0),'white_concrete': (208.0, 215.0, 214.0),'yellow_concrete': (242.0, 22.0, 176.0),}

#used to match pixel colors tp blocks
def closest_color(rgb,COLORS):  # https://stackoverflow.com/questions/54242194/python-find-the-closest-color-to-a-color-from-giving-list-of-colors
    r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = COLORS[color]
        color_diff = math.sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]
'''creates the datapack to be sent to the client'''


#fills datapack function file with the image data
def create_function(image,pref_width,pref_height,function_path):
    f =  open(function_path,"w")
    img = im.open(image)
    img = img.convert("RGB")
    img = img.resize((pref_width,pref_height),resample=3)
    width = img.width
    height = img.height
    array = np.asarray(img)
    array = array.tolist()
    try:
        for row in array:
            for pixel in row:
                pixel.pop(3)
    except IndexError:
        pass
    with open("create.mcfunction","a") as f:
        for row_index, row in enumerate(array):
            for pixel_index, pixel in enumerate(row):
                f.write("fill" + f" ^{width-pixel_index} ^{height-row_index} ^ ^{width-pixel_index} ^{height-row_index} ^ {closest_color(pixel,concrete)}\n")
def copy_datapack(src,dest):
    try:
        shutil.copytree(src, dest)
    except OSError as err:
 
        # error caused if the source was not a directory
        if err.errno == errno.ENOTDIR:
            shutil.copy2(src, dest)
        else:
            print("Error: % s" % err)

def parse_image(image):
    pass
