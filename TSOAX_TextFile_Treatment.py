##Code for rearranging TSOAX Tracking output raw file
##Author: Marine SILVIN - April 2021
## silvinm@igbmc.fr

# with the help of Matthieu BASTO, Bryan SIENA and Baptiste SION

# This macro can be modified and redistributed.
# Please do not remove the initial author from the code.


from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
import os
from math import sqrt
import re
import matplotlib.pyplot as plt

root = Tk()
root.withdraw()

# =============================================================================
#Choose your path directory
# =============================================================================
path = askdirectory(title='Select Working Folder') # shows dialog box and return the path
print(path)
os.chdir(path)


# =============================================================================
#Choose the raw TSOAX File on which you want to work
# =============================================================================
file_name = askopenfilename()


# =============================================================================
#Read the TSOAX File and Split it in 3 distinct text files (Parameters, Snakes, Tracking)
# =============================================================================
with open(file_name, "r") as RawFile:
    tst = RawFile.read()
    sepfile = tst.split("Tracks")
    with open("Tracking.txt","w") as fichier3:
        fichier3.write("Tracks"+sepfile[1])

    ListPart2 = sepfile[0].split("#1")
    Part1 = ListPart2[0]

    with open("Parameters.txt","w") as fichier1:
        fichier1.write(Part1)

    separator = ("#1")
    text = separator.join(ListPart2[1:])

    with open("DataMicrofilament.txt","w") as fichier2:
        fichier2.write(text)


# =============================================================================
#Create txt file with only filament list (supp $frame, #1 and [...]) and save it to a new txtfile
# =============================================================================
bad_lines = ['#', "$frame","["]

with open('DataMicrofilament.txt','r') as oldfile, open('Clean List of Filament.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_line in line for bad_line in bad_lines):
            newfile.write(line)


# =============================================================================
#Open and read this last new file to do the calcul
# =============================================================================
listeComplete=[]
with open("Clean List of Filament.txt",'r') as file:
    contenu = file.read()
    lignes = contenu.split('\n')[1:-1]
    for ligne in lignes:
        ligne=re.split('\s+',ligne)
        filament = {"id":ligne[0],"x":ligne[2],"y":ligne[3]}
        listeComplete.append(filament)

idPrecedent = 0
dictFinal={}
distance=0
for elem in listeComplete:
    if idPrecedent!=int(elem["id"]):
        dictFinal[str(idPrecedent)]=distance
        distance=0
        idPrecedent= int(elem["id"])
        xPrec = float(elem["x"])
        yPrec = float(elem["y"])
    else:
        distance += sqrt((float(elem["x"])-float(xPrec))**2 + (float(elem["y"])-float(yPrec))**2)
        xPrec=elem["x"]
        yPrec=elem["y"]
dictFinal[str(idPrecedent)]=distance
#print(dictFinal['10416'])


# =============================================================================
# Plot creation to have an idea of the length repartition by ID
# =============================================================================
xplot = []
yplot = []
for iden, value in dictFinal.items():
    print("Id =", iden, " \t distance = ", value)
    xplot.append(float(iden))
    yplot.append(value)
plt.plot(xplot, yplot, 'r+')
plt.xlabel('Id')
plt.ylabel('distance(pixel)')
plt.show()


# =============================================================================
# Merge length and tracking results + Saving Results in a new text file
# =============================================================================
tracks=[]
with open('Tracking.txt','r') as FileTracking:
    filetrack = FileTracking.read()
    for row in filetrack.splitlines():
        linestack = row.split(" ")
        tracks.append(linestack)
tracks = tracks[1:]

for i in range(len(tracks)):
    for j in range(len(tracks[i])):
        if tracks[i][j] != '':
            tracks[i][j]=dictFinal[tracks[i][j]]

with open('resultat.txt','w') as resu:
    resu.write("Tracks\n")
    for liste in tracks:
        for elem in liste:
            #print(elem)
            resu.write(str(elem)+" ")
        resu.write("\n")



'''
#remove intermediate files
if os.path.exists("Clean List of Filament.txt"):
  os.remove("Clean List of Filament.txt")
else:
  print("The file does not exist")

if os.path.exists( "DataMicrofilament.txt"):
  os.remove("DataMicrofilament.txt")
else:
  print("The file does not exist")

if os.path.exists("Parameters.txt"):
  os.remove("Parameters.txt")
else:
  print("The file does not exist")

if os.path.exists("Tracking.txt"):
  os.remove("Tracking.txt")
else:
  print("The file does not exist")
'''