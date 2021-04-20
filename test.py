from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
import os
from math import sqrt
import re
import pandas as pd

root = Tk()
root.withdraw()

#Choose your path directory
path = askdirectory(title='Select Folder') # shows dialog box and return the path
print(path)
os.chdir(path)

'''
#Create txt file with only filament list
bad_lines = ['#', "$frame","["]

with open('DataMicrofilament.txt','r') as oldfile, open('Clean List of Filament.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_line in line for bad_line in bad_lines):
            newfile.write(line)

'''



frameAnalyse = open('Clean List of Filament.txt','r')
txt = frameAnalyse.read().split()

#print(txt[0])
id = 0
list_id=[]
#pos = 1
#list_pos = []
x = 2
list_x=[]
y = 3
list_y=[]

#permet de compter le nombre d'iterations disponibles par frame
longueurComp = int(len(txt)/6)


# Recupere chaque colone et affiche son contenu
for i in range (0,longueurComp):
    list_id.append(txt[id])
    list_x.append(txt[x])
    list_y.append(txt[y])

    id += 6
    #pos += 6
    x += 6
    y += 6

#print(list_id,'\n', list_x,'\n', list_y)
listCalcFilament = []
listIDepure = []
lenfilament = 0
for z in range(len(list_id)-1):
    if list_id[z] == list_id[z+1]:
        lenfilament += sqrt(
                (float(list_x[z + 1]) - float(list_x[z])) ** 2 + (float(list_y[z + 1]) - float(list_y[z])) ** 2)
        IDfilament = list_id[z]

    else:
        #print("Done for this filament n°", IDfilament)
        #calc_distance = (IDfilament, lenfilament)
        listCalcFilament.append(lenfilament)
        listIDepure.append(IDfilament)
        #print("Le filament ID n°", IDfilament, "a pour longueur", lenfilament)
        lenfilament = 0


frameAnalyse.close()

FileTracking = []
with open('Tracking.txt','r') as Tracks:
    filetrack = Tracks.read()
    for row in filetrack.splitlines():
        linestack = row.split(" ")
        FileTracking.append(linestack)
FileTracking = FileTracking[1:]

#print(type(FileTracking[2]))

# Program to check if a Python list contains elements of another list
for item in FileTracking:
    for element in item:
        if element in listIDepure:
            print(element)
            IndexElement = listIDepure.index(element)
            LongueurIndexe = listCalcFilament[IndexElement]
            [e.replace(str(element), str(LongueurIndexe)) for e in item]
            #print("result replacement:" , item)
            #print("Element change:", element, "par", LongueurIndexe)
            sec = input('Voilà ce que jai fait\n', )
            print('Going to sleep for', sec, 'seconds.')
            time.sleep(int(sec))
        else:
            print("This element does not exist", element)

Tracks.close()
