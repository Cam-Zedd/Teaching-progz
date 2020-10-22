#!python3
# -*- coding: utf-8 -*-
### import
import matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os
import sys

##################################### file read #################################

#declare
energy=list()
IR=list()
RAMAN=list()
### read the file and store the data
for line in open(sys.argv[1], "r"): #open file, read, for line sys.argv[1] is my argument
	if "Frequencies ---" in line: #stack the energy
		for freq in line.split()[2:]: #loop over all values of splited 
			energy.append(float(freq))
	if "IR Intensities ---" in line: #stack the intensities
		for intensities in line.split()[3:]:
			IR.append(float(intensities))
	if "Raman Activities ---" in line: #stack the intensities
		for inten in line.split()[3:]:
			RAMAN.append(float(inten))
print(energy) #print all the required data on prompt for user

#Cam's layout
SMALL_SIZE = 24
BIGGER_SIZE = 32
plt.rcParams.update({'font.size': SMALL_SIZE,
					 'axes.titlesize':BIGGER_SIZE, 'axes.edgecolor':'black','axes.labelsize':BIGGER_SIZE, 'axes.linewidth':2,
					 'xtick.labelsize':SMALL_SIZE, 'xtick.major.size':10, 'xtick.major.width':2, 'lines.markersize':10,'patch.linewidth':3.0,
					 'ytick.labelsize':SMALL_SIZE, 'ytick.major.size':10, 'ytick.major.width':2, 'ytick.minor.size':6, 'ytick.minor.width':1})


#######plot in cm-1
#### IF RAMAN and IR COMPUTATION
if len(IR)==len(RAMAN):
	fig1, ax = plt.subplots()
#spectrum=spec(excplot[0],excplot[2],sigma,x)
#ax.plot(x,spectrum,"--k")
	ax.vlines(energy[:], 0, IR[:], label='IR', color='r', lw=2, linestyles='solid')
	ax.vlines(energy[:], 0, RAMAN[:], label='RAMAN', color='b', lw=2, linestyles='solid')
	ax.set_xlabel(r"$\bar{\nu}$ (cm$^{-1})$")
	ax.set_ylabel(r"Relative Intensity")
	fig2, ax = plt.subplots()
	ax.vlines(energy[:], 0, RAMAN[:], label='RAMAN', color='b', lw=2, linestyles='solid')
	ax.set_xlabel(r"$\bar{\nu}$ (cm$^{-1})$")
	ax.set_ylabel(r"Relative Intensity")
	fig3, ax = plt.subplots()
	ax.vlines(energy[:], 0, IR[:], label='IR', color='r', lw=2, linestyles='solid')
	ax.set_xlabel(r"$\bar{\nu}$ (cm$^{-1})$")
	ax.set_ylabel(r"Relative Intensity")
#IF ONLY IR
else:
	fig4, ax2 = plt.subplots()
	ax2.vlines(energy[:], 0, IR[:], label='IR', color='r', lw=2, linestyles='solid')
	ax2.set_xlabel(r"$\bar{\nu}$ (cm$^{-1})$")
	ax2.set_ylabel(r"Relative Intensity")
#ax.set_xlim(e/1.1,maxeV*1.1)
#ax.set_ylim(0,max(spectrum)*1.1)
plt.legend(loc='upper left', frameon=False)

plt.show()

	
### change to an nparray and  transpose for plotting
# excitation=np.array(excitation) #prepare for plot and transpose
# excplot=excitation.transpose() #new variable for plotting

'''
### Gaussian function

Adapted from Michael Dommett code

def spec(E,f,sigma,x):
    spectrum=[]
    for E1 in x:
        tot=0
        for E2,os in zip(E,f):
            tot+=os*np.exp(-((((E2-E1)/sigma)**2)))
        spectrum.append(tot)
    return spectrum #prepare spectrum for the values to be plotted

### set up the min and max value for x plot
mineV=np.amin(excplot[0])
maxeV=np.amax(excplot[0])
minnm=np.amin(excplot[1])
maxnm=np.amax(excplot[1])

### x and sigma	change sigma for HWHM
x=np.linspace(mineV/1.1,maxeV*1.1,num=2000)
sigma=0.1

### plot
#Cam's layout
SMALL_SIZE = 18
BIGGER_SIZE = 22
plt.rcParams.update({'font.size': SMALL_SIZE,
					 'axes.titlesize':BIGGER_SIZE, 'axes.edgecolor':'black','axes.labelsize':BIGGER_SIZE, 'axes.linewidth':2,
					 'xtick.labelsize':SMALL_SIZE, 'xtick.major.size':10, 'xtick.major.width':2, 'lines.markersize':10,'patch.linewidth':3.0,
					 'ytick.labelsize':SMALL_SIZE, 'ytick.major.size':10, 'ytick.major.width':2, 'ytick.minor.size':6, 'ytick.minor.width':1})


#######plot in eV
fig1, ax = plt.subplots()
spectrum=spec(excplot[0],excplot[2],sigma,x)
ax.plot(x,spectrum,"--k")
ax.vlines(excplot[0], 0, excplot[2], label='TD-DFT oscillator strengths', color='r', lw=2, linestyles='solid')
ax.set_xlim(mineV/1.1,maxeV*1.1)
ax.set_ylim(0,max(spectrum)*1.1)
ax.legend(loc='upper left', frameon=False)
ax.set_xlabel(r"Energy (eV)")
ax.set_ylabel(r"f (oscillator strength)")


#######plot in nm
fig2,ax2 = plt.subplots()
ax2.vlines(excplot[1], 0, excplot[2], label='TD-DFT oscillator strengths', color='b', lw=2, linestyles='solid')
ax2.plot(1240/x,spectrum,"--k")
ax2.set_xlim(minnm/1.1,maxnm*1.1)
ax2.set_ylim(0,max(spectrum)*1.1)
ax2.legend(loc='upper left', frameon=False)
ax2.set_xlabel(r" $\lambda$ (nm)")
ax2.set_ylabel(r"f (oscillator strength)")
'''



