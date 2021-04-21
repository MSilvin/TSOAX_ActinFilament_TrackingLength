##Code for rearranging TSOAX Tracking output raw file

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
#print(listCalcFilament[25])


#Reading the Tracking file + supp first line "Tracks"
FileTracking = []
with open('Tracking.txt','r') as Tracks:
    filetrack = Tracks.read()
    for row in filetrack.splitlines():
        linestack = row.split(" ")
        FileTracking.append(linestack)
FileTracking = FileTracking[1:]

#print(type(FileTracking[2]))

#Where you search for ID and replace it by the length of the filament in the Tracking file
for i in range(len(listIDepure)):
    for j in range(len(FileTracking)):
        for k in range(len(FileTracking[j])):
            if FileTracking[j][k] == listIDepure[i]:
                FileTracking[j][k] = str(listCalcFilament[i])


#Extract the result in a final text file
with open('TrackingResult.txt','w') as resu:
    for liste in FileTracking:
        for elem in liste:
            #print(elem)
            resu.write(elem+" ")
        resu.write("\n")

Tracks.close()


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