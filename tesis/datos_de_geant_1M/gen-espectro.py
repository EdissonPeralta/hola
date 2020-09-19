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

#fig = plt.figure(figsize=(mt.cm2inch(18.0),mt.cm2inch(10.0)))
fig, axs=plt.subplots(1,1,sharey=True)
grid = plt.GridSpec(1, 1, wspace=0.25, hspace=0.2,left=0.1,right=0.98,bottom=0.17,top=0.98)


ax =fig.add_subplot(grid[0,0])
ax.tick_params(bottom=True,top=True,right=True,direction='in',which='both')

f = np.genfromtxt('gMC_h11_Ge.csv',delimiter=',')
f2 = np.genfromtxt('gMC_h10_Ge.csv',delimiter=',')
f3 = np.genfromtxt('gMC_h9_Ge.csv',delimiter=',')
f4 = np.genfromtxt('gMC_h8_Ge.csv',delimiter=',')
f5 = np.genfromtxt('gMC_h7_Ge.csv',delimiter=',')
f6 = np.genfromtxt('gMC_h6_Ge.csv',delimiter=',')
f7 = np.genfromtxt('gMC_h5_Ge.csv',delimiter=',')
f8 = np.genfromtxt('gMC_h4_Ge.csv',delimiter=',')
f9 = np.genfromtxt('gMC_h3_Ge.csv',delimiter=',')
f10 = np.genfromtxt('gMC_h2_Ge.csv',delimiter=',')
f11 = np.genfromtxt('gMC_h1_Ge.csv',delimiter=',')
y = f[2:,1]
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
x = np.arange(0,len(y))
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
ax.plot(x,y,drawstyle='steps-mid')
ax.plot(x2,y2,drawstyle='steps-mid')
ax.plot(x3,y3,drawstyle='steps-mid')
ax.plot(x4,y4,drawstyle='steps-mid')
ax.plot(x5,y5,drawstyle='steps-mid')
ax.plot(x,y6,drawstyle='steps-mid')
ax.plot(x7,y7,drawstyle='steps-mid')
ax.plot(x8,y8,drawstyle='steps-mid')
ax.plot(x9,y9,drawstyle='steps-mid')
ax.plot(x10,y10,drawstyle='steps-mid')
ax.plot(x11,y11,drawstyle='steps-mid')
ax.set_xlabel(r'$E_\gamma$ (keV)')
#ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('cuentas/keV')
plt.xlim(10,700)
plt.ylim(0,5100)
plt.show()

