from PIL import ImageTk, Image


"""    
Filtro tono de gris1
Tomamos de cada pixel los valores de rojo, verde y azul
Calculamos la siguiente formula 
gris = (rojo*0.3) + (verde*0.59) + (azul*0.11)
Le ponemos el resultado a cada entrada del pixel
"""
def filtroGris1(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            gris = int(round((r*0.3) + (g*0.59) + (b*0.11)))
            pixels[i,j] = (gris,gris,gris)
    return aplica

"""
Filtro tono de gris2
Todas las entradas toman el valor del rojo de cada pixel
"""
def filtroGris2(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()        
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            pixels[i,j] = (r,r,r)
    return aplica


"""
Filtro tono de gris3
Todas las entradas toman el valor del verde de cada pixel
"""
def filtroGris3(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            pixels[i,j] = (g,g,g)
    return aplica

"""
Filtro tono de gris4
Todas las entradas toman el valor del azul de cada pixel
"""
def filtroGris4(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()         
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            pixels[i,j] = (b,b,b)
    return aplica

"""
Filtro tono de gris5
Se toman los tres valores rgb de cada pixel, se suman y se divide entre tres
El resultado se coloca en cada entreda del pixel
"""
def filtroGris5(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            gris = int(round((r+g+b)/3))
            pixels[i,j] = (gris,gris,gris)
    return aplica
"""
Filtro tono de gris6
Se suman los valores del rojo y verde, se dividen entre 2
El resultado se coloca en cada entrada del rgb de cada pixel
"""
def filtroGris6(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            gris = int(round((r+g)/2))
            pixels[i,j] = (gris,gris,gris)
    return aplica

"""            
Filtro tono de gris7
Se suman los valores del rojo y azul, se dividen entre 2
El resultado se coloca en cada entrada del rgb de cada pixel
"""
def filtroGris7(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            gris = int(round((r+b)/2))
            pixels[i,j] = (gris,gris,gris)
    return aplica
    
"""
Filtro tono de gris8
Se suman los valores del verde y azul, se dividen entre 2
El resultado se coloca en cada entrada del rgb de cada pixel
"""
def filtroGris8(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            gris = int(round((g+b)/2))
            pixels[i,j] = (gris,gris,gris)
    return aplica
