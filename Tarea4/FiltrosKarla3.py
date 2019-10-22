import tkFileDialog
from Tkinter import *
from PIL import ImageTk, Image
import random
import os
import tkMessageBox
from Tarea3 import *

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
        self.filtroMenu.add_command(label="Colores", command = lambda: self.aplicaLetra(1))
        self.filtroMenu.add_command(label="Gris", command = lambda: self.aplicaLetra(2))
        self.filtroMenu.add_command(label="Simbolos", command = lambda: self.aplicaLetra(8))
        self.filtroMenu.add_command(label="SimbolosGris", command = lambda: self.aplicaLetra(3))
        self.filtroMenu.add_command(label="SimbolosColor", command = lambda: self.aplicaLetra(4))
        self.filtroMenu.add_command(label="Palabra", command = self.aplicaPalabra)
        self.filtroMenu.add_command(label="Naipes", command = lambda: self.aplicaLetra(5))
        self.filtroMenu.add_command(label="Domino Negro", command = lambda: self.aplicaLetra(6))
        self.filtroMenu.add_command(label="Domino Blanco", command = lambda: self.aplicaLetra(7))
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

    """
    Ventana emergente para dar el tamanio del mosaico para el filtro de letras
    """
    def aplicaLetra(self,opcion):
        if self.filtroVentana.find_all() != ():

            self.top = Toplevel()

            self.label = Label (self.top, text= "Introduce el tamanio del mosaico\nDa dos valores positivos para (x,y) ")
            self.label.pack()

            self.entraX = IntVar()
            Entry(self.top, textvariable=self.entraX).pack()

            self.entraY = IntVar()
            Entry(self.top, textvariable=self.entraY).pack()

            self.text = Label (self.top, text="Dar un nombre al archivo html que se va a generar")
            self.text.pack()

            self.nombre = StringVar()
            Entry(self.top, textvariable=self.nombre).pack()

            self.buttontext = StringVar()
            self.buttontext.set("Genera imagen")

            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.obtenLetra(self.entraX,self.entraY,self.nombre,opcion)).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

    """
    Con los valores de la ventana emergente y el nombre
    Se les pasa a alguna funcion de los filtros de letras
    """
    def obtenLetra(self,valorX,valorY,nombreA,opcion):
        self.entraX = valorX.get()
        self.entraY = valorY.get()
        self.nombre = nombreA.get()
        if(opcion == 1):
            letraColor(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 2):
            letraGris(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 3):
            simbolosGris(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 4):
            simbolosColor(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 5):
            naipes(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 6):
            dominoN(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 7):
            dominoB(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        elif(opcion == 8):
            simbolos(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre)
        self.top.destroy()

    """
    Ventana emergente para dar el tamanio del mosaico para el filtro de una cadena
    """
    def aplicaPalabra(self):
        if self.filtroVentana.find_all() != ():

            self.top = Toplevel()

            self.label = Label (self.top, text= "Introduce el tamanio del mosaico\nDa dos valores positivos para (x,y) ")
            self.label.pack()

            self.entraX = IntVar()
            Entry(self.top, textvariable=self.entraX).pack()

            self.entraY = IntVar()
            Entry(self.top, textvariable=self.entraY).pack()

            self.peticion = Label(self.top, text="Da una cadena para el filtro")
            self.peticion.pack()

            self.cadena = StringVar()
            Entry(self.top, textvariable=self.cadena).pack()

            self.text = Label (self.top, text="Dar un nombre al archivo html que se va a generar")
            self.text.pack()

            self.nombre = StringVar()
            Entry(self.top, textvariable=self.nombre).pack()

            self.buttontext = StringVar()
            self.buttontext.set("Genera imagen")

            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.obtenPalabra(self.entraX,self.entraY,self.nombre,self.cadena)).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

    """
    Con los valores de la ventana emergente,el nombre y la cadena
    Se le pasa a la funcion palabra
    """
    def obtenPalabra(self,valorX,valorY,nombreA,cadenaA):
        self.entraX = valorX.get()
        self.entraY = valorY.get()
        self.nombre = nombreA.get()
        self.cadena = cadenaA.get()
        palabra(self.imagen,self.aplica,self.entraX,self.entraY,self.nombre,self.cadena)
        self.top.destroy()

#Se ejecuta el programa
root = Tk()
root.title("Filter Kar")
root.wm_state("normal")

app = Filtros(root)

root.mainloop()
