import tkFileDialog
from Tkinter import *
from PIL import ImageTk, Image
import random
import os
from Recursiva import *

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
        self.filtroMenu.add_command(label="Recursiva gris", command = lambda: self.aplicaMosaico(2))
        self.filtroMenu.add_command(label="Recursiva color", command = lambda: self.aplicaMosaico(3))
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


 
#    Ventana emergente para dar el tamanio del mosaico para el filtro mosaico

    def aplicaMosaico(self,opcion):
        if self.filtroVentana.find_all() != ():

            self.top = Toplevel()

            self.label = Label (self.top, text= "Introduce el tamanio del mosaico\nDa dos valores positivos para (x,y) ")
            self.label.pack()

            self.entraX = IntVar()
            Entry(self.top, textvariable=self.entraX).pack()

            self.entraY = IntVar()
            Entry(self.top, textvariable=self.entraY).pack()

            self.label2 = Label (self.top, text= "Advertencia, el filtro puede tardar en aplicarse ")
            self.label2.pack()

            self.buttontext = StringVar()
            self.buttontext.set("Aplica mosaico")
            self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.obtenMosaico(self.entraX,self.entraY,opcion)).pack()
        else:
            tkMessageBox.showwarning("Error","Escoge una imagen antes de aplicar un filtro")

   
    def obtenMosaico(self,valorX,valorY,opcion):
        self.entraX = valorX
        self.entraY = valorY
        if(opcion == 1):
            self.nuevaImagen = filtroMosaico(self.imagen,self.aplica,self.entraX,self.entraY)
        elif(opcion == 2):
            generaImagenesGris(self.imagen,self.aplica)
            self.nuevaImagen = aplicaRecursivaGris(self.imagen,self.aplica,self.entraX,self.entraY)
            eliminaImagenesGris()
        elif(opcion == 3):
            self.nuevaImagen = aplicaRecursivaColor(self.imagen,self.aplica,self.entraX,self.entraY)
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
