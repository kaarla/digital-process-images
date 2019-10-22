from PIL import ImageTk, Image
from AltoContraste import *
from TonosGris import *

def puntosAcumulados(tam,pix):
    lista = [None] * tam
    n = pix/2
    if(pix % 2 == 0):
        m = n-1
    else:
        m = n
    inicia = (tam/2)-n
    termina = (tam/2)+m
    for i in range(inicia,termina):
        lista[i] = True
    return lista


def filtroAtt(imagen,aplica,tam):
    imgGris = filtroGris1(imagen,aplica)
    imgBN = filtroAltoContraste(imgGris,aplica)
    ancho = imagen.size[0]
    alto = imagen.size[1]
    nuevoAlto = alto - tam
    rgb = imgBN.convert('RGB')
    pixels = aplica.load()
    for i in range(ancho):
        for j in range(0,nuevoAlto,tam):
            negros = 0
            salto = j + tam
            for k in range(j,salto):
                r,g,b = rgb.getpixel((i,k))
                if(r == 0):
                    negros += 1
            lista = puntosAcumulados(tam,negros)
            for k in range(j,salto):
                if(lista[k-j] == True):
                    pixels[i,k] = (0,0,0)
                else:
                    pixels[i,k] = (255,255,255)
    return aplica


