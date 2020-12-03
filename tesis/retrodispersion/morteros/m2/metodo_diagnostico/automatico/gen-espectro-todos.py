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
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import NullFormatter
import scipy.stats as st
from scipy.stats import norm

#fig = plt.figure(figsize=(mt.cm2inch(18.0),mt.cm2inch(10.0)))
fig, ax=plt.subplots(1,1,sharey=True)
#grid = plt.GridSpec(1, 1, wspace=0.25, hspace=0.2,left=0.1,right=0.98,bottom=0.17,top=0.98)

#ax =fig.add_subplot(grid[0,0])
#ax.tick_params(bottom=True,top=True,right=True,direction='in',which='both')


f1 = np.genfromtxt('gMC_h1_NaI0.csv',delimiter=',')
f2 = np.genfromtxt('gMC_h1_NaI1.csv',delimiter=',')
f3 = np.genfromtxt('gMC_h1_NaI2.csv',delimiter=',')
f4 = np.genfromtxt('gMC_h1_NaI3.csv',delimiter=',')
f5 = np.genfromtxt('gMC_h1_NaI4.csv',delimiter=',')
f6 = np.genfromtxt('gMC_h1_NaI5.csv',delimiter=',')
f7 = np.genfromtxt('gMC_h1_NaI6.csv',delimiter=',')
f8 = np.genfromtxt('gMC_h1_NaI7.csv',delimiter=',')
f9 = np.genfromtxt('gMC_h1_NaI8.csv',delimiter=',')
f10 = np.genfromtxt('gMC_h1_NaI9.csv',delimiter=',')
f11 = np.genfromtxt('gMC_h1_NaI10.csv',delimiter=',')
f12 = np.genfromtxt('gMC_h1_NaI11.csv',delimiter=',')
f13 = np.genfromtxt('gMC_h1_NaI12.csv',delimiter=',')
f14 = np.genfromtxt('gMC_h1_NaI13.csv',delimiter=',')
f15 = np.genfromtxt('gMC_h1_NaI14.csv',delimiter=',')
f16 = np.genfromtxt('gMC_h1_NaI15.csv',delimiter=',')
f17 = np.genfromtxt('gMC_h1_NaI16.csv',delimiter=',')
f18 = np.genfromtxt('gMC_h1_NaI17.csv',delimiter=',')
f19 = np.genfromtxt('gMC_h1_NaI18.csv',delimiter=',')
f20 = np.genfromtxt('gMC_h1_NaI19.csv',delimiter=',')
f21 = np.genfromtxt('gMC_h1_NaI20.csv',delimiter=',')
f22 = np.genfromtxt('gMC_h1_NaI21.csv',delimiter=',')
f23 = np.genfromtxt('gMC_h1_NaI22.csv',delimiter=',')
f24 = np.genfromtxt('gMC_h1_NaI23.csv',delimiter=',')
f25 = np.genfromtxt('gMC_h1_NaI24.csv',delimiter=',')
f26 = np.genfromtxt('gMC_h1_NaI25.csv',delimiter=',')
f27 = np.genfromtxt('gMC_h1_NaI26.csv',delimiter=',')
f28 = np.genfromtxt('gMC_h1_NaI27.csv',delimiter=',')
f29 = np.genfromtxt('gMC_h1_NaI28.csv',delimiter=',')
f30 = np.genfromtxt('gMC_h1_NaI29.csv',delimiter=',')
f31 = np.genfromtxt('gMC_h1_NaI30.csv',delimiter=',')
f32 = np.genfromtxt('gMC_h1_NaI31.csv',delimiter=',')
f33 = np.genfromtxt('gMC_h1_NaI32.csv',delimiter=',')






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
y11 = f11[2:,1]
y12 = f12[2:,1]
y13 = f13[2:,1]
y14 = f14[2:,1]
y15 = f15[2:,1]
y16 = f16[2:,1]
y17 = f17[2:,1]
y18 = f18[2:,1]
y19 = f19[2:,1]
y20 = f20[2:,1]
y21 = f21[2:,1]
y22 = f22[2:,1]
y23 = f23[2:,1]
y24 = f24[2:,1]
y25 = f25[2:,1]
y26 = f26[2:,1]
y27 = f27[2:,1]
y28 = f28[2:,1]
y29 = f29[2:,1]
y30 = f30[2:,1]
y31 = f31[2:,1]
y32 = f32[2:,1]





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
x11 = np.arange(0,len(y11))
x12 = np.arange(0,len(y12))
x13 = np.arange(0,len(y13))
x14 = np.arange(0,len(y14))
x15 = np.arange(0,len(y15))
x16 = np.arange(0,len(y16))
x17 = np.arange(0,len(y17))
x18 = np.arange(0,len(y18))
x19 = np.arange(0,len(y19))
x20 = np.arange(0,len(y20))
x21 = np.arange(0,len(y21))
x22 = np.arange(0,len(y22))
x23 = np.arange(0,len(y23))
x24 = np.arange(0,len(y24))
x25 = np.arange(0,len(y25))
x26 = np.arange(0,len(y26))
x27 = np.arange(0,len(y27))
x28 = np.arange(0,len(y28))
x29 = np.arange(0,len(y29))
x30 = np.arange(0,len(y30))
x31 = np.arange(0,len(y31))
x32 = np.arange(0,len(y32))
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::: CUENTAS :::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::: CUENTAS :::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# FUNCION ENCARGADA DE DAR EL "FWHM" para el Ge-HP

####################################################
"""
def FWHM_Ge(Eg):
    f0 = 1.24
    f1 = 0.00068
    return f0 + f1 * Eg
"""
##########################################

#FUNCION ENCARGADA DE DAR EL "FWHM" PARA EL NaI

def FWHM_Ge(Eg):
    f0=1
    f1=0.027
    f2=1.2
    return f0 + f1 * Eg + f2 * np.sqrt(Eg)



########################################################################


################# 0.2 cm #######################



############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y1))
espectro1=np.zeros(len(y1))
for c in k:
    miu1=float(c)
    sigma1= 0.425 * FWHM_Ge(miu1)
    nue_cuen1 = int(y1[c])
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


################# 0.4 cm #######################



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


################# 0.6 cm #######################


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





################# 0.8 cm #######################


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




################# 1.0 cm #######################


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






################# 1.2 cm #######################


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





################# 1.4 cm #######################


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





################# 1.6 cm #######################


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





################# 1.8 cm #######################

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




################# 2.0 cm #######################

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

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y11))
espectro11=np.zeros(len(y11))
for c in k:
    miu11=float(c)
    sigma11= 0.425 * FWHM_Ge(miu11)
    nue_cuen11 = int(y11[c])
    if nue_cuen11>0:
        
        s=norm.rvs(loc=miu11,scale=sigma11, size= nue_cuen11,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro11[k]=espectro11[k]+hist[j]
            
############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y12))
espectro12=np.zeros(len(y12))
for c in k:
    miu12=float(c)
    sigma12= 0.425 * FWHM_Ge(miu12)
    nue_cuen12 = int(y12[c])
    if nue_cuen12>0:
        
        s=norm.rvs(loc=miu12,scale=sigma12, size= nue_cuen12,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro12[k]=espectro12[k]+hist[j]
#################################################################################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y13))
espectro13=np.zeros(len(y13))
for c in k:
    miu13=float(c)
    sigma13= 0.425 * FWHM_Ge(miu13)
    nue_cuen13 = int(y13[c])
    if nue_cuen13>0:
        
        s=norm.rvs(loc=miu13,scale=sigma13, size= nue_cuen13,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro13[k]=espectro13[k]+hist[j]



############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y14))
espectro14=np.zeros(len(y14))
for c in k:
    miu14=float(c)
    sigma14= 0.425 * FWHM_Ge(miu14)
    nue_cuen14 = int(y14[c])
    if nue_cuen14>0:

        s=norm.rvs(loc=miu14,scale=sigma14, size= nue_cuen14,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro14[k]=espectro14[k]+hist[j]
########################################################################





################# 1.8 cm #######################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y15))
espectro15=np.zeros(len(y15))
for c in k:
    miu15=float(c)
    sigma15= 0.425 * FWHM_Ge(miu15)
    nue_cuen15 = int(y15[c])
    if nue_cuen15>0:

        s=norm.rvs(loc=miu15,scale=sigma15, size= nue_cuen15,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro15[k]=espectro15[k]+hist[j]
########################################################################




################# 2.0 cm #######################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y16))
espectro16=np.zeros(len(y16))
for c in k:
    miu16=float(c)
    sigma16= 0.425 * FWHM_Ge(miu16)
    nue_cuen16 = int(y16[c])
    if nue_cuen16>0:
        
        s=norm.rvs(loc=miu16,scale=sigma16, size= nue_cuen16,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro16[k]=espectro16[k]+hist[j]
########################################################################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y17))
espectro17=np.zeros(len(y17))
for c in k:
    miu17=float(c)
    sigma17= 0.425 * FWHM_Ge(miu17)
    nue_cuen17 = int(y17[c])
    if nue_cuen17>0:
        
        s=norm.rvs(loc=miu17,scale=sigma17, size= nue_cuen17,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro17[k]=espectro17[k]+hist[j]
            
############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y18))
espectro18=np.zeros(len(y18))
for c in k:
    miu18=float(c)
    sigma18= 0.425 * FWHM_Ge(miu18)
    nue_cuen18 = int(y18[c])
    if nue_cuen18>0:
        
        s=norm.rvs(loc=miu18,scale=sigma18, size= nue_cuen18,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro18[k]=espectro18[k]+hist[j]
#################################################################################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y19))
espectro19=np.zeros(len(y19))
for c in k:
    miu19=float(c)
    sigma19= 0.425 * FWHM_Ge(miu19)
    nue_cuen19 = int(y19[c])
    if nue_cuen19>0:
        
        s=norm.rvs(loc=miu19,scale=sigma19, size= nue_cuen19,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro19[k]=espectro19[k]+hist[j]
########################################################################3
############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y20))
espectro20=np.zeros(len(y20))
for c in k:
    miu20=float(c)
    sigma20= 0.425 * FWHM_Ge(miu20)
    nue_cuen20 = int(y20[c])
    if nue_cuen20>0:
        
        s=norm.rvs(loc=miu20,scale=sigma20, size= nue_cuen20,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro20[k]=espectro20[k]+hist[j]
########################################################################





################# 1.6 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y21))
espectro21=np.zeros(len(y21))
for c in k:
    miu21=float(c)
    sigma21= 0.425 * FWHM_Ge(miu21)
    nue_cuen21 = int(y21[c])
    if nue_cuen21>0:

        s=norm.rvs(loc=miu21,scale=sigma21, size= nue_cuen21,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro21[k]=espectro21[k]+hist[j]
########################################################################





################# 1.8 cm #######################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y22))
espectro22=np.zeros(len(y22))
for c in k:
    miu22=float(c)
    sigma22= 0.425 * FWHM_Ge(miu22)
    nue_cuen22 = int(y22[c])
    if nue_cuen22>0:

        s=norm.rvs(loc=miu22,scale=sigma22, size= nue_cuen22,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro22[k]=espectro22[k]+hist[j]
########################################################################




################# 2.0 cm #######################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y23))
espectro23=np.zeros(len(y23))
for c in k:
    miu23=float(c)
    sigma23= 0.425 * FWHM_Ge(miu23)
    nue_cuen23 = int(y23[c])
    if nue_cuen23>0:
        
        s=norm.rvs(loc=miu23,scale=sigma23, size= nue_cuen23,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro23[k]=espectro23[k]+hist[j]
########################################################################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y24))
espectro24=np.zeros(len(y24))
for c in k:
    miu24=float(c)
    sigma24= 0.425 * FWHM_Ge(miu24)
    nue_cuen24 = int(y24[c])
    if nue_cuen24>0:
        
        s=norm.rvs(loc=miu24,scale=sigma24, size= nue_cuen24,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro24[k]=espectro24[k]+hist[j]
            
############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y25))
espectro25=np.zeros(len(y25))
for c in k:
    miu25=float(c)
    sigma25= 0.425 * FWHM_Ge(miu25)
    nue_cuen25 = int(y25[c])
    if nue_cuen25>0:
        
        s=norm.rvs(loc=miu25,scale=sigma25, size= nue_cuen25,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro25[k]=espectro25[k]+hist[j]
#################################################################################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y26))
espectro26=np.zeros(len(y26))
for c in k:
    miu26=float(c)
    sigma26= 0.425 * FWHM_Ge(miu26)
    nue_cuen26 = int(y26[c])
    if nue_cuen26>0:
        
        s=norm.rvs(loc=miu26,scale=sigma26, size= nue_cuen26,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro26[k]=espectro26[k]+hist[j]



############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y27))
espectro27=np.zeros(len(y27))
for c in k:
    miu27=float(c)
    sigma27= 0.425 * FWHM_Ge(miu27)
    nue_cuen27 = int(y27[c])
    if nue_cuen27>0:

        s=norm.rvs(loc=miu27,scale=sigma27, size= nue_cuen27,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro27[k]=espectro27[k]+hist[j]
########################################################################





################# 1.8 cm #######################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y28))
espectro28=np.zeros(len(y28))
for c in k:
    miu28=float(c)
    sigma28= 0.425 * FWHM_Ge(miu28)
    nue_cuen28 = int(y28[c])
    if nue_cuen28>0:

        s=norm.rvs(loc=miu28,scale=sigma28, size= nue_cuen28,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro28[k]=espectro28[k]+hist[j]
########################################################################




################# 2.0 cm #######################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y29))
espectro29=np.zeros(len(y29))
for c in k:
    miu29=float(c)
    sigma29= 0.425 * FWHM_Ge(miu29)
    nue_cuen29 = int(y29[c])
    if nue_cuen29>0:
        
        s=norm.rvs(loc=miu29,scale=sigma29, size= nue_cuen29,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro29[k]=espectro29[k]+hist[j]
########################################################################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y30))
espectro30=np.zeros(len(y30))
for c in k:
    miu30=float(c)
    sigma30= 0.425 * FWHM_Ge(miu30)
    nue_cuen30 = int(y30[c])
    if nue_cuen30>0:
        
        s=norm.rvs(loc=miu30,scale=sigma30, size= nue_cuen30,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro30[k]=espectro30[k]+hist[j]
            
############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y31))
espectro31=np.zeros(len(y31))
for c in k:
    miu31=float(c)
    sigma31= 0.425 * FWHM_Ge(miu31)
    nue_cuen31 = int(y31[c])
    if nue_cuen31>0:
        
        s=norm.rvs(loc=miu31,scale=sigma31, size= nue_cuen31,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro31[k]=espectro31[k]+hist[j]
#################################################################################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y32))
espectro32=np.zeros(len(y32))
for c in k:
    miu32=float(c)
    sigma32= 0.425 * FWHM_Ge(miu32)
    nue_cuen32 = int(y32[c])
    if nue_cuen32>0:
        
        s=norm.rvs(loc=miu32,scale=sigma32, size= nue_cuen32,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro32[k]=espectro32[k]+hist[j]
#########################################################################

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::: Graficas despues de aplicar el filtro Gaussiano ::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


ax.plot(x1,espectro1,drawstyle='steps-mid',label='0.0 cm')
ax.plot(x2,espectro2,drawstyle='steps-mid',label='0.5 cm')
ax.plot(x3,espectro3,drawstyle='steps-mid',label='1.0 cm')
ax.plot(x4,espectro4,drawstyle='steps-mid',label='1.5 cm')
ax.plot(x5,espectro5,drawstyle='steps-mid',label='2.0 cm')
ax.plot(x6,espectro6,drawstyle='steps-mid',label='2.5 cm')
ax.plot(x7,espectro7,drawstyle='steps-mid',label='3.0 cm')
ax.plot(x8,espectro8,drawstyle='steps-mid',label='3.5 cm')
ax.plot(x9,espectro9,drawstyle='steps-mid',label='4.0 cm')
ax.plot(x10,espectro10,drawstyle='steps-mid',label='4.5 cm')
ax.plot(x11,espectro11,drawstyle='steps-mid',label='5.0 cm')
ax.plot(x12,espectro12,drawstyle='steps-mid',label='5.5 cm')
ax.plot(x13,espectro13,drawstyle='steps-mid',label='6.0 cm')
ax.plot(x14,espectro14,drawstyle='steps-mid',label='6.5 cm')
ax.plot(x15,espectro15,drawstyle='steps-mid',label='7.0 cm')
ax.plot(x16,espectro16,drawstyle='steps-mid',label='7.5 cm')
ax.plot(x17,espectro17,drawstyle='steps-mid',label='8.0 cm')
ax.plot(x18,espectro18,drawstyle='steps-mid',label='1.0 cm')
ax.plot(x19,espectro19,drawstyle='steps-mid',label='1.5 cm')
ax.plot(x20,espectro20,drawstyle='steps-mid',label='2.0 cm')
ax.plot(x21,espectro21,drawstyle='steps-mid',label='2.5 cm')
ax.plot(x22,espectro22,drawstyle='steps-mid',label='3.0 cm')
ax.plot(x23,espectro23,drawstyle='steps-mid',label='3.5 cm')
ax.plot(x24,espectro24,drawstyle='steps-mid',label='4.0 cm')
ax.plot(x25,espectro25,drawstyle='steps-mid',label='4.5 cm')
ax.plot(x26,espectro26,drawstyle='steps-mid',label='5.0 cm')
ax.plot(x27,espectro27,drawstyle='steps-mid',label='5.5 cm')
ax.plot(x28,espectro28,drawstyle='steps-mid',label='6.0 cm')
ax.plot(x29,espectro29,drawstyle='steps-mid',label='6.5 cm')
ax.plot(x30,espectro30,drawstyle='steps-mid',label='7.0 cm')
ax.plot(x31,espectro31,drawstyle='steps-mid',label='7.5 cm')
ax.plot(x32,espectro32,drawstyle='steps-mid',label='8.0 cm')

############################################################################################################
######################## EJES ##############################################################################
############################################################################################################

ax.set_xlabel(r'$E_\gamma$ (keV)', size=20)
#ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('cuentas/keV', size=20)
plt.xlim(0,300)
#plt.ylim(0,2300)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
leg=plt.legend(loc="center left",prop={'size': 14})
for legobj in leg.legendHandles: #tamaño de la leyenda
    legobj.set_linewidth(5.0) #tamaño de la leyenda
plt.show()

###############################################################################################################
################################################################################################################
##################################################################################################################
#########################################################################
################# INICIO DE CONTEO  #####################################
#########################################################################

E1=197 #keV
E2= 262 #keV

############################################
############################################
ejex1=x1[E1:E2]
cuentas1=0
for i in range(len(ejex1)):
   cuentas1=cuentas1+espectro1[i]
    
print (cuentas1)
############################################
############################################

ejex2=x2[E1:E2]
cuentas2=0
for i in range(len(ejex2)):
   cuentas2=cuentas2+espectro2[i]
    
print (cuentas2)
############################################
############################################

ejex3=x3[E1:E2]
cuentas3=0
for i in range(len(ejex3)):
   cuentas3=cuentas3+espectro3[i]
    
print (cuentas3)
############################################
############################################


ejex4=x4[E1:E2]
cuentas4=0
for i in range(len(ejex4)):
   cuentas4=cuentas4+espectro4[i]
    
print (cuentas4)
############################################
############################################




ejex5=x5[E1:E2]
cuentas5=0
for i in range(len(ejex5)):
   cuentas5=cuentas5+espectro5[i]
    
print (cuentas5)
############################################
############################################






ejex6=x6[E1:E2]
cuentas6=0
for i in range(len(ejex6)):
   cuentas6=cuentas6+espectro6[i]
    
print (cuentas6)
############################################
############################################





ejex7=x7[E1:E2]
cuentas7=0
for i in range(len(ejex7)):
   cuentas7=cuentas7+espectro7[i]
    
print (cuentas7)
############################################
############################################

ejex8=x8[E1:E2]
cuentas8=0
for i in range(len(ejex8)):
   cuentas8=cuentas8+espectro8[i]
    
print (cuentas8)
############################################
############################################

ejex9=x9[E1:E2]
cuentas9=0
for i in range(len(ejex9)):
   cuentas9=cuentas9+espectro9[i]
    
print (cuentas9)
############################################
############################################


ejex10=x10[E1:E2]
cuentas10=0
for i in range(len(ejex10)):
   cuentas10=cuentas10+espectro10[i]
    
print (cuentas10)
############################################
############################################


ejex11=x11[E1:E2]
cuentas11=0
for i in range(len(ejex11)):
   cuentas11=cuentas11+espectro11[i]
    
print (cuentas11)
############################################
############################################


ejex12=x12[E1:E2]
cuentas12=0
for i in range(len(ejex12)):
   cuentas12=cuentas12+espectro12[i]
    
print (cuentas12)
############################################
############################################


ejex13=x13[E1:E2]
cuentas13=0
for i in range(len(ejex13)):
   cuentas13=cuentas13+espectro13[i]
    
print (cuentas13)
############################################
############################################

############################################
############################################

ejex14=x14[E1:E2]
cuentas14=0
for i in range(len(ejex14)):
   cuentas14=cuentas14+espectro14[i]
    
print (cuentas14)
############################################
############################################

ejex15=x15[E1:E2]
cuentas15=0
for i in range(len(ejex15)):
   cuentas15=cuentas15+espectro15[i]
    
print (cuentas15)
############################################
############################################


ejex16=x16[E1:E2]
cuentas16=0
for i in range(len(ejex16)):
   cuentas16=cuentas16+espectro16[i]
    
print (cuentas16)
############################################
############################################


ejex17=x17[E1:E2]
cuentas17=0
for i in range(len(ejex17)):
   cuentas17=cuentas17+espectro17[i]
    
print (cuentas17)
############################################
############################################


ejex18=x18[E1:E2]
cuentas18=0
for i in range(len(ejex18)):
   cuentas18=cuentas18+espectro18[i]
    
print (cuentas18)
############################################
############################################


ejex19=x19[E1:E2]
cuentas19=0
for i in range(len(ejex19)):
   cuentas19=cuentas19+espectro19[i]
    
print (cuentas19)

############################################
############################################
############################################
############################################


ejex20=x20[E1:E2]
cuentas20=0
for i in range(len(ejex20)):
   cuentas20=cuentas20+espectro20[i]
    
print (cuentas20)
############################################
############################################


ejex21=x21[E1:E2]
cuentas21=0
for i in range(len(ejex21)):
   cuentas21=cuentas21+espectro21[i]
    
print (cuentas21)
############################################
############################################


ejex22=x22[E1:E2]
cuentas22=0
for i in range(len(ejex22)):
   cuentas22=cuentas22+espectro22[i]
    
print (cuentas22)
############################################
############################################


ejex23=x23[E1:E2]
cuentas23=0
for i in range(len(ejex23)):
   cuentas23=cuentas23+espectro23[i]
    
print (cuentas23)
############################################
############################################

ejex24=x24[E1:E2]
cuentas24=0
for i in range(len(ejex24)):
   cuentas24=cuentas24+espectro24[i]
    
print (cuentas24)
############################################
############################################


ejex25=x25[E1:E2]
cuentas25=0
for i in range(len(ejex25)):
   cuentas25=cuentas25+espectro25[i]
    
print (cuentas25)
############################################
############################################

ejex26=x26[E1:E2]
cuentas26=0
for i in range(len(ejex26)):
   cuentas26=cuentas26+espectro26[i]
    
print (cuentas26)
############################################
############################################


############################################
############################################

ejex27=x27[E1:E2]
cuentas27=0
for i in range(len(ejex27)):
   cuentas27=cuentas27+espectro27[i]
    
print (cuentas27)
############################################
############################################

ejex28=x28[E1:E2]
cuentas28=0
for i in range(len(ejex28)):
   cuentas28=cuentas28+espectro28[i]
    
print (cuentas28)
############################################
############################################


ejex29=x29[E1:E2]
cuentas29=0
for i in range(len(ejex29)):
   cuentas29=cuentas29+espectro29[i]
    
print (cuentas29)
############################################
############################################


ejex30=x30[E1:E2]
cuentas30=0
for i in range(len(ejex30)):
   cuentas30=cuentas30+espectro30[i]
    
print (cuentas30)
############################################
############################################


ejex31=x31[E1:E2]
cuentas31=0
for i in range(len(ejex31)):
   cuentas31=cuentas31+espectro31[i]
    
print (cuentas31)
############################################
############################################


ejex32=x32[E1:E2]
cuentas32=0
for i in range(len(ejex32)):
   cuentas32=cuentas32+espectro32[i]
    
print (cuentas32)

############################################
############################################



###################################################################

cuentas_totales=[cuentas1, cuentas2, cuentas3, cuentas4, cuentas5, cuentas6, cuentas7, cuentas8, cuentas9, cuentas10, cuentas11, cuentas12, cuentas13, cuentas14, cuentas15, cuentas16, cuentas17, cuentas18, cuentas19,cuentas20, cuentas21, cuentas22, cuentas23, cuentas24, cuentas25, cuentas26, cuentas27, cuentas28, cuentas29, cuentas30, cuentas31, cuentas32]

ejex_graf=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]

fig2, axs=plt.subplots(1,1,sharey=False)
x=np.linspace(0.2,13.0,10000)


axs.set_xlabel(r'$x$ (cm)', size=20)
axs.set_ylabel('Intensidad (cuentas)', size=20)

axs.plot(ejex_graf,cuentas_totales,'o', label='Ajuste ',color='purple')
#plt.xticks(ejex_graf,fontsize=16)
plt.yticks(fontsize=16)
#plt.xlim(-1.0, 5.5)

"""
leg=axs.legend(loc="upper left",prop={'size': 14})
for legobj in leg.legendHandles: #tamaño de la leyenda
    legobj.set_linewidth(2.0) #tamaño de la leyenda
"""
plt.show()
