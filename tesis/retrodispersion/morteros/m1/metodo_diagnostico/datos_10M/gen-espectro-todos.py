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

f1 = np.genfromtxt('gMC_h(0.0)_Ge.csv',delimiter=',')
f2 = np.genfromtxt('gMC_h(0.5)_Ge.csv',delimiter=',')
f3 = np.genfromtxt('gMC_h(1.0)_Ge.csv',delimiter=',')
f4 = np.genfromtxt('gMC_h(1.5)_Ge.csv',delimiter=',')
f5 = np.genfromtxt('gMC_h(2.0)_Ge.csv',delimiter=',')
f6 = np.genfromtxt('gMC_h(2.5)_Ge.csv',delimiter=',')
f7 = np.genfromtxt('gMC_h(3.0)_Ge.csv',delimiter=',')
f8 = np.genfromtxt('gMC_h(3.5)_Ge.csv',delimiter=',')
f9 = np.genfromtxt('gMC_h(4.0)_Ge.csv',delimiter=',')
f10 = np.genfromtxt('gMC_h(4.5)_Ge.csv',delimiter=',')
f11 = np.genfromtxt('gMC_h(5.0)_Ge.csv',delimiter=',')
f12 = np.genfromtxt('gMC_h(5.5)_Ge.csv',delimiter=',')
f13 = np.genfromtxt('gMC_h(6.0)_Ge.csv',delimiter=',')

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

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::: CUENTAS :::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


"""
# FUNCION ENCARGADA DE DAR EL "FWHM" para el Ge-HP

####################################################
def FWHM_Ge(Eg):
    f0 = 1.24
    f1 = 0.00068
    return f0 + f1 * Eg
##########################################

k=np.arange(10,len(y1))
espectro=np.zeros(len(y1))

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


"""
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::: Graficas :::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::






ax.plot(x1,y1,drawstyle='steps-mid')
ax.plot(x2,y2,drawstyle='steps-mid')
ax.plot(x3,y3,drawstyle='steps-mid')
ax.plot(x4,y4,drawstyle='steps-mid')
ax.plot(x5,y5,drawstyle='steps-mid')
ax.plot(x6,y6,drawstyle='steps-mid')
ax.plot(x7,y7,drawstyle='steps-mid')
ax.plot(x8,y8,drawstyle='steps-mid')
ax.plot(x9,y9,drawstyle='steps-mid')
ax.plot(x10,y10,drawstyle='steps-mid')
ax.plot(x11,y11,drawstyle='steps-mid')
ax.plot(x12,y12,drawstyle='steps-mid')
ax.plot(x13,y13,drawstyle='steps-mid')

ax.set_xlabel(r'$E_\gamma$ (keV)')
#ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('cuentas/keV')
plt.xlim(0,300)
plt.ylim(0,500)
plt.show()

