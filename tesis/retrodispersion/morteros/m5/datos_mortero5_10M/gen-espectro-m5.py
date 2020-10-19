import matplotlib as mpl
import random as rn
import scipy.stats as st
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#::::::::::::::::::::::::::::::::::::
#:::::::: ESPECTRO EXPERIMENTAL::::::
#::::::::::::::::::::::::::::::::::::

from scipy.optimize import curve_fit
#from scipy.signal import find_peaks
from astropy.io import ascii

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
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import NullFormatter
import scipy.stats as st
from scipy.stats import norm


#fig = plt.figure(figsize=(mt.cm2inch(18.0),mt.cm2inch(10.0)))
fig, ax=plt.subplots(1,1,sharey=False)
grid = plt.GridSpec(1, 1, wspace=0.25, hspace=0.2,left=0.1,right=0.98,bottom=0.17,top=0.98)


#ax =fig.add_subplot(grid[0,0])
#ax.tick_params(bottom=True,top=True,right=True,direction='in',which='both')


f1 = np.genfromtxt('gMC_h1_Ge.csv',delimiter=',')
f2 = np.genfromtxt('gMC_h2_Ge.csv',delimiter=',')
f3 = np.genfromtxt('gMC_h3_Ge.csv',delimiter=',')
f4 = np.genfromtxt('gMC_h4_Ge.csv',delimiter=',')
f5 = np.genfromtxt('gMC_h5_Ge.csv',delimiter=',')
f6 = np.genfromtxt('gMC_h6_Ge.csv',delimiter=',')
f7 = np.genfromtxt('gMC_h7_Ge.csv',delimiter=',')
f8 = np.genfromtxt('gMC_h8_Ge.csv',delimiter=',')
f9 = np.genfromtxt('gMC_h9_Ge.csv',delimiter=',')
f10 = np.genfromtxt('gMC_h10_Ge.csv',delimiter=',')

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

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::: CUENTAS :::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# FUNCION ENCARGADA DE DAR EL "FWHM" para el Ge-HP

####################################################
"""
def FWHM_Ge(Eg):
    f0 = 1.24
    f1 = 0.00068
    return f0 + f1 * Eg
"""
##########################################

#FUNCION ENCARGADA DE DAR EL "FWHM" PARA EL NaI

def FWHM_Ge(Eg):
    f0=1
    f1=0.027
    f2=1.2
    return f0 + f1 * Eg + f2 * np.sqrt(Eg)



########################################################################


################# 0.2 cm #######################



############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y1))
espectro1=np.zeros(len(y1))
for c in k:
    miu1=float(c)
    sigma1= 0.425 * FWHM_Ge(miu1)
    nue_cuen1 = int(y1[c])
    if nue_cuen1>0:

        s=norm.rvs(loc=miu1,scale=sigma1, size= nue_cuen1,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro1[k]=espectro1[k]+hist[j]
########################################################################


################# 0.4 cm #######################



############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y2))
espectro2=np.zeros(len(y2))
for c in k:
    miu2=float(c)
    sigma2= 0.425 * FWHM_Ge(miu2)
    nue_cuen2 = int(y2[c])
    if nue_cuen2>0:

        s=norm.rvs(loc=miu2,scale=sigma2, size= nue_cuen2,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro2[k]=espectro2[k]+hist[j]
########################################################################


################# 0.6 cm #######################


############### SE APLICA EL FWHM ####################

k=np.arange(10,len(y3))
espectro3=np.zeros(len(y3))
for c in k:
    miu3=float(c)
    sigma3= 0.425 * FWHM_Ge(miu3)
    nue_cuen3 = int(y3[c])
    if nue_cuen3>0:
        
        s=norm.rvs(loc=miu3,scale=sigma3, size= nue_cuen3,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro3[k]=espectro3[k]+hist[j]
########################################################################





################# 0.8 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y4))
espectro4=np.zeros(len(y4))
for c in k:
    miu4=float(c)
    sigma4= 0.425 * FWHM_Ge(miu4)
    nue_cuen4 = int(y4[c])
    if nue_cuen4>0:

        s=norm.rvs(loc=miu4,scale=sigma4, size= nue_cuen4,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro4[k]=espectro4[k]+hist[j]
########################################################################




################# 1.0 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y5))
espectro5=np.zeros(len(y5))
for c in k:
    miu5=float(c)
    sigma5= 0.425 * FWHM_Ge(miu5)
    nue_cuen5 = int(y5[c])
    if nue_cuen5>0:

        s=norm.rvs(loc=miu5,scale=sigma5, size= nue_cuen5,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro5[k]=espectro5[k]+hist[j]
########################################################################






################# 1.2 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y6))
espectro6=np.zeros(len(y6))
for c in k:
    miu6=float(c)
    sigma6= 0.425 * FWHM_Ge(miu6)
    nue_cuen6 = int(y6[c])
    if nue_cuen6>0:
        
        s=norm.rvs(loc=miu6,scale=sigma6, size= nue_cuen6,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro6[k]=espectro6[k]+hist[j]
########################################################################





################# 1.4 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y7))
espectro7=np.zeros(len(y7))
for c in k:
    miu7=float(c)
    sigma7= 0.425 * FWHM_Ge(miu7)
    nue_cuen7 = int(y7[c])
    if nue_cuen7>0:
        
        s=norm.rvs(loc=miu7,scale=sigma7, size= nue_cuen7,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro7[k]=espectro7[k]+hist[j]
########################################################################





################# 1.6 cm #######################


############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y8))
espectro8=np.zeros(len(y8))
for c in k:
    miu8=float(c)
    sigma8= 0.425 * FWHM_Ge(miu8)
    nue_cuen8 = int(y8[c])
    if nue_cuen8>0:

        s=norm.rvs(loc=miu8,scale=sigma8, size= nue_cuen8,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro8[k]=espectro8[k]+hist[j]
########################################################################





################# 1.8 cm #######################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y9))
espectro9=np.zeros(len(y9))
for c in k:
    miu9=float(c)
    sigma9= 0.425 * FWHM_Ge(miu9)
    nue_cuen9 = int(y9[c])
    if nue_cuen9>0:

        s=norm.rvs(loc=miu9,scale=sigma9, size= nue_cuen9,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro9[k]=espectro9[k]+hist[j]
########################################################################




################# 2.0 cm #######################

############### SE APLICA EL FWHM ####################
k=np.arange(10,len(y10))
espectro10=np.zeros(len(y10))
for c in k:
    miu10=float(c)
    sigma10= 0.425 * FWHM_Ge(miu10)
    nue_cuen10 = int(y10[c])
    if nue_cuen10>0:
        
        s=norm.rvs(loc=miu10,scale=sigma10, size= nue_cuen10,random_state=12345)
        smin=int(round(s.min()))-1
        smax=int(round(s.max()))+1
        binx=np.arange(smin, smax)
        hist, bin_edge=np.histogram(s,bins=binx)
        
        for j in np.arange(0,len(hist)):
            k=bin_edge[j]
            espectro10[k]=espectro10[k]+hist[j]
########################################################################

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::: Graficas despues de aplicar el filtro Gaussiano ::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

ax.plot(x1,espectro1,drawstyle='steps-mid',label='1 cm')
ax.plot(x2,espectro2,drawstyle='steps-mid',label='2 cm')
ax.plot(x3,espectro3,drawstyle='steps-mid',label='3 cm')
ax.plot(x4,espectro4,drawstyle='steps-mid',label='4 cm')
ax.plot(x5,espectro5,drawstyle='steps-mid',label='5 cm')
ax.plot(x6,espectro6,drawstyle='steps-mid',label='6 cm')
ax.plot(x7,espectro7,drawstyle='steps-mid',label='7 cm')
ax.plot(x8,espectro8,drawstyle='steps-mid',label='8 cm')
ax.plot(x9,espectro9,drawstyle='steps-mid',label='9 cm')
ax.plot(x10,espectro10,drawstyle='steps-mid',label='10 cm')

############################################################################################################
######################## EJES ##############################################################################
############################################################################################################

ax.set_xlabel(r'$E_\gamma$ (keV)', size=20)
#ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('cuentas/keV', size=20)
plt.xlim(0,300)
plt.ylim(0,2300)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
leg=plt.legend(loc="center left",prop={'size': 14})
for legobj in leg.legendHandles: #tamaño de la leyenda
    legobj.set_linewidth(5.0) #tamaño de la leyenda
plt.show()


#########################################################################
################# INICIO DE CONTEO  #####################################
#########################################################################

E1=197 #keV
E2= 262 #keV

############################################
############################################
ejex1=x1[E1:E2]
cuentas1=0
for i in range(len(ejex1)):
   cuentas1=cuentas1+espectro1[i]
    
print (cuentas1)
############################################
############################################

ejex2=x2[E1:E2]
cuentas2=0
for i in range(len(ejex2)):
   cuentas2=cuentas2+espectro2[i]
    
print (cuentas2)
############################################
############################################

ejex3=x3[E1:E2]
cuentas3=0
for i in range(len(ejex3)):
   cuentas3=cuentas3+espectro3[i]
    
print (cuentas3)
############################################
############################################


ejex4=x4[E1:E2]
cuentas4=0
for i in range(len(ejex4)):
   cuentas4=cuentas4+espectro4[i]
    
print (cuentas4)
############################################
############################################




ejex5=x5[E1:E2]
cuentas5=0
for i in range(len(ejex5)):
   cuentas5=cuentas5+espectro5[i]
    
print (cuentas5)
############################################
############################################






ejex6=x6[E1:E2]
cuentas6=0
for i in range(len(ejex6)):
   cuentas6=cuentas6+espectro6[i]
    
print (cuentas6)
############################################
############################################





ejex7=x7[E1:E2]
cuentas7=0
for i in range(len(ejex7)):
   cuentas7=cuentas7+espectro7[i]
    
print (cuentas7)
############################################
############################################

ejex8=x8[E1:E2]
cuentas8=0
for i in range(len(ejex8)):
   cuentas8=cuentas8+espectro8[i]
    
print (cuentas8)
############################################
############################################

ejex9=x9[E1:E2]
cuentas9=0
for i in range(len(ejex9)):
   cuentas9=cuentas9+espectro9[i]
    
print (cuentas9)
############################################
############################################


ejex10=x10[E1:E2]
cuentas10=0
for i in range(len(ejex10)):
   cuentas10=cuentas10+espectro10[i]
    
print (cuentas10)
############################################
############################################


#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#INTENSIDADES Y SUS ERRORES RESPECTIVOS

intensidades=[cuentas1, cuentas2, cuentas3, cuentas4, cuentas5, cuentas6, cuentas7, cuentas8, cuentas9, cuentas10]
int_max=max(intensidades)
intensidades=intensidades/int_max
errores_inten=[math.sqrt(cuentas1),math.sqrt(cuentas2),math.sqrt(cuentas3), math.sqrt(cuentas4), math.sqrt(cuentas5), math.sqrt(cuentas6), math.sqrt(cuentas7), math.sqrt(cuentas8), math.sqrt(cuentas9), math.sqrt(cuentas10)]

propaga_error_y=[cuentas1/int_max*math.sqrt((math.sqrt(cuentas1)/cuentas1)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)), cuentas2/int_max*math.sqrt((math.sqrt(cuentas2)/cuentas2)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)), cuentas3/int_max*math.sqrt((math.sqrt(cuentas3)/cuentas3)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)), cuentas4/int_max*math.sqrt((math.sqrt(cuentas4)/cuentas4)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)),cuentas5/int_max*math.sqrt((math.sqrt(cuentas5)/cuentas5)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)),cuentas6/int_max*math.sqrt((math.sqrt(cuentas6)/cuentas6)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)),cuentas7/int_max*math.sqrt((math.sqrt(cuentas7)/cuentas7)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)),cuentas8/int_max*math.sqrt((math.sqrt(cuentas8)/cuentas8)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)),cuentas9/int_max*math.sqrt((math.sqrt(cuentas9)/cuentas9)**2+math.sqrt((math.sqrt(int_max)/int_max)**2)),cuentas10/int_max*math.sqrt((math.sqrt(cuentas10)/cuentas10)**2+math.sqrt((math.sqrt(int_max)/int_max)**2))]

propaga_error_x=[0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005]


#GROSORES
grosor=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]


#REGRESION
print (propaga_error_y)


mu_T=-1.6
def intensidad(grosor,mu_T):
    return (1-np.exp(mu_T*grosor))


popt_retro,pcov_retro=curve_fit(intensidad, grosor, intensidades,p0=[mu_T],sigma=propaga_error_y)


perror=np.sqrt(np.diag(pcov_retro))
print ("error")
print (perror)
print ("-----------------")
print ("mu_T")
print (popt_retro)

mu_T=popt_retro

densidad=1.60
Ddensidad=0.06
mu_T_masico_sim=mu_T/densidad
error=mu_T_masico_sim*math.sqrt((perror/mu_T)**2+(Ddensidad/densidad)**2)
print (mu_T_masico_sim, error)


######################################################
mu_1=7.876E-02
mu_2=1.274E-01
mu_T_masico_nist=mu_1-(mu_2/math.cos(3*math.pi/4))
print (mu_T_masico_nist)
####################################################


fig2, axs=plt.subplots(1,1,sharey=False)
x=np.linspace(0.2,10.0,10000)
axs.errorbar(grosor,intensidades,yerr=propaga_error_y, xerr=propaga_error_x,fmt='.',color='purple', markersize=12,label='Geant4')

#axs.plot(grosor,intensidades,'o', label='Geant4',color='purple')

axs.set_xlabel(r'$t$ (cm)', size=20)
axs.set_ylabel('intensidad (cuentas)', size=20)
plt.text(8.0,0.3,r'Geant4: $\mu_T$=0.189(9)$\frac{cm^2}{g}$', size=15)
plt.text(8.0,0.2,r'NIST: $\mu_T$=0.258$\frac{cm^2}{g}$', size=15)
plt.text(8.0,0.1,r'Discrepancia: 26.7$\%$', size=15)
axs.plot(x,intensidad(x,mu_T), label='Ajuste ',color='red')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

leg=axs.legend(loc="center right",prop={'size': 14})
for legobj in leg.legendHandles: #tamaño de la leyenda
    legobj.set_linewidth(2.0) #tamaño de la leyenda
plt.show()
