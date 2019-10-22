from PIL import ImageTk, Image
from FiltroMosaico import *
from TonosGris import *

"""
Dada una imagen le aplicamos el filtro mosaico
Por cada pixel generamos una instruccion en html
Se toma el color del pixel y se escribe una letra M en el archivo html que se crea
"""
def letraColor(image,aplica,mosX,mosY,nombre):
    mosaico = filtroMosaico(image,aplica,mosX,mosY)
    ancho = mosaico.size[0]
    alto = mosaico.size[1]
    rgb = mosaico.convert('RGB')
    f = open(nombre + '.html','w')
    for i in range(alto):
        for j in range(ancho):
            r,g,b = rgb.getpixel((j,i))
            f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">M</font>')
        f.write('<br>')
    f.close()

"""
Dada una imagen le aplicamos el filtro mosaico
Luego aplicamos un tono de gris
Por cada pixel generamos una instruccion en html
Se toma el color del pixel y se escribe una letra M en el archivo html que se crea
"""
def letraGris(image,aplica,mosX,mosY,nombre):
    mosaico = filtroMosaico(image,aplica,mosX,mosY)
    gris = filtroGris1(mosaico,aplica)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgb = gris.convert('RGB')
    f = open(nombre + '.html','w')
    for i in range(alto):
        for j in range(ancho):
            r,g,b = rgb.getpixel((j,i))
            f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">M</font>')
        f.write('<br>')
    f.close()

"""
Dada una imagen le aplicamos el filtro mosaico
Luego aplicamos un tono de gris
Por cada pixel generamos una instruccion en html
Se verifica en que rango cae el valor
Dependiendo del rango se coloca un simbolo
"""
def simbolos(image,aplica,mosX,mosY,nombre):
    mosaico = filtroMosaico(image,aplica,mosX,mosY)
    gris = filtroGris1(mosaico,aplica)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgb = gris.convert('RGB')
    f = open(nombre + '.html','w')
    f.write("<PRE>")
    for i in range(alto):
        for j in range(ancho):
            r,g,b = rgb.getpixel((j,i))
            if(r >= 0 and r < 16):
                f.write('<font size="1">M</font>')
            elif(r >= 16 and r < 32):
                f.write('<font size="1">N</font>')
            elif(r >= 32 and r < 48):
                f.write('<font size="1">H</font>')
            elif(r >= 48 and r < 64):
                f.write('<font size="1">#</font>')
            elif(r >= 64 and r < 80):
                f.write('<font size="1">Q</font>')
            elif(r >= 80 and r < 96):
                f.write('<font size="1">U</font>')
            elif(r >= 96 and r < 112):
                f.write('<font size="1">A</font>')
            elif(r >= 112 and r < 128):
                f.write('<font size="1">D</font>')
            elif(r >= 128 and r < 144):
                f.write('<font size="1">O</font>')
            elif(r >= 144 and r < 160):
                f.write('<font size="1">Y</font>')
            elif(r >= 160 and r < 176):
                f.write('<font size="1">2</font>')
            elif(r >= 176 and r < 192):
                f.write('<font size="1">$</font>')
            elif(r >= 192 and r < 208):
                f.write('<font size="1">%</font>')
            elif(r >= 208 and r < 224):
                f.write('<font size="1">+</font>')
            elif(r >= 224 and r < 240):
                f.write('<font size="1">-</font>')
            elif(r >= 240 and r < 256):
                f.write('<font size="1">M</font>')
        f.write('<br>')
    f.close()

"""
Dada una imagen le aplicamos el filtro mosaico
Luego aplicamos un tono de gris
Por cada pixel generamos una instruccion en html
Se toma el color del pixel y se verifica en que rango cae el valor
Dependiendo del rango se coloca un simbolo
"""
def simbolosGris(image,aplica,mosX,mosY,nombre):
    mosaico = filtroMosaico(image,aplica,mosX,mosY)
    gris = filtroGris1(mosaico,aplica)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgb = gris.convert('RGB')
    f = open(nombre + '.html','w')
    f.write("<PRE>")
    for i in range(alto):
        for j in range(ancho):
            r,g,b = rgb.getpixel((j,i))
            if(r >= 0 and r < 16):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">M</font>')
            elif(r >= 16 and r < 32):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">N</font>')
            elif(r >= 32 and r < 48):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">H</font>')
            elif(r >= 48 and r < 64):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">#</font>')
            elif(r >= 64 and r < 80):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">Q</font>')
            elif(r >= 80 and r < 96):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">U</font>')
            elif(r >= 96 and r < 112):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">A</font>')
            elif(r >= 112 and r < 128):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">D</font>')
            elif(r >= 128 and r < 144):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">O</font>')
            elif(r >= 144 and r < 160):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">Y</font>')
            elif(r >= 160 and r < 176):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">2</font>')
            elif(r >= 176 and r < 192):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">$</font>')
            elif(r >= 192 and r < 208):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">%</font>')
            elif(r >= 208 and r < 224):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">+</font>')
            elif(r >= 224 and r < 240):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">-</font>')
            elif(r >= 240 and r < 256):
                f.write('<font size="1" style="color:rgb(0,0,0);">M</font>')
        f.write('<br>')
    f.close()

"""
Dada una imagen le aplicamos el filtro mosaico
Por cada pixel generamos una instruccion en html
Se toma el color del pixel y se verifica en que rango cae el valor
Dependiendo del rango se coloca un simbolo
"""
def simbolosColor(image,aplica,mosX,mosY,nombre):
    mosaico = filtroMosaico(image,aplica,mosX,mosY)
    rgbMos = mosaico.convert('RGB')
    anchoM = mosaico.size[0]
    altoM = mosaico.size[1]
    gris = filtroGris1(mosaico,aplica)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgbGris = gris.convert('RGB')
    f = open(nombre + '.html','w')
    f.write("<PRE>")
    for i in range(alto):
        for j in range(ancho):
            rc,gc,bc = rgbGris.getpixel((j,i))
            r,g,b = rgbMos.getpixel((j,i))
            if(rc >= 0 and rc < 16):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">M</font>')
            elif(rc >= 16 and rc < 32):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">N</font>')
            elif(rc >= 32 and rc < 48):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">H</font>')
            elif(rc >= 48 and rc < 64):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">#</font>')
            elif(rc >= 64 and rc < 80):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">Q</font>')
            elif(rc >= 80 and rc < 96):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">U</font>')
            elif(rc >= 96 and rc < 112):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">A</font>')
            elif(rc >= 112 and rc < 128):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">D</font>')
            elif(rc >= 128 and rc < 144):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">O</font>')
            elif(rc >= 144 and rc < 160):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">Y</font>')
            elif(rc >= 160 and rc < 176):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">2</font>')
            elif(rc >= 176 and rc < 192):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">$</font>')
            elif(rc >= 192 and rc < 208):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">%</font>')
            elif(rc >= 208 and rc < 224):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">+</font>')
            elif(rc >= 224 and rc < 240):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">-</font>')
            elif(rc >= 240 and rc < 256):
                f.write('<font size="1" style="color:rgb(0,0,0);">M</font>')
        f.write('<br>')
    f.close()

"""
Dada una imagen le aplicamos el filtro mosaico
Se da una cadena que va a generar la imagen
Por cada pixel generamos una instruccion en html
Se toma el color del pixel y se verifica en que rango cae el valor
Dependiendo del rango se coloca alguna letra de la cadena dado el contador
"""
def palabra(image,aplica,mosX,mosY,nombre,cadena):
    mosaico = filtroMosaico(image,aplica,mosX,mosY)
    ancho = mosaico.size[0]
    alto = mosaico.size[1]
    contador = 0;
    rgb = mosaico.convert('RGB')
    f = open(nombre + '.html','w')
    f.write("<PRE>")
    for i in range(alto):
        for j in range(ancho):
            r,g,b = rgb.getpixel((j,i))
            if(contador < len(cadena)):
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">'+cadena[contador]+'</font>')
                contador = contador + 1
            else:
                contador = 0
                f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">'+cadena[contador]+'</font>')
                contador = contador + 1
        f.write('<br>')
    f.close()

"""
Dada una imagen le aplicamos el filtro mosaico
Luego aplicamos un tono de gris
Por cada pixel generamos una instruccion en html
Se toma el color del pixel y se verifica en que rango cae el valor
Dependiendo del rango se coloca un naipe
"""
def naipes(image,aplica,mosX,mosY,nombre):
    mosaico = filtroMosaico(image,aplica,mosX,mosY)
    gris = filtroGris1(mosaico,aplica)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgb = gris.convert('RGB')
    f = open(nombre + '.html','w')
    f.write("<PRE><style>@font-face{font-family: 'Playcrds';src: url('dominos-cartas_FILES/Playcrds.TTF') format('truetype');}font{font-family: 'Playcrds'}</style>")
    for i in range(alto):
        for j in range(ancho):
            r,g,b = rgb.getpixel((j,i))
            if(r >= 0 and r < 19):
                f.write('<font size="1">A</font>')
            elif(r >= 19 and r < 38):
                f.write('<font size="1">B</font>')
            elif(r >= 38 and r < 57):
                f.write('<font size="1">C</font>')
            elif(r >= 57 and r < 76):
                f.write('<font size="1">D</font>')
            elif(r >= 76 and r < 95):
                f.write('<font size="1">E</font>')
            elif(r >= 95 and r < 114):
                f.write('<font size="1">F</font>')
            elif(r >= 114 and r < 133):
                f.write('<font size="1">G</font>')
            elif(r >= 133 and r < 152):
                f.write('<font size="1">H</font>')
            elif(r >= 152 and r < 171):
                f.write('<font size="1">I</font>')
            elif(r >= 171 and r < 190):
                f.write('<font size="1">J</font>')
            elif(r >= 190 and r < 209):
                f.write('<font size="1">K</font>')
            elif(r >= 209 and r < 228):
                f.write('<font size="1">L</font>')
            elif(r >= 228 and r < 256):
                f.write('<font size="1">M</font>')
        f.write('<br>')
    f.close()

"""
Dada una imagen le aplicamos el filtro mosaico
Luego aplicamos un tono de gris
Por cada pixel generamos una instruccion en html
Se toma el color del pixel y se verifica en que rango cae el valor
Dependiendo del rango se coloca un domino negro
"""
def dominoN(image,aplica,mosX,mosY,nombre):
    mosaico = filtroMosaico(image,aplica,mosX,mosY)
    gris = filtroGris1(mosaico,aplica)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgb = gris.convert('RGB')
    f = open(nombre + '.html','w')
    f.write("<PRE><style>@font-face{font-family: 'lasvbld_';src: url('dominos-cartas_FILES/lasvbld_.TTF') format('truetype');}font{font-family: 'lasvbld_'}</style>")
    for i in range(alto):
        for j in range(ancho):
            r,g,b = rgb.getpixel((j,i))
            if(r >= 0 and r < 25):
                f.write('<font size="1">0</font>')
            elif(r >= 25 and r < 50):
                f.write('<font size="1">1</font>')
            elif(r >= 50 and r < 75):
                f.write('<font size="1">2</font>')
            elif(r >= 75 and r < 100):
                f.write('<font size="1">3</font>')
            elif(r >= 100 and r < 125):
                f.write('<font size="1">4</font>')
            elif(r >= 125 and r < 150):
                f.write('<font size="1">5</font>')
            elif(r >= 150 and r < 175):
                f.write('<font size="1">6</font>')
            elif(r >= 175 and r < 200):
                f.write('<font size="1">7</font>')
            elif(r >= 200 and r < 225):
                f.write('<font size="1">8</font>')
            elif(r >= 225 and r < 256):
                f.write('<font size="1">9</font>')
        f.write('<br>')
    f.close()

"""
Dada una imagen le aplicamos el filtro mosaico
Luego aplicamos un tono de gris
Por cada pixel generamos una instruccion en html
Se toma el color del pixel y se verifica en que rango cae el valor
Dependiendo del rango se coloca un domino blanco
"""
def dominoB(image,aplica,mosX,mosY,nombre):
    mosaico = filtroMosaico(image,aplica,mosX,mosY)
    gris = filtroGris1(mosaico,aplica)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgb = gris.convert('RGB')
    f = open(nombre + '.html','w')
    f.write("<PRE><style>@font-face{font-family: 'lasvwd__';src: url('dominos-cartas_FILES/lasvwd__.TTF') format('truetype');}font{font-family: 'lasvwd__'}</style>")
    for i in range(alto):
        for j in range(ancho):
            r,g,b = rgb.getpixel((j,i))
            if(r >= 0 and r < 25):
                f.write('<font size="1">0</font>')
            elif(r >= 25 and r < 50):
                f.write('<font size="1">1</font>')
            elif(r >= 50 and r < 75):
                f.write('<font size="1">2</font>')
            elif(r >= 75 and r < 100):
                f.write('<font size="1">3</font>')
            elif(r >= 100 and r < 125):
                f.write('<font size="1">4</font>')
            elif(r >= 125 and r < 150):
                f.write('<font size="1">5</font>')
            elif(r >= 150 and r < 175):
                f.write('<font size="1">6</font>')
            elif(r >= 175 and r < 200):
                f.write('<font size="1">7</font>')
            elif(r >= 200 and r < 225):
                f.write('<font size="1">8</font>')
            elif(r >= 225 and r < 256):
                f.write('<font size="1">9</font>')
        f.write('<br>')
    f.close()
