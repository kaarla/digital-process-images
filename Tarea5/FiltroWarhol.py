from PIL import ImageTk, Image
import tkMessageBox


def filtroWarhol(imagen,aplica,rojo,verde,azul):
    if ((rojo > 255 or rojo < 0) or (verde > 255 or verde < 0) or (azul > 255 or azul < 0)):
        tkMessageBox.showwarning("Error","Escoge un valores validos entre 0 y 255")
        return aplica
    else:
        rgb = imagen.convert('RGB')
        pixels = aplica.load()
        for i in range(imagen.size[0]):
            for j in range(imagen.size[1]):
                r,g,b = rgb.getpixel((i,j))
                andRojo = (rojo & r)
                andVerde = (verde & g)
                andAzul = (azul & b)
                pixels[i,j] = (andRojo,andVerde,andAzul)
        return aplica
