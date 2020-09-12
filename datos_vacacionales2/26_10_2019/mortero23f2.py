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



datos2FM23=ascii.read('26-10-2019-PX5-HPGe-300s-fuentes2-23.MCA', data_start=0)

g=len(datos2FM23)

cuentas2FM23=np.zeros(g)
#canalM11=np.zeros(g)
ejeX2FM23=np.zeros(g)
for i in range(0,g):
    cuentas2FM23[i]=datos2FM23[i][0]
    #canal[i]=datos[i][0]
    ejeX2FM23[i]=i




#########################################################
#################### 22Na-511keV ########################
#########################################################

M1=int(max(cuentas2FM23[1000:1120]))


for i in range(1000,1120):
	if cuentas2FM23[i]==M1:
		miu1=ejeX2FM23[i]

sigma1=math.sqrt(miu1)


cuentas1=cuentas2FM23[1000:1120]
eje1=ejeX2FM23[1000:1120]

a0=1
a1=1
sigma1=1.5
def gaussi1(x,M1,miu1,sigma1,a1,a0):
	return M1*(np.exp(-((miu1-x)**2)/((math.sqrt(2)*sigma1)**2)))+((a1*x)+a0)

popt_gaussi1, pcov=curve_fit(gaussi1, eje1, cuentas1, p0=[M1,miu1,sigma1,a1,a0])

errores1= np.sqrt(np.diag(pcov))

print('errores1',errores1)

M1=popt_gaussi1[0]
miu1=popt_gaussi1[1]
sigma1=popt_gaussi1[2]
a1=popt_gaussi1[3]
a0=popt_gaussi1[4]

print('nuevas cuentas')
nue_cuen1=math.sqrt(2*math.pi)*M1*sigma1
print(nue_cuen1)
print(M1,'----',sigma1)


erroresM1=errores1[0]
erroressigma1=errores1[2]

print(erroresM1)
print(erroressigma1)
incer1=nue_cuen1*math.sqrt((erroresM1/M1)**2+(erroressigma1/sigma1)**2)

print('incertidumbre en las cuentas!!!')
print(incer1)

#########################################################
#################### 137Cs - 661keV #####################
#########################################################

M2=int(max(cuentas2FM23[1320:1420]))


for i in range(1320,1420):
	if cuentas2FM23[i]==M2:
		miu2=ejeX2FM23[i]

sigma2=math.sqrt(miu2)


cuentas2=cuentas2FM23[1320:1420]
eje2=ejeX2FM23[1320:1420]


a02=1
a12=1
sigma2=1.5
def gaussi2(x,M2,miu2,sigma2,a12,a02):
	return M2*(np.exp(-((miu2-x)**2)/((math.sqrt(2)*sigma2)**2)))+((a12*x)+a02)

popt_gaussi2, pcov2=curve_fit(gaussi1, eje2, cuentas2, p0=[M2,miu2,sigma2,a12,a02])

errores2=np.sqrt(np.diag(pcov2))

print(errores2)

M2=popt_gaussi2[0]
miu2=popt_gaussi2[1]
sigma2=popt_gaussi2[2]
a12=popt_gaussi2[3]
a02=popt_gaussi2[4]

print('nuevas cuentas2')
nue_cuen2=math.sqrt(2*math.pi)*M2*sigma2
print(nue_cuen2)
print(M2,'----',sigma2)



erroresM2=errores2[0]
erroressigma2=errores2[2]

print(erroresM2)
print(erroressigma2)
incer2=nue_cuen2*math.sqrt((erroresM2/M2)**2+(erroressigma2/sigma2)**2)

print('incertidumbre en las cuentas!!!')
print(incer2)





#########################################################
#################### 22Na - 1274keV #####################
#########################################################
M3=int(max(cuentas2FM23[2620:2680]))


for i in range(2620,2680):
	if cuentas2FM23[i]==M3:
		miu3=ejeX2FM23[i]

sigma3=math.sqrt(miu3)


cuentas3=cuentas2FM23[2620:2680]
eje3=ejeX2FM23[2620:2680]



a03=1
a13=1
sigma3=1.5
def gaussi3(x,M3,miu3,sigma3,a13,a03):
	return M3*(np.exp(-((miu3-x)**2)/((math.sqrt(2)*sigma3)**2)))+((a13*x)+a03)

popt_gaussi3, pcov3=curve_fit(gaussi3, eje3, cuentas3, p0=[M3,miu3,sigma3,a13,a03])

errores3= np.sqrt(np.diag(pcov3))

print(errores3)


M3=popt_gaussi3[0]
miu3=popt_gaussi3[1]
sigma3=popt_gaussi3[2]
a13=popt_gaussi3[3]
a03=popt_gaussi3[4]

print('nuevas cuentas3')
nue_cuen3=math.sqrt(2*math.pi)*M3*sigma3
print(nue_cuen3)
print(M3,'----',sigma3)


erroresM3=errores3[0]
erroressigma3=errores3[2]

print(erroresM3)
print(erroressigma3)
incer3=nue_cuen3*math.sqrt((erroresM3/M3)**2+(erroressigma3/sigma3)**2)

print('incertidumbre en las cuentas!!!')
print(incer3)


fig, axs=plt.subplots(1,1,sharey=False)

fig.suptitle('  ', fontsize=18)
plt.xlabel('CANAL ', fontsize=20)
plt.ylabel('CUENTAS', fontsize=20)
x=np.linspace(0,8000,10000)

axs.plot(x,gaussi1(x,M1,miu1,sigma1,a1,a0),color='black')
axs.plot(x,gaussi2(x,M2,miu2,sigma2,a12,a02),color='purple')
axs.plot(x,gaussi3(x,M3,miu3,sigma3,a13,a03),color='green')


axs.step(eje1,cuentas1,color='red')
axs.step(eje2,cuentas2,color='red')
axs.step(eje3,cuentas3,color='red')


plt.show()


"""
<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 5
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 288.990000
REAL_TIME - 300.000000
START_TIME - 10/26/2019 10:17:10
SERIAL_NUMBER - 0
<<DATA>>
-------------------------------------------------
<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=80;    20MHz/80MHz
TPEA=5.600;    Peaking Time
GAIF=0.9630;    Fine Gain
GAIN=2.343;    Total Gain (Analog * Fine)
RESL=125;    Detector Reset Lockout
TFLA=0.600;    Flat Top
TPFA=400;    Fast Channel Peaking Time
PURE=ON;    PUR Interval On/Off
RTDE=OFF;    RTD On/Off
MCAS=NORM;    MCA Source
MCAC=8192;    MCA/MCS Channels
SOFF=OFF;    Set Spectrum Offset
AINP=POS;    Analog Input Pos/Neg
INOF=DEF;    Input Offset
GAIA=5;    Analog Gain Index
CUSP=0;    Non-Trapezoidal Shaping
PDMD=NORM;    Peak Detect Mode (Min/Max)
THSL=0.512;    Slow Threshold
TLLD=11;    LLD Threshold
THFA=2.00;    Fast Threshold
DACO=OFF;    DAC Output
DACF=50;    DAC Offset
RTDS=0;    RTD Sensitivity
RTDT=0.00;    RTD Threshold
BLRM=1;    BLR Mode
BLRD=3;    BLR Down Correction
BLRU=0;    BLR Up Correction
AUO1=ICR;    AUX_OUT Selection
PRET=300.0;    Preset Time
PRER=OFF;    Preset Real Time
PREC=OFF;    Preset Counts
PRCL=15;    Preset Counts Low Threshold
PRCH=8191;    Preset Counts High Threshold
HVSE=0;    HV Set
TECS=OFF;    TEC Set
PAPZ=42.0;    Pole-Zero
PAPS=ON;    Preamp 8.5/5 (N/A)
SCOE=FA;    Scope Trigger Edge
SCOT=12;    Scope Trigger Position
SCOG=1;    Digital Scope Gain
MCSL=0;    MCS Low Threshold
MCSH=8191;    MCS High Threshold
MCST=0.01;    MCS Timebase
AUO2=SCA8;    AUX_OUT2 Selection
TPMO=OFF;    Test Pulser On/Off
GPED=RI;    G.P. Counter Edge
GPIN=PILEUP;    G.P. Counter Input
GPME=ON;    G.P. Counter Uses MCA_EN?
GPGA=ON;    G.P. Counter Uses GATE?
GPMC=ON;    G.P. Counter Cleared With MCA Counters?
MCAE=OFF;    MCA/MCS Enable
VOLU=OFF;    Speaker On/Off
CON1=DAC;    Connector 1
CON2=AUXOUT2;    Connector 2
<<DP5 CONFIGURATION END>>
<<DPP STATUS>>
Device Type: PX5
Serial Number: 2522
Firmware: 6.08  Build:  6
FPGA: 6.11
Fast Count: 872112
Slow Count: 840141
GP Count: 17987
Accumulation Time: 300.000000
Real Time: 300.802000
Dead Time: 3.67%
HV Volt: 31V
TEC Temp: 100K
Board Temp: 32°C
<<DPP STATUS END>>

"""