import matplotlib as mpl
import matplotlib as mpl
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

mpl.rcParams['legend.fontsize'] = 12
mpl.rcParams['axes.labelsize'] = 12
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12
mpl.rcParams['text.usetex'] = True
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['mathtext.fontset'] = 'dejavusans'
mpl.rcParams['text.latex.preamble'] = [r'\usepackage{mathrsfs}']
#mpl.rcParams['text.latex.preamble'] = [r'\usepackage{pxfonts}']
mpl.rcParams.update({'font.size': 12})

#import metodos_MC as mt
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import NullFormatter
import scipy.stats as st
from scipy.stats import norm


fig, ax=plt.subplots(1,1,sharey=False)
grid = plt.GridSpec(1, 1, wspace=0.25, hspace=0.2,left=0.1,right=0.98,bottom=0.17,top=0.98)


f1 = np.genfromtxt('gMC_h1_Ge.csv',delimiter=',')
f2 = np.genfromtxt('gMC_h2_Ge.csv',delimiter=',')
f3 = np.genfromtxt('gMC_h3_Ge.csv',delimiter=',')
f4 = np.genfromtxt('gMC_h4_Ge.csv',delimiter=',')
f5 = np.genfromtxt('gMC_h5_Ge.csv',delimiter=',')
f6 = np.genfromtxt('gMC_h6_Ge.csv',delimiter=',')
f7 = np.genfromtxt('gMC_h7_Ge.csv',delimiter=',')
f8 = np.genfromtxt('gMC_h8_Ge.csv',delimiter=',')
f9 = np.genfromtxt('gMC_h9_Ge.csv',delimiter=',')
f10 = np.genfromtxt('gMC_h10_Ge.csv',delimiter=',')
f0 = np.genfromtxt('gMC_h0_Ge.csv',delimiter=',')
y1 = f1[2:,1]
y2 = f2[2:,1]
y3 = f3[2:,1]
y4 = f4[2:,1]
y5 = f5[2:,1]
y6 = f6[2:,1]
y7 = f7[2:,1]
y8 = f8[2:,1]
y9 = f9[2:,1]
y10 = f10[2:,1]
y0 = f0[2:,1]
x1 = np.arange(0,len(y1))
x2 = np.arange(0,len(y2))
x3 = np.arange(0,len(y3))
x4 = np.arange(0,len(y4))
x5 = np.arange(0,len(y5))
x6 = np.arange(0,len(y6))
x7 = np.arange(0,len(y7))
x8 = np.arange(0,len(y8))
x9 = np.arange(0,len(y9))
x10 = np.arange(0,len(y10))
x0 = np.arange(0,len(y0))

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::: CUENTAS :::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# FUNCION ENCARGADA DE DAR EL "FWHM" para el Ge-HP

####################################################
def FWHM_Ge(Eg):
    f0 = 1.24
    f1 = 0.00068
    return f0 + f1 * Eg
##########################################

#FUNCION ENCARGADA DE DAR EL "FWHM" PARA EL NaI

#def FWHM_Ge(Eg):
#    f0=1
#    f1=0.0027
#    f2=1.2
#    return f0 + f1 * Eg + f2 * np.sqrt(Eg)


###############################################

################# 10 cm #######################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y1))
espectro1=np.zeros(len(y1))
for c in k:
    miu1=float(c)
    sigma1= 0.425 * FWHM_Ge(miu1)
    nue_cuen1 = int(y1[c])
    if nue_cuen1>0:
        

        s=norm.rvs(loc=miu1, scale=sigma1, size= nue_cuen1,random_state=123)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro1[k]=espectro1[k]+hist[j]
########################################################################


################# 9 cm #######################



############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y2))
espectro2=np.zeros(len(y2))
for c in k:
    miu2=float(c)
    sigma2= 0.425 * FWHM_Ge(miu2)
    nue_cuen2 = int(y2[c])
    if nue_cuen2>0:

        s=norm.rvs(loc=miu2,scale=sigma2, size= nue_cuen2,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro2[k]=espectro2[k]+hist[j]
########################################################################


################# 8 cm #######################



############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y3))
espectro3=np.zeros(len(y3))
for c in k:
    miu3=float(c)
    sigma3= 0.425 * FWHM_Ge(miu3)
    nue_cuen3 = int(y3[c])
    if nue_cuen3>0:

        s=norm.rvs(loc=miu3,scale=sigma3, size= nue_cuen3,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro3[k]=espectro3[k]+hist[j]
########################################################################


################# 7 cm #######################


############### SE APLICA EL FWHM ####################

k=np.arange(10,len(y4))
espectro4=np.zeros(len(y4))
for c in k:
    miu4=float(c)
    sigma4= 0.425 * FWHM_Ge(miu4)
    nue_cuen4 = int(y4[c])
    if nue_cuen4>0:
        
        s=norm.rvs(loc=miu4,scale=sigma4, size= nue_cuen4,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro4[k]=espectro4[k]+hist[j]
########################################################################





################# 6 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y5))
espectro5=np.zeros(len(y5))
for c in k:
    miu5=float(c)
    sigma5= 0.425 * FWHM_Ge(miu5)
    nue_cuen5 = int(y5[c])
    if nue_cuen5>0:

        s=norm.rvs(loc=miu5,scale=sigma5, size= nue_cuen5,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro5[k]=espectro5[k]+hist[j]
########################################################################




################# 5 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y6))
espectro6=np.zeros(len(y6))
for c in k:
    miu6=float(c)
    sigma6= 0.425 * FWHM_Ge(miu6)
    nue_cuen6 = int(y6[c])
    if nue_cuen6>0:

        s=norm.rvs(loc=miu6,scale=sigma6, size= nue_cuen6,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro6[k]=espectro6[k]+hist[j]
########################################################################






################# 4 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y7))
espectro7=np.zeros(len(y7))
for c in k:
    miu7=float(c)
    sigma7= 0.425 * FWHM_Ge(miu7)
    nue_cuen7 = int(y7[c])
    if nue_cuen7>0:
        
        s=norm.rvs(loc=miu7,scale=sigma7, size= nue_cuen7,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro7[k]=espectro7[k]+hist[j]
########################################################################





################# 3 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y8))
espectro8=np.zeros(len(y8))
for c in k:
    miu8=float(c)
    sigma8= 0.425 * FWHM_Ge(miu8)
    nue_cuen8 = int(y8[c])
    if nue_cuen8>0:
        
        s=norm.rvs(loc=miu8,scale=sigma8, size= nue_cuen8,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro8[k]=espectro8[k]+hist[j]
########################################################################





################# 2 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y9))
espectro9=np.zeros(len(y9))
for c in k:
    miu9=float(c)
    sigma9= 0.425 * FWHM_Ge(miu9)
    nue_cuen9 = int(y9[c])
    if nue_cuen9>0:

        s=norm.rvs(loc=miu9,scale=sigma9, size= nue_cuen9,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro9[k]=espectro9[k]+hist[j]
########################################################################





################# 1 cm #######################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y10))
espectro10=np.zeros(len(y10))
for c in k:
    miu10=float(c)
    sigma10= 0.425 * FWHM_Ge(miu10)
    nue_cuen10 = int(y10[c])
    if nue_cuen10>0:

        s=norm.rvs(loc=miu10,scale=sigma10, size= nue_cuen10,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro10[k]=espectro10[k]+hist[j]
########################################################################




################# 0.0 cm #######################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y0))
espectro0=np.zeros(len(y0))
for c in k:
    miu0=float(c)
    sigma0= 0.425 * FWHM_Ge(miu0)
    nue_cuen0 = int(y0[c])
    if nue_cuen0>0:
        
        s=norm.rvs(loc=miu0,scale=sigma0, size= nue_cuen0,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro0[k]=espectro0[k]+hist[j]
            
########################################################################
#################### AJUSTES A LOS FOTOPICOS  ##########################
########################################################################

max1=int(max(espectro1[657:665]))


for i in range(657,665):
    if espectro1[i]==max1:
        mu1=x1[i]

sig1= 0.425 * FWHM_Ge(mu1)

cuentas1=espectro1[657:665]
eje1=x1[657:665]

a0=1
a1=1
def gaussi1(t,max1,mu1,sig1,a1,a0):
	return max1*(np.exp(-((mu1-t)**2)/((math.sqrt(2)*sig1)**2)))+((a1*t)+a0)

popt_gaussi1, pcov=curve_fit(gaussi1, eje1, cuentas1, p0=[max1,mu1,sig1,a1,a0])

errores1= np.sqrt(np.diag(pcov))


max1=popt_gaussi1[0]
mu1=popt_gaussi1[1]
sig1=popt_gaussi1[2]
a1=popt_gaussi1[3]
a0=popt_gaussi1[4]


print('nuevas cuentas 1')
cuentas1=math.sqrt(2*math.pi)*max1*sig1
print(cuentas1)


errores_max1=errores1[0]
errores_sig1=errores1[2]

incer1=cuentas1*math.sqrt((errores_max1/max1)**2+(errores_sig1/sig1)**2)

print('incertidumbre en las cuentas!!!')
print(incer1)

print ("------------------------------------")

######################################################################
######################################################################

max2=int(max(espectro2[657:665]))


for i in range(657,665):
    if espectro2[i]==max2:
        mu2=x2[i]

sig2= 0.425 * FWHM_Ge(mu2)

cuentas2=espectro2[657:665]
eje2=x2[657:665]

a0_2=1
a1_2=1
def gaussi2(t,max2,mu2,sig2,a1_2,a0_2):
	return max2*(np.exp(-((mu2-t)**2)/((math.sqrt(2)*sig2)**2)))+((a1_2*t)+a0_2)

popt_gaussi2, pcov2=curve_fit(gaussi2, eje2, cuentas2, p0=[max2,mu2,sig2,a1_2,a0_2])

errores2= np.sqrt(np.diag(pcov2))


max2=popt_gaussi2[0]
mu2=popt_gaussi2[1]
sig2=popt_gaussi2[2]
a1_2=popt_gaussi2[3]
a0_2=popt_gaussi2[4]

print('nuevas cuentas 2')
cuentas2=math.sqrt(2*math.pi)*max2*sig2
print(cuentas2)


errores_max2=errores2[0]
errores_sig2=errores2[2]

incer2=cuentas2*math.sqrt((errores_max2/max2)**2+(errores_sig2/sig2)**2)

print('incertidumbre en las cuentas!!!')
print(incer2)

print ("------------------------------------")



######################################################################
######################################################################

max3=int(max(espectro3[657:665]))


for i in range(657,665):
    if espectro3[i]==max3:
        mu3=x3[i]

sig3= 0.425 * FWHM_Ge(mu3)

cuentas3=espectro3[657:665]
eje3=x3[657:665]

a0_3=1
a1_3=1
def gaussi3(t,max3,mu3,sig3,a1_3,a0_3):
	return max3*(np.exp(-((mu3-t)**2)/((math.sqrt(2)*sig3)**2)))+((a1_3*t)+a0_3)

popt_gaussi3, pcov3=curve_fit(gaussi3, eje3, cuentas3, p0=[max3,mu3,sig3,a1_3,a0_3])

errores3= np.sqrt(np.diag(pcov3))


max3=popt_gaussi3[0]
mu3=popt_gaussi3[1]
sig3=popt_gaussi3[2]
a1_3=popt_gaussi3[3]
a0_3=popt_gaussi3[4]

print('nuevas cuentas 3')
cuentas3=math.sqrt(2*math.pi)*max3*sig3
print(cuentas3)


errores_max3=errores3[0]
errores_sig3=errores3[2]

incer3=cuentas3*math.sqrt((errores_max3/max3)**2+(errores_sig3/sig3)**2)

print('incertidumbre en las cuentas!!!')
print(incer3)

print ("------------------------------------")



########################################################################
########################################################################

max4=int(max(espectro4[657:665]))


for i in range(657,665):
    if espectro4[i]==max4:
        mu4=x4[i]

sig4= 0.425 * FWHM_Ge(mu4)

cuentas4=espectro4[657:665]
eje4=x4[657:665]

a0_4=1
a1_4=1
def gaussi4(t,max4,mu4,sig4,a1_4,a0_4):
	return max4*(np.exp(-((mu4-t)**2)/((math.sqrt(2)*sig4)**2)))+((a1_4*t)+a0_4)

popt_gaussi4, pcov4=curve_fit(gaussi4, eje4, cuentas4, p0=[max4,mu4,sig4,a1_4,a0_4])

errores4= np.sqrt(np.diag(pcov4))



max4=popt_gaussi4[0]
mu4=popt_gaussi4[1]
sig4=popt_gaussi4[2]
a1_4=popt_gaussi4[3]
a0_4=popt_gaussi4[4]

print('nuevas cuentas 4')
cuentas4=math.sqrt(2*math.pi)*max4*sig4
print(cuentas4)


errores_max4=errores4[0]
errores_sig4=errores4[2]

incer4=cuentas4*math.sqrt((errores_max4/max4)**2+(errores_sig4/sig4)**2)

print('incertidumbre en las cuentas!!!')
print(incer4)

print ("------------------------------------")
######################################################################
######################################################################

max5=int(max(espectro5[657:665]))


for i in range(657,665):
    if espectro5[i]==max5:
        mu5=x5[i]


sig5= 0.425 * FWHM_Ge(mu5)

cuentas5=espectro5[657:665]
eje5=x5[657:665]

a0_5=1
a1_5=1
def gaussi5(t,max5,mu5,sig5,a1_5,a0_5):
	return max5*(np.exp(-((mu5-t)**2)/((math.sqrt(2)*sig5)**2)))+((a1_5*t)+a0_5)

popt_gaussi5, pcov5=curve_fit(gaussi5, eje5, cuentas5, p0=[max5,mu5,sig5,a1_5,a0_5])

errores5= np.sqrt(np.diag(pcov5))



max5=popt_gaussi5[0]
mu5=popt_gaussi5[1]
sig5=popt_gaussi5[2]
a1_5=popt_gaussi5[3]
a0_5=popt_gaussi5[4]

print('nuevas cuentas 5')
cuentas5=math.sqrt(2*math.pi)*max5*sig5
print(cuentas5)


errores_max5=errores5[0]
errores_sig5=errores5[2]

incer5=cuentas5*math.sqrt((errores_max5/max5)**2+(errores_sig5/sig5)**2)

print('incertidumbre en las cuentas!!!')
print(incer5)

print ("------------------------------------")



######################################################################
######################################################################


max6=int(max(espectro6[657:665]))


for i in range(657,665):
    if espectro6[i]==max6:
        mu6=x6[i]

sig6= 0.425 * FWHM_Ge(mu6)

cuentas6=espectro6[657:665]
eje6=x6[657:665]

a0_6=1
a1_6=1
def gaussi6(t,max6,mu6,sig6,a1_6,a0_6):
	return max6*(np.exp(-((mu6-t)**2)/((math.sqrt(2)*sig6)**2)))+((a1_6*t)+a0_6)

popt_gaussi6, pcov6=curve_fit(gaussi6, eje6, cuentas6, p0=[max6,mu6,sig6,a1_6,a0_6])

errores6= np.sqrt(np.diag(pcov6))


max6=popt_gaussi6[0]
mu6=popt_gaussi6[1]
sig6=popt_gaussi6[2]
a1_6=popt_gaussi6[3]
a0_6=popt_gaussi6[4]


print('nuevas cuentas 6')
cuentas6=math.sqrt(2*math.pi)*max6*sig6
print(cuentas6)


errores_max6=errores6[0]
errores_sig6=errores6[2]

incer6=cuentas6*math.sqrt((errores_max6/max6)**2+(errores_sig6/sig6)**2)

print('incertidumbre en las cuentas!!!')
print(incer6)

print ("------------------------------------")


######################################################################
######################################################################

max7=int(max(espectro7[657:665]))


for i in range(657,665):
    if espectro7[i]==max7:
        mu7=x7[i]

sig7= 0.425 * FWHM_Ge(mu7)

cuentas7=espectro7[657:665]
eje7=x7[657:665]

a0_7=1
a1_7=1
def gaussi7(t,max7,mu7,sig7,a1_7,a0_7):
	return max7*(np.exp(-((mu7-t)**2)/((math.sqrt(2)*sig7)**2)))+((a1_7*t)+a0_7)

popt_gaussi7, pcov7=curve_fit(gaussi7, eje7, cuentas7, p0=[max7,mu7,sig7,a1_7,a0_7])

errores7= np.sqrt(np.diag(pcov7))


max7=popt_gaussi7[0]
mu7=popt_gaussi7[1]
sig7=popt_gaussi7[2]
a1_7=popt_gaussi7[3]
a0_7=popt_gaussi7[4]


print('nuevas cuentas 7')
cuentas7=math.sqrt(2*math.pi)*max7*sig7
print(cuentas7)


errores_max7=errores7[0]
errores_sig7=errores7[2]

incer7=cuentas7*math.sqrt((errores_max7/max7)**2+(errores_sig7/sig7)**2)

print('incertidumbre en las cuentas!!!')
print(incer7)

print ("------------------------------------")


######################################################################
######################################################################

max8=int(max(espectro8[657:665]))


for i in range(657,665):
    if espectro8[i]==max8:
        mu8=x8[i]

sig8= 0.425 * FWHM_Ge(mu8)

cuentas8=espectro8[657:665]
eje8=x8[657:665]

a0_8=1
a1_8=1
def gaussi8(t,max8,mu8,sig8,a1_8,a0_8):
	return max8*(np.exp(-((mu8-t)**2)/((math.sqrt(2)*sig8)**2)))+((a1_8*t)+a0_8)

popt_gaussi8, pcov8=curve_fit(gaussi8, eje8, cuentas8, p0=[max8,mu8,sig8,a1_8,a0_8])

errores8= np.sqrt(np.diag(pcov8))


max8=popt_gaussi8[0]
mu8=popt_gaussi8[1]
sig8=popt_gaussi8[2]
a1_8=popt_gaussi8[3]
a0_8=popt_gaussi8[4]


print('nuevas cuentas 8')
cuentas8=math.sqrt(2*math.pi)*max8*sig8
print(cuentas8)


errores_max8=errores8[0]
errores_sig8=errores8[2]

incer8=cuentas8*math.sqrt((errores_max8/max8)**2+(errores_sig8/sig8)**2)

print('incertidumbre en las cuentas!!!')
print(incer8)

print ("------------------------------------")


######################################################################
######################################################################

max9=int(max(espectro9[657:665]))


for i in range(657,665):
    if espectro9[i]==max9:
        mu9=x9[i]

sig9= 0.425 * FWHM_Ge(mu9)

cuentas9=espectro9[657:665]
eje9=x9[657:665]

a0_9=1
a1_9=1
def gaussi9(t,max9,mu9,sig9,a1_9,a0_9):
	return max9*(np.exp(-((mu9-t)**2)/((math.sqrt(2)*sig9)**2)))+((a1_9*t)+a0_9)

popt_gaussi9, pcov9=curve_fit(gaussi9, eje9, cuentas9, p0=[max9,mu9,sig9,a1_9,a0_9])

errores9= np.sqrt(np.diag(pcov9))



max9=popt_gaussi9[0]
mu9=popt_gaussi9[1]
sig9=popt_gaussi9[2]
a1_9=popt_gaussi9[3]
a0_9=popt_gaussi9[4]

print('nuevas cuentas 9')
cuentas9=math.sqrt(2*math.pi)*max9*sig9
print(cuentas9)


errores_max9=errores9[0]
errores_sig9=errores9[2]

incer9=cuentas9*math.sqrt((errores_max9/max9)**2+(errores_sig9/sig9)**2)

print('incertidumbre en las cuentas!!!')
print(incer9)

print ("------------------------------------")

######################################################################
######################################################################

max10=int(max(espectro10[657:665]))


for i in range(657,665):
    if espectro10[i]==max10:
        mu10=x10[i]

sig10= 0.425 * FWHM_Ge(mu10)

cuentas10=espectro10[657:665]
eje10=x10[657:665]

a0_10=1
a1_10=1
def gaussi10(t,max10,mu10,sig10,a1_10,a0_10):
	return max10*(np.exp(-((mu10-t)**2)/((math.sqrt(2)*sig10)**2)))+((a1_10*t)+a0_10)

popt_gaussi10, pcov10=curve_fit(gaussi10, eje10, cuentas10, p0=[max10,mu10,sig10,a1_10,a0_10])

errores10= np.sqrt(np.diag(pcov10))


max10=popt_gaussi10[0]
mu10=popt_gaussi10[1]
sig10=popt_gaussi10[2]
a1_10=popt_gaussi10[3]
a0_10=popt_gaussi10[4]

print('nuevas cuentas 10')
cuentas10=math.sqrt(2*math.pi)*max10*sig10
print(cuentas10)


errores_max10=errores10[0]
errores_sig10=errores10[2]

incer10=cuentas10*math.sqrt((errores_max10/max10)**2+(errores_sig10/sig10)**2)

print('incertidumbre en las cuentas!!!')
print(incer10)

print ("------------------------------------")



####################################################################
####################################################################

max0=int(max(espectro0[657:665]))


for i in range(657,665):
    if espectro0[i]==max0:
        mu0=x0[i]

sig0= 0.425 * FWHM_Ge(mu0)

cuentas0=espectro0[657:665]
eje0=x0[657:665]

a0_0=1
a1_0=1
def gaussi0(t,max0,mu0,sig0,a1_0,a0_0):
	return max0*(np.exp(-((mu0-t)**2)/((math.sqrt(2)*sig0)**2)))+((a1_0*t)+a0_0)

popt_gaussi0, pcov0=curve_fit(gaussi0, eje0, cuentas0, p0=[max0,mu0,sig0,a1_0,a0_0])

errores0= np.sqrt(np.diag(pcov0))


max0=popt_gaussi0[0]
mu0=popt_gaussi0[1]
sig0=popt_gaussi0[2]
a1_0=popt_gaussi0[3]
a0_0=popt_gaussi0[4]

print('nuevas cuentas 11')
cuentas0=math.sqrt(2*math.pi)*max0*sig0
print(cuentas0)


errores_max0=errores0[0]
errores_sig0=errores0[2]

incer0=cuentas0*math.sqrt((errores_max0/max0)**2+(errores_sig0/sig0)**2)

print('incertidumbre en las cuentas!!!')
print(incer0)

print ("------------------------------------")

###################################################################################################
###################################################################################################
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::: GRAFICAS DE LOS AJUSTES ::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""
ax.plot(x1,gaussi1(x1,max1,mu1,sig1,a1,a0),drawstyle='steps-mid',label='0.2 cm',color='purple')
ax.plot(x2,gaussi1(x2,max2,mu2,sig2,a1_2,a0_2),drawstyle='steps-mid',label='0.2 cm',color='purple')
ax.plot(x3,gaussi1(x3,max3,mu3,sig3,a1_3,a0_3),drawstyle='steps-mid',label='0.2 cm',color='purple')
ax.plot(x4,gaussi1(x4,max4,mu4,sig4,a1_4,a0_4),drawstyle='steps-mid',label='0.2 cm',color='purple')
ax.plot(x5,gaussi5(x5,max5,mu5,sig5,a1_5,a0_5),drawstyle='steps-mid',label='0.2 cm',color='purple')
ax.plot(x6,gaussi6(x6,max6,mu6,sig6,a1_6,a0_6),drawstyle='steps-mid',label='0.2 cm',color='purple')
ax.plot(x7,gaussi7(x7,max7,mu7,sig7,a1_7,a0_7),drawstyle='steps-mid',label='0.2 cm',color='purple')
ax.plot(x8,gaussi1(x8,max8,mu8,sig8,a1_8,a0_8),drawstyle='steps-mid',label='0.2 cm',color='purple')
ax.plot(x9,gaussi9(x9,max9,mu9,sig9,a1_9,a0_9),drawstyle='steps-mid',label='0.2 cm',color='purple')
ax.plot(x10,gaussi10(x10,max10,mu10,sig10,a1_10,a0_10),drawstyle='steps-mid',label='0.2 cm',color='purple')
ax.plot(x11,gaussi10(x11,max11,mu11,sig11,a1_11,a0_11),drawstyle='steps-mid',label='0.2 cm',color='purple')
"""
########################################################################
########################################################################
########################################################################

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::: Graficas de la simulación ::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
ax.plot(x0,espectro0,drawstyle='steps-mid',label='0.0 cm', color= 'lime')
ax.plot(x1,espectro1,drawstyle='steps-mid',label='1.0 cm')
ax.plot(x2,espectro2,drawstyle='steps-mid',label='2.0 cm')
ax.plot(x3,espectro3,drawstyle='steps-mid',label='3.0 cm')
ax.plot(x4,espectro4,drawstyle='steps-mid',label='4.0 cm')
ax.plot(x5,espectro5,drawstyle='steps-mid',label='5.0 cm')
ax.plot(x6,espectro6,drawstyle='steps-mid',label='6.0 cm')
ax.plot(x7,espectro7,drawstyle='steps-mid',label='7.0 cm')
ax.plot(x8,espectro8,drawstyle='steps-mid',label='8.0 cm')
ax.plot(x9,espectro9,drawstyle='steps-mid',label='9.0 cm')
ax.plot(x10,espectro10,drawstyle='steps-mid',label='10.0 cm')



ax.set_xlabel(r'$E_\gamma$ (keV)', size=23)
#ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('cuentas/keV', size=23)
#plt.xlim(0,1400)
#plt.ylim(0,7000)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
leg=plt.legend(loc=(0.6,0.35),prop={'size': 14})
for legobj in leg.legendHandles: #tamaño de la leyenda
    legobj.set_linewidth(5.0) #tamaño de la leyenda
plt.show()
"""
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################

#INTENSIDADES Y SUS ERRORES RESPECTIVOS

intensidades=[cuentas1, cuentas2, cuentas3, cuentas4, cuentas5,  cuentas7, cuentas8, cuentas9, cuentas10,cuentas11]
int_max=max(intensidades)
#intensidades=intensidades/int_max
errores_inten=[incer1,incer2,incer3, incer4, incer5, incer7, incer8,incer9, incer10,incer11]
#errores_inten=errores_inten/int_max

#GROSORES
grosor=[0.0, 0.2, 0.4, 0.6, 0.8, 1.2, 1.4, 1.6, 1.8, 2.0]


#REGRESION



mu_T=0.6
n0=max(intensidades)

def intensidad(grosor,n0,mu_T):
    return n0 * (np.exp(mu_T * grosor))


popt_retro,pcov_retro=curve_fit(intensidad, grosor, intensidades,p0=[n0,mu_T], sigma=errores_inten)


perror=np.sqrt(np.diag(pcov_retro))
print ("error")
print (perror)
print ("-----------------")
print ("mu_T")
print (popt_retro)

mu_T=popt_retro[1]
n0=popt_retro[0]

fig2, axs=plt.subplots(1,1,sharey=False)
axs.errorbar(grosor,intensidades,yerr=errores_inten,xerr=None,fmt='.',color='purple', markersize=12,label='experimento')

axs.set_xlabel(r'$Grosor$ (cm)')
axs.set_ylabel('intensidad (cuentas)')
x=np.linspace(0,2,10000)
axs.plot(x,intensidad(x,n0,mu_T), label='ajuste',color='red')
plt.yscale('log')
leg=axs.legend(loc="center right")
for legobj in leg.legendHandles: #tamaño de la leyenda
    legobj.set_linewidth(2.0) #tamaño de la leyenda
plt.show()

"""
