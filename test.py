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

linestrack = []
with open('Tracking.txt','r') as Tracks:
    filetrack = Tracks.read()
    for row in filetrack.splitlines():
        FileTracking = row.split(" ")
    #    print(FileTracking)

# Program to check if a Python list contains elements of another list


for index, ID in enumerate(FileTracking)
    set1 = set(FileTracking)
    set2 = set(listIDepure)
    for m in range(len(FileTracking)-1):
        if set1.intersection(set2):
            FileTracking[index] =



Tracks.close()