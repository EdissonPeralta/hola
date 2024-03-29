#-*- coding: utf-8 -*-
"""creator on Thu Sept 17
@author: Fabian Pastrana
"""

import numpy as np
import glob
from numpy import genfromtxt
import csv
import pandas as pd
import os

number=os.path.basename(__file__)[:-3]
number=list(number)
idx=[]
for i in range(len(number)):
    if number[i]=='_':
        idx.extend([i])

inicio=float(''.join(number[idx[-1]+1:]))
paso=float(''.join(number[idx[-3]+1:idx[-2]]))
number=float(''.join(number[0:idx[0]]))
valor=inicio+number*paso
if valor >=0:
    valor=list('+'+str(valor)+'*cm')
else:
    valor=list(str(valor)+'*cm')
    
filenames=['gMCDetectorConstruction.cc','gMCRunAction.cc']

#:::::::::::::lectura de los datos:::::Detector Construction:::::::::::::::::

H=open(filenames[0],"r")
h=[]
for line in H:
    h.extend([line])
#ahora ubico dónde está pos1
index=[[],[]]
n=0
for i in range(len(h)):
    try:
        index[1].extend([h[i].index('placa_hz')])
        index[0].extend([i])
    except ValueError:
        n+=1
print(index)
index=[index[0][0],index[1][0]]
print(h[index[0]:index[1]])
index2=[]
index2.extend([h[index[0]].index('=')])
index2.extend([h[index[0]].index(';')])

print(h[index[0]][index2[0]+1:index2[1]])
for i in range(len(h)):
    h[i]=list(h[i])
h[index[0]][index2[0]+1:index2[1]]=valor
for i in range(len(h)):
    h[i]=''.join(h[i])

f=open(filenames[0],'w')
for line in h:
    f.write(line)
f.close

#:::::::::::::lectura de los datos:::::Nombre Espectro:::::::::::::::::
H=open(filenames[1],"r")
h=[]
for line in H:
    h.extend([line])
#ahora ubico dónde está pos1
index=[[],[]]
n=0
for i in range(len(h)):
    try:
        index[1].extend([h[i].index('CreateH1')])
        index[0].extend([i])
    except ValueError:
        n+=1


index=[index[0][0],index[1][0]]

index2=[]
index2.extend([h[index[0]].index('(')])
index2.extend([h[index[0]].index(',')])
print(h[index[0]][index2[0]+2:index2[1]-1])
valor=number
valor=list('NaI'+str(int(valor)))
print(valor)
for i in range(len(h)):
    h[i]=list(h[i])
h[index[0]][index2[0]+2:index2[1]-1]=valor
for i in range(len(h)):
    h[i]=''.join(h[i])

f=open(filenames[1],'w')
for line in h:
    f.write(line)
f.close

