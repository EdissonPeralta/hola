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

filenames=["1-TransmisionParafina60s.mtxt","2-TransmisionParafina60s.mtxt", "3-TransmisionParafina60s.mtxt", "4-TransmisionParafina60s.mtxt"]


h=[genfromtxt(f,comments='#',delimiter='   ',usecols=0,skip_header=10) for f in filenames]
