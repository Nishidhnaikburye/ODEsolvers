# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:50:52 2024

@author: nishi
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

k = 1.0
m = 1.0
c = 0.5

F0 = 0.5      # Amplitude of the driving force (N)
omega = 1.5   # Angular frequency of the driving force (rad/s)

# Define the system of ODEs
def system(t, variables):
    x, v = variables
    dxdt = v
    dvdt = (-k/m) * x   - (c/m) * v 
    return [dxdt, dvdt]

# Initial conditions
x0 = 1.0   # Initial value of x displacement
v0 = 0.0   # Initial value of v velocity 
initial_conditions = [x0, v0]

# Time span
t_span = (0, 30)  # Solve from t=0 to t=5
t_eval = np.linspace(*t_span, 100)  # Time points to evaluate the solution

# Solve the system of ODEs
solution = solve_ivp(system, t_span, initial_conditions, t_eval=t_eval, method='RK45')

# Extract the solutions
t = solution.t
x = solution.y[0]  # First row corresponds to x(t)
v = solution.y[1]  # Second row corresponds to y(t)

# Plot the results
plt.figure(figsize=(10, 6))

# Plot x(t)
plt.plot(t, x, label="x(t)", color="blue", linewidth=2)

# Plot y(t)
plt.plot(t, v, label="v(t)", color="orange", linewidth=2)


U = 0.5 * k * x**2  # U = (1/2) * k * x^2

# plt.plot(t, U, label="u(t)", color="orange", linewidth=2)


plt.title("Solution of Coupled ODEs", fontsize=16)
plt.xlabel("Time (t)", fontsize=14)
plt.ylabel("Values of x(t) and y(t)", fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()
