import random as rn
import scipy.stats as st
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
from astropy.io import ascii

mu=[0.316,0.2453,0.20,0.172,0.166,0.162,0.082,0.092]
error=[0.005,0.0009,0.01,0.006,0.002,0.003,0.007,0.002]
energia=[80.99,122.06,136.47,302.85,383.84,356.01,1173.22,1332.49]



a01=1
a11=4
a0=1

def gaussi1(x,a01,a11):
	#return ((a11*mu)+a01)
	return a01*(x**(a11))

popt_gaussi1, pcov1=curve_fit(gaussi1, energia, mu, p0=[a01,a11], sigma=error)


perr1= np.sqrt(np.diag(pcov1))

print(popt_gaussi1)

print('===============')

print(perr1)


a01=popt_gaussi1[0]
a11=popt_gaussi1[1]


fig, axs=plt.subplots(1,1,sharey=False)

plt.title("MORTEROS 1", size=22)
plt.xlabel("Energía (keV)",size=22)  
plt.ylabel("μ (1/cm)",size=22)

mpl.rcParams.update({'font.size': 17})


plt.xticks(fontsize=20)

plt.yticks(fontsize=20)




#(u"μ={}, σ²={}".format(mu, sigma))

x=np.linspace(80,1340,10000)


axs.plot(x,gaussi1(x,a01,a11),color='purple')

axs.set_yscale('log')
axs.set_xscale('log')
plt.errorbar(energia,mu,yerr=error,xerr=None,fmt='.',color='brown', markersize=12)

plt.xticks(np.arange(x.min(), x.max(), 1000))
plt.yticks(np.arange(x.min(), x.max(), 10000))
plt.show()