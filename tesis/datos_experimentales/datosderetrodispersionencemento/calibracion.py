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



datosM0=ascii.read('13-11-2020-NaI-Detector-3600s-fuenteCs137-L0.mca', data_start=0)
datosM1=ascii.read('13-11-2020-NaI-Detector-3600s-fuenteCs137-L1.mca', data_start=0)
datosM2=ascii.read('13-11-2020-NaI-Detector-3600s-fuenteCs137-L2.mca', data_start=0)
datosM3=ascii.read('13-11-2020-NaI-Detector-3600s-fuenteCs137-L3.mca', data_start=0)
datosM4=ascii.read('13-11-2020-NaI-Detector-3600s-fuenteCs137-L4.mca', data_start=0)
datosM5=ascii.read('13-11-2020-NaI-Detector-3600s-fuenteCs137-L5.mca', data_start=0)
datosM6=ascii.read('13-11-2020-NaI-Detector-3600s-fuenteCs137-L6.mca', data_start=0)
datosM7=ascii.read('13-11-2020-NaI-Detector-3600s-fuenteCs137-L7.mca', data_start=0)
datosM8=ascii.read('13-11-2020-NaI-Detector-3600s-fuenteCs137-L8.mca', data_start=0)
datosM9=ascii.read('13-11-2020-NaI-Detector-3600s-fuenteCs137-L9.mca', data_start=0)
datosM10=ascii.read('13-11-2020-NaI-Detector-3600s-fuenteCs137-L10.mca', data_start=0)
datosM11=ascii.read('13-11-2020-NaI-Detector-3600s-fuenteCs137-L11.mca', data_start=0)
datosM12=ascii.read('13-11-2020-NaI-Detector-3600s-fuenteCs137-L12.mca', data_start=0)

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
for i in range(0,g12):
    cuentasM11[i]=datosM11[i][0]
    #canal[i]=datos[i][0]
    ejeXM11[i]=i

cuentasM12=np.zeros(g12)
canalM12=np.zeros(g12)
ejeXM12=np.zeros(g12)
for i in range(0,g12):
    cuentasM12[i]=datosM12[i][0]
    #canal[i]=datos[i][0]
    ejeXM12[i]=i
    


#ajuste para acomodar los picos

########################### L0 #############################3

m01=60
m02=110

m11=640
m12=760

maximo0=int(max(cuentasM0[m01:m02]))
maximo1=int(max(cuentasM0[m11:m12]))

for i in range(m01,m02):
	if cuentasM0[i]==maximo0:
		d0=ejeXM0[i]
                
for i in range(m11,m12):
	if cuentasM0[i]==maximo1:
		d1=ejeXM0[i]

a1=(662-32)/(d1-d0)
a0=32-a1*d0

def regresion(x):
    return a0 + a1 * x

for j in range (len(ejeXM0)):
    canalM0[j]= regresion(ejeXM0[j])

########################### L1 #############################3


maximo0=int(max(cuentasM1[m01:m02]))
maximo1=int(max(cuentasM1[m11:m12]))

for i in range(m01,m02):
	if cuentasM1[i]==maximo0:
		d0=ejeXM1[i]
                
for i in range(m11,m12):
	if cuentasM1[i]==maximo1:
		d1=ejeXM1[i]

a1=(662-32)/(d1-d0)
a0=32-a1*d0

def regresion(x):
    return a0 + a1 * x

for j in range (len(ejeXM1)):
    canalM1[j]= regresion(ejeXM1[j])

print(a1,a0)
####################################################################

########################### L2 #############################3

maximo0=int(max(cuentasM2[m01:m02]))
maximo1=int(max(cuentasM2[m11:m12]))

for i in range(m01,m02):
	if cuentasM2[i]==maximo0:
		d0=ejeXM2[i]
                
for i in range(m11,m12):
	if cuentasM2[i]==maximo1:
		d1=ejeXM2[i]

a1=(662-32)/(d1-d0)
a0=32-a1*d0


def regresion(x):
    return a0 + a1 * x


for j in range (len(ejeXM2)):
    canalM2[j]= regresion(ejeXM2[j])


####################################################################


########################### L3 #############################3

maximo0=int(max(cuentasM3[m01:m02]))
maximo1=int(max(cuentasM3[m11:m12]))

for i in range(m01,m02):
	if cuentasM3[i]==maximo0:
		d0=ejeXM3[i]
                
for i in range(m11,m12):
	if cuentasM3[i]==maximo1:
		d1=ejeXM3[i]

a1=(662-32)/(d1-d0)
a0=32-a1*d0


def regresion(x):
    return a0 + a1 * x

for j in range (len(ejeXM3)):
    canalM3[j]= regresion(ejeXM3[j])


####################################################################


########################### L4 #############################3
maximo0=int(max(cuentasM4[m01:m02]))
maximo1=int(max(cuentasM4[m11:m12]))

for i in range(m01,m02):
	if cuentasM4[i]==maximo0:
		d0=ejeXM4[i]
                
for i in range(m11,m12):
	if cuentasM4[i]==maximo1:
		d1=ejeXM4[i]

a1=(662-32)/(d1-d0)
a0=32-a1*d0


def regresion(x):
    return a0 + a1 * x

for j in range (len(ejeXM4)):
    canalM4[j]= regresion(ejeXM4[j])


####################################################################


########################### L5 #############################3
maximo0=int(max(cuentasM5[m01:m02]))
maximo1=int(max(cuentasM5[m11:m12]))

for i in range(m01,m02):
	if cuentasM5[i]==maximo0:
		d0=ejeXM5[i]
                
for i in range(m11,m12):
	if cuentasM5[i]==maximo1:
		d1=ejeXM5[i]

a1=(662-32)/(d1-d0)
a0=32-a1*d0


def regresion(x):
    return a0 + a1 * x

for j in range (len(ejeXM5)):
    canalM5[j]= regresion(ejeXM5[j])


####################################################################


########################### L6 #############################3
maximo0=int(max(cuentasM6[m01:m02]))
maximo1=int(max(cuentasM6[m11:m12]))

for i in range(m01,m02):
	if cuentasM6[i]==maximo0:
		d0=ejeXM6[i]
                
for i in range(m11,m12):
	if cuentasM6[i]==maximo1:
		d1=ejeXM6[i]

a1=(662-32)/(d1-d0)
a0=32-a1*d0


def regresion(x):
    return a0 + a1 * x

for j in range (len(ejeXM6)):
    canalM6[j]= regresion(ejeXM6[j])


####################################################################

########################### L7 #############################3
maximo0=int(max(cuentasM7[m01:m02]))
maximo1=int(max(cuentasM7[m11:m12]))

for i in range(m01,m02):
	if cuentasM7[i]==maximo0:
		d0=ejeXM7[i]
                
for i in range(m11,m12):
	if cuentasM7[i]==maximo1:
		d1=ejeXM7[i]

a1=(662-32)/(d1-d0)
a0=32-a1*d0


def regresion(x):
    return a0 + a1 * x

for j in range (len(ejeXM7)):
    canalM7[j]= regresion(ejeXM7[j])


####################################################################

########################### L8 #############################3
maximo0=int(max(cuentasM8[m01:m02]))
maximo1=int(max(cuentasM8[m11:m12]))

for i in range(m01,m02):
	if cuentasM8[i]==maximo0:
		d0=ejeXM8[i]
                
for i in range(m11,m12):
	if cuentasM8[i]==maximo1:
		d1=ejeXM8[i]

a1=(662-32)/(d1-d0)
a0=32-a1*d0


def regresion(x):
    return a0 + a1 * x

for j in range (len(ejeXM8)):
    canalM8[j]= regresion(ejeXM8[j])


####################################################################

########################### L9 #############################3
maximo0=int(max(cuentasM9[m01:m02]))
maximo1=int(max(cuentasM9[m11:m12]))

for i in range(m01,m02):
	if cuentasM9[i]==maximo0:
		d0=ejeXM9[i]
                
for i in range(m11,m12):
	if cuentasM9[i]==maximo1:
		d1=ejeXM9[i]

a1=(662-32)/(d1-d0)
a0=32-a1*d0


def regresion(x):
    return a0 + a1 * x

for j in range (len(ejeXM9)):
    canalM9[j]= regresion(ejeXM9[j])


####################################################################

########################### L10 #############################3
maximo0=int(max(cuentasM10[m01:m02]))
maximo1=int(max(cuentasM10[m11:m12]))

for i in range(m01,m02):
	if cuentasM10[i]==maximo0:
		d0=ejeXM10[i]
                
for i in range(m11,m12):
	if cuentasM10[i]==maximo1:
		d1=ejeXM10[i]

a1=(662-32)/(d1-d0)
a0=32-a1*d0


def regresion(x):
    return a0 + a1 * x

for j in range (len(ejeXM10)):
    canalM10[j]= regresion(ejeXM10[j])


##############################################################

########################### L11 #############################3
maximo0=int(max(cuentasM11[m01:m02]))
maximo1=int(max(cuentasM11[m11:m12]))

for i in range(m01,m02):
	if cuentasM11[i]==maximo0:
		d0=ejeXM11[i]
                
for i in range(m11,m12):
	if cuentasM11[i]==maximo1:
		d1=ejeXM11[i]

a1=(662-32)/(d1-d0)
a0=32-a1*d0


def regresion(x):
    return a0 + a1 * x

for j in range (len(ejeXM11)):
    canalM11[j]= regresion(ejeXM11[j])


##############################################################


########################### L12 #############################3
maximo0=int(max(cuentasM12[m01:m02]))
maximo1=int(max(cuentasM12[m11:m12]))

for i in range(m01,m02):
	if cuentasM12[i]==maximo0:
		d0=ejeXM12[i]
                
for i in range(m11,m12):
	if cuentasM12[i]==maximo1:
		d1=ejeXM12[i]

a1=(662-32)/(d1-d0)
a0=32-a1*d0


def regresion(x):
    return a0 + a1 * x

for j in range (len(ejeXM12)):
    canalM12[j]= regresion(ejeXM12[j])


##############################################################


fig, axs=plt.subplots(1,1,sharey=False)


#fig.suptitle('COMPARACIÓN DE REGIÓN COMPTON', fontsize=18)
plt.xlabel('Energía (keV)', fontsize=14)
plt.ylabel('cuentas', fontsize=14)
x=np.linspace(0,8000,10000)
#axs.plot(x,pdf3_3(x),color='purple')  

#x = range(799)
#plt.plot(x,histogram3,linestyle='steps-mid',color='orange')
axs.step(canalM0,cuentasM0, where='mid', color= 'red')
axs.step(canalM1,cuentasM1, where='mid',color= 'purple')
axs.step(canalM2,cuentasM2, where='mid',color= 'aqua')
axs.step(canalM3,cuentasM3, where='mid',color= 'yellow')
axs.step(canalM4,cuentasM4, where='mid',color= 'black')
axs.step(canalM5,cuentasM5, where='mid',color= 'orange')
axs.step(canalM6,cuentasM6, where='mid',color= 'green')
axs.step(canalM7,cuentasM7, where='mid',color= 'blue')
axs.step(canalM8,cuentasM8, where='mid',color= 'yellow')
axs.step(canalM9,cuentasM9, where='mid',color= 'black')
axs.step(canalM10,cuentasM10, where='mid',color= 'orange')
axs.step(canalM11,cuentasM11, where='mid',color= 'green')
axs.step(canalM12,cuentasM12, where='mid',color= 'blue')

plt.show()
    

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
axs.plot(grosor,intensidades,'o',color= 'blue')
         
plt.show()

"""
################## L0 #################################333

<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 3597.141000
REAL_TIME - 3597.141000
START_TIME - 11/13/2020 09:14:37
SERIAL_NUMBER - 0
<<DATA>>
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1263;    Fine Gain
GAIN=2.879;    Total Gain (Analog * Fine)
RESL=OFF;    Detector Reset Lockout
TFLA=0.200;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
SCTC=OFF;    Scintillator Time Constant
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=1024;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=NEG;    Analog Input Pos/Neg
GAIA=2;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.500;    Slow Threshold
TLLD=OFF;    LLD Threshold
THFA=511.93;    Fast Threshold
DACO=PEAK;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=PEAKH;    AUX_OUT Selection
PRET=OFF;    Preset Time
PRER=3600.000;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=0;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=750;    HV Set
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=ICR;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=FA;    G.P. Counter Edge
GPIN=AUX2;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: TB5
Serial Number: 1168
Firmware: 6.09  Build:  0
FPGA: 6.11
Fast Count: 38460
Slow Count: 124873988
GP Count: 38460
Accumulation Time: 3597.141000
Real Time: 3600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 295.8K
Board Temp: 26\B0C
<<DPP STATUS END>>

###################### L1 ################################

<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 3597.142000
REAL_TIME - 3597.142000
START_TIME - 11/13/2020 10:20:39
SERIAL_NUMBER - 0
<<DATA>>
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1263;    Fine Gain
GAIN=2.879;    Total Gain (Analog * Fine)
RESL=OFF;    Detector Reset Lockout
TFLA=0.200;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
SCTC=OFF;    Scintillator Time Constant
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=1024;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=NEG;    Analog Input Pos/Neg
GAIA=2;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.500;    Slow Threshold
TLLD=OFF;    LLD Threshold
THFA=511.93;    Fast Threshold
DACO=PEAK;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=PEAKH;    AUX_OUT Selection
PRET=OFF;    Preset Time
PRER=3600.000;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=0;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=750;    HV Set
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=ICR;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=FA;    G.P. Counter Edge
GPIN=AUX2;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: TB5
Serial Number: 1168
Firmware: 6.09  Build:  0
FPGA: 6.11
Fast Count: 37922
Slow Count: 124932677
GP Count: 37922
Accumulation Time: 3597.142000
Real Time: 3600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 295.6K
Board Temp: 25\B0C
<<DPP STATUS END>>

###################### L2 ##########################
<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 3597.142000
REAL_TIME - 3597.142000
START_TIME - 11/13/2020 11:23:37
SERIAL_NUMBER - 0
<<DATA>>
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1263;    Fine Gain
GAIN=2.879;    Total Gain (Analog * Fine)
RESL=OFF;    Detector Reset Lockout
TFLA=0.200;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
SCTC=OFF;    Scintillator Time Constant
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=1024;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=NEG;    Analog Input Pos/Neg
GAIA=2;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.500;    Slow Threshold
TLLD=OFF;    LLD Threshold
THFA=511.93;    Fast Threshold
DACO=PEAK;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=PEAKH;    AUX_OUT Selection
PRET=OFF;    Preset Time
PRER=3600.000;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=0;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=750;    HV Set
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=ICR;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=FA;    G.P. Counter Edge
GPIN=AUX2;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: TB5
Serial Number: 1168
Firmware: 6.09  Build:  0
FPGA: 6.11
Fast Count: 37810
Slow Count: 124973164
GP Count: 37810
Accumulation Time: 3597.142000
Real Time: 3600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 295.7K
Board Temp: 25\B0C
<<DPP STATUS END>>

##################### L3 ##############################
<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 3597.142000
REAL_TIME - 3597.142000
START_TIME - 11/13/2020 12:23:59
SERIAL_NUMBER - 0
<<DATA>>
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1263;    Fine Gain
GAIN=2.879;    Total Gain (Analog * Fine)
RESL=OFF;    Detector Reset Lockout
TFLA=0.200;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
SCTC=OFF;    Scintillator Time Constant
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=1024;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=NEG;    Analog Input Pos/Neg
GAIA=2;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.500;    Slow Threshold
TLLD=OFF;    LLD Threshold
THFA=511.93;    Fast Threshold
DACO=PEAK;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=PEAKH;    AUX_OUT Selection
PRET=OFF;    Preset Time
PRER=3600.000;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=0;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=750;    HV Set
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=ICR;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=FA;    G.P. Counter Edge
GPIN=AUX2;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: TB5
Serial Number: 1168
Firmware: 6.09  Build:  0
FPGA: 6.11
Fast Count: 38041
Slow Count: 125012405
GP Count: 38041
Accumulation Time: 3597.142000
Real Time: 3600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 296.1K
Board Temp: 26\B0C
<<DPP STATUS END>>

##################### L4 ##############################

<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 3597.142000
REAL_TIME - 3597.142000
START_TIME - 11/13/2020 13:39:49
SERIAL_NUMBER - 0
<<DATA>>
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1263;    Fine Gain
GAIN=2.879;    Total Gain (Analog * Fine)
RESL=OFF;    Detector Reset Lockout
TFLA=0.200;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
SCTC=OFF;    Scintillator Time Constant
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=1024;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=NEG;    Analog Input Pos/Neg
GAIA=2;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.500;    Slow Threshold
TLLD=OFF;    LLD Threshold
THFA=511.93;    Fast Threshold
DACO=PEAK;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=PEAKH;    AUX_OUT Selection
PRET=OFF;    Preset Time
PRER=3600.000;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=0;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=750;    HV Set
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=ICR;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=FA;    G.P. Counter Edge
GPIN=AUX2;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: TB5
Serial Number: 1168
Firmware: 6.09  Build:  0
FPGA: 6.11
Fast Count: 38533
Slow Count: 125028525
GP Count: 38533
Accumulation Time: 3597.142000
Real Time: 3600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 296.2K
Board Temp: 26\B0C
<<DPP STATUS END>>

##################### L5 ##############################

<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 3597.142000
REAL_TIME - 3597.142000
START_TIME - 11/13/2020 14:40:17
SERIAL_NUMBER - 0
<<DATA>>
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1263;    Fine Gain
GAIN=2.879;    Total Gain (Analog * Fine)
RESL=OFF;    Detector Reset Lockout
TFLA=0.200;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
SCTC=OFF;    Scintillator Time Constant
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=1024;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=NEG;    Analog Input Pos/Neg
GAIA=2;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.500;    Slow Threshold
TLLD=OFF;    LLD Threshold
THFA=511.93;    Fast Threshold
DACO=PEAK;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=PEAKH;    AUX_OUT Selection
PRET=OFF;    Preset Time
PRER=3600.000;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=0;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=750;    HV Set
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=ICR;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=FA;    G.P. Counter Edge
GPIN=AUX2;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: TB5
Serial Number: 1168
Firmware: 6.09  Build:  0
FPGA: 6.11
Fast Count: 37677
Slow Count: 125067692
GP Count: 37677
Accumulation Time: 3597.142000
Real Time: 3600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 295.1K
Board Temp: 26\B0C
<<DPP STATUS END>>

##################### L6 ##############################

<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 3597.143000
REAL_TIME - 3597.143000
START_TIME - 11/17/2020 07:04:35
SERIAL_NUMBER - 0
<<DATA>>
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1263;    Fine Gain
GAIN=2.879;    Total Gain (Analog * Fine)
RESL=OFF;    Detector Reset Lockout
TFLA=0.200;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
SCTC=OFF;    Scintillator Time Constant
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=1024;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=NEG;    Analog Input Pos/Neg
GAIA=2;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.500;    Slow Threshold
TLLD=OFF;    LLD Threshold
THFA=511.93;    Fast Threshold
DACO=PEAK;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=PEAKH;    AUX_OUT Selection
PRET=OFF;    Preset Time
PRER=3600.000;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=0;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=750;    HV Set
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=ICR;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=FA;    G.P. Counter Edge
GPIN=AUX2;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: TB5
Serial Number: 1168
Firmware: 6.09  Build:  0
FPGA: 6.11
Fast Count: 36623
Slow Count: 125048163
GP Count: 36623
Accumulation Time: 3597.143000
Real Time: 3600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 295.1K
Board Temp: 25\B0C
<<DPP STATUS END>>

##################### L7 ##############################

<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 3597.142000
REAL_TIME - 3597.142000
START_TIME - 11/17/2020 08:05:52
SERIAL_NUMBER - 0
<<DATA>>
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1263;    Fine Gain
GAIN=2.879;    Total Gain (Analog * Fine)
RESL=OFF;    Detector Reset Lockout
TFLA=0.200;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
SCTC=OFF;    Scintillator Time Constant
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=1024;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=NEG;    Analog Input Pos/Neg
GAIA=2;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.500;    Slow Threshold
TLLD=OFF;    LLD Threshold
THFA=511.93;    Fast Threshold
DACO=PEAK;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=PEAKH;    AUX_OUT Selection
PRET=OFF;    Preset Time
PRER=3600.000;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=0;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=750;    HV Set
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=ICR;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=FA;    G.P. Counter Edge
GPIN=AUX2;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: TB5
Serial Number: 1168
Firmware: 6.09  Build:  0
FPGA: 6.11
Fast Count: 36310
Slow Count: 125036793
GP Count: 36310
Accumulation Time: 3597.142000
Real Time: 3600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 295.2K
Board Temp: 26\B0C
<<DPP STATUS END>>

##################### L8 ##############################

<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 3597.142000
REAL_TIME - 3597.142000
START_TIME - 11/17/2020 10:08:42
SERIAL_NUMBER - 0
<<DATA>>
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1263;    Fine Gain
GAIN=2.879;    Total Gain (Analog * Fine)
RESL=OFF;    Detector Reset Lockout
TFLA=0.200;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
SCTC=OFF;    Scintillator Time Constant
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=1024;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=NEG;    Analog Input Pos/Neg
GAIA=2;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.500;    Slow Threshold
TLLD=OFF;    LLD Threshold
THFA=511.93;    Fast Threshold
DACO=PEAK;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=PEAKH;    AUX_OUT Selection
PRET=OFF;    Preset Time
PRER=3600.000;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=0;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=750;    HV Set
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=ICR;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=FA;    G.P. Counter Edge
GPIN=AUX2;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: TB5
Serial Number: 1168
Firmware: 6.09  Build:  0
FPGA: 6.11
Fast Count: 38464
Slow Count: 125050815
GP Count: 38464
Accumulation Time: 3597.142000
Real Time: 3600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 295.5K
Board Temp: 25\B0C
<<DPP STATUS END>>

##################### L9 ##############################

<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 3597.142000
REAL_TIME - 3597.142000
START_TIME - 11/17/2020 11:09:46
SERIAL_NUMBER - 0
<<DATA>>
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1263;    Fine Gain
GAIN=2.879;    Total Gain (Analog * Fine)
RESL=OFF;    Detector Reset Lockout
TFLA=0.200;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
SCTC=OFF;    Scintillator Time Constant
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=1024;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=NEG;    Analog Input Pos/Neg
GAIA=2;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.500;    Slow Threshold
TLLD=OFF;    LLD Threshold
THFA=511.93;    Fast Threshold
DACO=PEAK;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=PEAKH;    AUX_OUT Selection
PRET=OFF;    Preset Time
PRER=3600.000;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=0;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=750;    HV Set
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=ICR;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=FA;    G.P. Counter Edge
GPIN=AUX2;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: TB5
Serial Number: 1168
Firmware: 6.09  Build:  0
FPGA: 6.11
Fast Count: 48048
Slow Count: 125096220
GP Count: 48048
Accumulation Time: 3597.142000
Real Time: 3600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 295.6K
Board Temp: 26\B0C
<<DPP STATUS END>>

##################### L10 ##############################

<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 3597.142000
REAL_TIME - 3597.142000
START_TIME - 11/17/2020 12:11:41
SERIAL_NUMBER - 0
<<DATA>>
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1263;    Fine Gain
GAIN=2.879;    Total Gain (Analog * Fine)
RESL=OFF;    Detector Reset Lockout
TFLA=0.200;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
SCTC=OFF;    Scintillator Time Constant
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=1024;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=NEG;    Analog Input Pos/Neg
GAIA=2;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.500;    Slow Threshold
TLLD=OFF;    LLD Threshold
THFA=511.93;    Fast Threshold
DACO=PEAK;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=PEAKH;    AUX_OUT Selection
PRET=OFF;    Preset Time
PRER=3600.000;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=0;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=750;    HV Set
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=ICR;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=FA;    G.P. Counter Edge
GPIN=AUX2;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: TB5
Serial Number: 1168
Firmware: 6.09  Build:  0
FPGA: 6.11
Fast Count: 37357
Slow Count: 125069733
GP Count: 37357
Accumulation Time: 3597.142000
Real Time: 3600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 295.8K
Board Temp: 26\B0C
<<DPP STATUS END>>

##################### L11 ##############################

<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 3597.142000
REAL_TIME - 3597.142000
START_TIME - 11/17/2020 13:13:27
SERIAL_NUMBER - 0
<<DATA>>
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1263;    Fine Gain
GAIN=2.879;    Total Gain (Analog * Fine)
RESL=OFF;    Detector Reset Lockout
TFLA=0.200;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
SCTC=OFF;    Scintillator Time Constant
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=1024;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=NEG;    Analog Input Pos/Neg
GAIA=2;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.500;    Slow Threshold
TLLD=OFF;    LLD Threshold
THFA=511.93;    Fast Threshold
DACO=PEAK;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=PEAKH;    AUX_OUT Selection
PRET=OFF;    Preset Time
PRER=3600.000;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=0;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=750;    HV Set
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=ICR;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=FA;    G.P. Counter Edge
GPIN=AUX2;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: TB5
Serial Number: 1168
Firmware: 6.09  Build:  0
FPGA: 6.11
Fast Count: 37456
Slow Count: 125056430
GP Count: 37456
Accumulation Time: 3597.142000
Real Time: 3600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 295.8K
Board Temp: 26\B0C
<<DPP STATUS END>>

##################### L12 ##############################

<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 3597.142000
REAL_TIME - 3597.142000
START_TIME - 11/18/2020 09:48:01
SERIAL_NUMBER - 0
<<DATA>>
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1263;    Fine Gain
GAIN=2.879;    Total Gain (Analog * Fine)
RESL=OFF;    Detector Reset Lockout
TFLA=0.200;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
SCTC=OFF;    Scintillator Time Constant
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=1024;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=NEG;    Analog Input Pos/Neg
GAIA=2;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.500;    Slow Threshold
TLLD=OFF;    LLD Threshold
THFA=511.93;    Fast Threshold
DACO=PEAK;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=PEAKH;    AUX_OUT Selection
PRET=OFF;    Preset Time
PRER=3600.000;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=0;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=750;    HV Set
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=ICR;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=FA;    G.P. Counter Edge
GPIN=AUX2;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: TB5
Serial Number: 1168
Firmware: 6.09  Build:  0
FPGA: 6.11
Fast Count: 37035
Slow Count: 125002633
GP Count: 37035
Accumulation Time: 3597.142000
Real Time: 3600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 295.6K
Board Temp: 26\B0C
<<DPP STATUS END>>

########################################################

"""
