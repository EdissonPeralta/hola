#-*- coding: utf-8 -*-
"""creator on Thu Sept 17
@author: Fabian Pastrana
"""
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
import matplotlib.ticker as ticker #para los ticks
import csv

mpl.rcParams.update({"font.family":"sans-serif",
                     "text.usetex":True,
                     "legend.fontsize":12,
                     "axes.labelsize":12,
                     "xtick.labelsize":12,
                     "ytick.labelsize":12,
                     "mathtext.fontset":"dejavusans",
                     "text.latex.preamble":r"\usepackage{mathrsfs}"
})

codes=[]
names=[]
for i in range(20):
     codes.extend([str(i+1)+'-TransmisionParafina60s-G128-Thr160.mtxt'])
     names.extend([i+1])


c=[genfromtxt(f,dtype=int,skip_header=974,skip_footer=11,usecols={1}) for f in codes]

x=np.arange(0,len(c[0]))

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::GRAFICAS::::::::::GRAFICAS::::::::::GRAFICAS::::::::::GRAFICAS::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

fig_1,axs=plt.subplots(1,1)
axs.set_ylabel(r'Cuentas')
axs.set_xlabel(r'Canales')
for i in range(len(c)):
    axs.step(x,c[i],where='mid',label=str(names[i]))
axs.legend(loc='upper left',title='Medicion',ncol=2)
axs.set_xlim(0,400)
axs.set_ylim(-10,700)
fig_1.tight_layout()
fig_1.savefig('1.pdf')

plt.show()
