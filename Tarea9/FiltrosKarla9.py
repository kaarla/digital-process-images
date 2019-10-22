import tkFileDialog
from Tkinter import *
from PIL import ImageTk, Image
import random
import os
import tkMessageBox
from Esteganografia import *
from Estereograma import *

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
        self.filtroMenu.add_command(label="Cifrar", command=self.aplicaCifrado)
        self.filtroMenu.add_command(label="Descifrar", command= self.obtenDescifrado)
        self.menuBar.add_cascade(label="Esteganografia", menu=self.filtroMenu)
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


    def aplicaFiltro(self,opcion):
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

    def aplicaCifrado(self):
        if self.filtroVentana.find_all() != ():
            self.top = Toplevel()

            self.label = Label (self.top, text= "Introduce el mensaje que quieres ocultar")
            self.label.pack()

            self.entrytext = StringVar()
            Entry(self.top, textvariable=self.entrytext).pack()

            self.label2 = Label (self.top, text = "Introduce el nombre de la nueva imagen que se va a generar")
            self.label2.pack()

            self.nombre = StringVar()
            Entry(self.top,textvariable=self.nombre).pack()

            self.buttontext = StringVar()
            self.buttontext.set("Cifrar mensaje")
            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.sacaCifrado(self.entrytext,self.nombre)).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

    def sacaCifrado(self,valor,nombre):

        self.entrytext = valor.get()
        self.nombre = nombre.get()
        self.nuevaImagen = cifrar(self.imagen,self.entrytext,self.nombre)
        imageAplica = ImageTk.PhotoImage(self.nuevaImagen)
        self.filtroVentana.image = imageAplica
        self.filtroVentana.create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")
        self.top.destroy()

    def obtenDescifrado(self):
        if self.filtroVentana.find_all() != ():
            self.top2 = Toplevel()
            self.label2 = Label(self.top2, text="Puede tardar un poco en descrifrar el mensaje")
            self.label2.pack()
            self.buttontext = StringVar()
            self.buttontext.set("Descifrar mensaje")
            self.button = Button(self.top2, textvariable=self.buttontext, command= self.sacaDescifrado).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

    def sacaDescifrado(self):
        cadena = descifrar(self.imagen)
        self.top = Toplevel()
        self.top.geometry("%dx%d%+d%+d" % (300, 200, 500, 250))
        self.label = Label(self.top, text="El mensaje oculto es " + cadena)
        self.label.pack()
        self.top2.destroy()

#Se ejecuta el programa
root = Tk()
root.title("Filter Kar")
root.wm_state("normal")

app = Filtros(root)

root.mainloop()
