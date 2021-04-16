from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
import os
from math import sqrt

root = Tk()
root.withdraw()

#Choose your path directory
path = askdirectory(title='Select Folder') # shows dialog box and return the path
print(path)
os.chdir(path)

#Choose the file on which you want to run this code
file_name = askopenfilename()

'''
#lire le fichier général
#split le fichier en 3 parties distinctes (Parameters, Snakes, Tracking)

with open(file_name, "r") as RawFile:
    tst = RawFile.read()
    #print(tst)
    sepfile = tst.split("Tracks")
    with open("Tracking.txt","w") as fichier3:
        fichier3.write("Tracks"+sepfile[1])

    ListPart2 = sepfile[0].split("#1")
    Part1 = ListPart2[0]

    with open("Parameters.txt","w") as fichier1:
        fichier1.write(Part1)

    separator = ("#1")
    text = separator.join(ListPart2[1:])
#    text="#1"+text
    with open("DataMicrofilament.txt","w") as fichier2:
        fichier2.write(text)
'''

#create list en séparant par $frame et dans ce cas, affiche que pour tout le premier ID
frameAnalyse = open('DataMicrofilament.txt','r')
txt = frameAnalyse.read().split('$frame',1)
stringinter = txt[0].split()
print(stringinter,'\n')
#Definie les positions des colonnes des informations
id = 0
list_id=[]
#pos = 1
#list_pos = []
x = 2
list_x=[]
y = 3
list_y=[]
#permet de compter le nombre d'iterations disponibles par frame
longueurComp = int(len(stringinter)/6)

# Recupere chaque colone et affiche son contenu
for i in range (0,longueurComp):
    list_id.append(stringinter[id])
    #list_pos.append(stringinter[pos])
    list_x.append(stringinter[x])
    list_y.append(stringinter[y])

    id += 6
    #pos += 6
    x += 6
    y += 6

print(list_id)
#print(list_id,'\n', list_x,'\n', list_y)


'''
#calcul des longueurs
lenfilament = 0
for i in range(len(list_x) - 1):
    lenfilament += sqrt((float(list_x[i+1]) - float(list_x[i]))**2 + (float(list_y[i+1]) - float(list_y[i]))**2)
    IDfilament = list_id[i]
print("Le filament ID n°", IDfilament, "a pour longueur", lenfilament)
'''


frameAnalyse.close()


