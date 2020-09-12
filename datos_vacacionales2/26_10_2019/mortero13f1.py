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



datos1FM13=ascii.read('26-10-2019-PX5-HPGe-1200s-fuentes1-13.MCA', data_start=0)

g=len(datos1FM13)

cuentas1FM13=np.zeros(g)
#canalM11=np.zeros(g)
ejeX1FM13=np.zeros(g)
for i in range(0,g):
    cuentas1FM13[i]=datos1FM13[i][0]
    #canal[i]=datos[i][0]
    ejeX1FM13[i]=i




#########################################################
#################### 133Ba-80.99keV ###############
#########################################################

M1=int(max(cuentas1FM13[140:200]))


for i in range(140,200):
	if cuentas1FM13[i]==M1:
		miu1=ejeX1FM13[i]

sigma1=math.sqrt(miu1)


cuentas1=cuentas1FM13[140:200]
eje1=ejeX1FM13[140:200]

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
#########################################################


M2=int(max(cuentas1FM13[240:263]))


for i in range(240,263):
	if cuentas1FM13[i]==M2:
		miu2=ejeX1FM13[i]

sigma2=math.sqrt(miu2)


cuentas2=cuentas1FM13[240:263]
eje2=ejeX1FM13[240:263]


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
#########################################################

M3=int(max(cuentas1FM13[270:291]))


for i in range(278,291):
	if cuentas1FM13[i]==M3:
		miu3=ejeX1FM13[i]

sigma3=math.sqrt(miu3)


cuentas3=cuentas1FM13[278:291]
eje3=ejeX1FM13[278:291]



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



#########################################################
#########################################################


M4=int(max(cuentas1FM13[620:640]))


for i in range(620,640):
	if cuentas1FM13[i]==M4:
		miu4=ejeX1FM13[i]

sigma4=math.sqrt(miu4)


cuentas4=cuentas1FM13[620:640]
eje4=ejeX1FM13[620:640]

a04=1
a14=1
sigma4=1.5
def gaussi4(x,M4,miu4,sigma4,a14,a04):
	return M4*(np.exp(-((miu4-x)**2)/((math.sqrt(2)*sigma4)**2)))+((a14*x)+a04)

popt_gaussi4, pcov4=curve_fit(gaussi4, eje4, cuentas4, p0=[M4,miu4,sigma4,a14,a04])

errores4= np.sqrt(np.diag(pcov4))

print(errores4)


M4=popt_gaussi4[0]
miu4=popt_gaussi4[1]
sigma4=popt_gaussi4[2]
a14=popt_gaussi4[3]
a04=popt_gaussi4[4]

print('nuevas cuentas4')
nue_cuen4=math.sqrt(2*math.pi)*M4*sigma4
print(nue_cuen4)
print(M4,'----',sigma4)


erroresM4=errores4[0]
erroressigma4=errores4[2]

print(erroresM4)
print(erroressigma4)
incer4=nue_cuen4*math.sqrt((erroresM4/M4)**2+(erroressigma4/sigma4)**2)

print('incertidumbre en las cuentas !!!')
print(incer4)




########################################################
########################################################
M5=int(max(cuentas1FM13[734:747]))


for i in range(734,747):
	if cuentas1FM13[i]==M5:
		miu5=ejeX1FM13[i]

sigma5=math.sqrt(miu5)


cuentas5=cuentas1FM13[734:747]
eje5=ejeX1FM13[734:747]


a05=1
a15=1
sigma5=1.5
def gaussi5(x,M5,miu5,sigma5,a15,a05):
	return M5*(np.exp(-((miu5-x)**2)/((math.sqrt(2)*sigma5)**2)))+((a15*x)+a05)

popt_gaussi5, pcov5=curve_fit(gaussi5, eje5, cuentas5, p0=[M5,miu5,sigma5,a15,a05])

errores5= np.sqrt(np.diag(pcov5))

print(errores5)


M5=popt_gaussi5[0]
miu5=popt_gaussi5[1]
sigma5=popt_gaussi5[2]
a15=popt_gaussi5[3]
a05=popt_gaussi5[4]

print('nuevas cuentas5')
nue_cuen5=math.sqrt(2*math.pi)*M5*sigma5
print(nue_cuen5)
print(M5,'----',sigma5)


erroresM5=errores5[0]
erroressigma5=errores5[2]

print(erroresM5)
print(erroressigma5)
incer5=nue_cuen5*math.sqrt((erroresM5/M5)**2+(erroressigma5/sigma5)**2)

print('incertidumbre en las cuentas!!!')
print(incer5)



########################################################
########################################################


M6=int(max(cuentas1FM13[780:820]))


for i in range(780,820):
	if cuentas1FM13[i]==M6:
		miu6=ejeX1FM13[i]

sigma6=math.sqrt(miu6)


cuentas6=cuentas1FM13[780:820]
eje6=ejeX1FM13[780:820]



a06=1
a16=1
sigma6=1.5
def gaussi6(x,M6,miu6,sigma6,a16,a06):
	return M6*(np.exp(-((miu6-x)**2)/((math.sqrt(2)*sigma6)**2)))+((a16*x)+a06)

popt_gaussi6, pcov6=curve_fit(gaussi6, eje6, cuentas6, p0=[M6,miu6,sigma6,a16,a06])

errores6= np.sqrt(np.diag(pcov6))

print(errores6)


M6=popt_gaussi6[0]
miu6=popt_gaussi6[1]
sigma6=popt_gaussi6[2]
a16=popt_gaussi6[3]
a06=popt_gaussi6[4]

print('nuevas cuentas6')
nue_cuen6=math.sqrt(2*math.pi)*M6*sigma6
print(nue_cuen6)
print(M6,'----',sigma6)


erroresM6=errores6[0]
erroressigma6=errores6[2]

print(erroresM6)
print(erroressigma6)
incer6=nue_cuen6*math.sqrt((erroresM6/M6)**2+(erroressigma6/sigma6)**2)

print('incertidumbre en las cuentas!!!')
print(incer6)



########################################################
########################################################

M7=int(max(cuentas1FM13[2425:2450]))


for i in range(2425,2450):
	if cuentas1FM13[i]==M7:
		miu7=ejeX1FM13[i]

sigma7=math.sqrt(miu7)


cuentas7=cuentas1FM13[2425:2450]
eje7=ejeX1FM13[2425:2450]



a07=1
a17=1
sigma7=1.5
def gaussi7(x,M7,miu7,sigma7,a17,a07):
	return M7*(np.exp(-((miu7-x)**2)/((math.sqrt(2)*sigma7)**2)))+((a17*x)+a07)

popt_gaussi7, pcov7=curve_fit(gaussi7, eje7, cuentas7, p0=[M7,miu7,sigma7,a17,a07])

errores7= np.sqrt(np.diag(pcov7))

print(errores7)


M7=popt_gaussi7[0]
miu7=popt_gaussi7[1]
sigma7=popt_gaussi7[2]
a17=popt_gaussi7[3]
a07=popt_gaussi7[4]

print('nuevas cuentas7')
nue_cuen7=math.sqrt(2*math.pi)*M7*sigma7
print(nue_cuen7)
print(M7,'----',sigma7)


erroresM7=errores7[0]
erroressigma7=errores7[2]

print(erroresM7)
print(erroressigma7)
incer7=nue_cuen7*math.sqrt((erroresM7/M7)**2+(erroressigma7/sigma7)**2)

print('incertidumbre en las cuentas!!!')
print(incer7)




#########################################################
#########################################################

M8=int(max(cuentas1FM13[2760:2780]))


for i in range(2760,2780):
	if cuentas1FM13[i]==M8:
		miu8=ejeX1FM13[i]

sigma8=math.sqrt(miu8)


cuentas8=cuentas1FM13[2760:2780]
eje8=ejeX1FM13[2760:2780]



a08=1
a18=1
sigma8=1.5
def gaussi8(x,M8,miu8,sigma8,a18,a08):
	return M8*(np.exp(-((miu8-x)**2)/((math.sqrt(2)*sigma8)**2)))+((a18*x)+a08)

popt_gaussi8, pcov8=curve_fit(gaussi8, eje8, cuentas8, p0=[M8,miu8,sigma8,a18,a08])

errores8= np.sqrt(np.diag(pcov8))

print(errores8)


M8=popt_gaussi8[0]
miu8=popt_gaussi8[1]
sigma8=popt_gaussi8[2]
a18=popt_gaussi8[3]
a08=popt_gaussi8[4]

print('nuevas cuentas8')
nue_cuen8=math.sqrt(2*math.pi)*M8*sigma8
print(nue_cuen8)
print(M8,'----',sigma8)


erroresM8=errores8[0]
erroressigma8=errores8[2]

print(erroresM8)
print(erroressigma8)
incer8=nue_cuen8*math.sqrt((erroresM8/M8)**2+(erroressigma8/sigma8)**2)

print('incertidumbre en las cuentas!!!')
print(incer8)




#########################################################






fig, axs=plt.subplots(1,1,sharey=False)

fig.suptitle('  ', fontsize=18)
plt.xlabel('CANAL ', fontsize=20)
plt.ylabel('CUENTAS', fontsize=20)
x=np.linspace(0,8000,10000)

axs.plot(x,gaussi4(x,M1,miu1,sigma1,a1,a0),color='black')
axs.plot(x,gaussi4(x,M2,miu2,sigma2,a12,a02),color='purple')
axs.plot(x,gaussi4(x,M3,miu3,sigma3,a13,a03),color='green')
axs.plot(x,gaussi4(x,M4,miu4,sigma4,a14,a04),color='pink')
axs.plot(x,gaussi4(x,M5,miu5,sigma5,a15,a05),color='blue')
axs.plot(x,gaussi4(x,M6,miu6,sigma6,a16,a06),color='gray')
axs.plot(x,gaussi4(x,M7,miu7,sigma7,a17,a07),color='yellow')
axs.plot(x,gaussi4(x,M8,miu8,sigma8,a18,a08))



 
axs.step(eje2,cuentas2,color='red')
axs.step(eje3,cuentas3,color='red')
axs.step(eje7,cuentas7,color='red')
axs.step(eje8,cuentas8,color='red')
axs.step(eje1,cuentas1,color='red')
axs.step(eje4,cuentas4,color='red')
axs.step(eje5,cuentas5,color='red')
axs.step(eje6,cuentas6,color='red')
plt.show()






"""
<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 5
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 1200.000000
REAL_TIME - 1200.000000
START_TIME - 10/26/2019 14:48:57
SERIAL_NUMBER - 0
<<DATA>>
--------------------------------------------------
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
PRET=1200.0;    Preset Time
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
Fast Count: 463081
Slow Count: 465713
GP Count: 1513
Accumulation Time: 1200.000000
Real Time: 1203.215000
Dead Time:       
HV Volt: 31V
TEC Temp: 100K
Board Temp: 34°C
<<DPP STATUS END>>

"""