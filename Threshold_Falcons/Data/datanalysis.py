import csv
import matplotlib.pyplot as plt
import numpy as np
import pylab

#fctn that creates data lists
def lists(condition, line, liste):
    if line[1] == condition:            #delimitates the condition in which the box will be
        for j in range(2,len(line)-1):
            liste.append(line[j])       # puts all the lentil lenghts-values from boxes in the same conditions on the same list
    return liste

#fctn that will parse our document into a list for X file and X condition
def list_condition(nom_fichier, condition):
    dd = open(nom_fichier, 'r')         #opens the file
    data = dd.readlines()               #reads the file
    lista = list()                      #creates a list
    for i in data:
        line = i.split(',')             #converts the string in a lists
        lists(condition, line, lista)   #applicates the first fonction to X conditions
    return lista

print(list_condition("data_debut.csv", "Blue"))
#fctn that will do a sustraction from two lists
def sustraction(nom_fichier_debut, nom_fichier_fin, condition):
    lista_debut = list_condition(nom_fichier_debut, condition)          # liste du debut de l'experience
    lista_fin = list_condition(nom_fichier_fin, condition)              # liste du fin de l'experience
    sustr = [float(m) - float(n) for m,n in zip(lista_fin,lista_debut)] #does the sustraction of our two lists
    return sustr

#fctn that allows to compare a list with the "None" condition values
def comp(nom_fichier_debut, nom_fichier_fin, condition):
    lista = list_condition(nom_fichier_debut, condition)                 #initial list of the condition we want to NORMALIZE
    lista = [float(i) for i in lista]                                    #Convert list of str to a list of float
    sustr = sustraction(nom_fichier_debut, nom_fichier_fin, condition)   #difference that we want to NORMALIZE
    sustrNone = sustraction(nom_fichier_debut, nom_fichier_fin, "None")  #list of condition "None"
    sustrNone = [float(i) for i in sustrNone]                            #Convert list of str to a list of float
    moyennenone = (sum(sustrNone) / len(sustrNone))                      #"None" values' mean
    difference = [i - moyennenone for i in sustr]                        #difference between our list values and "None" mean
    final = [(difference[i] / lista[i]) for i in range(0,len(lista))]    #division between this difference and lentils' initial lenght
    return final

conditions = ["None", "UV", "Red", "Green", "Blue", "IR", "Sunlight"]    #name of the conditions
data = list()
for i in range(len(conditions)):					 #loop to create a graph for each condition
    a = comp('data_debut.csv', 'data_fin.csv', conditions[i])		 #do the fonction "comp" for each condition
    data.append(a)
#    b = sustraction('data_debut.csv', 'data_fin.csv', conditions[i])
    c = list()
    for j in a:								 #loop that deletes negative values and add the legnth of other lentils to a list.
        if j >= 0:
            c.append(j)
    data.append(c)							 #adds positive lengths for each condition to a single list

plt.boxplot(data)							 #creates a boxplot for our data
pylab.xticks([1,2,3,4, 5, 6, 7], conditions)				 #changes the x axis fot condition names
plt.ylabel('Lentils length')						 #label x axis
plt.title("Comparation")						 #boxplot's title
plt.show()								 #it shows the boxplot
