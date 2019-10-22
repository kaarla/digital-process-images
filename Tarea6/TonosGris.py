from PIL import ImageTk, Image


def filtroGris1(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            gris = int(round((r*0.3) + (g*0.59) + (b*0.11)))
            pixels[i,j] = (gris,gris,gris)
    return aplica

def filtroGris2(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()        
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            pixels[i,j] = (r,r,r)
    return aplica


def filtroGris3(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            pixels[i,j] = (g,g,g)
    return aplica


def filtroGris4(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()         
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            pixels[i,j] = (b,b,b)
    return aplica


def filtroGris5(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            gris = int(round((r+g+b)/3))
            pixels[i,j] = (gris,gris,gris)
    return aplica

def filtroGris6(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            gris = int(round((r+g)/2))
            pixels[i,j] = (gris,gris,gris)
    return aplica

def filtroGris7(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            gris = int(round((r+b)/2))
            pixels[i,j] = (gris,gris,gris)
    return aplica
    

def filtroGris8(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            gris = int(round((g+b)/2))
            pixels[i,j] = (gris,gris,gris)
    return aplica
