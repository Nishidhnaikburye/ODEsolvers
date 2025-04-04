# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 07:39:01 2024

@author: nishi
"""

# Adding inline command to make plots appear under comments
import numpy as np
import matplotlib.pyplot as plt
import time, sys

#Same initial conditions as in step 1 with courant number and viscosity added
grid_length = 2
grid_points = 41
dx = grid_length / (grid_points - 1) 
nt = 500
nu = 0.3 # viscosity of the system
sig= 0.2 #courant number
dt = sig * dx**2 / nu #Dynamically scaling dt based on grid size to ensure convergence

#Initiallizing the shape of the wave to the same one from step 1 and displaying it
u = np.ones(grid_points)
u[int(.5/ dx):int(1 / dx + 1)] = 2
plt.plot(np.linspace(0,grid_length,grid_points), u);
plt.ylim(1,2);
plt.xlabel('x')
plt.ylabel('u')
plt.title('1D Diffusion t=0')

un = np.ones(grid_points)

for n in range(nt): #Runs however many timesteps you set earlier
    un = u.copy()   #copy the u array to not overwrite values
    for i in range(1,grid_points-1):
        u[i] = un[i] + nu * (dt/dx**2) * (un[i+1]- 2*un[i] + un[i-1]) 
    if n % 10 == 0:
        plt.plot(np.linspace(0,grid_length,grid_points), u)
    
    
plt.xlabel('x')
plt.ylabel('u')
plt.title('1D Diffusion t=10')
plt.show()