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

mpl.rcParams.update({"text.usetex":True,
                     "font.family":"serif",
                     "font.sans-serif":["Computer Modern San serif"],
                     "legend.fontsize":12,
                     "axes.labelsize":12,
                     "xtick.labelsize":12,
                     "ytick.labelsize":12,
                     "figure.figsize":(3.4,3.2),
                     "mathtext.fontset":"dejavusans",
                     "text.latex.preamble":r"\usepackage{amsmath}"
})


#morteros
datosM0=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L0.mca', data_start=0)
datosM1=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L1.mca', data_start=0)
datosM2=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L2.mca', data_start=0)
datosM3=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L3.mca', data_start=0)
datosM4=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L4.mca', data_start=0)
datosM5=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L5.mca', data_start=0)
datosM6=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L6.mca', data_start=0)
datosM7=ascii.read('01-12-2020-NaI-Detector-3600s-fuenteCs137-L7.mca', data_start=0)
datosM8=ascii.read('01-12-2020-NaI-Detector-3600s-fuenteCs137-L8.mca', data_start=0)
datosM9=ascii.read('01-12-2020-NaI-Detector-3600s-fuenteCs137-L9.mca', data_start=0)
datosM10=ascii.read('01-12-2020-NaI-Detector-3600s-fuenteCs137-L10.mca', data_start=0)
datosM11=ascii.read('01-12-2020-NaI-Detector-3600s-fuenteCs137-L11.mca', data_start=0)
datosM12=ascii.read('01-12-2020-NaI-Detector-3600s-fuenteCs137-L12.mca', data_start=0)



g0=len(datosM0)
g1=len(datosM1)
g2=len(datosM2)
g3=len(datosM3)
g4=len(datosM4)
g5=len(datosM5)
g6=len(datosM6)
g7=len(datosM7)
g8=len(datosM8)
g9=len(datosM9)
g10=len(datosM10)
g11=len(datosM11)
g12=len(datosM12)



###################################################################################
    
cuentasM0=np.zeros(g0)
canalM0=np.zeros(g0)
ejeXM0=np.zeros(g0)
for i in range(0,g0):
    cuentasM0[i]=datosM0[i][0]
    #canal[i]=datos[i][0]
    ejeXM0[i]=i

cuentasM1=np.zeros(g1)
canalM1=np.zeros(g1)
ejeXM1=np.zeros(g1)
for i in range(0,g1):
    cuentasM1[i]=datosM1[i][0]
    #canal[i]=datos[i][0]
    ejeXM1[i]=i

cuentasM2=np.zeros(g2)
canalM2=np.zeros(g2)
ejeXM2=np.zeros(g2)
for i in range(0,g2):
    cuentasM2[i]=datosM2[i][0]
    #canal[i]=datos[i][0]
    ejeXM2[i]=i

cuentasM3=np.zeros(g3)
canalM3=np.zeros(g3)
ejeXM3=np.zeros(g3)
for i in range(0,g3):
    cuentasM3[i]=datosM3[i][0]
    #canal[i]=datos[i][0]
    ejeXM3[i]=i

cuentasM4=np.zeros(g4)
canalM4=np.zeros(g4)
ejeXM4=np.zeros(g4)
for i in range(0,g4):
    cuentasM4[i]=datosM4[i][0]
    #canal[i]=datos[i][0]
    ejeXM4[i]=i

cuentasM5=np.zeros(g5)
canalM5=np.zeros(g5)
ejeXM5=np.zeros(g5)
for i in range(0,g5):
    cuentasM5[i]=datosM5[i][0]
    #canal[i]=datos[i][0]
    ejeXM5[i]=i


cuentasM6=np.zeros(g6)
canalM6=np.zeros(g6)
ejeXM6=np.zeros(g6)
for i in range(0,g6):
    cuentasM6[i]=datosM6[i][0]
    #canal[i]=datos[i][0]
    ejeXM6[i]=i
    
cuentasM7=np.zeros(g7)
canalM7=np.zeros(g7)
ejeXM7=np.zeros(g7)
for i in range(0,g7):
    cuentasM7[i]=datosM7[i][0]
    #canal[i]=datos[i][0]
    ejeXM7[i]=i

cuentasM8=np.zeros(g8)
canalM8=np.zeros(g8)
ejeXM8=np.zeros(g8)
for i in range(0,g8):
    cuentasM8[i]=datosM8[i][0]
    #canal[i]=datos[i][0]
    ejeXM8[i]=i

cuentasM9=np.zeros(g9)
canalM9=np.zeros(g9)
ejeXM9=np.zeros(g9)
for i in range(0,g9):
    cuentasM9[i]=datosM9[i][0]
    #canal[i]=datos[i][0]
    ejeXM9[i]=i

cuentasM10=np.zeros(g10)
canalM10=np.zeros(g10)
ejeXM10=np.zeros(g10)
for i in range(0,g10):
    cuentasM10[i]=datosM10[i][0]
    #canal[i]=datos[i][0]
    ejeXM10[i]=i

cuentasM11=np.zeros(g11)
canalM11=np.zeros(g11)
ejeXM11=np.zeros(g11)
for i in range(0,g11):
    cuentasM11[i]=datosM1[i][0]
    #canal[i]=datos[i][0]
    ejeXM11[i]=i

cuentasM12=np.zeros(g12)
canalM12=np.zeros(g12)
ejeXM12=np.zeros(g12)
for i in range(0,g12):
    cuentasM12[i]=datosM12[i][0]
    #canal[i]=datos[i][0]
    ejeXM12[i]=i

fig, axs=plt.subplots(1,1,figsize=(6,3.5))


#fig.suptitle('COMPARACIÓN DE REGIÓN COMPTON', fontsize=18)
plt.xlabel('Canales')
plt.ylabel('cuentas')
x=np.linspace(0,8000,10000)
#axs.plot(x,pdf3_3(x),color='purple')  

#x = range(799)
#plt.plot(x,histogram3,linestyle='steps-mid',color='orange')

axs.step(ejeXM0,cuentasM0, where='mid',color= 'blue',label='L0')

axs.step(ejeXM1,cuentasM1, where='mid',color= 'red',label='L1')

axs.step(ejeXM2,cuentasM2, where='mid',color= 'aqua',label='L2')

axs.step(ejeXM3,cuentasM3, where='mid',color= 'purple',label='L3')

axs.step(ejeXM4,cuentasM4, where='mid',color= 'black', label='L4')

axs.step(ejeXM5,cuentasM5, where='mid',color= 'yellow', label='L5')

axs.step(ejeXM6,cuentasM6, where='mid',color= 'green', label='L6')

axs.step(ejeXM7,cuentasM7, where='mid',color= 'deeppink', label='L7')

axs.step(ejeXM8,cuentasM8, where='mid',color= 'orange', label='L8')

axs.step(ejeXM9,cuentasM9, where='mid',color= 'indigo', label='L9')

axs.step(ejeXM10,cuentasM10, where='mid',color= 'crimson', label='L10')

axs.step(ejeXM11,cuentasM11, where='mid',color= 'magenta', label='L11')

axs.step(ejeXM12,cuentasM12, where='mid',color= 'greenyellow', label='L12')



leg=plt.legend(loc='upper left', bbox_to_anchor=(1, 1.05))#,prop={'size': 14})
#for legobj in leg.legendHandles: #tamaño de la leyenda
#    legobj.set_linewidth(5.0) #tamaño de la leyenda
fig.tight_layout()
plt.show()
