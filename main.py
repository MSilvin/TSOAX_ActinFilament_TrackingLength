
#---------------SEPARATION DES FICHIERS------------#
f = open('tracking_snakes.txt', 'r')
txt = f.read()

def set():
  Setup = open('Setup.txt','w')
  texteSetup = txt.split('#1',1)
  Setup.write(texteSetup[0])
  Setup.close

def track():
  Tracks= open('Tracks.txt','w')
  texteTracks = txt.split('Tracks',1)
  Tracks.write(texteTracks[1])
  Tracks.close

def frame():
  Frame= open('Frame.txt','w')
  texteFrame = txt.split('#1',1)
  text=texteFrame[1].split('Tracks',1)
  Frame.write(text[0])
  Frame.close

set()
track()
frame()

f.close()

#---------------Calcul des longueurs Frames------------#
def analyse():
  frameAnalyse = open('Frame.txt','r')
  txt = frameAnalyse.read().split('$frame',1)
  stringinter = txt[0].split()
  print(stringinter,'\n')

  # Definie les position de colones des informations
  id  = 0
  list_id=[]
  pos = 1
  list_pos=[]
  x   = 2
  list_x=[]
  y   = 3
  list_y=[]
  #permet de compter le nombre d'iterations disponibles par frame
  longueurComp = int(len(stringinter)/6) 

  # Recupere chaque colone et affiche son contenu
  for i in range (0,longueurComp):
    list_id.append(stringinter[id])
    list_pos.append(stringinter[pos])
    list_x.append(stringinter[x])
    list_y.append(stringinter[y])

    id  += 6
    pos += 6
    x   += 6
    y   += 6 

  print(list_id,'\n',list_pos,'\n', list_x,'\n', list_y)

  frameAnalyse.close()



analyse()