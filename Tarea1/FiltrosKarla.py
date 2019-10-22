import tkFileDialog
from Tkinter import *
from PIL import ImageTk, Image
import random
import os

class Filtros(Frame):

    #Constructor de la clase
    def __init__(self, parent):

        Frame.__init__(self,parent)
        self.pack(fill=BOTH, expand=True)
        self.creaMenu()
        self.creaCanvas()

    #Funcion para cargar el menun en la ventana
    def creaMenu(self):

        self.menuBar = Menu(self)
        self.archivoMenu = Menu(self.menuBar, tearoff=0)
        self.archivoMenu.add_command(label="Abrir", command=self.escogerImagen)
        self.menuBar.add_cascade(label="Imagen", menu=self.archivoMenu)
        self.filtroMenu = Menu(self.menuBar, tearoff=0)
        self.filtroMenu.add_command(label="Mica rojo", command = self.aplicaFiltroRojo)
        self.filtroMenu.add_command(label="Mica azul", command = self.aplicaFiltroAzul)
        self.filtroMenu.add_command(label="Mica Verde", command = self.aplicaFiltroVerde)
        self.filtroMenu.add_command(label="Escala de grises", command = self.aplicaFiltroGris)
        self.filtroMenu.add_command(label="Azar", command = self.aplicaFiltroRandom)
        self.menuBar.add_cascade(label="Filtros", menu=self.filtroMenu)
        root.config(menu=self.menuBar)


    def creaCanvas(self):

        self.originalVentana = Canvas(self, bg="pink",width=500,height=400)
        self.originalVentana.pack(side=LEFT, fill=BOTH, expand=True)

        self.filtroVentana = Canvas(self,bg ="orange",width=500,height=400 )
        self.filtroVentana.pack(side=RIGHT, fill=BOTH, expand=True)

    #Funcion para colocar las imagenes en las areas para imagenes
    def escogerImagen(self):
        size = 500,500
        self.ruta = tkFileDialog.askopenfilename()
        self.imagen = Image.open(self.ruta)
        self.aplica = Image.open(self.ruta)
        self.imagen.thumbnail(size,Image.ANTIALIAS)
        self.aplica.thumbnail(size,Image.ANTIALIAS)
        self.rgb = self.imagen.convert('RGB')
        self.pixels = self.aplica.load()
        imageFile = ImageTk.PhotoImage(self.imagen)
        imageAplica = ImageTk.PhotoImage(self.aplica)
        self.originalVentana.image = imageFile
        self.originalVentana.create_image(imageFile.width()/2, imageFile.height()/2, anchor=CENTER, image=imageFile, tags="bg_img")
        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")
        self.originalVentana.create_text((250,380),text="Imagen original")
        self.filtroVentana.create_text((250,380),text="Imagen con filtro")

    """ Filtro rojo
    Recorremos cada pixel de la imagen original mientras asignamos a los de la nueva imagen solamen
    te los valores de r (rojo) originales, mientras que  g (verde) y b (azul) quedan en ceros.
    """
    def filtroRojo(self):
        newName = str("red" + str(random.randint(1, 1000)) + ".png")
        newIm = Image.new("RGB", self.imagen.size)
        for i in range(self.imagen.size[0]):
            for j in range(self.imagen.size[1]):
                r,g,b = self.rgb.getpixel((i,j))
                newIm.putpixel((i, j), (r, 0, 0))
                self.pixels[i,j] = (r, 0, 0)
        newIm.save(newName)
        return self.aplica

    #Funcion para llamar al filtro en el menu
    def aplicaFiltroRojo(self):
        imagen = self.filtroRojo()
        imageAplica = ImageTk.PhotoImage(imagen)
        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")

    """ Filtro azul
    Recorremos cada pixel de la imagen original mientras asignamos a los de la nueva imagen solamen
    te los valores de b (azul) originales, mientras que r (rojo)  y g (verde) quedan en ceros.
    """
    def filtroAzul(self):
        newName = str("blue" + str(random.randint(1, 1000)) + ".png")
        newIm = Image.new("RGB", self.imagen.size)
        for i in range(self.imagen.size[0]):
            for j in range(self.imagen.size[1]):
                r,g,b = self.rgb.getpixel((i,j))
                newIm.putpixel((i, j), (0, 0, b))
                self.pixels[i,j] = (0,0,b)
        newIm.save(newName)
        return self.aplica

    #Funcion para llamar al filtro en el menu
    def aplicaFiltroAzul(self):
        imagen = self.filtroAzul()
        imageAplica = ImageTk.PhotoImage(imagen)
        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")

    """ Filtro verde
    Recorremos cada pixel de la imagen original mientras asignamos a los de la nueva imagen solamen
    te los valores de g (verde) originales, mientras que r (rojo)  y b (azul) quedan en ceros.
    """
    def filtroVerde(self):
        newName = str("green" + str(random.randint(1, 1000)) + ".png")
        newIm = Image.new("RGB", self.imagen.size)
        for i in range(self.imagen.size[0]):
            for j in range(self.imagen.size[1]):
                r,g,b = self.rgb.getpixel((i, j))
                newIm.putpixel((i, j), (0, g, 0))
                self.pixels[i,j] = (0, g, 0)
        newIm.save(newName)
        return self.aplica

    #Funcion para llamar al filtro en el menu
    def aplicaFiltroVerde(self):
        imagen = self.filtroVerde()
        imageAplica = ImageTk.PhotoImage(imagen)
        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")

    """ Filtro random
    Recorremos cada pixel de la imagen original mientras asignamos a los de la nueva imagen un valor aleatorio
    calculado con la clase Random.
    """
    def filtroRandom(self):
        newName = str("random" + str(random.randint(1, 1000)) + ".png")
        newIm = Image.new("RGB", self.imagen.size)
        for i in range(self.imagen.size[0]):
            for j in range(self.imagen.size[1]):
                r,g,b = self.rgb.getpixel((i, j))
                newIm.putpixel((i, j), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                self.pixels[i,j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        newIm.save(newName)
        return self.aplica

    #Funcion para llamar al filtro en el menu
    def aplicaFiltroRandom(self):
        imagen = self.filtroRandom()
        imageAplica = ImageTk.PhotoImage(imagen)
        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")

    """
    Filtro Escala de grises
    Recorremos cada pixel de la imagen original y tomamod los valores de rojo, verde y azul
    Calculamos el valor de r, g y b de los nuevos pixeles de acuerdo a la proporcion
     gris = (rojo*0.3) + (verde*0.59) + (azul*0.11)
    Asignamos el valor 'gris' a r, g, y b del nuevo pixel.
    """

    def filtroGris(self):
        newName = str("grayScale" + str(random.randint(1, 1000)) + ".png")
        newIm = Image.new("RGB", self.imagen.size)
        for i in range(self.imagen.size[0]):
            for j in range(self.imagen.size[1]):
                r,g,b = self.rgb.getpixel((i,j))
                gris = int(round((r*0.3) + (g*0.59) + (b*0.11)))
                newIm.putpixel((i, j), (gris, gris, gris))
                self.pixels[i,j] = (gris,gris,gris)
        newIm.save(newName)
        return self.aplica

    #Funcion para llamar al filtro en el menu
    def aplicaFiltroGris(self):
        imagen = self.filtroGris()
        imageAplica = ImageTk.PhotoImage(imagen)
        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")


#Se ejecuta el programa
root = Tk()
root.title("Filter Kar")
root.wm_state("normal")

app = Filtros(root)

root.mainloop()
