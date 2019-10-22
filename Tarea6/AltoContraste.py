from PIL import ImageTk, Image
from TonosGris import *


def filtroAltoContraste(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            prom = (r+g+b)/3
            if prom >= 128:
                prom  = 255
            elif prom < 128:
                prom = 0
            pixels[i,j] = (prom,prom,prom)
    return aplica

def filtroInverso(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            prom = (r+g+b)/3
            if prom < 128:
                prom  = 255
            elif prom >= 128:
                prom = 0
            pixels[i,j] = (prom,prom,prom)
    return aplica
