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



datosM11=ascii.read('10-11-2020-NaI-Detector-600s-fuenteBa133.mca', data_start=0)
datosM12=ascii.read('10-11-2020-NaI-Detector-600s-fuenteCo57.mca', data_start=0)
datosM13=ascii.read('10-11-2020-NaI-Detector-600s-fuenteCs137.mca', data_start=0)

g1=len(datosM11)
g2=len(datosM12)
g3=len(datosM13)


cuentasM11=np.zeros(g1)
canalM11=np.zeros(g1)
ejeXM11=np.zeros(g1)
for i in range(0,g1):
    cuentasM11[i]=datosM11[i][0]
    #canal[i]=datos[i][0]
    ejeXM11[i]=i

cuentasM12=np.zeros(g2)
canalM12=np.zeros(g2)
ejeXM12=np.zeros(g2)
for i in range(0,g2):
    cuentasM12[i]=datosM12[i][0]
    #canal[i]=datos[i][0]
    ejeXM12[i]=i

cuentasM13=np.zeros(g3)
canalM13=np.zeros(g3)
ejeXM13=np.zeros(g3)
for i in range(0,g3):
    cuentasM13[i]=datosM13[i][0]
    #canal[i]=datos[i][0]
    ejeXM13[i]=i

    
    
fig, axs=plt.subplots(1,1,sharey=False)


#fig.suptitle('COMPARACIÓN DE REGIÓN COMPTON', fontsize=18)
plt.xlabel('Energía (keV)', fontsize=14)
plt.ylabel('cuentas', fontsize=14)
x=np.linspace(0,8000,10000)
#axs.plot(x,pdf3_3(x),color='purple')  

#x = range(799)
#plt.plot(x,histogram3,linestyle='steps-mid',color='orange')
axs.plot(ejeXM11,cuentasM11,color='black')#133Ba
axs.plot(ejeXM12,cuentasM12,color='purple')#57Co
#axs.plot(ejeXM13,cuentasM13,color='red')

plt.show()
    

"""
################## Ba133 ##############################
<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 599.524000
REAL_TIME - 599.524000
START_TIME - 11/10/2020 11:47:50
SERIAL_NUMBER - 0
<<DATA>>

<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1267;    Fine Gain
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
PRER=600.000;    Preset Real Time
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
Fast Count: 6480
Slow Count: 1630742
GP Count: 6480
Accumulation Time: 599.524000
Real Time: 600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 297.2K
Board Temp: 26°C
<<DPP STATUS END>>


######################### Co57 ##########################


<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 599.524000
REAL_TIME - 599.524000
START_TIME - 11/10/2020 11:08:04
SERIAL_NUMBER - 0
<<DATA>>


<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1267;    Fine Gain
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
PRER=600.000;    Preset Real Time
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
Fast Count: 6335
Slow Count: 447293
GP Count: 6335
Accumulation Time: 599.524000
Real Time: 600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 297.2K
Board Temp: 27°C
<<DPP STATUS END>>

############################## Cs137 ##########################################

<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 599.524000
REAL_TIME - 599.524000
START_TIME - 11/10/2020 12:05:41
SERIAL_NUMBER - 0
<<DATA>>

<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1267;    Fine Gain
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
PRER=600.000;    Preset Real Time
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
Fast Count: 6221
Slow Count: 1254595
GP Count: 6221
Accumulation Time: 599.524000
Real Time: 600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 297.2K
Board Temp: 26°C
<<DPP STATUS END>>

################################# Na22 ##########################
<<PMCA SPECTRUM>>
TAG - live_data
DESCRIPTION - 
GAIN - 2
THRESHOLD - 0
LIVE_MODE - 0
PRESET_TIME - 0
LIVE_TIME - 599.524000
REAL_TIME - 599.524000
START_TIME - 11/10/2020 11:27:17
SERIAL_NUMBER - 0
<<DATA>>


<<END>>
<<DP5 CONFIGURATION>>
RESC=?;    Reset Configuration
CLCK=20;    20MHz/80MHz
TPEA=1.600;    Peaking Time
GAIF=1.1267;    Fine Gain
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
PRER=600.000;    Preset Real Time
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
Fast Count: 235466
Slow Count: 16681632
GP Count: 235466
Accumulation Time: 599.524000
Real Time: 600.000000
Dead Time:       
HV Volt: 750V
TEC Temp: 297.3K
Board Temp: 28\B0C
<<DPP STATUS END>>

"""
