import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
import numpy as np
from scipy.integrate import quad
from glob import glob
from numpy import genfromtxt
from scipy import stats
import matplotlib as mpl
from scipy.stats import norm
import matplotlib.ticker as ticker #para los ticks

mpl.rcParams.update({"text.usetex":True,
                     "font.family":"serif",
                     "font.sans-serif":["Computer Modern San serif"],
                     "legend.fontsize":12,
                     "axes.labelsize":12,
                     "xtick.labelsize":12,
                     "ytick.labelsize":12,
                     "figure.figsize":(3.4,3.2),
                     "mathtext.fontset":"dejavusans",
                     "text.latex.preamble":r"\usepackage{amsmath}"
})

x=[1,2,3,4,5]

alpha_nist=[1.56, 1.31, 1.20, 1.15, 2.31]
error1=[0.15, 0.09, 0.07, 0.06, 0.39]
alpha_geant=[1.18, 1.12, 1.11, 1.07, 1.57]
error2=[0.08, 0.05, 0.08, 0.05, 0.21]

n_nist=[0.46, 0.44, 0.42, 0.42, 0.52]
error3=[0.02, 0.01, 0.01, 0.01, 0.03]
n_geant=[0.44, 0.43, 0.44, 0.43, 0.49]
error4=[0.01, 0.01, 0.01, 0.01, 0.02]

fig_1,axs=plt.subplots(1,1,figsize=(3.5,4))

axs.set_ylabel(r'$\alpha$')
axs.set_xlabel(r'Lote de morteros')
#plt.title("Morteros 1")

axs.errorbar(x, alpha_geant, yerr=error2, fmt='o', c='red',ecolor='k',label=r'$\alpha_{Geant4}$')
axs.errorbar(x,alpha_nist, yerr=error1, fmt='o',c='purple',ecolor='k',label=r'$\alpha_{NIST}$')

axs.legend()

#plt.xticks(fontsize=20)
#plt.yticks(fontsize=20)
leg=plt.legend(loc="upper left")#,prop={'size': 20})
#for legobj in leg.legendHandles: #tamaño de la leyenda
#    legobj.set_linewidth(2.5) #tamaño de la leyenda

fig_1.tight_layout()

plt.show()

#########################################
fig_2,axs=plt.subplots(1,1,figsize=(3.5,4))

axs.set_ylabel(r'n')
axs.set_xlabel(r'Lote de morteros')
axs.errorbar(x, n_geant, yerr=error4, fmt='o', c='blue',ecolor='k',label=r'$n_{Geant4}$')
axs.errorbar(x,n_nist, yerr=error3, fmt='o',c='olive',ecolor='k',label=r'$n_{NIST}$')
axs.legend()

#plt.xticks(fontsize=20)
#plt.yticks(fontsize=20)
leg=plt.legend(loc="upper left")#,prop={'size': 20})
#for legobj in leg.legendHandles: #tamaño de la leyenda
#    legobj.set_linewidth(2.5) #tamaño de la leyenda

fig_2.tight_layout()

plt.show()
