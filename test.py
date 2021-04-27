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



# =============================================================================
# Init
# =============================================================================
class row:
    def _init_(self):
        self.id = 0
        self.c2 = []
        self.x = []
        self.y = []
        self.c5 = []
        self.c6 = []


import math
import re
import matplotlib.pyplot as plt

doc = open("Clean List of Filament.txt", 'r')

docu = []
line = doc.readline()
line = doc.readline()
# =============================================================================
# get data
# =============================================================================
while line != '':
    ro = row()
    nb = re.split("\s+", line)
    ro.id = nb[0]
    ro.c2 = nb[1]
    ro.x = nb[2]
    ro.y = nb[3]
    ro.c5 = nb[4]
    ro.c6 = nb[5]

    docu.append(ro)
    line = doc.readline()

idActu = docu[0].id
resultat = {}
xn = float(docu[0].x)
yn = float(docu[0].y)
distance = 0
# =============================================================================
# sort data
# =============================================================================
for i in range(len(docu)):
    if idActu == docu[i].id:
        deltaX = float(docu[i].x) - float(xn)
        deltaY = float(docu[i].y) - float(yn)
        d = math.sqrt(deltaX ** 2 + deltaY ** 2)
        distance += d
        xn = float(docu[i].x)
        yn = float(docu[i].y)
    else:
        xn = float(docu[i].x)
        yn = float(docu[i].y)
        resultat[idActu] = distance
        distance = 0
        idActu = docu[i].id
resultat[idActu] = distance
xplot = []
yplot = []
for iden, value in resultat.items():
    print("Id =", iden, " \t distance = ", value)
    xplot.append(float(iden))
    yplot.append(value)
plt.plot(xplot, yplot, 'r+')
plt.xlabel('Id')
plt.ylabel('distance(pixel)')
plt.show()
doc.close()
# =============================================================================
# switch id with length
# =============================================================================
doc = open("Tracking.txt", 'r')
fulltxt = doc.read()
lines = re.split("\n", fulltxt)
mem = []
for nb in range(len(lines)):
    woleNb = re.split("\s+", lines[nb])
    for nb in range(len(woleNb)):
        if woleNb[nb] != '0' and woleNb[nb] != 'Tracks' and woleNb[nb] != '':
            woleNb[nb] = resultat[woleNb[nb]]
    mem.append(woleNb)
for row in mem:
    for nb in row:
        print(nb, end=' ')
    print()
doc.close()

