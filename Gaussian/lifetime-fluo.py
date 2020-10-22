#!python3
# -*- coding: utf-8 -*-
""""
This program allows one to simulate the fluorescence 
rate constant and lifetime after a TD-DFT computation

The whole equation of k_r is : 

k_r = (4/3)((\Delta E_{1-0})/c)^3(|µ_{1-0}|^2)

\Delta E_{1-0} is the energy difference between GS and ES
taken from electronic vertical emission (TD-DFT).


|µ_{1-0}|^2 is given in the Gaussian output
below the line :

<<<Ground to excited state transition electric dipole moments (Au):>>>
You need to look for the root of interest together with the column Dip. S.
It's already in a.u, therefore everything gonna be computed in a.u.


(see Rega et al, JPCA, 2012, 116, 7491 and Halet et al, ChemPhotoChem, 2020, 4, 173) 
"""


# #####   variables to be entered by user
#
#vertical emission wavelength = vem
#dipS = |µ_{1-0}|^2
vem = 432 #nm
dipS = 0.4572 # a.u.
#
# #### end of variables entered by user


# constant data 
c = 137.04 #a.u.
t = 2.42*10**(-17)

# unit conversion of vem
DeltaEeV = 1240/vem
DeltaE_10_au = DeltaEeV/27.21

#computation of k_r
k_r_au = (4/3)*((DeltaE_10_au/c)**3)*dipS
print("The rate constant k_r is computed =",format(k_r_au,"10.4E"),"a.u.") #scientific format
k_r_sec = k_r_au/t
print("The rate constant k_r is computed =",format(k_r_sec,"10.4E"),"s-1") #scientific format

#computation of lifetime
tau = 1/k_r_sec
print("The fluorescence lifetime is computed =",format(tau,"10.4E"),"s") #scientific format
