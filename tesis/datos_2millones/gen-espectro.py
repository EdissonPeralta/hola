import matplotlib as mpl
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


#fig = plt.figure(figsize=(mt.cm2inch(18.0),mt.cm2inch(10.0)))
fig, axs=plt.subplots(1,1,sharey=False)
grid = plt.GridSpec(1, 1, wspace=0.25, hspace=0.2,left=0.1,right=0.98,bottom=0.17,top=0.98)


ax =fig.add_subplot(grid[0,0])
ax.tick_params(bottom=True,top=True,right=True,direction='in',which='both')

f = np.genfromtxt('gMC_h11_Ge.csv',delimiter=',')
f1 = np.genfromtxt('gMC_h10_Ge.csv',delimiter=',')
f2 = np.genfromtxt('gMC_h9_Ge.csv',delimiter=',')
f3 = np.genfromtxt('gMC_h8_Ge.csv',delimiter=',')
f4 = np.genfromtxt('gMC_h7_Ge.csv',delimiter=',')
f5 = np.genfromtxt('gMC_h6_Ge.csv',delimiter=',')
f6 = np.genfromtxt('gMC_h5_Ge.csv',delimiter=',')
f7 = np.genfromtxt('gMC_h4_Ge.csv',delimiter=',')
f8 = np.genfromtxt('gMC_h3_Ge.csv',delimiter=',')
f9 = np.genfromtxt('gMC_h2_Ge.csv',delimiter=',')
f10 = np.genfromtxt('gMC_h1_Ge.csv',delimiter=',')
y = f[2:,1]
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
x = np.arange(0,len(y))
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
k=np.arange(10,len(y))
espectro=np.zeros(len(y))
for c in k:
    miu10=float(c)
    sigma10= 0.425 * FWHM_Ge(miu10)
    nue_cuen10 = int(y[c])
    if nue_cuen10>0:
        

        s=norm.rvs(loc=miu10, scale=sigma10, size= nue_cuen10,random_state=123)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro[k]=espectro[k]+hist[j]
########################################################################


################# 9 cm #######################



############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y1))
espectro9=np.zeros(len(y1))
for c in k:
    miu9=float(c)
    sigma9= 0.425 * FWHM_Ge(miu9)
    nue_cuen9 = int(y1[c])
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


################# 8 cm #######################



############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y2))
espectro8=np.zeros(len(y2))
for c in k:
    miu8=float(c)
    sigma8= 0.425 * FWHM_Ge(miu8)
    nue_cuen8 = int(y2[c])
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


################# 7 cm #######################


############### SE APLICA EL FWHM ####################

k=np.arange(10,len(y3))
espectro7=np.zeros(len(y3))
for c in k:
    miu7=float(c)
    sigma7= 0.425 * FWHM_Ge(miu7)
    nue_cuen7 = int(y3[c])
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





################# 6 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y4))
espectro6=np.zeros(len(y4))
for c in k:
    miu6=float(c)
    sigma6= 0.425 * FWHM_Ge(miu6)
    nue_cuen6 = int(y4[c])
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




################# 5 cm #######################


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






################# 4 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y6))
espectro4=np.zeros(len(y6))
for c in k:
    miu4=float(c)
    sigma4= 0.425 * FWHM_Ge(miu4)
    nue_cuen4 = int(y6[c])
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





################# 3 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y7))
espectro3=np.zeros(len(y7))
for c in k:
    miu3=float(c)
    sigma3= 0.425 * FWHM_Ge(miu3)
    nue_cuen3 = int(y7[c])
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





################# 2 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y8))
espectro2=np.zeros(len(y8))
for c in k:
    miu2=float(c)
    sigma2= 0.425 * FWHM_Ge(miu2)
    nue_cuen2 = int(y8[c])
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





################# 1 cm #######################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y9))
espectro1=np.zeros(len(y9))
for c in k:
    miu1=float(c)
    sigma1= 0.425 * FWHM_Ge(miu1)
    nue_cuen1 = int(y9[c])
    if nue_cuen1>0:

        s=norm.rvs(loc=miu1,scale=sigma1, size= nue_cuen1,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro1[k]=espectro1[k]+hist[j]
########################################################################




################# 0.0 cm #######################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y10))
espectro0=np.zeros(len(y10))
for c in k:
    miu0=float(c)
    sigma0= 0.425 * FWHM_Ge(miu0)
    nue_cuen0 = int(y10[c])
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



#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::: Graficas :::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
ax.plot(x,espectro,drawstyle='steps-mid')
ax.plot(x1,espectro1,drawstyle='steps-mid')
ax.plot(x2,espectro2,drawstyle='steps-mid')
ax.plot(x3,espectro3,drawstyle='steps-mid')
ax.plot(x4,espectro4,drawstyle='steps-mid')
ax.plot(x5,espectro5,drawstyle='steps-mid')
ax.plot(x6,espectro6,drawstyle='steps-mid')
ax.plot(x7,espectro7,drawstyle='steps-mid')
ax.plot(x8,espectro8,drawstyle='steps-mid')
ax.plot(x9,espectro9,drawstyle='steps-mid')
ax.plot(x10,espectro0,drawstyle='steps-mid')
ax.set_xlabel(r'$E_\gamma$ (keV)')
#ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('cuentas/keV')
plt.xlim(10,700)
plt.ylim(0,32000)
plt.show()

