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
from scipy.signal import find_peaks
from astropy.io import ascii



datos1=ascii.read('10agua1A.txt', data_start=0) #negro
datos2=ascii.read('9agua1jabon3A.txt', data_start=0)#purpura
datos3=ascii.read('8agua2jabon1B.txt', data_start=0)#verde

g1=len(datos1)
g2=len(datos2)
g3=len(datos3)

tiempo1=np.zeros(g1)
x1=np.zeros(g1)
y1=np.zeros(g1)
radio1=np.zeros(g1)
for i in range(0,g1):
    tiempo1[i]=datos1[i][0]
    x1[i]=datos1[i][1]
    y1[i]=datos1[i][2]
    radio1[i]=math.sqrt(x1[i]**2+y1[i]**2)


tiempo2=np.zeros(g2)
x2=np.zeros(g2)
y2=np.zeros(g2)
radio2=np.zeros(g2)
for i in range(0,g2):
    tiempo2[i]=datos2[i][0]
    x2[i]=datos2[i][1]
    y2[i]=datos2[i][2]
    radio2[i]=math.sqrt(x2[i]**2+y2[i]**2)



tiempo3=np.zeros(g3)
x3=np.zeros(g3)
y3=np.zeros(g3)
radio3=np.zeros(g3)
for i in range(0,g3):
    tiempo3[i]=datos3[i][0]
    x3[i]=datos3[i][1]
    y3[i]=datos3[i][2]
    radio3[i]=math.sqrt(x3[i]**2+y3[i]**2)
    
a01=9
a11=1
a21=1

def gaussi1(x11,a01,a11,a21):
	#return a0+a1*x1**a2
	return a01*(1-a11*np.exp(-a21*x11))

popt_gaussi1, pcov=curve_fit(gaussi1, tiempo1, radio1, p0=[a01,a11,a21])

errores1= np.sqrt(np.diag(pcov))


a01=popt_gaussi1[0]
a11=popt_gaussi1[1]
a21=popt_gaussi1[2]


erroresa01=errores1[0]
erroresa11=errores1[1]
erroresa21=errores1[2]

print ('---------PRIMER AJUSTE-------------')
print (a01,a11,a21)
print (erroresa01,erroresa11,erroresa21)
print (gaussi1(100,a01,a11,a21)-gaussi1(0,a01,a11,a21))
print ('----------------------------------')

a02=8
a12=1
a22=1

def gaussi2(x12,a02,a12,a22):
	#return a0+a1*x1**a2
	return a02*(1-a12*np.exp(-a22*x12))

popt_gaussi2, pcov=curve_fit(gaussi2, tiempo2, radio2, p0=[a02,a12,a22])

errores2= np.sqrt(np.diag(pcov))


a02=popt_gaussi2[0]
a12=popt_gaussi2[1]
a22=popt_gaussi2[2]


erroresa02=errores2[0]
erroresa12=errores2[1]
erroresa22=errores2[2]


print ('-----------SEGUNDO AJUSTE------------')
print (a02,a12,a22)
print (erroresa02,erroresa12,erroresa22)
print (gaussi1(100,a02,a12,a22)-gaussi1(0,a02,a12,a22))
print ('----------------------------------')



a03=8
a13=1
a23=1

def gaussi3(x13,a03,a13,a23):
	#return a0+a1*x1**a2
	return a03*(1-a13*np.exp(-a23*x13))

popt_gaussi3, pcov=curve_fit(gaussi3, tiempo3, radio3, p0=[a03,a13,a23])

errores3= np.sqrt(np.diag(pcov))


a03=popt_gaussi3[0]
a13=popt_gaussi3[1]
a23=popt_gaussi3[2]


erroresa03=errores3[0]
erroresa13=errores3[1]
erroresa23=errores3[2]


print ('--------------TERCER AJUSTE-----------')
print (a03,a13,a23)
print (erroresa03,erroresa13,erroresa23)
print (gaussi1(100,a03,a13,a23)-gaussi1(0,a03,a13,a23))
print ('----------------------------------')



fig, axs=plt.subplots(1,1,sharey=False)


fig.suptitle('COMPORTAMIENTO DE 1 GOTA DE LA COMPOSIÓN \n AGUA + DETERGENTE + TINTA CHINA', fontsize=20)
plt.xlabel('Tiempo (seg)', fontsize=15)
plt.ylabel('Radio (mm)', fontsize=17)
plt.text(3.5, 16, r'$a_0=18.39\pm0.03; a_1=0.152\pm0.001; a_2=0.45\pm0.01$',{'color': 'k', 'fontsize': 10, 'ha': 'center', 'va': 'center','bbox': dict(boxstyle="round", fc="w", ec="k", pad=0.2)})

axs.plot(tiempo1,gaussi1(tiempo1,a01,a11,a21),color='black', label = 'AJUSTE-1')
axs.plot(tiempo1,radio1,color='red', label = 'EXPERIMENTAL-1')
axs.plot(tiempo2,gaussi1(tiempo2,a02,a12,a22),color='purple', label = 'AJUSTE-2')
axs.plot(tiempo2,radio2,color='aqua', label = 'EXPERIMENTAL-2')
axs.plot(tiempo3,gaussi1(tiempo3,a03,a13,a23),color='lime', label = 'AJUSTE-3')
axs.plot(tiempo3,radio3,color='gold', label = 'EXPERIMENTAL-3')



leg=plt.legend(loc="center right")
for legobj in leg.legendHandles: #tamaño de la leyenda
    legobj.set_linewidth(5.0) #tamaño de la leyenda
plt.show()