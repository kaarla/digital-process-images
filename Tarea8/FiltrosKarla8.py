import tkFileDialog
from Tkinter import *
from PIL import ImageTk, Image
import random
import os
import tkMessageBox
from FiltroSepia import *
from Dithering import *

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
        self.filtroMenu.add_command(label="Filtro Sepia", command = self.aplicaSepia)
        self.filtroMenu.add_command(label="Dithering", command = lambda: self.aplicaFiltro())
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


    def aplicaFiltro(self):
        if self.filtroVentana.find_all() != ():
            self.nuevaImagen = dithering(self.imagen,self.aplica)
            imageAplica = ImageTk.PhotoImage(self.nuevaImagen)
            self.filtroVentana.image = imageAplica
            self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

    def aplicaSepia(self):
        if self.filtroVentana.find_all() != ():
            self.top = Toplevel()

            self.label = Label (self.top, text= "Introduce la cantidad de brillo que quieres\nTiene que ser un valor entre 0 y 255.")
            self.label.pack()

            self.entrytext = IntVar()
            Entry(self.top, textvariable=self.entrytext).pack()

            self.buttontext = StringVar()
            self.buttontext.set("Aplica Sepia")
            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.sacaSepia(self.entrytext)).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")


    def sacaSepia(self,valor):

        self.entrytext = valor.get()
        self.nuevaImagen = filtroSepia(self.imagen,self.aplica,self.entrytext)
        imageAplica = ImageTk.PhotoImage(self.nuevaImagen)
        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")
        self.top.destroy()
#Se ejecuta el programa
root = Tk()
root.title("Filter Kar")
root.wm_state("normal")

app = Filtros(root)

root.mainloop()
