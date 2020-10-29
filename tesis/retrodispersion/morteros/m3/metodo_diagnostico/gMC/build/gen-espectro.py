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

import metodos_MC as mt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import NullFormatter

fig = plt.figure(figsize=(mt.cm2inch(18.0),mt.cm2inch(10.0)))
grid = plt.GridSpec(1, 1, wspace=0.25, hspace=0.2,left=0.1,right=0.98,bottom=0.17,top=0.98)

ax = fig.add_subplot(grid[0,0])
ax.tick_params(bottom=True,top=True,right=True,direction='in',which='both')

f = np.genfromtxt('gMC_h1_Ge.csv',delimiter=',')
y = f[2:,1]
x = np.arange(0,len(y))
ax.plot(x,y,drawstyle='steps-mid')
ax.set_xlabel(r'$E_\gamma$ (keV)')
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('cuentas/keV')

plt.show()

