import csv
import matplotlib.pyplot as plt
import numpy as np

#fctn that creates data lists
def lists(condition, line, liste):
    if line[1] == condition:            #delimitates the condition in which the box will be
        for j in range(2,len(line)-1):
            liste.append(line[j])       # puts all the lentil lenghts-values from boxes in the same conditions on the same list
    return liste

#fctn that will parse our document into a list for X file (LOL) and X condition
def list_condition(nom_fichier, condition):
    dd = open(nom_fichier, 'r')         #opens the file
    data = dd.readlines()               #reads the file
    lista = list()                      #creates a list
    for i in data:
        line = i.split(',')             #converts the string in a lists
        lists(condition, line, lista)   #applicates the first fonction to X conditions
    return lista

def sustraction(nom_fichier, condition):
    lista = list_condition(nom_fichier, condition)
    lista_None = list_condition(nom_fichier, condition)
    sustr = [float(m) - float(n) for m,n in zip(lista_fin,lista_debut)]
    return sustr

#A FAIRE !!!!!!!
def comp(nom_fichier_debut, nom_fichier_fin, condition):
    lista_debut = list_condition(nom_fichier_debut, condition)
    lista_fin = list_condition(nom_fichier_fin, "None")
    sustr = [float(m) - float(n) for m,n in zip(lista_fin,lista_debut)]
    return sustr

a = sustraction('data_debut.csv', 'data_fin.csv', "Sunlight")
b = sustraction('data_debut.csv', 'data_fin.csv', "None")
c = list()
d = list()
for i in a:
    c.append(1)
    d.append(2)

plt.plot(c, a, 'o')
plt.plot(d, b, 'o')
plt.show()



#conposd= list_condition('data_debut.csv', 'Sunlight')
#conposf, connegf, uvf, bluef, greenf, reff, irf = list_same_condition('data_fin.csv')
#print(conposd)
#print(connegd)

#def list_same_condition(nom_fichier):
#    dd = open(nom_fichier, 'r')         #opens the file
#    data = dd.readlines()               #reads the file
#    conpos = list()                     #delimitation of lists
#    conneg = list()
#    uv = list()
#    blue = list()
#    green = list()
#    red = list()
#    ir = list()
#    for i in data:
#        line = i.split(',')               #converts the strings in lists
#        lists("Sunlight", line, conpos)   #applicates the first fonction to all conditions
#        lists("None", line, conneg)
#        lists("UV", line, uv)
#        lists("Blue", line, blue)
#        lists("Green", line, green)
#        lists("Red", line, red)
#        lists("IR", line, ir)
#    return conpos, conneg, uv, blue, green, red, ir
#
#conposd, connegd, uvd, blued, greend, redd, ird = list_same_condition('data_debut.csv')
#conposf, connegf, uvf, bluef, greenf, reff, irf = list_same_condition('data_fin.csv')
#print(conposd)
#print(connegd)
