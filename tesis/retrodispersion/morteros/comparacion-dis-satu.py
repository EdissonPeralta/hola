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

mu_geant=[1.6, 1.8, 1.6, 1.7, 1.58]
error2=[0.1, 0.1, 0.1, 0.1, 0.07]
mu_nist=[1.5, 1.5, 1.5, 1.5, 1.5]

#jk=['a','b','c','d','e']

fig_1,axs=plt.subplots(1,1,figsize=(4,4))

axs.set_ylabel(r'Profundidad (cm)')
axs.set_xlabel(r'Lote de morteros')
#plt.title("Morteros 1")

axs.errorbar(x, mu_geant, yerr=error2, fmt='o', c='red',ecolor='k',label=r'Profundidad Geant4')
axs.errorbar(x, mu_nist, yerr=None, fmt='o',c='purple',ecolor='k',label=r'Profundidad real')
#plt.xticks(jk)
axs.legend()

#plt.xticks(fontsize=20)
#plt.yticks(fontsize=20)
leg=plt.legend(loc="upper right")#,prop={'size': 20})
#for legobj in leg.legendHandles: #tamaño de la leyenda
#    legobj.set_linewidth(2.5) #tamaño de la leyenda

fig_1.tight_layout()

plt.show()
 

