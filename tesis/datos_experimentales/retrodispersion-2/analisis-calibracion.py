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

#calibracion



datosMC0=ascii.read('27-11-2020-NaI-Detector-600s-fuente133Ba57Co-fondo.mca', data_start=0)
datosMC1=ascii.read('27-11-2020-NaI-Detector-600s-fuente133Ba57Co-L1.mca', data_start=0)
datosMC2=ascii.read('27-11-2020-NaI-Detector-600s-fuente133Ba57Co-L2.mca', data_start=0)
datosMC3=ascii.read('27-11-2020-NaI-Detector-600s-fuente133Ba57Co-L3.mca', data_start=0)
datosMC4=ascii.read('27-11-2020-NaI-Detector-600s-fuente133Ba57Co-L4.mca', data_start=0)
datosMC5=ascii.read('27-11-2020-NaI-Detector-600s-fuente133Ba57Co-L5.mca', data_start=0)
datosMC6=ascii.read('27-11-2020-NaI-Detector-600s-fuente133Ba57Co-L6.mca', data_start=0)

#morteros
datosM0=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L0.mca', data_start=0)
datosM1=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L1.mca', data_start=0)
datosM2=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L2.mca', data_start=0)
datosM3=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L3.mca', data_start=0)
datosM4=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L4.mca', data_start=0)
datosM5=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L5.mca', data_start=0)
datosM6=ascii.read('27-11-2020-NaI-Detector-3600s-fuenteCs137-L6.mca', data_start=0)

gC0=len(datosMC0)
gC1=len(datosMC1)
gC2=len(datosMC2)
gC3=len(datosMC3)
gC4=len(datosMC4)
gC5=len(datosMC5)
gC6=len(datosMC6)


g0=len(datosM0)
g1=len(datosM1)
g2=len(datosM2)
g3=len(datosM3)
g4=len(datosM4)
g5=len(datosM5)
g6=len(datosM6)


cuentasMC0=np.zeros(gC0)
canalMC0=np.zeros(gC0)
ejeXMC0=np.zeros(gC0)
for i in range(0,gC0):
    cuentasMC0[i]=datosMC0[i][0]
    #canal[i]=datos[i][0]
    ejeXMC0[i]=i

cuentasMC1=np.zeros(gC1)
canalMC1=np.zeros(gC1)
ejeXMC1=np.zeros(gC1)
for i in range(0,gC1):
    cuentasMC1[i]=datosMC1[i][0]
    #canal[i]=datos[i][0]
    ejeXMC1[i]=i

cuentasMC2=np.zeros(gC2)
canalMC2=np.zeros(gC2)
ejeXMC2=np.zeros(gC2)
for i in range(0,gC2):
    cuentasMC2[i]=datosMC2[i][0]
    #canal[i]=datos[i][0]
    ejeXMC2[i]=i

cuentasMC3=np.zeros(gC3)
canalMC3=np.zeros(gC3)
ejeXMC3=np.zeros(gC3)
for i in range(0,gC3):
    cuentasMC3[i]=datosMC3[i][0]
    #canal[i]=datos[i][0]
    ejeXMC3[i]=i

cuentasMC4=np.zeros(gC4)
canalMC4=np.zeros(gC4)
ejeXMC4=np.zeros(gC4)
for i in range(0,gC4):
    cuentasMC4[i]=datosMC4[i][0]
    #canal[i]=datos[i][0]
    ejeXMC4[i]=i

cuentasMC5=np.zeros(gC5)
canalMC5=np.zeros(gC5)
ejeXMC5=np.zeros(gC5)
for i in range(0,gC5):
    cuentasMC5[i]=datosMC5[i][0]
    #canal[i]=datos[i][0]
    ejeXMC5[i]=i

cuentasMC6=np.zeros(gC6)
canalMC6=np.zeros(gC6)
ejeXMC6=np.zeros(gC6)
for i in range(0,gC6):
    cuentasMC6[i]=datosMC6[i][0]
    #canal[i]=datos[i][0]
    ejeXMC6[i]=i

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

##################################################################################
#ajuste para acomodar los picos

########################### L0 #############################3

#PRIMER PICO
m01=76
m02=113

#SEGUNDO PICO
m11=113
m12=157

#TERCER PICO (en canales)
m21=346
m22=430


maximo0=int(max(cuentasMC0[m01:m02]))
maximo1=int(max(cuentasMC0[m11:m12]))
maximo2=int(max(cuentasMC0[m21:m22]))

for i in range(m01,m02):
	if cuentasMC0[i]==maximo0:
		d0=ejeXMC0[i]
                
for i in range(m11,m12):
	if cuentasMC0[i]==maximo1:
		d1=ejeXMC0[i]

for i in range(m21,m22):
	if cuentasMC0[i]==maximo2:
		d2=ejeXMC0[i]
                



y=[81,122,356] #energía
x=[d0,d1,d2] #canales

a1=1
a0=7
def regresion(t,a1,a0):
    return ((t*a1)+a0)

popt_retro,pcov_retro=curve_fit(regresion, x, y, p0=[a1,a0])

a1=popt_retro[0]
a0=popt_retro[1]



for j in range (len(ejeXMC0)):
    canalMC0[j]= regresion(ejeXMC0[j],a1,a0)




E1=int(regresion(m21,a1,a0)) #keV
E2=int(regresion(m22,a1,a0)) #keV)

energia0=canalMC0[E1:E2]
cuentas0=0
for i in range(len(energia0)):
   cuentas0=cuentas0+cuentasMC0[i]
    
print (cuentas0)

for j in range (len(canalM0)):
    cuentasM0[j]= cuentasM0[j]/cuentas0

########################### L1 #############################3


maximo0=int(max(cuentasMC1[m01:m02]))
maximo1=int(max(cuentasMC1[m11:m12]))
maximo2=int(max(cuentasMC1[m21:m22]))

for i in range(m01,m02):
	if cuentasMC1[i]==maximo0:
		d0=ejeXMC1[i]
                
for i in range(m11,m12):
	if cuentasMC1[i]==maximo1:
		d1=ejeXMC1[i]

for i in range(m21,m22):
	if cuentasMC1[i]==maximo2:
		d2=ejeXMC1[i]

y=[81,122,356] #energía
x=[d0,d1,d2] #canales

popt_retro,pcov_retro=curve_fit(regresion, x, y, p0=[a1,a0])

a1=popt_retro[0]
a0=popt_retro[1]

for j in range (len(ejeXMC1)):
    canalMC1[j]= regresion(ejeXMC1[j], a1, a0)

E1=int(regresion(m21,a1,a0)) #keV
E2=int(regresion(m22,a1,a0)) #keV)

energia1=canalMC1[E1:E2]
cuentas1=0
for i in range(len(energia1)):
   cuentas1=cuentas1+cuentasMC1[i]
    
print (cuentas1)

for j in range (len(canalM1)):
    cuentasM1[j]= cuentasM1[j]/cuentas1
####################################################################

########################### L2 #############################3

maximo0=int(max(cuentasMC2[m01:m02]))
maximo1=int(max(cuentasMC2[m11:m12]))
maximo2=int(max(cuentasMC2[m21:m22]))

for i in range(m01,m02):
	if cuentasM2[i]==maximo0:
		d0=ejeXM2[i]
                
for i in range(m11,m12):
	if cuentasM2[i]==maximo1:
		d1=ejeXM2[i]

for i in range(m21,m22):
	if cuentasMC2[i]==maximo2:
		d2=ejeXMC2[i]

y=[81,122,356] #energía
x=[d0,d1,d2] #canales

popt_retro,pcov_retro=curve_fit(regresion, x, y, p0=[a1,a0])

a1=popt_retro[0]
a0=popt_retro[1]


for j in range (len(ejeXMC2)):
    canalMC2[j]= regresion(ejeXMC2[j], a1, a0)

E1=int(regresion(m21,a1,a0)) #keV
E2=int(regresion(m22,a1,a0)) #keV)

energia2=canalMC2[E1:E2]
cuentas2=0
for i in range(len(energia2)):
   cuentas2=cuentas2+cuentasMC2[i]
    
print (cuentas2)

for j in range (len(canalM2)):
    cuentasM2[j]= cuentasM2[j]/cuentas2
####################################################################


########################### L3 #############################3

maximo0=int(max(cuentasMC3[m01:m02]))
maximo1=int(max(cuentasMC3[m11:m12]))
maximo2=int(max(cuentasMC3[m21:m22]))

for i in range(m01,m02):
    if cuentasMC3[i]==maximo0:
        d0=ejeXMC3[i]

for i in range(m11,m12):
    if cuentasMC3[i]==maximo1:
        d1=ejeXMC3[i]


for i in range(m11,m12):
    if cuentasMC3[i]==maximo2:
        d2=ejeXMC3[i]


y=[81,122,356] #energía
x=[d0,d1,d2] #canales

popt_retro,pcov_retro=curve_fit(regresion, x, y, p0=[a1,a0])

a1=popt_retro[0]
a0=popt_retro[1]


for j in range (len(ejeXMC3)):
    canalMC3[j]= regresion(ejeXMC3[j],a1,a0)

E1=int(regresion(m21,a1,a0)) #keV
E2=int(regresion(m22,a1,a0)) #keV)

energia3=canalMC3[E1:E2]
cuentas3=0
for i in range(len(energia3)):
   cuentas3=cuentas3+cuentasMC3[i]
    
print (cuentas3)
for j in range (len(canalM3)):
    cuentasM3[j]= cuentasM3[j]/cuentas3
####################################################################


########################### L4 #############################3
maximo0=int(max(cuentasMC4[m01:m02]))
maximo1=int(max(cuentasMC4[m11:m12]))
maximo2=int(max(cuentasMC4[m21:m22]))

for i in range(m01,m02):
	if cuentasMC4[i]==maximo0:
		d0=ejeXMC4[i]
                
for i in range(m11,m12):
	if cuentasMC4[i]==maximo1:
		d1=ejeXMC4[i]


for i in range(m21,m22):
	if cuentasMC4[i]==maximo2:
		d2=ejeXMC4[i]

y=[81,122,356] #energía
x=[d0,d1,d2] #canales

popt_retro,pcov_retro=curve_fit(regresion, x, y, p0=[a1,a0])

a1=popt_retro[0]
a0=popt_retro[1]

for j in range (len(ejeXMC4)):
    canalMC4[j]= regresion(ejeXMC4[j],a1,a0)

E1=int(regresion(m21,a1,a0)) #keV
E2=int(regresion(m22,a1,a0)) #keV)

energia4=canalMC4[E1:E2]
cuentas4=0
for i in range(len(energia4)):
   cuentas4=cuentas4+cuentasMC4[i]
    
print (cuentas4)
for j in range (len(canalM4)):
    cuentasM4[j]= cuentasM4[j]/cuentas4
####################################################################


########################### L5 #############################3
maximo0=int(max(cuentasMC5[m01:m02]))
maximo1=int(max(cuentasMC5[m11:m12]))
maximo2=int(max(cuentasMC5[m21:m22]))
for i in range(m01,m02):
	if cuentasMC5[i]==maximo0:
		d0=ejeXMC5[i]
                
for i in range(m11,m12):
	if cuentasMC5[i]==maximo1:
		d1=ejeXMC5[i]

for i in range(m21,m22):
	if cuentasMC5[i]==maximo2:
		d2=ejeXMC5[i]

y=[81,122,356] #energía
x=[d0,d1,d2] #canales

popt_retro,pcov_retro=curve_fit(regresion, x, y, p0=[a1,a0])

a1=popt_retro[0]
a0=popt_retro[1]

for j in range (len(ejeXMC5)):
    canalMC5[j]= regresion(ejeXMC5[j],a1,a0)
    
E1=int(regresion(m21,a1,a0)) #keV
E2=int(regresion(m22,a1,a0)) #keV)

energia5=canalMC5[E1:E2]
cuentas5=0
for i in range(len(energia5)):
   cuentas5=cuentas5+cuentasMC5[i]
    
print (cuentas5)
for j in range (len(canalM5)):
    cuentasM5[j]= cuentasM5[j]/cuentas5
####################################################################


########################### L6 #############################3
maximo0=int(max(cuentasMC6[m01:m02]))
maximo1=int(max(cuentasMC6[m11:m12]))
maximo2=int(max(cuentasMC6[m21:m22]))

for i in range(m01,m02):
	if cuentasMC6[i]==maximo0:
		d0=ejeXMC6[i]
                
for i in range(m11,m12):
	if cuentasMC6[i]==maximo1:
		d1=ejeXMC6[i]

for i in range(m21,m22):
	if cuentasMC6[i]==maximo2:
		d2=ejeXMC6[i]

y=[81,122,356] #energía
x=[d0,d1,d2] #canales

popt_retro,pcov_retro=curve_fit(regresion, x, y, p0=[a1,a0])

a1=popt_retro[0]
a0=popt_retro[1]

for j in range (len(ejeXMC6)):
    canalMC6[j]= regresion(ejeXMC6[j],a1,a0)

E1=int(regresion(m21,a1,a0)) #keV
E2=int(regresion(m22,a1,a0)) #keV)

energia6=canalMC6[E1:E2]
cuentas6=0
for i in range(len(energia6)):
   cuentas6=cuentas6+cuentasMC6[i]
    
print (cuentas6)
for j in range (len(canalM6)):
    cuentasM6[j]= cuentasM6[j]/cuentas6
##############################################################

fig, axs=plt.subplots(1,1,sharey=False)


#fig.suptitle('COMPARACIÓN DE REGIÓN COMPTON', fontsize=18)
plt.xlabel('Energía (keV)', fontsize=14)
plt.ylabel('cuentas', fontsize=14)
x=np.linspace(0,8000,10000)
#axs.plot(x,pdf3_3(x),color='purple')  

#x = range(799)
#plt.plot(x,histogram3,linestyle='steps-mid',color='orange')

axs.step(canalMC0,cuentasM0, where='mid',color= 'blue',label='L0')


axs.step(canalMC1,cuentasM1, where='mid',color= 'red',label='L1')

axs.step(canalMC2,cuentasM2, where='mid',color= 'aqua',label='L2')

axs.step(canalMC3,cuentasM3, where='mid',color= 'purple',label='L3')

axs.step(canalMC4,cuentasM4, where='mid',color= 'black', label='L4')

axs.step(canalMC5,cuentasM5, where='mid',color= 'yellow', label='L5')

axs.step(canalMC6,cuentasM6, where='mid',color= 'green', label='L6')
leg=plt.legend(loc='upper right',prop={'size': 14})
for legobj in leg.legendHandles: #tamaño de la leyenda
    legobj.set_linewidth(5.0) #tamaño de la leyenda

plt.show()
    
"""
E1=190 #keV
E2=250 #keV

############################################################
energia0=canalM0[E1:E2]
cuentas0=0
for i in range(len(energia0)):
   cuentas0=cuentas0+cuentasM0[i]
    
print (cuentas0)

#############################################################

############################################################
energia1=canalM1[E1:E2]
cuentas1=0
for i in range(len(energia1)):
   cuentas1=cuentas1+cuentasM1[i]
    
print (cuentas1)

#############################################################

############################################################
energia2=canalM2[E1:E2]
cuentas2=0
for i in range(len(energia2)):
   cuentas2=cuentas2+cuentasM2[i]
    
print (cuentas2)

#############################################################

############################################################
energia3=canalM3[E1:E2]
cuentas3=0
for i in range(len(energia3)):
   cuentas3=cuentas3+cuentasM3[i]
    
print (cuentas3)

#############################################################


############################################################
energia4=canalM4[E1:E2]
cuentas4=0
for i in range(len(energia4)):
   cuentas4=cuentas4+cuentasM4[i]
    
print (cuentas4)

#############################################################

############################################################
energia5=canalM5[E1:E2]
cuentas5=0
for i in range(len(energia5)):
   cuentas5=cuentas5+cuentasM5[i]
    
print (cuentas5)

#############################################################

############################################################
energia6=canalM6[E1:E2]
cuentas6=0
for i in range(len(energia6)):
   cuentas6=cuentas6+cuentasM6[i]
    
print (cuentas6)

#############################################################

############################################################
energia7=canalM7[E1:E2]
cuentas7=0
for i in range(len(energia7)):
   cuentas7=cuentas7+cuentasM7[i]
    
print (cuentas7)

#############################################################

############################################################
energia8=canalM8[E1:E2]
cuentas8=0
for i in range(len(energia8)):
   cuentas8=cuentas8+cuentasM8[i]
    
print (cuentas8)

#############################################################


############################################################
energia9=canalM9[E1:E2]
cuentas9=0
for i in range(len(energia9)):
   cuentas9=cuentas9+cuentasM9[i]
    
print (cuentas9)

#############################################################

############################################################
energia10=canalM10[E1:E2]
cuentas10=0
for i in range(len(energia10)):
   cuentas10=cuentas10+cuentasM10[i]
    
print (cuentas10)

#############################################################

############################################################
energia11=canalM11[E1:E2]
cuentas11=0
for i in range(len(energia11)):
   cuentas11=cuentas11+cuentasM11[i]
    
print (cuentas11)

#############################################################
############################################################
energia12=canalM12[E1:E2]
cuentas12=0
for i in range(len(energia12)):
   cuentas12=cuentas12+cuentasM12[i]
    
print (cuentas12)

#############################################################


intensidades=[cuentas1,cuentas2,cuentas3,cuentas4,cuentas5,cuentas6,cuentas7,cuentas8,cuentas9,cuentas10,cuentas11,cuentas12]

int_max=max(intensidades)
intensidades=intensidades/int_max
errores_inten=[math.sqrt(cuentas1),math.sqrt(cuentas2),math.sqrt(cuentas3), math.sqrt(cuentas4), math.sqrt(cuentas5), math.sqrt(cuentas6), math.sqrt(cuentas7), math.sqrt(cuentas8), math.sqrt(cuentas9), math.sqrt(cuentas10),  math.sqrt(cuentas11),  math.sqrt(cuentas12)]

propaga_error_y=[cuentas1/int_max*math.sqrt((math.sqrt(cuentas1)/cuentas1)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)), cuentas2/int_max*math.sqrt((math.sqrt(cuentas2)/cuentas2)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)), cuentas3/int_max*math.sqrt((math.sqrt(cuentas3)/cuentas3)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)), cuentas4/int_max*math.sqrt((math.sqrt(cuentas4)/cuentas4)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)),cuentas5/int_max*math.sqrt((math.sqrt(cuentas5)/cuentas5)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)),cuentas6/int_max*math.sqrt((math.sqrt(cuentas6)/cuentas6)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)),cuentas7/int_max*math.sqrt((math.sqrt(cuentas7)/cuentas7)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)),cuentas8/int_max*math.sqrt((math.sqrt(cuentas8)/cuentas8)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)),cuentas9/int_max*math.sqrt((math.sqrt(cuentas9)/cuentas9)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)),cuentas10/int_max*math.sqrt((math.sqrt(cuentas10)/cuentas10)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)), cuentas11/int_max*math.sqrt((math.sqrt(cuentas11)/cuentas11)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)), cuentas12/int_max*math.sqrt((math.sqrt(cuentas12)/cuentas12)**2+math.sqrt((math.sqrt(int_max)/int_max)**2))]

propaga_error_x=[0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005, 0.005, 0.005, 0.005]


#GROSORES-MODIFICAR
grosor=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]

fig2, axs=plt.subplots(1,1,sharey=False)
plt.xlabel('t(cm)', fontsize=14)
plt.ylabel('Intensidad', fontsize=14)
axs.plot(grosor,intensidades,'o',color= 'blue')
         
plt.show()
"""





