import numpy as np
import scipy.stats as st
from scipy.stats import norm

'''-----------------------------------------------------------
---------------------- SE OBTIENEN LOS DATOS -------------------
   -----------------------------------------------------------'''

date='03-12-2020'; detector='BF3'; setup='A'
gain='128'

path='Data/'+date+'/'+detector+setup+'/'

T_array=['045','085','130','135','155','180']

for T in T_array:
        file=detector+setup+'-G'+gain+'-Th'+T+'-TransmiParaf-'

        fondo = np.genfromtxt(' BF3A-G128-Th045-TransmiParaf-Cf252-130s.mtxt',skip_header=11,skip_footer=972)
        fuente = np.genfromtxt(' BF3A-G128-Th045-TransmiParaf-Cf252-130s.mtxt',skip_header=11,skip_footer=972)

        if setup == 'A':
            globals()['yAs'+str(T)]=fuente[0:,3]; globals()['yAb'+str(T)]=fondo[0:,3]
            globals()['D_yA'+str(T)]= globals()['yAs'+str(T)] - globals()['yAb'+str(T)]

        elif setup == 'B':
            globals()['yBr'+str(T)]=fuente[0:,2]; globals()['yBr'+str(T)]=fondo[0:,3]
            globals()['D_yB'+str(T)]= globals()['yBs'+str(T)] - globals()['yBb'+str(T)]

X = np.arange(0,len(globals()['y'+str(setup)+str(1)])+1)
