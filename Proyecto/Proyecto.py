import tkFileDialog
from Tkinter import *
from PIL import ImageTk, Image
import random
import os
import tkMessageBox
from FotoMosaico import *
from FiltroMosaico import *

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
        self.filtroMenu.add_command(label="Genera archivo de imagenes", command= self.generaArchivo)
        self.filtroMenu.add_command(label="Genera imagen", command= self.aplicaFotoMosaico)
        self.menuBar.add_cascade(label="Foto Mosaico", menu=self.filtroMenu)
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

    """
    Funcion que indica que va a tardar el foto mosaico y pide la carpeta de imagenes que se usara
    """
    def aplicaFotoMosaico(self):
        if self.filtroVentana.find_all() != ():
            self.top = Toplevel()

            self.label = Label (self.top, text= "Introduce el tamanio del mosaico\nDa dos valores positivos para (x,y) ")
            self.label.pack()

            self.entraX = IntVar()
            Entry(self.top, textvariable=self.entraX).pack()

            self.entraY = IntVar()
            Entry(self.top, textvariable=self.entraY).pack()

            self.label3 = Label(self.top, text="Introduce el nombre del archivo que contiene la informacion de las imagenes a usar")
            self.label3.pack()

            self.archivo = StringVar()
            Entry(self.top, textvariable=self.archivo).pack()

            self.label4 = Label (self.top, text="Selecciona la carpeta con las imagenes a usar")
            self.label4.pack()

            self.buttontext = StringVar()
            self.buttontext.set("Obten fotomosaico")
            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.sacaFotoMosaico(self.entraX,self.entraY,self.archivo)).pack()

            self.label2 = Label (self.top, text = "Va a tardar en generar el foto mosaico")
            self.label2.pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

    def sacaFotoMosaico(self,valorX,valorY,nombre):
        self.entraX = valorX.get()
        self.entraY = valorY.get()
        self.archivo = nombre.get()
        carpeta = tkFileDialog.askdirectory()
        self.nuevaImagen = filtroFotoMosaico(self.imagen,self.aplica,carpeta,self.entraX,self.entraY,self.archivo)
        imageAplica = ImageTk.PhotoImage(self.nuevaImagen)
        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")
        self.top.destroy()


    def generaArchivo(self):
        if self.filtroVentana.find_all() != ():
            self.top = Toplevel()
            self.label2 = Label(self.top, text="Da un nombre al archivo .txt que se va a generar")
            self.label2.pack()
            self.nombre = StringVar()
            Entry(self.top, textvariable=self.nombre).pack()
            self.label = Label (self.top, text= "Selecciona la carpeta con las imagenes que se usaran para el fotomosaico")
            self.label.pack()
            self.buttontext = StringVar()
            self.buttontext.set("Selecciona carpeta")
            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.generaArchivoImg(self.nombre)).pack()
            self.label3 = Label(self.top, text="Se va a tardar en generar el archivo")
            self.label3.pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")


    def generaArchivoImg(self,archivo):
        self.nombre = archivo.get()
        carpeta = tkFileDialog.askdirectory()
        guardaImagenes(carpeta,self.nombre)
        self.top.destroy()

#Se ejecuta el programa
root = Tk()
root.title("Filter Kar")
root.wm_state("normal")

app = Filtros(root)

root.mainloop()
