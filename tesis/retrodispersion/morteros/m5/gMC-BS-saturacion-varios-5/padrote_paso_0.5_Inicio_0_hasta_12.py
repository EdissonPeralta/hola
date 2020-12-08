#*-* coding: utf-8 *-*
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

hasta=float(''.join(number[idx[-1]+1:]))
inicio=float(''.join(number[idx[-3]+1:idx[-2]]))
paso=float(''.join(number[idx[-5]+1:idx[-4]]))
print(inicio,paso,hasta)

N=int(hasta)

filenames=['0.py']

H=open(filenames[0],"r")
h=[]
for line in H:
    h.extend([line])
for i in range(len(h)):
    h[i]=''.join(h[i])
filenames=[]
for i in range(N):
    filenames.extend([str(i+1)+'_Paso_'+str(paso)+'_Inicio_'+str(inicio)+'.py'])



path='/home/edisson/Documents/hola/tesis/retrodispersion/morteros/m5/gMC-BS-saturacion-varios-5/src'

for i in range(len(filenames)):
    filename=os.path.join(path,filenames[i])
    f=open(filename,'w')
    for line in h:
        f.write(line)
    f.close
    
path='/home/edisson/Documents/hola/tesis/retrodispersion/morteros/m4/gMC-BS-saturacion-varios-5/src'


f=open('myscript','w')
f.write('#! /bin/sh'+' \n')

for i in range(len(filenames)):
    f.write('cd '+path+' \ \n')
    f.write('pwd'+' \ \n')
    f.write('python3 '+filenames[i]+' \ \n')
    f.write('echo '+filenames[i]+' \ \n')
    f.write('rm -rf '+filenames[i]+' \ \n')
    f.write('cd ../build/ '+' \ \n')
    f.write('make -j4')
    f.write(' && pwd'+' \ \n')
    f.write('./gMC run1.mac '+' \ \n')
f.close

