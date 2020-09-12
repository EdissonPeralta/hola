import random as rn
import scipy.stats as st
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
from astropy.io import ascii

################################################
# ACÁ DEFINO LAS INTENSIDADES ENCONTRADAS 
#Y LAS PONGO EN FORMA DE VECTOR
##################################################

intensidades22na511=[148925,132409,116194,102521,90773]
errores22na511=[1057,920,765,630,522]
intensidades137cs661=[7775,6814,6001,5544,5056]
errores137cs661=[90,70,73,67,58]
intensidades22na1274=[42164,38897,35912,33243,30475]
errores22na1274=[469,438,390,330,299]


#------------------------------------------------------------

#########################################
#ESTOS SON LOS GROSORES DE LOS MORTEROS
############################################
mor1=(8.86+9.03+9.16+8.71)/(4*10)
mor2=(8.58+9.65+9.59+9.37)/(4*10)
mor3=(8.80+9.67+10.69+10.18)/(4*10)
mor4=(9.34+8.96+10.16+8.63)/(4*10)
#------------------------------------------------------------

############################################
#VARIOS INTENTOS DE COMO DEFINIR LOS GROSORES
#############################################

#distancia1=np.array[(0,mor1,mor1+mor2,mor1+mor2+mor3,mor1+mor2+mor3+mor4)]
distancia1=[0,mor1,mor1+mor2,mor1+mor2+mor3,mor1+mor2+mor3+mor4]
#distancia1=[0,0.894,1.823,2.807,3.7344]
#------------------------------------------------------


#############################################
#   REGRESIÓN
#############################################
a01C=15179
a11C=sum(distancia1)/5

def gaussi1(mu,a11C,a01C):
	#return ((a11*mu)+a01)
	return a01C*np.exp(mu*a11C)

popt_gaussi1, pcov1=curve_fit(gaussi1, distancia1, intensidades22na511, p0=[a11C,a01C], sigma=errores22na511)

a01B=23652
a11B=sum(distancia1)/5

def gaussi2(mu,a11B,a01B):
	#return ((a11*mu)+a01)
	return a01B*np.exp(mu*a11B)


popt_gaussi2, pcov2=curve_fit(gaussi2, distancia1, intensidades137cs661, p0=[a11B,a01B],sigma=errores137cs661)

a01C7=3005
a11C7=sum(distancia1)/5
def gaussi3(mu,a11C7,a01C7):
	#return ((a11*mu)+a01)
	return a01C7*np.exp(mu*a11C7)


popt_gaussi3, pcov3=curve_fit(gaussi3, distancia1, intensidades22na1274, p0=[a11C7,a01C7],sigma=errores22na1274)


perr1= np.sqrt(np.diag(pcov1));
perr2= np.sqrt(np.diag(pcov2));
perr3= np.sqrt(np.diag(pcov3))


print(perr1,perr2,perr3)
####################################################
#OBTENCIÓN DE DATOS DE LA REGRESION
####################################################

print('valores de los ajustes(pendiente,corte)')


print(popt_gaussi1)
print(popt_gaussi2)
print(popt_gaussi3)

print('_______________________')



####################################################
#              GRAFICAR
#######################################################
a11=popt_gaussi1[0]
a01=popt_gaussi1[1]

a12=popt_gaussi2[0]
a02=popt_gaussi2[1]

a13=popt_gaussi3[0]
a03=popt_gaussi3[1]



fig, axs=plt.subplots(1,1,sharey=False)

plt.title("MORTEROS1", size=25)
plt.xlabel("X (cm)",size=22)  
plt.ylabel("Intensidad",size=22)

x=np.linspace(0,4,10000)

mpl.rcParams.update({'font.size': 17})


plt.xticks(fontsize=16)

plt.yticks(fontsize=16)


plt.errorbar(distancia1,intensidades22na511,yerr=errores22na511,xerr=None,fmt='.',color='red', markersize=12)
plt.errorbar(distancia1,intensidades137cs661,yerr=errores137cs661,xerr=None,fmt='.',color='blue', markersize=12)
plt.errorbar(distancia1,intensidades22na1274,yerr=errores22na1274,xerr=None,fmt='.',color='green', markersize=12)

axs.semilogy(x,gaussi1(x,a11,a01),color='red', label = "511keV")
axs.semilogy(x,gaussi2(x,a12,a02),color='blue', label = "661keV")
axs.semilogy(x,gaussi3(x,a13,a03),color='green', label = "1274keV")



"""
plt.semilogy(distancia1,intensidades57Co, color='green', label = "57Co")
plt.semilogy(distancia1,intensidades133Ba, color='blue', label = "133Ba")
plt.semilogy(distancia1,intensidades60Co, color='red', label = "60Co")
"""

plt.legend(loc="center right")

plt.show()