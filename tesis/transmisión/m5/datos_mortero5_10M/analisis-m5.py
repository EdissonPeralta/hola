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

filenames=["gMC_h0_Ge.csv", "gMC_h1_Ge.csv","gMC_h2_Ge.csv","gMC_h3_Ge.csv","gMC_h4_Ge.csv","gMC_h4_Ge.csv","gMC_h5_Ge.csv","gMC_h6_Ge.csv","gMC_h7_Ge.csv","gMC_h8_Ge.csv","gMC_h9_Ge.csv","gMC_h10_Ge.csv"]


h=[genfromtxt(f,comments='#',delimiter=',',usecols=0,skip_header=9) for f in filenames]
#creando un canalero para graficar
x=np.linspace(h[0][0],len(h[0])-1,len(h[0]))
y=x #esto es para graficar al final ya que x se pierde en el camino


#número de picos
pic=8

#numero de espectros
num=11

#grosor de las placas usadas
grosor=[0.0 ,1.0 ,2.0 ,3.0 ,4.0 ,5.0 ,6.0 ,7.0 ,8.0 ,9.0 ,10.0]
#energía de loss picos s analizar
energy=[81,122,356,511,662,1173,1273,1332]

#:::::::::::::::::::::finltro gaussiano:::::::::::::::::::::::::::::..
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def FWHM_Ge(Eg):
    f0 = 1.24
    f1 = 0.00068
    return f0 + f1 * Eg # Eg(keV)

def FWHM_NaI(Eg):
    f0 = 1.0
    f1 = 0.027
    f2 = 1.2
    return f0 + f1 * Eg  + f2 * np.sqrt(Eg) # Eg(keV)

espectro1 = np.zeros((len(h),len(h[0]))) # histograma del espectro con FWHM Ge

x = np.arange(0,len(h[0]))
for j in range(len(h)):
    for c in x:
        Eg = float(c)
        sigma= 0.425 * FWHM_Ge(Eg)
        N = int(h[j][c])
        if N > 0:
            s = norm.rvs(loc=Eg,scale=sigma,size=N,random_state=12345)
            s_min = int(round(s.min())) - 1
            s_max = int(round(s.max())) + 1
            binx = np.arange(s_min, s_max)
            hist, bin_edges = np.histogram(s,bins=binx)
        
            for i in np.arange(0,len(hist)):
                k = bin_edges[i]
                espectro1[j][k] = espectro1[j][k] + hist[i]
h=espectro1




#limito mis canales para el ajuste gaussiano en términos de energía
xdown=[]
xup=[]
for i in range(len(energy)):
    xdown.extend([energy[i]-6])
    xup.extend([energy[i]+6])
xdown=np.array(xdown, dtype=int)
xup=np.array(xup, dtype=int)
size=(xup-xdown)
mode=stats.mode(size)
size=mode[0][0]
#debido a que no siempre van a ser del mismo tamaño, lo corrijo
for i in range(len(xdown)):
    if xup[i]-xdown[i]!=mode[0][0]:
        xup[i]+=1

        
#creo los arreaglos en cero para meter el hitorama alrededor del pico interés
xs=np.zeros((num,pic,size))
ys=np.zeros((num,pic,size))
#arreglos alrededor de los picos de interés

for i in range(len(xs)):
    for j in range(len(xs[0])):
        xs[i][j]=x[int(xdown[j]):int(xup[j])]
        ys[i][j]=h[i][int(xdown[j]):int(xup[j])]

#arreglos para ubicar los picos 
peaksy=np.zeros((num,pic))
peaksx=np.zeros((num,pic))


#encunetor los picos
for i in range(len(xs)): #recorro sobre todas las graficas
    for j in range(len(xs[0])): #recorro sobre todos los picos de interés
        peaks, _ = find_peaks(ys[i][j], height=250,width=1, prominence=100)
        print(peaks)
        if len(peaks)>1:#porque a vesces el pico no es claro
            peaksy[i][j]=ys[i][j][peaks[len(peaks)-1]] #ubico el valor real de l
            peaksx[i][j]=xs[i][j][peaks[len(peaks)-1]] #ubico el valor real de x
        peaksy[i][j]=ys[i][j][peaks[0]] #ubico el valor real de los conteos
        peaksx[i][j]=xs[i][j][peaks[0]] #ubico el valor real de x


#inicializo las varaibales a ajusta
amp=np.zeros((num,pic))
damp=np.zeros((num,pic))
cen=np.zeros((num,pic))
dcen=np.zeros((num,pic))
sigma=np.zeros((num,pic))
dsigma=np.zeros((num,pic))
a0=np.zeros((num,pic))
a1=np.zeros((num,pic))

#hago una apuesta incial a los valores que espero
for i in range(len(xs)):
    for j in range(len(xs[0])):
        amp[i][j]=peaksy[i][j] #inicio la amplictud 
        cen[i][j]=peaksx[i][j] #incicio el valor del centro
        sigma[i][j]=2 #la inicio en dos por constumbre, devería ser poisson pero quedaría muy muy grande

#defino la gaussiana a ajustar, con una linea
def _gaussian(x, amp,cen,sigma):
    return amp*(np.exp(-((x-cen)**2)/(2*(sigma)**2)))
def _1gaussian(x, amp,cen,sigma,a0,a1):
    return amp*(np.exp(-((x-cen)**2)/(2*(sigma)**2)))+a0+a1*(x-cen)

popt_gauss= np.zeros((num,pic,5))
pcov_gauss=np.zeros((num,pic,5,5))

#ajustes
for i in range(len(xs)):
    for j in range(len(xs[0])):
        popt_gauss[i][j], pcov_gauss[i][j] = curve_fit(_1gaussian, xs[i][j], ys[i][j], p0=[amp[i][j], cen[i][j], 1.5,a0[i][j],a1[i][j]])

#Una vez hecho el ajuste, le doy los valores

for i in range(len(xs)):
    for j in range(len(xs[0])):
        amp[i][j]=popt_gauss[i][j][0]
        damp[i][j]=np.sqrt(pcov_gauss[i][j][0][0])
        cen[i][j]=popt_gauss[i][j][1]
        dcen[i][j]=np.sqrt(pcov_gauss[i][j][1][1])
        sigma[i][j]=popt_gauss[i][j][2]
        dsigma[i][j]=np.sqrt(pcov_gauss[i][j][2][2])
        a0[i][j]=popt_gauss[i][j][3]
        a1[i][j]=popt_gauss[i][j][4]


#:::::::::::Coeficiente de atenuacion::::::::Coeficiente de atenuación:::::::::
#:::::::::::Coeficiente de atenuacion::::::::Coeficiente de atenuación:::::::::

I=np.zeros((num,pic))
dI=np.zeros((num,pic))
for i in range(len(xs)):
    for j in range(len(xs[0])):
        I[i][j]=np.sqrt(2*np.pi)*sigma[i][j]*amp[i][j]
        dI[i][j]=I[i][j]*np.sqrt(np.square(damp[i][j]/amp[i][j])+np.square(dsigma[i][j]/sigma[i][j]))
        
       
#lo que hago al tranponer es que I[0] sean todas inensidades del pico 0  
I=I.transpose()
dI=dI.transpose()
#print(dI)
#print(I[1])
#arrays para guaradr los resultados de los ajustes
I0=np.zeros(pic)
dI0=np.zeros(pic)
mu=np.zeros(pic)
dmu=np.zeros(pic)
popt_exp= np.zeros((pic,2))
pcov_exp=np.zeros((num,2,2))

#la funciona exponencial a ajustar 
def _exp(x, I0,mu):
    return I0*np.exp(-mu*x) #exp a ajustar

#el ajuste para enocntrar el coeficiente de absorción
for i in range(len(xs[0])):
    popt_exp[i], pcov_exp[i] = curve_fit(_exp, grosor, I[i], p0=[I0[i], mu[i]],sigma=dI[i])
    I0[i]=popt_exp[i][0]
    dI0[i]=np.sqrt(pcov_exp[i][0][0])
    mu[i]=popt_exp[i][1]
    dmu[i]=np.sqrt(pcov_exp[i][1][1])

#print(mu[1])


    
density=1.602 #g/cm3 computing in a external excel
ddensity=0.016 #g/cm3 DEBO CALCULARLA BIEN !!!!

muu=mu/density 
dmu=muu*np.sqrt((dmu/mu)*(dmu/mu)+(ddensity/density)*(ddensity/density))
mu=muu
#print('coeficiente de abosrcion másicos g/cm3 experimentales')
#print(energy)
#print(mu)#in the second position because is there where the 662 keV is
#print(dmu)

#ahora pongo los valores que me da el nist y hago ajustes a una funcion potencia
munist=[2.437E-01, 1.664E-01, 1.024E-01, 8.819E-02, 7.876E-02, 6.000E-02, 5.756E-02, 5.625E-02]

#ahora pongo los valores experimentales
muexp=[0.18867332, 0.14790356, 0.09812104, 0.08385468,0.07720204, 0.06038583, 0.05390741, 0.05053051] #falta cambiarlo !!!!
dmuexp=[0.00709664, 0.00321366, 0.0050095,  0.00236088, 0.00270814, 0.0035002, 0.00150228, 0.00614035] #falta cambiarlo !!!!




def myExpFunc(x, a, b):
    return a * np.power(x, b)

popt, pcov = curve_fit(myExpFunc, energy, mu,sigma=dmu)
pop_exp, pcov_exp = curve_fit(myExpFunc, energy, munist,sigma=None)
alph_exp=popt[0]
dalph_exp=np.sqrt(pcov[0][0])
alph2_exp=popt[1]
dalph2_exp=np.sqrt(pcov[1][1])
alph_nist=pop_exp[0]
dalph_nist=np.sqrt(pcov_exp[0][0])
alph2_nist=pop_exp[1]
dalph2_nist=np.sqrt(pcov_exp[1][1])

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::GRAFICAS:::::GRAFICAS:::::GRAFICAS:::::GRAFICAS:::::GRAFICAS:::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::GRAFICAS:::::GRAFICAS:::::GRAFICAS:::::GRAFICAS:::::GRAFICAS:::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""
#espectro completo
fig_1,axs=plt.subplots(1,1,figsize=(6.5,4))
axs.set_ylabel(r'Cuentas')
axs.set_xlabel(r'$E_{\gamma}$ keV')
axs.step(x,h[0],where='mid')
#for i in range(num):
#    axs.step(y,h[i],where='mid')
for i in range(pic):
    if i==pic-1:
        axs.text(peaksx[0][i],peaksy[0][i],str(energy[i])+' keV', fontsize=11,ha='left')
    else:
        axs.text(peaksx[0][i],peaksy[0][i],str(energy[i])+' keV', fontsize=11,ha='center')
        
#fig_1.savefig('1.pdf')
"""
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""
#grafico algun picos
fig_1,axs=plt.subplots(2,2,figsize=(6.5,4))
ii,jj=0,0
for j in range(0,8,2):
    pico=j
    for i in range(len(xs)):
        axs[ii][jj].step(xs[i][pico],ys[i][pico],where='mid')
    axs[ii][jj].set_ylabel(r'Cuentas')
    axs[ii][jj].set_xlabel(r'Canales')
    if jj==1 and ii==1:
        jj=0
        ii=1
    elif jj==1 and ii==0:
        ii+=1
    elif jj==0 and ii==0:
        jj+=1
#fig_1.tight_layout()
#fig_1.savefig('2.pdf')
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""
#grafico los ajuste a la funcion potencia
xx=x[50:]
fig_1,axs=plt.subplots(1,1,figsize=(6,3.5))

axs.set_ylabel(r"$\mu$ (cm$^2$/g)")
axs.set_xlabel(r'$E_{\gamma}$ (keV)')

#plt.tick_params(
#    axis='y',          # changes apply to the y-axis
#    which='both',      # both major and minor ticks are affected
#    labelsize=12) 
axs.set_ylim(4*10**(-2), 3*10**(-1))
axs.loglog()
axs.yaxis.set_major_locator(ticker.AutoLocator())
axs.yaxis.set_minor_locator(ticker.AutoMinorLocator())
axs.yaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
axs.set_xlim(7*10**1, 1.5*10**(3))
axs.set_xticks([8*10**1, 2*10**2, 5*10**2, 1*10**3, 1.5*10**3])
axs.set_xticklabels(['80','200','500','1000','1500'])


#SIMULACION

print (np.round(alph_exp,2))


print (np.round(dalph_exp,2))

print (np.round(alph2_exp,2))
print (np.round(dalph2_exp,2))
#######################################

 #NIST

print (np.round(alph_nist,2))

print (np.round(dalph_nist,2))
print (np.round(alph2_nist,2))

print (np.round(dalph2_nist,2))


#los labels para que queden como una ecuación 

#grafico
plt.title("Morteros 5")
axs.plot(xx, myExpFunc(xx, *popt), 'C0', color='red')

axs.errorbar(energy, mu, yerr=dmu, fmt='o', c='red',ecolor='k',label=r"Simulación")

axs.plot(xx, myExpFunc(xx, *pop_exp), 'purple')

axs.errorbar(energy,munist,yerr=None, fmt='o',c='purple',ecolor='k',label=r'NIST')
axs.legend()
plt.tick_params(labelright=True, right=True)
#plt.xticks(fontsize=20)
#plt.yticks(fontsize=20)
leg=plt.legend(loc="upper right")#,prop={'size': 20})
#for legobj in leg.legendHandles: #tamaño de la leyenda
#    legobj.set_linewidth(2.5) #tamaño de la leyenda

fig_1.tight_layout()
plt.show()


"""

pico_graf=2
fig_2,axs=plt.subplots(1,1)
axs.set_ylabel(r'Cuentas')
axs.set_xlabel(r'$E_{\gamma}$ keV')
for i in range(len(cen)):
    axs.step(xs[i][pico_graf],ys[i][pico_graf],where='mid')
    axs.plot(y[int(xbot[pico_graf]):int(xtop[pico_graf])],_1gaussian(y[int(xbot[pico_graf]):int(xtop[pico_graf])],amp[i][pico_graf],cen[i][pico_graf],sigma[i][pico_graf],a0[i][pico_graf],a1[i][pico_graf]),c='k')
fig_2.savefig('2.pdf')


"""
