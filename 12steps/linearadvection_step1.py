# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 06:43:48 2024

@author: nishi
"""

import numpy as np              #here we load numpy
from matplotlib import pyplot as plt      #here we load matplotlib
import time, sys   

nx = 41
nt = 25
dx = 2.0/(nx-1)
dt = 0.025
c = 1 

x = np.linspace(0, 2, nx)

u = np.zeros(nx)

for i in range(nx):
    if(x[i]>0.8 and x[i]<1.2):
        u[i] = 1.0
        
    
un = np.ones(nx) #initialize a temporary array

t = 0

endT = dt * nt
print(endT)

while(t<endT):
    
    un = u.copy()
    
    for i in range(0,nx):
        CFL = (c*dt/dx)
        u[i] = un[i] - CFL * (un[i] - un[i-1])
    plt.plot(u)
    
    t = t + dt


plt.show()
        
