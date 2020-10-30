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

fig, ax=plt.subplots(1,1,sharey=True)


f = np.genfromtxt('gMC_h1_Ge.csv',delimiter=',')
y = f[2:,1]
x = np.arange(0,len(y))
ax.plot(x,y,drawstyle='steps-mid',color='purple')

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::: CUENTAS :::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# FUNCION ENCARGADA DE DAR EL "FWHM" para el Ge-HP
"""
####################################################
def FWHM_Ge(Eg):
    f0 = 1.24
    f1 = 0.00068
    return f0 + f1 * Eg
##########################################
"""
##########################################

#FUNCION ENCARGADA DE DAR EL "FWHM" PARA EL NaI

def FWHM_Ge(Eg):
    f0=1
    f1=0.027
    f2=1.2
    return f0 + f1 * Eg + f2 * np.sqrt(Eg)

###############################################

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



#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::: Graficas :::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::





ax.plot(x,espectro,drawstyle='steps-mid',color='red')
ax.set_xlabel(r'$E_\gamma$ (keV)')
#ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('cuentas/keV')
plt.xlim(1,650)
plt.ylim(0,3000)
plt.show()

