from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
import os
from math import sqrt

root = Tk()
root.withdraw()


#Choose your path directory
path = askdirectory(title='Select Working Folder') # shows dialog box and return the path
print(path)
os.chdir(path)

#Choose the raw TSOAX File on which you want to work
file_name = askopenfilename()


#Read the TSOAX File and Split it in 3 distinct text files (Parameters, Snakes, Tracking)
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


#Create txt file with only filament list (supp $frame, #1 and [...]) and save it to a new txtfile
bad_lines = ['#', "$frame","["]

with open('DataMicrofilament.txt','r') as oldfile, open('Clean List of Filament.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_line in line for bad_line in bad_lines):
            newfile.write(line)


#Open and read this last new file to do the calcul
frameAnalyse = open('Clean List of Filament.txt','r')
txt = frameAnalyse.read().split()
id = 0
list_id=[]
x = 2
list_x=[]
y = 3
list_y=[]
longueurComp = int(len(txt)/6)  #count the number of iterations per frame

# Stack in independant lists ID, x and y column
for i in range (0,longueurComp):
    list_id.append(txt[id])
    list_x.append(txt[x])
    list_y.append(txt[y])

    id += 6
    x += 6
    y += 6
#print(list_id,'\n', list_x,'\n', list_y)


#Calcul part + Return a list of each ID with its total length
listCalcFilament = []
lenfilament = 0
for z in range(len(list_id)-1):
    if list_id[z] == list_id[z+1]:
        lenfilament += sqrt(
                (float(list_x[z + 1]) - float(list_x[z])) ** 2 + (float(list_y[z + 1]) - float(list_y[z])) ** 2)
        IDfilament = list_id[z]

    else:
        print("Done for this filament n°", IDfilament)
        calc_distance = (IDfilament, lenfilament)
        listCalcFilament.append(calc_distance)
        print("Le filament ID n°", IDfilament, "a pour longueur", lenfilament)
        lenfilament = 0
#print(listCalcFilament[25])


frameAnalyse.close()


