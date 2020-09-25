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


intensidades133ba80=[15179,10306,7306,5460,4174]
errores133ba80=[254,291,290,285,273]
intensidades57co122=[23652,18212,11635,10993,9645]
errores57co122=[183,223,171,253,231]
intensidades57Co136=[3005,2308,1953,1487,1214]
errores57co136=[158,223,149,121,102]

intensidades133ba302=[7078,5693,4792,4028,3400]
errores133ba302=[91,63,89,95,95]
intensidades133ba383=[20863,16963,14731,13081,10968]
errores133ba383=[120,147,121,112,198]
intensidades133ba356=[2822,2357,2040,1697,1567]
errores133ba356=[60,40,36,39,37]

intensidades60co1173=[5549,5029,4762,4473,3890]
errores60co1173=[105,56,46,50,87]
intensidades60co1332=[5153,4661,4384,4018,3735]
errores60co1332=[73,77,35,90,34]
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

popt_gaussi1, pcov1=curve_fit(gaussi1, distancia1, intensidades133ba80, p0=[a11C,a01C], sigma=errores133ba80)

a01B=23652
a11B=sum(distancia1)/5

def gaussi2(mu,a11B,a01B):
	#return ((a11*mu)+a01)
	return a01B*np.exp(mu*a11B)


popt_gaussi2, pcov2=curve_fit(gaussi2, distancia1, intensidades57co122, p0=[a11B,a01B],sigma=errores57co122)

a01C7=3005
a11C7=sum(distancia1)/5
def gaussi3(mu,a11C7,a01C7):
	#return ((a11*mu)+a01)
	return a01C7*np.exp(mu*a11C7)


popt_gaussi3, pcov3=curve_fit(gaussi3, distancia1, intensidades57Co136, p0=[a11C7,a01C7],sigma=errores57co136)


a0122na=7078
a1122na=sum(distancia1)/5

def gaussi4(mu,a1122na,a0122na):
	#return ((a11*mu)+a01)
	return a0122na*np.exp(mu*a1122na)

popt_gaussi4, pcov4=curve_fit(gaussi4, distancia1, intensidades133ba302, p0=[a1122na,a0122na], sigma=errores133ba302)


a01137cs=20863
a11137cs=sum(distancia1)/5
def gaussi5(mu,a11137cs,a01137cs):
	#return ((a11*mu)+a01)
	return a01137cs*np.exp(mu*a11137cs)


popt_gaussi5, pcov5=curve_fit(gaussi5, distancia1, intensidades133ba383, p0=[a11137cs,a01137cs],sigma=errores133ba383)


a0160co2=2822
a1160co2=sum(distancia1)/5

def gaussi6(mu,a1160co2,a0160co2):
	#return ((a11*mu)+a01)
	return a0160co2*np.exp(mu*a1160co2)


popt_gaussi6, pcov6=curve_fit(gaussi6, distancia1, intensidades133ba356, p0=[a1160co2,a0160co2],sigma=errores133ba356)


a0122na2co=5549
a1122na2co=sum(distancia1)/5

def gaussi7(mu,a1122na2co,a0122na2co):
	#return ((a11*mu)+a01)
	return a0122na2co*np.exp(mu*a1122na2co)

popt_gaussi7, pcov7=curve_fit(gaussi7, distancia1, intensidades60co1173, p0=[a1122na2co,a0122na2co], sigma=errores60co1173)


a0160co13=5153
a1160co13=sum(distancia1)/5

def gaussi8(mu,a1160co13,a0160co13):
	#return ((a11*mu)+a01)
	return a0160co13*np.exp(mu*a1160co13)

popt_gaussi8, pcov8=curve_fit(gaussi7, distancia1, intensidades60co1332, p0=[a1160co13,a0160co13], sigma=errores60co1332)




perr8= np.sqrt(np.diag(pcov8));
perr7= np.sqrt(np.diag(pcov7));
perr5= np.sqrt(np.diag(pcov5));
perr6= np.sqrt(np.diag(pcov6));
perr4= np.sqrt(np.diag(pcov4));
perr3= np.sqrt(np.diag(pcov3));
perr2= np.sqrt(np.diag(pcov2));
perr1= np.sqrt(np.diag(pcov1))


print(perr8,perr7,perr5,perr6,perr4,perr3,perr2,perr1)
####################################################
#OBTENCIÓN DE DATOS DE LA REGRESION
####################################################

print('valores de los ajustes(pendiente,corte)')

print(popt_gaussi8)
print(popt_gaussi7)
print(popt_gaussi5)
print(popt_gaussi6)
print(popt_gaussi4)
print(popt_gaussi3)
print(popt_gaussi2)
print(popt_gaussi1)

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

a14=popt_gaussi4[0]
a04=popt_gaussi4[1]

a16=popt_gaussi6[0]
a06=popt_gaussi6[1]

a15=popt_gaussi5[0]
a05=popt_gaussi5[1]

a17=popt_gaussi7[0]
a07=popt_gaussi7[1]


a18=popt_gaussi8[0]
a08=popt_gaussi8[1]

fig, axs=plt.subplots(1,1,sharey=False)

plt.title("MORTEROS1", size=25)
plt.xlabel("X (cm)",size=22)  
plt.ylabel("Intensidad",size=22)

x=np.linspace(0,4,10000)

mpl.rcParams.update({'font.size': 17})


plt.xticks(fontsize=16)

plt.yticks(fontsize=16)


plt.errorbar(distancia1,intensidades133ba80,yerr=errores133ba80,xerr=None,fmt='.',color='red', markersize=12)
plt.errorbar(distancia1,intensidades57co122,yerr=errores57co122,xerr=None,fmt='.',color='blue', markersize=12)
plt.errorbar(distancia1,intensidades57Co136,yerr=errores57co136,xerr=None,fmt='.',color='green', markersize=12)
plt.errorbar(distancia1,intensidades133ba302,yerr=errores133ba302,xerr=None,fmt='.',color='teal', markersize=12)
plt.errorbar(distancia1,intensidades133ba383,yerr=errores133ba383,xerr=None,fmt='.',color='black', markersize=12)
plt.errorbar(distancia1,intensidades133ba356,yerr=errores133ba356,xerr=None,fmt='.',color='green', markersize=12)
plt.errorbar(distancia1,intensidades60co1173,yerr=errores60co1173,xerr=None,fmt='.',color='deeppink', markersize=12)
plt.errorbar(distancia1,intensidades60co1332,yerr=errores60co1332,xerr=None,fmt='.',color='red', markersize=12)

axs.semilogy(x,gaussi3(x,a11,a01),color='red', label = "80keV")
axs.semilogy(x,gaussi3(x,a12,a02),color='blue', label = "122keV")
axs.semilogy(x,gaussi3(x,a13,a03),color='green', label = "136keV")
axs.semilogy(x,gaussi3(x,a14,a04),color='teal', label = "302keV")
axs.semilogy(x,gaussi3(x,a15,a05),color='black', label = "383keV")
axs.semilogy(x,gaussi3(x,a16,a06),color='green', label = "356keV")
axs.semilogy(x,gaussi3(x,a17,a07),color='deeppink', label = "1173keV")
axs.semilogy(x,gaussi3(x,a18,a08),color='red', label = "1332keV")




"""
plt.semilogy(distancia1,intensidades57Co, color='green', label = "57Co")
plt.semilogy(distancia1,intensidades133Ba, color='blue', label = "133Ba")
plt.semilogy(distancia1,intensidades60Co, color='red', label = "60Co")
"""

#plt.legend(loc="center right")

plt.show()