import string
import random


def estereograma(archivo,nombre):
    f = open(archivo,"r")
    g = open(nombre+".txt","w")
    lines = f.readlines()
    abc = string.letters
    sub = abc[26:]
    for i in lines:
        for j in i:
            rand = random.choice(sub)
            g.write(rand)
        g.write("\n")
    g.close()
