import random as rn
import scipy.stats as st
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#::::::::::::::::::::::::::::::::::::
#:::::::: ESPECTRO EXPERIMENTAL::::::
#::::::::::::::::::::::::::::::::::::

from scipy.optimize import curve_fit
#from scipy.signal import find_peaks
from astropy.io import ascii

eje2=[254,284,2438,2769]
cuentas2=[122,136,1173,1332]

a12=1
a02=1

def gaussi2(x,a12,a02):
	return ((a12*x)+a02)

popt_gaussi2, pcov2=curve_fit(gaussi2, eje2, cuentas2, p0=[a12,a02])

errores2=np.sqrt(np.diag(pcov2))

#print(errores2)
print(popt_gaussi2)


a0=popt_gaussi2[0]
a1=popt_gaussi2[1]

enegia1=popt_gaussi2[0]*169+popt_gaussi2[1]
print(enegia1)

enegia4=popt_gaussi2[0]*630+popt_gaussi2[1]
print(enegia4)

enegia5=popt_gaussi2[0]*740+popt_gaussi2[1]
print(enegia5)

enegia6=popt_gaussi2[0]*1062+popt_gaussi2[1]
print(enegia6)


fig, axs=plt.subplots(1,1,sharey=False)


x=np.linspace(0,8000,10000)

#axs.plot(x,gaussi2(x,a0,a1),color='black')
axs.plot(eje2,cuentas2,color='red')

plt.show()