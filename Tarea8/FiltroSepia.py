from PIL import ImageTk, Image
from TonosGris import *
import tkMessageBox

def filtroSepia(imagen,aplica,depth):
    gris = filtroGris5(imagen,aplica)
    rgb = gris.convert('RGB')
    pixels = aplica.load()
    ancho = gris.size[0]
    alto = gris.size[1]
    if depth >= 0 and depth <= 255:
        for i in range(ancho):
            for j in range(alto):
                r,g,b = rgb.getpixel((i,j))
                rr = r+(depth*2)
                gg = g+depth
                if (rr <= ((depth*2)-1)):
                    rr = 255
                if (gg <= (depth-1)):
                    gg = 255
                pixels[i,j] = (rr,gg,b)
        return aplica
    else:
        tkMessageBox.showwarning("Error","Escoge un valor valido entre 0 y 255")
        return imagen
                    
            
