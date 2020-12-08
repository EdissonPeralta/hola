#########
# para que "import metodos_MC" funcione debe incluir el directorio en el que está
# este archivo en el PATH de PYTHON. En mi computador:
# > export PYTHONPATH=$PYTHONPATH:/home/fernando/ng/materialesConstruccion
#

import numpy as np
from scipy.optimize import curve_fit

def cm2inch(cm):
    return cm/2.54

def recta(x,b0,b1,x0):
    return b0 + b1 * (x-x0)

def fitRecta(x,y,sgm,x0):
    b0 = (y[0]+y[-1])/2.
    b1 = (y[-1]-y[0])/(x[-1]-x[0])
    popt, pcov = curve_fit(lambda x, b0, b1 : recta(x,b0,b1,x0),x,y,sigma=sgm)
    return popt, pcov

def exponencial(x,I_0,mu):
    return I_0 * np.exp(-mu*x)

def fitExponencial(x,y,sigmay):
    I0 = y[0]
    mu = np.log(y[0]/y[-1])/x[-1]
    p0 = np.array([I0, mu])
    popt, pcov = curve_fit(exponencial,x,y,p0,sigma=sigmay)
    return popt, pcov

def gauss(x,mu,stdv,amp):
    z = (mu-x)/stdv
    return amp*np.exp(-0.5*z**2)

def gaussBckgrnd(x,mu,stdv,amp,b0,b1):
    z = (mu-x)/stdv
    gauss = amp*np.exp(-0.5*z**2)
    fondo = b0 + b1 * (x - mu)
    return gauss + fondo

def tandem(x,mu1,stdv1,amp1,mu2,stdv2,amp2,b0,b1):
    z1 = 0.5 * (mu1-x)/stdv1
    gauss1 = amp1*np.exp(-z1**2)
    z2 = 0.5 * (mu2-x)/stdv2
    gauss2 = amp2*np.exp(-z2**2)
    fondo = b0 + b1 * (x - mu1)
    return gauss1 + gauss2 + fondo

def fitGaussBckgrnd(x,y,ncrt):
    b0 = (y[0]+y[-1])/2.0
    b1 = (y[-1]-y[0])/(x[-1]-x[0])
    yb = y[0] + b1*(np.array(x)-x[0])
    diff = y-yb
    mean = diff.mean()
    if mean < 0:
        mu = x[np.argmin(np.array(diff))]
        M = min(y)-b0
    else:
        mu = x[np.argmax(np.array(diff))]
        M = max(y)-b0

    sgm = (x[-1] - x[0]) / 9.0
    p0 = np.array([mu,sgm,M,b0,b1])    
    popt, pcov = curve_fit(gaussBckgrnd,x,y,p0,sigma=ncrt)
    return popt, pcov

def fitGaussBckgrndSigma1(x,y):
    b0 = (y[0]+y[-1])/2
    b1 = (y[-1]-y[0])/(x[-1]-x[0])
    yb = y[0] + b1*(np.array(x)-x[0])
    diff = y-yb
    mean = diff.mean()
    if mean < 0:
        mu = x[np.argmin(np.array(y))]
        M = min(y)-b0
    else:
        mu = x[np.argmax(np.array(y))]
        M = max(y)-b0

    s = (x[-1] - x[0]) / 9
    p0 = np.array([mu,s,M,b0,b1])    
    popt, pcov = curve_fit(gaussBckgrnd,x,y,p0)
    return popt, pcov

def triplete(x,mu1,sigma1,amp1,mu2,sigma2,amp2,mu3,sigma3,amp3,b0,b1):
    z1 = 0.5*((x-mu1)/sigma1)**2
    z2 = 0.5*((x-mu2)/sigma2)**2
    z3 = 0.5*((x-mu3)/sigma3)**2
    g1 = amp1*np.exp(-z1)
    g2 = amp2*np.exp(-z2)
    g3 = amp3*np.exp(-z3)
    return  g1 + g2 + +g3 + b0 + b1*(x-mu2)
