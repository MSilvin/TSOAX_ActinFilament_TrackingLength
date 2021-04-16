from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
import os
from math import sqrt
import re


root = Tk()
root.withdraw()

#Choose your path directory
path = askdirectory(title='Select Folder') # shows dialog box and return the path
print(path)
os.chdir(path)

'''


'''
#Create txt file with only filament list
bad_lines = ['#', "$frame"]

with open('DataMicrofilament.txt','r') as oldfile, open('Clean List of Filament.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_line in line for bad_line in bad_lines):
            newfile.write(line)



frameAnalyse = open('Clean List of Filament.txt','r')
txt = frameAnalyse.read()#.split()


print(txt)



frameAnalyse.close()
