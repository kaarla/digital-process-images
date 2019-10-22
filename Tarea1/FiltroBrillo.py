#Image filters module
from PIL import Image
import random
import sys

def bright(w, h, im, num):
    newIm = Image.new("RGB", (w, h))
    for n in range(0, w):
        for m in range(0, h):
            r, g, b = im.getpixel((n, m))
            newIm.putpixel((n, m), (fixRGBValue(r + num), fixRGBValue(g + num), fixRGBValue(b + num)))
    return newIm

def saveImage((im, name)):
    im.save(name)

def fixRGBValue(val):
    if (val > 255):
        return 255
    if (val < 0):
        return 0
    return val

if __name__ == "__main__":
    im = Image.open(sys.argv[1])
    rgb_im = im.convert('RGB')
    w, h = rgb_im.size
    saveImage((bright(w, h, rgb_im, int(sys.argv[2])), (sys.argv[3] + ".png")))
